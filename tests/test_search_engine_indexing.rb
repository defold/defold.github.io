# frozen_string_literal: true

require "fileutils"
require "jekyll"
require "minitest/autorun"
require "rexml/document"
require "time"
require "tmpdir"
require "yaml"

class SearchEngineIndexingTest < Minitest::Test
  ROOT = File.expand_path("..", __dir__)
  ORIGIN = "https://www.defold.com"

  def self.output
    @output ||= Dir.mktmpdir("defold-search-engine-test") do |directory|
      source = File.join(directory, "source")
      destination = File.join(directory, "site")
      FileUtils.mkdir_p(File.join(source, "_includes"))
      FileUtils.mkdir_p(File.join(source, "_layouts"))
      FileUtils.mkdir_p(File.join(source, "_data"))
      File.write(File.join(source, "_data", "engine_versions.yml"),
                 { "stable" => "1.13.1", "beta" => "1.13.2", "alpha" => "1.14.0" }.to_yaml)

      %w[head.html search_engine_metadata.html googleanalytics.html googletagmanager_head.html].each do |name|
        FileUtils.cp(File.join(ROOT, "_includes", name), File.join(source, "_includes", name))
      end
      %w[api page post].each do |layout|
        File.write(File.join(source, "_layouts", "#{layout}.html"),
                   '<html><head>{% include head.html %}</head><body>{{ content }}</body></html>')
      end
      %w[redirect assetportal_redirect].each do |layout|
        FileUtils.cp(File.join(ROOT, "_layouts", "#{layout}.html"),
                     File.join(source, "_layouts", "#{layout}.html"))
      end
      FileUtils.cp(File.join(ROOT, "sitemap.xml"), source)
      FileUtils.cp(File.join(ROOT, "robots.txt"), source)

      api = { "layout" => "api", "ref" => "b2d-lua", "type" => "Defold Lua" }
      %w[stable beta alpha].each do |branch|
        prefix = branch == "stable" ? "ref" : "ref/#{branch}"
        write_page(source, "#{prefix}/b2d-lua.md", api.merge("branch" => branch))
        # Alias detection must work without Pagefind's exclusion flag.
        write_page(source, "#{prefix}/b2d.md", api.merge("branch" => branch))
        write_page(source, "#{prefix}/overview_defoldlua.md",
                   api.merge("branch" => branch, "ref" => "overview"))
      end
      write_page(source, "ref/beta/bullet3d-lua.md",
                 api.merge("branch" => "beta", "ref" => "bullet3d-lua"))
      write_page(source, "extension-iap/iap_api.html",
                 api.merge("branch" => "stable", "type" => "Extension", "ref" => "extension-iap_iap"))
      write_page(source, "ref/stable/b2d-lua.md",
                 "layout" => "redirect", "redirect_to" => "/ref/b2d-lua/")
      write_page(source, "assets_stars.html", "layout" => "assetportal_redirect")
      write_page(source, "pagefind-only.html", "pagefind_exclude" => true)
      write_page(source, "google-only.html", "noindex" => true)
      write_page(source, "sitemap-only.html", "sitemap" => false)
      write_page(source, "duplicate.html", "canonical" => "/pagefind-only/")
      write_page(source, "updated.html", "last_modified_at" => "2026-09-10T12:30:00Z")
      write_page(source, "undated.html")
      write_page(source, "unpublished.html", "published" => false)
      write_page(source, "_posts/2026-01-02-release.md", "layout" => "post")
      write_page(source, "_posts/2026-01-03-hidden.md", "layout" => "post", "noindex" => true)
      write_page(source, "style.css", "layout" => nil)
      write_page(source, "feed.xml", "layout" => nil)

      Jekyll::Site.new(Jekyll.configuration(
        "source" => source,
        "destination" => destination,
        "cache_dir" => File.join(directory, "cache"),
        "url" => ORIGIN,
        "name" => "Defold",
        "permalink" => "pretty",
        "future" => true,
        "unpublished" => true,
        "quiet" => true
      )).process

      Dir.glob(File.join(destination, "**", "*"))
         .select { |path| File.file?(path) }
         .to_h { |path| [path.delete_prefix(destination), File.read(path)] }
    end
  end

  def self.write_page(source, path, data = {})
    target = File.join(source, path)
    FileUtils.mkdir_p(File.dirname(target))
    File.write(target, { "layout" => "page", "title" => "Documentation" }.merge(data).to_yaml +
                       "---\nDocumentation content.\n")
  end

  def html(path)
    self.class.output.fetch("#{path}index.html")
  end

  def sitemap
    REXML::Document.new(self.class.output.fetch("/sitemap.xml"))
  end

  def sitemap_urls
    sitemap.get_elements("urlset/url/loc").map(&:text)
  end

  def assert_indexing(path, indexable:, canonical: path)
    content = html(path)
    robots = content.scan(/<meta name="robots" content="([^"]+)"/).flatten
    assert_equal 1, robots.length, path
    assert_equal !indexable, robots.first.split(/,\s*/).include?("noindex"), path
    assert_includes content, %(<link rel="canonical" href="#{ORIGIN}#{canonical}">)
    assert_equal indexable, sitemap_urls.include?(ORIGIN + path), path
  end

  def test_stable_and_extension_references_are_indexable
    assert_indexing "/ref/b2d-lua/", indexable: true
    assert_indexing "/ref/overview_defoldlua/", indexable: true
    assert_indexing "/extension-iap/iap_api/", indexable: true
  end

  def test_preview_references_and_overviews_are_indexable_with_their_own_canonicals
    %w[beta alpha].each do |branch|
      assert_indexing "/ref/#{branch}/b2d-lua/", indexable: true
      assert_indexing "/ref/#{branch}/overview_defoldlua/", indexable: true
    end
    assert_indexing "/ref/beta/bullet3d-lua/", indexable: true
    assert_equal "", self.class.output.fetch("/robots.txt")[/^Disallow:(.*)$/, 1].strip
  end

  def test_engine_api_titles_identify_the_channel_and_version
    {
      "/ref/b2d-lua/" => "1.13.1 (Stable)",
      "/ref/beta/b2d-lua/" => "1.13.2 (Beta)",
      "/ref/alpha/b2d-lua/" => "1.14.0 (Alpha)",
      "/ref/beta/bullet3d-lua/" => "1.13.2 (Beta)",
      "/ref/alpha/overview_defoldlua/" => "1.14.0 (Alpha)"
    }.each do |path, version|
      assert_includes html(path), "<title>Documentation | Defold #{version}</title>"
    end
    assert_includes html("/extension-iap/iap_api/"), "<title>Documentation | Defold</title>"
    assert_includes html("/pagefind-only/"), "<title>Documentation | Defold</title>"
  end

  def test_aliases_and_redirects_remain_excluded
    ["/ref/", "/ref/beta/", "/ref/alpha/"].each do |prefix|
      assert_indexing "#{prefix}b2d/", indexable: false, canonical: "#{prefix}b2d-lua/"
    end
    assert_indexing "/ref/stable/b2d-lua/", indexable: false, canonical: "/ref/b2d-lua/"
    assert_indexing "/assets_stars/", indexable: false, canonical: "/assets/"
  end

  def test_google_and_pagefind_exclusions_are_independent
    assert_indexing "/pagefind-only/", indexable: true
    assert_indexing "/google-only/", indexable: false
    refute_includes sitemap_urls, ORIGIN + "/sitemap-only/"
    refute_includes html("/sitemap-only/"), 'content="noindex'
    refute_includes sitemap_urls, ORIGIN + "/duplicate/"
    assert_includes html("/duplicate/"), %(<link rel="canonical" href="#{ORIGIN}/pagefind-only/">)
  end

  def test_sitemap_contains_only_canonical_published_html_pages
    expected = %w[
      /ref/b2d-lua/ /ref/overview_defoldlua/ /extension-iap/iap_api/
      /ref/beta/b2d-lua/ /ref/beta/overview_defoldlua/ /ref/beta/bullet3d-lua/
      /ref/alpha/b2d-lua/ /ref/alpha/overview_defoldlua/
      /pagefind-only/ /updated/ /undated/ /2026/01/02/release/
    ].map { |path| ORIGIN + path }
    assert_equal expected.sort, sitemap_urls.sort
  end

  def test_lastmod_uses_only_explicit_content_update_dates
    dates = sitemap.get_elements("urlset/url").filter_map do |entry|
      if entry.elements["lastmod"]
        [entry.elements["loc"].text, Time.iso8601(entry.elements["lastmod"].text).utc.iso8601]
      end
    end
    assert_equal [[ORIGIN + "/updated/", "2026-09-10T12:30:00Z"]], dates
    assert_empty sitemap.get_elements("urlset/url/priority")
    assert_empty sitemap.get_elements("urlset/url/changefreq")
  end
end
