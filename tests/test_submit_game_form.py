import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FORM = (ROOT / "submit_game.html").read_text(encoding="utf-8")


class SubmitGameFormTests(unittest.TestCase):
    def test_generated_metadata_matches_showcase_submission_contract(self):
        for field in (
            "name",
            "description",
            "url",
            "developer",
            "publisher",
            "releasedate",
            "platforms",
            "images",
        ):
            self.assertRegex(FORM, rf"\n\s*{field}: ")

        for obsolete_field in ("id", "tags", "downloads", "license", "showcase"):
            self.assertNotRegex(FORM, rf"\n\s*{obsolete_field}: ")

    def test_asset_tags_and_legacy_inputs_are_not_exposed(self):
        self.assertNotIn("site.asset_allowed_tags", FORM)
        self.assertNotIn('name="tags"', FORM)
        self.assertNotIn("game_downloads", FORM)
        self.assertNotIn("game_license", FORM)

    def test_required_game_url_and_platform_validation_are_present(self):
        self.assertRegex(
            FORM,
            r'<input id="game_url" type="url" name="url"[^>]* required>',
        )
        self.assertIn("Select at least one platform.", FORM)

    def test_platform_selection_clears_previous_validation_error(self):
        self.assertRegex(
            FORM,
            r'<fieldset[^>]*onchange="showcase_clear_platform_validation\(\)"[^>]*>'
            r'\s*<legend>Platforms</legend>',
        )
        clear_validation = re.search(
            r"function showcase_clear_platform_validation\(\) \{(.*?)\n\s*\}",
            FORM,
            re.DOTALL,
        )
        self.assertIsNotNone(clear_validation)
        self.assertIn('setCustomValidity("")', clear_validation.group(1))

    def test_issue_targets_games_showcase_and_requests_webp_roles(self):
        self.assertIn(
            "https://github.com/defold/games-showcase/issues/new",
            FORM,
        )
        for role, dimensions in (
            ("full", "2000x750"),
            ("half", "1200x600"),
            ("third", "800x600"),
        ):
            self.assertIn(f'"- {role}, {dimensions}: "', FORM)
            self.assertIn(f'slug + "-{role}.webp"', FORM)


if __name__ == "__main__":
    unittest.main()
