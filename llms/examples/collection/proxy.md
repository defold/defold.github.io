# Proxy

This example shows how to use collection proxies to load and unload collections.

[Project files](https://github.com/defold/examples/tree/master/collection/proxy)

The setup consists of several collections and game objects.

proxy.collection
: This is the bootstrap collection specified in `game.project`. Contains:
  - A *Script* that handles loading and unloading of collection proxies
  - Four *Collection proxies* referencing a menu collection and three level collections.

menu.collection
: This collection contains a menu. Contains:
  - A *GUI* with some box and text nodes that acts as buttons.
  - A *GUI script* that handles the logic of clicking on the buttons and sending messages back to the proxy.collection.

level1-3.collection
: Collections representing the levels of a game. Contains:
  - *Script* with logic to send a message back to the proxy.collection to show the menu again.

## Scripts

### controller.script

```lua
local function show(self, proxy) -- <5>
	if self.current_proxy then -- <6>
		msg.post(self.current_proxy, "unload") -- <7>
		self.current_proxy = nil
	end
	msg.post(proxy, "async_load") -- <8>
end

function init(self)
	msg.post(".", "acquire_input_focus") -- <1>
	self.current_proxy = nil -- <2>
	msg.post("#", "show_menu") -- <3>
end

function on_message(self, message_id, message, sender)
	if message_id == hash("show_menu") then -- <4>
		show(self, "#menuproxy")
	elseif message_id == hash("show_level1") then
		show(self, "#level1proxy")
	elseif message_id == hash("show_level2") then
		show(self, "#level2proxy")
	elseif message_id == hash("show_level3") then
		show(self, "#level3proxy")
	elseif message_id == hash("proxy_loaded") then -- <9>
		self.current_proxy = sender -- <10>
		msg.post(sender, "enable") -- <11>
	elseif message_id == hash("proxy_unloaded") then
		print("Unloaded", sender)
	end
end

--[[
1. Acquire input focus for this game object. This is required for input to be able to propagate into any of the collection proxies on the same game object as this script.
2. Create a variable `current_proxy` to track which collection proxy that is loaded.
3. Post a `show_menu` message to the `on_message` function of this script. This load and show the first screen.
4. Message handler that will react to `show_menu`, `show_level1`, `show_level2` and `show_level3` messages and load the appropriate collection proxy.
5. A helper function to unload any currently loaded collection proxy and load a new collection proxy.
6. Check if a collection proxy is loaded.
7. Send an `unload` message to the currently loaded collection proxy. This will immediately unload the proxy and all of its resources. A `proxy_unloaded` message will be sent when it has been unloaded.
8. Send an `async_load` message to the collection proxy that should be loaded. This will start loading the collection proxy and all of its resources. A `proxy_loaded` message will be sent when it has been loaded.
9. Handle the `proxy_loaded` message. This is sent when a collection proxy has finished loading. The collection and all resources will be loaded but no game objects or components will be active/enabled.
10. Store the url of the proxy that was loaded. This is used in the helper function to unload it when showing another collection proxy.
11. Enable the loaded collection proxy. This will activate/enable all game objects and components within the collection.
--]]
```

### menu.gui_script

```lua
function init(self)
	msg.post(".", "acquire_input_focus") -- <1>
end

function on_input(self, action_id, action)
	if action_id == hash("touch") and action.released then -- <2>
		if gui.pick_node(gui.get_node("level1"), action.x, action.y) then -- <3>
			msg.post("proxy:/controller#controller", "show_level1") -- <4>
		elseif gui.pick_node(gui.get_node("level2"), action.x, action.y) then
			msg.post("proxy:/controller#controller", "show_level2")
		elseif gui.pick_node(gui.get_node("level3"), action.x, action.y) then
			msg.post("proxy:/controller#controller", "show_level3")
		end
	end
end

--[[
1. Acquire input focus for this script.
2. Check if a mouse click/screen touch is released.
3. Check if the mouse click/screen touch happened on top of any of the buttons.
4. Send a `show_level1` message to the controller script component in the `proxy` collection.
--]]
```

### level.script

```lua
function init(self)
	msg.post(".", "acquire_input_focus")
end

function on_input(self, action_id, action)
	if action_id == hash("touch") and action.released then
		msg.post("proxy:/controller", "show_menu")
	end
end
```
