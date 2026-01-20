# Particle effect example - confetti

This example shows a simple particle effect to imitate confetti.

[Project files](https://github.com/defold/examples/tree/master/particles/confetti)

In this example we create a confetti fireworks effect. It is usually used on final screens to congratulate the player on successful completion of a level or game.

The particlefx consists of 6 emitters. They are all the same, but with different images and RGB colors.

It has two modifiers:
 - Acceleration to make the particles fly downwards, i.e. to simulate gravity.
 - Drag to slow down the initial speed of the particles.

Changed properties (from default):
 - Blend Mode: Alpha for transparency blending
 - Max Particle Count: 8 to limit number of particles
 - Emitter Type: 2D Cone to set initial direction of the particles
 - Spawn Rate: 500 to spawn all particles at once
 - Emitter Size X: 100 +/- 20
 - Initial Speed: 1500 +/- 300 to make particles fly upwards

In addition, the curves for Life Scale, Life Alpha, Life Rotation properties have been adjusted to make the particles look like real confetti.

The main script `confetti.script` spawns the particlefx on startup or when any key is pressed or the mouse button is clicked. It also has a timer that spawns the particlefx in a loop with a 3 second delay.

## Scripts

### confetti.script

```lua
local function single_shot()
	particlefx.play("#particles") -- <1>
end

function init(self)
	single_shot()

	timer.delay(3, true, single_shot) -- <2>

	msg.post(".", "acquire_input_focus")
end

function on_input(self, action_id, action)
	if action_id == hash("mouse_button_left") and action.pressed then -- <3>
		single_shot()
	end
end

--[[
1. Start playing the particle effect in component "particles" in this game object.
2. Setup timer to do a single shot of confetti every 3 seconds.
3. Play the effect when left mouse button (or touch) is pressed.
--]]
```
