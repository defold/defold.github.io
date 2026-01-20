# Message passing

This example shows how to communicate between two script components in two separate game objects.

[Project files](https://github.com/defold/examples/tree/master/basics/message_passing)

## Scripts

### spaceship1.script

```lua
local function landed(self) -- <2>
	label.set_text("#speech", "I'm there!")
	msg.post("spaceship2#script", "i'm there")
end

function on_message(self, message_id, message, sender)
	if message_id == hash("go to") then -- <1>
		label.set_text("#speech", "Ok...")
		go.animate(".", "position", go.PLAYBACK_ONCE_FORWARD, message.position, go.EASING_INOUTCUBIC, 1, 0, landed)
	end	
end

--[[
1. If someone sends us a "go to" message, set the speech label text and animate to the position supplied
   in the message data. At the end of animation, call the function `landed()`
2. This function is called when the position animation is completed. It sets the speech label text and then
   sends a message called "i'm there" to the component "script" in the "spaceship2" game object.
--]]
```

### spaceship2.script

```lua
function init(self)
	msg.post(".", "acquire_input_focus") -- <1>
	self.moving = false -- <2>
end

local function landed(self) -- <6>
	self.moving = false
	label.set_text("#speech", "Hey, go to the opposite side!")
	local pos = go.get_position()
	local opposite = vmath.vector3()
	opposite.x = 720 - pos.x
	opposite.y = 720 - pos.y
	msg.post("spaceship1#script", "go to", { position = opposite })
end

function on_message(self, message_id, message, sender)
	if message_id == hash("go to") then -- <5>
		self.moving = true
		label.set_text("#speech", "I'm going...")
		go.animate(".", "position", go.PLAYBACK_ONCE_FORWARD, message.position, go.EASING_INOUTCUBIC, 1.5, 0, landed)
	elseif message_id == hash("i'm there") then -- <7>
		label.set_text("#speech", "Great!")		
	end
end

function on_input(self, action_id, action)
	if action_id == hash("touch") and action.pressed and not self.moving then -- <3>
		local pos = vmath.vector3(action.x, action.y, 0)
		msg.post("#", "go to", { position = pos }) -- <4>
	end
end

--[[
1. Tell the engine that we want to receive input.
2. Store a flag in the current script component instance that tells us if the spaceship is moving or not.
3. If user clicked and the spaceship is not moving.
4. Send a message to this script component ("#" is shorthand for that) saying "go to" and the clicked position
   as part of the message data.
5. If a "go to" message is received, set the speech label text and then animate the position of the current 
   game object ("." is shorthand for that) to the position send in the message data. When the animation is
   done the function `landed()` is called.
6. When `landed()` is called on animation complete, set the label text, then calculate a position on the
   opposite of the screen and send a message called "go to" to the component "script" in the game object
   "spaceship11". Supplied with the message is the opposite position as message data.
7. If someone sends us a message called "i'm there" we react by just changing the speech label text.   
--]]
```
