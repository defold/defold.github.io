# Kinematic physics

This example shows a simple setup with a kinematic physics objects. The difference between dynamic objects, simulated by the physics engine, and kinematic objects, that are user controlled, is clearly seen here.

Source: [https://github.com/defold/examples/tree/master/physics/kinematic](https://github.com/defold/examples/tree/master/physics/kinematic)

The setup consists of three game objects. The *game.project* physics *GravityY* property is set to -500 to match the scale of the setup.

block
: The square stone block. Contains:
  - A *Sprite* component with the stone block image.
  - A *Collision object* component. The *Type* is set to `KINEMATIC`. A box *Shape* matching the sprite image is added to the components.
  - A script that moves the game object to where the user clicks.

block2
: The rectangular stone block. Contains:
  - A *Sprite* component with the stone block image.
  - A *Collision object* component. Also has *Type* set to `DYNAMIC`, *Friction* set to 0 and *Restitution* to 1.0. A box *Shape* matching the sprite image is added to the components.

walls
: The outer walls. Contains:
  - A *Collision object* component. The *Type* is set to `STATIC`. 4 box *Shapes* are added to the component. These are placed just outside of the game view.

## Scripts

### kinematic.script

```lua
function init(self)
    msg.post(".", "acquire_input_focus") -- <1>
    self.moving = false -- <2>
end

local function landed(self) -- <9>
    self.moving = false
end

function on_input(self, action_id, action)
    if action_id == hash("touch") and action.pressed then -- <3>
		if not self.moving then -- <4>
			msg.post("#label", "disable") -- <5>
			self.moving = true -- <6>
			pos = vmath.vector3(action.x, action.y, 0) -- <7>
			go.animate(".", "position", go.PLAYBACK_ONCE_FORWARD, pos, go.EASING_LINEAR, 0.5, 0, landed) -- <8>
		end
	end
end

--[[
1. Tell the engine that this object ("." is shorthand for the current game object) should listen to input. Any input will be received in the `on_input()` function.
2. Store a flag in `self` (the current script component) to indicate if the game object is moving or not.
3. If we receive an input action named "touch" and it is pressed then run the following.
4. If the `moving` flag is not set.
5. Disable (don't show) the help text label.
6. Set the `moving` flag.
7. Create a new position called `pos` (of type `vector3`) where the user clicked.
8. Animate the game object's ("." is shorthand for the current game object) position to `pos`.
   When the animation is done, call the function `landed()`.
9. The function `landed()` is called when the animation is done. It just resets the `moving` flag
   so subsequent clicks will result in a new movement.
--]]
```
