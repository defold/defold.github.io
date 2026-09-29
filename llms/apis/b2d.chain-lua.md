# b2d.chain

**Namespace:** `b2d.chain`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_box2d_chain_v3.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/box2d/v3/script_box2d_chain_v3.cpp`

Functions for Box2D v3 chains. A chain owns multiple connected segment
shapes, so it is represented by a separate `b2Chain` handle.

## API

### b2Chain
*Type:* TYPEDEF
An opaque handle to a chain of connected segment shapes attached to a
b2Body. Create one with b2d.body.create_chain, use the functions
in b2d.chain to inspect or configure it, and release it with
b2d.chain.destroy. Destroying its body also destroys the chain.

**Parameters**

- `value` (userdata) - Box2D chain handle

**Examples**

```
local body = b2d.get_body("#collisionobject")
local chain = b2d.body.create_chain(body, {
    vertices = {
        vmath.vector3(-64, 0, 0),
        vmath.vector3(0, 16, 0),
        vmath.vector3(64, 0, 0),
    },
})
print(b2d.chain.get_segment_count(chain))

```

### b2d.chain.destroy
*Type:* FUNCTION
Destroying a chain removes all segment shapes owned by the chain. Destroying
any segment shape through b2d.body.destroy_shape also destroys its parent chain.

**Parameters**

- `chain` (b2Chain) - chain

### b2d.chain.from_shape
*Type:* FUNCTION
Returns nil if the shape is not a chain segment.

**Parameters**

- `shape_id` (b2Shape) - shape handle from a shape info table, or pass <code>body, shape_index</code>

**Returns**

- `chain` (b2Chain | nil) - parent chain, or <code>nil</code> if the shape is not a chain segment

### b2d.chain.get_friction
*Type:* FUNCTION
Get chain friction.

**Parameters**

- `chain` (b2Chain) - chain

**Returns**

- `friction` (number) - chain friction

### b2d.chain.get_geometry
*Type:* FUNCTION
Get the chain geometry.

**Parameters**

- `chain` (b2Chain) - chain

**Returns**

- `geometry` (b2d.chain_geometry) - chain geometry

### b2d.chain.get_material
*Type:* FUNCTION
Get chain material id.

**Parameters**

- `chain` (b2Chain) - chain

**Returns**

- `material` (integer) - chain material id

### b2d.chain.get_restitution
*Type:* FUNCTION
Get chain restitution.

**Parameters**

- `chain` (b2Chain) - chain

**Returns**

- `restitution` (number) - chain restitution

### b2d.chain.get_segment_count
*Type:* FUNCTION
Get the number of segment shapes in a chain.

**Parameters**

- `chain` (b2Chain) - chain

**Returns**

- `count` (integer) - segment count

### b2d.chain.get_segments
*Type:* FUNCTION
Get the segment shapes owned by a chain.

**Parameters**

- `chain` (b2Chain) - chain

**Returns**

- `segments` (b2d.shape_info[]) - chain segment shapes

### b2d.chain.get_world
*Type:* FUNCTION
Get the world owning a chain.

**Parameters**

- `chain` (b2Chain) - chain

**Returns**

- `world` (b2World) - owning world

### b2d.chain.is_valid
*Type:* FUNCTION
Validate a chain handle.

**Parameters**

- `chain` (b2Chain) - chain

**Returns**

- `valid` (boolean) - true if the chain handle still refers to a live Box2D chain

### b2d.chain.set_friction
*Type:* FUNCTION
Set chain friction.

**Parameters**

- `chain` (b2Chain) - chain
- `friction` (number) - chain friction

### b2d.chain.set_material
*Type:* FUNCTION
Set chain material id.

**Parameters**

- `chain` (b2Chain) - chain
- `material` (integer) - chain material id

### b2d.chain.set_restitution
*Type:* FUNCTION
Set chain restitution.

**Parameters**

- `chain` (b2Chain) - chain
- `restitution` (number) - chain restitution
