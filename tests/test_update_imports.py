import ast
import contextlib
import io
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import yaml
from PIL import Image
from scripts.frontpage_images import regenerate_game_images


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


def load_image_copier():
    namespace = {"os": os, "Path": Path, "shutil": shutil}
    for name in ("games_showcase_root", "copy_game_images"):
        exec(function_source(name), namespace)
    return namespace["copy_game_images"]


@contextlib.contextmanager
def working_directory(path):
    previous = Path.cwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(previous)


def load_game_importer(games_json: Path, featured_json: Path):
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
        "copy_game_images": load_image_copier(),
        "regenerate_game_images": regenerate_game_images,
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

    def test_ci_refreshes_showcase_only_on_explicit_update(self):
        build_workflow = (ROOT / ".github/workflows/build_site.yml").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("--download", build_workflow)

        update_workflow = (ROOT / ".github/workflows/update_site.yml").read_text(
            encoding="utf-8"
        )
        steps = yaml.safe_load(update_workflow)["jobs"]["update_site"]["steps"]
        self.assertEqual(
            [step for step in steps if "game" in step.get("run", "")],
            [{
                "if": "env.ACTION == 'games-showcase'",
                "name": "Update games",
                "run": "python update.py --download games-showcase",
            }],
        )
        self.assertNotIn("/images/games/", (ROOT / ".gitignore").read_text())


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
            Image.new("RGB", (800, 600), "red").save(images / filename, "WEBP")
        write_json(source / "games_order.json", ["beta", "alpha"])
        write_json(source / "showcase_featured_full.json", ["alpha"])
        return source

    def run_import(self, root: Path):
        games_output = root / "output" / "games.json"
        featured_output = root / "output" / "featured.json"
        games_output.parent.mkdir(exist_ok=True)
        importer = load_game_importer(games_output, featured_output)
        with working_directory(root), contextlib.redirect_stdout(io.StringIO()):
            importer(str(root))
        return (
            json.loads(games_output.read_text(encoding="utf-8")),
            json.loads(featured_output.read_text(encoding="utf-8")),
        )

    def test_import_uses_upstream_order_featured_and_images(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.make_source(root)

            games, featured = self.run_import(root)

            self.assertEqual([game["id"] for game in games], ["beta", "alpha"])
            self.assertEqual(featured, ["alpha"])
            self.assertEqual(
                {path.name for path in (root / "images" / "games").iterdir()},
                {"alpha-full.webp", "alpha-third.webp", "beta-half.webp",
                 "alpha-third-256w.webp", "alpha-third-384w.webp", "alpha-third-512w.webp"},
            )

    def test_import_rejects_featured_list_different_from_full_games(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self.make_source(root)
            write_json(source / "showcase_featured_full.json", [])

            with self.assertRaisesRegex(RuntimeError, "Featured IDs must exactly match"):
                self.run_import(root)

    def test_images_copy_only_changed_references_and_prune_obsolete_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self.make_source(root) / "games" / "images"
            (source / "unused.webp").write_bytes(b"unused upstream image")
            destination = root / "images" / "games"
            destination.mkdir(parents=True)
            (destination / "alpha-full.webp").write_bytes((source / "alpha-full.webp").read_bytes())
            # Same size and timestamp must not hide changed image content.
            (destination / "alpha-third.webp").write_bytes(bytes((source / "alpha-third.webp").stat().st_size))
            timestamp = (source / "alpha-third.webp").stat().st_mtime_ns
            os.utime(destination / "alpha-third.webp", ns=(timestamp, timestamp))
            (destination / "obsolete.webp").write_bytes(b"old image")

            with mock.patch.object(shutil, "copyfile", wraps=shutil.copyfile) as copy:
                self.run_import(root)

            self.assertEqual(
                {Path(call.args[1]).name for call in copy.call_args_list},
                {"alpha-third.webp", "beta-half.webp"},
            )
            self.assertEqual(
                {path.name for path in destination.iterdir()},
                {"alpha-full.webp", "alpha-third.webp", "beta-half.webp",
                 "alpha-third-256w.webp", "alpha-third-384w.webp", "alpha-third-512w.webp"},
            )
            for path in source.iterdir():
                if path.name != "unused.webp":
                    self.assertEqual((destination / path.name).read_bytes(), path.read_bytes())

            with working_directory(root), mock.patch.object(shutil, "copyfile") as copy:
                load_image_copier()(str(root), {"alpha-full.webp", "alpha-third.webp", "beta-half.webp"})
            copy.assert_not_called()

    def test_repeated_import_regenerates_variants_and_replaces_game_manifest_entries(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self.make_source(root)
            manifest_path = root / "_data/responsive_images.json"
            unrelated = {"/images/editor/editor.webp": "/images/editor/editor-350w.webp 350w"}
            write_json(manifest_path, {**unrelated, "/images/games/deleted.webp": "/missing.webp 256w"})
            self.run_import(root)
            variant = root / "images/games/alpha-third-256w.webp"
            before = variant.read_bytes()

            # The importer prunes all variants; changed originals must generate
            # fresh image content, with no stale or missing manifest candidates.
            Image.new("RGB", (800, 600), "blue").save(source / "games/images/alpha-third.webp", "WEBP")
            self.run_import(root)
            self.assertNotEqual(variant.read_bytes(), before)
            manifest = json.loads(manifest_path.read_text())
            self.assertEqual(set(manifest), {*unrelated, "/images/games/alpha-third.webp"})
            self.assertEqual(manifest["/images/editor/editor.webp"], unrelated["/images/editor/editor.webp"])
            for candidate in manifest["/images/games/alpha-third.webp"].split(", "):
                url, width = candidate.split()
                with Image.open(root / url.lstrip("/")) as image:
                    self.assertEqual(image.width, int(width[:-1]))

            # Removing a full showcase game also removes its manifest entries
            # and variants, rather than preserving URLs for obsolete images.
            (source / "games/alpha.json").unlink()
            write_json(source / "games_order.json", ["beta"])
            write_json(source / "showcase_featured_full.json", [])
            self.run_import(root)
            self.assertEqual(json.loads(manifest_path.read_text()), unrelated)
            self.assertEqual([p.name for p in (root / "images/games").iterdir()], ["beta-half.webp"])

    def test_missing_image_does_not_change_existing_snapshots(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = self.make_source(root)
            self.run_import(root)
            snapshots = {
                path: path.read_bytes()
                for directory in (root / "output", root / "images", root / "_data")
                for path in directory.rglob("*") if path.is_file()
            }
            (source / "games" / "images" / "alpha-third.webp").unlink()
            (source / "games" / "images" / "alpha-full.webp").write_bytes(b"new")
            importer = load_game_importer(
                root / "output" / "games.json", root / "output" / "featured.json"
            )
            with working_directory(root), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(RuntimeError, "Missing showcase images"):
                    importer(str(root))
            for path, content in snapshots.items():
                self.assertEqual(path.read_bytes(), content)


if __name__ == "__main__":
    unittest.main()
