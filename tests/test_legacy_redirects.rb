# frozen_string_literal: true

require "fileutils"
require "json"
require "minitest/autorun"
require "tmpdir"
require_relative "../_plugins/legacy-redirects/generator"

class LegacyRedirectsTest < Minitest::Test
  ROOT = File.expand_path("..", __dir__)

  def setup
    @directory = Dir.mktmpdir("defold-legacy-redirects")
    @source = File.join(@directory, "source")
    FileUtils.mkdir_p(File.join(@source, "_layouts"))
    FileUtils.cp(File.join(ROOT, "_layouts/redirect.html"), File.join(@source, "_layouts"))
    write_page("ref/dmengine/index.html")
  end

  def teardown
    FileUtils.remove_entry(@directory)
  end

  def test_directory_index_uses_existing_redirect_layout
    site = make_site([{ "from" => "/ref/dmEngine", "to" => "/ref/dmengine/" }])
    generate(site)
    page = site.pages.find { |item| item.url == "/ref/dmEngine/" }
    refute_nil page
    assert_equal false, page.data["sitemap"]
    assert_equal true, page.data["pagefind_exclude"]
    site.render
    site.write
    output = File.read(File.join(site.dest, "ref/dmEngine/index.html"))
    assert_includes output, 'content="noindex, follow"'
    assert_includes output, 'content="0; url=/ref/dmengine/"'
    assert_includes output, 'href="https://defold.com/ref/dmengine/"'
    assert_includes output, 'data-pagefind-ignore="all"'
    assert_includes output, 'window.location.search'
    assert_includes output, 'window.location.hash'
  end

  def test_missing_target_stops_generation
    assert_invalid([{ "from" => "/old/", "to" => "/missing/" }], "target does not exist")
  end

  def test_real_page_cannot_be_overwritten
    assert_invalid([{ "from" => "/ref/dmengine", "to" => "/ref/dmengine/" }], "collides")
  end

  def test_static_file_cannot_be_replaced_by_directory
    File.write(File.join(@source, "occupied"), "static")
    assert_invalid([{ "from" => "/occupied/", "to" => "/ref/dmengine/" }], "collides")
  end

  def test_static_file_cannot_be_replaced_by_file
    File.write(File.join(@source, "occupied.html"), "static")
    assert_invalid([{ "from" => "/occupied.html", "to" => "/ref/dmengine/" }], "collides")
  end

  def test_other_generators_outputs_are_protected
    site = make_site([{ "from" => "/generated/", "to" => "/ref/dmengine/" }])
    site.pages << Jekyll::PageWithoutAFile.new(site, site.source, "generated", "index.html")
    assert_raises(Defold::LegacyRedirectError) { generate(site) }
  end

  def test_duplicate_slash_variants_are_rejected
    assert_invalid(%w[/old /old/].map { |from| { "from" => from, "to" => "/ref/dmengine/" } }, "duplicate")
  end

  def test_redirect_chains_and_cycles_are_rejected
    assert_invalid([
      { "from" => "/old/", "to" => "/older/" },
      { "from" => "/older/", "to" => "/old/" }
    ], "target does not exist")
  end

  def test_invalid_paths_are_rejected
    ["//example.com/", "https://example.com/", "/ref/?q=1", "/ref/#anchor", "/../ref/", "/ref/./", "/ref//x/", nil].each do |value|
      %w[from to].each do |key|
        entry = { "from" => "/old/", "to" => "/ref/dmengine/" }.merge(key => value)
        assert_invalid([entry], "site-relative path")
      end
    end
    assert_invalid({}, "expected an array")
    assert_invalid([nil], "expected from/to paths")
  end

  def test_file_sources_keep_their_exact_path
    site = make_site([{ "from" => "/legacy.html", "to" => "/ref/dmengine/" }])
    generate(site)
    assert site.pages.any? { |page| page.url == "/legacy.html" }
  end

  def test_entire_catalog_has_existing_targets_and_no_collisions
    site = Jekyll::Site.new(Jekyll.configuration(
      "source" => ROOT,
      "destination" => File.join(@directory, "catalog"),
      "quiet" => true
    ))
    site.reset
    site.read
    before = site.pages.length
    generate(site)
    entries = JSON.parse(File.read(File.join(ROOT, "_data/legacy_redirects.json")))
    assert_equal 89, entries.length
    assert_equal before + entries.length, site.pages.length
    assert entries.all? { |entry| entry.fetch("from").start_with?("/ref/") }
  end

  private

  def write_page(path)
    filename = File.join(@source, path)
    FileUtils.mkdir_p(File.dirname(filename))
    File.write(filename, "---\nlayout: null\n---\nTarget\n")
  end

  def make_site(entries)
    site = Jekyll::Site.new(Jekyll.configuration(
      "source" => @source,
      "destination" => File.join(@directory, "site"),
      "url" => "https://defold.com",
      "quiet" => true
    ))
    site.reset
    site.read
    site.data["legacy_redirects"] = entries
    site
  end

  def generate(site)
    Defold::LegacyRedirectsGenerator.new.generate(site)
  end

  def assert_invalid(entries, message)
    site = make_site(entries)
    before = site.pages.length
    error = assert_raises(Defold::LegacyRedirectError) { generate(site) }
    assert_includes error.message, message
    assert_equal before, site.pages.length
  end
end
