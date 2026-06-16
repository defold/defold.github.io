# Box2D Mouse Joint

Create a mouse joint that pulls dynamic bodies toward a moving target.

[Project files](https://github.com/defold/examples/tree/master/physics/box2d_mouse_joint)

This example shows how to create and control Box2D mouse joints from Lua. A visible target point moves automatically until you move the mouse or drag a touch point. Two dynamic bodies follow the same target with different spring settings, making the softer joint stretch behind the target while the tighter joint follows more closely.

## What You'll Learn

- How to get Box2D bodies from collision object components with `b2d.get_body()`.
- How to create a mouse joint with `b2d.joint.create_mouse()`.
- How `frequency` (V2) or `hertz` (V3), `damping_ratio`, and `max_force` affect spring-like motion.
- How to update the joint target every frame with `b2d.joint.set_mouse_target()`.

## Setup

The collection contains 5 game objects:

`controller`
: Contains both backend scripts, `box2d_mouse_joint_v2.script` and `box2d_mouse_joint_v3.script`. Each script checks the active Box2D version and only one script runs.

`target`
: Contains the visible target sprite and a static collision object. The static body is used as the mouse-joint anchor.

`soft_body`
: Contains the orange sprite and a dynamic collision object. This body is connected with lower spring frequency/hertz and damping, so it follows the target more softly.

`tight_body`
: Contains the blue sprite and a dynamic collision object. This body is connected with higher spring frequency/hertz, damping, and max force, so it follows the target more tightly.

`info`
: Contains labels for the soft body, tight body, input instruction, and active Box2D backend.

The project uses `box2D_V2.appmanifest` by default. To compare the newer backend, switch the native extension app manifest in `game.project` to `box2D_V3.appmanifest`.

## How It Works

The mouse joint connects the invisible static body to a dynamic body. The joint does not move the body instantly. Instead, it applies a limited spring-damper force toward the target position. This is why the body can stretch, overshoot, and settle.

The V2 script uses `frequency` and `damping_ratio` in the joint definition. The V3 script uses `hertz` and `damping_ratio`. Both scripts then call `b2d.joint.set_mouse_target()` every frame so the target can move continuously.

The example creates two mouse joints with different values. The orange body uses a lower frequency/hertz and lower damping, so it visibly lags behind. The blue body uses a higher frequency/hertz, more damping, and a larger max force, so it feels tighter and follows the target more directly.

## Scripts

### box2d_mouse_joint_v3.script

```lua
local TOUCH = hash("touch")

local START_TARGET = vmath.vector3(360, 420, 0)
local SOFT_START = vmath.vector3(270, 310, 0)
local TIGHT_START = vmath.vector3(450, 310, 0)

local SOFT_LINE_COLOR = vmath.vector4(1.0, 0.65, 0.22, 1.0)
local TIGHT_LINE_COLOR = vmath.vector4(0.35, 0.85, 1.0, 1.0)
local TARGET_LINE_COLOR = vmath.vector4(0.45, 1.0, 0.65, 1.0)

local function draw_line(from, to, color)
	-- <1> Draw a debug/helper line through the render socket.
	-- These lines are not persistent scene objects. They exist for one frame,
	-- so the script redraws them every update.
	msg.post("@render:", "draw_line", {
		start_point = from,
		end_point = to,
		color = color
	})
end

local function set_target(self, position)
	-- <2> Store the current mouse-joint target as a world-space position.
	-- The mouse joint does not connect to a real "mouse body". It tracks this
	-- world point, which we later pass to b2d.joint.set_mouse_target().
	self.target = vmath.vector3(position.x, position.y, 0)

	-- <3> Move the visible target marker so users can see what point the
	-- mouse joints are trying to follow.
	go.set_position(self.target, self.target_url)
end

local function reset_body(body, position)
	-- <4> Teleport the physics body to a known start position.
	-- b2d.body.set_transform() directly sets the Box2D body's world transform.
	-- This is useful for setup/reset, but should generally not be used every
	-- frame for normal gameplay motion because it bypasses physical simulation.
	b2d.body.set_transform(body, position, 0)

	-- <5> Clear leftover motion so both bodies start the example cleanly.
	b2d.body.set_linear_velocity(body, vmath.vector3())
	b2d.body.set_angular_velocity(body, 0)

	-- <6> Wake the body so Box2D immediately simulates it after the reset.
	-- This is safer here than relying on b2d.joint.wake_bodies(), which may not
	-- be available in all beta/V2 runtime builds.
	b2d.body.set_awake(body, true)
end

local function setup_body(body)
	-- <7> Disable gravity for this body.
	-- A mouse joint is easiest to understand when the only visible force is the
	-- spring-like pull toward the target, not gravity pulling the body downward.
	b2d.body.set_gravity_scale(body, 0)

	-- <8> Prevent rotation.
	-- This keeps the demo visually focused on mouse-joint translation/stretching
	-- instead of the boxes spinning while they follow the target.
	b2d.body.set_fixed_rotation(body, true)

	-- <9> Add linear damping.
	-- This damps velocity over time and helps the bodies settle instead of
	-- sliding forever after the target moves.
	b2d.body.set_linear_damping(body, 1.5)
end

local function create_mouse_joints(self)
	-- <10> Get native Box2D body handles from Defold collision object components.
	-- b2d.get_body() takes a collision object URL and returns the b2Body handle
	-- used by the new Box2D scripting API.
	local anchor_body = b2d.get_body(msg.url(nil, "target", "collisionobject"))
	self.soft_body = b2d.get_body(msg.url(nil, "soft_body", "collisionobject"))
	self.tight_body = b2d.get_body(msg.url(nil, "tight_body", "collisionobject"))

	setup_body(self.soft_body)
	setup_body(self.tight_body)

	reset_body(self.soft_body, SOFT_START)
	reset_body(self.tight_body, TIGHT_START)

	-- <11> Create the softer mouse joint.
	-- A mouse joint connects two Box2D bodies, but its main job is to make body_b
	-- follow a world-space target point. Here the target object acts as the
	-- static reference body, and soft_body is the dynamic body being pulled.
	self.soft_joint = b2d.joint.create_mouse(anchor_body, self.soft_body, {
		-- <12> Initial world target. This will be updated every frame later.
		target = self.target,

		-- <13> Maximum force the joint is allowed to apply.
		-- Lower values make the body lag behind more because the joint cannot
		-- instantly pull it to the target.
		max_force = 850,

		-- <14> Spring frequency in Box2D V3 terms.
		-- Lower hertz means a softer, slower spring.
		hertz = 1.5,

		-- <15> Damping ratio controls how much oscillation is removed.
		-- Lower damping allows more elastic movement and visible overshoot.
		damping_ratio = 0.35,

		-- <16> The connected bodies should not collide with each other.
		-- This is usually what you want for a joint demonstration.
		collide_connected = false,
	})

	-- <17> Create the tighter mouse joint.
	-- It follows the same target, but with much stronger spring settings.
	self.tight_joint = b2d.joint.create_mouse(anchor_body, self.tight_body, {
		target = self.target,

		-- <18> Higher max_force lets the joint pull harder.
		max_force = 6500,

		-- <19> Higher hertz means the spring reacts faster and feels stiffer.
		hertz = 8.0,

		-- <20> Higher damping removes oscillation, so the body follows in a
		-- tighter, more controlled way.
		damping_ratio = 0.9,

		collide_connected = false,
	})
end

local function update_auto_target(self, dt)
	if self.user_control then
		return
	end

	-- <21> Animate the target before the user touches/clicks.
	-- This keeps the example alive on the website even without interaction.
	self.time = self.time + dt

	set_target(self, vmath.vector3(
	360 + math.cos(self.time * 1.35) * 170,
	395 + math.sin(self.time * 1.10) * 95,
	0
))
end

local function update_joints(self)
-- <22> Update both mouse joints with the current target.
-- This is the key runtime control call. The joint was created once in init(),
-- but its target can be changed every frame.
b2d.joint.set_mouse_target(self.soft_joint, self.target)
b2d.joint.set_mouse_target(self.tight_joint, self.target)

-- <23> Make sure the bodies are awake when the target moves.
-- Sleeping bodies may not visibly react until woken by the simulation.
b2d.body.set_awake(self.soft_body, true)
b2d.body.set_awake(self.tight_body, true)
end

local function draw_connections(self)
-- <24> Query the current simulated body positions from Box2D.
-- We draw lines from the target to each body to visualize the stretch of
-- each mouse joint.
local soft_position = b2d.body.get_position(self.soft_body)
local tight_position = b2d.body.get_position(self.tight_body)

draw_line(self.target, soft_position, SOFT_LINE_COLOR)
draw_line(self.target, tight_position, TIGHT_LINE_COLOR)

-- <25> Draw a small cross at the target point so the user can clearly see
-- what the bodies are following.
draw_line(self.target + vmath.vector3(-18, 0, 0), self.target + vmath.vector3(18, 0, 0), TARGET_LINE_COLOR)
draw_line(self.target + vmath.vector3(0, -18, 0), self.target + vmath.vector3(0, 18, 0), TARGET_LINE_COLOR)
end

function init(self)
-- <26> Run this script only when the active Box2D backend is V3.
-- The same collection can include both V2 and V3 scripts, but only one
-- should initialize depending on the current app manifest/backend.
self.active = b2d.get_version().major == 3

if not self.active then
	return
end

self.target_url = msg.url(nil, "target", nil)
self.time = 0
self.user_control = false

set_target(self, START_TARGET)
create_mouse_joints(self)

-- <27> Show which backend-specific script is active.
label.set_text("/info#version_label", "Box2D V3 mouse joint")

-- <28> Acquire input focus so this script receives mouse/touch input in
-- on_input().
msg.post(".", "acquire_input_focus")
end

function update(self, dt)
if not self.active then
	return
end

update_auto_target(self, dt)
update_joints(self)
draw_connections(self)
end

function on_input(self, action_id, action)
if not self.active then
	return
end

-- <29> Mouse input commonly arrives with action_id == nil, while touch input
-- uses the "touch" binding. Both provide screen-space x/y coordinates here.
if (action_id == TOUCH or action_id == nil) and action.x and action.y then
	self.user_control = true
	set_target(self, vmath.vector3(action.x, action.y, 0))
end
end

function final(self)
if not self.active then
	return
end

-- <30> Destroy scripted joints explicitly when the script is finalized.
-- This keeps the example clean when the collection is unloaded or hot-reloaded.
b2d.joint.destroy(self.soft_joint)
b2d.joint.destroy(self.tight_joint)

msg.post(".", "release_input_focus")
end

--[[
1. `@render:` is Defold's render socket. The "draw_line" message draws a temporary helper line.
2. A mouse joint follows a world-space target point. It does not require the mouse itself to be a physics body.
3. The target marker is only visual. Moving it makes the invisible target position understandable.
4. `b2d.body.set_transform()` directly sets the Box2D body position and angle. Good for reset/setup, not for continuous gameplay movement.
5. Clearing velocity prevents the reset state from inheriting old momentum.
6. `b2d.body.set_awake()` forces the body to participate in simulation immediately.
7. `b2d.body.set_gravity_scale(body, 0)` disables gravity for this body only.
8. `b2d.body.set_fixed_rotation(body, true)` prevents the body from rotating, keeping the example readable.
9. `b2d.body.set_linear_damping()` makes velocity decay over time, reducing endless drift.
10. `b2d.get_body()` converts a Defold collision object component URL into a native Box2D body handle.
11. `b2d.joint.create_mouse()` creates a mouse joint between two bodies. The second body is the one visibly pulled toward the target.
12. `target` is the initial world-space point the mouse joint tries to follow.
13. `max_force` caps the force used by the joint. Too low = very stretchy; higher = stronger pull.
14. `hertz` is the V3 spring frequency. Lower values feel softer, higher values feel tighter.
15. `damping_ratio` controls oscillation. Lower values bounce more; higher values settle faster.
16. `collide_connected = false` prevents the two bodies connected by the joint from colliding.
17. The tight joint uses the same API but different parameters, demonstrating how tuning changes the feel.
18. Higher `max_force` allows stronger correction toward the target.
19. Higher `hertz` makes the constraint respond faster.
20. Higher `damping_ratio` removes more bounce.
21. Automatic target motion makes the example self-demonstrating.
22. `b2d.joint.set_mouse_target()` updates the world target of an existing mouse joint every frame.
23. Waking bodies avoids cases where sleeping physics bodies do not react immediately to the changed target.
24. `b2d.body.get_position()` reads the current simulated world position from Box2D.
25. The target cross is a visual helper, not part of the physics simulation.
26. `b2d.get_version().major` lets one shared collection choose the correct backend-specific script.
27. `label.set_text()` updates the on-screen backend label.
28. `acquire_input_focus` is required before this script receives `on_input()` callbacks.
29. Pointer input takes over from automatic motion and drives the mouse-joint target directly.
30. `b2d.joint.destroy()` removes joints created through the scripted joint API.
]]
```

### box2d_mouse_joint_v2.script

```lua
local TOUCH = hash("touch")

local START_TARGET = vmath.vector3(360, 420, 0)
local SOFT_START = vmath.vector3(270, 310, 0)
local TIGHT_START = vmath.vector3(450, 310, 0)

local SOFT_LINE_COLOR = vmath.vector4(1.0, 0.65, 0.22, 1.0)
local TIGHT_LINE_COLOR = vmath.vector4(0.35, 0.85, 1.0, 1.0)
local TARGET_LINE_COLOR = vmath.vector4(0.45, 1.0, 0.65, 1.0)

local function draw_line(from, to, color)
	-- <1> Draw a debug/helper line through the render socket.
	-- The line exists for one frame only, so it must be redrawn every update.
	msg.post("@render:", "draw_line", {
		start_point = from,
		end_point = to,
		color = color
	})
end

local function set_target(self, position)
	-- <2> Store the current mouse-joint target as a world-space point.
	-- The mouse/touch pointer is not a Box2D body. It is only a target position
	-- that the mouse joint tries to pull the dynamic body toward.
	self.target = vmath.vector3(position.x, position.y, 0)

	-- <3> Move the visible target marker so the user can see the point followed
	-- by both mouse joints.
	go.set_position(self.target, self.target_url)
end

local function reset_body(body, position)
	-- <4> Set the Box2D body transform directly.
	-- This is good for example setup/reset. Do not use this as normal per-frame
	-- movement, because it teleports the body and can produce non-physical motion.
	b2d.body.set_transform(body, position, 0)

	-- <5> Clear previous motion so the example starts from a deterministic state.
	b2d.body.set_linear_velocity(body, vmath.vector3())
	b2d.body.set_angular_velocity(body, 0)

	-- <6> Wake the body so it reacts immediately after reset.
	b2d.body.set_awake(body, true)
end

local function setup_body(body)
	-- <7> Disable gravity for this body.
	-- This keeps the example focused on the mouse-joint spring behaviour.
	b2d.body.set_gravity_scale(body, 0)

	-- <8> Prevent the body from rotating.
	-- Rotation would add noise to the visual explanation, while this example is
	-- about soft versus tight positional following.
	b2d.body.set_fixed_rotation(body, true)

	-- <9> Add linear damping.
	-- This reduces endless sliding and helps the body settle after movement.
	b2d.body.set_linear_damping(body, 1.5)
end

local function create_mouse_joints(self)
	-- <10> Get native Box2D body handles from Defold collision object components.
	-- `target` acts as the static/reference body for the mouse joints.
	local anchor_body = b2d.get_body(msg.url(nil, "target", "collisionobject"))
	self.soft_body = b2d.get_body(msg.url(nil, "soft_body", "collisionobject"))
	self.tight_body = b2d.get_body(msg.url(nil, "tight_body", "collisionobject"))

	setup_body(self.soft_body)
	setup_body(self.tight_body)

	reset_body(self.soft_body, SOFT_START)
	reset_body(self.tight_body, TIGHT_START)

	-- <11> Create a soft V2 mouse joint.
	-- In Box2D V2-style definitions, spring frequency is controlled by
	-- `frequency`, not `hertz`.
	self.soft_joint = b2d.joint.create_mouse(anchor_body, self.soft_body, {
		-- <12> Initial world target. This value is later updated every frame.
		target = self.target,

		-- <13> Maximum force the joint can apply.
		-- Lower max force allows more visible lag/stretch.
		max_force = 850,

		-- <14> V2 spring frequency.
		-- Lower frequency makes the body follow more softly and slowly.
		frequency = 1.5,

		-- <15> Damping ratio.
		-- Lower damping allows more bounce/overshoot.
		damping_ratio = 0.35,

		-- <16> The connected bodies should not collide with each other.
		collide_connected = false,
	})

	-- <17> Create a tighter V2 mouse joint.
	-- It follows the same target, but uses stronger/stiffer parameters.
	self.tight_joint = b2d.joint.create_mouse(anchor_body, self.tight_body, {
		target = self.target,

		-- <18> Higher max force means the body can be pulled more aggressively.
		max_force = 6500,

		-- <19> Higher frequency means a stiffer/faster spring response.
		frequency = 8.0,

		-- <20> Higher damping removes more oscillation.
		damping_ratio = 0.9,

		collide_connected = false,
	})
end

local function update_auto_target(self, dt)
	if self.user_control then
		return
	end

	-- <21> Animate the target automatically before user interaction.
	-- This makes the example demonstrate itself on the examples website.
	self.time = self.time + dt

	set_target(self, vmath.vector3(
	360 + math.cos(self.time * 1.35) * 170,
	395 + math.sin(self.time * 1.10) * 95,
	0
))
end

local function update_joints(self)
-- <22> Update both mouse joints with the current world target.
-- The joints are created once, but their target can be changed every frame.
b2d.joint.set_mouse_target(self.soft_joint, self.target)
b2d.joint.set_mouse_target(self.tight_joint, self.target)

-- <23> Keep the bodies awake while the target moves.
-- This avoids relying on b2d.joint.wake_bodies(), which may not exist in
-- the active V2 runtime.
b2d.body.set_awake(self.soft_body, true)
b2d.body.set_awake(self.tight_body, true)
end

local function draw_connections(self)
-- <24> Read the current simulated positions from Box2D.
-- These positions are the result of the physics step, not manually animated
-- sprite positions.
local soft_position = b2d.body.get_position(self.soft_body)
local tight_position = b2d.body.get_position(self.tight_body)

-- <25> Draw spring-like helper lines from the target to each body.
-- The longer the line, the more that body is lagging/stretching.
draw_line(self.target, soft_position, SOFT_LINE_COLOR)
draw_line(self.target, tight_position, TIGHT_LINE_COLOR)

-- <26> Draw a small cross at the target point.
draw_line(self.target + vmath.vector3(-18, 0, 0), self.target + vmath.vector3(18, 0, 0), TARGET_LINE_COLOR)
draw_line(self.target + vmath.vector3(0, -18, 0), self.target + vmath.vector3(0, 18, 0), TARGET_LINE_COLOR)
end

function init(self)
-- <27> Run this script only when the active Box2D backend is V2.
-- The same collection may contain both V2 and V3 scripts, but only the
-- matching one should initialize.
self.active = b2d.get_version().major == 2

if not self.active then
	return
end

self.target_url = msg.url(nil, "target", nil)
self.time = 0
self.user_control = false

set_target(self, START_TARGET)
create_mouse_joints(self)

-- <28> Show which backend-specific script is active.
label.set_text("/info#version_label", "Box2D V2 mouse joint")

-- <29> Required before this script receives on_input() callbacks.
msg.post(".", "acquire_input_focus")
end

function update(self, dt)
if not self.active then
	return
end

update_auto_target(self, dt)
update_joints(self)
draw_connections(self)
end

function on_input(self, action_id, action)
if not self.active then
	return
end

-- <30> Mouse input usually comes with action_id == nil, while touch input
-- uses the configured "touch" binding. Both provide x/y screen coordinates.
if (action_id == TOUCH or action_id == nil) and action.x and action.y then
	self.user_control = true
	set_target(self, vmath.vector3(action.x, action.y, 0))
end
end

function final(self)
if not self.active then
	return
end

-- <31> Destroy scripted joints explicitly when the script is finalized.
b2d.joint.destroy(self.soft_joint)
b2d.joint.destroy(self.tight_joint)

msg.post(".", "release_input_focus")
end

--[[
1. `@render:` is Defold's render socket. The "draw_line" message draws a temporary helper line.
2. A mouse joint follows a world-space target point. The pointer itself is not a physics body.
3. The target marker is only visual. It helps show what the bodies are trying to follow.
4. `b2d.body.set_transform()` directly changes the body's world transform. Good for setup/reset, not continuous movement.
5. Clearing linear and angular velocity removes previous momentum.
6. `b2d.body.set_awake()` wakes the body so it reacts immediately in the simulation.
7. `b2d.body.set_gravity_scale(body, 0)` disables gravity for this body only.
8. `b2d.body.set_fixed_rotation(body, true)` prevents rotation and keeps the visual demonstration clean.
9. `b2d.body.set_linear_damping()` damps velocity over time and reduces endless drift.
10. `b2d.get_body()` converts a Defold collision object URL into a Box2D body handle used by the b2d API.
11. `b2d.joint.create_mouse()` creates a mouse joint between two bodies. The second body is the one visibly pulled toward the target.
12. `target` is the initial world-space target point.
13. `max_force` caps how strongly the joint can pull. Lower values create more visible stretch.
14. `frequency` is the V2 spring frequency. Lower values feel softer; higher values feel tighter.
15. `damping_ratio` controls bounce and overshoot. Lower values oscillate more; higher values settle faster.
16. `collide_connected = false` prevents the connected bodies from colliding with each other.
17. The tight joint uses the same mouse-joint API but different parameters.
18. Higher `max_force` lets the joint correct the body's position more strongly.
19. Higher `frequency` makes the spring respond faster.
20. Higher `damping_ratio` removes more oscillation.
21. Automatic target motion keeps the example animated before the user interacts.
22. `b2d.joint.set_mouse_target()` updates the world target of an existing mouse joint.
23. Waking the bodies avoids sleeping-body cases where the target changes but the body does not visibly react immediately.
24. `b2d.body.get_position()` reads the current simulated world position of a body.
25. The helper lines visualize how far each body stretches away from the target.
26. The target cross is a visual helper, not part of the physics simulation.
27. `b2d.get_version().major` selects the backend-specific script.
28. `label.set_text()` updates the label. It uses message passing internally, so the URL must be correct.
29. `acquire_input_focus` is needed to receive `on_input()`.
30. Pointer input switches the example from automatic motion to direct user-controlled target movement.
31. `b2d.joint.destroy()` removes joints created through the scripted joint API.
]]
```
