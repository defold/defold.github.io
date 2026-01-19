# Look at

This example shows how to rotate a game object to look at the mouse cursor

Source: [https://github.com/defold/examples/tree/master/movement/look_at](https://github.com/defold/examples/tree/master/movement/look_at)

This example shows how to rotate a game object to look at the mouse cursor. It reads the mouse position in `on_input` and uses the mathematical function `math.atan2(x, y)` to calculate the angle between the ray to the point to look at and the positive x-axis. This angle is used to set the rotation of the game object to always look at the mouse position. 

The example is suitable for the movement in two dimensions, for platformers or top-down games. For 3D objects, check out the [next example](/examples/movement/look_rotation/).

## Scripts

### look_at.script

```lua
function init(self)
	-- make sure the script will receive user input
	msg.post(".", "acquire_input_focus")
end

local function look_at(target_position)
	-- own positon
	local my_position = go.get_position()

	-- calculate the angle that this object has to rotate to look at the given point
	local angle = math.atan2(my_position.x - target_position.x, target_position.y - my_position.y)
	-- set rotation as a quaternion
	go.set_rotation(vmath.quat_rotation_z(angle))
end

function on_input(self, action_id, action)
	-- mouse/finger movement has action_id set to nil
	if not action_id then
		-- the position to look at (mouse/finger)
		local target_position = vmath.vector3(action.x, action.y, 0)
		-- rotate this object to look at the target position
		look_at(target_position)
	end
end
```
