---
author: Defold Foundation
brief: This example shows how to get local UV coordinates of a sprite regardless of sprite size
category: material
layout: example
opengraph_image: https://www.defold.com/examples/material/sprite_local_uv/example.png
path: material/sprite_local_uv
scripts: sprite_local_uv.script, sprite_local_uv.vp, sprite_local_uv.fp
tags: sprite
thumbnail: example.png
title: Sprite local UV
twitter_image: https://www.defold.com/examples/material/sprite_local_uv/example.png

---

The example uses two game objects, each with a sprite component and a script.

![example](example.png)

The sprite component uses a custom sprite material `sprite_local_uv.material` with `local_position` and `sprite_size` as two vertex attributes. The `local_position` attribute is of semantic type "Position" and coordinate space "Local" while the `sprite_size` attribute is of semantic type "User" and will be set by the script.

![material](material.png)

The script gets the size of the sprite and sets it as the `sprite_size` vertex attribute.