# Box2D dynamic shape scale and mass

Resize dynamic Box2D collision shapes at runtime and recalculate body mass.

[Project files](https://github.com/defold/examples/tree/master/physics/box2d_dynamic_scale)

This example shows how to change bodies shapes and mass in runtime.

It includes 4 independent dynamic Box2D bodies.

Click or tap to give every square body a new random size,
update its collision shape, recalculate its mass, and apply a random  impulse.

## What You'll Learn

- How to get a Box2D body from a Defold collision object
- How to detect the active Box2D version with `b2d.get_version()`
- How to resize collision geometry through the V2 fixture API
- How to resize collision geometry through the V3 shape API
- How `update_mass = true` makes body mass follow the new collision size
- How to apply a dynamic impulse to the body

## Setup

The collection contains four instances of `block.go` game object.
The `block.go` prototype contains:

- `script_v3`, which runs only with the Box2D V3 backend
- `script_v2`, which runs only with the Box2D V2 backend
- a square sprite
- a dynamic box collision object with base half-extents of `40.0`

The collection also contains `walls` game object with:

- one static collision object with four box shapes around the play area
- a label that explains the click or tap interaction.

The `game.project` of this example is configured to build with `/box2d_v3.appmanifest` by default.
To test V2 locally after downloading the example, change `Native Extensions -> App Manifest` in `game.project` to `/box2d_v2.appmanifest`.

## How It Works

Both scripts read `b2d.get_version()` in `init()` and are only active if a matching version is used -
`box2d_dynamic_scale_v2.script` only continues when the major version is 2,
while `box2d_dynamic_scale_v3.script` only continues when the major version is 3.

The active script acquires input focus and initialized a random number generator.

When the built-in `touch` action is pressed, each block picks a random uniform scale from `0.5` to `1.5`.
The script multiplies the base sprite size and base collision half-extent by that scale,
so the visible square and physics box stay aligned.

The mass changes because `update_mass = true` makes Box2D recalculate the body mass from the resized shape.

In Box2D V2, collision geometry is attached to a body through fixtures.
The V2 script reads the first fixture with `b2d.body.get_fixtures()`
and resizes it with `b2d.fixture.set_shape(body, fixture.index, shape, true)`.

In Box2D V3, collision geometry is attached through shapes.
The V3 script reads the first shape with `b2d.body.get_shapes()`
and resizes it with `b2d.shape.set_shape(shape.shape_id, shape, true)`.

After resizing, the active script applies a random linear impulse at the body's world center.
Since each body has just recalculated its mass from its new collision size,
the resulting movement makes the size and mass changes visible.

## Scripts

### box2d_dynamic_scale_v3.script

```lua
function init(self)
	-- This script uses the Box2D V3 fixture API.
	self.active = b2d.get_version().major == 3

	-- If Box2D V3 is not used, skip further processing
	if not self.active then
		return
	end

	-- `b2d.get_body()` returns the native Box2D body created by the given collision object.
	self.body = b2d.get_body("#collisionobject")

	-- In Box2D V3, collision geometry and material data live in shapes.
	self.shape_id = b2d.body.get_shapes(self.body)[1].shape_id

	-- Acquire input focus to handle inputs
	msg.post(".", "acquire_input_focus")

	-- Initialize random number generator
	math.randomseed(os.time())
end

-- The built-in touch action also covers mouse clicks in the built-in all.input_binding.
local TOUCH = hash("touch")

-- Base size will be used to change the scale around the initial size
local BASE_SIZE = 80.0
local BASE_HALF_EXTENT = 40.0

-- Helper function to get a random scale with values in range 0.5-1.5
local function get_random_scale()
	local random_number = math.random(5,15)/10
	return vmath.vector3(random_number, random_number, 0)
end

local function resize_body(self, scale_vector)
	local half_extent = BASE_HALF_EXTENT * scale_vector.x

	-- The last parameter update_mass set to true will cause the mass to be updated.
	local update_mass = true

	-- Update a box shape using the polygon box convenience format.
	-- V3 collision geometry is addressed through shapes.
	-- The shape type must match the current fixture shape type.
	b2d.shape.set_shape(self.shape_id, {
		type = b2d.shape.SHAPE_TYPE_BOX,
		hx = half_extent,
		hy = half_extent,
	}, update_mass)

	-- Also change the vector size to match the new shape
	local size_vector = BASE_SIZE * scale_vector
	go.set("#sprite", "size", size_vector)
end

function on_input(self, action_id, action)
	-- If Box2D V3 is not used, skip further processing
	if not self.active then
		return
	end

	if action_id == TOUCH and action.pressed then
		-- When click or touch is pressed - change the scale randomly
		resize_body(self, get_random_scale())

		-- And apply a random impulse to the center of the body
		-- to notice mass differences applied
		local random_impulse_x = math.random(-400,400)
		local random_impulse_y = math.random(-400,400)
		local impulse = vmath.vector3(random_impulse_x, random_impulse_y, 0)
		b2d.body.apply_linear_impulse(self.body, impulse, b2d.body.get_world_center(self.body))
	end
end
```

### box2d_dynamic_scale_v2.script

```lua
function init(self)
	-- This script uses the Box2D V2 fixture API.
	self.active = b2d.get_version().major == 2

	-- If Box2D V2 is not used, skip further processing
	if not self.active then
		return
	end

	-- `b2d.get_body()` returns the native Box2D body created by the given collision object.
	self.body = b2d.get_body("#collisionobject")

	-- In Box2D V2, collision geometry and material data live in fixtures.
	self.fixture_index = b2d.body.get_fixtures(self.body)[1].index
	-- v3: 
	self.shape_id = b2d.body.get_shapes(self.body)[1].shape_id

	-- Acquire input focus to handle inputs
	msg.post(".", "acquire_input_focus")

	-- Initialize random number generator
	math.randomseed(os.time())
end

-- The built-in touch action also covers mouse clicks in the built-in all.input_binding.
local TOUCH = hash("touch")

-- Base size will be used to change the scale around the initial size
local BASE_SIZE = 80.0
local BASE_HALF_EXTENT = 40.0

-- Helper function to get a random scale with values in range 0.5-1.5
local function get_random_scale()
	local random_number = math.random(5,15)/10
	return vmath.vector3(random_number, random_number, 0)
end

local function resize_body(self, scale_vector)
	local half_extent = BASE_HALF_EXTENT * scale_vector.x

	-- The last parameter update_mass set to true will cause the mass to be updated.
	local update_mass = true

	-- Update a box shape using the polygon box convenience format.
	-- V2 collision geometry is addressed through fixtures attached to the body.
	-- The shape type must match the current fixture shape type.
	b2d.fixture.set_shape(self.body, self.fixture_index, {
		type = b2d.shape.SHAPE_TYPE_BOX,
		hx = half_extent,
		hy = half_extent,
	}, update_mass)

	-- Also change the vector size to match the new shape
	local size_vector = BASE_SIZE * scale_vector
	go.set("#sprite", "size", size_vector)
end

function on_input(self, action_id, action)
	-- If Box2D V2 is not used, skip further processing
	if not self.active then
		return
	end

	if action_id == TOUCH and action.pressed then
		-- When click or touch is pressed - change the scale randomly
		resize_body(self, get_random_scale())

		-- And apply a random impulse to the center of the body
		-- to notice mass differences applied
		local random_impulse_x = math.random(-400,400)
		local random_impulse_y = math.random(-400,400)
		local impulse = vmath.vector3(random_impulse_x, random_impulse_y, 0)
		b2d.body.apply_linear_impulse(self.body, impulse, b2d.body.get_world_center(self.body))
	end
end
```
