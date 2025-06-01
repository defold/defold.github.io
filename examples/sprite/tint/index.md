---
author: Defold Foundation
brief: This example shows how tint a sprite at run-time
category: sprite
layout: example
opengraph_image: https://www.defold.com/examples/sprite/tint/bunntint_thumb.png
path: sprite/tint
scripts: tint.script
tags: sprite
thumbnail: bunntint_thumb.png
title: Sprite tint
twitter_image: https://www.defold.com/examples/sprite/tint/bunntint_thumb.png

---

The example uses a script to tint (color) sprites in a couple of different ways. The tint is a fragment constant on the sprite material and it is used in the sprite.fp fragment shader program to modify the color sampled from the texture.

It is important to keep in mind that each tinted sprite generates a new draw call since a modified tint value will break the built in draw call batching in Defold.

![tint](tint.png)

![sprite material](spritematerial.png)