---
author: The Defold Foundation
authors:
- github: defold
  id: 41055a22bd3f5b94c6182d496d7083e7
  name: The Defold Foundation
brief: This example shows how to use collection proxies to show a splash screen while loading a game menu.
category: collection
layout: example
license: CC0-1.0
license_url: https://creativecommons.org/publicdomain/zero/1.0/
opengraph_image: https://www.defold.com/examples/collection/splash/splash.png
path: collection/splash
scripts: controller.script
tags: collection
thumbnail: splash.png
title: Splash
twitter_image: https://www.defold.com/examples/collection/splash/splash.png
---

The setup consists of several collections and game objects.

![splash](splash.png)

splash.collection
: This is the bootstrap collection specified in `game.project`. Contains:
  - A *Script* that handles loading and unloading of collection proxies
  - Two *Collection proxies* referencing the splash screen and a menu collection.

![menu](menu.png)

menu.collection
: This collection contains a menu. Contains:
  - A *GUI* with some box and text nodes that acts as buttons.

![splashscreen](splashscreen.png)

splashscreen.collection
: Collections representing the splash screen.
