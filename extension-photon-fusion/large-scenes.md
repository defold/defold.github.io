---
brief: Fusion supports Scene Objects which are static world elements that exist in the scene from the start but still need to sync state across clients.
github: https://github.com/defold/extension-photon-fusion
layout: manual
locale: en
title: Photon Fusion - Large Scenes
toc:
- Large Scenes
- Overview
---

# Large Scenes

Most multiplayer frameworks only handle dynamically spawned objects - entities created at runtime by player actions. But many games have static world elements (doors, switches, elevators, pickups) that exist in the scene from the start and still need to sync state across clients.

Fusion supports these as "scene objects." Unlike spawned objects, scene objects do not need to be spawned at runtime - they derive their network identity deterministically from their game object id, so every client can identify them without a spawn message. This page covers how to load and register scenes that contain these pre-placed networked nodes.

## Overview

Large scenes contain dozens, hundreds, or even thousands of pre-placed game objects (doors, elevators, pickups). These scene objects use deterministic IDs derived from their game object ids and do not have to be spawner. It is enough to register them as scene objects using `fusion.create_map_object()`.

```lua
-- door.script

function init(self)
	local map = 1
	local owner_mode = fusion.OWNERMODE_MASTERCLIENT
	local options = {}
	fusion.create_map_object(map, owner_mode, options)
end
```

Late-joining clients automatically receive current state from the server cache.