import json
import tempfile
import unittest
from pathlib import Path

from scripts.author_profiles import (
    DEFAULT_AVATAR,
    DEFAULT_EXAMPLE_LICENSE,
    AuthorProfileValidationError,
    AuthorRegistry,
    canonical_author_id,
    enrich_example,
    example_author_names,
    generate_author_outputs,
)


class AuthorProfileTestCase(unittest.TestCase):
    def make_registry(self, records):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        profile_dir = Path(temporary.name)
        (profile_dir / "profiles.json").write_text(json.dumps(records), encoding="utf-8")
        return AuthorRegistry.load(profile_dir)

    def test_resolves_canonical_github_alias_and_case_insensitively(self):
        registry = self.make_registry(
            [
                {
                    "name": "Alexey Gulev",
                    "github": "AGulev",
                    "aliases": ["agulev", "Alex Gulev"],
                }
            ]
        )
        expected_id = canonical_author_id("Alexey Gulev")
        for identity in ("Alexey Gulev", "alexey gulev", "AGulev", "agulev", "ALEX GULEV"):
            self.assertEqual(expected_id, registry.resolve(identity)["id"])

    def test_unknown_author_gets_stable_minimal_profile(self):
        registry = self.make_registry([{"name": "Known"}])
        first = registry.resolve("New Contributor")
        second = registry.resolve("new contributor")
        self.assertEqual(first["id"], second["id"])
        self.assertEqual("New Contributor", first["name"])
        self.assertEqual([], first["links"])
        self.assertEqual([], first["support"])

    def test_preferred_multiple_authors_are_resolved_and_deduplicated(self):
        registry = self.make_registry(
            [
                {"name": "Alice", "aliases": ["A"]},
                {"name": "Bob", "github": "bob-dev"},
            ]
        )
        example = enrich_example(
            {"title": "Example", "authors": ["A", "bob-dev", "Alice"]}, registry
        )
        self.assertEqual(["Alice", "Bob"], [author["name"] for author in example["authors"]])
        self.assertEqual("Alice, Bob", example["author"])

    def test_legacy_comma_separated_authors_are_supported(self):
        registry = self.make_registry([{"name": "Alice"}, {"name": "Bob"}])
        self.assertEqual(
            ["Alice", "Bob"],
            example_author_names({"author": "Alice, Bob"}, registry),
        )

    def test_default_and_custom_example_licenses(self):
        registry = self.make_registry([{"name": "Alice"}])
        default = enrich_example({"author": "Alice"}, registry)
        custom = enrich_example({"author": "Alice", "license": "MIT"}, registry)
        self.assertEqual(DEFAULT_EXAMPLE_LICENSE, default["license"])
        self.assertIn("license_url", default)
        self.assertEqual("MIT", custom["license"])
        self.assertNotIn("license_url", custom)

    def test_profile_validation_rejects_ambiguous_aliases(self):
        with self.assertRaisesRegex(AuthorProfileValidationError, "Duplicate author identity"):
            self.make_registry(
                [
                    {"name": "Alice", "aliases": ["shared"]},
                    {"name": "Bob", "aliases": ["SHARED"]},
                ]
            )

    def test_profile_validation_rejects_long_bio_and_http_links(self):
        with self.assertRaisesRegex(AuthorProfileValidationError, "bio must be"):
            self.make_registry([{"name": "Alice", "bio": "x" * 281}])
        with self.assertRaisesRegex(AuthorProfileValidationError, "https URL"):
            self.make_registry(
                [
                    {
                        "name": "Alice",
                        "links": [{"type": "website", "url": "http://example.com"}],
                    }
                ]
            )

    def test_profile_validation_rejects_unsafe_support_destination(self):
        with self.assertRaisesRegex(AuthorProfileValidationError, "not an allowed"):
            self.make_registry(
                [
                    {
                        "name": "Alice",
                        "support": [
                            {
                                "type": "github_sponsors",
                                "url": "https://example.com/sponsors/alice",
                            }
                        ],
                    }
                ]
            )

    def test_profile_validation_rejects_malformed_fields(self):
        with self.assertRaisesRegex(AuthorProfileValidationError, "aliases must be an array"):
            self.make_registry([{"name": "Alice", "aliases": "A"}])
        with self.assertRaisesRegex(AuthorProfileValidationError, "at most three"):
            self.make_registry(
                [
                    {
                        "name": "Alice",
                        "support": [
                            {"type": "ko_fi", "url": f"https://ko-fi.com/a{index}"}
                            for index in range(4)
                        ],
                    }
                ]
            )

    def test_aggregation_handles_asset_example_combined_and_unknown_authors(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "author_profiles").mkdir(parents=True)
            (root / "_data" / "assets").mkdir(parents=True)
            profiles = [
                {"name": "Alice", "aliases": ["A"]},
                {"name": "Bob"},
                {"name": "Carol"},
            ]
            (root / "author_profiles" / "profiles.json").write_text(
                json.dumps(profiles), encoding="utf-8"
            )
            assets = {
                "alice-asset": {"author": "A", "stars": 4},
                "carol-asset": {"author": "Carol", "stars": 2},
                "mystery-asset": {"author": "Mystery"},
            }
            for asset_id, asset in assets.items():
                (root / "_data" / "assets" / f"{asset_id}.json").write_text(
                    json.dumps(asset), encoding="utf-8"
                )
            examples = [
                {
                    "authors": ["Alice", "Bob", "Alice"],
                    "brief": "Shared example",
                    "path": "test/shared",
                    "title": "Shared",
                }
            ]
            (root / "_data" / "examplesindex.json").write_text(
                json.dumps(examples), encoding="utf-8"
            )

            generated = generate_author_outputs(root, sync_example_pages=False)
            by_name = {author["name"]: author for author in generated}
            self.assertEqual((1, 1), (len(by_name["Alice"]["assets"]), len(by_name["Alice"]["examples"])))
            self.assertEqual((0, 1), (len(by_name["Bob"]["assets"]), len(by_name["Bob"]["examples"])))
            self.assertEqual((1, 0), (len(by_name["Carol"]["assets"]), len(by_name["Carol"]["examples"])))
            self.assertEqual(1, len(by_name["Mystery"]["assets"]))
            self.assertEqual(DEFAULT_AVATAR, by_name["Mystery"]["avatar_url"])

            alias_page = root / "authors" / f"{canonical_author_id('A')}.md"
            self.assertTrue(alias_page.is_file())
            self.assertIn(f"canonical: /authors/{canonical_author_id('Alice')}/", alias_page.read_text())
            self.assertIn(f"author: {canonical_author_id('A')}", alias_page.read_text())
            alias_data = json.loads(
                (root / "_data" / "authors" / f"{canonical_author_id('A')}.json").read_text()
            )
            self.assertEqual(canonical_author_id("A"), alias_data["id"])

            generated_asset = json.loads(
                (root / "_data" / "assets" / "alice-asset.json").read_text()
            )
            self.assertEqual(canonical_author_id("A"), generated_asset["author_id"])

    def test_current_registry_covers_all_generated_source_names(self):
        root = Path(__file__).resolve().parents[1]
        registry = AuthorRegistry.load(root / "author_profiles")
        source_names = []
        for asset_path in (root / "_data" / "assets").glob("*.json"):
            source_names.append(json.loads(asset_path.read_text(encoding="utf-8"))["author"])
        examples = json.loads((root / "_data" / "examplesindex.json").read_text(encoding="utf-8"))
        for example in examples:
            source_names.extend(example_author_names(example, registry))
        missing = sorted({name for name in source_names if not registry.is_registered(name)})
        self.assertEqual([], missing)

    def test_insality_keeps_existing_hash(self):
        root = Path(__file__).resolve().parents[1]
        registry = AuthorRegistry.load(root / "author_profiles")
        self.assertEqual(
            "fdec556e51a2ad846db08b8ba0ae3b86",
            registry.resolve("Insality")["id"],
        )
        self.assertEqual(
            registry.resolve("Insality")["id"],
            registry.resolve("Maxim Tuprikov")["id"],
        )

    def test_generated_assets_keep_legacy_source_name_hashes(self):
        root = Path(__file__).resolve().parents[1]
        for asset_path in (root / "_data" / "assets").glob("*.json"):
            asset = json.loads(asset_path.read_text(encoding="utf-8"))
            self.assertEqual(
                canonical_author_id(asset["author"]),
                asset["author_id"],
                asset_path.name,
            )

        expected_legacy_ids = {
            "Defold": "7a2340205545b175e20f44488bd30a49",
            "Maxim Tuprikov": "1b1571ed4750bae48c69aa21ab265ef2",
            "The Defold Foundation": "41055a22bd3f5b94c6182d496d7083e7",
        }
        for name, expected_id in expected_legacy_ids.items():
            self.assertEqual(expected_id, canonical_author_id(name))

    def test_generated_compatibility_pages_target_merged_profiles(self):
        root = Path(__file__).resolve().parents[1]
        aliases = {
            "Maxim Tuprikov": "Insality",
            "AGulev": "Alexey Gulev",
            "agulev": "Alexey Gulev",
            "Defold": "Defold Foundation",
            "The Defold Foundation": "Defold Foundation",
        }
        for alias, canonical in aliases.items():
            page = root / "authors" / f"{canonical_author_id(alias)}.md"
            self.assertTrue(page.is_file(), alias)
            content = page.read_text(encoding="utf-8")
            self.assertIn(f"author: {canonical_author_id(alias)}", content)
            self.assertIn(f"canonical: /authors/{canonical_author_id(canonical)}/", content)
            alias_data = root / "_data" / "authors" / f"{canonical_author_id(alias)}.json"
            self.assertTrue(alias_data.is_file(), alias)


if __name__ == "__main__":
    unittest.main()
