import ast
import contextlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UPDATE_SOURCE = (ROOT / "update.py").read_text(encoding="utf-8")
UPDATE_TREE = ast.parse(UPDATE_SOURCE)


def function_source(name: str) -> str:
    node = next(
        item
        for item in UPDATE_TREE.body
        if isinstance(item, ast.FunctionDef) and item.name == name
    )
    return ast.get_source_segment(UPDATE_SOURCE, node)


def load_game_importer(games_json: Path, featured_json: Path, copy_calls: list):
    def find_files(root_dir, pattern):
        return sorted(str(path) for path in Path(root_dir).rglob(pattern))

    def read_as_json(path):
        return json.loads(Path(path).read_text(encoding="utf-8"))

    def write_as_json(path, value, ensure_ascii=True):
        Path(path).write_text(
            json.dumps(value, indent=4, sort_keys=True, ensure_ascii=ensure_ascii),
            encoding="utf-8",
        )

    namespace = {
        "os": os,
        "find_files": find_files,
        "read_as_json": read_as_json,
        "write_as_json": write_as_json,
        "copy_game_images": lambda tmp_dir: copy_calls.append(Path(tmp_dir)),
        "GAMES_JSON": str(games_json),
        "SHOWCASE_FEATURED_FULL_JSON": str(featured_json),
    }
    for name in ("games_showcase_root", "process_games"):
        exec(function_source(name), namespace)
    return namespace["process_games"]


def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


class UpdateImportBoundaryTests(unittest.TestCase):
    def test_generated_catalogs_preserve_only_stable_attribution(self):
        assets = [
            json.loads(path.read_text(encoding="utf-8"))
            for path in (ROOT / "_data" / "assets").glob("*.json")
        ]
        examples = json.loads(
            (ROOT / "_data" / "examplesindex.json").read_text(encoding="utf-8")
        )

        self.assertTrue(all("author_id" in asset for asset in assets))
        self.assertTrue(all("author" not in asset for asset in assets))
        self.assertTrue(all(item.get("author_ids") for item in examples))
        self.assertTrue(
            all("author" not in item and "authors" not in item for item in examples)
        )
        self.assertTrue(all("license_url" not in item for item in examples))

    def test_author_enrichment_is_not_part_of_imports(self):
        self.assertNotIn("author_profiles", UPDATE_SOURCE)
        self.assertNotIn("enrich_example", UPDATE_SOURCE)
        self.assertNotIn("generate_author_outputs", UPDATE_SOURCE)

    def test_asset_and_example_importers_are_independent(self):
        self.assertNotIn("examplesindex", function_source("process_assets"))
        self.assertNotIn("_data/assets", function_source("process_examples"))

    def test_all_does_not_commit_implicitly(self):
        expansion = UPDATE_SOURCE.split('if "all" in args.commands:', 1)[1].split(
            "for command in args.commands:", 1
        )[0]
        self.assertIn('commands.remove("commit")', expansion)
        self.assertNotIn('commands.append("commit")', expansion)

    def test_ci_commits_only_after_complete_validation(self):
        workflow = (ROOT / ".github/workflows/update_site.yml").read_text(
            encoding="utf-8"
        )
        build = workflow.index("name: Build Jekyll site")
        pagefind = workflow.index("name: Index site with Pagefind")
        commit = workflow.index("name: Commit generated site")
        self.assertLess(build, pagefind)
        self.assertLess(pagefind, commit)

    def test_ci_downloads_showcase_images_before_each_build(self):
        build_workflow = (ROOT / ".github/workflows/build_site.yml").read_text(
            encoding="utf-8"
        )
        self.assertLess(
            build_workflow.index("name: Download showcase images"),
            build_workflow.index("name: Build Jekyll site"),
        )

        update_workflow = (ROOT / ".github/workflows/update_site.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn("python update.py --download games-showcase", update_workflow)
        self.assertIn("python update.py --download game-images", update_workflow)


class GamesShowcaseImportTests(unittest.TestCase):
    def make_source(self, root: Path):
        source = root / "games-showcase-master"
        images = source / "games" / "images"
        images.mkdir(parents=True)
        games = {
            "alpha": {
                "name": "Alpha",
                "showcase": "full",
                "images": {"full": "alpha-full.webp", "third": "alpha-third.webp"},
            },
            "beta": {
                "name": "Beta",
                "showcase": "half",
                "images": {"half": "beta-half.webp"},
            },
        }
        for game_id, game in games.items():
            write_json(source / "games" / f"{game_id}.json", game)
        for filename in ("alpha-full.webp", "alpha-third.webp", "beta-half.webp"):
            (images / filename).write_bytes(b"fixture")
        write_json(source / "games_order.json", ["beta", "alpha"])
        write_json(source / "showcase_featured_full.json", ["alpha"])
        return source

    def run_import(self, root: Path):
        games_output = root / "output" / "games.json"
        featured_output = root / "output" / "featured.json"
        games_output.parent.mkdir()
        copy_calls = []
        importer = load_game_importer(games_output, featured_output, copy_calls)
        with contextlib.redirect_stdout(io.StringIO()):
            importer(str(root))
        return (
            json.loads(games_output.read_text(encoding="utf-8")),
            json.loads(featured_output.read_text(encoding="utf-8")),
            copy_calls,
        )

    def test_import_uses_upstream_order_featured_and_images(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.make_source(root)

            games, featured, copy_calls = self.run_import(root)

            self.assertEqual([game["id"] for game in games], ["beta", "alpha"])
            self.assertEqual(featured, ["alpha"])
            self.assertEqual(copy_calls, [root])

    def test_import_rejects_missing_referenced_image(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self.make_source(root)
            (source / "games" / "images" / "alpha-full.webp").unlink()

            with self.assertRaisesRegex(RuntimeError, "Missing showcase images"):
                self.run_import(root)

    def test_import_rejects_featured_list_different_from_full_games(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self.make_source(root)
            write_json(source / "showcase_featured_full.json", [])

            with self.assertRaisesRegex(RuntimeError, "Featured IDs must exactly match"):
                self.run_import(root)


if __name__ == "__main__":
    unittest.main()
