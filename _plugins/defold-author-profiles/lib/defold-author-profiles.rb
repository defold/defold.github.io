# frozen_string_literal: true

require "uri"

module Defold
  class AuthorProfileError < Jekyll::Errors::FatalException; end

  class AuthorRegistry
    ID_PATTERN = /\A[a-z0-9]+(?:-[a-z0-9]+)*\z/
    GITHUB_PATTERN = /\A[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?\z/
    MAX_BIO_LENGTH = 400
    PROFILE_FIELDS = %w[id name github bio avatar links support].freeze
    LINK_TYPES = %w[website github external x bluesky mastodon linkedin youtube].freeze
    SUPPORT_DESTINATIONS = {
      "github_sponsors" => ["github.com", "/sponsors/"],
      "ko_fi" => ["ko-fi.com", "/"],
      "patreon" => ["patreon.com", "/"],
      "buy_me_a_coffee" => ["buymeacoffee.com", "/"],
      "paypal" => ["paypal.me", "/"]
    }.freeze

    attr_reader :profiles

    def initialize(records)
      fail_with("_data/authors.json must contain an array") unless records.is_a?(Array)
      fail_with("_data/authors.json must contain at least one profile") if records.empty?

      @profiles = []
      @by_id = {}
      records.each_with_index { |record, index| add_profile(record, index) }
    end

    def fetch(author_id, context)
      unless author_id.is_a?(String) && ID_PATTERN.match?(author_id)
        fail_with("#{context}: author_id must use lowercase ASCII kebab-case")
      end
      profile = @by_id[author_id]
      fail_with("#{context}: unknown author_id #{author_id.inspect}") unless profile
      profile
    end

    private

    def add_profile(record, index)
      context = "_data/authors.json[#{index}]"
      fail_with("#{context}: profile must be an object") unless record.is_a?(Hash)

      unknown_fields = record.keys.map(&:to_s) - PROFILE_FIELDS
      fail_with("#{context}: unknown profile field(s): #{unknown_fields.sort.join(', ')}") unless unknown_fields.empty?

      profile = stringify_keys(record)
      profile["id"] = clean_string(profile["id"], "#{context}: id")
      profile["name"] = clean_string(profile["name"], "#{context}: name")
      unless ID_PATTERN.match?(profile["id"])
        fail_with("#{profile['name']}: id must use lowercase ASCII kebab-case")
      end
      if @by_id.key?(profile["id"])
        fail_with("Duplicate author id #{profile['id'].inspect}")
      end

      validate_github(profile)
      validate_bio(profile)
      validate_avatar(profile)
      profile["links"] = validate_links(profile["links"], profile["name"])
      profile["support"] = validate_support(profile["support"], profile["name"])

      @profiles << profile
      @by_id[profile["id"]] = profile
    end

    def validate_github(profile)
      return unless profile.key?("github")

      profile["github"] = clean_string(profile["github"], "#{profile['name']}: github").delete_prefix("@")
      fail_with("#{profile['name']}: malformed GitHub username") unless GITHUB_PATTERN.match?(profile["github"])
    end

    def validate_bio(profile)
      return unless profile.key?("bio")

      profile["bio"] = clean_string(profile["bio"], "#{profile['name']}: bio")
      if profile["bio"].length > MAX_BIO_LENGTH
        fail_with("#{profile['name']}: bio must be at most #{MAX_BIO_LENGTH} characters")
      end
    end

    def validate_avatar(profile)
      return unless profile.key?("avatar")

      avatar = clean_string(profile["avatar"], "#{profile['name']}: avatar")
      if avatar.start_with?("/") && !avatar.start_with?("//") && !avatar.split("/").include?("..")
        profile["avatar"] = avatar
      else
        profile["avatar"] = validate_https_url(avatar, "#{profile['name']}: avatar")
      end
    end

    def validate_links(value, profile_name)
      return [] if value.nil?
      fail_with("#{profile_name}: links must be an array") unless value.is_a?(Array)

      value.map.with_index do |raw_link, index|
        context = "#{profile_name}: links[#{index}]"
        fail_with("#{context} must be an object") unless raw_link.is_a?(Hash)
        link = stringify_keys(raw_link)
        unknown = link.keys - %w[type label url]
        fail_with("#{context}: unknown field(s): #{unknown.sort.join(', ')}") unless unknown.empty?
        fail_with("#{context}.type is invalid") unless LINK_TYPES.include?(link["type"])
        link["url"] = validate_https_url(link["url"], "#{context}.url")
        link["label"] = clean_string(link["label"], "#{context}.label") if link.key?("label")
        link
      end
    end

    def validate_support(value, profile_name)
      return [] if value.nil?
      fail_with("#{profile_name}: support must be an array") unless value.is_a?(Array)
      fail_with("#{profile_name}: support allows at most three actions") if value.length > 3

      value.map.with_index do |raw_support, index|
        context = "#{profile_name}: support[#{index}]"
        fail_with("#{context} must be an object") unless raw_support.is_a?(Hash)
        support = stringify_keys(raw_support)
        unknown = support.keys - %w[type label url]
        fail_with("#{context}: unknown field(s): #{unknown.sort.join(', ')}") unless unknown.empty?
        destination = SUPPORT_DESTINATIONS[support["type"]]
        fail_with("#{context}.type is invalid") unless destination
        support["url"] = validate_https_url(support["url"], "#{context}.url")
        uri = URI.parse(support["url"])
        host = uri.host.to_s.downcase.delete_prefix("www.")
        unless host == destination[0] && uri.path.start_with?(destination[1])
          fail_with("#{context}.url is not an allowed #{support['type']} destination")
        end
        support["label"] = clean_string(support["label"], "#{context}.label") if support.key?("label")
        support
      end
    end

    def validate_https_url(value, context)
      value = clean_string(value, context)
      uri = URI.parse(value)
      unless uri.is_a?(URI::HTTPS) && uri.host && !uri.userinfo
        fail_with("#{context} must be an absolute https URL without credentials")
      end
      value
    rescue URI::InvalidURIError
      fail_with("#{context} must be an absolute https URL")
    end

    def clean_string(value, context)
      fail_with("#{context} must be a non-empty string") unless value.is_a?(String)
      value = value.gsub(/\s+/, " ").strip
      fail_with("#{context} must be a non-empty string") if value.empty?
      value
    end

    def stringify_keys(hash)
      hash.each_with_object({}) { |(key, value), result| result[key.to_s] = value }
    end

    def fail_with(message)
      raise AuthorProfileError, message
    end
  end

  class AuthorPage < Jekyll::PageWithoutAFile
    def initialize(site, profile, asset_ids, examples)
      super(site, site.source, File.join("authors", profile["id"]), "index.html")
      self.content = ""
      self.data = {
        "layout" => "author",
        "title" => profile["name"],
        "author_profile" => profile,
        "author_id" => profile["id"],
        "asset_ids" => asset_ids,
        "examples" => examples,
        "asset_count" => asset_ids.length,
        "example_count" => examples.length
      }
    end
  end

  class AuthorProfilesGenerator < Jekyll::Generator
    safe true
    priority :highest

    def generate(site)
      registry = AuthorRegistry.new(site.data["authors"])
      assets_by_author = Hash.new { |hash, key| hash[key] = [] }
      examples_by_author = Hash.new { |hash, key| hash[key] = [] }

      resolve_assets(site, registry, assets_by_author)
      resolve_examples(site, registry, examples_by_author)

      referenced_ids = (assets_by_author.keys | examples_by_author.keys).sort
      directory = referenced_ids.map do |author_id|
        profile = registry.fetch(author_id, "author directory")
        asset_ids = assets_by_author[author_id].uniq.sort
        examples = examples_by_author[author_id].uniq { |example| example["path"] }.sort_by { |example| example["path"] }
        site.pages << AuthorPage.new(site, profile, asset_ids, examples)
        profile.merge(
          "url" => "/authors/#{author_id}/",
          "asset_count" => asset_ids.length,
          "example_count" => examples.length
        )
      end
      site.data["author_directory"] = directory.sort_by { |profile| profile["name"].downcase }
    rescue AuthorProfileError => error
      Jekyll.logger.abort_with("Author profiles:", error.message)
    end

    private

    def resolve_assets(site, registry, assets_by_author)
      assets = site.data["assets"]
      raise AuthorProfileError, "_data/assets must contain an object" unless assets.is_a?(Hash)

      assets.each do |asset_id, asset|
        context = "asset #{asset_id}"
        raise AuthorProfileError, "#{context}: record must be an object" unless asset.is_a?(Hash)
        profile = resolve_profile(asset, registry, context)
        asset["id"] = asset_id
        asset["author_profile"] = profile
        assets_by_author[profile["id"]] << asset_id
      end
    end

    def resolve_examples(site, registry, examples_by_author)
      examples = site.data["examplesindex"]
      raise AuthorProfileError, "_data/examplesindex.json must contain an array" unless examples.is_a?(Array)

      examples.each_with_index do |example, index|
        context = "example #{example['path'] || index}"
        raise AuthorProfileError, "#{context}: record must be an object" unless example.is_a?(Hash)
        profiles = example_profiles(example, registry, context).uniq { |profile| profile["id"] }
        raise AuthorProfileError, "#{context}: author_ids must not be empty" if profiles.empty?
        example["author_profiles"] = profiles
        profiles.each { |profile| examples_by_author[profile["id"]] << example }
      end
    end

    def resolve_profile(record, registry, context)
      if record.key?("author")
        raise AuthorProfileError, "#{context}: legacy author field is not supported"
      end
      registry.fetch(record["author_id"], context)
    end

    def example_profiles(example, registry, context)
      legacy_fields = %w[author authors].select { |field| example.key?(field) }
      unless legacy_fields.empty?
        raise AuthorProfileError, "#{context}: legacy #{legacy_fields.join(' and ')} field is not supported"
      end
      author_ids = example["author_ids"]
      unless author_ids.is_a?(Array) && !author_ids.empty?
        raise AuthorProfileError, "#{context}: author_ids must be a non-empty array"
      end
      if author_ids.length != author_ids.uniq.length
        raise AuthorProfileError, "#{context}: author_ids must not contain duplicates"
      end
      author_ids.map.with_index { |author_id, index| registry.fetch(author_id, "#{context} author_ids[#{index}]") }
    end
  end
end
