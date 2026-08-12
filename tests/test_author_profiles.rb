# frozen_string_literal: true

require "json"
require "minitest/autorun"
require "tmpdir"
require "jekyll"
require "defold-author-profiles"

class AuthorProfilesTest < Minitest::Test
  def self.site
    @site ||= begin
      config = Jekyll.configuration(
        "source" => File.expand_path("..", __dir__),
        "destination" => File.join(Dir.tmpdir, "defold-author-profile-test"),
        "quiet" => true
      )
      site = Jekyll::Site.new(config)
      site.reset
      site.read
      Defold::AuthorProfilesGenerator.new.generate(site)
      site
    end
  end

  def site
    self.class.site
  end

  def test_registry_has_explicit_kebab_case_ids
    profiles = site.data.fetch("authors")
    ids = profiles.map { |profile| profile.fetch("id") }

    assert ids.all? { |author_id| Defold::AuthorRegistry::ID_PATTERN.match?(author_id) }
    refute profiles.any? { |profile| profile.key?("aliases") }
  end

  def test_registry_rejects_duplicate_and_malformed_ids
    assert_raises(Defold::AuthorProfileError) do
      Defold::AuthorRegistry.new([{ "id" => "Not Valid", "name" => "Alice" }])
    end
    assert_raises(Defold::AuthorProfileError) do
      Defold::AuthorRegistry.new(
        [
          { "id" => "shared", "name" => "Alice" },
          { "id" => "shared", "name" => "Bob" }
        ]
      )
    end
  end

  def test_registry_validates_profile_urls
    assert_raises(Defold::AuthorProfileError) do
      Defold::AuthorRegistry.new(
        [
          {
            "id" => "alice",
            "name" => "Alice",
            "links" => [{ "type" => "website", "url" => "http://example.com" }]
          }
        ]
      )
    end
  end

  def test_generator_resolves_every_catalog_record
    profiles_by_id = site.data.fetch("authors").to_h do |profile|
      [profile.fetch("id"), profile]
    end

    site.data.fetch("assets").each_value do |asset|
      assert_equal asset.fetch("author_profile").fetch("id"), asset.fetch("author_id")
      assert_equal profiles_by_id.fetch(asset.fetch("author_id")).fetch("name"),
                   asset.fetch("author_profile").fetch("name")
      refute asset.key?("author")
    end
    site.data.fetch("examplesindex").each do |example|
      assert_equal example.fetch("author_profiles").map { |profile| profile.fetch("id") },
                   example.fetch("author_ids")
      example.fetch("author_profiles").each do |profile|
        assert_equal profiles_by_id.fetch(profile.fetch("id")).fetch("name"),
                     profile.fetch("name")
      end
      refute example.key?("author")
      refute example.key?("authors")
    end
  end

  def test_generator_resolves_legacy_example_author
    registry = Defold::AuthorRegistry.new(
      [{ "id" => "alice", "name" => "Alice" }]
    )
    generator = Defold::AuthorProfilesGenerator.new
    example = { "author" => "Alice" }

    profiles = generator.send(:example_profiles, example, registry, "example test")

    assert_equal %w[alice], profiles.map { |profile| profile.fetch("id") }
    assert_equal %w[alice], example.fetch("author_ids")
    refute example.key?("author")
  end

  def test_generator_rejects_invalid_catalog_attribution
    registry = Defold::AuthorRegistry.new(
      [{ "id" => "alice", "name" => "Alice" }]
    )
    generator = Defold::AuthorProfilesGenerator.new

    assert_raises(Defold::AuthorProfileError) do
      generator.send(:resolve_profile, { "author_id" => "Not Valid" }, registry, "asset test")
    end
    assert_raises(Defold::AuthorProfileError) do
      generator.send(:example_profiles, { "authors" => ["Alice"] }, registry, "example test")
    end
    assert_raises(Defold::AuthorProfileError) do
      generator.send(:example_profiles, { "author_ids" => %w[alice alice] }, registry, "example test")
    end
  end

  def test_directory_matches_generated_contributions
    directory = site.data.fetch("author_directory")
    pages = site.pages.select { |page| page.data["layout"] == "author" }

    assert_equal directory.map { |profile| profile.fetch("url") }.sort,
                 pages.map(&:url).sort
    assert_equal directory.map { |profile| profile.fetch("name").downcase }.sort,
                 directory.map { |profile| profile.fetch("name").downcase }
  end

  def test_only_stable_author_routes_are_generated
    author_pages = site.pages.select { |page| page.data["layout"] == "author" }
    urls = author_pages.map(&:url)

    refute urls.any? { |url| %r{/authors/[0-9a-f]{32}/}.match?(url) }
    assert_empty Dir[File.join(File.expand_path("..", __dir__), "authors", "*.md")]
  end
end
