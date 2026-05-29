---
author: JuLongZhiLu(巨龙之路)
brief: Apply a linear impulse to a dynamic physics body on click or touch.
category: physics
layout: example
opengraph_image: https://www.defold.com/examples/physics/apply_linear_impulse/thumbnail.png
path: physics/apply_linear_impulse
scripts: cube.script
tags: physics
thumbnail: thumbnail.png
title: Apply Linear Impulse
twitter_image: https://www.defold.com/examples/physics/apply_linear_impulse/thumbnail.png

---

This example shows how a Box2D body can be pushed instantly with a linear impulse.

## What You'll Learn

- How to get the Box2D body from a collision object.
- How to apply an impulse at a world position.
- How to receive touch and mouse input in a script.

## Setup

The collection contains a cube game object with a sprite, a dynamic collision object, and `/example/cube.script`. A static platform collision object catches the cube after the impulse. The project enables fixed-step physics and uses Box2D through Defold's built-in `b2d` API.

![setup](setup.webp)

## How It Works

The script acquires input focus and listens for the built-in `touch` action. When the player clicks or touches the screen, it gets the cube's Box2D body, reads the body's current world position, and applies an upward linear impulse at that point.

Read more about the [Box2D API here](https://defold.com/ref/stable/b2d-lua/).