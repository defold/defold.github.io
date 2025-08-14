---
brief: This manual covers how to integrate a game with the Photon Realtime SDK.
github: https://github.com/defold/extension-photon-realtime
language: en
layout: manual
title: Photon Realtime
toc:
- Defold Photon Realtime extension API documentation
- Installation
- Usage
- License
- Example
- Source code
---

# Defold Photon Realtime extension API documentation

Photon Realtime offers powerful tools for creating multiplayer games and advanced networked experiences through the Photon Realtime SDK. It provides scalable solutions for essential features such as authentication, matchmaking, and fast, reliable communication. This extension adds a Lua interface, enabling seamless integration of Photon Realtime services into your Defold game.


## Installation

To use Photon Realtime in your Defold project, add a version of the Photon Realtime extension to your `game.project` dependencies from the list of available [Releases](https://github.com/defold/extension-photon-realtime/releases). Find the version you want, copy the URL to ZIP archive of the release and add it to the project dependencies.

![](add-dependency.png)

Select `Project->Fetch Libraries` once you have added the version to `game.project` to download the version and make it available in your project.


## Usage

The Photon Realtime SDK is based around the concept of `Operations`, `Operation Responses` and `Events`. Clients call `Operations` on the server side and get `Operation Responses` for most of those. Aside from `Operation Responses`, clients also receive `Events`, which are used independently of what the client asked for.

While in a room, the operation `RaiseEvent` is used to pass data to the others, which receive a custom event.

Make sure to read the [official Photon Realtime documentation](https://doc.photonengine.com/realtime/current/getting-started/realtime-intro) to learn more about the various ways Photon Realtime can be used to create multiplayer games.


```lua
local EVENT_POSX = 1
local EVENT_POSY = 2

function init(self)
	-- initialize realtime
	-- the callback function will receive events from photon
	realtime.init(app_id, app_version, function(self, id, data)
		-- handle errors
		if data.error_code and data.error_code > 0 then
			print(data.error_string)
			return
		end

		-- check responses and events, some examples below
		if id == realtime.EVENT_CONNECTRETURN then
			print("connected!")

			-- join or create a random room
			realtime.join_or_create_random_room(game_id, room_options, join_options)
		elseif id == realtime.EVENT_JOINRANDOMORCREATEROOMRETURN then
			print(data.local_player_nr)

			-- raise a custom event with position data
			local pos = go.get_position()
			realtime.raise_event(false, pos.x, EVENT_POSX)
			realtime.raise_event(false, pos.y, EVENT_POSY)
		elseif message_id == realtime.EVENT_CUSTOMEVENTACTION then
			-- custom events sent using realtime.raise_event() end up here
			if data.event_code == EVENT_POSX then
				print(data.event_content)
			end
		end
	end)

	-- connect to server
	realtime.connect({})
end

function update(self, dt)
	-- call frequently to check for events
	realtime.update()
end

```


## License

You must read and agree to the [Exit Games End User License Terms](https://github.com/defold/extension-photon-realtime/blob/master/realtime/license.txt) before using Photon Realtime in your own project.


## Example

[Refer to the example project](https://github.com/defold/extension-photon-realtime/blob/master/example) to see a complete example of how the integration works. Video showing four connected clients:

[![Watch the video](https://img.youtube.com/vi/G5w62I-I2hA/0.jpg)](https://youtu.be/G5w62I-I2hA)


## Source code

The source code is available on [GitHub](https://github.com/defold/extension-photon-realtime)
## API reference
[API Reference - realtime](/extension-photon-realtime/realtime_api)
