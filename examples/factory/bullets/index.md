---
author: Defold Foundation
authors:
- github: defold
  id: f0ed797e86f7025f8ba5455479852ca5
  name: Defold Foundation
brief: This example shows how to dynamically spawn bullet game objects using a factory component.
category: factory
layout: example
license: CC0-1.0
license_url: https://creativecommons.org/publicdomain/zero/1.0/
path: factory/bullets
scripts: player.script
tags: factory
title: Shoot bullets
---

This example shows how to dynamically spawn bullet game objects using a factory component and how to also move and delete the bullets. The setup consists of two game objects; one for the player and one for the bullet that is spawned using a factory component.

Combine this example with some of the examples from the movement and physics categories to create a shoot 'em up game!

player
: The red ship at the bottom. Contains:
  - A *Sprite* component with the spaceship image.
  - A *Factory* component to spawn bullet game objects
  - A script to handle spawning of bullets.

bullet
: The bullet fired by the player. Contains:
  - A *Sprite* component with a bullet image.
