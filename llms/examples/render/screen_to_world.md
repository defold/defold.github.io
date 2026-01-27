# Screen to World

This example shows how to convert from screen to world coordinates while using a camera.

[Project files](https://github.com/defold/examples/tree/master/render/screen_to_world)

The `bee.script` uses the `camera.screen_to_world()` function to convert from screen space coordinates to world coordinates using the view and projection of a camera component.

## Scripts

### bee.script

```lua
function init(self)
	-- send input events to this script
	msg.post(".", "acquire_input_focus")
end

function on_input(self, action_id, action)
	if action_id == hash("touch") and action.pressed then
		-- convert mouse/touch screen position to world position
		local screen = vmath.vector3(action.screen_x, action.screen_y, 0)
		local world = camera.screen_to_world(screen, "#camera")

		-- alternative using camera.screen_xy_to_world(x, y, camera)
		-- local world = camera.screen_xy_to_world(action.screen_x, action.screen_y, v)

		-- animate bee to new world position
		go.animate(".", "position", go.PLAYBACK_ONCE_FORWARD, world, go.EASING_LINEAR, 0.5, 0)
	end
end
```
