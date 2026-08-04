---
author: Defold Foundation
authors:
- github: defold
  id: f0ed797e86f7025f8ba5455479852ca5
  name: Defold Foundation
brief: This example shows how to use a camera component and have it follow a game object. Click to toggle between following the game object and staying stationary.
category: render
layout: example
license: CC0-1.0
license_url: https://creativecommons.org/publicdomain/zero/1.0/
opengraph_image: https://www.defold.com/examples/render/camera/camera.png
path: render/camera
scripts: bee.script, camera.script
tags: render
thumbnail: camera.png
title: Camera
twitter_image: https://www.defold.com/examples/render/camera/camera.png
---

![camera](camera.png)

The setup consists of one `bee` game object that the camera can follow and one `camera` game object containing the camera component. The camera component will when active send view and projection updates to the render script.

bee
: The bee. Contains:
  - A *Sprite* component with the bee image.
  - A script that tells the camera whether it should follow the game object or not.

camera
: The camera. Contains:
  - A *Camera* component. The camera component has Orthographic Projection enabled.
  - A script that controls the camera component.
