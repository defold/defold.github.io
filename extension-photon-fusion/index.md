---
brief: This manual covers how to integrate a game with the Photon Fusion SDK.
github: https://github.com/defold/extension-photon-fusion
layout: manual
locale: en
title: Photon Fusion
toc:
- Fusion Defold Intro
- Simple Connection and Matchmaking
- Shared Authority Replication
- Engine-First Integration
- Where to Go Next
- License
- Example
- Source code
---

## Fusion Defold Intro

Photon Fusion Defold brings scalable multiplayer networking to Defold as a drop-in native extension. It is built on top of the same battle-tested infrastructure that powers thousands of live titles across every major platform. You get room-based matchmaking, efficient state replication with late join support, forecast physics prediction and flexible RPCs. And better, everything is designed from the ground up to feel native to Defold's workflow.


## Simple Connection and Matchmaking
Getting players into the same session is the first challenge when creating a multiplayer game. Fusion handles this end to end: game clients connect to Photon Cloud's global network of region clusters, and get matched into a room instance, all done directly in Lua. Rooms are configurable with max player counts, custom properties and lobby filtering, so you can build anything from a quick-match to a private lobby system.

You do not need to provision or maintain any servers. Photon manages hosting, scaling and region routing worldwide.

See [Connection & Matchmaking](connection) for the full API.


```lua
fusion.on_event(function(self, event_id, data)
	if event_id == fusion.EVENT_CONNECTED then
		fusion.join_or_create_room("lobby")
	end
end)

fusion.connect("player_123", "eu")
```

## Shared Authority Replication
In traditional client-server networking, one player hosts and every other player depends on that host's connection and hardware. Fusion uses a **shared authority** model instead: every client owns and simulates its own objects locally, while the Photon Fusion server code maintains a stateful cache of the world. When a new player joins mid-match, they receive the state snapshot automatically, no manual state transfer code required.

Replication works at the property level. Fusion tracks individual values (position, health, score) and only distributes what has actually changed since the last update, keeping bandwidth low while keeping **per-object full consistency**. For larger worlds and more complex cases, **Area of Interest** filtering lets you work with dynamic spatial regions so clients only receive updates for nearby objects, scaling gracefully to dozens or even hundreds of players.

If you need extra security, you can even deploy **custom server-side plugins** that validate state changes before they reach other clients — useful for competitive games or anti-cheat.

See [Replication](replication) for details.


## Engine-First Integration
Fusion was designed with Defold's idioms in mind. You write gameplay code in Lua, load collections, spawn game objects and react to messages and callbacks exactly as you would in a single-player project.

Spawning networked objects follows the same pattern: register an existing game object as networked or spawn it from Fusion using `fusion.spawn()` and it will be created on every client in the same room.

The [Quick Start Guide](quick-start-guide) walks through a full example in under 10 minutes.

```lua
local factory_url = "example:/game#playerfactory"
local position = vmath.vector3(100, 100, 0)
local rotation = vmath.quat_rotation_z(math.rad(45))
local scene = 1
local owner_mode = fusion.OWNERMODE_PLAYERATTACHED
local id = fusion.spawn(factory_url, position, rotation, scene, owner_mode)
```

## Where to Go Next
* [Quick Start Guide](quick-start-guide) — Build a multiplayer demo in 10 steps
* [Installation](installation) — Requirements and installation
* [Connection](connection) — Initialization, rooms and signals
* [Replication](replication) — Authority, replication modes and properties
* [Spawning](spawning) — Dynamic networked objects and sub-objects
* [RPCs](rpcs) — Remote procedure calls
* [Physics Replication] — Forecast smoothing for rigid bodies


## License

You must read and agree to the [Exit Games End User License Terms](https://github.com/defold/extension-photon-fusion/blob/master/fusion/license.txt) before using Photon Fusion in your own project.


## Example

[Refer to the example project](https://github.com/defold/extension-photon-fusion/blob/master/example) to see a complete example of how the integration works. Video showing four connected clients:


## Source code

The source code is available on [GitHub](https://github.com/defold/extension-photon-fusion)
## API reference
[API Reference - fusion](/extension-photon-fusion/fusion_api)
