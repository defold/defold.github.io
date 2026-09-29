# bullet3d.collision_object

**Namespace:** `bullet3d.collision_object`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_bullet3d_collision_object.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/bullet3d/script_bullet3d_collision_object.cpp`

Functions shared by rigid bodies and trigger ghost objects. Defold keeps
ownership of each object's user pointer, motion state, collision shape, and
world membership. Logical child shapes are inspected and mutated through
`bullet3d.shape`; ownership is not transferred to Lua.

Positions, distances, and CCD thresholds use Defold units. Rotations,
coefficients, flags, activation state, and time values use Bullet values.
Floating-point and vector inputs must be finite. CCD radii and motion
thresholds must also be non-negative.

## API

### bullet3d.collision_object.activate
*Type:* FUNCTION
Activate a collision object

**Parameters**

- `object` (btCollisionObject) - collision object
- `force` (boolean) (optional) - force activation of a static or kinematic object; defaults to <code>false</code>

### bullet3d.collision_object.ACTIVATION_STATE
*Type:* ENUM
Collision object activation states

**Members**

- `bullet3d.collision_object.ACTIVE_TAG` - Active simulation state.
- `bullet3d.collision_object.ISLAND_SLEEPING` - Sleeping simulation state.
- `bullet3d.collision_object.WANTS_DEACTIVATION` - Wants-deactivation simulation state.
- `bullet3d.collision_object.DISABLE_DEACTIVATION` - Disable automatic deactivation.
- `bullet3d.collision_object.DISABLE_SIMULATION` - Disable simulation.

### bullet3d.collision_object.COLLISION_FLAG
*Type:* ENUM
Collision object flags

**Members**

- `bullet3d.collision_object.CF_DYNAMIC_OBJECT` - Zero-valued default dynamic-object flag. Compare the complete collision-flags value with this constant; do not pass it to <code>has_collision_flag</code>, since zero is not a bit that can be tested.
- `bullet3d.collision_object.CF_STATIC_OBJECT` - Static collision object flag.
- `bullet3d.collision_object.CF_KINEMATIC_OBJECT` - Kinematic collision object flag.
- `bullet3d.collision_object.CF_NO_CONTACT_RESPONSE` - Disable contact response flag.
- `bullet3d.collision_object.CF_CUSTOM_MATERIAL_CALLBACK` - Custom material callback flag.
- `bullet3d.collision_object.CF_CHARACTER_OBJECT` - Character collision object flag.
- `bullet3d.collision_object.CF_DISABLE_VISUALIZE_OBJECT` - Disable debug visualization flag.
- `bullet3d.collision_object.CF_DISABLE_SPU_COLLISION_PROCESSING` - Disable SPU collision processing flag.

### bullet3d.collision_object.force_activation_state
*Type:* FUNCTION
Force the activation state

**Parameters**

- `object` (btCollisionObject) - collision object
- `state` (bullet3d.collision_object.ACTIVATION_STATE) - activation state

### bullet3d.collision_object.get_activation_state
*Type:* FUNCTION
Get the activation state

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `state` (bullet3d.collision_object.ACTIVATION_STATE) - activation state

### bullet3d.collision_object.get_ccd_motion_threshold
*Type:* FUNCTION
Get the CCD motion threshold

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `threshold` (number) - threshold in Defold units

### bullet3d.collision_object.get_ccd_swept_sphere_radius
*Type:* FUNCTION
Get the CCD swept sphere radius

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `radius` (number) - radius in Defold units

### bullet3d.collision_object.get_collision_filter_group
*Type:* FUNCTION
Returns the raw unsigned 16-bit filter group that Defold assigned to the
object's Bullet broadphase proxy. Use this value as category_bits in a
bullet3d.world query filter. Bullet applies reciprocal filtering: the
query's mask_bits must include this group, and the query's category_bits
must be included in the object's filter mask.

**Parameters**

- `object` (btCollisionObject) - collision object in a Bullet world

**Returns**

- `group` (integer) - raw unsigned 16-bit collision filter group

### bullet3d.collision_object.get_collision_filter_mask
*Type:* FUNCTION
Returns the raw unsigned 16-bit filter mask that Defold assigned to the
object's Bullet broadphase proxy. Use this value as mask_bits in a
bullet3d.world query filter. Bullet applies reciprocal filtering: the
query's category_bits must be included in this mask, and the query's
mask_bits must include the object's filter group.

**Parameters**

- `object` (btCollisionObject) - collision object in a Bullet world

**Returns**

- `mask` (integer) - raw unsigned 16-bit collision filter mask

### bullet3d.collision_object.get_collision_flags
*Type:* FUNCTION
Get collision flags

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `flags` (integer) - bit field of <code>CF_*</code> constants

### bullet3d.collision_object.get_contact_processing_threshold
*Type:* FUNCTION
Get the contact processing threshold

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `threshold` (number) - threshold in Defold units

### bullet3d.collision_object.get_deactivation_time
*Type:* FUNCTION
Get deactivation time

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `seconds` (number) - deactivation time

### bullet3d.collision_object.get_friction
*Type:* FUNCTION
Get friction

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `friction` (number) - friction coefficient

### bullet3d.collision_object.get_internal_type
*Type:* FUNCTION
Get the Bullet collision object type

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `type` (bullet3d.collision_object.INTERNAL_TYPE) - native collision object type

### bullet3d.collision_object.get_position
*Type:* FUNCTION
Get the world position

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `position` (vector3) - world position in Defold units

### bullet3d.collision_object.get_restitution
*Type:* FUNCTION
Get restitution

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `restitution` (number) - restitution coefficient

### bullet3d.collision_object.get_rotation
*Type:* FUNCTION
Get the world rotation

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `rotation` (quaternion) - world rotation

### bullet3d.collision_object.get_world_transform
*Type:* FUNCTION
Get the world transform

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `position` (vector3) - world position in Defold units
- `rotation` (quaternion) - world rotation

### bullet3d.collision_object.has_collision_flag
*Type:* FUNCTION
Test a collision flag

**Parameters**

- `object` (btCollisionObject) - collision object
- `flag` (integer) - collision flag or mask

**Returns**

- `set` (boolean) - <code>true</code> when all requested flag bits are set

### bullet3d.collision_object.has_contact_response
*Type:* FUNCTION
Test whether the object responds to contacts

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `result` (boolean) - contact response state

### bullet3d.collision_object.INTERNAL_TYPE
*Type:* ENUM
Native collision object types

**Members**

- `bullet3d.collision_object.CO_COLLISION_OBJECT` - Generic collision object type.
- `bullet3d.collision_object.CO_RIGID_BODY` - Rigid body collision object type.
- `bullet3d.collision_object.CO_GHOST_OBJECT` - Ghost collision object type.
- `bullet3d.collision_object.CO_SOFT_BODY` - Soft body collision object type.
- `bullet3d.collision_object.CO_HF_FLUID` - Height-field fluid collision object type.

### bullet3d.collision_object.is_active
*Type:* FUNCTION
This exposes Bullet's native btCollisionObject::isActive result. It is
false for ISLAND_SLEEPING and DISABLE_SIMULATION, and true for the
other activation states available to Defold collision objects. It is
unrelated to whether the Defold component is enabled.

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `active` (boolean) - active state

### bullet3d.collision_object.is_awake
*Type:* FUNCTION
Box2D-style name for the same simulation state returned by
bullet3d.collision_object.is_active.

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `awake` (boolean) - <code>false</code> when sleeping or simulation is disabled

### bullet3d.collision_object.is_ghost_object
*Type:* FUNCTION
Test whether the object is a ghost trigger

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `result` (boolean) - ghost object state

### bullet3d.collision_object.is_kinematic
*Type:* FUNCTION
Test whether the object is kinematic

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `kinematic` (boolean) - kinematic state

### bullet3d.collision_object.is_rigid_body
*Type:* FUNCTION
Test whether the object is a rigid body

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `result` (boolean) - rigid body state

### bullet3d.collision_object.is_static
*Type:* FUNCTION
Test whether the object is static

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `static` (boolean) - static state

### bullet3d.collision_object.is_static_or_kinematic
*Type:* FUNCTION
Test whether the object is static or kinematic

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `result` (boolean) - static or kinematic state

### bullet3d.collision_object.is_valid
*Type:* FUNCTION
Test whether a collision object handle is valid

**Parameters**

- `object` (btCollisionObject) - collision object

**Returns**

- `valid` (boolean) - <code>true</code> if the native object still exists

### bullet3d.collision_object.set_activation_state
*Type:* FUNCTION
Set the activation state

**Parameters**

- `object` (btCollisionObject) - collision object
- `state` (bullet3d.collision_object.ACTIVATION_STATE) - activation state

### bullet3d.collision_object.set_awake
*Type:* FUNCTION
Passing true calls Bullet's activate(). Passing false requests the
native ISLAND_SLEEPING state. As in Bullet, static or kinematic objects are
not activated without force, and protected DISABLE_DEACTIVATION or
DISABLE_SIMULATION states are not replaced by a sleeping request.

**Parameters**

- `object` (btCollisionObject) - collision object
- `awake` (boolean) - requested awake state

### bullet3d.collision_object.set_ccd_motion_threshold
*Type:* FUNCTION
Set the CCD motion threshold

**Parameters**

- `object` (btCollisionObject) - collision object
- `threshold` (number) - finite non-negative threshold in Defold units

**Examples**

Enable continuous collision detection for a small, fast-moving body:
```
function init(self)
    local body = bullet3d.get_rigid_body("#collisionobject")
    bullet3d.collision_object.set_ccd_swept_sphere_radius(body, 0.25)
    bullet3d.collision_object.set_ccd_motion_threshold(body, 0.5)
