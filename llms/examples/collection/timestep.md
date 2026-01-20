# Time-step

This example shows how to speed up or slow down animations in a collection proxy by changing the time step of the collection proxy.

[Project files](https://github.com/defold/examples/tree/master/collection/timestep)

The setup consists of a `timestep.collection` and a `game.collection`.

timestep.collection
: This is the bootstrap collection specified in `game.project`. Contains:
  - A *Script* that handles loading of the `game.collection` and controls the time-step of `game.collection` using the `set_time_step` message.

game.collection
: This collection contains a "game" with some animated game objects. Contains:
  - Five animated game objects that are animated using `go.animate()`
  - A *Script* that starts the game object animations and lets the user control the time-step through messages sent to the *Script* in the `timestep.collection`.

## Scripts

### controller.script

```lua
-- speed of the time in the collection proxy
go.property("speed", 1)

function init(self)
	-- acquire input for this script
	msg.post(".", "acquire_input_focus")
	-- load the collection proxy
	msg.post("#gameproxy", "async_load")
end

function update(self, dt)
	-- update the time step of the proxy each frame since it might be animated
	msg.post("#gameproxy", "set_time_step", { factor = self.speed, mode = 0 })
	label.set_text("#label", tostring(self.speed))
end

function on_message(self, message_id, message, sender)
	if message_id == hash("proxy_loaded") then
		msg.post(sender, "enable")
	elseif message_id == hash("animate_speed") then
		-- cancel any current animation of the speed property
		go.cancel_animations("#", "speed")
		-- start animation of the speed property
		local to = message.to
		local change = math.abs(self.speed - to)
		local rate_of_change = 2
		local duration = change / rate_of_change
		go.animate("#", "speed", go.PLAYBACK_ONCE_FORWARD, to, go.EASING_LINEAR, duration)
	elseif message_id == hash("change_speed") then
		-- cancel any current animation of the speed property
		go.cancel_animations("#", "speed")
		-- make sure speed never goes below 0
		self.speed = math.max(self.speed + message.amount, 0)
	end
end
```

### game.script

```lua
function init(self)
	-- get input to this script
	msg.post(".", "acquire_input_focus")

	-- animate some game objects
	go.animate("enemy1", "position.x", go.PLAYBACK_LOOP_PINGPONG, 720, go.EASING_INOUTQUAD, 5, 0)
	go.animate("enemy2", "position.x", go.PLAYBACK_LOOP_PINGPONG, 720, go.EASING_INOUTQUAD, 5, 0.5)
	go.animate("enemy3", "position.x", go.PLAYBACK_LOOP_PINGPONG, 720, go.EASING_INOUTQUAD, 5, 1)
	go.animate("enemy4", "position.x", go.PLAYBACK_LOOP_PINGPONG, 720, go.EASING_INOUTQUAD, 5, 1.5)
end

function on_input(self, action_id, action)
	if action_id == hash("key_left") then
		msg.post("timestep:/controller", "change_speed", { amount = -0.01 })
	elseif action_id == hash("key_right") then
		msg.post("timestep:/controller", "change_speed", { amount = 0.01 })
	elseif action_id == hash("key_space") and action.pressed then
		-- flip self.to between 0 and 3 each time
		self.to = 3 - (self.to or 0)
		msg.post("timestep:/controller", "animate_speed", { to = self.to })
	end
end
```
