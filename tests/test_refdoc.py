import copy
import unittest

import refdoc


class RefdocFormatTests(unittest.TestCase):
    def test_missing_version_is_legacy_v1(self):
        self.assertEqual(1, refdoc.format_version({}))

    def test_rejects_invalid_and_unknown_versions(self):
        for version in (True, "2", 3):
            with self.subTest(version=version):
                with self.assertRaises(ValueError):
                    refdoc.format_version({"format_version": version})

    def test_rejects_mixed_versions_in_one_namespace(self):
        with self.assertRaisesRegex(ValueError, "mixes.*1 and 2"):
            refdoc.require_matching_format_versions(
                {}, {"format_version": 2}, "go-lua", "go-extra.json")

    def test_prepares_v2_lua_types_and_enum_members(self):
        api = {
            "format_version": 2,
            "info": {"api_language": "Lua"},
            "elements": [
                {
                    "type": "ENUM",
                    "name": "go.EASING",
                    "parameters": [],
                    "members": [],
                },
                {
                    "type": "CONSTANT",
                    "name": "go.EASING_LINEAR",
                    "brief": "linear easing",
                    "description": "",
                    "parameters": [],
                },
                {
                    "type": "CONSTANT",
                    "name": "go.PLAYBACK_NONE",
                    "parameters": [],
                },
                {
                    "type": "TYPEDEF",
                    "name": "go.target",
                    "parameters": [{"name": "value", "types": ["string", "url"]}],
                },
                {
                    "type": "STRUCT",
                    "name": "on_input.action",
                    "members": [{"name": "pressed?", "type": "boolean"}],
                },
            ],
        }

        prepared = refdoc.prepare_lua_v2(copy.deepcopy(api))
        enum, enum_constant, standalone, alias, record = prepared["elements"]

        self.assertEqual("integer", enum["value_type"])
        self.assertEqual(
            [{"name": "go.EASING_LINEAR", "doc": "linear easing"}],
            enum["members"])
        self.assertTrue(enum_constant["is_enum_member"])
        self.assertEqual("go.EASING", enum_constant["value_type"])
        self.assertFalse(standalone["is_enum_member"])
        self.assertEqual("string | url", alias["target_type"])
        self.assertEqual("pressed", record["members"][0]["display_name"])
        self.assertTrue(record["members"][0]["is_optional"])

    def test_links_documented_and_builtin_types(self):
        namespaces = {
            "go-lua": {
                "format_version": 2,
                "info": {"api_language": "Lua"},
                "elements": [
                    {"type": "ENUM", "name": "go.PLAYBACK"},
                    {
                        "type": "FUNCTION",
                        "name": "go.animate",
                        "description": "",
                        "parameters": [
                            {
                                "name": "playback",
                                "types": ["go.PLAYBACK"],
                                "doc": "",
                            },
                            {
                                "name": "callback",
                                "types": [
                                    "fun(self:any, url:url, property:hash)"
                                ],
                                "doc": (
                                    'Receives <span class="type">url</span>.\n'
                                    '<dl>\n'
                                    '<dt><code>self</code></dt>\n'
                                    '<dd><span class="type">object</span> '
                                    'The current object.</dd>\n'
                                    '<dt><code>url</code></dt>\n'
                                    '<dd><span class="type">url</span> '
                                    'The component address.</dd>\n'
                                    '<dt><code>values</code></dt>\n'
                                    '<dd><span class="type">hash[</span>] '
                                    'The identifiers.</dd>\n'
                                    '</dl>'
                                ),
                            },
                        ],
                    },
                ],
            },
            "builtins-lua": {
                "format_version": 2,
                "info": {"api_language": "Lua"},
                "elements": [{"type": "TYPEDEF", "name": "hash"}],
            },
            "msg-lua": {
                "format_version": 2,
                "info": {"api_language": "Lua"},
                "elements": [{"type": "CLASS", "name": "url"}],
            },
            "vmath-lua": {
                "format_version": 2,
                "info": {"api_language": "Lua"},
                "elements": [{"type": "CLASS", "name": "vector3"}],
            },
        }
        targets = refdoc.lua_type_targets(namespaces)

        prepared = refdoc.prepare_lua_v2(
            copy.deepcopy(namespaces["go-lua"]), "go-lua", targets)
        playback, callback = prepared["elements"][1]["parameters"]

        self.assertEqual(
            '<a href="#go.PLAYBACK">go.PLAYBACK</a>',
            playback["types_html"][0])
        callback_html = callback["types_html"][0]
        callback_table_html = callback["types_table_html"][0]
        self.assertTrue(callback_html.startswith("fun("))
        self.assertIn("function</a>(\n\tself:", callback_table_html)
        self.assertIn(",\n\turl:", callback_table_html)
        self.assertIn(",\n\tproperty:", callback_table_html)
        self.assertIn(
            'self:<a href="../../../manuals/lua/'
            '#variables-and-data-types">any</a>',
            callback_html)
        self.assertIn(
            'url:<a href="../msg-lua/#url">url</a>', callback_html)
        self.assertNotIn('<a href="../msg-lua/#url">url</a>:', callback_html)
        self.assertIn(
            'property:<a href="../builtins-lua/#hash">hash</a>',
            callback_html)
        self.assertIn(
            '<span class="type"><a href="../msg-lua/#url">url</a></span>',
            callback["doc"])
        self.assertIn(
            '<dt class="api-lua-v2-type-definition"><code>self:'
            '<a href="../../../manuals/lua/#variables-and-data-types">'
            'object</a></code></dt>\n<dd>The current object.</dd>',
            callback["doc"])
        self.assertIn(
            '<dt class="api-lua-v2-type-definition"><code>url:'
            '<a href="../msg-lua/#url">url</a></code></dt>\n'
            '<dd>The component address.</dd>',
            callback["doc"])
        self.assertIn(
            '<dt class="api-lua-v2-type-definition"><code>values:'
            '<a href="../builtins-lua/#hash">hash</a>[]</code></dt>\n'
            '<dd>The identifiers.</dd>',
            callback["doc"])
        self.assertNotIn('href="/', callback_html)

        self.assertEqual(
            '<a href="../vmath-lua/#vector3">vector3</a>[]',
            refdoc.link_lua_type("vector3[]", "go-lua", targets))

    def test_does_not_guess_between_ambiguous_type_targets(self):
        targets = {
            "b2Body": [
                (0, "b2d-lua", "b2Body"),
                (0, "b2d.body-lua", "b2Body"),
            ],
        }

        self.assertEqual(
            "b2Body", refdoc.link_lua_type("b2Body", "go-lua", targets))
        self.assertEqual(
            '<a href="#b2Body">b2Body</a>',
            refdoc.link_lua_type("b2Body", "b2d-lua", targets))

    def test_formats_structured_table_types_at_top_level_only(self):
        self.assertEqual(
            "function(\n"
            "\tcallback:fun(x:number, y:number),\n"
            "\toptions:{ value:number, label:string }):boolean",
            refdoc.format_lua_type_for_table(
                "fun(callback:fun(x:number, y:number), "
                "options:{ value:number, label:string }):boolean"))
        self.assertEqual(
            "{index?:integer,\nkey?:hash,\nkeys?:hash[]}",
            refdoc.format_lua_type_for_table(
                "{ index?:integer, key?:hash, keys?:hash[] }"))

    def test_preserves_nested_type_definition_structure(self):
        value = (
            '<dl><dt><code>outer</code></dt>'
            '<dd><span class="type">table</span> Entries:'
            '<dl><dt><code>inner</code></dt>'
            '<dd><span class="type">string</span> A value.</dd>'
            '</dl></dd></dl>')

        formatted = refdoc._format_lua_type_definitions(value)

        self.assertIn(
            '<dt><code>outer</code></dt>'
            '<dd><span class="type">table</span> Entries:<dl>',
            formatted)
        self.assertIn(
            '<dt class="api-lua-v2-type-definition">'
            '<code>inner:string</code></dt>\n<dd>A value.</dd>',
            formatted)
        self.assertEqual(2, formatted.count("<dl>"))
        self.assertEqual(2, formatted.count("</dl>"))


if __name__ == "__main__":
    unittest.main()
