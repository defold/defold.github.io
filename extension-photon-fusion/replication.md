---
brief: In a multiplayer game, each client runs its own copy of the simulation. This manual covers how Fusion keeps these copies consistent.
github: https://github.com/defold/extension-photon-fusion
layout: manual
locale: en
title: Photon Fusion - Replication
toc:
- Replication
- How to replicate an object
- Authority and Ownership
- API Quick Reference
- Transaction (default)
- Player Attached
- Dynamic
- Master Client
- Owner change event
- Interest Management (AOI)
- Interest events
---

# Replication
In a multiplayer game, each client runs its own copy of the simulation. Replication is the mechanism that keeps these copies consistent: one client (the authority) writes the definitive values for an object's properties, the server accepts them and distributes them to every other client. Without replication, each player would see a different game.

Fusion replicates at the property level. Individual values like position, health or score are tracked independently. The server only sends properties that have changed since the last update, minimizing bandwidth.

## How to replicate an object
Register a game object using `fusion.register_object()` to handle property sync for the game object. The authority client writes values to the server; remote clients receive and optionally smooth them.

```lua
local factory_url = "example:/game#playerfactory"
local scene = 1
local owner_mode = fusion.OWNERMODE_PLAYERATTACHED
local id = go.get_id()
fusion.register_object(factory_url, scene, owner_mode, id)
```

Call `fusion.unregister_object(id)` to no longer handle property sync for a game object.

## Authority and Ownership
Authority determines which client is allowed to write a networked object's properties. Only the authority client's values are accepted by the server - all other clients receive read-only copies. Fusion has several authority modes: Transaction, Player Attached, Dynamic and Master Client.

Authority mode is decided when the object is registered with Fusion:

```lua
local function on_player_joined()
	fusion.register_object(scene, factory_url, fusion.OWNERMODE_TRANSACTION, id)
	fusion.register_object(scene, factory_url, fusion.OWNERMODE_PLAYERATTACHED, id)
	fusion.register_object(scene, factory_url, fusion.OWNERMODE_DYNAMIC, id)
	fusion.register_object(scene, factory_url, fusion.OWNERMODE_MASTERCLIENT, id)
	fusion.register_object(scene, factory_url, fusion.OWNERMODE_GAMEGLOBAL, id)
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