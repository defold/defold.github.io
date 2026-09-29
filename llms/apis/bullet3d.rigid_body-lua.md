# bullet3d.rigid_body

**Namespace:** `bullet3d.rigid_body`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_bullet3d_rigid_body.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/bullet3d/script_bullet3d_rigid_body.cpp`

Rigid body functions accept the collision object userdata returned by
`bullet3d.get_rigid_body()`. Passing a trigger ghost object raises an error.
Defold retains ownership of the collision shape, motion state, world
membership, and native user pointer. The shape's logical children can be
mutated through `bullet3d.shape`; shared resource shapes become per-instance
copies on first mutation. Mass and local inertia can be changed for dynamic
bodies without changing their Defold collision-object type.

Linear quantities use Defold units. Angular velocity, damping, and factors
are unscaled. Torque and angular impulse use squared physics scale because
inertia scales with length squared. Floating-point and vector inputs must be
finite. Damping must be in `[0, 1]`, and sleeping thresholds must be
non-negative.

## API

### bullet3d.rigid_body.apply_central_force
*Type:* FUNCTION
Apply a force at the center of mass

**Parameters**

- `body` (btRigidBody) - rigid body
- `force` (vector3) - force in Defold units

### bullet3d.rigid_body.apply_central_impulse
*Type:* FUNCTION
Apply an impulse at the center of mass

**Parameters**

- `body` (btRigidBody) - rigid body
- `impulse` (vector3) - impulse in Defold units

### bullet3d.rigid_body.apply_force
*Type:* FUNCTION
This has the same point semantics as b2d.body.apply_force: world_position
is the point where the force is applied. The binding converts it to the
center-of-mass-relative offset expected by Bullet's applyForce method.

**Parameters**

- `body` (btRigidBody) - rigid body
- `force` (vector3) - force in Defold units
- `world_position` (vector3) - application point in world space and Defold units

**Examples**

Apply an upward force at the game object's current world position:
```
function init(self)
    local body = bullet3d.get_rigid_body("#collisionobject")
    local force = vmath.vector3(0, 100, 0)
    bullet3d.rigid_body.apply_force(body, force, go.get_world_position())
end

