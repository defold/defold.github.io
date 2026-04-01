# Orthographic Zoom

This example shows how to zoom an orthographic camera in and out by changing Orthographic Zoom while the camera is in Fixed mode.

[Project files](https://github.com/defold/examples/tree/master/render/orthographic_zoom)

This example shows the recommended setup for gameplay zoom with an orthographic camera: keep the camera component in orthographic `Fixed` mode, then change `orthographic_zoom` from script.

## Setup

The setup consists of three parts:

- `camera` - game object containing the `camera` component, the `zoom.script`, and a `label` that displays the current zoom value. The `camera` component has `Orthographic Projection` enabled and `Orthographic Zoom Mode` set to `Fixed` with `Orthographic Zoom` set to `1.0` initially.

- `tilemap`- a simple level tilemap that makes the zoom effect easy to see as you move between a closer and wider view.

- `gui` - a GUI scene with a short instruction label describing the available controls.

## How it works

* Scrolling the mouse wheel changes the camera zoom in small fixed steps.
* Clicking or touching and moving up and down changes the zoom continuously based on the pointer delta.
* The script clamps the zoom between minimum and maximum values before writing it back to the camera component, so the example stays within a useful range.

Because the camera is in orthographic `Fixed` mode, the zoom behavior is controlled directly by the `orthographic_zoom` value instead of being recalculated by another orthographic mode.

## Credits

This project uses the following free art assets:
- Pixel Art Top Down Basic tilesets by Cainos: [https://cainos.itch.io/pixel-art-top-down-basic](https://cainos.itch.io/pixel-art-top-down-basic)

## Scripts

### zoom.script

```lua
-- Local constants to define maximum and minimum zoom:
local MIN_ZOOM = 0.75
local MAX_ZOOM = 3.0

-- Local constants to define how fast zooming is on input:
local SCROLL_ZOOM_STEP = 0.1
local DRAG_ZOOM_SCALE = 0.01

-- Helper function to update the label with information on current zoom value.
local function update_zoom_label(zoom)
	label.set_text("#zoom_label", string.format("Orthographic Zoom: %.2f", zoom))
end

-- Helper function to clamp the zoom between minimum and maximum values.
local function clamp_zoom(zoom)
	return math.min(MAX_ZOOM, math.max(MIN_ZOOM, zoom))
end

-- Helper function to set the new clamped zoom on the camera component and update label.
local function set_zoom(self, zoom)
	self.zoom = clamp_zoom(zoom)
	go.set("#camera", "orthographic_zoom", self.zoom)
	update_zoom_label(self.zoom)
end

function init(self)
	-- Acquire input focus for the example:
	msg.post(".", "acquire_input_focus")

	-- You can set manually the orthographic mode to fixed too
	-- (optional, as we set it in the component already):
	camera.set_orthographic_mode("#camera", camera.ORTHO_MODE_FIXED)

	-- Get the current zoom of the camera component:
	self.zoom = go.get("#camera", "orthographic_zoom")

	-- Update the information about zoom on the label:
	update_zoom_label(self.zoom)
end

function on_input(self, action_id, action)
	-- Handle input on mouse scroll and touch/click:
	if action_id == hash("mouse_wheel_up") then
		-- Increasing zoom makes the orthographic camera zoom in.
		set_zoom(self, self.zoom + SCROLL_ZOOM_STEP)
	elseif action_id == hash("mouse_wheel_down") then
		-- Decreasing zoom makes the orthographic camera zoom out.
		set_zoom(self, self.zoom - SCROLL_ZOOM_STEP)
	elseif action_id == hash("touch") and not action.pressed and not action.released then
		-- While dragging, use the vertical pointer delta for continuous zoom control.
		-- Positive `action.dy` means the pointer moved up on screen.
		go.cancel_animations("#camera", "orthographic_zoom")
		set_zoom(self, self.zoom + action.dy * DRAG_ZOOM_SCALE)
	end
end
```
