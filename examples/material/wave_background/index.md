---
author: JuLongZhiLu(巨龙之路), Brian Kramer
authors:
- id: 8ce6b18f49fadbbf198cf2f6ec7243c6
  name: JuLongZhiLu(巨龙之路)
- github: subsoap
  id: 4e5137947a2d2210327998871d8dd3c7
  name: Brian Kramer
brief: Shows how to use a Time shader constant to achieve a moving wave effect
category: material
layout: example
license: CC0-1.0
license_url: https://creativecommons.org/publicdomain/zero/1.0/
opengraph_image: https://www.defold.com/examples/material/wave_background/thumbnail.png
path: material/wave_background
scripts: wave_background.fp
tags: material
thumbnail: thumbnail.png
title: Wave Background
twitter_image: https://www.defold.com/examples/material/wave_background/thumbnail.png
---

This example contains a game object with a sprite component. The `Image` and `Default Animation properties` of the sprite component cannot be left empty, otherwise an error will occur. In the example the built-in `/builtins/graphics/particle_blob.tilesource` is used and animation is set to `anim`. You can adjust the size of the wave background by modifying the `Size` property of the sprite component.

Example uses a Fragment Constant of type `Time` introduced in Defold 1.12.3.

![image](image.png)
