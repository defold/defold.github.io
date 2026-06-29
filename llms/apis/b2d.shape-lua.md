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

- `capacity` (number) - maximum contact data count

### b2d.shape.get_contact_data
*Type:* FUNCTION
Get touching contact data for a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `contacts` (table) - array of contact tables

### b2d.shape.get_mass_data
*Type:* FUNCTION
Get mass data for a shape.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `data` (table) - table with <code>mass</code>, <code>center</code>, and <code>inertia</code>

### b2d.shape.get_material
*Type:* FUNCTION
Get shape material id.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `material` (number) - shape material id

### b2d.shape.get_sensor_capacity
*Type:* FUNCTION
Get sensor overlap capacity.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `capacity` (number) - maximum sensor overlap count

### b2d.shape.get_sensor_overlaps
*Type:* FUNCTION
Get sensor overlaps.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `overlaps` (table) - array of shape info tables

### b2d.shape.get_shape
*Type:* FUNCTION
Get a shape's geometry.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `shape` (table) - shape table with numeric <code>type</code> from <code>b2d.shape.SHAPE_TYPE_*</code>

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
- `max_fraction` (number) - optional maximum translation fraction, defaults to 1

**Returns**

- `hit` (table) - hit table with <code>point</code>, <code>normal</code>, <code>fraction</code>, and <code>iterations</code>, or nil

### b2d.shape.set_material
*Type:* FUNCTION
Set shape material id.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>
- `material` (number) - shape material id

### b2d.shape.set_shape
*Type:* FUNCTION
This updates the shape geometry using the same table format as
b2d.body.create_shape and b2d.shape.get_shape. The body mass is not
updated unless update_mass is true.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>
- `definition` (table) - shape table with numeric <code>type</code> from <code>b2d.shape.SHAPE_TYPE_*</code>
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

### b2d.shape.SHAPE_TYPE_BOX
*Type:* CONSTANT
Uses the polygon enum value, but indicates the hx/hy box convenience format.

### b2d.shape.SHAPE_TYPE_BOX
*Type:* CONSTANT
Uses the polygon enum value, but indicates the hx/hy box convenience format.

### b2d.shape.SHAPE_TYPE_CAPSULE
*Type:* CONSTANT
Capsule shape type.

### b2d.shape.SHAPE_TYPE_CHAIN
*Type:* CONSTANT
Chain shape type.

### b2d.shape.SHAPE_TYPE_CIRCLE
*Type:* CONSTANT
Circle shape type.

### b2d.shape.SHAPE_TYPE_CIRCLE
*Type:* CONSTANT
Circle shape type.

### b2d.shape.SHAPE_TYPE_EDGE
*Type:* CONSTANT
Edge shape type.

### b2d.shape.SHAPE_TYPE_EDGE
*Type:* CONSTANT
Compatibility alias for b2d.shape.SHAPE_TYPE_SEGMENT.

### b2d.shape.SHAPE_TYPE_GRID
*Type:* CONSTANT
Grid shape type.

### b2d.shape.SHAPE_TYPE_POLYGON
*Type:* CONSTANT
Polygon shape type.

### b2d.shape.SHAPE_TYPE_POLYGON
*Type:* CONSTANT
Polygon shape type.

### b2d.shape.SHAPE_TYPE_SEGMENT
*Type:* CONSTANT
Segment shape type.

### b2Shape
*Type:* TYPEDEF
Box2D shape

**Parameters**

- `value` (userdata)
