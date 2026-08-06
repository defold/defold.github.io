import tempfile
import unittest
from pathlib import Path

from example_scripts import (
    copy_example_scripts,
    example_include_name,
    find_example_scripts,
    resolve_example_script,
    resolve_example_scripts,
)


class ExampleScriptResolutionTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.project_dir = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def add_script(self, relative_path):
        path = self.project_dir / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("function init(self) end\n", encoding="utf-8")

    def test_unique_filename_is_found_anywhere_in_project(self):
        self.add_script("main/scroll_manager/scroll_item.script")
        available = find_example_scripts(self.project_dir)

        self.assertEqual(
            resolve_example_script("scroll_item.script", available),
            "main/scroll_manager/scroll_item.script",
        )

    def test_exact_path_is_supported_but_suffix_path_is_not(self):
        self.add_script("main/scroll_manager/scroll_item.script")
        available = find_example_scripts(self.project_dir)

        self.assertEqual(
            resolve_example_script("main/scroll_manager/scroll_item.script", available),
            "main/scroll_manager/scroll_item.script",
        )
        with self.assertRaisesRegex(ValueError, "does not exist"):
            resolve_example_script("scroll_manager/scroll_item.script", available)

    def test_ambiguous_filename_requires_an_exact_path(self):
        self.add_script("main/first/controller.script")
        self.add_script("main/second/controller.script")
        available = find_example_scripts(self.project_dir)

        with self.assertRaisesRegex(
            ValueError,
            "main/first/controller.script, main/second/controller.script",
        ):
            resolve_example_script("controller.script", available)

    def test_generated_and_dependency_directories_are_ignored(self):
        self.add_script("main/controller.script")
        self.add_script("build/controller.script")
        self.add_script(".internal/lib/controller.script")
        self.add_script("node_modules/package/controller.script")

        self.assertEqual(find_example_scripts(self.project_dir), ["main/controller.script"])

    def test_declared_path_controls_nested_include_name(self):
        self.add_script("main/scroll_manager/scroll_item.script")
        available = find_example_scripts(self.project_dir)
        includes_dir = self.project_dir / "includes"

        resolved = resolve_example_scripts("scroll_item.script", available)
        self.assertEqual(resolved, [("scroll_item.script", "main/scroll_manager/scroll_item.script")])
        self.assertEqual(example_include_name("scroll_item.script"), "scroll_item_script.md")
        self.assertEqual(
            example_include_name("main/scroll_manager/scroll_item.script"),
            "main/scroll_manager/scroll_item_script.md",
        )

        copy_example_scripts(self.project_dir, includes_dir, resolved)
        self.assertTrue((includes_dir / "scroll_item_script.md").is_file())

        nested = resolve_example_scripts("main/scroll_manager/scroll_item.script", available)
        copy_example_scripts(self.project_dir, includes_dir, nested)
        self.assertTrue((includes_dir / "main/scroll_manager/scroll_item_script.md").is_file())

    def test_unsafe_or_non_normalized_paths_are_rejected(self):
        for script in (
            "/main/controller.script",
            "./main/controller.script",
            "main/../controller.script",
            "main\\controller.script",
        ):
            with self.subTest(script=script), self.assertRaisesRegex(ValueError, "normalized"):
                resolve_example_script(script, [])


if __name__ == "__main__":
    unittest.main()
