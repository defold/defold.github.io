---
author: Defold Foundation
brief: This example shows how to use physics raycasts to detect collisions along a straight line from a start point to an end point.
category: physics
layout: example
opengraph_image: https://www.defold.com/examples/physics/raycast/raycast.png
path: physics/raycast
scripts: raycast.script
tags: physics
thumbnail: raycast.png
title: Raycast
twitter_image: https://www.defold.com/examples/physics/raycast/raycast.png

---

![raycast](raycast.png)

The setup consists of two different kinds of game objects.

bee
: The bee. Contains:
  - A *Sprite* component with the bee image.
  - A script that performs raycasts from the game object position to the position of mouse/touch input.

stone
: The square stone block. Contains:
  - A *Sprite* component with the stone block image.
  - A *Collision object* component with a group set to `stone`.