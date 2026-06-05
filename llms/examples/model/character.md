# Character - Skeletal Animation

This example shows how to play skeletal animations on a glTF character model and trigger them from GUI buttons.

[Project files](https://github.com/defold/examples/tree/master/model/character)

This example uses a skinned glTF character with multiple animations and a simple orbit camera. The model contains both mesh and animation data, so the example can switch animations and visible mesh parts without loading any extra assets.

## What You'll Learn

- How to play named skeletal animations from a glTF model
- How to toggle mesh parts on a skinned model to change the visible equipment
- How to use Defold's built-in skinned model material for animated meshes
- How to orbit a camera around a 3D character
- How to trigger animations from GUI buttons

## Setup

The collection contains five game objects: `floor`, `wall`, `player`, `camera`, and `gui`.

`floor`
: Contains a Model component using `floor_tile_large.gltf.glb` with the dungeon texture. It forms the ground plane of the scene.

`wall`
: Contains a Model component using `wall.gltf.glb` with the same dungeon texture. It closes off the back of the room.

`player`
: Contains `player.script` and a skinned Model component using `Knight.glb` and `knight_texture.png`. The animated `knight_texture` material slot uses `/builtins/materials/model_skinned.material`, which supports the skeleton skinning used by the character mesh. The glTF file includes the character meshes, skeleton, and animation clips.

`camera`
: Contains a Camera component and `orbit_camera.script`. Drag or touch to orbit around the character, and use the mouse wheel to zoom. The script exposes `zoom`, `min_zoom`, `max_zoom`, `zoom_speed`, `rotation_speed`, and `offset` as properties so the camera can be tuned from the collection.

`gui`
: Contains `example.gui` and `example.gui_script`. The GUI shows a short instruction label plus five buttons labeled `1` to `5`. Clicking or tapping them sends animation messages to the player.

## How It Works

`player.script` starts the model in `Idle`, then enables the mesh parts that define the chosen loadout. Pressing keys `1` to `5`, or clicking the GUI buttons, calls `model.play_anim()` with different animation names stored in the glTF file.

`example.gui_script` uses `gui.pick_node()` to detect which button was clicked or tapped. It sends the chosen animation name to the player with `msg.post()`, so the GUI stays decoupled from the model logic.

The orbit camera script keeps the character centered while the player drags, touches, or scrolls. Zoom changes are clamped between the `min_zoom` and `max_zoom` properties, making it easy to inspect the animation from different angles without moving the character itself.

The model and assets are [made by Kay Lousberg](https://kaylousberg.com/game-assets/).

## Scripts

### player.script

```lua
local function play_animation(name)
	model.play_anim("#model", name, go.PLAYBACK_LOOP_FORWARD)
end

function init(self)
	msg.post(".", "acquire_input_focus") -- <1>
	play_animation("Idle") -- <2>

	model.set_mesh_enabled("#model", "1H_Sword", true) -- <3>
	model.set_mesh_enabled("#model", "1H_Sword_Offhand", false)
	model.set_mesh_enabled("#model", "2H_Sword", false)

	model.set_mesh_enabled("#model", "Knight_Helmet", true)
	model.set_mesh_enabled("#model", "Knight_Cape", true)

	model.set_mesh_enabled("#model", "Spike_Shield", true)
	model.set_mesh_enabled("#model", "Round_Shield", false)
	model.set_mesh_enabled("#model", "Rectangle_Shield", false)
	model.set_mesh_enabled("#model", "Badge_Shield", false)
end

function on_message(self, message_id, message, sender)
	if message_id == hash("play_idle") then -- <4>
		play_animation("Idle")
	elseif message_id == hash("play_walk") then
		play_animation("Walking_A")
	elseif message_id == hash("play_attack") then
		play_animation("1H_Melee_Attack_Chop")
	elseif message_id == hash("play_block") then
		play_animation("Block")
	elseif message_id == hash("play_cheer") then
		play_animation("Cheer")
	end
end

function on_input(self, action_id, action)
	if action_id == hash("key_1") then
		play_animation("Idle") -- <5>
	elseif action_id == hash("key_2") then
		play_animation("Walking_A") -- <6>
	elseif action_id == hash("key_3") then
		play_animation("1H_Melee_Attack_Chop") -- <7>
	elseif action_id == hash("key_4") then
		play_animation("Block") -- <8>
	elseif action_id == hash("key_5") then
		play_animation("Cheer") -- <9>
	end
end

--[[
1. Acquire input focus so the number keys are sent to the script.
2. Start with the model's Idle animation.
3. Enable the mesh parts that define the visible weapon, helmet, cape, and shield.
4. Accept animation messages from the GUI and play the requested animation.
5. Play the idle animation.
6. Play the walking animation.
7. Play the chop attack animation.
8. Play the block animation.
9. Play the cheer animation.
]]
```

### orbit_camera.script

```lua
go.property("zoom", 3) -- <1>
go.property("min_zoom", 3) -- <2>
go.property("max_zoom", 20) -- <3>
go.property("zoom_speed", 0.1) -- <4>
go.property("rotation_speed", 0.5) -- <5>
go.property("offset", vmath.vector3(0, 0, 0)) -- <6>

local function clamp_zoom(self)
	self.zoom_offset = math.min(math.max(self.zoom + self.zoom_offset, self.min_zoom), self.max_zoom) - self.zoom
end

function init(self)
	msg.post(".", "acquire_input_focus") -- <7>

	self.yaw = go.get(".", "euler.y") -- <8>
	self.pitch = go.get(".", "euler.x")
	self.zoom_offset = 0
	clamp_zoom(self)
	self.current_yaw = self.yaw
	self.current_pitch = self.pitch
	self.current_zoom = self.zoom_offset
end

function update(self, dt)
	self.current_yaw = vmath.lerp(0.15, self.current_yaw, self.yaw) -- <9>
	self.current_pitch = vmath.lerp(0.15, self.current_pitch, self.pitch)
	self.current_zoom = vmath.lerp(0.15, self.current_zoom, self.zoom_offset)

	local camera_yaw = vmath.quat_rotation_y(math.rad(self.current_yaw))
	local camera_pitch = vmath.quat_rotation_x(math.rad(self.current_pitch))
	local camera_rotation = camera_yaw * camera_pitch
	local camera_position = self.offset + vmath.rotate(camera_rotation, vmath.vector3(0, 0, self.zoom + self.current_zoom))

	go.set_position(camera_position) -- <10>
	go.set_rotation(camera_rotation)
end

function on_input(self, action_id, action)
	if action_id == hash("touch") and not action.pressed then
		self.yaw = self.yaw - action.dx * self.rotation_speed -- <11>
		self.pitch = self.pitch + action.dy * self.rotation_speed
	elseif action_id == hash("mouse_wheel_up") then
		self.zoom_offset = self.zoom_offset - self.zoom * self.zoom_speed -- <12>
		clamp_zoom(self)
	elseif action_id == hash("mouse_wheel_down") then
		self.zoom_offset = self.zoom_offset + self.zoom * self.zoom_speed -- <13>
		clamp_zoom(self)
	end
end

--[[
1. Default zoom distance from the model.
2. Minimum allowed zoom distance.
3. Maximum allowed zoom distance.
4. Zoom speed multiplier for the mouse wheel.
5. Rotation speed multiplier for drag and touch input.
6. Camera offset from the model origin.
7. Enable input so drag, touch, and wheel events reach the script.
8. Store the starting camera angles from the current game object rotation.
9. Smooth the camera toward the target rotation and zoom.
10. Apply the computed camera position every frame.
11. Drag or touch rotates the camera around the model.
12. Mouse wheel up zooms in, then clamps the zoom distance.
13. Mouse wheel down zooms out, then clamps the zoom distance.
]]
```

### example.gui_script

```lua
local BUTTONS = {
	{ node = "button_1", message = hash("play_idle") },
	{ node = "button_2", message = hash("play_walk") },
	{ node = "button_3", message = hash("play_attack") },
	{ node = "button_4", message = hash("play_block") },
	{ node = "button_5", message = hash("play_cheer") },
}

local function post_animation(message_id)
	msg.post("player#player", message_id)
end

function init(self)
	msg.post(".", "acquire_input_focus") -- <1>

	self.buttons = {}
	for i = 1, #BUTTONS do
		self.buttons[i] = {
			node = gui.get_node(BUTTONS[i].node),
			message = BUTTONS[i].message,
		}
	end
end

function on_input(self, action_id, action)
	if (action_id == hash("touch") or action_id == hash("mouse_button_left")) and action.pressed then -- <2>
		for i = 1, #self.buttons do
			local button = self.buttons[i]
			if gui.pick_node(button.node, action.x, action.y) then -- <3>
				post_animation(button.message) -- <4>
				break
			end
		end
	end
end

--[[
1. Acquire input focus so the GUI receives clicks and touches.
2. React to mouse or touch press events.
3. Check whether the pointer landed on one of the button nodes.
4. Send the selected animation message to the player script.
]]
```
