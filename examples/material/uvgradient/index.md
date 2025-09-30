---
author: Defold Foundation
brief: This example shows how to apply a basic shader to a full screen quad.
category: material
layout: example
opengraph_image: https://www.defold.com/examples/material/uvgradient/stretched-mesh.png
path: material/uvgradient
scripts: uvgradient.fp
tags: material
thumbnail: stretched-mesh.png
title: UV Gradient
twitter_image: https://www.defold.com/examples/material/uvgradient/stretched-mesh.png

---

This example contains a game object with a model component. The model component uses the `/builtins/assets/meshes/quad.dae` mesh, which is a rectangle 1 by 1 unit large. The game object is scaled to the dimensions of the screen so that the mesh covers the entire screen.

![stretched game object](stretched-mesh.png)

The shader is very basic and sets the fragment color based on the UV position, thus creating a color gradient. This is a good starting point when experimenting with graphical effects using a shader.