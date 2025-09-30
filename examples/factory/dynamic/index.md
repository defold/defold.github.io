---
author: Defold Foundation
brief: This example shows how to change the prototype game object used by a factory component.
category: factory
layout: example
opengraph_image: https://www.defold.com/examples/factory/dynamic/bullets_collection.png
path: factory/dynamic
scripts: dynamic.script
tags: factory
thumbnail: bullets_collection.png
title: Dynamic factories
twitter_image: https://www.defold.com/examples/factory/dynamic/bullets_collection.png

---

This example shows how to change the prototype game object used by a factory component. All prototype bullets are stored in a collection and referenced as a collection proxy. The collection proxy is never loaded, but it will ensure that the bullet prototypes are included in the build even though they are not immediately used by a factory. Another alternative is to load bullet prototypes using Live Update.

ship
: The red ship at the bottom. Contains:
  - A *Sprite* component with the spaceship image.
  - A *Factory* component to spawn bullet game objects. This component has the *Dynamic Protoype* option checked.
  - A *Collection Proxy* component referencing a collection containing all bullet types
  - A *Script* component to handle spawning of bullets.

All bullets are added in the bullets.collection:

![](bullets_collection.png)

The bullets.collection is referenced from the dynamic.collection as a collection proxy:

![](dynamic_collection.png)