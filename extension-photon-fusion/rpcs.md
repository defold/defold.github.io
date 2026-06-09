---
brief: Remote Procedure Calls lets one client invoke a function on other clients without storing anything in the sync buffer.
github: https://github.com/defold/extension-photon-fusion
layout: manual
locale: en
title: Photon Fusion - Remote Procedure Calls
toc:
- RPCs
- Overview
- Subscribe
- Where to Go Next
---

# RPCs
Replication handles continuous state - properties that change over time like position, health or score. But games also need one-shot events: a player fires a weapon, sends a chat message or triggers an ability. Remote Procedure Calls (RPCs) fill this gap by letting one client invoke a function on other clients without storing anything in the sync buffer.

RPCs are fire-and-forget - they are delivered once and not retained. If a client joins after an RPC was sent, it will not receive that call. For state that must survive late joins, use replicated properties instead.


## Overview
Fusion RPCs are sent using `fusion.rpc()`, either to a specific player or to all players. RPCs are received as events.

```lua
-- set target_player to 0 to broadcast to all players
local target_player = 0
local target_object = 0
local event = hash("chat_message")
local data = { text = "Hello" }
fusion.rpc(target_player, target_object, event, data)

fusion.on_event(function(self, event_id, data)
	if event_id == fusion.EVENT_RPC then
		print(data.event)				-- "chat_message"
		print(message.text)				-- "Hello"
	end
end)
```


## Subscribe

```lua
function init(self)
	fusion.subscribe_rpc(hash("some_message"))
end

function final(self)
	fusion.unsubscribe_rpc(hash("some_message"))
end

function on_message(self, message_id, message, sender)
	if message_id == hash("some_message") then
		pprint(message)
	end
end
```


## Where to Go Next
* [Back to the Introduction](..)
* [Quick Start Guide](../quick-start-guide) — Build a multiplayer demo in 10 steps