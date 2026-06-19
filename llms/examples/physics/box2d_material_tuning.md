# Box2D Material Properties Tuning

Tune Box2D density, friction, and restitution from script using Box2D V2 legacy and Box2D V3.

[Project files](https://github.com/defold/examples/tree/master/physics/box2d_material_tuning)

This example compares three dynamic balls whose Box2D material properties are tuned from script. It works with both Box2D V2 legacy and Box2D V3 by attaching one script for each backend. Each script checks `b2d.get_version()` during `init()` and becomes a no-op when the other backend is active.

Click or tap the window to reset the balls and watch the comparison again.

## What You'll Learn

* How to get a Box2D body from a Defold collision object
* How to detect the active Box2D version with `b2d.get_version()`
* How to tune density, friction, and restitution through the V2 fixture API
* How to tune density, friction, and restitution through the V3 shape API
* How to switch the project between Box2D V2 and V3 with app manifests

## Setup

The collection contains three spawner game objects, one for each material: Ice, Rubber, and Gold. Each spawner has both backend scripts, a label, and a local factory component named `ball_factory`.

All three factories point at `/example/ball.go`, a shared prototype with one sprite and one dynamic circle collision object. The active script creates a ball at the spawner's position, tints the spawned sprite, applies the material settings, and gives it a starting velocity and spin from the spawner's script properties.

The material comparison comes from per-instance script property overrides:

`Ice`
: Low friction and low restitution, so the ball slides along the ramp.

`Rubber`
: Medium friction and high restitution, so the ball bounces more.

`Gold`
: High density, high friction, and low restitution, so the ball feels heavier and settles quickly.

The static scene is built from white walls, and three colored ramps.

The `game.project` of this example is configured to build with `/box2d_v3.appmanifest` by default. To test V2 locally after downloading the example, change `Native Extensions -> App Manifest` in `game.project` to `/box2d_v2.appmanifest`.

## How It Works

Both scripts read `b2d.get_version()` once. `box2d_material_tuning_v2.script` only continues when the major version is 2, while `box2d_material_tuning_v3.script` only continues when the major version is 3.

`go.property()` exposes the material settings on each script instance. The Ice, Rubber, and Gold spawners use the same scripts, but each spawner overrides density, friction, restitution, velocity, spin, tint, and material name in the collection.

`b2d.get_body()` returns the Box2D body owned by the spawned ball's collision object. The active script then updates the ball with the backend-specific material API.

There is a significant difference between Box2D V2 legacy and Box2D V3.

In Box2D V2 legacy, collision geometry and material properties are attached to a body through fixtures. The V2 script reads the first fixture with `b2d.body.get_fixtures()` and uses `b2d.fixture.set_density()`, `b2d.fixture.set_friction()`, and `b2d.fixture.set_restitution()` to tune the ball. When setting density, the script asks Box2D to update the body mass from the new value.

In Box2D V3, the script uses the shape API instead of the V2 fixture API. It reads the first shape with `b2d.body.get_shapes()` and uses `b2d.shape.set_density()`, `b2d.shape.set_friction()`, and `b2d.shape.set_restitution()`. After changing density, it calls `b2d.body.reset_mass_data()` so the body mass reflects the new density immediately.

After applying the values, each script reads them back and shows them on the label attached to the same spawner. Clicking or tapping makes each active spawner delete its current ball, spawn a fresh one from its own factory, and reapply its material settings for the current backend.

## Scripts

### box2d_material_tuning_v3.script

```lua
go.property("material", hash("Material")) -- <1>
go.property("density", 1.0)
go.property("friction", 0.2)
go.property("restitution", 0.2)
go.property("velocity", vmath.vector3())
go.property("spin", 0.0)
go.property("tint", vmath.vector4(1, 1, 1, 1))

local MATERIAL_NAMES = {
	[hash("Ice")] = "Ice",
	[hash("Rubber")] = "Rubber",
	[hash("Gold")] = "Gold",
}

local function label_text(self, density, friction, restitution)
	local name = MATERIAL_NAMES[self.material] or "Material"
	return string.format("%s V3\nDensity: %.1f\nFriction: %.2f\nRestit.: %.2f", name, density, friction, restitution)
end

local function configure_material(self)
	local body = b2d.get_body(msg.url(nil, self.ball_id, "collisionobject")) -- <2>
	local shape = b2d.body.get_shapes(body)[1] -- <3>
	b2d.shape.set_density(body, shape.index, self.density) -- <4>
	b2d.body.reset_mass_data(body) -- <5>
	b2d.shape.set_friction(body, shape.index, self.friction) -- <6>
	b2d.shape.set_restitution(body, shape.index, self.restitution) -- <7>

	local density = b2d.shape.get_density(body, shape.index) -- <8>
	local friction = b2d.shape.get_friction(body, shape.index) -- <9>
	local restitution = b2d.shape.get_restitution(body, shape.index) -- <10>
	label.set_text("#label", label_text(self, density, friction, restitution)) -- <11>

	return body
end

local function delete_ball(self)
	if self.ball_id then -- <12>
		go.delete(self.ball_id)
		self.ball_id = nil
	end
end

local function respawn_ball(self)
	delete_ball(self) -- <13>

	self.ball_id = factory.create("#ball_factory", go.get_position()) -- <14>
	go.set(msg.url(nil, self.ball_id, "sprite"), "tint", self.tint) -- <15>

	local body = configure_material(self)
	if b2d.body.set_active then -- <16>
		b2d.body.set_active(body, true) -- <17>
	end
	b2d.body.set_linear_velocity(body, self.velocity) -- <18>
	b2d.body.set_angular_velocity(body, self.spin) -- <19>
end

function init(self)
	local b2d_version = b2d.get_version() -- <20>
	self.active = b2d_version.major == 3 -- <21>

	if not self.active then -- <22>
		return
	end

	msg.post(".", "acquire_input_focus") -- <23>
	respawn_ball(self)
end

-------------------
-- Input handling:

local TOUCH = hash("touch")

function on_input(self, action_id, action)
	if not self.active then -- <24>
		return
	end

	if action_id == TOUCH and action.pressed then -- <25>
		respawn_ball(self) -- <26>
	end
end

--[[
1. Exposes the material settings as script properties. Each spawner overrides these values in the collection.
2. Gets the Box2D body from this spawner's current factory-created ball.
3. Gets the first shape from the ball body. Box2D V3 uses shapes instead of the V2 fixture API.
4. Sets the shape density through the Box2D V3 shape API.
5. Recalculates the body mass so the new density affects the ball immediately.
6. Sets the shape friction. Low values slide more; high values grip more.
7. Sets the shape restitution. Low values absorb impact; high values bounce more.
8. Reads the applied density back from the V3 shape.
9. Reads the applied friction back from the V3 shape.
10. Reads the applied restitution back from the V3 shape.
11. Updates the label with the values currently applied to this ball.
12. Checks whether a previously spawned ball exists before deleting it.
13. Removes the previous ball before spawning a new one, so each spawner controls one active ball.
14. Spawns a new ball from the local factory at the spawner's position.
15. Applies this spawner's tint to the spawned ball sprite.
16. Checks whether this Box2D build exposes explicit body activation.
17. Activates the spawned body through the Box2D body API when `set_active()` is available.
18. Sets the ball's linear velocity through the Box2D body API.
19. Sets the ball's angular velocity through the Box2D body API.
20. Reads the active Box2D backend version.
21. Enables this script only when the project is running the Box2D V3 backend.
22. Stops the script early when Box2D V3 is not active, because the example uses V3 shape API calls.
23. Acquires input focus so this script can receive click or touch input.
24. Skips input handling if this script is inactive.
25. Handles a click or touch press and uses it as a manual reset for the ball.
26. Respawns the ball and reapplies the V3 material settings.
]]
```

### box2d_material_tuning_v2.script

```lua
go.property("material", hash("Material")) -- <1>
go.property("density", 1.0)
go.property("friction", 0.2)
go.property("restitution", 0.2)
go.property("velocity", vmath.vector3())
go.property("spin", 0.0)
go.property("tint", vmath.vector4(1, 1, 1, 1))

local MATERIAL_NAMES = {
	[hash("Ice")] = "Ice",
	[hash("Rubber")] = "Rubber",
	[hash("Gold")] = "Gold",
}

local function label_text(self, density, friction, restitution)
	local name = MATERIAL_NAMES[self.material] or "Material"
	return string.format("%s V2\nDensity: %.1f\nFriction: %.2f\nRestit.: %.2f", name, density, friction, restitution)
end

local function configure_material(self)
	local body = b2d.get_body(msg.url(nil, self.ball_id, "collisionobject")) -- <2>
	local fixture = b2d.body.get_fixtures(body)[1] -- <3>
	b2d.fixture.set_density(body, fixture.index, self.density, true) -- <4>
	b2d.fixture.set_friction(body, fixture.index, self.friction) -- <5>
	b2d.fixture.set_restitution(body, fixture.index, self.restitution) -- <6>

	local density = b2d.fixture.get_density(body, fixture.index) -- <7>
	local friction = b2d.fixture.get_friction(body, fixture.index) -- <8>
	local restitution = b2d.fixture.get_restitution(body, fixture.index) -- <9>
	label.set_text("#label", label_text(self, density, friction, restitution)) -- <10>

	return body
end

local function delete_ball(self)
	if self.ball_id then -- <11>
		go.delete(self.ball_id)
		self.ball_id = nil
	end
end

local function respawn_ball(self)
	delete_ball(self) -- <12>

	self.ball_id = factory.create("#ball_factory", go.get_position()) -- <13>
	go.set(msg.url(nil, self.ball_id, "sprite"), "tint", self.tint) -- <14>

	local body = configure_material(self)
	if b2d.body.set_active then -- <15>
		b2d.body.set_active(body, true) -- <16>
	end
	b2d.body.set_linear_velocity(body, self.velocity) -- <17>
	b2d.body.set_angular_velocity(body, self.spin) -- <18>
end

function init(self)
	local b2d_version = b2d.get_version() -- <19>
	self.active = b2d_version.major == 2 -- <20>

	if not self.active then -- <21>
		return
	end

	msg.post(".", "acquire_input_focus") -- <22>
	respawn_ball(self)
end

-------------------
-- Input handling:

local TOUCH = hash("touch")

function on_input(self, action_id, action)
	if not self.active then -- <23>
		return
	end

	if action_id == TOUCH and action.pressed then -- <24>
		respawn_ball(self) -- <25>
	end
end

--[[
1. Exposes the material settings as script properties. Each spawner overrides these values in the collection.
2. Gets the Box2D body from this spawner's current factory-created ball.
3. Gets the first fixture from the ball body. In Box2D V2, a fixture attaches the collision shape and material properties to a body.
4. Sets the fixture density and updates the body mass from the new density.
5. Sets the fixture friction. Low values slide more; high values grip more.
6. Sets the fixture restitution. Low values absorb impact; high values bounce more.
7. Reads the applied density back from the V2 fixture.
8. Reads the applied friction back from the V2 fixture.
9. Reads the applied restitution back from the V2 fixture.
10. Updates the label with the values currently applied to this ball.
11. Checks whether a previously spawned ball exists before deleting it.
12. Removes the previous ball before spawning a new one, so each spawner controls one active ball.
13. Spawns a new ball from the local factory at the spawner's position.
14. Applies this spawner's tint to the spawned ball sprite.
15. Checks whether this Box2D build exposes explicit body activation.
16. Activates the spawned body through the Box2D body API when `set_active()` is available.
17. Sets the ball's linear velocity through the Box2D body API.
18. Sets the ball's angular velocity through the Box2D body API.
19. Reads the active Box2D backend version.
20. Enables this script only when the project is running the Box2D V2 backend.
21. Stops the script early when Box2D V2 is not active, because the example uses V2 fixture API calls.
22. Acquires input focus so this script can receive click or touch input.
23. Skips input handling if this script is inactive.
24. Handles a click or touch press and uses it as a manual reset for the ball.
25. Respawns the ball and reapplies the V2 material settings.
]]
```
