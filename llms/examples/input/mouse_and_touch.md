# Mouse and Touch Events

Shows how to read mouse and/or touch movement and mouse button/touch state.

[Project files](https://github.com/defold/examples/tree/master/input/mouse_and_touch)

This example shows how to receive mouse and touch input in a script and display the current pointer position and button state.

Move the mouse or touch the window to update the label.
Press and release the left mouse button or touch the screen to see the state change.

## What You'll Learn

* How to acquire and release input focus
* How to read pointer coordinates from `action.x` and `action.y`
* How to handle the built-in `touch` action for mouse and touch input
* How to use `action.pressed` and `action.released`

## Setup

The collection contains one game object with `mouse_and_touch.script` and one label component. The script receives input and updates the label text with the current pointer position and state.

The project uses the built-in `/builtins/input/all.input_bindingc` input binding.
In that binding, the left mouse button and touch input are already mapped to the `touch` and `touch_multi` actions.
You can create and setup your own input bindings, and remember to adjust the action ids in the scripts accordingly.

## How It Works

The script asks for input focus in `init()`. After that, Defold calls `on_input()` when mouse or touch input is received.

Each input action contains the current pointer position in `action.x` and `action.y`. When the action id is `hash("touch")` or `hash("touch_multi")`, the script checks `action.pressed` and `action.released` to update a small state string.

The label text is written again with the pointer coordinates and the state to the local label component with `label.set_text()`.

## Scripts

### mouse_and_touch.script

```lua
function init(self)
	msg.post(".", "acquire_input_focus") -- <1>
	self.state = "released"
end

local TOUCH_ACTION_ID = hash("touch")
local TOUCH_MULTI_ACTION_ID =hash("touch_multi")

function on_input(self, action_id, action)
	local pos = vmath.vector3(action.x, action.y, 0) -- <2>
	if action_id == TOUCH_ACTION_ID or action_id == TOUCH_MULTI_ACTION_ID then  -- <3>
		if action.pressed then -- <4>
			self.state = "pressed"
		elseif action.released then -- <5>
			self.state = "released"
		end
	end
	local text = ("x: %d y: %d state: %s"):format(pos.x, pos.y, self.state) -- <6>
	label.set_text("#label", text)
end

function final(self)
	msg.post(".", "release_input_focus") -- <7>
end

--[[
1. Tell the engine that this object ("." is shorthand for the current game object) wants to receive input. The function `on_input()` will be called whenever input is received.
2. Read the position of the mouse pointer or touch event.
3. The left mouse button in the input bindings will also be used for touch events on a phone/tablet.
4. The 'pressed' state will be true starting on the frame when the mouse button/finger is pressed.
5. The 'released' state will be true starting on the frame when the mouse button/finger is released.
6. Rebuild the text to include the position and state and then set this text to the label.
7. In `final` release the input focus.
--]]
```
