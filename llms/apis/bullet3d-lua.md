# bullet3d

**Namespace:** `bullet3d`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_bullet3d.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/bullet3d/script_bullet3d.cpp`

Native-style access to the Bullet 3D world and collision objects owned by
Defold. World creation, destruction and stepping remain controlled by Defold.
The backend name refers to three-dimensional physics.

World, collision-object and rigid-body userdata are borrowed handles to
Defold-owned objects. Shape userdata are borrowed logical child-slot handles
attached to a collision object. Constraint userdata identify auxiliary native
objects owned by this Lua API; destroy them explicitly when no longer needed.
They are also destroyed automatically when a required body or world is
destroyed.

A collision-object, rigid-body or shape handle becomes invalid when its
collision object is deleted or reloaded. A world handle remains valid across
collision-object reloads, but becomes invalid when its collection and physics
world are destroyed. The corresponding `is_valid()` function is safe for
checking a retained handle; every other operation rejects an invalid handle.

## API

### btCollisionObject
*Type:* TYPEDEF
Bullet collision object

**Parameters**

- `value` (userdata)

### btDiscreteDynamicsWorld
*Type:* TYPEDEF
Bullet dynamics world

**Parameters**

- `value` (userdata)

### btRigidBody
*Type:* TYPEDEF
Rigid bodies use the same Lua userdata representation as collision objects,
but rigid-body functions validate the native type before upcasting it.

**Parameters**

- `value` (userdata)

### bullet3d.get_collision_object
*Type:* FUNCTION
This returns both rigid bodies and ghost trigger objects.
This function raises an error unless the collection uses 3D physics.

**Parameters**

- `url` (string | hash | url) - collision object component URL

**Returns**

- `object` (btCollisionObject | nil) - the collision object, or <code>nil</code>

### bullet3d.get_rigid_body
*Type:* FUNCTION
Trigger components are ghost objects, so this function returns nil for them.
This function raises an error unless the collection uses 3D physics.

**Parameters**

- `url` (string | hash | url) - collision object component URL

**Returns**

- `body` (btRigidBody | nil) - the rigid body handle, or <code>nil</code>

**Examples**

```
local world = bullet3d.get_world()
local body = bullet3d.get_rigid_body("#collisionobject")
if world and body and bullet3d.rigid_body.is_valid(body) then
    bullet3d.rigid_body.apply_central_impulse(body, vmath.vector3(0, 10, 0))
end

-- A trigger is a collision object, not a rigid body.
local trigger = bullet3d.get_collision_object("#trigger")
assert(trigger and bullet3d.get_rigid_body("#trigger") == nil)

```

### bullet3d.get_version
*Type:* FUNCTION
Get the Bullet version

**Returns**

- `info` (bullet3d.version_info) - version information

### bullet3d.get_world
*Type:* FUNCTION
This function raises an error unless the collection uses 3D physics.

**Returns**

- `world` (btDiscreteDynamicsWorld | nil) - the world, or <code>nil</code> if the collection has no physics world

### bullet3d.version_info
*Type:* STRUCT
Bullet version information

**Members**

- `version` (string) - full Bullet version string
- `number` (integer) - compact numeric Bullet version
- `major` (integer) - major version number
- `minor` (integer) - minor version number
