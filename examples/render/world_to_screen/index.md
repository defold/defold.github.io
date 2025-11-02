---
author: Artsiom Trubchyk
brief: This example demonstrates how to convert 3D world coordinates to 2D screen coordinates using camera transformations.
category: render
layout: example
opengraph_image: https://www.defold.com/examples/render/world_to_screen/thumbnail.png
path: render/world_to_screen
scripts: player.script
tags: render
thumbnail: thumbnail.png
title: World to Screen
twitter_image: https://www.defold.com/examples/render/world_to_screen/thumbnail.png

---

This example shows how to convert world positions to screen coordinates for UI positioning. It features:

* A `world_to_screen()` function that transforms 3D world positions to 2D screen coordinates using the camera's view and projection matrices.
* A ghost character that rotates around a crypt in 3D space while floating up and down.
* A player name label in the GUI that follows the character's world position by converting it to screen coordinates.
* Demonstrates practical use of world-to-screen conversion for positioning UI elements relative to 3D objects.