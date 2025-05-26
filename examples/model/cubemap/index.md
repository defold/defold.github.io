---
author: Defold Foundation
brief: This example shows how to use a cubemap to draw environment reflections on a model.
category: model
layout: example
path: model/cubemap
scripts: cubemap.script, cubemap_model.fp, cubemap_model.vp
tags: model
title: Cubemap Reflection

---

This example contains a game object with a model component in the shape of the Defold logo. The model has a special `cubemap_model.material` which uses a cubemap sampler to calculate reflections on the model from the cubemap.