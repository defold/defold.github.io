# b2d.body

**Namespace:** `b2d.body`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_box2d_body.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/box2d/script_box2d_body.cpp`

Functions for interacting with Box2D bodies.

## API

### b2Body
*Type:* TYPEDEF
Box2D body

**Parameters**

- `value` (userdata)

### b2d.body.apply_angular_impulse
*Type:* FUNCTION
Apply an angular impulse.

**Parameters**

- `body` (b2Body) - body
- `impulse` (number) - impulse the angular impulse in units of kg<em>m</em>m/s

### b2d.body.apply_force
*Type:* FUNCTION
Apply a force at a world point. If the force is not
applied at the center of mass, it will generate a torque and
affect the angular velocity. This wakes up the body.

**Parameters**

- `body` (b2Body) - body
- `force` (vector3) - the world force vector, usually in Newtons (N).
- `point` (vector3) - the world position of the point of application.

### b2d.body.apply_force_to_center
*Type:* FUNCTION
Apply a force to the center of mass. This wakes up the body.

**Parameters**

- `body` (b2Body) - body
- `force` (vector3) - the world force vector, usually in Newtons (N).

### b2d.body.apply_linear_impulse
*Type:* FUNCTION
Apply an impulse at a point. This immediately modifies the velocity.
It also modifies the angular velocity if the point of application
is not at the center of mass. This wakes up the body.

**Parameters**

- `body` (b2Body) - body
- `impulse` (vector3) - the world impulse vector, usually in N-seconds or kg-m/s.
- `point` (vector3) - the world position of the point of application.

### b2d.body.apply_torque
*Type:* FUNCTION
Apply a torque. This affects the angular velocity
without affecting the linear velocity of the center of mass.
This wakes up the body.

**Parameters**

- `body` (b2Body) - body
- `torque` (number) - torque about the z-axis (out of the screen), usually in N-m.

### b2d.body.B2_DYNAMIC_BODY
*Type:* CONSTANT
Dynamic body

### b2d.body.B2_KINEMATIC_BODY
*Type:* CONSTANT
Kinematic body

### b2d.body.B2_STATIC_BODY
*Type:* CONSTANT
Static (immovable) body

### b2d.body.enable_sleep
*Type:* FUNCTION
You can disable sleeping on this body. If you disable sleeping, the body will be woken.

**Parameters**

- `body` (b2Body) - body
- `enable` (boolean) - if false, the body will never sleep, and consume more CPU

### b2d.body.get_angle
*Type:* FUNCTION
Get the angle in radians.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `angle` (number) - the current world rotation angle in radians.

### b2d.body.get_angular_damping
*Type:* FUNCTION
Get the angular damping of the body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `damping` (number) - the damping

### b2d.body.get_angular_velocity
*Type:* FUNCTION
Get the angular velocity.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `velocity` (number) - the angular velocity in radians/second.

### b2d.body.get_gravity_scale
*Type:* FUNCTION
Get the gravity scale of the body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `scale` (number) - the scale

### b2d.body.get_linear_damping
*Type:* FUNCTION
Get the linear damping of the body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `damping` (number) - the damping

### b2d.body.get_linear_velocity
*Type:* FUNCTION
Get the linear velocity of the center of mass.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `velocity` (vector3) - the linear velocity of the center of mass.

### b2d.body.get_linear_velocity_from_local_point
*Type:* FUNCTION
Get the world velocity of a local point.

**Parameters**

- `body` (b2Body) - body
- `local_point` (vector3) - a point in local coordinates.

**Returns**

- `velocity` (vector3) - the world velocity of a point.

### b2d.body.get_linear_velocity_from_world_point
*Type:* FUNCTION
Get the world linear velocity of a world point attached to this body.

**Parameters**

- `body` (b2Body) - body
- `world_point` (vector3) - a point in world coordinates.

**Returns**

- `velocity` (vector3) - the world velocity of a point.

### b2d.body.get_local_center_of_mass
*Type:* FUNCTION
Get the local position of the center of mass.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `center` (vector3) - Get the local position of the center of mass.

### b2d.body.get_local_point
*Type:* FUNCTION
Gets a local point relative to the body's origin given a world point.

**Parameters**

- `body` (b2Body) - body
- `world_point` (vector3) - a point in world coordinates.

**Returns**

- `vector` (vector3) - the corresponding local point relative to the body's origin.

### b2d.body.get_local_vector
*Type:* FUNCTION
Gets a local vector given a world vector.

**Parameters**

- `body` (b2Body) - body
- `world_vector` (vector3) - a vector in world coordinates.

**Returns**

- `vector` (vector3) - the corresponding local vector.

### b2d.body.get_mass
*Type:* FUNCTION
Get the total mass of the body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `mass` (number) - the mass, usually in kilograms (kg).

### b2d.body.get_position
*Type:* FUNCTION
Get the world body origin position.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `position` (vector3) - the world position of the body's origin.

### b2d.body.get_rotational_inertia
*Type:* FUNCTION
Get the rotational inertia of the body about the local origin.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `inertia` (number) - the rotational inertia, usually in kg-m^2.

### b2d.body.get_type
*Type:* FUNCTION
Get the type of this body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `type` (b2BodyType) - the body type

### b2d.body.get_world
*Type:* FUNCTION
Get the parent world of this body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `world` (b2World)

### b2d.body.get_world_center_of_mass
*Type:* FUNCTION
Get the world position of the center of mass.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `center` (vector3) - Get the world position of the center of mass.

### b2d.body.get_world_point
*Type:* FUNCTION
Get the world coordinates of a point given the local coordinates.

**Parameters**

- `body` (b2Body) - body
- `local_vector` (vector3) - localPoint a point on the body measured relative the the body's origin.

**Returns**

- `vector` (vector3) - the same point expressed in world coordinates.

### b2d.body.get_world_vector
*Type:* FUNCTION
Get the world coordinates of a vector given the local coordinates.

**Parameters**

- `body` (b2Body) - body
- `local_vector` (vector3) - a vector fixed in the body.

**Returns**

- `vector` (vector3) - the same vector expressed in world coordinates.

### b2d.body.is_active
*Type:* FUNCTION
Get the active state of the body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `enabled` (boolean) - is the body active

### b2d.body.is_awake
*Type:* FUNCTION
Get the sleeping state of this body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `enabled` (boolean) - true if the body is awake, false if it's sleeping.

### b2d.body.is_bullet
*Type:* FUNCTION
Is this body in bullet mode

**Parameters**

- `body` (b2Body) - body

**Returns**

- `enabled` (boolean) - true if the body is in bullet mode

### b2d.body.is_fixed_rotation
*Type:* FUNCTION
Does this body have fixed rotation?

**Parameters**

- `body` (b2Body) - body

**Returns**

- `enabled` (boolean) - is the rotation fixed

### b2d.body.is_sleeping_enabled
*Type:* FUNCTION
Is this body allowed to sleep

**Parameters**

- `body` (b2Body) - body

**Returns**

- `enabled` (boolean) - true if the body is allowed to sleep

### b2d.body.reset_mass_data
*Type:* FUNCTION
This resets the mass properties to the sum of the mass properties of the fixtures.
This normally does not need to be called unless you called SetMassData to override

**Parameters**

- `body` (b2Body) - body

### b2d.body.set_active
*Type:* FUNCTION
Set the active state of the body. An inactive body is not
simulated and cannot be collided with or woken up.
If you pass a flag of true, all fixtures will be added to the
broad-phase.
If you pass a flag of false, all fixtures will be removed from
the broad-phase and all contacts will be destroyed.
Fixtures and joints are otherwise unaffected. You may continue
to create/destroy fixtures and joints on inactive bodies.
Fixtures on an inactive body are implicitly inactive and will
not participate in collisions, ray-casts, or queries.
Joints connected to an inactive body are implicitly inactive.
An inactive body is still owned by a b2World object and remains
in the body list.

**Parameters**

- `body` (b2Body) - body
- `enable` (boolean) - true if the body should be active

### b2d.body.set_angular_damping
*Type:* FUNCTION
Set the angular damping of the body.

**Parameters**

- `body` (b2Body) - body
- `damping` (number) - the damping

### b2d.body.set_angular_velocity
*Type:* FUNCTION
Set the angular velocity.

**Parameters**

- `body` (b2Body) - body
- `omega` (number) - the new angular velocity in radians/second.

### b2d.body.set_awake
*Type:* FUNCTION
Set the sleep state of the body. A sleeping body has very low CPU cost.

**Parameters**

- `body` (b2Body) - body
- `enable` (boolean) - flag set to false to put body to sleep, true to wake it.

### b2d.body.set_bullet
*Type:* FUNCTION
Should this body be treated like a bullet for continuous collision detection?

**Parameters**

- `body` (b2Body) - body
- `enable` (boolean) - if true, the body will be in bullet mode

### b2d.body.set_fixed_rotation
*Type:* FUNCTION
Set this body to have fixed rotation. This causes the mass to be reset.

**Parameters**

- `body` (b2Body) - body
- `enable` (boolean) - true if the rotation should be fixed

### b2d.body.set_gravity_scale
*Type:* FUNCTION
Set the gravity scale of the body.

**Parameters**

- `body` (b2Body) - body
- `scale` (number) - the scale

### b2d.body.set_linear_damping
*Type:* FUNCTION
Set the linear damping of the body.

**Parameters**

- `body` (b2Body) - body
- `damping` (number) - the damping

### b2d.body.set_linear_velocity
*Type:* FUNCTION
Set the linear velocity of the center of mass.

**Parameters**

- `body` (b2Body) - body
- `velocity` (vector3) - the new linear velocity of the center of mass.

### b2d.body.set_transform
*Type:* FUNCTION
Set the position of the body's origin and rotation.
This breaks any contacts and wakes the other bodies.
Manipulating a body's transform may cause non-physical behavior.

**Parameters**

- `body` (b2Body) - body
- `position` (vector3) - the world position of the body's local origin.
- `angle` (number) - the world position of the body's local origin.

### b2d.body.set_type
*Type:* FUNCTION
Set the type of this body. This may alter the mass and velocity.

**Parameters**

- `body` (b2Body) - body
- `type` (b2BodyType) - the body type

### b2World
*Type:* TYPEDEF
Box2D world

**Parameters**

- `value` (userdata)
