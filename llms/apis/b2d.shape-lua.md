# b2d.shape

**Namespace:** `b2d.shape`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_box2d_shape_v2.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/box2d/v2/script_box2d_shape_v2.cpp`

Constants for functional shape tables used with `b2d.body.create_fixture`
and returned from `b2d.fixture.get_shape`.

## API

### b2d.shape.are_contact_events_enabled
*Type:* FUNCTION
Check if contact events are enabled for a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `enabled` (boolean) - true if contact events are enabled

### b2d.shape.are_hit_events_enabled
*Type:* FUNCTION
Check if hit events are enabled for a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `enabled` (boolean) - true if hit events are enabled

### b2d.shape.are_pre_solve_events_enabled
*Type:* FUNCTION
Check if pre-solve events are enabled for a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `enabled` (boolean) - true if pre-solve events are enabled

### b2d.shape.are_sensor_events_enabled
*Type:* FUNCTION
Check if sensor events are enabled for a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `enabled` (boolean) - true if sensor events are enabled

### b2d.shape.definition
*Type:* TYPEDEF
A reusable table describing Box2D shape geometry. It is accepted by shape
creation, query, cast, and update functions, and is returned by
b2d.shape.get_shape or b2d.fixture.get_shape. Available fields
depend on type:

Circle: radius and optional center.
Capsule: radius, center1, and center2.
Edge or segment: v1, v2, and optional ghost vertices v0 and v3.
Box: half-extents hx and hy, with optional center and angle in radians.
Polygon: vertices.
Chain: vertices, with optional loop and ghost-vertex fields.

The union covers both supported Box2D runtime versions; some shape types are
only available with one version.

**Parameters**

- `value` ({ type:b2d.shape.SHAPE_TYPE, radius:number, center?:vector3 } | { type:b2d.shape.SHAPE_TYPE, radius:number, center1:vector3, center2:vector3 } | { type:b2d.shape.SHAPE_TYPE, v1:vector3, v2:vector3, v0?:vector3, v3?:vector3 } | { type:b2d.shape.SHAPE_TYPE, hx:number, hy:number, center?:vector3, angle?:number } | { type:b2d.shape.SHAPE_TYPE, vertices:vector3[], loop?:boolean, prev_vertex?:vector3, next_vertex?:vector3 })

**Examples**

```
local circle = {
    type = b2d.shape.SHAPE_TYPE_CIRCLE,
    radius = 16,
    center = vmath.vector3(0, 8, 0),
}

local box = {
    type = b2d.shape.SHAPE_TYPE_BOX,
    hx = 32,
    hy = 8,
    angle = math.rad(15),
}

