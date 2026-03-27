# Apply force

This example demonstrates how to apply directional force to all dynamic blocks on touch/click and draws debug direction lines.

[Project files](https://github.com/defold/examples/tree/master/physics/apply_force)

This example demonstrates how to apply directional force to all dynamic blocks on touch/click and draws debug direction lines.

## Setup

Scene consists of a few game objects:

- `controller`
  - Main object that contains `/example/apply_force.script` and a label with usage text.
- `block1`, `block2`, `block3`, `block4`
  - Dynamic rigid bodies (sprite + dynamic collision object).
- `walls`
  - Static boundary collision object around the screen.

Proposed settings regarding physics in the `game.project` file:

## Script flow

A single controller script handles input for the whole scene.
When you touch/click, it loops over all dynamic blocks, computes a force vector for each one, applies the force, and draws a debug line that visualizes the direction.

1. acquires input focus in `init()`
2. listens to `hash("touch")` in `on_input()`
3. iterates over all block ids
4. computes `force = (touch - center) * force_factor`
5. posts `apply_force` to each block
6. posts `@render: draw_line` for debug visualization

## Scripts

### apply_force.script

```lua
-- Multiplier applied to the touch->block direction vector.
local force_factor = 30

-- Debug line color used by @render:draw_line.
local debug_line_color = vmath.vector4(0, 0.5, 1, 1)

-- Game object ids of dynamic blocks controlled by this script.
-- The script is attached to the "controller" object in the collection.
local blocks = {
	[1] = "block1",
	[2] = "block2",
	[3] = "block3",
	[4] = "block4",
}

function init(self)
	-- <1> Receive touch/mouse input in on_input().
	msg.post(".", "acquire_input_focus")
end

-- Pre-hashed action id for the touch action.
local touch_action_id = hash("touch")

function on_input(self, action_id, action)
	-- <2> Built-in "touch" also maps mouse clicks on desktop.
	if action_id == touch_action_id then
		-- <3> Iterate over all blocks and apply force to each.
		for _, block in pairs(blocks) do
			-- <4> Compute the force vector by subtracting the block center from the touch position.
			local center = go.get_world_position(block)
			local touch = vmath.vector3(action.x, action.y, center.z)
			local force = (touch - center) * force_factor

			-- <5> Send force to the block's dynamic collision object.
			msg.post(block, "apply_force", {
				force = force,
				position = center
			})

			-- <6> Visualize direction from touch point to block center.
			msg.post("@render:", "draw_line", {
				start_point = touch,
				end_point = center,
				color = debug_line_color
			})
		end
	end
end

function final(self)
	-- Stop receiving input when the controller is destroyed.
	msg.post(".", "release_input_focus")
end
```
