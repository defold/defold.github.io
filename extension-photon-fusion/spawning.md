---
brief: Networked spawning turns a local scene instantiation into a coordinated event across all peers.
github: https://github.com/defold/extension-photon-fusion
layout: manual
locale: en
title: Photon Fusion - Spawning
toc:
- Spawning
- Spawn and Despawn
- Events
- Messages
---

# Spawning
In single-player, instantiating a scene creates a local game object. In multiplayer, the same operation must create that game object on every connected client and assign it a network identity so the replication system can track it. This is what networked spawning does - it turns a local scene instantiation into a coordinated event across all peers.

Despawning is the reverse: it removes the object from every client and frees its network identity. Late-joining clients automatically receive the current set of spawned objects when they enter the room.

## Spawn and Despawn
Call `fusion.spawn()` to create a networked game object instance and `fusion.despawn()` to remove it from all clients.

```lua
-- create a networked object
local factory_url = "example:/game#playerfactory"
local position = vmath.vector3(100, 100, 0)
local rotation = vmath.quat_rotation_z(math.rad(45))
local scene = 1
local owner_mode = fusion.OWNERMODE_PLAYERATTACHED
local id = fusion.spawn(factory_url, position, rotation, scene, owner_mode)
print("Created a networked game object with id", id)

-- delete the game object
fusion.despawn(id)
```


## Events
Fusion emits events when objects are created or destroyed, on all clients.

```lua
fusion.on_event(function(self, event_id, data)
	if event_id == fusion.EVENT_OBJECT_CREATED then
		print("Object id", data)
	elseif event_id == fusion.EVENT_OBJECT_DESTROYED then
		print("Object id", data)
	end
end)
```

## Messages
Fusion will send a message to the created game object when it is ready:

```lua
function on_message(self, message_id, message, sender)
	if message_id == fusion.EVENT_OBJECT_READY then
		print("I am ready and will sync my state")
	end
end
```