```

### b2d.shape.enable_contact_events
*Type:* FUNCTION
Enable or disable contact events for a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>
- `enable` (boolean) - true to enable contact events

### b2d.shape.enable_hit_events
*Type:* FUNCTION
Enable or disable hit events for a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>
- `enable` (boolean) - true to enable hit events

### b2d.shape.enable_pre_solve_events
*Type:* FUNCTION
Enable or disable pre-solve events for a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>
- `enable` (boolean) - true to enable pre-solve events

### b2d.shape.enable_sensor_events
*Type:* FUNCTION
Enable or disable sensor events for a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>
- `enable` (boolean) - true to enable sensor events

### b2d.shape.get_body
*Type:* FUNCTION
Get the body owning a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `body` (b2Body) - owning body

### b2d.shape.get_closest_point
*Type:* FUNCTION
Get the closest point on a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>
- `target` (vector3) - world target point

**Returns**

- `point` (vector3) - closest world point on the shape

### b2d.shape.get_contact_capacity
*Type:* FUNCTION
Get shape contact capacity.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `capacity` (integer) - maximum contact data count

### b2d.shape.get_contact_data
*Type:* FUNCTION
Get touching contact data for a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `contacts` (b2d.contact_data[]) - touching contacts

### b2d.shape.get_mass_data
*Type:* FUNCTION
Get mass data for a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `data` (b2d.mass_data) - shape mass data

### b2d.shape.get_material
*Type:* FUNCTION
Get shape material id.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `material` (integer) - shape material id

### b2d.shape.get_sensor_capacity
*Type:* FUNCTION
Get sensor overlap capacity.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `capacity` (integer) - maximum sensor overlap count

### b2d.shape.get_sensor_overlaps
*Type:* FUNCTION
Get sensor overlaps.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `overlaps` (b2d.shape_info[]) - overlapping shapes

### b2d.shape.get_shape
*Type:* FUNCTION
Get a shape's geometry.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `shape` (b2d.shape.definition) - shape table with numeric <code>type</code> from <code>b2d.shape.SHAPE_TYPE_*</code>

### b2d.shape.get_world
*Type:* FUNCTION
Get the world owning a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `world` (b2World) - owning world

### b2d.shape.is_valid
*Type:* FUNCTION
Validate a shape handle.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `valid` (boolean) - true if the shape handle still refers to a live Box2D shape

### b2d.shape.ray_cast
*Type:* FUNCTION
Ray cast a shape directly.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>
- `origin` (vector3) - world ray origin
- `translation` (vector3) - world ray translation
- `max_fraction` (number) (optional) - optional maximum translation fraction, defaults to 1

**Returns**

- `hit` (b2d.shape_cast_output | nil) - cast result, or <code>nil</code>

### b2d.shape.set_material
*Type:* FUNCTION
Set shape material id.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>
- `material` (integer) - shape material id

### b2d.shape.set_shape
*Type:* FUNCTION
This updates the shape geometry using the same table format as
b2d.body.create_shape and b2d.shape.get_shape. The body mass is not
updated unless update_mass is true.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>
- `definition` (b2d.shape.definition) - shape table with numeric <code>type</code> from <code>b2d.shape.SHAPE_TYPE_*</code>
- `update_mass` (boolean) - true to reset body mass from shapes

**Examples**

```
local body = b2d.get_body("#collisionobject")

-- Move a circle shape relative to the body origin.
local circle = b2d.shape.get_shape(body, 1)
circle.center = vmath.vector3(24, 0, 0)
b2d.shape.set_shape(body, 1, circle, true)

-- Replace a segment shape's local endpoints.
b2d.shape.set_shape(body, 2, {
    type = b2d.shape.SHAPE_TYPE_SEGMENT,
    v1 = vmath.vector3(-32, 0, 0),
    v2 = vmath.vector3( 32, 0, 0),
})

-- Update a box shape using the polygon box convenience format.
b2d.shape.set_shape(body, 3, {
    type = b2d.shape.SHAPE_TYPE_BOX,
    hx = 16,
    hy = 8,
    center = vmath.vector3(0, 20, 0),
    angle = math.rad(30),
}, true)

```

### b2d.shape.SHAPE_TYPE
*Type:* ENUM
Box2D shape types.

**Members**

- `b2d.shape.SHAPE_TYPE_BOX` - Box shape type alias. Uses the polygon enum value, but indicates the <code>hx</code>/<code>hy</code> box convenience format.
- `b2d.shape.SHAPE_TYPE_CAPSULE` - Capsule shape type.
- `b2d.shape.SHAPE_TYPE_CHAIN` - Chain shape type.
- `b2d.shape.SHAPE_TYPE_CIRCLE` - Circle shape type.
- `b2d.shape.SHAPE_TYPE_EDGE` - Edge shape type alias. Compatibility alias for <code>b2d.shape.SHAPE_TYPE_SEGMENT</code>.
- `b2d.shape.SHAPE_TYPE_GRID` - Grid shape type.
- `b2d.shape.SHAPE_TYPE_POLYGON` - Polygon shape type.
- `b2d.shape.SHAPE_TYPE_SEGMENT` - Segment shape type.

### b2Shape
*Type:* TYPEDEF
An opaque handle to one collision shape attached to a b2Body. Obtain
shape handles from b2d.body.get_shapes or when creating shapes, then use
the functions in b2d.shape to inspect or modify them. A shape is owned by its
body and its handle becomes invalid when the shape or body is destroyed.

**Parameters**

- `value` (userdata) - Box2D shape handle

**Examples**

```
local body = b2d.get_body("#collisionobject")
local shapes = b2d.body.get_shapes(body)
local shape = shapes[1].shape_id
pprint(b2d.shape.get_shape(shape))

```