```

### bullet3d.rigid_body.apply_force_at_relative_position
*Type:* FUNCTION
This exposes Bullet's btRigidBody::applyForce point convention directly.
relative_position is an offset from the body's center of mass expressed in
world axes, not a world position or body-local coordinate.

**Parameters**

- `body` (btRigidBody) - rigid body
- `force` (vector3) - force in Defold units
- `relative_position` (vector3) - center-of-mass-relative offset in world axes and Defold units

### bullet3d.rigid_body.apply_impulse
*Type:* FUNCTION
This exposes Bullet's btRigidBody::applyImpulse point convention directly.
relative_position is an offset from the body's center of mass expressed in
world axes, not a world position or body-local coordinate.

**Parameters**

- `body` (btRigidBody) - rigid body
- `impulse` (vector3) - impulse in Defold units
- `relative_position` (vector3) - center-of-mass-relative offset in world axes and Defold units

### bullet3d.rigid_body.apply_linear_impulse
*Type:* FUNCTION
This has the same point semantics as b2d.body.apply_linear_impulse.
world_position is converted to the center-of-mass-relative offset expected
by Bullet's applyImpulse method.

**Parameters**

- `body` (btRigidBody) - rigid body
- `impulse` (vector3) - impulse in Defold units
- `world_position` (vector3) - application point in world space and Defold units

### bullet3d.rigid_body.apply_torque
*Type:* FUNCTION
Apply torque

**Parameters**

- `body` (btRigidBody) - rigid body
- `torque` (vector3) - torque in Defold squared units

### bullet3d.rigid_body.apply_torque_impulse
*Type:* FUNCTION
Apply a torque impulse

**Parameters**

- `body` (btRigidBody) - rigid body
- `impulse` (vector3) - angular impulse in Defold squared units

### bullet3d.rigid_body.clear_forces
*Type:* FUNCTION
Clear accumulated force and torque

**Parameters**

- `body` (btRigidBody) - rigid body

### bullet3d.rigid_body.compute_aabb
*Type:* FUNCTION
Calls Bullet's native btRigidBody::getAabb, which immediately calculates
the bounds from the body's current collision shape and world transform. This
does not read the broadphase proxy's cached AABB.

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `aabb` (bullet3d.world.aabb) - world-space bounds in Defold units

### bullet3d.rigid_body.FLAG
*Type:* ENUM
Combine these constants into the complete flag mask accepted by
bullet3d.rigid_body.set_flags().

**Members**

- `bullet3d.rigid_body.BT_DISABLE_WORLD_GRAVITY` - Disable automatic world gravity. Set this bit before assigning custom body gravity that must survive later world-gravity changes or re-adding the body to a world.
- `bullet3d.rigid_body.BT_ENABLE_GYROSCOPIC_FORCE_EXPLICIT` - Enable explicit gyroscopic force integration.
- `bullet3d.rigid_body.BT_ENABLE_GYROSCOPIC_FORCE_IMPLICIT_WORLD` - Enable implicit world-space gyroscopic force integration.
- `bullet3d.rigid_body.BT_ENABLE_GYROSCOPIC_FORCE_IMPLICIT_BODY` - Enable implicit body-space gyroscopic force integration. This flag is enabled by default for newly constructed rigid bodies.

### bullet3d.rigid_body.get_angular_damping
*Type:* FUNCTION
Get angular damping

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `damping` (number) - angular damping

### bullet3d.rigid_body.get_angular_factor
*Type:* FUNCTION
Get the angular factor

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `factor` (vector3) - per-axis angular factor

### bullet3d.rigid_body.get_angular_sleeping_threshold
*Type:* FUNCTION
Get the angular sleeping threshold

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `threshold` (number) - threshold in radians per second

### bullet3d.rigid_body.get_angular_velocity
*Type:* FUNCTION
Get angular velocity

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `velocity` (vector3) - angular velocity in radians per second

### bullet3d.rigid_body.get_center_of_mass_position
*Type:* FUNCTION
Get the center-of-mass world position

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `position` (vector3) - center-of-mass position in Defold units

### bullet3d.rigid_body.get_damping
*Type:* FUNCTION
Get linear and angular damping

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `linear` (number) - linear damping
- `angular` (number) - angular damping

### bullet3d.rigid_body.get_flags
*Type:* FUNCTION
Get rigid body flags

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `flags` (integer) - rigid body flags

### bullet3d.rigid_body.get_gravity
*Type:* FUNCTION
Get body gravity

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `gravity` (vector3) - gravity in Defold units per second squared

### bullet3d.rigid_body.get_inverse_mass
*Type:* FUNCTION
Get inverse mass

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `inverse_mass` (number) - inverse mass

### bullet3d.rigid_body.get_linear_damping
*Type:* FUNCTION
Get linear damping

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `damping` (number) - linear damping

### bullet3d.rigid_body.get_linear_factor
*Type:* FUNCTION
Get the linear factor

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `factor` (vector3) - per-axis linear factor

### bullet3d.rigid_body.get_linear_sleeping_threshold
*Type:* FUNCTION
Get the linear sleeping threshold

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `threshold` (number) - threshold in Defold units per second

### bullet3d.rigid_body.get_linear_velocity
*Type:* FUNCTION
Get linear velocity

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `velocity` (vector3) - velocity in Defold units per second

### bullet3d.rigid_body.get_linear_velocity_from_local_point
*Type:* FUNCTION
This has the same point semantics as
b2d.body.get_linear_velocity_from_local_point. The local origin is the
body's center of mass.

**Parameters**

- `body` (btRigidBody) - rigid body
- `local_point` (vector3) - point in body-local space and Defold units

**Returns**

- `velocity` (vector3) - point velocity in Defold units per second

### bullet3d.rigid_body.get_linear_velocity_from_world_point
*Type:* FUNCTION
This has the same point semantics as
b2d.body.get_linear_velocity_from_world_point.

**Parameters**

- `body` (btRigidBody) - rigid body
- `world_point` (vector3) - point in world space and Defold units

**Returns**

- `velocity` (vector3) - point velocity in Defold units per second

### bullet3d.rigid_body.get_local_inertia
*Type:* FUNCTION
Returns the diagonal local inertia in Defold mass-times-distance-squared
units. A zero component denotes an axis with zero inverse inertia.

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `inertia` (vector3) - diagonal local inertia

### bullet3d.rigid_body.get_mass
*Type:* FUNCTION
Get mass

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `mass` (number) - mass, or zero for an infinite-mass body

### bullet3d.rigid_body.get_total_force
*Type:* FUNCTION
Get total accumulated force

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `force` (vector3) - accumulated force in Defold units

### bullet3d.rigid_body.get_total_torque
*Type:* FUNCTION
Get total accumulated torque

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `torque` (vector3) - accumulated torque in Defold squared units

### bullet3d.rigid_body.get_velocity_in_local_point
*Type:* FUNCTION
The relative position is expressed in world axes. Despite Bullet's function
name, it is not a body-local coordinate.

**Parameters**

- `body` (btRigidBody) - rigid body
- `relative_position` (vector3) - center-of-mass-relative offset in world axes and Defold units

**Returns**

- `velocity` (vector3) - point velocity in Defold units per second

### bullet3d.rigid_body.get_world
*Type:* FUNCTION
Get the body's world

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `world` (btDiscreteDynamicsWorld) - owning world

### bullet3d.rigid_body.has_flag
*Type:* FUNCTION
Test a rigid body flag

**Parameters**

- `body` (btRigidBody) - rigid body
- `flag` (integer) - flag or mask

**Returns**

- `set` (boolean) - <code>true</code> when all requested flag bits are set

### bullet3d.rigid_body.is_valid
*Type:* FUNCTION
Test whether a handle refers to a valid rigid body

**Parameters**

- `body` (btRigidBody) - rigid body

**Returns**

- `valid` (boolean) - rigid body validity

### bullet3d.rigid_body.set_angular_damping
*Type:* FUNCTION
Set angular damping

**Parameters**

- `body` (btRigidBody) - rigid body
- `damping` (number) - finite angular damping in <code>[0, 1]</code>

### bullet3d.rigid_body.set_angular_factor
*Type:* FUNCTION
Set the angular factor

**Parameters**

- `body` (btRigidBody) - rigid body
- `factor` (vector3) - per-axis angular factor

### bullet3d.rigid_body.set_angular_velocity
*Type:* FUNCTION
Set angular velocity

**Parameters**

- `body` (btRigidBody) - rigid body
- `velocity` (vector3) - finite angular velocity in radians per second

### bullet3d.rigid_body.set_damping
*Type:* FUNCTION
Set linear and angular damping

**Parameters**

- `body` (btRigidBody) - rigid body
- `linear` (number) - finite linear damping in <code>[0, 1]</code>
- `angular` (number) - finite angular damping in <code>[0, 1]</code>

### bullet3d.rigid_body.set_flags
*Type:* FUNCTION
This replaces the complete flag mask. Every enabled gyroscopic mode is
evaluated independently, so clear existing gyroscopic mode bits before
selecting a different mode.

**Parameters**

- `body` (btRigidBody) - rigid body
- `flags` (integer) - rigid body flags

### bullet3d.rigid_body.set_gravity
*Type:* FUNCTION
A later bullet3d.world.set_gravity() call, or removing and re-adding the
body to a world, can overwrite custom body gravity unless the body's
BT_DISABLE_WORLD_GRAVITY flag is set.

**Parameters**

- `body` (btRigidBody) - rigid body
- `gravity` (vector3) - gravity in Defold units per second squared

**Examples**

Give one body persistent custom gravity without discarding its other flags:
```
function init(self)
    local body = bullet3d.get_rigid_body("#collisionobject")
    local flags = bullet3d.rigid_body.get_flags(body)
    flags = bit.bor(flags, bullet3d.rigid_body.BT_DISABLE_WORLD_GRAVITY)
    bullet3d.rigid_body.set_flags(body, flags)
    bullet3d.rigid_body.set_gravity(body, vmath.vector3(0, 4, 0))
