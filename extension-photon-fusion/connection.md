---
brief: This manual covers the full connection lifecycle, from initialization and server connection through room creation, joining and disconnection.
github: https://github.com/defold/extension-photon-fusion
layout: manual
locale: en
title: Photon Fusion - Connection
toc:
- Connection & Matchmaking
- Initialization
- Connecting
- Authentication
- Connecting and Joining
- Room Operations
- Connection Status
- Events
- Disconnecting
- Example
- Where to Go Next
---

# Connection & Matchmaking
Before any game objects can sync, players must connect to a server and be grouped into a shared session. Photon uses a two-tier architecture: clients first connect to a master server for matchmaking, then get routed to a game server hosting a room. A room is an isolated session where a fixed group of players share game state, exchange RPCs and replicate objects.

This page covers the full connection lifecycle, from initialization and server connection through room creation, joining and disconnection.

## Initialization
Call `fusion.initialize_from_settings()` to load the App ID and version from *game.project* Settings, or pass them explicitly by calling `fusion.init()`.


```lua

-- initialize fusion with settings from game.project
fusion.init_from_settings()

-- initialize fusion with provided settings
fusion.init(app_id, app_version)
```

## Connecting
Use `fusion.connect()` to connect to the master server:

```lua
-- connect with specified username
fusion.connect(username)
```

### Authentication

Pass an optional second argument to send authentication values to Photon:

```lua
fusion.connect("Player", {
    type = fusion.AUTH_TYPE_CUSTOM,
    user_id = "player_123",
    data = { token = login_token }
})
```

The display name and authentication user id are separate. All fields in the authentication table are optional:

| Field | Type | Description |
| --- | --- | --- |
| `type` | number | A `fusion.AUTH_TYPE_*` constant. Defaults to `fusion.AUTH_TYPE_NONE`. |
| `user_id` | string | User id to send to Photon. The authentication provider can assign or override it. |
| `parameters` | string | URL-encoded query string, without a leading `?`. Encode individual names and values before joining them with `=` and `&`. |
| `data` | string or table | POST data: a string or a table with string keys and string, finite number or boolean values. Property tables are sent as JSON. Nested tables are not supported; an empty table is an empty property map. |

Available types are `AUTH_TYPE_NONE`, `AUTH_TYPE_CUSTOM`, `AUTH_TYPE_STEAM`, `AUTH_TYPE_FACEBOOK`, `AUTH_TYPE_OCULUS`, `AUTH_TYPE_PLAYSTATION4`, `AUTH_TYPE_XBOX`, `AUTH_TYPE_VIVEPORT`, `AUTH_TYPE_NINTENDOSWITCH`, `AUTH_TYPE_PLAYSTATION5`, `AUTH_TYPE_EPIC` and `AUTH_TYPE_FACEBOOKGAMING` (all prefixed with `fusion.`).

For Steam, obtain a ticket through your Steam integration and pass its hexadecimal encoding in the `ticket` parameter, as described in [Photon's Steam authentication guide](https://doc.photonengine.com/pun/current/connection-and-authentication/authentication/steam-auth):

```lua
fusion.connect("Player", {
    type = fusion.AUTH_TYPE_STEAM,
    parameters = "ticket=" .. steam_ticket_hex
})
```

Calling `fusion.connect()`, `fusion.connect(username)` or `fusion.connect(username, nil)` keeps anonymous authentication. Use `fusion.connect(nil, auth)` to authenticate without a display name. Invalid option names, types or data raise a Lua error before connecting.

Configure the selected provider in the Photon dashboard. To require authentication, disable **Allow anonymous clients** there; supplying authentication values in the client does not itself prevent other clients from connecting anonymously. Keep provider secrets on the server or in the dashboard. See [Photon's custom authentication setup](https://doc.photonengine.com/realtime/current/connection-and-authentication/authentication/custom-authentication).

## Connecting and Joining
Connecting and joining are separate steps. Connect to the Photon master server first, then join or create a room once the connection succeeds.

```lua
fusion.on_event(function(self, event_id, data)
	if event_id == fusion.EVENT_CONNECTED then
		fusion.join_or_create_room("lobby")
	end
end)

fusion.connect("player_123")
```

## Room Operations
A room is a shared session where players sync objects and exchange RPCs. Fusion provides methods to create, join or leave rooms.

```lua
-- Create a new room (fails if it already exists)
fusion.create_room("my_room", create_room_options)

-- Join an existing room (empty name = random room)
fusion.join_room("my_room", join_room_options)

-- Join if rooms exists, create if does not
fusion.join_or_create_room("my_room", create_room_options, join_room_options)

-- Leave current room (stays connected for re-matchmaking)
fusion.leave_room()
```

## Connection Status
Fusion tracks a linear state machine from disconnected through connecting, connected, joining and finally in-room.

* `fusion.STATE_DISCONNECTED` - Not connected
* `fusion.STATE_CONNECTING` - Establishing connection
* `fusion.STATE_CONNECTED` -  Connected to master server, can join rooms
* `fusion.STATE_JOINING_ROOM` - Join in progress
* `fusion.STATE_IN_ROOM` - In a room, can spawn objects and sync
* `fusion.STATE_LEAVING_ROOM` - Leaving room
* `fusion.STATE_DISCONNECTING` - Disconnecting from master server

Query connection state using `fusion.get_state()`. Other useful query methods:

* `fusion.get_disconnect_cause()`
* `fusion.is_connected()`
* `fusion.is_running()`
* `fusion.is_in_room()`
* `fusion.is_master_client()`


## Events
Listen for events to avoid polling status each frame:

* `fusion.EVENT_CONNECTED` - connected to master server
* `fusion.EVENT_DISCONNECTED` - disconnected from master server (voluntarily)
* `fusion.EVENT_FORCED_DISCONNECT` - disconnected from master server
* `fusion.EVENT_ROOM_JOINED` - successfully entered a room (safe to spawn objects)
* `fusion.EVENT_ROOM_LEFT` - left a room (voluntarily or disconnected)

```lua
fusion.on_event(function(self, event_id, data)
	if event_id == fusion.EVENT_CONNECTED then
		fusion.join_or_create_room("lobby")
	elseif event_id == fusion.EVENT_ROOM_JOINED then
		print("joined room:", data.name)
	end
end)
```

## Disconnecting
Call `fusion.disconnect()` to cleanly leave the current room and close the server connection.


## Example
A complete script that connects to Photon Cloud, joins a room with custom options and prints when the player enters.

```lua

fusion.init_from_settings()

fusion.on_event(function(self, event_id, data)
	if event_id == fusion.EVENT_CONNECTED then
		local options = {
			max_players = 8,
			is_visible = true,
			custom_properties = { map = "arena" },
			lobby_properties = { "map" }
		}
		fusion.join_or_create_room("lobby", options)
	elseif event_id == fusion.EVENT_ROOM_JOINED then
		print("joined room:", data.name)
	end
end)

fusion.connect()
```


## Where to Go Next
* [Back to the Introduction](..)
* [Quick Start Guide](../quick-start-guide) — Build a multiplayer demo in 10 steps