end

```

### bullet3d.collision_object.set_ccd_swept_sphere_radius
*Type:* FUNCTION
Set the CCD swept sphere radius

**Parameters**

- `object` (btCollisionObject) - collision object
- `radius` (number) - finite non-negative radius in Defold units

### bullet3d.collision_object.set_contact_processing_threshold
*Type:* FUNCTION
Set the contact processing threshold

**Parameters**

- `object` (btCollisionObject) - collision object
- `threshold` (number) - finite threshold in Defold units

### bullet3d.collision_object.set_deactivation_time
*Type:* FUNCTION
Set deactivation time

**Parameters**

- `object` (btCollisionObject) - collision object
- `seconds` (number) - finite deactivation time

### bullet3d.collision_object.set_friction
*Type:* FUNCTION
Set friction

**Parameters**

- `object` (btCollisionObject) - collision object
- `friction` (number) - finite friction coefficient

### bullet3d.collision_object.set_position
*Type:* FUNCTION
The owning game object's position is updated as well.

**Parameters**

- `object` (btCollisionObject) - collision object
- `position` (vector3) - finite world position in Defold units

### bullet3d.collision_object.set_restitution
*Type:* FUNCTION
Set restitution

**Parameters**

- `object` (btCollisionObject) - collision object
- `restitution` (number) - finite restitution coefficient

### bullet3d.collision_object.set_rotation
*Type:* FUNCTION
The owning game object's rotation is updated as well.

**Parameters**

- `object` (btCollisionObject) - collision object
- `rotation` (quaternion) - finite, non-zero world rotation; normalized by the binding

### bullet3d.collision_object.set_world_transform
*Type:* FUNCTION
The owning game object's position and rotation are updated as well, so the
transform persists when Defold synchronizes game objects into Bullet.

**Parameters**

- `object` (btCollisionObject) - collision object
- `position` (vector3) - finite world position in Defold units
- `rotation` (quaternion) - finite, non-zero world rotation; normalized by the binding

**Examples**

Move a collision object while preserving its rotation:
```
function init(self)
    local object = bullet3d.get_collision_object("#collisionobject")
    local position, rotation = bullet3d.collision_object.get_world_transform(object)
    bullet3d.collision_object.set_world_transform(
        object,
        position + vmath.vector3(0, 5, 0),
        rotation)
    bullet3d.collision_object.activate(object, true)
end

```
