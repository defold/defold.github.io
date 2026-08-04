---
author: Defold Foundation
authors:
- github: defold
  id: f0ed797e86f7025f8ba5455479852ca5
  name: Defold Foundation
brief: This example shows how to speed up or slow down animations in a collection proxy by changing the time step of the collection proxy.
category: collection
layout: example
license: CC0-1.0
license_url: https://creativecommons.org/publicdomain/zero/1.0/
opengraph_image: https://www.defold.com/examples/collection/timestep/thumbnail.png
path: collection/timestep
scripts: controller.script, game.script
tags: collection
thumbnail: thumbnail.png
title: Time-step
twitter_image: https://www.defold.com/examples/collection/timestep/thumbnail.png
---

The setup consists of a `timestep.collection` and a `game.collection`.

timestep.collection
: This is the bootstrap collection specified in `game.project`. Contains:
  - A *Script* that handles loading of the `game.collection` and controls the time-step of `game.collection` using the `set_time_step` message.

game.collection
: This collection contains a "game" with some animated game objects. Contains:
  - Five animated game objects that are animated using `go.animate()`
  - A *Script* that starts the game object animations and lets the user control the time-step through messages sent to the *Script* in the `timestep.collection`.
