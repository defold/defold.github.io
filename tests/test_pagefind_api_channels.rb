# frozen_string_literal: true

require "fileutils"
require "jekyll"
require "minitest/autorun"
require "tmpdir"
require "yaml"

class PagefindApiChannelsTest < Minitest::Test
  ROOT = File.expand_path("..", __dir__)
  VERSIONS = { "stable" => "1.13.1", "beta" => "1.13.2", "alpha" => "1.14.0" }.freeze

  def self.output
    @output ||= Dir.mktmpdir("defold-pagefind-channels-test") do |directory|
      source = File.join(directory, "source")
      destination = File.join(directory, "site")
      %w[_includes _layouts _data].each { |path| FileUtils.mkdir_p(File.join(source, path)) }
      %w[head.html search_engine_metadata.html googleanalytics.html googletagmanager_head.html
         api_channel_switcher.html pagefind_channel_filter.html].each do |name|
        FileUtils.cp(File.join(ROOT, "_includes", name), File.join(source, "_includes", name))
      end
      %w[topnav.html catalog_search_field.html marksearchhits.html copy-icon-for-code-snippets.html].each do |name|
        File.write(File.join(source, "_includes", name), "")
      end
      Dir.glob(File.join(ROOT, "_includes", "{api,ref}_*.html")).each do |path|
        FileUtils.cp(path, File.join(source, "_includes"))
      end
      File.write(File.join(source, "_layouts", "base.html"),
                 '<html><head>{% include head.html %}</head><body>{{ content }}</body></html>')
      FileUtils.cp(File.join(ROOT, "_layouts", "api.html"), File.join(source, "_layouts"))
      FileUtils.cp(File.join(ROOT, "_layouts", "redirect.html"), File.join(source, "_layouts"))
      File.write(File.join(source, "_data", "engine_versions.yml"), VERSIONS.to_yaml)
      File.write(File.join(source, "_data", "branchindex.yml"), VERSIONS.keys.to_yaml)
      File.write(File.join(source, "_data", "refindex.yml"), [].to_yaml)
      reference = {
        "info" => { "api_language" => "Lua", "brief" => "Fixture API", "name" => "Fixture" },
        "elements" => [{ "type" => "FUNCTION", "name" => "fixture.create", "parameters" => [],
                         "returnvalues" => [], "description" => "Create a fixture." }]
      }
      File.write(File.join(source, "_data", "ref.yml"),
                 VERSIONS.keys.to_h do |branch|
                   lua = reference.merge("format_version" => branch == "stable" ? 1 : 2)
                   if branch == "alpha"
                     lua = lua.merge("elements" => reference["elements"] +
                       [reference["elements"].first.merge("name" => "fixture.experimental")])
                   end
                   cpp = reference.merge("info" => reference["info"].merge("api_language" => "C++"))
                   [branch, { "fixture-lua" => lua, "fixture-cpp" => cpp }]
                 end.to_yaml)
      File.write(File.join(source, "_data", "extensions.yml"), { "fixture" => reference }.to_yaml)

      VERSIONS.each_key do |branch|
        prefix = branch == "stable" ? "ref" : "ref/#{branch}"
        data = { "layout" => "api", "branch" => branch, "ref" => "fixture-lua", "type" => "Defold Lua" }
        write_page(source, "#{prefix}/fixture-lua.md", data)
        write_page(source, "#{prefix}/fixture-cpp.md", data.merge("ref" => "fixture-cpp", "type" => "Defold C++"))
        write_page(source, "#{prefix}/fixture.md", data.merge("pagefind_exclude" => true))
        write_page(source, "#{prefix}/overview_defoldlua.md", data.merge("ref" => "overview"))
      end
      write_page(source, "extension/fixture.md",
                 "layout" => "api", "branch" => "stable", "ref" => "fixture", "type" => "Extension")
      write_page(source, "manual.md", "layout" => "base")
      write_page(source, "ref/stable/fixture-lua.md",
                 "layout" => "redirect", "redirect_to" => "/ref/fixture-lua/")

      Jekyll::Site.new(Jekyll.configuration(
        "source" => source, "destination" => destination,
        "cache_dir" => File.join(directory, "cache"), "permalink" => "pretty",
        "url" => "https://www.defold.com", "quiet" => true
      )).process
      Dir.glob(File.join(destination, "**", "*.html"))
         .to_h { |path| [path.delete_prefix(destination), File.read(path)] }
    end
  end

  def self.write_page(source, path, data)
    target = File.join(source, path)
    FileUtils.mkdir_p(File.dirname(target))
    File.write(target, { "title" => "API reference (Fixture)" }.merge(data).to_yaml +
                      "---\n<main data-pagefind-body>Shared fixture documentation.</main>\n")
  end

  def html(path)
    self.class.output.fetch("#{path}index.html")
  end

  def test_each_channel_is_searchable_and_identified_with_its_engine_version
    VERSIONS.each do |branch, version|
      prefix = branch == "stable" ? "/ref" : "/ref/#{branch}"
      content = html("#{prefix}/fixture-lua/")
      refute_match(/id="page"[^>]*data-pagefind-ignore/, content)
      assert_includes content, 'data-pagefind-body'
      assert_includes content, 'data-pagefind-filter="section">API'
      assert_includes content, %(data-pagefind-filter="API channel[content]" content="#{branch.capitalize}")
      assert_includes content, %(data-pagefind-meta="title">API reference (Fixture) — #{branch.capitalize} (#{version}))
      %w[desktop mobile].each do |viewport|
        controls = content[/<fieldset id="api-search-#{viewport}-channel".*?<\/fieldset>/m]
        assert_equal 3, controls.scan('type="radio" name="channel"').length
        assert_equal 1, controls.scan(/\bchecked\b/).length
        assert_includes controls, %(value="#{branch}" checked)
        assert_equal 3, controls.scan('data-pagefind-channel-count').length
      end
    end
  end

  def test_aliases_overviews_and_redirects_remain_excluded
    ["/ref", "/ref/beta", "/ref/alpha"].each do |prefix|
      ["fixture", "overview_defoldlua"].each do |page|
        content = html("#{prefix}/#{page}/")
        assert_match(/id="page"[^>]*data-pagefind-ignore/, content)
        refute_includes content, 'data-pagefind-filter="section">API'
      end
    end
    refute_includes html("/ref/stable/fixture-lua/"), 'data-pagefind-body'
  end

  def test_manuals_and_extensions_are_available_in_every_channel
    ["/manual/", "/extension/fixture/"].each do |path|
      VERSIONS.each_key do |branch|
        assert_includes html(path), %(data-pagefind-filter="API channel:#{branch.capitalize}")
      end
    end
    extension = html("/extension/fixture/")
    refute_includes extension, 'data-pagefind-meta="title"'
    assert_equal 2, extension.scan('value="stable" checked').length
    assert_includes extension, 'data-pagefind-weight="1"'
  end

  def test_channel_preference_applies_to_function_sections_in_lua_and_cpp
    %w[lua cpp].each do |language|
      weights = ["/ref", "/ref/beta", "/ref/alpha"].map do |prefix|
        content = html("#{prefix}/fixture-#{language}/")
        content.scan(/data-pagefind-weight="([^"]+)"/).flatten.each do |weight|
          assert_operator Float(weight), :>, 0
          assert_operator Float(weight), :<=, 10
        end
        Float(content[/<div data-pagefind-weight="([^"]+)">\s*<h4 id="fixture.create/, 1])
      end
      assert_operator weights[0], :>, weights[1]
      assert_operator weights[1], :>, weights[2]
    end
  end
end
