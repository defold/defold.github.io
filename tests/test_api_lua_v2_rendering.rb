# frozen_string_literal: true

require "fileutils"
require "json"
require "jekyll"
require "minitest/autorun"
require "tmpdir"

class ApiLuaV2RenderingTest < Minitest::Test
  ROOT = File.expand_path("..", __dir__)
  INCLUDES = %w[
    api_lua_v2.html
    api_lua_v2_parameters.html
    api_lua_v2_signature.html
    api_lua_v2_summary.html
    ref_anchor_target.html
    ref_anchorlink.html
  ].freeze

  def test_member_markup_and_long_alias_signature
    Dir.mktmpdir("defold-api-lua-v2-test") do |directory|
      source = File.join(directory, "source")
      destination = File.join(directory, "site")
      includes = File.join(source, "_includes")
      data = File.join(source, "_data")
      FileUtils.mkdir_p([includes, data])

      INCLUDES.each do |name|
        FileUtils.cp(
          File.join(ROOT, "_includes", name),
          File.join(includes, name)
        )
      end

      File.write(
        File.join(source, "index.html"),
        "---\n---\n{% include api_lua_v2.html ref=site.data.ref %}\n"
      )
      File.write(
        File.join(data, "ref.json"),
        JSON.pretty_generate(reference_document)
      )

      site = Jekyll::Site.new(Jekyll.configuration(
        "source" => source,
        "destination" => destination,
        "cache_dir" => File.join(directory, "cache"),
        "quiet" => true
      ))
      site.process

      rendered = File.read(File.join(destination, "index.html"))
      assert_includes(
        rendered,
        '<code class="api-lua-v2-signature">render.render_target_params = '
      )
      assert_includes rendered, "Use <code>code</code> formatting."
    end
  end

  private

  def reference_document
    {
      "info" => {
        "brief" => "Render API",
        "description_html" => "Render documentation."
      },
      "elements" => [
        {
          "type" => "TYPEDEF",
          "name" => "render.render_target_params",
          "brief" => "Render-target parameters.",
          "target_type_html" => (
            "{ sample_count?:integer, " \
            "[graphics.BUFFER_TYPE]:render.render_target_buffer_params }"
          ),
          "description" => "Target configuration.",
          "examples" => []
        },
        {
          "type" => "STRUCT",
          "name" => "render.render_target_buffer_params",
          "brief" => "Render-target buffer parameters.",
          "description" => "Buffer configuration.",
          "examples" => [],
          "members" => [
            {
              "display_name" => "format",
              "is_optional" => false,
              "type_html" => "graphics.TEXTURE_FORMAT",
              "doc" => "Use <code>code</code> formatting."
            }
          ]
        }
      ]
    }
  end
end
