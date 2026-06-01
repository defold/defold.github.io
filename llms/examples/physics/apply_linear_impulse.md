# Apply Linear Impulse

Apply a linear impulse to a dynamic physics body on click or touch.

[Project files](https://github.com/defold/examples/tree/master/physics/apply_linear_impulse)

This example shows how a Box2D body can be pushed instantly with a linear impulse.

## What You'll Learn

- How to get the Box2D body from a collision object.
- How to apply an impulse at a world position.
- How to receive touch and mouse input in a script.

## Setup

The collection contains a cube game object with a sprite, a dynamic collision object, and `/example/apply_linear_impulse.script`. A static platform collision object catches the cube after the impulse. The project enables fixed-step physics and uses Box2D through Defold's built-in `b2d` API.

## How It Works

The script acquires input focus and listens for the built-in `touch` action. When the player clicks or touches the screen, it gets the cube's Box2D body, reads the body's current center of mass, and applies an upward linear impulse at that point.

Read more about the [Box2D API here](https://defold.com/ref/stable/b2d-lua/).

## Scripts

### apply_linear_impulse.script

```lua
function init(self)
	msg.post(".", "acquire_input_focus") -- <1>
end

function on_input(self, action_id, action)
	if action_id == hash("touch") and action.pressed then -- <2>
		local body = b2d.get_body("#collisionobject") -- <3>
		local center = b2d.body.get_world_center(body) -- <4>

		b2d.body.apply_linear_impulse(body, vmath.vector3(0, 600, 0), center) -- <5>
	end
end

function final(self)
	msg.post(".", "release_input_focus") -- <6>
end

--[[
1. The cube game object receives touch and mouse input.
2. The built-in touch action is sent when clicking or touching the screen.
3. b2d.get_body() gets the Box2D body from the cube collision object.
4. The body's world center of mass is used as the impulse application point.
5. apply_linear_impulse() immediately changes the body's velocity upward.
6. Input focus is released when the script instance is destroyed.
--]]
```
