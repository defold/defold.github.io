# Box2D Sensors

Create Box2D sensors from static collision shapes.

[Project files](https://github.com/defold/examples/tree/master/physics/box2d_sensor_toggle)

This example shows how to utilize the Box2D scripting API to operate with sensors (triggers).
It spawns dynamic physics balls from slightly different random positions near the top of the scene,
and gravity pulls each ball down, and these pass through two collision objects.

## What You'll Learn

- How to get a Box2D body from a collision object with `b2d.get_body()`.
- How to turn a Box2D V2 fixture into a sensor with `b2d.fixture.set_sensor()`.
- How to recreate a Box2D V3 shape as a sensor with `b2d.body.create_shape()`.
- How to count V2 sensor overlaps from `trigger_response` enter/exit messages.
- How to poll V3 sensor overlaps with `b2d.shape.get_sensor_overlaps()`.

## Setup

The collection contains one `controller` game object with `spawn.script` and a `ball_factory`.
The factory creates `ball.go` - a small prototype with one sprite and one dynamic circle collision object.

The two sensor game objects both contain:

- `sensor_box2d_v3.script` - for Box2D V3 example handling
- `sensor_box2d_v2.script` - for Box2D V2 example handling
- A sprite, label, and static collision object with component id `collisionobject`.

The collision objects are of type `Static` in the editor.

All sensors use the `sensor` collision group and mask the `ball` group.
The spawned ball belongs to the `ball` collision group and masks the `sensor` group,
so the sensor overlaps only include spawned balls.

The `game.project` currently uses `/box2d_v3.appmanifest`.
To test V2 locally, change `Native Extensions -> App Manifest` to `/box2d_v2.appmanifest`.
Gravity set in `game.project` causes the falling motion.

## How It Works

The controller spawns a ball repeateadly with `factory.create()`.
Each ball is spawned at a random X position near the center, and is deleted after a short delay.
The spawned balls pass through the sensor's collision object shapes.

Each sensor has two backend scripts (V2 and V3), but only one runs processing depending on a choosen Box2D version.
Each script checks `b2d.get_version().major` in `init()` and returns immediately when the active backend does not match.

At startup, the active Box2D script changes the static collision geometry into a sensor (trigger) through the `b2d` API.
Box2D V2 and V3 expose this through different scripting APIs:

- V2 uses fixtures and Defold trigger messages.
- V3 uses shapes and can poll a sensor shape's current overlaps directly.

In Box2D V2, `sensor_box2d_v2.script` gets the body with `b2d.get_body("#collisionobject")`,
reads the first fixture with `b2d.body.get_fixtures()`, and calls `b2d.fixture.set_sensor()`,
so the fixture no longer blocks the balls. V2 fixture sensors do not expose a `get_sensor_overlaps()` polling API.
But Defold still sends `trigger_response` messages when another collision object enters or exits the sensor,
and the script maintains a Lua table of current overlapping ball ids.

In Box2D V3, `sensor_box2d_v3.script` uses the shape API.
It reads the first editor-authored shape with `b2d.body.get_shapes()` and `b2d.shape.get_shape()`,
destroys that solid shape, and creates a replacement with `b2d.body.create_shape()` using the same geometry and `sensor = true`.
The V3 script then calls `b2d.shape.enable_sensor_events()` for the new sensor shape.
In `update()`, it polls the current overlaps with `b2d.shape.get_sensor_overlaps()`.
This returns shape info tables for the shapes currently overlapping the sensor.

Both scripts gives us the same result: each sensor sprite scales up while at least one ball overlaps it,
and the label shows the current overlap count reported by the active backend path.

## Scripts

### sensor_box2d_v3.script

```lua
-- Helper function to create a sensor from the collision object for scripting
local function create_sensor_shape()
	-- `b2d.get_body()` returns the native Box2D body created by this collision object.
	local body = b2d.get_body("#collisionobject")

	-- In Box2D V3, collision geometry is attached to a body as shapes.
	-- Read the first editor-authored shape so the runtime sensor keeps the same size.
	local shape = b2d.body.get_shapes(body)[1]
	local shape_definition = b2d.shape.get_shape(body, shape.index)

	-- The editor-authored shape is solid, so it would block the falling ball.
	-- Remove it before creating the replacement sensor shape.
	b2d.body.destroy_shape(body, shape.index)

	-- A sensor shape reports overlaps without producing collision response.
	-- The ball can pass through it, but Box2D still tracks which shapes overlap it.
	local sensor = b2d.body.create_shape(body, {
		shape = shape_definition,
		friction = 0.0,
		restitution = 0.0,
		sensor = true,
	})

	-- V3 sensor overlap polling is opt-in. Without this call,
	-- `get_sensor_overlaps()` would not return the current overlap list.
	b2d.shape.enable_sensor_events(sensor.shape_id, true)
	return sensor.shape_id
end

function init(self)
	-- This script uses the Box2D V3 shape API.
	self.active = b2d.get_version().major == 3

	-- If Box2D V3 is not used, skip further processing
	if not self.active then
		return
	end

	self.sensor_shape = create_sensor_shape()
	self.overlaps = {}
end

local NORMAL_SCALE = vmath.vector3(1.0)
local LARGER_SCALE = vmath.vector3(1.1)

function update(self, dt)
	-- If Box2D V3 is not used, skip further processing
	if not self.active then
		return
	end

	-- V3 returns the shapes currently overlapping this sensor shape.
	self.overlaps = b2d.shape.get_sensor_overlaps(self.sensor_shape)

	-- Set the sprite scale to indicate the overlapping visually
	if #self.overlaps > 0 then
		go.set("#sprite", "scale", LARGER_SCALE)
	else
		go.set("#sprite", "scale", NORMAL_SCALE)
	end

	-- Update the label text to show the amount of overlaps
	label.set_text("#label", "Overlaps: " .. #self.overlaps)
end
```

### sensor_box2d_v2.script

```lua
-- Helper function to convert a collision object to a sensor (trigger) for scripting
local function enable_sensor_fixture()
	-- `b2d.get_body()` returns the native Box2D body created by this collision object.
	local body = b2d.get_body("#collisionobject")

	-- In Box2D V2, collision geometry and material data live in fixtures.
	-- The collection-authored fixture starts solid, so the ball would collide with it.
	local fixture = b2d.body.get_fixtures(body)[1]

	-- Turning the fixture into a sensor disables physical collision response.
	-- Box2D still reports trigger-style enter/exit interactions for overlaps.
	b2d.fixture.set_sensor(body, fixture.index, true)
end

function init(self)
	-- This script uses the Box2D V2 fixture API.
	self.active = b2d.get_version().major == 2

	-- If Box2D V2 is not used, skip further processing
	if not self.active then
		return
	end

	enable_sensor_fixture()
	self.overlaps = {}
end

local NORMAL_SCALE = vmath.vector3(1.0)
local LARGER_SCALE = vmath.vector3(1.1)

function on_message(self, message_id, message, sender)
	-- If Box2D V2 is not used, skip further processing
	if not self.active then
		return
	end

	-- Defold sends `trigger_response` when a sensor fixture starts or stops
	-- overlapping another collision object allowed by the collision mask.
	if message_id == hash("trigger_response") then

		-- Store overlaps in a table or clear those that exited the sensor
		if message.enter then
			self.overlaps[message.other_id] = true
		else
			self.overlaps[message.other_id] = nil
		end

		-- Count overlaps
		local count = 0
		for i,v in pairs(self.overlaps) do count = count + 1 end

		-- Set the sprite scale to indicate the overlapping visually
		if count > 0 then
			go.set("#sprite", "scale", LARGER_SCALE)
		else
			go.set("#sprite", "scale", NORMAL_SCALE)
		end

		-- Update the label text to show the amount of overlaps
		label.set_text("#label", "Overlaps: " .. count)
	end
end
```

### spawn.script

```lua
-- Helper function to spawn a ball at random position on top and remove it after a moment
local function spawn_ball()
	-- X position is random between 200-600
	local x = 400 + math.random(-200, 200)

	-- Spawn the ball from the ball_factory, assign the random position
	-- and store the created instance's id
	local id = factory.create("#ball_factory", vmath.vector3(x, 600, 0.0))

	-- After a moment remove the spawned ball
	timer.delay(1.2, false, function()
		go.delete(id)
	end)
end

function init(self)
	-- Initialize random number generator
	math.randomseed(os.time())

	-- Use the above helper function to spawn the ball every 0.5 second
	timer.delay(0.2, true, spawn_ball)
end
```
