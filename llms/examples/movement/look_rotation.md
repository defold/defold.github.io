# Look rotation

This example shows how to rotate a game object to look at the object in 3D space.

Source: [https://github.com/defold/examples/tree/master/movement/look_rotation](https://github.com/defold/examples/tree/master/movement/look_rotation)

This example shows how to orient a game object to look at the target game object in 3D space. For this purpose, we created the function `quat_look_rotation` (also called `LookRotation` or `looking_at` in the industry). This function creates a rotation matrix from the forward and upwards vectors and then converts it to a quaternion. The function also handles the case where no upwards direction is specified, using the default (0, 1, 0) in that case.

Note: to properly apply the resulting rotation, you must remember that your game object must face backwards to the "z" axis, i.e. in Defold the "forward" direction is vector (0, 0, -1).

In this demo you can rotate the camera by holding down the mouse button. And also switch "targets" by pressing any key.

The models used in this example are from Kenney's [Prototype Kit](https://kenney.nl/assets/prototype-kit), licensed under CC0.

## Scripts

### look_rotation.script

```lua
--- Creates a rotation with the specified forward and upwards directions.
-- @param forward vector3 The forward direction.
-- @param upwards vector3|nil The upwards direction.
-- @return quat The rotation.
local function quat_look_rotation(forward, upwards)
	-- If no upwards direction is specified, use the default (0, 1, 0)
	upwards = upwards or vmath.vector3(0, 1, 0)

	-- No zero vectors
	if vmath.length_sqr(forward) < 0.0000000001 or vmath.length_sqr(upwards) < 0.0000000001 then
		return vmath.quat()
	end

	-- Create a rotation matrix from the forward and upwards vectors
	local matrix = vmath.matrix4_look_at(vmath.vector3(0), forward, upwards)

	-- Convert the matrix to a quaternion and return it
	return vmath.conj(vmath.quat_matrix4(matrix))
end

local function next_target(self)
	self.target = (self.target or 0) + 1
	if self.target > #self.targets then
		self.target = 1
	end

	local target_id = self.targets[self.target]

	local from = go.get_position("/sword")
	local to = go.get_position(target_id)

	self.target_rotation = quat_look_rotation(to - from)
end

function init(self)
	-- Acquire input focus to receive input events
	msg.post(".", "acquire_input_focus")

	-- List of target objects
	self.targets = {
		"/target1",
		"/target2",
		"/target3"
	}

	-- Set the initial target
	next_target(self)
end

function update(self, dt)
	-- If a target rotation is set, smoothly rotate the sword to face the target
	if self.target_rotation then
		-- Important: we must use vmath.slerp to animate quaternions
		local q = vmath.slerp(0.15, go.get_rotation("/sword"), self.target_rotation)
		go.set_rotation(q, "/sword")
	end
end

function on_input(self, action_id, action)
	-- If the left mouse button (or touch) is pressed, set the next target
	if action_id == hash("mouse_button_left") and action.pressed then
		next_target(self)
	end
end
```
