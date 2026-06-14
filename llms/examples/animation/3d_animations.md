# 3D Animations - Skinned Model

Learn how to play 3D animations from a GLB model using skinned model material.

[Project files](https://github.com/defold/examples/tree/master/animation/3d_animations)

This example shows how to play skeletal animations from a skinned GLB model using `model.play_anim()`.

Click or tap any button to play the matching animation on the character. The selected button is dimmed to show the currently chosen animation.

The project uses a character from the [Quaternius Universal Animation Library](https://quaternius.itch.io/universal-animation-library).

## What You'll Learn

* How to play skeletal model animations with `model.play_anim()`
* How to use `model_skinned.material` for animated skinned models
* How to build a simple GUI animation picker
* How to detect GUI button clicks with `gui.pick_node()`
* How to send animation commands from a GUI script to a game object script with `msg.post()`

## Setup

The collection contains 4 game objects:

`character`
: Contains the model component and `main.script`. The model component uses the animated GLB model and the built-in `/builtins/materials/model_skinned.material`.

`gui`
: Contains `main.gui` and `main.gui_script`. The GUI contains one button for each animation clip. The button boxes are placed on the `boxes` layer, and the text labels are placed on the `texts` layer so the labels render above the boxes.

`plane`
: Contains a simple static model for the floor.

`camera`
: Contains a camera component to show the setup in game.

The model must use a skinned material. If the model uses `/builtins/materials/model.material`, the animation can be started in code, but the mesh will not visibly follow the skeleton. For skeletal animation, use `/builtins/materials/model_skinned.material`.

## How It Works

The standard free file version contains 45 animation clips, including idle, walk, jog, sprint, crouch, jump, swimming, spell, pistol, punch, and sword animations.
The GUI lists them as buttons. Clicking a button sends a message from the GUI script to the model script, which then plays the selected animation on the model component.

The model script owns animation playback. It defines a message id called `play_model_animation` and starts a default animation in `init()`:
```lua
local MSG_PLAY_MODEL_ANIMATION = hash("play_model_animation")
local DEFAULT_ANIMATION = hash("Sword_Idle")

local function play_animation(animation_id)
	model.play_anim("#model", animation_id, go.PLAYBACK_LOOP_FORWARD)
end

function init(self)
	play_animation(DEFAULT_ANIMATION)
end
```

When the script receives a `play_model_animation` message, it reads the animation id from the message and plays that animation on the local model component:
```lua
function on_message(self, message_id, message, sender)
	if message_id == MSG_PLAY_MODEL_ANIMATION then
		play_animation(message.animation_id)
	end
end
```

The GUI script owns the button list and input handling. It stores all animation names in an `ANIMATIONS` table. During `init()`, it finds the matching GUI nodes, sets the button text, and stores each button node together with its animation name.

The GUI script also acquires input focus:
```lua
msg.post(".", "acquire_input_focus")
```

When the user clicks or taps, `on_input()` checks every button with `gui.pick_node()`. If the pointer is inside a button, the GUI script sends a message to the model script:
```lua
msg.post(MODEL_SCRIPT, MSG_PLAY_MODEL_ANIMATION, {
	animation_id = hash(button.animation_id),
	animation_name = button.animation_id,
})
```

The GUI script does not call `model.play_anim()` directly. This keeps the GUI responsible only for interface and input, while the model game object remains responsible for model animation playback.

## Messages from GUI to Game objects

The GUI component and the model component live on different game objects. Instead of making the GUI script directly control the model component, the GUI sends a small command message:
```lua
play_model_animation
```

This is a common Defold pattern. The sender does not need to know how animation playback is implemented. It only sends the requested animation id. The receiver decides what to do with it.

This makes the example easy to extend. For example, the model script could later add animation blending, validation, transition rules, sound effects, or root motion handling without changing the GUI script.

## Scripts

### main.script

```lua
local MSG_PLAY_MODEL_ANIMATION = hash("play_model_animation") -- <1>
local DEFAULT_ANIMATION = hash("Sword_Idle") -- <2>

local function play_animation(animation_id)
	model.play_anim("#model", animation_id, go.PLAYBACK_LOOP_FORWARD) -- <3>
end

function init(self)
	play_animation(DEFAULT_ANIMATION) -- <4>
end

function on_message(self, message_id, message, sender)
	if message_id == MSG_PLAY_MODEL_ANIMATION then -- <5>
		play_animation(message.animation_id)
	end
end

-- <1> This message id is shared with the GUI script. The GUI does not call the model API directly; it asks this script to play an animation.
-- <2> The character starts in a known default pose/animation before the user selects anything from the GUI.
-- <3> model.play_anim() is called on the model component attached to the same game object as this script. The animation id must match a clip imported from the GLB.
-- <4> Start the default animation when the game object is initialized.
-- <5> React only to the animation-selection message. The selected animation id is sent by the GUI script in the message table.
```

### main.gui_script

```lua
local TOUCH = hash("touch") -- <1>
local MSG_PLAY_MODEL_ANIMATION = hash("play_model_animation") -- <2>
local MODEL_SCRIPT = "/character#main" -- <3>

local ANIMATIONS = { -- <4>
	"A_TPose",
	"Crouch_Fwd_Loop",
	"Crouch_Idle_Loop",
	"Dance_Loop",
	"Death01",
	"Driving_Loop",
	"Fixing_Kneeling",
	"Hit_Chest",
	"Hit_Head",
	"Idle_Loop",
	"Idle_Talking_Loop",
	"Idle_Torch_Loop",
	"Interact",
	"Jog_Fwd_Loop",
	"Jump_Land",
	"Jump_Loop",
	"Jump_Start",
	"PickUp_Table",
	"Pistol_Aim_Down",
	"Pistol_Aim_Neutral",
	"Pistol_Aim_Up",
	"Pistol_Idle_Loop",
	"Pistol_Reload",
	"Pistol_Shoot",
	"Punch_Cross",
	"Punch_Jab",
	"Push_Loop",
	"Roll",
	"Roll_RM",
	"Sitting_Enter",
	"Sitting_Exit",
	"Sitting_Idle_Loop",
	"Sitting_Talking_Loop",
	"Spell_Simple_Enter",
	"Spell_Simple_Exit",
	"Spell_Simple_Idle_Loop",
	"Spell_Simple_Shoot",
	"Sprint_Loop",
	"Swim_Fwd_Loop",
	"Swim_Idle_Loop",
	"Sword_Attack",
	"Sword_Attack_RM",
	"Sword_Idle",
	"Walk_Formal_Loop",
	"Walk_Loop",
}

local function set_button_enabled(button_node, enabled)
	local color = enabled and vmath.vector4(1, 1, 1, 1) or vmath.vector4(0.7, 0.7, 0.7, 1)
	gui.set_color(button_node, color) -- <5>
end

function init(self)
	msg.post(".", "acquire_input_focus") -- <6>

	self.buttons = {} -- <7>
	self.selected_index = nil

	for index, animation_id in ipairs(ANIMATIONS) do -- <8>
		local button_id = "button_" .. string.format("%02d", index)
		local text_id = "button_text_" .. string.format("%02d", index)
		local button_node = gui.get_node(button_id)
		local text_node = gui.get_node(text_id)

		gui.set_text(text_node, animation_id) -- <9>
		set_button_enabled(button_node, true)

		self.buttons[index] = { -- <10>
			node = button_node,
			animation_id = animation_id,
		}
	end
end

function on_input(self, action_id, action)
	if action_id ~= TOUCH or not action.pressed then -- <11>
		return false
	end

	for index, button in ipairs(self.buttons) do
		if gui.pick_node(button.node, action.x, action.y) then -- <12>
			if self.selected_index then
				set_button_enabled(self.buttons[self.selected_index].node, true)
			end

			self.selected_index = index
			set_button_enabled(button.node, false) -- <13>

			msg.post(MODEL_SCRIPT, MSG_PLAY_MODEL_ANIMATION, { -- <14>
				animation_id = hash(button.animation_id),
				animation_name = button.animation_id,
			})

			return true
		end
	end

	return false
end

-- <1> The input binding uses the touch action for both mouse clicks and touch input in this example.
-- <2> This is the same message id used by main.script, so both scripts agree on the command name.
-- <3> GUI scripts cannot address model components directly in a clean way here, so the GUI sends a message to the character script instead.
-- <4> The animation list is ordered to match the generated GUI buttons: button_01 plays the first clip, button_02 the second clip, and so on.
-- <5> The selected button is dimmed by changing the box node color. The text nodes stay unchanged and remain readable on the separate text layer.
-- <6> The GUI must acquire input focus before on_input() receives click/touch events.
-- <7> Store runtime references to the GUI nodes once during init instead of resolving them every click.
-- <8> Button and text node ids are generated from the animation index, matching the button_01/button_text_01 naming convention in main.gui.
-- <9> The visible label is filled from the animation list, so the GUI file does not need to hardcode animation names in every text node.
-- <10> Each button entry stores the clickable box node and the animation id it should request.
-- <11> Ignore all non-press input events. This prevents the same click/touch from triggering repeatedly during release or movement phases.
-- <12> gui.pick_node() tests whether the click position is inside the button box node.
-- <13> Re-enable the previously selected button and dim the newly selected one to show which animation is currently active.
-- <14> Send the selected animation to the model-owning script. The animation is sent as a hash for model.play_anim(), with the string kept only as readable debug/context data.
```
