# Orbit Camera

This example demonstrates how to create script to control a 3D camera with the mouse. Scroll wheel is used to zoom in and out.

[Project files](https://github.com/defold/examples/tree/master/render/orbit_camera)

In this example, we create a script to control a 3D camera using the mouse and mouse scroll wheel.

We added two objects to the collection: a camera (`/camera`) and an object (`/crate`) that we will explore. In the `camera` object, we added the `orbit_camera.script` - the script that controls the camera. The properties defined in the script are:
- `zoom`: the initial zoom level.
- `zoom_speed`: the speed of the zoom.
- `rotation_speed`: the speed of the rotation.
- `offset`: the offset of the camera from the origin. Use it to move the camera away from the origin.

During `init`, the script sets up the camera projection, acquires input focus, and establishes starting values for yaw, pitch, and zoom.

In the `update` loop, the script smoothly interpolates camera rotation and zoom (note: `vmath.lerp` is used and it doesn't depend on the delta time, so the camera will move at different speed on different devices), calculates the camera's rotation and position based on current yaw, pitch, and zoom values, and then updates the camera's position and rotation accordingly. This creates a fluid, responsive camera movement!

The function `on_input` handles user input to control the camera. As the user moves the mouse or touches the screen, the script adjusts the yaw and pitch values, allowing the camera to rotate around its focal point. Additionally, it responds to mouse wheel input, adjusting the zoom level to move the camera closer to or further from the center point.

The model used in this example is from Kenney's [Prototype Pack](https://kenney.nl/assets/prototype-kit), licensed under CC0.

## Scripts

### orbit_camera.script

```lua
-- The initial zoom level
go.property("zoom", 3)
-- The speed of the zoom
go.property("zoom_speed", 0.1)
-- The speed of the rotation
go.property("rotation_speed", 0.5)
-- The offset of the camera from the origin
go.property("offset", vmath.vector3(0, 0, 0))

function init(self)
	-- Acquire input focus to receive input events
	msg.post(".", "acquire_input_focus")

	-- Initialize start values
	self.yaw = go.get(".", "euler.y")
	self.pitch = go.get(".", "euler.x")
	self.zoom_offset = 0
	self.current_yaw = self.yaw
	self.current_pitch = self.pitch
	self.current_zoom = self.zoom_offset
end

function update(self, dt)
	-- Animate camera rotation and zoom
	self.current_yaw = vmath.lerp(0.15, self.current_yaw, self.yaw)
	self.current_pitch = vmath.lerp(0.15, self.current_pitch, self.pitch)
	self.current_zoom = vmath.lerp(0.15, self.current_zoom, self.zoom_offset)

	-- Calculate rotation and position
	local camera_yaw = vmath.quat_rotation_y(math.rad(self.current_yaw))
	local camera_pitch = vmath.quat_rotation_x(math.rad(self.current_pitch))
	local camera_rotation = camera_yaw * camera_pitch
	local camera_position = self.offset + vmath.rotate(camera_rotation, vmath.vector3(0, 0, self.zoom + self.current_zoom))

	-- Set camera position and rotation
	go.set_position(camera_position)
	go.set_rotation(camera_rotation)
end

function on_input(self, action_id, action)
	if action_id == hash("touch") and not action.pressed then
		self.yaw   = self.yaw   - action.dx * self.rotation_speed
		self.pitch = self.pitch + action.dy * self.rotation_speed
	elseif action_id == hash("mouse_wheel_up") then
		self.zoom_offset = self.zoom_offset - self.zoom * self.zoom_speed
	elseif action_id == hash("mouse_wheel_down") then
		self.zoom_offset = self.zoom_offset + self.zoom * self.zoom_speed
	end
end
```
