# Finite State Machines

Shows how to build a small Finite State Machine module and use it to control character and animation states.

[Project files](https://github.com/defold/examples/tree/master/animation/animation_states)

You can control the example in two ways:

- Use the keyboard: `Left`/`Right` arrow keys, `Space`, `X`, and `C`
- Click or touch the on-screen buttons: `idle`, `run`, `turn`, `jump`, `attack`, and `crouch`

The keyboard `C` key is a held crouch input. The GUI `crouch` button toggles crouch on and off.

This example shows how to build a small **Finite State Machine** (FSM) Lua module and use it in more than one place:

- animation states in `knight.script`
- locomotion states (`idle`, `run`) in `control.gui_script`
- posture states (`standing`, `crouching`) in `control.gui_script`

## What You'll Learn

- What Finite State Machines are
- How to create generic FSM logic in a reusable Lua module
- How to use multiple smaller FSMs for different control concerns
- How to combine several control states into one animation target
- How to insert intermediate animation states automatically

### Finite State Machines

A **Finite-State Machine** is a model with a finite set of possible states, one active state at a time, and explicit rules for moving from one state to another. FSMs are used in digital logic, software, and AI because they make behavior depend on clear state and transition rules.

Check also:
- [Simplest Lua Finite State Machine on lua-users.org](http://lua-users.org/wiki/FiniteStateMachine)
- [Lua Finite State Machine by Kyle Conroy](https://github.com/kyleconroy/lua-state-machine)
- [Lua FSM by unindented](https://github.com/unindented/lua-fsm)
- [Lua FSM by recih](https://github.com/recih/lua-fsm)
- ["Simple Lua FSM" video by Mahri2D](https://www.youtube.com/watch?v=aVFMDiaQ_Qc)
- ["How I think of state machines, coded in Defold" video by kags](https://www.youtube.com/watch?v=Hb3GEcTgkrg)

## Setup

The collection contains two game objects:

`gui`
: Contains `control.gui` and `control.gui_script`. This script owns input focus, handles keyboard and pointer input, and uses two FSMs: one for locomotion (`idle` / `run`) and one for posture (`standing` / `crouching`).

`knight`
: Contains the sprite and `knight.script`. This script owns the animation FSM. It stores the current animation state, validates transitions with the reusable FSM module, plays flipbooks, and notifies the GUI whenever the active animation changes.

## Input

The GUI stores raw input intent, then the locomotion and posture FSMs turn that intent into stable control states:

- locomotion FSM: `idle` or `run`
- posture FSM: `standing` or `crouching`

For keyboard movement, the most recently pressed direction key wins. That lets the turn animation finish and continue into a run as long as one movement key is still held.

The example uses these input bindings:

Key Triggers:

- `Space` - jump
- `C` - crouch
- `X` - attack
- `Right` - right
- `Left` - left

Mouse Triggers:

- `Button left` -touch (for left mouse clicks and touch input)

## How It Works

The example separates three different jobs:

### Reusable FSM module

`fsm.lua` contains the generic part:

- create a machine with `new()`
- read state with `get_state_name()` and `get_state()`
- perform direct transitions with `set_state()`
- find multi-step routes with `find_path()`

This keeps the reusable code small and focused.

### Animation FSM

The knight owns one animation FSM with states such as:

- `standing_idle`
- `standing_run`
- `standing_jump`
- `standing_turn`
- `crouching_idle`
- `crouching_run`
- `to_crouch`
- `to_standing`

When the requested animation is not directly reachable, the knight asks `fsm.find_path()` for a legal route and automatically inserts intermediate animation states. This keeps the controller states simple while still allowing animated transitions such as standing up or crouching down.

For example:

- `standing_idle` → `crouching_run` becomes `standing_idle` → `to_crouch` → `crouching_run`
- `crouching_run` → `standing_idle` becomes `crouching_run` → `to_standing` → `standing_idle`

### Control FSMs

The GUI owns two simpler FSMs:

- locomotion FSM: `idle` / `run`
- posture FSM: `standing` / `crouching`

These smaller machines are easier to understand than one larger controller state containing every combination directly.

The GUI combines them into one animation target for the knight:

- `standing` + `idle` -> `standing_idle`
- `standing` + `run` -> `standing_run`
- `crouching` + `idle` -> `crouching_idle`
- `crouching` + `run` -> `crouching_run`

The GUI sends stable looping targets with `set_target_state`. One-shot actions such as jump, attack, and turn are sent separately with `trigger_state`.

## Why Split It Like This?

Using several small FSMs keeps each machine focused on one question:

- locomotion asks: "idle or run?"
- posture asks: "standing or crouching?"
- animation asks: "which exact animation state should play now?"

That is often easier to read and maintain than one large state table that tries to represent every control and animation concern at once.

## Animation Atlas

The sprite component uses a flipbook atlas with the standing, crouching, attack, jump, and transition animations for the knight character.

> This example uses the Free Knight Character by Nauris "aamatniekss":
> https://aamatniekss.itch.io/fantasy-knight-free-pixelart-animated-character

## Scripts

### knight.script

```lua
local fsm = require("example.fsm")

local SET_TARGET_STATE = hash("set_target_state")
local TRIGGER_STATE = hash("trigger_state")
local ANIMATION_DONE = hash("animation_done")
local ANIMATION_STATE_CHANGED = hash("animation_state_changed")

local GUI_URL = "/gui#control"

-- <1>
local ANIMATION_STATES = {
	standing_idle = {
		animation = hash("idle"),
		loop = true
	},
	standing_run = {
		animation = hash("run"),
		loop = true
	},
	standing_jump = {
		animation = hash("jump"),
		loop = false
	},
	standing_attack = {
		animation = hash("attack"),
		loop = false
	},
	standing_turn = {
		animation = hash("turn_around"),
		loop = false
	},
	crouching_idle = {
		animation = hash("crouch_idle"),
		loop = true
	},
	crouching_run = {
		animation = hash("crouch_walk"),
		loop = true
	},
	crouching_attack = {
		animation = hash("crouch_attack"),
		loop = false
	},
	to_crouch = {
		animation = hash("to_crouch"),
		loop = false
	},
	to_standing = {
		animation = hash("from_crouch"),
		loop = false
	}
}

-- <2>
local ANIMATION_TRANSITIONS = {
	standing_idle = { "standing_run", "standing_jump", "standing_attack", "standing_turn", "to_crouch" },
	standing_run = { "standing_idle", "standing_jump", "standing_attack", "standing_turn", "to_crouch" },
	standing_jump = { "standing_idle", "standing_run", "standing_attack", "standing_turn", "to_crouch" },
	standing_attack = { "standing_idle", "standing_run", "standing_jump", "standing_turn", "to_crouch" },
	standing_turn = { "standing_idle", "standing_run", "standing_jump", "standing_attack", "to_crouch" },
	crouching_idle = { "crouching_run", "crouching_attack", "to_standing" },
	crouching_run = { "crouching_idle", "crouching_attack", "to_standing" },
	crouching_attack = { "crouching_idle", "crouching_run", "to_standing" },
	to_crouch = { "crouching_idle", "crouching_run", "crouching_attack" },
	to_standing = { "standing_idle", "standing_run", "standing_jump", "standing_attack", "standing_turn" }
}

-- <3>
local function get_animation_state_name(self)
	return fsm.get_state_name(self.animation_fsm)
end

-- <4>
local function get_animation_state(self)
	return fsm.get_state(self.animation_fsm)
end

-- <5>
local function stop_jump_effect(self)
	local position = go.get_position()
	go.cancel_animations(".", "position.y")
	go.set_position(vmath.vector3(position.x, self.ground_y, position.z))
end

-- <6>
local function start_jump_effect(self)
	stop_jump_effect(self)
	go.animate(".", "position.y", go.PLAYBACK_ONCE_PINGPONG, self.ground_y + 50, go.EASING_INOUTCUBIC, 0.6)
end

-- <7>
local function apply_facing(self)
	self.facing_left = self.desired_facing_left
	sprite.set_hflip("#sprite", self.facing_left)
end

-- <8>
local function refresh_visuals(self, previous_state_name)
	local state = get_animation_state(self)
	local current_state_name = get_animation_state_name(self)

	-- <9>
	if not state or not current_state_name then
		return
	end

	-- <10>
	if previous_state_name == "standing_jump" and current_state_name ~= "standing_jump" then
		stop_jump_effect(self)
	end

	-- <11>
	if current_state_name ~= "standing_turn" then
		apply_facing(self)
	end

	-- <12>
	sprite.play_flipbook("#sprite", state.animation)

	-- <13>
	if current_state_name == "standing_jump" then
		start_jump_effect(self)
	end

	-- <14>
	msg.post(GUI_URL, ANIMATION_STATE_CHANGED, { state = current_state_name })
end

-- <15>
local function enter_animation_state(self, next_state_name)
	local previous_state_name = get_animation_state_name(self)

	-- <16>
	if previous_state_name == next_state_name then
		if next_state_name ~= "standing_turn" then
			apply_facing(self)
		end

		return
	end

	-- <17>
	if not fsm.set_state(self.animation_fsm, next_state_name) then
		return
	end

	refresh_visuals(self, previous_state_name)
end

-- <18>
local function advance_animation_fsm(self, allow_from_finished_state)
	local requested_state = self.trigger_state or self.target_state
	local current_state = get_animation_state(self)

	-- <19>
	if not requested_state then
		return
	end

	-- <20>
	if not allow_from_finished_state and current_state and not current_state.loop then
		return
	end

	-- <21>
	if requested_state == get_animation_state_name(self) then
		enter_animation_state(self, requested_state)
		return
	end

	local path = fsm.find_path(self.animation_fsm, requested_state)

	-- <22>
	if not path then
		return
	end

	-- <23>
	for _, next_state_name in ipairs(path) do
		enter_animation_state(self, next_state_name)

		if not get_animation_state(self).loop then
			return
		end
	end
end

function init(self)
	-- <24>
	self.animation_fsm = fsm.new({
		states = ANIMATION_STATES,
		transitions = ANIMATION_TRANSITIONS
	})

	self.target_state = "standing_idle"
	self.trigger_state = nil
	self.facing_left = false
	self.desired_facing_left = false
	self.ground_y = go.get_position().y

	-- <25>
	enter_animation_state(self, self.target_state)
end

function on_message(self, message_id, message)
	-- <26>
	if message_id == SET_TARGET_STATE then
		self.target_state = message.state
		self.desired_facing_left = message.facing_left
		advance_animation_fsm(self)

	-- <27>
	elseif message_id == TRIGGER_STATE then
		self.trigger_state = message.state
		self.desired_facing_left = message.facing_left
		advance_animation_fsm(self)

	-- <28>
	elseif message_id == ANIMATION_DONE then
		if get_animation_state_name(self) == "standing_turn" then
			apply_facing(self)
		end

		-- <29>
		if self.trigger_state == get_animation_state_name(self) then
			self.trigger_state = nil
		end

		-- <30>
		advance_animation_fsm(self, true)
	end
end

--[[
1. `ANIMATION_STATES` is the data table for the knight animation FSM. Each state only stores the animation id and whether the state loops.
2. `ANIMATION_TRANSITIONS` is the animation graph. The knight may only move along these legal transitions.
3. `get_animation_state_name()` reads the current animation state id from the reusable FSM module.
4. `get_animation_state()` reads the current animation state's data table from the reusable FSM module.
5. `stop_jump_effect()` clears the extra Y movement used to visualize a jump and snaps the knight back to the ground height.
6. `start_jump_effect()` starts the temporary Y animation for the jump. This can stay simple because jump is not cancelable in this example.
7. `apply_facing()` updates the sprite horizontal flip from the direction requested by the GUI controller.
8. `refresh_visuals()` handles the visual side effects of entering a state. It does not choose the next state; it only updates how the current state looks.
9. This guard leaves the helper idle if it is called before the FSM has an active state.
10. When the FSM leaves `standing_jump`, the jump offset is removed so the knight returns to ground level.
11. `standing_turn` is special because the knight should keep the old facing until the turn animation finishes.
12. Every animation state plays its own configured flipbook on the sprite.
13. Entering `standing_jump` also starts the extra Y movement so the jump is easier to see.
14. The knight reports the active animation state to the GUI so the control panel can highlight the correct buttons.
15. `enter_animation_state()` is the one place where the knight animation FSM actually changes state.
16. Re-entering the same state does not restart the flipbook; it only applies a facing change when the state allows immediate facing updates.
17. `fsm.set_state()` performs one legal direct transition. If the transition is invalid, the function stops there.
18. `advance_animation_fsm()` is the main stepper for the animation FSM. It moves the knight toward the latest requested state.
19. If nothing has been requested, there is nothing for the animation FSM to do.
20. If a non-looping state is still playing, the knight waits for `animation_done` before continuing.
21. If the requested state is already active, the knight only needs to apply same-state side effects such as facing.
22. If the reusable FSM module cannot find a legal path, the knight ignores that request.
23. The animation FSM walks along the path until it reaches a non-looping state that must finish before the next step can happen.
24. The knight creates one reusable FSM instance for its animation logic.
25. The knight starts by entering `standing_idle` through the same helper used for all later state changes.
26. `set_target_state` updates the stable looping state the knight should eventually settle into.
27. `trigger_state` starts a one-shot state such as jump, attack, or turn.
28. Because `sprite.play_flipbook()` is called without a completion callback, Defold sends `animation_done` when a non-looping flipbook finishes.
29. After a one-shot trigger finishes, the trigger request is cleared so the knight can continue toward the latest stable target.
30. Passing `true` here allows the FSM to continue from the finished non-looping state instead of stopping on it.
--]]
```

### control.gui_script

```lua
local fsm = require("example.fsm")

local SET_TARGET_STATE = hash("set_target_state")
local TRIGGER_STATE = hash("trigger_state")
local ANIMATION_STATE_CHANGED = hash("animation_state_changed")

local KNIGHT_URL = "/knight#knight"

-- <1>
local INPUT = {
	TOUCH = hash("touch"),
	LEFT = hash("left"),
	RIGHT = hash("right"),
	JUMP = hash("jump"),
	ATTACK = hash("attack"),
	CROUCH = hash("crouch")
}

local DEFAULT_COLOR = vmath.vector4(0.3, 0.4, 0.8, 1.0)
local ACTIVE_COLOR = vmath.vector4(0.4, 0.5, 0.9, 1.0)

-- <2>
local LOCOMOTION_STATES = {
	idle = {},
	run = {}
}

-- <3>
local LOCOMOTION_TRANSITIONS = {
	idle = { "run" },
	run = { "idle" }
}

-- <4>
local POSTURE_STATES = {
	standing = {},
	crouching = {}
}

-- <5>
local POSTURE_TRANSITIONS = {
	standing = { "crouching" },
	crouching = { "standing" }
}

-- <6>
local STATE_HIGHLIGHTS = {
	standing_idle = { "idle" },
	standing_run = { "run" },
	standing_jump = { "jump" },
	standing_attack = { "attack" },
	standing_turn = { "turn_around" },
	crouching_idle = { "crouch" },
	crouching_run = { "run", "crouch" },
	crouching_attack = { "attack", "crouch" },
	to_crouch = { "crouch" },
	to_standing = { "crouch" }
}

-- <7>
local function get_locomotion_state(self)
	return fsm.get_state_name(self.locomotion_fsm)
end

-- <8>
local function get_posture_state(self)
	return fsm.get_state_name(self.posture_fsm)
end

-- <9>
local function update_button_visual(node, is_active)
	gui.set_color(node, is_active and ACTIVE_COLOR or DEFAULT_COLOR)
end

-- <10>
local function refresh_buttons(self, state_name)
	for _, node in pairs(self.buttons) do
		update_button_visual(node, false)
	end

	for _, node_id in ipairs(STATE_HIGHLIGHTS[state_name] or {}) do
		update_button_visual(self.buttons[node_id], true)
	end
end

-- <11>
local function is_keyboard_running(self)
	return self.keyboard_direction_left ~= nil
end

-- <12>
local function refresh_keyboard_direction(self)
	if self.left_down and not self.right_down then
		self.keyboard_direction_left = true
	elseif self.right_down and not self.left_down then
		self.keyboard_direction_left = false
	elseif not self.left_down and not self.right_down then
		self.keyboard_direction_left = nil
	end
end

-- <13>
local function get_requested_direction(self)
	if self.keyboard_direction_left ~= nil then
		return self.keyboard_direction_left
	end

	return self.direction_left
end

-- <14>
local function update_control_fsms(self)
	local next_locomotion_state = "idle"
	local next_posture_state = "standing"

	if self.run_requested or is_keyboard_running(self) then
		next_locomotion_state = "run"
	end

	if self.crouch_toggled or self.crouch_down then
		next_posture_state = "crouching"
	end

	if next_locomotion_state ~= get_locomotion_state(self) then
		fsm.set_state(self.locomotion_fsm, next_locomotion_state)
	end

	if next_posture_state ~= get_posture_state(self) then
		fsm.set_state(self.posture_fsm, next_posture_state)
	end
end

-- <15>
local function get_base_state(self)
	local locomotion_state = get_locomotion_state(self)
	local posture_state = get_posture_state(self)

	if posture_state == "crouching" then
		return locomotion_state == "run" and "crouching_run" or "crouching_idle"
	end

	return locomotion_state == "run" and "standing_run" or "standing_idle"
end

-- <16>
local function send_base_state(self)
	msg.post(KNIGHT_URL, SET_TARGET_STATE, {
		state = get_base_state(self),
		facing_left = self.direction_left
	})
end

-- <17>
local function send_trigger_state(self, state_name)
	msg.post(KNIGHT_URL, TRIGGER_STATE, {
		state = state_name,
		facing_left = self.direction_left
	})
end

-- <18>
local function sync_knight(self, play_turn_animation)
	local previous_direction_left = self.direction_left

	self.direction_left = get_requested_direction(self)
	update_control_fsms(self)

	-- <19>
	if play_turn_animation and previous_direction_left ~= self.direction_left and get_posture_state(self) == "standing" then
		send_trigger_state(self, "standing_turn")
	end

	send_base_state(self)
end

-- <20>
local function request_idle(self)
	self.run_requested = false
	sync_knight(self)
end

-- <21>
local function request_run(self)
	self.run_requested = true
	sync_knight(self)
end

-- <22>
local function request_turn(self)
	self.direction_left = not get_requested_direction(self)

	if get_posture_state(self) == "standing" then
		send_trigger_state(self, "standing_turn")
	end

	send_base_state(self)
end

-- <23>
local function request_jump(self)
	if get_posture_state(self) == "crouching" then
		return
	end

	send_trigger_state(self, "standing_jump")
end

-- <24>
local function request_attack(self)
	local attack_state = get_posture_state(self) == "crouching" and "crouching_attack" or "standing_attack"
	send_trigger_state(self, attack_state)
end

-- <25>
local function request_crouch_toggle(self)
	self.crouch_toggled = not self.crouch_toggled
	sync_knight(self)
end

-- <26>
local function press_button(self, node_id)
	if node_id == "idle" then
		request_idle(self)
	elseif node_id == "run" then
		request_run(self)
	elseif node_id == "turn_around" then
		request_turn(self)
	elseif node_id == "jump" then
		request_jump(self)
	elseif node_id == "attack" then
		request_attack(self)
	elseif node_id == "crouch" then
		request_crouch_toggle(self)
	end
end

-- <27>
local function pick_button(self, x, y)
	for node_id, node in pairs(self.buttons) do
		if gui.pick_node(node, x, y) then
			return node_id
		end
	end

	return nil
end

function init(self)
	-- <28>
	self.buttons = {
		idle = gui.get_node("idle"),
		run = gui.get_node("run"),
		turn_around = gui.get_node("turn_around"),
		jump = gui.get_node("jump"),
		attack = gui.get_node("attack"),
		crouch = gui.get_node("crouch")
	}

	-- <29>
	self.locomotion_fsm = fsm.new({
		states = LOCOMOTION_STATES,
		transitions = LOCOMOTION_TRANSITIONS,
		initial_state = "idle"
	})

	self.posture_fsm = fsm.new({
		states = POSTURE_STATES,
		transitions = POSTURE_TRANSITIONS,
		initial_state = "standing"
	})

	self.left_down = false
	self.right_down = false
	self.keyboard_direction_left = nil
	self.crouch_down = false
	self.crouch_toggled = false
	self.run_requested = false
	self.direction_left = false

	refresh_buttons(self, "standing_idle")

	-- <30>
	msg.post(".", "acquire_input_focus")
	send_base_state(self)
end

function on_input(self, action_id, action)
	-- <31>
	if action_id == INPUT.LEFT then
		if action.pressed then
			self.left_down = true
			self.keyboard_direction_left = true
			sync_knight(self, true)
		elseif action.released then
			self.left_down = false
			refresh_keyboard_direction(self)
			sync_knight(self)
		end

	-- <32>
	elseif action_id == INPUT.RIGHT then
		if action.pressed then
			self.right_down = true
			self.keyboard_direction_left = false
			sync_knight(self, true)
		elseif action.released then
			self.right_down = false
			refresh_keyboard_direction(self)
			sync_knight(self)
		end

	-- <33>
	elseif action_id == INPUT.CROUCH then
		if action.pressed then
			self.crouch_down = true
			sync_knight(self)
		elseif action.released then
			self.crouch_down = false
			sync_knight(self)
		end

	-- <34>
	elseif action_id == INPUT.JUMP and action.pressed then
		request_jump(self)

	-- <35>
	elseif action_id == INPUT.ATTACK and action.pressed then
		request_attack(self)

	-- <36>
	elseif action_id == INPUT.TOUCH and action.pressed then
		local node_id = pick_button(self, action.x, action.y)

		if node_id then
			press_button(self, node_id)
			return true
		end
	end
end

function on_message(self, message_id, message)
	-- <37>
	if message_id == ANIMATION_STATE_CHANGED then
		refresh_buttons(self, message.state)
	end
end

--[[
1. `INPUT` stores the action hashes used by the GUI controller.
2. `LOCOMOTION_STATES` defines one small control FSM with the states `idle` and `run`.
3. `LOCOMOTION_TRANSITIONS` says that locomotion may move back and forth between `idle` and `run`.
4. `POSTURE_STATES` defines another control FSM with the states `standing` and `crouching`.
5. `POSTURE_TRANSITIONS` says that posture may move back and forth between `standing` and `crouching`.
6. `STATE_HIGHLIGHTS` maps animation states to the GUI buttons that should be highlighted.
7. `get_locomotion_state()` reads the current state of the locomotion FSM.
8. `get_posture_state()` reads the current state of the posture FSM.
9. `update_button_visual()` changes one button between its default and active color.
10. `refresh_buttons()` redraws the whole control panel from the animation state reported by the knight.
11. Keyboard running stays active while at least one direction key is held.
12. `refresh_keyboard_direction()` keeps the most recently active keyboard direction and clears it only when both direction keys are released.
13. `get_requested_direction()` uses the active keyboard direction when present, otherwise it keeps the direction remembered from GUI controls.
14. `update_control_fsms()` derives the locomotion and posture states from the stored run and crouch input flags.
15. `get_base_state()` combines the two control FSM states into one stable looping animation target for the knight.
16. `send_base_state()` tells the knight which looping animation state it should settle into next.
17. `send_trigger_state()` starts one-shot states such as jump, attack, or turn.
18. `sync_knight()` is the main controller helper. It updates direction, advances the two control FSMs, and then sends the correct animation requests.
19. A standing direction change can play the dedicated turn animation, but crouching just changes facing immediately because there is no crouch turn state.
20. Clicking the idle button clears the stored run request.
21. Clicking the run button sets the stored run request.
22. Clicking the turn button flips direction but keeps the current locomotion and posture states.
23. Jump is only requested while the posture FSM is in the `standing` state.
24. Attack chooses the standing or crouching attack from the current posture FSM state.
25. Toggling crouch changes the raw crouch intent, and then the two controller FSMs derive the correct stable states from it.
26. `press_button()` translates GUI node names into controller actions.
27. `pick_button()` checks which on-screen button was clicked.
28. `init()` caches the GUI nodes used by the control panel.
29. The GUI creates two reusable FSM instances: one for locomotion and one for posture.
30. The GUI script owns input focus, then sends the initial idle target to the knight.
31. Left key input updates both the raw held-key state and the active keyboard direction.
32. Right key input works the same way as left key input.
33. Keyboard crouch behaves like a held input, so pressing and releasing it directly updates the raw crouch flag.
34. Jump input sends a one-shot jump request.
35. Attack input sends a one-shot attack request.
36. The mouse or single-touch action uses `gui.pick_node()` so the on-screen buttons work as controls.
37. The GUI only changes its highlights when the knight reports a new active animation state.
--]]
```
