---
brief: Remote Procedure Calls lets one client invoke a function on other clients without storing anything in the sync buffer.
github: https://github.com/defold/extension-photon-fusion
layout: manual
locale: en
title: Photon Fusion - Remote Procedure Calls
toc:
- Overview
---

Replication handles continuous state - properties that change over time like position, health or score. But games also need one-shot events: a player fires a weapon, sends a chat message or triggers an ability. Remote Procedure Calls (RPCs) fill this gap by letting one client invoke a function on other clients without storing anything in the sync buffer.

RPCs are fire-and-forget - they are delivered once and not retained. If a client joins after an RPC was sent, it will not receive that call. For state that must survive late joins, use replicated properties instead.

## Overview
Fusion RPCs are sent using `fusion.rpc()`, either to a specific player or to all players. RPCs are received as events.

```lua
-- set target_player to 0 to broadcast to all players
local target_player = 0
local descriptor = hash("chathandler")
local event = hash("on_message")
local data = json.encode({ text = "Hello" })
fusion.rpc(target_player, descriptor, event, data)

fusion.on_event(function(self, event_id, data)
	if event_id == fusion.EVENT_RPC then
		print(data.descriptor_type)		-- "chathandler"
		print(data.event)				-- "on_message"
		
		local message = json.decode(data.bytes)
		print(message.text)				-- "Hello"
	end
end)
```