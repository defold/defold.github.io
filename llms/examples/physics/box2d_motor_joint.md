# Box2D Motor Joint

Create and control a motorized Box2D joint from script using Box2D V2 and V3.

[Project files](https://github.com/defold/examples/tree/master/physics/box2d_motor_joint)

This example creates a motorized Box2D joint at runtime. It works with both Box2D V2 and V3 by attaching one script for each backend. Each script checks `b2d.get_version()` during `init()` and becomes a no-op when the other backend is active.

Click or tap the window to reverse the motor direction.

## What You'll Learn

- How to get Box2D body handles from Defold collision objects
- How to detect the active Box2D version with `b2d.get_version()`
- How to create a pivoted motor joint with `b2d.joint.create_revolute()`
- How to control joint motor speed with `b2d.joint.set_motor_speed()`
- How to tune the Box2D V3 joint solver with `b2d.world.set_joint_tuning()`

## Setup

The collection contains a static `pivot` game object, one dynamic `arm` game object with a particle effect, and a controller game object.

The `pivot` object marks the world point the arm should rotate around. The `arm` object is the dynamic body driven by the joint. The example uses a revolute joint with its motor enabled, because the revolute joint provides a stable hinge pivot while the motor drives the rotation.

The controller has both backend scripts attached. Each script checks `b2d.get_version()` and only runs when the selected app manifest matches its Box2D backend.

The `game.project` of this example is configured to build with `/box2D_V3.appmanifest` by default. To test V2 locally after downloading the example, change `Native Extensions -> App Manifest` in `game.project` to `/box2D_V2.appmanifest`.

## How It Works

Both scripts read `b2d.get_version()` once. `box2d_motor_joint_v2.script` only continues when the major version is 2, while `box2d_motor_joint_v3.script` only continues when the major version is 3.

`b2d.get_body()` returns the Box2D bodies owned by the `pivot` and `arm` collision objects. The active script then creates a revolute joint between those bodies with `b2d.joint.create_revolute()`.

The joint definition uses:

- `local_anchor_a` on the pivot body
- `local_anchor_b` on the arm body
- `enable_motor` to turn on the joint motor
- `max_motor_torque` to limit how strongly the motor can rotate the arm
- `motor_speed` to set the current motor direction and speed

The important part is the arm anchor. The pivot is placed in the collection as a visible reference point. The scripts convert that world position into the arm's local space, so the arm rotates around the same visible pivot instead of rotating around its center.

Click or tap to reverse the motor with `b2d.joint.set_motor_speed()`. The V3 script also calls `b2d.world.set_joint_tuning()` to adjust the joint solver used by the Box2D V3 backend.

## Scripts

### box2d_motor_joint_v3.script

```lua
local TOUCH = hash("touch")
local MOTOR_SPEED = 1.5
local MAX_MOTOR_TORQUE = 50000

local function update_label(self)
	local direction = self.direction > 0 and "counter-clockwise" or "clockwise"
	label.set_text("#label", string.format("Box2D V3 motor joint\nMotor: %s\nClick or touch to reverse", direction)) -- <1>
end

local function set_motor_speed(self)
	b2d.joint.set_motor_speed(self.joint, self.direction * MOTOR_SPEED) -- <2>
	update_label(self)
end

local function reverse_motor(self)
	self.direction = -self.direction -- <3>
	set_motor_speed(self)
end

function init(self)
	self.direction = -1

	local b2d_version = b2d.get_version() -- <4>
	self.active = b2d_version.major == 3 -- <5>

	if not self.active then -- <6>
		return
	end

	msg.post(".", "acquire_input_focus") -- <7>

	local world = b2d.get_world() -- <8>
	b2d.world.set_gravity(world, vmath.vector3()) -- <9>
	b2d.world.set_joint_tuning(world, 60, 1.0) -- <10>

	local pivot_position = go.get_position("pivot") -- <11>
	local pivot = b2d.get_body(msg.url(nil, "pivot", "collisionobject")) -- <12>
	local arm = b2d.get_body(msg.url(nil, "arm", "collisionobject")) -- <13>
	b2d.body.set_gravity_scale(arm, 0.0) -- <14>

	local arm_anchor = b2d.body.get_local_point(arm, pivot_position) -- <15>

	self.joint = b2d.joint.create_revolute(pivot, arm, { -- <16>
		local_anchor_a = vmath.vector3(),
		local_anchor_b = arm_anchor,
		enable_motor = true,
		max_motor_torque = MAX_MOTOR_TORQUE,
		motor_speed = self.direction * MOTOR_SPEED,
		collide_connected = false,
	})

	update_label(self)
end

-------------------
-- Input handling:

function on_input(self, action_id, action)
	if not self.active then -- <17>
		return
	end

	if action_id == TOUCH and action.pressed then -- <18>
		reverse_motor(self)
	end
end

function final(self)
	if not self.active then
		return
	end

	if self.joint then
		b2d.joint.destroy(self.joint) -- <19>
		self.joint = nil
	end

	msg.post(".", "release_input_focus") -- <20>
end

--[[
1. Updates the label with the active backend and the current motor direction.
2. Sets the motor speed on the revolute joint through the Box2D joint API.
3. Reverses the stored motor direction before applying the new speed.
4. Reads the active Box2D backend version.
5. Enables this script only when the project is running the Box2D V3 backend.
6. Stops the script early when Box2D V3 is not active.
7. Acquires input focus so this script can receive click or touch input.
8. Gets the current Box2D world handle.
9. Clears world gravity so the arm stays in the editor-placed setup.
10. Tunes the Box2D V3 joint solver used by the motorized joint.
11. Reads the editor-placed pivot position, which is the world point the arm should rotate around.
12. Gets the Box2D body from the static `pivot` collision object.
13. Gets the Box2D body from the dynamic `arm` collision object.
14. Disables gravity on the arm body so the example focuses on the joint motor.
15. Converts the pivot world position into the arm's local space using the V3 body helper. This keeps the arm rotating around the visible pivot.
16. Creates a revolute joint with its motor enabled. The revolute joint provides the pivot, while the motor drives the rotation.
17. Skips input handling if this script is inactive.
18. Handles a click or touch press and uses it to reverse the motor direction.
19. Destroys the runtime-created joint during cleanup.
20. Releases input focus when the script or collection is unloaded.
]]
```

### box2d_motor_joint_v2.script

```lua
local TOUCH = hash("touch")
local MOTOR_SPEED = 1.5
local MAX_MOTOR_TORQUE = 50000

local function update_label(self)
	local direction = self.direction > 0 and "counter-clockwise" or "clockwise"
	label.set_text("#label", string.format("Box2D V2 motor joint\nMotor: %s\nClick or touch to reverse", direction)) -- <1>
end

local function set_motor_speed(self)
	b2d.joint.set_motor_speed(self.joint, self.direction * MOTOR_SPEED) -- <2>
	update_label(self)
end

local function reverse_motor(self)
	self.direction = -self.direction -- <3>
	set_motor_speed(self)
end

function init(self)
	self.direction = -1

	local b2d_version = b2d.get_version() -- <4>
	self.active = b2d_version.major == 2 -- <5>

	if not self.active then -- <6>
		return
	end

	msg.post(".", "acquire_input_focus") -- <7>

	local pivot_position = go.get_position("pivot") -- <8>
	local arm_position = go.get_position("arm")
	local pivot = b2d.get_body(msg.url(nil, "pivot", "collisionobject")) -- <9>
	local arm = b2d.get_body(msg.url(nil, "arm", "collisionobject")) -- <10>
	b2d.body.set_gravity_scale(arm, 0.0) -- <11>

	local arm_anchor = vmath.vector3(
		pivot_position.x - arm_position.x,
		pivot_position.y - arm_position.y,
		pivot_position.z - arm_position.z
	) -- <12>

	self.joint = b2d.joint.create_revolute(pivot, arm, { -- <13>
		local_anchor_a = vmath.vector3(),
		local_anchor_b = arm_anchor,
		enable_motor = true,
		max_motor_torque = MAX_MOTOR_TORQUE,
		motor_speed = self.direction * MOTOR_SPEED,
		collide_connected = false,
	})

	update_label(self)
end

-------------------
-- Input handling:

function on_input(self, action_id, action)
	if not self.active then -- <14>
		return
	end

	if action_id == TOUCH and action.pressed then -- <15>
		reverse_motor(self)
	end
end

function final(self)
	if not self.active then
		return
	end

	if self.joint then
		b2d.joint.destroy(self.joint) -- <16>
		self.joint = nil
	end

	msg.post(".", "release_input_focus") -- <17>
end

--[[
1. Updates the label with the active backend and the current motor direction.
2. Sets the motor speed on the revolute joint through the Box2D joint API.
3. Reverses the stored motor direction before applying the new speed.
4. Reads the active Box2D backend version.
5. Enables this script only when the project is running the Box2D V2 backend.
6. Stops the script early when Box2D V2 is not active.
7. Acquires input focus so this script can receive click or touch input.
8. Reads the editor-placed pivot and arm positions used to calculate the local joint anchor.
9. Gets the Box2D body from the static `pivot` collision object.
10. Gets the Box2D body from the dynamic `arm` collision object.
11. Disables gravity on the arm body so the example focuses on the joint motor.
12. Converts the pivot world position into the arm's local space using the editor positions. This keeps the arm rotating around the visible pivot.
13. Creates a revolute joint with its motor enabled. The revolute joint provides the pivot, while the motor drives the rotation.
14. Skips input handling if this script is inactive.
15. Handles a click or touch press and uses it to reverse the motor direction.
16. Destroys the runtime-created joint during cleanup.
17. Releases input focus when the script or collection is unloaded.
]]
```
