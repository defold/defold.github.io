# -*- encoding: utf-8 -*-
# stub: liquid-c 4.0.1 ruby lib
# stub: ext/liquid_c/extconf.rb

Gem::Specification.new do |s|
  s.name = "liquid-c".freeze
  s.version = "4.0.1".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.metadata = { "allowed_push_host" => "https://rubygems.org" } if s.respond_to? :metadata=
  s.require_paths = ["lib".freeze]
  s.authors = ["Justin Li".freeze, "Dylan Thacker-Smith".freeze]
  s.date = "2023-01-11"
  s.email = ["gems@shopify.com".freeze]
  s.extensions = ["ext/liquid_c/extconf.rb".freeze]
  s.files = ["ext/liquid_c/extconf.rb".freeze]
  s.homepage = "https://github.com/shopify/liquid-c".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.3.3".freeze
  s.summary = "Liquid performance extension in C".freeze

  s.installed_by_version = "3.5.16".freeze if s.respond_to? :installed_by_version

  s.specification_version = 4

  s.add_runtime_dependency(%q<liquid>.freeze, [">= 3.0.0".freeze])
  s.add_development_dependency(%q<bundler>.freeze, [">= 1.5".freeze])
  s.add_development_dependency(%q<rake>.freeze, [">= 0".freeze])
  s.add_development_dependency(%q<rake-compiler>.freeze, [">= 0".freeze])
  s.add_development_dependency(%q<minitest>.freeze, [">= 0".freeze])
  s.add_development_dependency(%q<stackprof>.freeze, [">= 0".freeze])
end
