# frozen_string_literal: true

source "https://rubygems.org"

gem "jekyll", "~> 4.4.1"
# Jekyll 4 uses Liquid 4, while liquid-c 4.1 and newer require Liquid 5.
gem "liquid-c", "~> 4.0.1"
gem "logger"

group :jekyll_plugins do
  gem "defold-author-profiles", path: "_plugins/defold-author-profiles"
  gem "jekyll-default-layout"
  gem "jekyll-optional-front-matter"
  gem "jekyll-titles-from-headings"
end

group :test do
  gem "minitest", "~> 6.0"
end
