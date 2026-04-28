# Cancel animation

This example shows how to use `go.cancel_animations()` to stop a running animation and start a new one.

[Project files](https://github.com/defold/examples/tree/master/animation/cancel_animation)

The collection contains two game objects:
- `ship` with one sprite and one script.
- `description` with a label for displaying the instructions text

## How It Works

The script starts an animation of movement along the X axis in `init()`. The ship starts moving to the right and back. Then it listens for input so it can interrupt that animation.

Clicking or tapping cancels the currently played animations immediately and starts a new one to move the ship toward the new x position instead.

When the player presses the mouse button or touches the screen, the script first calls [`go.cancel_animations()`](https://defold.com/ref/go-lua/index.html#go.cancel_animations:url-property). Defold stops the running tween and leaves the game object's position exactly where it was at that moment.

The script then calls [`go.animate()`](https://defold.com/ref/go-lua/index.html#go.animate:url-property-playback-to-easing-duration-delay-complete_function) again with the clicked x coordinate as the new target. Because the old animation was canceled first, the new tween starts from the ship's current position instead of jumping back to the original starting point.

## Scripts

### cancel_animation.script

```lua
function init(self)
	msg.post(".", "acquire_input_focus") -- <1>
	go.animate(".", "position.x", go.PLAYBACK_ONCE_FORWARD, 600, go.EASING_INOUTSINE, 5.0) -- <2>
end

function on_input(self, action_id, action)
	if (action_id == hash("mouse_button_left") or action_id == hash("touch")) and action.pressed then -- <3>
		go.cancel_animations(".", "position") -- <4>
		go.animate(".", "position.x", go.PLAYBACK_ONCE_FORWARD, action.x, go.EASING_INOUTSINE, 1.2) -- <5>
	end
end

--[[
1. Acquire input focus so the script receives mouse clicks and touch presses.
2. Start with a long horizontal animation toward x = 600 so there is something to interrupt.
3. React to either a left mouse click or a touch press.
4. Cancel the running position animation. Defold keeps the property at its current value when the animation is canceled.
5. Start a new animation from that current x position toward the clicked x coordinate.
]]
```
