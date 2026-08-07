# frozen_string_literal: true

source "https://rubygems.org"

git_source(:github) {|repo_name| "https://github.com/#{repo_name}" }

gem "bundler"
gem "webrick"
gem "jekyll"
gem "liquid-c"
gem "csv"
gem "logger"
group :jekyll_plugins do
  gem 'github-pages'
  # GitHub Pages forces safe mode and disables repository-local _plugins.
  # Loading this path gem through Bundler keeps the build-time generator active.
  gem 'defold-author-profiles', path: '_plugins/defold-author-profiles'
end
