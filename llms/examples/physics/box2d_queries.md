# Box2D Queries

This example shows how to use Box2D world overlap and raycast queries.

[Project files](https://github.com/defold/examples/tree/master/physics/box2d_queries)

This example places four static targets with box, circle, triangle, and diamond collision shapes, and user controllable AABB, circle, and raycast queries.
Move the mouse or drag to move the query areas and aim the ray, watch the hit counts, and see the query overlays, ray, target shapes, and AABB (Axis Aligned Bounding Box) outlines change color.

It ships with app manifests for Box2D V3 and Box2D V2 (legacy Defold version).
The project is configured to build with the V3 app manifest by default, and the same script works with both Box2D backends.

## What You'll Learn

- How to get the active Box2D world with `b2d.get_world()`.
- How to build AABB, circle, and raycast queries.
- How to use `b2d.world.overlap_aabb()`, `b2d.world.overlap_shape()`, and `b2d.world.cast_ray()`.
- How to read query result tables and use them.
- How to handle the Box2D V2 and V3 query result table differences.
- How to draw temporary AABB and ray helper lines through the render socket.

## Setup

The collection contains one `controller` game object with the query script, and two visual query overlays: one AABB box and one circle shape sprite.
The overlay objects only show where the scripted queries are being run - they do not have collision objects.
The raycast is drawn as a temporary helper line from the center of the scene to the pointer.

Additionally, there are four static target objects with collision objects with shapes: one box, one circle, and two convex hull collision shapes - a triangle and a diamond (rotated square),
and sprites for visual representation of the shape. The target sprites highlight exact shape and raycast hits, while the line rectangles highlight the target broad-phase AABBs hit by the AABB query.

The `game.project` of this example is configured to build with `/box2d_v3.appmanifest` by default. To test V2 locally after downloading the example, change `Native Extensions -> App Manifest` in `game.project` to `/box2d_v2.appmanifest`.

## How It Works

The controller stores the mouse or touch position and uses `update()` to drive the queries each frame.
An AABB and a circle are tested directly against the Box2D world at the pointer position, and a ray is cast from the scene center to the pointer.

Each query uses the Box2D scripting API directly.

Unlike sensors or triggers, the query calls do not create persistent detector objects or send physics messages.
They immediately return the fixtures or shapes hit by the query for the current frame.

The AABB query builds a table with `lower` and `upper` vector fields, then passes it to `b2d.world.overlap_aabb()`.
The circle query builds a shape table with `type`, `center`, and `radius`, then passes it to `b2d.world.overlap_shape()`.
The raycast passes an origin position and a translation vector to `b2d.world.cast_ray()`.
The translation is the direction and length of the segment, not the end position.

The collection has one query controller script.
The script reads bodies directly from fixture hits in V2, while in V3 it reads bodies from shape hits with `b2d.shape.get_body()`.
The hit body's position is then matched against the cached target positions so the controller can update the correct target game object.
The script caches the four static target positions and their defined AABBs at startup.

The important backend difference is the query result format:
Box2D V2 overlap results expose the body directly as `hit.body`, while V2 raycast results expose it through `hit.fixture.body`.
Box2D V3 overlap results expose `hit.shape_id`, while V3 raycast results expose `hit.shape.shape_id`; both are passed to `b2d.shape.get_body()` to get the owning body.
After that, the rest of the example uses the body in the same way for both backends.

In `update()`, the query controller directly moves the query overlay sprites, changes target sprite colors, and draws the helper outlines and ray.
The controller updates the count label to display how many fixtures or shapes each query detects.
The target sprites are highlighted by the exact circle shape query and raycast results.
The target AABB helper outlines are highlighted separately by the AABB query results.
The helper visual outlines and ray are created using `draw_line` messages sent to `@render:` every frame, which then draws the debug lines on top.

## Scripts

### box2d_queries.script

```lua
-- Input action from the default input bindings for mouse or touch.
local TOUCH = hash("touch")

-- Static targets used by the example. Each entry stores the game object id,
-- its normal sprite color, and the AABB half-size used for the helper outline.
local TARGETS = {
	{ id = "box_target", color = vmath.vector4(0.4, 0.7, 1.0, 1.0), aabb_half_size = vmath.vector3(68.0, 68.0, 0.0) },
	{ id = "circle_target", color = vmath.vector4(0.9, 0.5, 0.2, 1.0), aabb_half_size = vmath.vector3(68.0, 68.0, 0.0) },
	{ id = "triangle_target", color = vmath.vector4(0.2, 0.5, 0.9, 1.0), aabb_half_size = vmath.vector3(32.0, 32.0, 0.0) },
	{ id = "diamond_target", color = vmath.vector4(0.9, 0.9, 0.4, 1.0), aabb_half_size = vmath.vector3(32.0, 32.0, 0.0) },
}

-- Query sizes used by the pointer-controlled AABB and circle queries.
local AABB_HALF_SIZE = vmath.vector3(66.0, 66.0, 0.0)
local CIRCLE_RADIUS = 64.0
local RAY_ORIGIN = vmath.vector3(360.0, 360.0, 0.0)

-- Colors used for helper lines, query overlays, and hit feedback.
local LINE_COLOR = vmath.vector4(1.0, 1.0, 1.0, 0.75)
local AABB_COLOR = vmath.vector4(1.0, 1.0, 1.0, 0.35)
local CIRCLE_COLOR = vmath.vector4(0.4, 0.9, 1.0, 0.35)
local HIT_COLOR = vmath.vector4(0.3, 1.0, 0.4, 1.0)

function init(self)
	-- Listen for mouse and touch input
	msg.post(".", "acquire_input_focus")

	-- Get the active Box2D world.
	self.world = b2d.get_world()

	-- Initialize the pointer position and targets
	self.pointer = vmath.vector3(360.0, 360.0, 0.0)
	self.targets = {}

	-- Fill in the targets data
	for index, target in ipairs(TARGETS) do
		local position = go.get_position(target.id)
		local aabb = { lower = position - target.aabb_half_size, upper = position + target.aabb_half_size }

		-- Cache target positions and defined AABBs at startup because the targets are static.
		self.targets[index] = {
			id = target.id,
			color = target.color,
			position = position,
			aabb = aabb,
		}
	end
end

function on_input(self, action_id, action)
	-- Handle touch/mouse input
	if action_id == TOUCH or action_id == nil then
		-- Store the pointer in world coordinates
		self.pointer = vmath.vector3(action.x, action.y, 0.0)
	end
end

-- Draw one temporary helper line through the render socket. They are sent every frame.
local function draw_line(from, to, color)
	msg.post("@render:", "draw_line", {
		start_point = from,
		end_point = to,
		color = color,
	})
end

-- Draw a rectangle outline from a Box2D AABB table with lower and upper fields.
local function draw_aabb(aabb, color)
	local lower = aabb.lower
	local upper = aabb.upper

	-- Create the corners of AABB to draw the lines connecting them
	local bottom_left = vmath.vector3(lower.x, lower.y, 0.0)
	local bottom_right = vmath.vector3(upper.x , lower.y, 0.0)
	local top_right = vmath.vector3(upper.x, upper.y, 0.0)
	local top_left = vmath.vector3(lower.x, upper.y, 0.0)

	-- Draw the 4 lines forming a rectangle representing the AABB
	draw_line(bottom_left, bottom_right, color)
	draw_line(bottom_right, top_right, color)
	draw_line(top_right, top_left, color)
	draw_line(top_left, bottom_left, color)
end

-- Return the Box2D body from a V2 or V3 overlap/raycast hit.
local function get_hit_body(hit)
	-- Box2D V2 overlap results expose the hit body directly.
	if hit.body then
		return hit.body
	elseif hit.fixture then
		return hit.fixture.body -- Box2D V2 raycast results expose the hit body through the fixture.
	elseif hit.shape then
		return b2d.shape.get_body(hit.shape.shape_id) -- Box2D V3 raycast results expose a shape info table with a shape id.
	end

	-- Box2D V3 overlap results expose a shape id, so the body is resolved from the shape.
	return b2d.shape.get_body(hit.shape_id) -- <7>
end

-- Convert overlap query results into a set of target ids.
local function collect_hit_targets(self, hits)
	local hit_targets = {}

	-- For each hit - read the hit body's position so it can be matched to one target game object.
	for _, hit in ipairs(hits) do
		local body_position = b2d.body.get_position(get_hit_body(hit))

		-- For each target check if position
		for _, target in ipairs(self.targets) do

			-- Check if shape position is almost the same as the given target position
			if vmath.length_sqr(body_position - target.position) < 0.1 then
				-- Save the data about hit in the table
				hit_targets[target.id] = true
				break
			end

		end
	end

	return hit_targets
end

function update(self, dt)
	-- Update the position of the queries
	local lower = self.pointer - AABB_HALF_SIZE
	local upper = self.pointer + AABB_HALF_SIZE
	local aabb = { lower = lower, upper = upper }
	local circle = { type = b2d.shape.SHAPE_TYPE_CIRCLE, center = self.pointer, radius = CIRCLE_RADIUS }
	local ray_delta = self.pointer - RAY_ORIGIN

	go.set_position(self.pointer, "/aabb")
	go.set_position(self.pointer, "/circle_query")

	-- Query all fixtures or shapes whose AABB overlaps the pointer-centered box
	local aabb_hits = b2d.world.overlap_aabb(self.world, aabb, nil, 16)

	-- Query all fixtures or shapes overlapping the pointer-centered circle
	local circle_hits = b2d.world.overlap_shape(self.world, circle, nil, 16)

	-- Cast a ray from the scene center using a translation vector.
	local ray_hits = b2d.world.cast_ray(self.world, RAY_ORIGIN, ray_delta, nil, 16)

	local aabb_targets = collect_hit_targets(self, aabb_hits)
	local circle_targets = collect_hit_targets(self, circle_hits)
	local ray_targets = collect_hit_targets(self, ray_hits)

	-- Change the circle shape tint to show if any overlap is detected
	go.set("/aabb#sprite", "tint", #aabb_hits > 0 and HIT_COLOR or AABB_COLOR)
	go.set("/circle_query#sprite", "tint", #circle_hits > 0 and HIT_COLOR or CIRCLE_COLOR)

	-- Draw the current AABB query visual shape to show if any overlap is detected
	draw_aabb(aabb, #aabb_hits > 0 and HIT_COLOR or LINE_COLOR)
	draw_line(RAY_ORIGIN, self.pointer, #ray_hits > 0 and HIT_COLOR or LINE_COLOR) -- Draw the ray in white, or green when it hits anything.

	-- Draw defined target AABBs outlines and highlight them when hit by the AABB query
	for _, target in ipairs(self.targets) do
		local shape_hit = circle_targets[target.id] or ray_targets[target.id]
		go.set("/" .. target.id .. "#sprite", "tint", shape_hit and HIT_COLOR or target.color) -- <12> Tint target sprites when the circle shape query or raycast hits the actual target shape.
		draw_aabb(target.aabb, aabb_targets[target.id] and HIT_COLOR or LINE_COLOR) -- <13> Highlight target AABBs only when the AABB query hits that target.
	end

	-- Show how many fixtures or shapes each query hit
	label.set_text("#counts", string.format("AABB: %d   Circle: %d   Ray: %d", #aabb_hits, #circle_hits, #ray_hits)) -- <14>
end
```
