# Physics debug

This example allows you to toggle physics debug visualization as well as changing the time step so the simulation runs at one tenth of the speed.

[Project files](https://github.com/defold/examples/tree/master/debug/physics)

With the physics visualization on, all collision object shapes are visible. In addition, at intersections the normals at the collision points are shown.

The example collection consists of:
- 4 blocks with dynamic collision objects with Restituion 1.0, so they bounce forever,
- 4 walls with static collision objects forming boundaries for the blocks,
- game object `go` with:
  - label with example description,
  - a script `physics.script` included below.

This collection is additionally loaded via a `Collection Proxy` component in `main.collection`. Therefore, sending message `set_time_step` to its url `"main:/loader#physicsproxy"` is causing the proxy to have a different update time, causing e.g. the slow-motion effect, which might be helpful when debugging physics.

## Scripts

### physics.script

```lua
function init(self)
	msg.post(".", "acquire_input_focus") -- <1>
	self.show_debug = false -- <2>
end

function on_input(self, action_id, action)
	if action_id == hash("touch") and action.pressed then
		msg.post("@system:", "toggle_physics_debug") -- <3>
		if self.show_debug then -- <4>
			msg.post("main:/loader#physicsproxy", "set_time_step", { factor = 1, mode = 0 })
		else
			msg.post("main:/loader#physicsproxy", "set_time_step", { factor = 0.1, mode = 1 })
		end
		self.show_debug = not self.show_debug -- <5>
	end
end

--[[
1. Make sure this game object's script component gets input from the engine.
2. A state flag to track if we show debug info or not.
3. If user clicks, toggle physics visualization.
4. In addition, we want to set the timestep. That is done through the collection proxy that loaded this example. Since we cannot get hold of the proxy from this side of it we message the loader game object in the main collection and it will relay the message to the proxy component.
5. Switch the `show_debug` flag.
--]]
```

### loader.script

```lua
function init(self)
    msg.post(".", "acquire_input_focus")
    msg.post("#physicsproxy", "load")
end

function on_message(self, message_id, message, sender)
    if message_id == hash("proxy_loaded") then
        msg.post(sender, "init")
        msg.post(sender, "enable")
    end
end
```
