---
brief: This manual covers how to integrate a game with the ODIN Voice SDK.
github: https://github.com/defold/extension-odin
language: en
layout: manual
title: ODIN Voice
toc:
- Defold ODIN Voice extension API documentation
- Not ready for production
- Installation
- Usage
- Example
- Source code
---

# Defold ODIN Voice extension API documentation

ODIN is a versatile cross-platform SDK engineered to seamlessly integrate real-time voice chat into multiplayer games. This extension adds a Lua interface, enabling seamless integration of ODIN Voice into your Defold game.

## Not ready for production

This integration is still in development and not ready for production use.


## Installation

To use ODIN Voice in your Defold project, add a version of the ODIN Voice extension to your `game.project` dependencies from the list of available [Releases](https://github.com/defold/extension-odin/releases). Find the version you want, copy the URL to ZIP archive of the release and add it to the project dependencies.

![](add-dependency.png)

Select `Project->Fetch Libraries` once you have added the version to `game.project` to download the version and make it available in your project.


## Usage

Make sure to read the [official ODIN Voice documentation](https://docs.4players.io/) to learn how ODIN Voice can be used to create multiplayer games.


```lua
	local ok = odin.init(function(self, event, data, msgid)
		if event == "RoomUpdated" then
			for i,update in ipairs(data.updates) do
				if update.kind == "Joined" then
					print(update.own_peer_id)
				elseif update.kind == "PeerJoined" then
					print(update.peer_id)
				elseif update.kind == "PeerLeft" then
					print(update.peer_id)
				end
			end
		elseif event == "RoomStatusChanged" then
			print(data.status)
		elseif event == "MessageReceived" then
			-- data received from odin.send()
		end
	end)
	if not ok then
		print("Error while initializing odin")
		return
	end

	ok = odin.create_room(room_id, user_id, access_key)
	if not ok then
		print("Error when creating room")
		return
	end

	ok = odin.send("Hello!")
	if not ok then
		print("Error when sending message")
		return
	end

	ok = odin.close_room()
	if not ok then
		print("Error when closing room")
		return
	end
```


## Example

[Refer to the example project](https://github.com/defold/extension-odin/blob/master/example) to see a complete example of how the integration works.

## Source code

The source code is available on [GitHub](https://github.com/defold/extension-odin)
## API reference
[API Reference - odin](/extension-odin/odin_api)
