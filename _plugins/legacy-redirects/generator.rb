# frozen_string_literal: true

require "jekyll"
require "set"

module Defold
  class LegacyRedirectError < Jekyll::Errors::FatalException; end

  class LegacyRedirectPage < Jekyll::PageWithoutAFile
    def initialize(site, source, target)
      # A directory index serves /x/ and lets the host normalize /x to /x/.
      # Writing both an extensionless file x and a directory x is impossible.
      super(site, site.source, "", "index.html")
      self.content = ""
      self.data = {
        "permalink" => source,
        "layout" => "redirect",
        "redirect_to" => target,
        "title" => "Redirecting",
        "sitemap" => false,
        "pagefind_exclude" => true
      }
    end
  end

  class LegacyRedirectsGenerator < Jekyll::Generator
    safe true
    priority :lowest

    def generate(site)
      entries = site.data.fetch("legacy_redirects", [])
      fail_map("expected an array") unless entries.is_a?(Array)

      existing = site.pages + site.collections.values.flat_map(&:docs) + site.static_files
      urls = existing.map(&:url).to_set
      destinations = existing.map { |item| item.destination(site.dest) }.to_set
      sources = Set.new

      # Validate the entire map before modifying site.pages.
      # Targets must already exist, so a redirect cannot point at another entry or form a cycle.
      pages = entries.each_with_index.map do |entry, index|
        fail_map("entry #{index}: expected from/to paths") unless entry.is_a?(Hash)
        source = path(entry["from"], index)
        target = path(entry["to"], index)
        source = "#{source}/" if File.extname(source).empty? && !source.end_with?("/")
        fail_map("entry #{index}: duplicate source #{source}") unless sources.add?(source)
        fail_map("entry #{index}: target does not exist: #{target}") unless urls.include?(target)

        page = LegacyRedirectPage.new(site, source, target)
        destination = page.destination(site.dest)
        collision = destinations.any? do |other|
          destination == other || destination.start_with?("#{other}/") || other.start_with?("#{destination}/")
        end
        fail_map("entry #{index}: source collides with an existing output: #{source}") if collision
        destinations.add(destination)
        page
      end
      site.pages.concat(pages)
    end

    private

    def path(value, index)
      unless value.is_a?(String) && %r{\A/(?:[A-Za-z0-9_~.-]+/)*[A-Za-z0-9_~.-]*\z}.match?(value) &&
             value != "/" && value.split("/").none? { |part| %w[. ..].include?(part) }
        fail_map("entry #{index}: expected a site-relative path without query or fragment: #{value.inspect}")
      end
      value
    end

    def fail_map(message)
      raise LegacyRedirectError, "_data/legacy_redirects.json: #{message}"
    end
  end
end
