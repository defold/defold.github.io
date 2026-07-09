# Box2D Prismatic Joint

Create a motorized Box2D prismatic joint with translation limits from script using Box2D.

[Project files](https://github.com/defold/examples/tree/master/physics/box2d_prismatic_joint)

This example creates a Box2D prismatic joint at runtime.
The blue dynamic body (slider) is constrained to a diagonal rail,
moves between two translation limits, and reverses its motor when it reaches either end.

Click or tap the window to reverse the motor manually.

There are no differences in scripting between Box2D V2 and V3 in this example.

## What You'll Learn

- How to get Box2D body handles from Defold collision objects
- How to create a prismatic joint with `b2d.joint.create_prismatic()`
- How `local_axis_a`, `lower_translation`, and `upper_translation` define the slide rail
- How to control a prismatic joint motor with `b2d.joint.set_motor_speed()`

## Setup

The collection contains:

- `controller` game object with the main script and labels with informations
- `rail` game object with static collision object for frame reference for the prismatic joint and a sprite rotated by 45 degrees around Z axis to indicate the "rail"
- `slider` game object with a dynamic collision object and a sprite to indicate where the slider is

The `rail` and `slider` bodies start at the same world position in the middle.

The `game.project` of this example is configured to build with `/box2d_v3.appmanifest` by default.
To test V2 locally after downloading the example, change `Native Extensions -> App Manifest` in `game.project` to `/box2d_v2.appmanifest`.

## How It Works

The script uses `b2d.get_body()` to fetch the Box2D bodies owned by the `rail` and `slider` collision objects.
Then calls `b2d.joint.create_prismatic()` which creates the prismatic joint between them,
with `local_axis_a` set to the same diagonal direction as the visible rail (rotated 45 degrees areound Z axis),
enables limits from `-110` to `110` project units, and a motor, sets a maximum motor force, and starts the slider moving along the rail.

The prismatic joint is a constraint solver - only defines *how* two bodies are allowed to move, not *why* they should move.
So normally, the slider would fall in the gravity direction, but would be moving constrained like a slider along a rail.
We enable the motor in the example to move in both direction along the rail.
Motor applied on a prismatic joint moves the object along the joint axis at the given linear speed.

During `update()`, the script reads `b2d.joint.get_joint_translation()`, which returns the position alongside the constraint,
and reverses the motor when the translation reaches either limit.

On input (touch or mouse click) the direction of the motor that applies force to the slider changes too.

## Scripts

### box2d_prismatic_joint.script

```lua
-- Unit vector for a 45 degree rail. This is the same direction as the rail sprite.
local AXIS = vmath.vector3(0.70710678, 0.70710678, 0)

-- Prismatic translation is measured along `local_axis_a`, in project units.
-- Define farthest limits on both ends:
local LOWER_TRANSLATION = -110
local UPPER_TRANSLATION = 110

-- Define motor speed that will be used to move the slider
local MOTOR_SPEED = 50

-- Some maximum motor force allows to apply a force on the slider to push it
local MAX_MOTOR_FORCE = 1200

function init(self)
	-- This will be storing a current direction of the slider
	self.direction = 1

	-- Acquire input focus to handle inputs
	msg.post(".", "acquire_input_focus")

	-- `b2d.get_body()` returns the native Box2D body created by the given collision object.
	local slider = b2d.get_body("/slider#collisionobject")
	local anchor = b2d.get_body("/rail#collisionobject")

	-- This creates a prismatic joint in runtime between the 2 bodies - an anchor and a slider.
	-- The joint axis matches the visible diagonal rail in the collection.
	self.joint = b2d.joint.create_prismatic(anchor, slider, {
		-- Both bodies start at the same position, so zero local anchors share the same joint origin.
		local_anchor_a = vmath.vector3(),
		local_anchor_b = vmath.vector3(),

		-- The axis is local to body A, the static anchor.
		local_axis_a = AXIS,

		-- Limits keep the dynamic body between the two ends of the rail.
		enable_limit = true,
		lower_translation = LOWER_TRANSLATION,
		upper_translation = UPPER_TRANSLATION,

		-- The motor pushes the slider along the axis without extra forces in update().
		enable_motor = true,
		max_motor_force = MAX_MOTOR_FORCE,
		motor_speed = self.direction * MOTOR_SPEED,

		-- The connected bodies do not need to collide with each other in this example.
		collide_connected = false,
	})
end

-- Helper function to reverse the motor direction
local function reverse_motor(self)
	-- Assign a negative direction to the current direction variable
	self.direction = -self.direction

	-- Positive and negative speed move the slider in opposite directions along the axis.
	b2d.joint.set_motor_speed(self.joint, self.direction * MOTOR_SPEED)
end

function update(self, dt)
	-- The function returns a translation on the defined joint in project units
	local translation = b2d.joint.get_joint_translation(self.joint)

	-- Reverse automatically when the slider reaches either translation limit.
	if self.direction > 0 and translation > UPPER_TRANSLATION then
		reverse_motor(self)
	elseif self.direction < 0 and translation < LOWER_TRANSLATION then
		reverse_motor(self)
	end

	-- Create a string describing the current direction
	local direction_string = self.direction > 0 and "up-right" or "down-left"

	-- Update the information on the label
	label.set_text("#label", string.format("Motor: %s\nTranslation: %.0f", direction_string, translation))
end

function on_input(self, action_id, action)
	-- The built-in touch action also covers mouse clicks in the built-in all.input_binding.
	if action_id == hash("touch") and action.pressed then
		-- When click or touch is pressed we reverse the motor direction
		reverse_motor(self)
	end
end

function final(self)
	-- Joints created through b2d.joint should be explicitly destroyed.
	if self.joint then
		b2d.joint.destroy(self.joint)
		self.joint = nil
	end

	-- Release input focus
	msg.post(".", "release_input_focus")
end
```
