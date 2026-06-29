# b2d.fixture

**Namespace:** `b2d.fixture`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_box2d_fixture_v2.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/box2d/v2/script_box2d_fixture_v2.cpp`

Functions for interacting with fixtures attached to Box2D bodies.
Fixtures are addressed functionally by `(body, fixture_index)` rather than persistent Lua handles.

## API

### b2d.fixture.get_aabb
*Type:* FUNCTION
Get fixture AABB for a child shape.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>
- `child_index` (number) - 1-based child shape index

**Returns**

- `aabb` (table) - table with <code>lower</code> and <code>upper</code>

### b2d.fixture.get_density
*Type:* FUNCTION
Get fixture density.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>

**Returns**

- `density` (number) - density in kg/m^2

### b2d.fixture.get_filter_data
*Type:* FUNCTION
Get fixture filter data for a child shape.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>
- `child_index` (number) - 1-based child shape index

**Returns**

- `filter` (table) - table with <code>category_bits</code>, <code>mask_bits</code>, and <code>group_index</code>

### b2d.fixture.get_friction
*Type:* FUNCTION
Get fixture friction.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>

**Returns**

- `friction` (number)

### b2d.fixture.get_restitution
*Type:* FUNCTION
Get fixture restitution.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>

**Returns**

- `restitution` (number)

### b2d.fixture.get_shape
*Type:* FUNCTION
Get the fixture shape as a functional shape table.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>

**Returns**

- `shape` (table) - shape table with numeric <code>type</code> from <code>b2d.shape.SHAPE_TYPE_*</code>,
suitable for reuse in <code>b2d.body.create_fixture</code>.
Circle shapes use <code>radius</code> and <code>center</code>, edge shapes use <code>v1</code>, <code>v2</code>, optional <code>v0</code>, <code>v3</code>,
polygon shapes use <code>vertices</code>, and chain shapes use <code>vertices</code>, <code>loop</code>, optional <code>prev_vertex</code>, and <code>next_vertex</code>.
Any angle values are in radians.

### b2d.fixture.get_type
*Type:* FUNCTION
Get the fixture type.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>

**Returns**

- `type` (number)

### b2d.fixture.is_sensor
*Type:* FUNCTION
Check if a fixture is a sensor.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>

**Returns**

- `enabled` (boolean)

### b2d.fixture.refilter
*Type:* FUNCTION
Refilter a fixture.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>
- `touch_proxies` (boolean) - if true, touch broad-phase proxies

### b2d.fixture.set_density
*Type:* FUNCTION
Set fixture density.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>
- `density` (number) - density in kg/m^2
- `update_mass` (boolean) - if true, reset body mass data after the change

### b2d.fixture.set_filter_data
*Type:* FUNCTION
Set fixture filter data for a child shape.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>
- `child_index` (number) - 1-based child shape index
- `filter` (table) - table with <code>category_bits</code>, <code>mask_bits</code>, and <code>group_index</code>

### b2d.fixture.set_friction
*Type:* FUNCTION
Set fixture friction.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>
- `friction` (number)

### b2d.fixture.set_restitution
*Type:* FUNCTION
Set fixture restitution.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>
- `restitution` (number)

### b2d.fixture.set_sensor
*Type:* FUNCTION
Set sensor mode for a fixture.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>
- `enabled` (boolean)

### b2d.fixture.set_shape
*Type:* FUNCTION
This updates the existing Box2D v2 shape using the same table format as
b2d.body.create_fixture and b2d.fixture.get_shape.
The shape type must match the current fixture shape type. Polygon updates must
keep the same vertex count. Chain shape geometry cannot be updated in-place.
The body mass is not updated unless update_mass is true.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>
- `shape` (table) - shape table with numeric <code>type</code> from <code>b2d.shape.SHAPE_TYPE_*</code>
- `update_mass` (boolean) - if true, reset body mass data after the change

**Examples**

```
local body = b2d.get_body("#collisionobject")

-- Move a circle shape relative to the body origin.
local circle = b2d.fixture.get_shape(body, 1)
circle.center = vmath.vector3(24, 0, 0)
b2d.fixture.set_shape(body, 1, circle, true)

-- Replace an edge shape's local endpoints.
b2d.fixture.set_shape(body, 2, {
    type = b2d.shape.SHAPE_TYPE_EDGE,
    v1 = vmath.vector3(-32, 0, 0),
    v2 = vmath.vector3( 32, 0, 0),
})

-- Update a box shape using the polygon box convenience format.
-- The existing polygon must already have four vertices.
b2d.fixture.set_shape(body, 3, {
    type = b2d.shape.SHAPE_TYPE_BOX,
    hx = 16,
    hy = 8,
    center = vmath.vector3(0, 20, 0),
    angle = math.rad(30),
}, true)

```

### b2d.fixture.test_point
*Type:* FUNCTION
Test a point against a fixture.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>
- `point` (vector3) - point in world coordinates

**Returns**

- `hit` (boolean)
