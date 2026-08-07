# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name = "defold-author-profiles"
  spec.version = "1.0.0"
  spec.summary = "Build-time author profile pages for the Defold website"
  spec.authors = ["Defold Foundation"]
  spec.files = ["lib/defold-author-profiles.rb"]
  spec.require_paths = ["lib"]
  spec.add_dependency "jekyll", ">= 3.9", "< 5"
end
