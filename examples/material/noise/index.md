---
author: The Defold Foundation
authors:
- github: defold
  id: 41055a22bd3f5b94c6182d496d7083e7
  name: The Defold Foundation
brief: This example shows how to use a noise function to generate clouds, smoke or similar effect using a shader.
category: material
layout: example
license: CC0-1.0
license_url: https://creativecommons.org/publicdomain/zero/1.0/
opengraph_image: https://www.defold.com/examples/material/noise/stretched-mesh.png
path: material/noise
scripts: noise.script, noise.fp
tags: material
thumbnail: stretched-mesh.png
title: Noise shader
twitter_image: https://www.defold.com/examples/material/noise/stretched-mesh.png
---

This example contains a game object with a model component. The model component uses the `/builtins/assets/meshes/quad.gltf` mesh, which is a rectangle 1 by 1 unit large. The game object is scaled to the dimensions of the screen so that the mesh covers the entire screen.

![stretched game object](stretched-mesh.png)

The shader applies multiple layers of noise to the uv coordinate to create a two dimensional flowing cloud or smoke like look. The shader also receives a time value from `noise.script` and applies this in the calculation to apply movement to the visual effect.
