---
brief: In a multiplayer game, each client runs its own copy of the simulation. This manual covers how Fusion keeps these copies consistent.
github: https://github.com/defold/extension-photon-fusion
layout: manual
locale: en
title: Photon Fusion - Replication
toc:
- Replication
- How to replicate an object
- Replicate script properties
- Authority and Ownership
- API Quick Reference
- Transaction (default)
- Player Attached
- Dynamic
- Master Client
- Owner change event
- Interest Management (AOI)
- Interest events
- Where to Go Next
---

# Replication
In a multiplayer game, each client runs its own copy of the simulation. Replication is the mechanism that keeps these copies consistent: one client (the authority) writes the definitive values for an object's properties, the server accepts them and distributes them to every other client. Without replication, each player would see a different game.

Fusion replicates at the property level. Individual values like position, health or score are tracked independently. The server only sends properties that have changed since the last update, minimizing bandwidth.


## How to replicate an object
Register a game object using `fusion.create_object()` to handle property sync for the game object. The authority client writes values to the server; remote clients receive and optionally smooth them.

```lua
local map = 1
local factory_url = "example:/game#playerfactory"
local owner_mode = fusion.OWNERMODE_PLAYERATTACHED
local options = {}
local id = go.get_id()
fusion.create_object(map, factory_url, owner_mode, options, id)
```

Call `fusion.destroy_object(id)` to no longer handle property sync for a game object.


## Replicate script properties
Position, rotation and scale is automatically replicated, but gameplay data like health, score or other more specific data needs to be added manually. It is possible to replicate game object properties of any accepted property type:

```lua
go.property("health", 10)
go.property("berserk", true)
go.property("direction", vmath.vector3(0, 1, 0))
-- and so on
```

In order to replicate a game object script property you need to explicily specify it when the game object is spawned or created:

```lua
local options = {
	properties = {
		-- id of the script component -> list of properties to replicate
		player = { "health", "berserk", "direction" }
	}
}
fusion.create_object(factory_url, map, owner_mode, options, id)
fusion.spawn(factory_url, position, rotation, map, owner_mode, options)
```

It is also possible to disable replication of the game object position, rotation and scale by setting the `replication_mode` option to `fusion.REPLICATION_MODE_NONE`:

```lua
local options = {
	replication_mode = fusion.REPLICATION_MODE_NONE
}
```


## Authority and Ownership
Authority determines which client is allowed to write a networked object's properties. Only the authority client's values are accepted by the server - all other clients receive read-only copies. Fusion has several authority modes: Transaction, Player Attached, Dynamic and Master Client.

Authority mode is decided when the object is registered with Fusion:

```lua
local function on_player_joined()
	fusion.create_object(factory_url, map, fusion.OWNERMODE_TRANSACTION, options, id)
	fusion.create_object(factory_url, map, fusion.OWNERMODE_PLAYERATTACHED, options, id)
	fusion.create_object(factory_url, map, fusion.OWNERMODE_DYNAMIC, options, id)
	fusion.create_object(factory_url, map, fusion.OWNERMODE_MASTERCLIENT, options, id)
	fusion.create_object(factory_url, map, fusion.OWNERMODE_GAMEGLOBAL, options, id)
end
```


### API Quick Reference

```lua
fusion.has_authority(id)           -- am I the current owner of the specified game object?
fusion.has_owner(id)               -- does the specified game object have an owner?
fusion.get_owner_id(id)            -- which player owns the specified game object?
fusion.want_authority(true, id)    -- claim ownership of the specified game object
fusion.want_authority(false, id)   -- release ownership of the specified game object
```


### Transaction (default)
Server-confirmed ownership transfers. The current owner keeps authority until it explicitly releases with `fusion.want_authority(false)`, at which point the server marks the object as an orphan (unowned). Any other client can then claim it with `fusion.want_authority(true)`.

On disconnect, the object stays alive as an orphan and other clients can claim it.


### Player Attached
Same request/release mechanics as Transaction, but with one key difference: when the owning player disconnects, the server automatically despawns the object.

Use this for player avatars, player-owned inventory, or anything that should not outlive its owner.


### Dynamic
Predictive authority is designed for fast-paced ownership transfers where waiting for server confirmation would feel sluggish.

`fusion.want_authority(true)` immediately assigns ownership locally and the client starts sending data at full rate. If the server agrees, nothing further happens, the client simply continues as authority. If the server rejects the claim (because another client's data arrived first), authority reverts.

`fusion.want_authority(false)` lowers the send rate, signalling that this client is willing to give up ownership. The server can then accept another client's predictive claim. The client will not re-claim automatically once the server confirms someone else took over.


#### Automatic send-rate management:

| Call                              | Update Interval |
|-----------------------------------|-----------------|
| `fusion.want_authority(true)`	    | 1 (every tick)  |
| `fusion.want_authority(false)`    | 16 (low rate)   |

The low send rate for the authority is the way to allow the server to accept a dynamic request (gives enough slack for a new client to send a new version first). It's possible to override the default permissive interval by passing a second argument: `fusion.set_send_rate(12)`.


### Master Client
Always owned by the current master client. Calls to `fusion.want_authority()` are ignored.

If the master client disconnects, Photon assigns a new master and ownership transfers automatically - no application code required.

Use this for shared singleton state: scoreboards, match timers, game-manager objects.


## Owner change event
The `fusion.EVENT_OBJECT_OWNER_CHANGED` event is sent whenever ownership resolves, regardless of mode:

```lua
fusion.on_event(function(self, event_id, data)
	if event_id == fusion.EVENT_OBJECT_OWNER_CHANGED then
		if fusion.has_authority(data.id) then
			print("I now own this object")
		end
	end
end)
```

A message is also sent to the game object:

```lua
function on_message(self, message_id, message, sender)
	if message_id == fusion.EVENT_OBJECT_OWNER_CHANGED then
		print("I have a new owner!", message.owner)
	end
end
```

## Interest Management (AOI)
Interest management controls which objects each client receives updates for, reducing bandwidth in large worlds. Objects publish interest keys and clients subscribe to receive updates:


| Interest | Publish                             | Subscribe                      |
|----------|-------------------------------------|--------------------------------|
| Area     | `fusion.set_area_interest_key(key)` | `fusion.set_area_keys(keys)`   |
| User     | `fusion.set_user_interest_key(key)` | `fusion.add_user_key(key)`     |
| Global   | `fusion.set_global_interest_key()`  | Updates received automatically |


### Interest events

```lua
fusion.on_event(function(self, event_id, data)
	if event_id == fusion.EVENT_INTEREST_ENTER then
		print("Object id", data)
	elseif event_id == fusion.EVENT_INTEREST_EXIT then
		print("Object id", data)
	end
end)
```


## Where to Go Next
* [Back to the Introduction](..)
* [Quick Start Guide](../quick-start-guide) — Build a multiplayer demo in 10 steps