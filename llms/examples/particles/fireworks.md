# Spawning Fireworks ParticleFX

This example shows how to spawn firework rockets with separate trail and burst particle effects, including a small dip before the burst.

[Project files](https://github.com/defold/examples/tree/master/particles/fireworks)

## Setup

The collection contains:

- one controller game object with `fireworks.script`;
- six embedded factories: one `trail` factory and one `splat` factory for each of the three colors;
- one GUI component that shows the click/tap instruction on screen.

Each firework is built from two separate particlefx game objects:

- a looping `trail` effect that represents the rocket while it is flying;
- a one-shot `splat` effect that represents the explosion at the end.

The script does not use `update()`. It spawns the trail object, animates it with `go.animate()`, and starts the burst effect from the animation callback when the flight finishes.

## Trail particlefx

Each `trail` particlefx file contains one looping cone emitter. The three color variants share the same setup and only differ in their base RGB values.

The trail emitter uses:

- `Emmision Space` : `World`, so emitted particles stay behind in world space instead of following the moving game object;
- `Particle Orientation` : `Movement direction`;
- additive blending;
- the `fw_circle_01` sprite from `/assets/sprites.atlas`;
- a spawn rate of `64`, particle lifetime `0.6`, and particle size around `40` with a small spread.

Because the sprite is a soft circle rather than a directional streak, the trail reads more like a glowing puff stream than a sharp rocket spark. The scale and alpha curves in the emitter make each particle start fairly full, then shrink and fade out quickly.

The trail game object itself is prepared by the script before the animation starts:

- position is set near the bottom of the screen;
- scale is animated down over time so the trail feels like it is burning out before the explosion.

## Burst particlefx

Each `splat` particlefx file is a one-shot layered burst built from five circle emitters. The red, green and blue files use the same emitter structure and timings, with color values changed per variant.

The five burst layers are:

- a `fw_trace_01` streak layer with movement-direction orientation, about `64` particles, lifetime around `1.6`, speed around `200`, and velocity stretching;
- a `fw_star_01` star layer with angular-velocity orientation, about `30` particles, lifetime around `1.6`, speed around `300`, and randomized rotation;
- a second `fw_trace_01` streak layer with additive blending for extra brightness;
- a `fw_light_01` flash layer that emits a single large soft light particle;
- a second additive `fw_light_01` layer that adds a smaller glow on top of the main flash.

The moving burst layers also use modifiers. The streak layers use acceleration, and the star and additive streak layers also use radial shaping, so the burst does not expand as a perfectly uniform circle. The two `fw_light_01` emitters do not throw particles outward; they behave more like expanding flashes at the center of the explosion.

Like the trail, the burst emitters also use `Emmision Space` : `World`, so the explosion stays fixed at the burst position after it has been spawned.

## Script and spawning

The script handles spawning in three ways:

- it launches one firework in `init()`;
- it starts a repeating timer that launches another firework every 3 seconds;
- it launches another firework when the left mouse button is pressed, which also works as click/tap input in the example.

To keep the effect under control, the script allows at most 16 active fireworks at the same time.

`spawn_firework()` first checks that limit. It then:

- picks a random color from `red`, `green` and `blue`;
- creates the matching trail and burst game objects with `factory.create()`;
- generates a random launch angle, launch strength and flight time;
- computes the initial position near the bottom of the screen, a peak position, and a burst position slightly below that peak;
- starts the trail particlefx;
- starts `go.animate()` for `position.x`, `position.y` and `scale`.

The values that control this motion are collected at the top of the script, including:

- launch strength and angle range;
- start position and horizontal spread;
- flight time and flight-distance ratio;
- how much of the total flight is used for the final dip;
- the minimum and maximum distance of that dip.

The rocket flight uses two separate property animations:

- `position.x` uses linear easing;
- `position.y` first uses `go.EASING_OUTQUAD` to rise to the peak, then `go.EASING_INQUAD` to dip slightly before the burst;
- `scale` is animated down during the flight.

Using different easing for X and Y gives a simple curved flight path without a manual simulation loop. Splitting the Y animation into two phases lets the rocket rise, dip a little, and then explode. When the second Y animation finishes, its completion callback stops and deletes the trail object, reads its final position, and plays the burst effect there. A separate one-shot timer then deletes the burst object after a short cleanup delay.

To reuse this setup in another project:

- add factories for the trail and burst particlefx game objects;
- spawn both objects with `factory.create()`;
- choose a start position, a target position and a flight time;
- animate the trail object with `go.animate()`;
- trigger and clean up the burst effect from the animation callback.

Particle sprites are CC0 from Kenney Particle Pack.

## Scripts

### fireworks.script

```lua
local COLORS = { "red", "green", "blue" }
local MAX_ACTIVE_FIREWORKS = 8
local AUTO_LAUNCH_DELAY = 3
local BURST_CLEANUP_DELAY = 1.5
local LAUNCH_STRENGTH_MIN = 400
local LAUNCH_STRENGTH_RANGE = 300
local LAUNCH_ANGLE_MIN = -0.28 * math.pi
local LAUNCH_ANGLE_RANGE = 0.56 * math.pi
local START_POSITION_X = 360
local START_POSITION_Y = 0
local START_POSITION_SPREAD = 350
local FLIGHT_TIME_MIN = 1.2
local FLIGHT_TIME_RANGE = 0.5
local FLIGHT_DISTANCE_RATIO = 0.55
local FALL_PHASE_RATIO = 0.2
local FALL_DISTANCE_MIN = 5
local FALL_DISTANCE_MAX = 35
local TRAIL_END_SCALE = 0.2

local active_fireworks = 0 -- <1>

local function delete_burst(burst_id)
	go.delete(burst_id) -- <2>
	active_fireworks = active_fireworks - 1 -- <3>
end

local function burst_firework(trail_id, burst_id)
	local position = go.get_position(trail_id) -- <4>
	particlefx.stop(trail_id, { clear = true }) -- <5>
	go.delete(trail_id) -- <6>
	go.set_position(position, burst_id) -- <7>
	particlefx.play(burst_id) -- <8>

	timer.delay(BURST_CLEANUP_DELAY, false, function() -- <9>
		delete_burst(burst_id)
	end)
end

local function spawn_firework()
	if active_fireworks >= MAX_ACTIVE_FIREWORKS then -- <10>
		return
	end

	local color = COLORS[math.random(#COLORS)] -- <11>
	local trail_id = factory.create("#" .. color .. "_trail_factory") -- <12>
	local burst_id = factory.create("#" .. color .. "_splat_factory") -- <13>

	local launch_strength = LAUNCH_STRENGTH_MIN + math.random() * LAUNCH_STRENGTH_RANGE -- <14>
	local launch_angle = LAUNCH_ANGLE_MIN + math.random() * LAUNCH_ANGLE_RANGE -- <15>
	local start_position = vmath.vector3(START_POSITION_X - math.sin(launch_angle) * START_POSITION_SPREAD, START_POSITION_Y, 0) -- <16>
	local flight_time = FLIGHT_TIME_MIN + math.random() * FLIGHT_TIME_RANGE -- <17>
	local velocity = vmath.vector3(launch_strength * math.sin(launch_angle), launch_strength * math.cos(launch_angle), 0)
	local peak_position = start_position + velocity * flight_time * FLIGHT_DISTANCE_RATIO -- <18>
	local fall_distance = FALL_DISTANCE_MIN + math.random() * (FALL_DISTANCE_MAX - FALL_DISTANCE_MIN)
	local end_position = peak_position - vmath.vector3(0, fall_distance, 0)
	local rise_time = flight_time * (1 - FALL_PHASE_RATIO)
	local fall_time = flight_time * FALL_PHASE_RATIO

	go.set_position(start_position, trail_id) -- <19>
	particlefx.play(trail_id) -- <20>
	active_fireworks = active_fireworks + 1 -- <21>

	go.animate(trail_id, "position.x", go.PLAYBACK_ONCE_FORWARD, end_position.x, go.EASING_LINEAR, flight_time) -- <22>
	go.animate(trail_id, "position.y", go.PLAYBACK_ONCE_FORWARD, peak_position.y, go.EASING_OUTQUAD, rise_time, 0, function()
		go.animate(trail_id, "position.y", go.PLAYBACK_ONCE_FORWARD, end_position.y, go.EASING_INQUAD, fall_time, 0, function() -- <23>
			burst_firework(trail_id, burst_id) -- <24>
		end)
	end)
	go.animate(trail_id, "scale", go.PLAYBACK_ONCE_FORWARD, TRAIL_END_SCALE, go.EASING_INQUAD, flight_time) -- <25>
end

function init(self)
	spawn_firework() -- <26>
	timer.delay(AUTO_LAUNCH_DELAY, true, spawn_firework) -- <27>
	msg.post(".", "acquire_input_focus") -- <28>
end

function on_input(self, action_id, action)
	if action_id == hash("mouse_button_left") and action.pressed then
		spawn_firework() -- <29>
	end
end

--[[
1. Keep a count of active fireworks so no more than 16 are running at once.
2. Delete the burst game object after its cleanup delay has finished.
3. Free one active firework slot when the burst object is removed.
4. Read the trail object's current position so the burst can be played there.
5. Stop the trail particle effect and clear already emitted particles when the flight ends.
6. Delete the trail game object once it has finished flying.
7. Move the burst object to the trail object's last position.
8. Play the burst particle effect at that position.
9. Start a one-shot timer that cleans up the burst after a short delay.
10. Stop spawning if the maximum number of active fireworks is already on screen.
11. Pick one of the available firework colors.
12. Create the trail game object for that color.
13. Create the burst game object for that color.
14. Randomize the launch strength so different rockets travel different distances.
15. Randomize the launch angle so the fireworks spread out across the screen.
16. Compute a start position near the bottom edge, offset by the launch angle.
17. Randomize how long the rocket flight lasts before it bursts.
18. Compute a peak position for the rocket, then offset the burst point downward so it dips a bit before exploding.
19. Place the trail object at the launch position.
20. Start the trail particle effect.
21. Reserve one active firework slot for this spawned rocket.
22. Animate the rocket horizontally with linear easing.
23. Animate the rocket upward first, then run a short downward animation before bursting.
24. Start the burst effect when the flight animation finishes.
25. Animate the rocket scale down over time so the trail looks like it is burning out.
26. Launch one firework immediately when the example starts.
27. Start a repeating timer that spawns another firework every 3 seconds.
28. Acquire input focus so the script can react to click or tap input.
29. Launch another firework when the left mouse button or a touch press is detected.
]]
```
