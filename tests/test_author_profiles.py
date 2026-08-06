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
        profile_file = Path(temporary.name) / "authors.json"
        profile_file.write_text(json.dumps(records), encoding="utf-8")
        return AuthorRegistry.load(profile_file)

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
        self.assertEqual("/images/people/avatar_user_profile_male.png", DEFAULT_AVATAR)

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

    def test_profile_validation_rejects_malformed_or_duplicate_stable_ids(self):
        with self.assertRaisesRegex(AuthorProfileValidationError, "lowercase 32-character"):
            self.make_registry([{"name": "Alice", "id": "not-a-hash"}])
        stable_id = canonical_author_id("Original Name")
        with self.assertRaisesRegex(AuthorProfileValidationError, "Duplicate author id"):
            self.make_registry(
                [
                    {"name": "Alice", "id": stable_id},
                    {"name": "Bob", "id": stable_id},
                ]
            )

    def test_profile_validation_rejects_long_bio_and_http_links(self):
        with self.assertRaisesRegex(AuthorProfileValidationError, "bio must be"):
            self.make_registry([{"name": "Alice", "bio": "x" * 401}])
        with self.assertRaisesRegex(AuthorProfileValidationError, "https URL"):
            self.make_registry(
                [
                    {
                        "name": "Alice",
                        "links": [{"type": "website", "url": "http://example.com"}],
                    }
                ]
            )

    def test_profile_links_accept_custom_github_and_external_titles(self):
        registry = self.make_registry(
            [
                {
                    "name": "Alice",
                    "links": [
                        {
                            "type": "github",
                            "label": "Defold projects",
                            "url": "https://github.com/alice/defold-projects",
                        },
                        {
                            "type": "external",
                            "label": "Portfolio",
                            "url": "https://example.com/alice",
                        },
                    ],
                }
            ]
        )
        profile = registry.resolve("Alice")
        self.assertEqual(["Defold projects", "Portfolio"], [link["label"] for link in profile["links"]])

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
            (root / "_data" / "assets").mkdir(parents=True)
            profiles = [
                {"name": "Alice", "aliases": ["A"]},
                {"name": "Bob"},
                {"name": "Carol"},
            ]
            (root / "_data" / "authors.json").write_text(
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
            (root / "_data" / "authors").mkdir()
            (root / "_data" / "authors" / "legacy.json").write_text("{}", encoding="utf-8")
            (root / "_data" / "authorindex.json").write_text("[]", encoding="utf-8")

            generated = generate_author_outputs(root, sync_example_pages=False)
            by_name = {author["name"]: author for author in generated}
            self.assertEqual((1, 1), (by_name["Alice"]["asset_count"], by_name["Alice"]["example_count"]))
            self.assertEqual((0, 1), (by_name["Bob"]["asset_count"], by_name["Bob"]["example_count"]))
            self.assertEqual((1, 0), (by_name["Carol"]["asset_count"], by_name["Carol"]["example_count"]))
            self.assertEqual(1, by_name["Mystery"]["asset_count"])

            alias_page = root / "authors" / f"{canonical_author_id('A')}.md"
            self.assertTrue(alias_page.is_file())
            self.assertIn(f"canonical: /authors/{canonical_author_id('Alice')}/", alias_page.read_text())
            self.assertIn(f"author_id: {canonical_author_id('Alice')}", alias_page.read_text())
            self.assertIn("author_name: \"Alice\"", alias_page.read_text())
            self.assertFalse((root / "_data" / "authorindex.json").exists())
            self.assertFalse((root / "_data" / "authors").exists())
            self.assertEqual(profiles, json.loads((root / "_data" / "authors.json").read_text()))

            generated_asset = json.loads(
                (root / "_data" / "assets" / "alice-asset.json").read_text()
            )
            self.assertEqual("Alice", generated_asset["author"])
            self.assertEqual(canonical_author_id("Alice"), generated_asset["author_id"])

    def test_current_registry_covers_all_generated_source_names(self):
        root = Path(__file__).resolve().parents[1]
        registry = AuthorRegistry.load(root / "_data" / "authors.json")
        source_names = []
        for asset_path in (root / "_data" / "assets").glob("*.json"):
            source_names.append(json.loads(asset_path.read_text(encoding="utf-8"))["author"])
        examples = json.loads((root / "_data" / "examplesindex.json").read_text(encoding="utf-8"))
        for example in examples:
            source_names.extend(example_author_names(example, registry))
        missing = sorted({name for name in source_names if not registry.is_registered(name)})
        self.assertEqual([], missing)
        self.assertIn("develops and maintains Defold", registry.resolve("Defold Foundation")["bio"])

    def test_insality_keeps_existing_hash(self):
        root = Path(__file__).resolve().parents[1]
        registry = AuthorRegistry.load(root / "_data" / "authors.json")
        self.assertEqual(
            "fdec556e51a2ad846db08b8ba0ae3b86",
            registry.resolve("Insality")["id"],
        )
        self.assertEqual(
            registry.resolve("Insality")["id"],
            registry.resolve("Maxim Tuprikov")["id"],
        )
        self.assertEqual(
            registry.resolve("Insality")["id"],
            registry.resolve("Maksim Tuprikov")["id"],
        )

    def test_defold_foundation_keeps_original_name_and_hash(self):
        root = Path(__file__).resolve().parents[1]
        registry = AuthorRegistry.load(root / "_data" / "authors.json")
        foundation = registry.resolve("The Defold Foundation")
        self.assertEqual("The Defold Foundation", foundation["name"])
        self.assertEqual("41055a22bd3f5b94c6182d496d7083e7", foundation["id"])
        self.assertEqual(foundation["id"], registry.resolve("Defold Foundation")["id"])
        self.assertEqual(foundation["id"], registry.resolve("Defold")["id"])

    def test_generated_assets_use_registry_canonical_names_and_ids(self):
        root = Path(__file__).resolve().parents[1]
        registry = AuthorRegistry.load(root / "_data" / "authors.json")
        for asset_path in (root / "_data" / "assets").glob("*.json"):
            asset = json.loads(asset_path.read_text(encoding="utf-8"))
            profile = registry.resolve(asset["author"])
            self.assertEqual(profile["name"], asset["author"], asset_path.name)
            self.assertEqual(profile["id"], asset["author_id"], asset_path.name)

    def test_generated_examples_use_registry_canonical_names_and_ids(self):
        root = Path(__file__).resolve().parents[1]
        registry = AuthorRegistry.load(root / "_data" / "authors.json")
        examples = json.loads((root / "_data" / "examplesindex.json").read_text(encoding="utf-8"))
        for example in examples:
            canonical_names = []
            for author in example["authors"]:
                profile = registry.resolve(author["name"])
                self.assertEqual(profile["name"], author["name"], example["path"])
                self.assertEqual(profile["id"], author["id"], example["path"])
                canonical_names.append(profile["name"])
            self.assertEqual(", ".join(canonical_names), example["author"], example["path"])

    def test_every_asset_and_example_author_link_has_a_generated_page(self):
        root = Path(__file__).resolve().parents[1]
        referenced_ids = set()
        for asset_path in (root / "_data" / "assets").glob("*.json"):
            asset = json.loads(asset_path.read_text(encoding="utf-8"))
            referenced_ids.add(asset["author_id"])
        examples = json.loads((root / "_data" / "examplesindex.json").read_text(encoding="utf-8"))
        for example in examples:
            referenced_ids.update(author["id"] for author in example["authors"])

        missing_pages = sorted(
            author_id
            for author_id in referenced_ids
            if not (root / "authors" / f"{author_id}.md").is_file()
        )
        self.assertEqual([], missing_pages)

    def test_generated_compatibility_pages_target_merged_profiles(self):
        root = Path(__file__).resolve().parents[1]
        aliases = {
            "Maxim Tuprikov": "Insality",
            "Maksim Tuprikov": "Insality",
            "AGulev": "Alexey Gulev",
            "agulev": "Alexey Gulev",
            "Defold": "The Defold Foundation",
            "Defold Foundation": "The Defold Foundation",
        }
        for alias, canonical in aliases.items():
            page = root / "authors" / f"{canonical_author_id(alias)}.md"
            self.assertTrue(page.is_file(), alias)
            content = page.read_text(encoding="utf-8")
            self.assertIn(f"author_id: {canonical_author_id(canonical)}", content)
            self.assertIn(f"canonical: /authors/{canonical_author_id(canonical)}/", content)

    def test_moon_active_keeps_rebranded_metadata_and_stable_url(self):
        root = Path(__file__).resolve().parents[1]
        registry = AuthorRegistry.load(root / "_data" / "authors.json")
        moon_active = registry.resolve("Moon Active")
        self.assertEqual("3df1fd354e03720134efea0ecae165f8", moon_active["id"])
        self.assertEqual(moon_active["id"], registry.resolve("Family Age")["id"])
        self.assertEqual(moon_active["id"], registry.resolve("Melsoft Games")["id"])
        self.assertIn("acquired by Moon Active", moon_active["bio"])
        self.assertEqual("https://www.moonactive.com", moon_active["links"][0]["url"])


if __name__ == "__main__":
    unittest.main()
