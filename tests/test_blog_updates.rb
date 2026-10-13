# frozen_string_literal: true

require "fileutils"
require "jekyll"
require "minitest/autorun"
require "rexml/document"
require "tmpdir"
require "yaml"

class BlogUpdatesTest < Minitest::Test
  ROOT = File.expand_path("..", __dir__)
  POSTS = [
    ["newsletter", ["newsletter"]],
    ["article", ["interview"]],
    ["both-tags", ["news", "newsletter"]],
    ["announcement", ["news"]],
    ["story", ["spotlight"]],
    ["tutorial", []],
    ["older-news", ["news"]],
    ["older-article", []]
  ].freeze

  def render(posts = POSTS)
    Dir.mktmpdir("defold-blog-updates-test") do |directory|
      source = File.join(directory, "source")
      destination = File.join(directory, "site")
      %w[_includes _layouts _posts].each { |name| FileUtils.mkdir_p(File.join(source, name)) }
      %w[news_and_blog_section.html post_preview_excerpt.html secondary_button.html].each do |name|
        FileUtils.cp(File.join(ROOT, "_includes", name), File.join(source, "_includes", name))
      end
      FileUtils.cp(File.join(ROOT, "_layouts", "redirect.html"), File.join(source, "_layouts"))
      FileUtils.cp(File.join(ROOT, "news.md"), source)
      File.write(File.join(source, "index.html"), "---\n---\n{% include news_and_blog_section.html split_news=true %}")
      File.write(File.join(source, "press.html"), "---\n---\n{% include news_and_blog_section.html %}")
      posts.each_with_index do |(slug, tags), index|
        metadata = { "title" => slug, "tags" => tags }
        File.write(File.join(source, "_posts", "2026-10-#{30 - index}-#{slug}.md"),
                   "#{metadata.to_yaml}---\nExcerpt for #{slug}.\n")
      end
      site = Jekyll::Site.new(Jekyll.configuration(
        "source" => source, "destination" => destination, "url" => "https://www.defold.com",
        "future" => true, "quiet" => true, "plugins" => [], "permalink" => "/:title/"
      ))
      site.process
      yield destination
    end
  end

  def cards(node)
    REXML::XPath.match(node, ".//a[contains(@class, 'page-post-panel-link')]").map { |link| link.attributes["href"] }
  end

  def test_homepage_orders_and_separates_newsletters_news_and_articles_without_duplicates
    render do |destination|
      document = REXML::Document.new(File.read(File.join(destination, "index.html")))
      groups = REXML::XPath.match(document, "//div[@class='page-card-group']")
      assert_equal 2, groups.size
      assert_equal ["/article/", "/story/", "/tutorial/"], cards(groups[0])
      assert_equal ["/newsletter/", "/both-tags/", "/announcement/"], cards(groups[1])
      links = REXML::XPath.match(document, "//a[@class='button secondary']")
      assert_equal ["/blog", "/blog"], links.map { |link| link.attributes["href"] }
    end
  end

  def test_fewer_than_three_posts_does_not_repeat_or_fill_from_the_other_group
    render(POSTS.first(2)) do |destination|
      document = REXML::Document.new(File.read(File.join(destination, "index.html")))
      groups = REXML::XPath.match(document, "//div[@class='page-card-group']")
      assert_equal ["/article/"], cards(groups[0])
      assert_equal ["/newsletter/"], cards(groups[1])
    end
  end

  def test_other_pages_show_six_newest_posts_in_one_group
    render do |destination|
      document = REXML::Document.new(File.read(File.join(destination, "press", "index.html")))
      assert_equal 1, REXML::XPath.match(document, "//div[@class='page-card-group']").size
      assert_equal ["/newsletter/", "/article/", "/both-tags/", "/announcement/", "/story/", "/tutorial/"], cards(document)
    end
  end

  def test_old_news_listing_redirects_to_the_complete_blog
    render do |destination|
      html = File.read(File.join(destination, "news", "index.html"))
      assert_includes html, 'new URL("/blog/", window.location.origin)'
      assert_includes html, 'content="0; url=/blog/"'
      assert_includes html, 'content="noindex, follow"'
      assert_includes html, 'href="https://www.defold.com/blog/"'
      assert_includes html, "This page has moved"
    end
  end
end
