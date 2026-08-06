import ast
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


class UpdateImportBoundaryTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
