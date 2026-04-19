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
- Connecting and Joining
- Room Operations
- Connection Status
- Events
- Disconnecting
- Example
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
-- connect with specified username and region taken from game.project
fusion.connect(username)

-- connect with specified username and region
fusion.connect(username, region)
```

## Connecting and Joining
Connecting and joining are separate steps. Connect to the Photon master server first, then join or create a room once the connection succeeds.

```lua
fusion.on_event(function(self, event_id, data)
	if event_id == fusion.EVENT_CONNECTED then
		fusion.join_or_create_room("lobby")
	end
end)

fusion.connect("player_123", "eu")
```

## Room Operations
A room is a shared session where players sync objects and exchange RPCs. Fusion provides methods to create, join or leave rooms.

```lua
-- Create a new room (fails if it already exists)
fusion.create_room("my_room", options)

-- Join an existing room (empty name = random room)
fusion.join_room("my_room", options)

-- Join if exists, create if not
fusion.join_or_create_room("my_room", options)

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