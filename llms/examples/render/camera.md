# Camera

This example shows how to use a camera component and have it follow a game object. Click to toggle between following the game object and staying stationary.

Source: [https://github.com/defold/examples/tree/master/render/camera](https://github.com/defold/examples/tree/master/render/camera)

The setup consists of one `bee` game object that the camera can follow and one `camera` game object containing the camera component. The camera component will when active send view and projection updates to the render script.

bee
: The bee. Contains:
  - A *Sprite* component with the bee image.
  - A script that tells the camera whether it should follow the game object or not.

camera
: The camera. Contains:
  - A *Camera* component. The camera component has Orthographic Projection enabled.
  - A script that controls the camera component.

## Scripts

### bee.script

```lua
function init(self)
	msg.post(".", "acquire_input_focus")
	go.animate(".", "position.x", go.PLAYBACK_LOOP_PINGPONG, 2000, go.EASING_INOUTQUAD, 10) -- <1>
	msg.post("camera", "follow") -- <2>
	self.follow = true -- <3>
end


function on_input(self, action_id, action)
	if action_id == hash("touch") and action.pressed then -- <4>
		self.follow = not self.follow
		if self.follow then
			msg.post("camera", "follow")
		else
			msg.post("camera", "unfollow")
		end
	end
end

--[[
1. Move this game object back and forth across the scene.
2. Send a message to the camera game object telling it to follow this game object.
3. Keep track of if the camera is following this game object or not.
4. Toggle between following and not following the game object when the left mouse button is clicked or the screen is touched.
--]]
```

### camera.script

```lua
function on_message(self, message_id, message, sender)
	if message_id == hash("follow") then -- <1>
		go.set_parent(".", sender) -- <2>
	elseif message_id == hash("unfollow") then -- <3>
		go.set_parent("camera", nil, true)
	end
end

--[[
1. Start following the game object that sent the `follow` message.
2. This is done by parenting the camera component to the game object that sent the message.
3. Stop following any game object. This is done removing the parent game object while maintaining the current world transform.
--]]
```
