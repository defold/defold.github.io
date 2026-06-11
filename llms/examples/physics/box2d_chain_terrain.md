# Box2D Chain Terrain

Create Box2D chain terrain from script using scripting with Box2D V2 (legacy) and V3.

[Project files](https://github.com/defold/examples/tree/master/physics/box2d_chain_terrain)

This example creates connected Box2D chain terrain at runtime. It works with both Box2D V2 and V3 by attaching one script for each backend. Each script checks `b2d.get_version()` during `init()` and becomes a no-op when the other backend is active.

Click or tap the window to reset the ball and watch it roll over the same chain again.

## What You'll Learn

- How to get a Box2D body from a Defold collision object
- How to detect the active Box2D version with `b2d.get_version()`
- How to create chain terrain with `b2d.body.create_fixture()` in Box2D V2 Legacy Defold version.
- How to create chain terrain with `b2d.body.create_chain()` in Box2D V3.

## Setup

The collection contains a static `terrain` game object with one collision object. This is required because the runtime-created terrain is attached to an existing Box2D body. Defold creates that body from the collision object in the collection.

The small box shape on `terrain` sits below the view. It is only a placeholder that gives the script a static body to attach the runtime chain to; the visible terrain is the chain itself, drawn with `@render:draw_line`.

The `controller` game object has both backend scripts, a label, and a local factory component named `ball_factory`. The factory points at `/example/ball.go`, a shared prototype with one sprite and one dynamic circle collision object.

The `game.project` of this example is configured to build with `/box2D_V3.appmanifest` by default. To test V2 locally after downloading the example, change `Native Extensions -> App Manifest` in `game.project` to `/box2D_V2.appmanifest`.

## How It Works

Both scripts read `b2d.get_version()` once. `box2d_chain_terrain_v2.script` only continues when the major version is 2 (Defold legacy version), while `box2d_chain_terrain_v3.script` only continues when the major version is 3.

`b2d.get_body()` returns the Box2D body owned by the hidden `terrain` collision object. The active script then builds the chain with the backend-specific chain API.

In Box2D V2 Legacy Defold version., the script passes a chain shape definition to `b2d.body.create_fixture()`, which creates connected segments on the same static body.

In Box2D V3, the script uses `b2d.body.create_chain()`, which creates a true chain with segment adjacency and ghost vertices.

The shape definition includes `prev_vertex` and `next_vertex`. These are ghost vertices placed just outside the first and last terrain points. They do not add visible terrain segments; they tell Box2D how the open chain would continue past its endpoints so endpoint collision normals stay consistent.

The script redraws the chain vertices each frame with `@render:draw_line`, because the chain itself is a physics shape and has no sprite. The ball is created from the factory, given an initial velocity with `b2d.body.set_linear_velocity()`, and then reset on a timer or when the user clicks or taps.

## Scripts

### box2d_chain_terrain_v3.script

```lua
local BALL_START = vmath.vector3(650, 545, 0)
local BALL_VELOCITY = vmath.vector3(-140, 0, 0)
local CHAIN_COLOR = vmath.vector4(0.0, 0.9, 0.88, 1.0)
local PREV_GHOST_VERTEX = vmath.vector3(715, 505, 0)
local NEXT_GHOST_VERTEX = vmath.vector3(35, 235, 0)

local TERRAIN_VERTICES = {
	vmath.vector3(650, 480, 0),
	vmath.vector3(560, 455, 0),
	vmath.vector3(470, 395, 0),
	vmath.vector3(380, 380, 0),
	vmath.vector3(300, 315, 0),
	vmath.vector3(210, 275, 0),
	vmath.vector3(95, 265, 0),
}

local function draw_line(from, to, color)
	msg.post("@render:", "draw_line", { start_point = from, end_point = to, color = color }) -- <1>
end

local function get_major_version()
	local version = b2d.get_version()
	if type(version) == "table" then
		return version.major
	end
	return tonumber(string.match(version, "^(%d+)"))
end

local function clear_shapes(body)
	local shapes = b2d.body.get_shapes(body) -- <2>
	for i = #shapes, 1, -1 do
		b2d.body.destroy_shape(body, shapes[i].index) -- <3>
	end
end

local function create_chain(body)
	clear_shapes(body)

	return b2d.body.create_chain(body, {
		vertices = TERRAIN_VERTICES,
		prev_vertex = PREV_GHOST_VERTEX,
		next_vertex = NEXT_GHOST_VERTEX,
		friction = 0.65,
		restitution = 0.2,
	}) -- <4>
end

local function delete_ball(self)
	if self.ball_id then
		go.delete(self.ball_id)
	end
end

local function spawn_ball(self)
	delete_ball(self)
	self.ball_id = factory.create("#ball_factory", BALL_START) -- <5>

	local ball_body = b2d.get_body(msg.url(nil, self.ball_id, "collisionobject"))
	if b2d.body.set_active then
		b2d.body.set_active(ball_body, true) -- <6>
	end
	b2d.body.set_linear_velocity(ball_body, BALL_VELOCITY) -- <7>
	b2d.body.set_angular_velocity(ball_body, -4.0)
end

local function draw_chain()
	for i = 1, #TERRAIN_VERTICES - 1 do
		draw_line(TERRAIN_VERTICES[i], TERRAIN_VERTICES[i + 1], CHAIN_COLOR) -- <8>
	end
end

local function start_reset_timer(self)
	self.reset_timer = timer.delay(2.5, true, function() spawn_ball(self) end) -- <9>
end

local function cancel_reset_timer(self)
	if self.reset_timer then
		timer.cancel(self.reset_timer)
		self.reset_timer = nil
	end
end

function init(self)
	self.active = get_major_version() == 3 -- <10>

	if not self.active then -- <11>
		return
	end

	msg.post(".", "acquire_input_focus")
	local terrain_body = b2d.get_body(msg.url(nil, "terrain", "collisionobject")) -- <12>
	self.chain, self.chain_segments = create_chain(terrain_body) -- <13>
	label.set_text("#label", "Box2D V3 chain\nClick or touch to reset")
	spawn_ball(self)
	start_reset_timer(self)
end

function update(self, dt)
	if self.active then
		draw_chain()
	end
end

local TOUCH = hash("touch")

function on_input(self, action_id, action)
	if not self.active then
		return
	end

	if action_id == TOUCH and action.pressed then -- <14>
		spawn_ball(self)
		cancel_reset_timer(self) -- <15>
		start_reset_timer(self)
	end
end

function final(self)
	if not self.active then
		return
	end

	delete_ball(self)
	cancel_reset_timer(self)
	msg.post(".", "release_input_focus")
end

--[[
1. Draw each terrain segment through the render socket. The lines are transient, so the chain is redrawn every frame.
2. Read the existing Box2D V3 shapes from the placeholder body.
3. Remove the placeholder shape before creating the V3 chain.
4. Create V3 chain terrain with `b2d.body.create_chain()` so ghost vertices are preserved.
5. Spawn one dynamic ball from the local factory at the start of the chain.
6. Explicitly activate the spawned body on backends that expose body activation.
7. Give the ball an initial velocity so it rolls across the terrain immediately.
8. Draw the runtime terrain again each frame because the render line messages do not persist.
9. Replay the ball automatically so the example stays active without input.
10. Detect whether the running engine uses the Box2D V3 backend. The helper accepts both table and string version formats.
11. Leave this script as a no-op when the project uses another backend.
12. Get the Box2D body owned by the hidden `terrain` collision object in the collection.
13. Build the V3 chain terrain and keep both returned handles alive.
14. Clicks and taps reset the ball manually.
15. Reset the repeating timer after manual input so the next automatic reset waits for a full interval.
]]
```

### box2d_chain_terrain_v2.script

```lua
local BALL_START = vmath.vector3(650, 545, 0)
local BALL_VELOCITY = vmath.vector3(-140, 0, 0)
local CHAIN_COLOR = vmath.vector4(0.0, 0.9, 0.88, 1.0)
local PREV_GHOST_VERTEX = vmath.vector3(715, 505, 0)
local NEXT_GHOST_VERTEX = vmath.vector3(35, 235, 0)

local TERRAIN_VERTICES = {
	vmath.vector3(650, 480, 0),
	vmath.vector3(560, 455, 0),
	vmath.vector3(470, 395, 0),
	vmath.vector3(380, 380, 0),
	vmath.vector3(300, 315, 0),
	vmath.vector3(210, 275, 0),
	vmath.vector3(95, 265, 0),
}

local function draw_line(from, to, color)
	msg.post("@render:", "draw_line", { start_point = from, end_point = to, color = color }) -- <1>
end

local function get_major_version()
	local version = b2d.get_version()
	if type(version) == "table" then
		return version.major
	end
	return tonumber(string.match(version, "^(%d+)"))
end

local function clear_fixtures(body)
	local fixtures = b2d.body.get_fixtures(body) -- <2>
	for i = #fixtures, 1, -1 do
		b2d.body.destroy_fixture(body, fixtures[i].index) -- <3>
	end
end

local function create_chain(body)
	clear_fixtures(body)

	return b2d.body.create_fixture(body, {
		density = 0.0,
		friction = 0.65,
		restitution = 0.2,
		shape = {
			type = b2d.shape.SHAPE_TYPE_CHAIN,
			vertices = TERRAIN_VERTICES,
			prev_vertex = PREV_GHOST_VERTEX,
			next_vertex = NEXT_GHOST_VERTEX,
		},
	}) -- <4>
end

local function delete_ball(self)
	if self.ball_id then
		go.delete(self.ball_id)
	end
end

local function spawn_ball(self)
	delete_ball(self)
	self.ball_id = factory.create("#ball_factory", BALL_START) -- <5>

	local ball_body = b2d.get_body(msg.url(nil, self.ball_id, "collisionobject"))
	if b2d.body.set_active then
		b2d.body.set_active(ball_body, true) -- <6>
	end
	b2d.body.set_linear_velocity(ball_body, BALL_VELOCITY) -- <7>
	b2d.body.set_angular_velocity(ball_body, -4.0)
end

local function draw_chain()
	for i = 1, #TERRAIN_VERTICES - 1 do
		draw_line(TERRAIN_VERTICES[i], TERRAIN_VERTICES[i + 1], CHAIN_COLOR) -- <8>
	end
end

local function start_reset_timer(self)
	self.reset_timer = timer.delay(2.5, true, function() spawn_ball(self) end) -- <9>
end

local function cancel_reset_timer(self)
	if self.reset_timer then
		timer.cancel(self.reset_timer)
		self.reset_timer = nil
	end
end

function init(self)
	self.active = get_major_version() == 2 -- <10>

	if not self.active then -- <11>
		return
	end

	msg.post(".", "acquire_input_focus")
	local terrain_body = b2d.get_body(msg.url(nil, "terrain", "collisionobject")) -- <12>
	self.chain = create_chain(terrain_body) -- <13>
	label.set_text("#label", "Box2D V2 chain\nClick or touch to reset")
	spawn_ball(self)
	start_reset_timer(self)
end

function update(self, dt)
	if self.active then
		draw_chain()
	end
end

local TOUCH = hash("touch")

function on_input(self, action_id, action)
	if not self.active then
		return
	end

	if action_id == TOUCH and action.pressed then -- <14>
		spawn_ball(self)
		cancel_reset_timer(self) -- <15>
		start_reset_timer(self)
	end
end

function final(self)
	if not self.active then
		return
	end

	delete_ball(self)
	cancel_reset_timer(self)
	msg.post(".", "release_input_focus")
end

--[[
1. Draw each terrain segment through the render socket. The lines are transient, so the chain is redrawn every frame.
2. Read the existing Box2D V2 fixtures from the placeholder body.
3. Remove the placeholder fixture so only the runtime chain remains.
4. Attach a V2 chain fixture to the terrain body with `b2d.body.create_fixture()` and `b2d.shape.SHAPE_TYPE_CHAIN`.
5. Spawn one dynamic ball from the local factory at the start of the chain.
6. Explicitly activate the spawned body on backends that expose body activation.
7. Give the ball an initial velocity so it rolls across the terrain immediately.
8. Draw the runtime terrain again each frame because the render line messages do not persist.
9. Replay the ball automatically so the example stays active without input.
10. Detect whether the running engine uses the Box2D V2 backend. The helper accepts both table and string version formats.
11. Leave this script as a no-op when the project uses another backend.
12. Get the Box2D body owned by the hidden `terrain` collision object in the collection.
13. Build the V2 chain terrain.
14. Clicks and taps reset the ball manually.
15. Reset the repeating timer after manual input so the next automatic reset waits for a full interval.
]]
```
