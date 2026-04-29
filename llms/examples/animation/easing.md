# Easing Functions (Tweens)

Demonstrates different easing functions available in Defold.

[Project files](https://github.com/defold/examples/tree/master/animation/easing)

This example compares the built-in easing constants that can be passed to `go.animate()`. Use the left and right arrow keys, or the on-screen buttons, to switch easing function and restart the same position, rotation, and scale animations.

## What You'll Learn

- How to pass built-in `go.EASING_*` constants to `go.animate()`
- How `go.PLAYBACK_LOOP_PINGPONG` moves a property back and forth
- How one script can animate different transform properties through script property overrides
- How a controller can restart several game objects by sending messages

## Setup

The collection contains one controller, one HUD, and three animated logo game objects:

`demo`
: Contains `controller.script`. It owns the current easing index, listens for left and right arrow input, and sends restart messages to the animated game objects.

`position_demo`
: Contains a logo sprite and `animator.script`. Its script properties override the start and end positions.

`rotation_demo`
: Contains a logo sprite and `animator.script`. Its script properties override the end Euler rotation.

`scale_demo`
: Contains a logo sprite and `animator.script`. Its script properties override the end scale.

`hud`
: Contains the GUI that shows the easing name, the easing graph, and the previous/next buttons.

## How It Works

`controller.script` loads the table of easing constants from `easing_functions.lua`. When the selected index changes, it sends the chosen easing value to each animated game object in a `"restart"` message.

Each animated game object uses the same `animator.script`. The script exposes start and end values for position, Euler rotation, and scale. In the collection, each game object overrides only the values it needs, so the position demo moves, the rotation demo rotates, and the scale demo scales.

When `animator.script` receives a new easing value, it resets its game object to the configured start transform and starts a ping-pong property animation toward the configured end transform. The target values and duration stay the same while the selected easing constant changes the interpolation curve.

Read more about property animations in the [manual](https://defold.com/manuals/property-animation/).

## Scripts

### animator.script

```lua
go.property("start_position", vmath.vector3()) -- <1>
go.property("end_position", vmath.vector3())
go.property("start_rotation", vmath.vector3())
go.property("end_rotation", vmath.vector3())
go.property("start_scale", vmath.vector3(1, 1, 1))
go.property("end_scale", vmath.vector3(1, 1, 1))
go.property("duration", 2)

local RESTART = hash("restart")

local function should_animate_position(self)
	return self.start_position ~= self.end_position -- <2>
end

local function should_animate_rotation(self)
	return self.start_rotation ~= self.end_rotation
end

local function should_animate_scale(self)
	return self.start_scale ~= self.end_scale
end

local function reset_position_rotation_scale(self)
	if should_animate_position(self) then
		go.set_position(self.start_position) -- <3>
	end
	if should_animate_rotation(self) then
		go.set(".", "euler", self.start_rotation)
	end
	if should_animate_scale(self) then
		go.set_scale(self.start_scale)
	end
end

local function animate(self)
	reset_position_rotation_scale(self)
	if should_animate_position(self) then
		go.animate(".", "position", go.PLAYBACK_LOOP_PINGPONG, self.end_position, self.easing, self.duration) -- <4>
	end
	if should_animate_rotation(self) then
		go.animate(".", "euler", go.PLAYBACK_LOOP_PINGPONG, self.end_rotation, self.easing, self.duration)
	end
	if should_animate_scale(self) then
		go.animate(".", "scale", go.PLAYBACK_LOOP_PINGPONG, self.end_scale, self.easing, self.duration)
	end
end

function on_message(self, message_id, message)
	if message_id == RESTART then
		self.easing = message.easing -- <5>
		animate(self)
	end
end

--[[
1. These script properties can be overridden per game object in the collection. The example uses one script for all three demos and changes only the relevant start/end values.
2. A transform property is animated only when its start and end values differ. The position demo changes position, the rotation demo changes Euler rotation, and the scale demo changes scale.
3. Reset the game object before starting the animation so every easing function begins from the same visual state.
4. `go.animate()` uses ping-pong playback to animate from the start value to the end value and back again in a loop.
5. The controller sends the selected built-in `go.EASING_*` constant in a `restart` message.
]]
```

### controller.script

```lua
local EASING_FUNCTIONS = require("example.easing_functions") -- <1>
local DEMO_URLS = { "position_demo", "rotation_demo", "scale_demo" } -- <2>

local PREVIOUS = -1
local NEXT = 1
local PREV_EASING_DEMO = hash("prev_easing_demo")
local NEXT_EASING_DEMO = hash("next_easing_demo")
local DEMO_CHANGED = hash("demo_changed")
local KEY_LEFT = hash("key_left")
local KEY_RIGHT = hash("key_right")
local RESTART = hash("restart")

local function wrap_index(index)
	if index < 1 then
		return #EASING_FUNCTIONS
	elseif index > #EASING_FUNCTIONS then
		return 1
	end
	return index
end

local function restart_demo_animations(easing)
	for _, url in ipairs(DEMO_URLS) do
		msg.post(url, RESTART, { easing = easing.value }) -- <3>
	end
end

local function update_gui(self)
	msg.post("/hud#gui", DEMO_CHANGED, { -- <4>
		index = self.index,
		total = #EASING_FUNCTIONS,
		easing_name = self.easing.name
	})
end

local function change_easing_demo(self, index_change)
	self.index = wrap_index(self.index + index_change) -- <5>
	self.easing = EASING_FUNCTIONS.get_by_index(self.index)
	restart_demo_animations(self.easing)
	update_gui(self)
end

function init(self)
	msg.post(".", "acquire_input_focus") -- <6>
	self.index = 1
	self.easing = EASING_FUNCTIONS.get_by_index(self.index)
	restart_demo_animations(self.easing)
	update_gui(self)
end

function final(self)
	msg.post(".", "release_input_focus")
end

function on_message(self, message_id)
	if message_id == PREV_EASING_DEMO then
		change_easing_demo(self, PREVIOUS)
	elseif message_id == NEXT_EASING_DEMO then
		change_easing_demo(self, NEXT)
	end
end

function on_input(self, action_id, action)
	if action_id == KEY_LEFT and action.pressed then -- <7>
		change_easing_demo(self, PREVIOUS)
	elseif action_id == KEY_RIGHT and action.pressed then
		change_easing_demo(self, NEXT)
	end
end

--[[
1. The helper module stores the built-in easing constants together with display names for the HUD.
2. These child game objects all use `animator.script`, but their script property overrides make them animate different transform properties.
3. The controller does not animate the logos directly. It sends the selected easing constant to each animator in a `restart` message.
4. The HUD receives only presentation data: the current index, total count, and easing name.
5. Wrap the index so pressing left on the first easing function jumps to the last one, and pressing right on the last jumps back to the first.
6. The controller acquires input focus so it can receive keyboard actions from the built-in input binding.
7. The left and right arrow keys step through the easing list.
]]
```
