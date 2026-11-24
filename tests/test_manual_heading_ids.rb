# frozen_string_literal: true

require "jekyll"
require "minitest/autorun"
require_relative "../_plugins/defold_gfm"

class ManualHeadingIdsTest < Minitest::Test
  def test_localized_headings_can_reuse_english_ids_starting_with_a_digit
    config = Jekyll.configuration("source" => File.expand_path("..", __dir__), "quiet" => true)
    html = Jekyll::Converters::Markdown.new(config).convert(<<~MARKDOWN)
      ## 2D graphics

      ## Orientacja sceny 2D i 3D {#2d-and-3d-scene-orientation}

      ### Автодополнение кода {#code-completion}

      ```
      ## Example {#2d-example}
      ```
    MARKDOWN

    assert_includes html, '<h2 id="2d-graphics">2D graphics</h2>'
    assert_includes html, '<h2 id="2d-and-3d-scene-orientation">Orientacja sceny 2D i 3D</h2>'
    assert_includes html, '<h3 id="code-completion">Автодополнение кода</h3>'
    assert_includes html, '## Example {#2d-example}'
  end
end