end

```

### bullet3d.rigid_body.set_linear_damping
*Type:* FUNCTION
Set linear damping

**Parameters**

- `body` (btRigidBody) - rigid body
- `damping` (number) - finite linear damping in <code>[0, 1]</code>

### bullet3d.rigid_body.set_linear_factor
*Type:* FUNCTION
Set the linear factor

**Parameters**

- `body` (btRigidBody) - rigid body
- `factor` (vector3) - per-axis linear factor

### bullet3d.rigid_body.set_linear_velocity
*Type:* FUNCTION
Set linear velocity

**Parameters**

- `body` (btRigidBody) - rigid body
- `velocity` (vector3) - finite velocity in Defold units per second

### bullet3d.rigid_body.set_mass
*Type:* FUNCTION
Recalculates local inertia from the body's current collision shape. Only a
dynamic body can be changed; zero mass cannot be used to convert it into a
static body. Values too small to have a finite native inverse are rejected.
The body is activated after the update.

**Parameters**

- `body` (btRigidBody) - dynamic rigid body
- `mass` (number) - finite mass greater than zero

**Examples**

Change the mass of a dynamic collision object and inspect its recalculated inertia:
```
function init(self)
    local body = bullet3d.get_rigid_body("#collisionobject")
    bullet3d.rigid_body.set_mass(body, 5)
    print("local inertia", bullet3d.rigid_body.get_local_inertia(body))
end

```

### bullet3d.rigid_body.set_mass_properties
*Type:* FUNCTION
Sets mass and diagonal local inertia together, updates the world-space
inertia tensor, and activates the body. Only dynamic bodies are accepted.
A zero inertia component is allowed and disables angular response on that
local axis; negative, non-finite, or nonzero values too small to have a
finite native inverse are rejected.

**Parameters**

- `body` (btRigidBody) - dynamic rigid body
- `mass` (number) - finite mass greater than zero
- `local_inertia` (vector3) - finite non-negative diagonal local inertia in Defold mass-times-distance-squared units

### bullet3d.rigid_body.set_sleeping_thresholds
*Type:* FUNCTION
Set the sleeping thresholds

**Parameters**

- `body` (btRigidBody) - rigid body
- `linear` (number) - finite non-negative linear threshold in Defold units per second
- `angular` (number) - finite non-negative angular threshold in radians per second
