# Box2D Revolute Bridge

Create a bridge from revolute joints between existing Defold collision objects.

[Project files](https://github.com/defold/examples/tree/master/physics/box2d_revolute_bridge)

This example builds a simple rope bridge from rectangular dynamic bodies connected with Box2D revolute joints.
A ball drops onto the bridge so the hinge chain bends under load.

Click or tap the window to reset the ball.

## What You'll Learn

- How to get Box2D bodies from Defold collision objects with `b2d.get_body()`
- How to connect two bodies with a `revolute` type joint
- How local joint anchors define hinge points on each connected body

## Setup

The collection contains these game objects:

`controller`
: Contains both backend scripts, `box2d_revolute_bridge_v2.script` and `box2d_revolute_bridge_v3.script`, plus the title and hint labels. Each script checks the active Box2D version and only one script runs.

`left_anchor` and `right_anchor`
: Static collision objects used as the fixed bridge supports.

`segment_01` to `segment_10`
: Dynamic rectangular collision objects. The active script creates revolute joints between neighboring segments.

`ball`
: A dynamic circle collision object that falls onto the bridge to show how the joints move.

`floor`, `left_wall`, and `right_wall`
: Static collision objects that keep the simulation in view after the ball falls through or off the bridge.

The project uses `box2d_v3.appmanifest` by default, so it runs with Box2D V3.
To use the older legacy V2 backend, switch the native extension app manifest in `game.project` to `/box2d_v2.appmanifest`.

## How It Works

Both scripts use the same collection-authored bodies. `b2d.get_body()` returns the Box2D body owned by each collision object, and `b2d.joint.create_revolute()` creates the hinge constraints at runtime.

Each bridge segment is 48 pixels wide. The script connects the right edge of one body to the left edge of the next body by using local anchors: `(24, 0, 0)` on the previous segment and `(-24, 0, 0)` on the current segment.
The first and last joints connect to static anchors at the bridge supports.

On reset, the script moves the ball up and drops it onto the bridge again. The joints are created once in `init()` and destroyed in `final()`.

## Scripts

### box2d_revolute_bridge_v3.script

```lua
local TOUCH = hash("touch")
local MOUSE_BUTTON_LEFT = hash("mouse_button_left")
local SEGMENT_HALF_WIDTH = 24
local START_BALL_POSITION = vmath.vector3(360, 610, 0)

local SEGMENTS = {
	"segment_01",
	"segment_02",
	"segment_03",
	"segment_04",
	"segment_05",
	"segment_06",
	"segment_07",
	"segment_08",
	"segment_09",
	"segment_10",
}

local function body(id)
	return b2d.get_body(msg.url(nil, id, "collisionobject")) -- <1>
end

local function create_joint(self, body_a, body_b, local_anchor_a, local_anchor_b)
	local joint = b2d.joint.create_revolute(body_a, body_b, { -- <2>
		local_anchor_a = local_anchor_a,
		local_anchor_b = local_anchor_b,
		collide_connected = false,
	})
	table.insert(self.joints, joint)
end

local function reset_body(body, position)
	b2d.body.set_transform(body, position, 0) -- <3>
	b2d.body.set_linear_velocity(body, vmath.vector3())
	b2d.body.set_angular_velocity(body, 0)
	b2d.body.set_awake(body, true)
end

local function reset_ball(self)
	go.set_position(START_BALL_POSITION, msg.url(nil, "ball", nil)) -- <4>
	reset_body(self.ball, START_BALL_POSITION) -- <5>
	b2d.body.set_linear_velocity(self.ball, vmath.vector3(0, -80, 0)) -- <6>
end

local function create_bridge(self)
	self.joints = {}

	local previous = body("left_anchor")
	for index, segment_id in ipairs(SEGMENTS) do
		local current = body(segment_id)

		local anchor_a = index == 1 and vmath.vector3() or vmath.vector3(SEGMENT_HALF_WIDTH, 0, 0)
		create_joint(self, previous, current, anchor_a, vmath.vector3(-SEGMENT_HALF_WIDTH, 0, 0)) -- <7>
		previous = current
	end

	create_joint(self, previous, body("right_anchor"), vmath.vector3(SEGMENT_HALF_WIDTH, 0, 0), vmath.vector3()) -- <8>
	self.ball = body("ball")
end

function init(self)
	self.active = b2d.get_version().major == 3 -- <9>
	if not self.active then
		return
	end

	label.set_text("#title", "Box2D V3 revolute bridge")
	create_bridge(self)
	reset_ball(self)
	msg.post(".", "acquire_input_focus") -- <10>
end

function on_input(self, action_id, action)
	if self.active and (action_id == TOUCH or action_id == MOUSE_BUTTON_LEFT) and action.pressed then -- <11>
		reset_ball(self)
	end
end

function final(self)
	if not self.active then
		return
	end

	for _, joint in ipairs(self.joints) do
		b2d.joint.destroy(joint) -- <12>
	end
	msg.post(".", "release_input_focus")
end

--[[
1. Get the native Box2D body owned by a Defold collision object in the collection.
2. Create one revolute joint. The local anchors define the hinge point on each connected body.
3. Reset a dynamic body to a known transform and clear its previous motion.
4. Move the visible ball game object back above the bridge so the reset is immediate.
5. Move the Box2D body to the same position and clear old motion.
6. Give the ball a small downward velocity so the reset immediately drops it onto the bridge.
7. Connect each segment to the previous body. The first segment connects to the left static anchor.
8. Connect the last segment to the right static anchor, completing the bridge.
9. Run this script only when the active Box2D backend is V3.
10. Acquire input so a click or touch can reset the ball.
11. Reset the ball when the user clicks or taps. The built-in input binding may send mouse clicks as `mouse_button_left` or `touch`.
12. Destroy the scripted joints when the collection is finalized.
]]
```

### box2d_revolute_bridge_v2.script

```lua
local TOUCH = hash("touch")
local MOUSE_BUTTON_LEFT = hash("mouse_button_left")
local SEGMENT_HALF_WIDTH = 24
local START_BALL_POSITION = vmath.vector3(360, 560, 0)

local SEGMENTS = {
	"segment_01",
	"segment_02",
	"segment_03",
	"segment_04",
	"segment_05",
	"segment_06",
	"segment_07",
	"segment_08",
	"segment_09",
	"segment_10",
}

local function body(id)
	return b2d.get_body(msg.url(nil, id, "collisionobject")) -- <1>
end

local function create_joint(self, body_a, body_b, local_anchor_a, local_anchor_b)
	local joint = b2d.joint.create_revolute(body_a, body_b, { -- <2>
		local_anchor_a = local_anchor_a,
		local_anchor_b = local_anchor_b,
		collide_connected = false,
	})
	table.insert(self.joints, joint)
end

local function reset_body(body, position)
	b2d.body.set_transform(body, position, 0) -- <3>
	b2d.body.set_linear_velocity(body, vmath.vector3())
	b2d.body.set_angular_velocity(body, 0)
	b2d.body.set_awake(body, true)
end

local function reset_ball(self)
	go.set_position(START_BALL_POSITION, msg.url(nil, "ball", nil)) -- <4>
	reset_body(self.ball, START_BALL_POSITION) -- <5>
	b2d.body.set_linear_velocity(self.ball, vmath.vector3(0, -80, 0)) -- <6>
end

local function create_bridge(self)
	self.joints = {}

	local previous = body("left_anchor")
	for index, segment_id in ipairs(SEGMENTS) do
		local current = body(segment_id)

		local anchor_a = index == 1 and vmath.vector3() or vmath.vector3(SEGMENT_HALF_WIDTH, 0, 0)
		create_joint(self, previous, current, anchor_a, vmath.vector3(-SEGMENT_HALF_WIDTH, 0, 0)) -- <7>
		previous = current
	end

	create_joint(self, previous, body("right_anchor"), vmath.vector3(SEGMENT_HALF_WIDTH, 0, 0), vmath.vector3()) -- <8>
	self.ball = body("ball")
end

function init(self)
	self.active = b2d.get_version().major == 2 -- <9>
	if not self.active then
		return
	end

	label.set_text("#title", "Box2D V2 revolute bridge")
	create_bridge(self)
	reset_ball(self)
	msg.post(".", "acquire_input_focus") -- <10>
end

function on_input(self, action_id, action)
	if self.active and (action_id == TOUCH or action_id == MOUSE_BUTTON_LEFT) and action.pressed then -- <11>
		reset_ball(self)
	end
end

function final(self)
	if not self.active then
		return
	end

	for _, joint in ipairs(self.joints) do
		b2d.joint.destroy(joint) -- <12>
	end
	msg.post(".", "release_input_focus")
end

--[[
1. Get the native Box2D body owned by a Defold collision object in the collection.
2. Create one revolute joint. The local anchors define the hinge point on each connected body.
3. Reset a dynamic body to a known transform and clear its previous motion.
4. Move the visible ball game object back above the bridge so the reset is immediate.
5. Move the Box2D body to the same position and clear old motion.
6. Give the ball a small downward velocity so the reset immediately drops it onto the bridge.
7. Connect each segment to the previous body. The first segment connects to the left static anchor.
8. Connect the last segment to the right static anchor, completing the bridge.
9. Run this script only when the active Box2D backend is V2.
10. Acquire input so a click or touch can reset the ball.
11. Reset the ball when the user clicks or taps. The built-in input binding may send mouse clicks as `mouse_button_left` or `touch`.
12. Destroy the scripted joints when the collection is finalized.
]]
```
