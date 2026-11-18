# frozen_string_literal: true

require "kramdown-parser-gfm"

module Kramdown
  module Parser
    class DefoldGFM < GFM
      # GFM can generate IDs starting with a digit, such as the slug for "2D graphics".
      # Allow translations to use those same IDs explicitly.
      NUMERIC_HEADING_ID = /[\t ]+\{#([0-9]#{REXML::XMLTokens::NAME_CHAR}*)\}\z/

      protected

      def parse_header_contents
        text, id = super
        if id.nil? && (match = NUMERIC_HEADING_ID.match(text))
          [text[0...match.begin(0)], match[1]]
        else
          [text, id]
        end
      end
    end
  end
end
