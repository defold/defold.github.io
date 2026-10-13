import ast
import json
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


class AssetFrontmatterTests(unittest.TestCase):
    def test_asset_metadata_survives_yaml_special_characters(self):
        source = (ROOT / "update.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        namespace = {"json": json}
        for node in tree.body:
            if isinstance(node, ast.Assign) and any(
                isinstance(target, ast.Name) and target.id == "ASSET_MD_FRONTMATTER"
                for target in node.targets
            ):
                namespace["ASSET_MD_FRONTMATTER"] = ast.literal_eval(node.value)
            if isinstance(node, ast.FunctionDef) and node.name == "asset_frontmatter":
                exec(ast.get_source_segment(source, node), namespace)
        description = 'Reflection modes: update every frame.\nIncludes "glass" # examples.'
        name = 'Defold Glass: Mirrors & "Reflections"'
        image = "https://defold.com/images/assets/defold-glass-thumb.webp"
        rendered = namespace["asset_frontmatter"]("defold-glass", name, description, image)
        metadata = yaml.safe_load(rendered.split("---", 2)[1])
        self.assertEqual(metadata["layout"], "asset")
        self.assertEqual(metadata["asset"], "defold-glass")
        self.assertEqual(metadata["title"], name)
        self.assertEqual(metadata["description"], description)
        self.assertEqual(metadata["opengraph_image"], image)
        self.assertEqual(metadata["twitter_image"], image)


if __name__ == "__main__":
    unittest.main()
