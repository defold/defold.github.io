# frozen_string_literal: true

require 'jekyll'
require 'fileutils'
require 'json'
require 'minitest/autorun'
require 'tmpdir'

class PlatformImagesTest < Minitest::Test
  ROOT = File.expand_path('..', __dir__)

  def test_webp_sources_have_independent_png_fallbacks
    Dir.mktmpdir('defold-platform-images') do |directory|
      source = File.join(directory, 'source')
      destination = File.join(directory, 'site')
      FileUtils.mkdir_p(File.join(source, '_includes'))
      FileUtils.mkdir_p(File.join(source, '_data'))
      FileUtils.cp(File.join(ROOT, '_includes/platforms.html'), File.join(source, '_includes'))
      FileUtils.cp(File.join(ROOT, '_data/responsive_images.json'), File.join(source, '_data'))
      File.write(File.join(source, 'index.html'), "---\n---\n{% include platforms.html %}")
      Jekyll::Site.new(Jekyll.configuration(
        'source' => source, 'destination' => destination,
        'cache_dir' => File.join(directory, 'cache'), 'plugins_dir' => [], 'quiet' => true
      )).process
      html = File.read(File.join(destination, 'index.html'))
      pictures = html.scan(/<picture class="platforms-grid-picture">(.*?)<\/picture>/m).flatten
      assert_equal 13, pictures.length
      pictures.each do |picture|
        webp = picture[/<source\b[^>]*>/]
        fallback = picture[/<img\b[^>]*>/]
        assert_includes webp, 'type="image/webp"'
        assert_includes webp, 'sizes="42px"'
        assert_match /srcset="[^"]+\.webp 42w/, webp
        assert_match %r{src="/images/logo/platform/100px-[^"]+\.png"}, fallback
        refute_includes fallback, 'srcset='
        fallback_path = fallback[/src="([^"]+)"/, 1]
        assert File.file?(File.join(ROOT, fallback_path.delete_prefix('/')))
      end
      assert_includes html, 'src="/images/logo/platform/xbox-stacked-white.svg"'
    end
  end
end
