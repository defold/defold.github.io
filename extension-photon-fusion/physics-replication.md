---
brief: Physics bodies are challenging to replicate because they move continuously under forces, collisions and gravity. Fusion solves this with velocity-based forecasting.
github: https://github.com/defold/extension-photon-fusion
layout: manual
locale: en
title: Photon Fusion - Physics Replication
toc:
- Overview
---

Physics bodies are challenging to replicate because they move continuously under forces, collisions and gravity. Naively snapping a remote body to each received position causes visible jitter, especially at typical network update rates of 10-30 times per second.

Fusion solves this with velocity-based forecasting: remote clients predict where the body should be using its last known velocity, then a spring-damper system smoothly corrects any drift when the next server update arrives. The result is smooth motion on remote clients even under moderate packet loss or latency.

## Overview
Fusion auto-detects the physics body and uses velocity-based forecast smoothing. Position, rotation, linear_velocity and angular_velocity are synced automatically.