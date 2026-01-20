# Cancel timer example

This example shows how to create timer and cancel it anytime, using built-in timer API.

[Project files](https://github.com/defold/examples/tree/master/timer/cancel_timer)

The example shows how to use Defold built-in timer and uses two indicators:

1. A particlefx gui node that is triggered every 1s.
2. A text node with an information displaying.

The particle fx is played every 1s showing small eruption.
You can click anywhere to cancel the timer and the particlefx won't be triggered anymore.

## Scripts

### cancel_timer.gui_script

```lua
function init(self)
	local interval = 1		-- <1>
	local repeating = true	-- <2>

	self.timer = timer.delay(interval, repeating, function()	-- <3>
		local node = gui.get_node("particlefx")					-- <4>
		gui.play_particlefx(node)								-- <5>
	end)

	msg.post(".", "acquire_input_focus")	-- <6>
end

function on_input(self, action_id, action)
	if action_id == hash("touch") and action.pressed then	-- <7>
		timer.cancel(self.timer)							-- <8>
		local node = gui.get_node("info")					-- <9>
		gui.set_text(node, "Timer cancelled.")				-- <10>
	end
end

--[[
1. We will use interval of 1 (s).
2. We will be repeating the timer endlessly.
3. Start the timer with interval (1s) and repeating (true) and pass a callback function.
	Store the handle to the timer in self.timer.
4. Get the particle fx node.
5. Play particle fx in each call of the callback function of the timer.
6. Tell the engine that this game object wants to receive input.
7. If the user clicks.
8. Cancel the timer using the saved self.timer handle.
9. Get the text node.
10. Update text node with an information that the timer was cancelled.
--]]
```
