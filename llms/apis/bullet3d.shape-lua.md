# bullet3d.shape

**Namespace:** `bullet3d.shape`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_bullet3d_shape.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/bullet3d/script_bullet3d_shape.cpp`

Borrowed shape handles identify a one-based child slot on a Defold-owned
collision object. They remain attached to that logical slot when its native
shape is replaced and become invalid with their owning collision object.
Shape mutation is copy-on-write, so instances sharing a collision resource
are not modified together. Lengths use Defold world units.

## API

### btCollisionShape
*Type:* TYPEDEF
Shape handles identify logical child slots and resolve the current native
shape on every call.

**Parameters**

- `value` (userdata)

### bullet3d.collision_object.get_shape
*Type:* FUNCTION
Get one attached shape by one-based index.

**Parameters**

- `object` (btCollisionObject) - collision object
- `shape_index` (integer) - one-based shape index

**Returns**

- `shape` (btCollisionShape) - borrowed logical shape handle

### bullet3d.collision_object.get_shape_count
*Type:* FUNCTION
Get the number of shapes attached to a collision object.

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `count` (integer) - shape count

### bullet3d.collision_object.get_shapes
*Type:* FUNCTION
Get all attached shapes.

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `shapes` (btCollisionShape[]) - array of borrowed shape handles

**Examples**

Enumerate the logical shapes attached to a collision object:
```
function init(self)
    local object = bullet3d.get_collision_object("#collisionobject")
    for _, shape in ipairs(bullet3d.collision_object.get_shapes(object)) do
        local index = bullet3d.shape.get_index(shape)
        local data = bullet3d.shape.get_shape(shape)
        print("shape", index, "type", data.type)
    end
end

```

### bullet3d.shape.definition
*Type:* TYPEDEF
A sphere has diameter; a box has dimensions; a capsule has diameter
and cylindrical-section height; and a convex hull has vertices.
Query functions also accept optional position, rotation, and
target_rotation fields. Lengths use Defold units.

**Parameters**

- `value` ({ type:bullet3d.shape.SHAPE_TYPE, diameter:number, position?:vector3, rotation?:quaternion, target_rotation?:quaternion } | { type:bullet3d.shape.SHAPE_TYPE, dimensions:vector3, position?:vector3, rotation?:quaternion, target_rotation?:quaternion } | { type:bullet3d.shape.SHAPE_TYPE, diameter:number, height:number, position?:vector3, rotation?:quaternion, target_rotation?:quaternion } | { type:bullet3d.shape.SHAPE_TYPE, vertices:vector3[], position?:vector3, rotation?:quaternion, target_rotation?:quaternion }) - collision shape definition

### bullet3d.shape.get_collision_object
*Type:* FUNCTION
Get the owning collision object.

**Parameters**

- `shape` (btCollisionShape) - shape handle

**Returns**

- `object` (btCollisionObject) - owning collision object

### bullet3d.shape.get_index
*Type:* FUNCTION
Get the one-based child index.

**Parameters**

- `shape` (btCollisionShape) - shape handle

**Returns**

- `shape_index` (integer) - one-based shape index

### bullet3d.shape.get_local_transform
*Type:* FUNCTION
A non-compound collision object's only shape has no child transform, so this
function returns the identity transform for it.

**Parameters**

- `shape` (btCollisionShape) - shape handle

**Returns**

- `position` (vector3) - local position
- `rotation` (quaternion) - local rotation

### bullet3d.shape.get_shape
*Type:* FUNCTION
The returned table always contains type, one of bullet3d.shape.SHAPE_TYPE_*.
A sphere also contains numeric diameter; a box contains vector3
dimensions; a capsule contains numeric diameter and cylindrical-section
height; a hull contains a vertices array of vector3 values; and a triangle
mesh contains only type. Primitive and hull tables use Defold units and can
be passed to a bullet3d.world shape query after adding the desired position
and optional rotation fields.

**Parameters**

- `shape` (btCollisionShape) - shape handle

**Returns**

- `data` (bullet3d.shape.definition) - typed shape geometry in Defold units

### bullet3d.shape.get_type
*Type:* FUNCTION
Get the normalized Defold shape type.

**Parameters**

- `shape` (btCollisionShape) - shape handle

**Returns**

- `type` (bullet3d.shape.SHAPE_TYPE) - collision shape type

### bullet3d.shape.is_valid
*Type:* FUNCTION
Test whether a shape handle and its owner still exist.

**Parameters**

- `shape` (btCollisionShape) - shape handle

**Returns**

- `valid` (boolean) - validity

### bullet3d.shape.set_local_transform
*Type:* FUNCTION
A non-compound collision object's only shape has no child transform and is
rejected. The binding normalizes the supplied rotation.

**Parameters**

- `shape` (btCollisionShape) - shape handle
- `position` (vector3) - finite local position
- `rotation` (quaternion) - finite non-zero local rotation

### bullet3d.shape.set_shape
*Type:* FUNCTION
The table uses the same format as get_shape. Its type must match the
existing shape because changing native shape type is not supported. Primitive
dimensions must be finite and greater than zero. Hulls require at least four
finite vertices. Triangle mesh geometry cannot be changed with this function.

**Parameters**

- `shape` (btCollisionShape) - shape handle
- `data` (bullet3d.shape.definition) - typed shape geometry in Defold units

**Examples**

Increase the dimensions of the first box shape by 50 percent for this instance:
```
function init(self)
    local object = bullet3d.get_collision_object("#collisionobject")
    local shape = bullet3d.collision_object.get_shape(object, 1)
    local data = bullet3d.shape.get_shape(shape)

    if data.type == bullet3d.shape.SHAPE_TYPE_BOX then
        data.dimensions = data.dimensions * 1.5
        bullet3d.shape.set_shape(shape, data)
    end
end

```

### bullet3d.shape.SHAPE_TYPE
*Type:* ENUM
Collision shape types

**Members**

- `bullet3d.shape.SHAPE_TYPE_BOX` - Box shape type Value <code>1</code>. Shape data contains positive vector3 <code>dimensions</code> in Defold units.
- `bullet3d.shape.SHAPE_TYPE_CAPSULE` - Capsule shape type Value <code>2</code>. Shape data contains a positive numeric <code>diameter</code> and positive numeric cylindrical-section <code>height</code> in Defold units.
- `bullet3d.shape.SHAPE_TYPE_HULL` - Convex hull shape type Value <code>3</code>. Shape data contains a <code>vertices</code> array with at least four finite vector3 values in Defold units.
- `bullet3d.shape.SHAPE_TYPE_MESH` - Triangle mesh shape type Value <code>4</code>. Shape data contains only the <code>type</code>; triangle geometry is read-only.
- `bullet3d.shape.SHAPE_TYPE_SPHERE` - Sphere shape type Value <code>0</code>. Shape data contains a positive numeric <code>diameter</code> in Defold units.
