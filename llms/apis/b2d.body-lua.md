# b2d.body

**Namespace:** `b2d.body`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_box2d_body_v2.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/box2d/v2/script_box2d_body_v2.cpp`

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

### b2d.body.apply_linear_impulse
*Type:* FUNCTION
Apply an impulse at a point. This immediately modifies the velocity.
It also modifies the angular velocity if the point of application
is not at the center of mass. This wakes up the body.

**Parameters**

- `body` (b2Body) - body
- `impulse` (vector3) - the world impulse vector, usually in N-seconds or kg-m/s.
- `point` (vector3) - the world position of the point of application.

### b2d.body.apply_linear_impulse_to_center
*Type:* FUNCTION
Apply a linear impulse to the center of mass.

**Parameters**

- `body` (b2Body) - body
- `impulse` (vector3) - world impulse vector

### b2d.body.apply_torque
*Type:* FUNCTION
Apply a torque. This affects the angular velocity
without affecting the linear velocity of the center of mass.
This wakes up the body.

**Parameters**

- `body` (b2Body) - body
- `torque` (number) - torque about the z-axis (out of the screen), usually in N-m.

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

### b2d.body.B2_DYNAMIC_BODY
*Type:* CONSTANT
Dynamic body

### b2d.body.B2_KINEMATIC_BODY
*Type:* CONSTANT
Kinematic body

### b2d.body.B2_KINEMATIC_BODY
*Type:* CONSTANT
Kinematic body

### b2d.body.B2_STATIC_BODY
*Type:* CONSTANT
Static (immovable) body

### b2d.body.B2_STATIC_BODY
*Type:* CONSTANT
Static (immovable) body

### b2d.body.compute_aabb
*Type:* FUNCTION
Compute the world AABB of all body shapes.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `aabb` (table) - table with <code>lower</code> and <code>upper</code> vector3 fields

### b2d.body.create_chain
*Type:* FUNCTION
Chains are one-sided connected segments with optional ghost vertices at
the ends of open chains. Ghost vertices are creation-time chain data only and
cannot be added to arbitrary shapes, bodies, or joints after creation.

definition.vertices
table array of local vector3 vertices. Open chains require at least 2 vertices. Loop chains require at least 4 vertices.
definition.loop
boolean true to create a closed loop chain.
definition.prev_vertex
vector3 optional ghost vertex before the first vertex for open chains.
definition.next_vertex
vector3 optional ghost vertex after the last vertex for open chains.
definition.friction
number optional friction.
definition.restitution
number optional restitution.
definition.material
number optional material id.
definition.filter
table optional filter with category_bits, mask_bits, and group_index.
definition.enable_sensor_events
boolean true to enable sensor events for chain segments.

**Parameters**

- `body` (b2Body) - body
- `definition` (table) - the chain definition

**Returns**

- `chain` (b2Chain) - created chain handle
- `segments` (table) - array of shape info tables for the chain segments

**Examples**

```
local chain, segments = b2d.body.create_chain(body, {
    vertices = {
        vmath.vector3(-64, 0, 0),
        vmath.vector3(0, 16, 0),
        vmath.vector3(64, 0, 0),
    },
    prev_vertex = vmath.vector3(-96, 0, 0),
    next_vertex = vmath.vector3(96, 0, 0),
    friction = 0.6,
})

```

### b2d.body.create_fixture
*Type:* FUNCTION
Creates a fixture and attach it to this body. Use this function if you need
to set some fixture parameters, like friction. Otherwise you can create the
fixture directly from a shape.
If the density is non-zero, this function automatically updates the mass of the body.
Contacts are not created until the next time step.

**Parameters**

- `body` (b2Body) - body
- `definition` (table) - fixture definition table with:
<code>shape</code> = shape table, <code>friction</code> = number, <code>restitution</code> = number,
<code>density</code> = number, <code>sensor</code> = boolean, and optional <code>filter</code> table.
Supported shape tables are:
<code>circle</code> = <code>{ type = b2d.shape.SHAPE_TYPE_CIRCLE, radius = number, center = vector3_or_nil }</code>
<code>edge</code> = <code>{ type = b2d.shape.SHAPE_TYPE_EDGE, v1 = vector3, v2 = vector3, v0 = vector3_or_nil, v3 = vector3_or_nil }</code>
<code>polygon</code> = <code>{ type = b2d.shape.SHAPE_TYPE_POLYGON, vertices = { vector3, ... } }</code>
<code>box</code> = <code>{ type = b2d.shape.SHAPE_TYPE_BOX, hx = number, hy = number, center = vector3_or_nil, angle = radians_or_nil }</code>
<code>chain</code> = <code>{ type = b2d.shape.SHAPE_TYPE_CHAIN, vertices = { vector3, ... }, loop = boolean_or_nil, prev_vertex = vector3_or_nil, next_vertex = vector3_or_nil }</code>

**Returns**

- `fixture` (table) - fixture info table with <code>index</code>, <code>type</code>, <code>sensor</code>, <code>density</code>, <code>friction</code>, <code>restitution</code>, and <code>child_count</code>

**Examples**

```
local body = b2d.get_body("#collisionobject")

local triangle = b2d.body.create_fixture(body, {
    density = 1.0,
    friction = 0.3,
    shape = {
        type = b2d.shape.SHAPE_TYPE_POLYGON,
        vertices = {
            vmath.vector3(-16, -16, 0),
            vmath.vector3( 16, -16, 0),
            vmath.vector3(  0,  16, 0),
        },
    },
})

```

### b2d.body.create_fixture
*Type:* FUNCTION
Creates a fixture from a shape and attach it to this body.
This is a convenience function. Use b2FixtureDef if you need to set parameters
like friction, restitution, user data, or filtering.
If the density is non-zero, this function automatically updates the mass of the body.

**Parameters**

- `body` (b2Body) - body
- `shape` (b2Shape) - the shape to be cloned.
- `density` (number) - the shape density (set to zero for static bodies).

### b2d.body.create_shape
*Type:* FUNCTION
Creates a shape and attaches it to this body.
If the density is non-zero, this function automatically updates the mass of the body.
Contacts are not created until the next time step.
The definition may include density, friction, restitution, material,
sensor or is_sensor, filter, and the shape table itself. The shape table
can be in definition.shape or directly in definition.

**Parameters**

- `body` (b2Body) - body
- `definition` (table) - the shape definition.

### b2d.body.destroy_fixture
*Type:* FUNCTION
Destroy a fixture from a body.

**Parameters**

- `body` (b2Body) - body
- `fixture_index` (number) - 1-based fixture index from <code>b2d.body.get_fixtures</code>

### b2d.body.destroy_shape
*Type:* FUNCTION
Destroy a shape. This removes the shape from the broad-phase and
destroys all contacts associated with this shape. This will
automatically adjust the mass of the body if the body is dynamic and the
shape has positive density.
All shapes attached to a body are implicitly destroyed when the body is destroyed.

**Parameters**

- `body` (b2Body) - body
- `shape_index` (number) - 1-based shape index from <code>b2d.body.get_shapes</code>

### b2d.body.dump
*Type:* FUNCTION
Print the body representation to the log output

**Parameters**

- `body` (b2Body) - body

### b2d.body.enable_contact_events
*Type:* FUNCTION
Enable or disable contact events on all body shapes.

**Parameters**

- `body` (b2Body) - body
- `enable` (boolean) - true to enable contact events

### b2d.body.enable_hit_events
*Type:* FUNCTION
Enable or disable hit events on all body shapes.

**Parameters**

- `body` (b2Body) - body
- `enable` (boolean) - true to enable hit events

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

### b2d.body.get_angular_velocity
*Type:* FUNCTION
Get the angular velocity.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `velocity` (number) - the angular velocity in radians/second.

### b2d.body.get_contact_data
*Type:* FUNCTION
Get touching contact data for a body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `contacts` (table) - array of contact tables

### b2d.body.get_contact_list
*Type:* FUNCTION
Get the list of all contacts attached to this body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `edge` (b2ContactEdge) - the first edge

### b2d.body.get_contact_list
*Type:* FUNCTION
Get the list of all contacts attached to this body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `edge` (b2ContactEdge) - the first edge

### b2d.body.get_fixtures
*Type:* FUNCTION
Get the fixtures attached to this body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `fixtures` (table) - array of fixture info tables with <code>index</code>, <code>type</code>, <code>sensor</code>, <code>density</code>, <code>friction</code>, <code>restitution</code>, and <code>child_count</code>

### b2d.body.get_force
*Type:* FUNCTION
Get the total force currently applied on this object

**Notes**

- Defold Specific

**Parameters**

- `body` (b2Body) - body

**Returns**

- `force` (vector3)

### b2d.body.get_force
*Type:* FUNCTION
Get the total force currently applied on this object

**Notes**

- Defold Specific

**Parameters**

- `body` (b2Body) - body

**Returns**

- `force` (vector3)

### b2d.body.get_gravity_scale
*Type:* FUNCTION
Get the gravity scale of the body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `scale` (number) - the scale

### b2d.body.get_gravity_scale
*Type:* FUNCTION
Get the gravity scale of the body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `scale` (number) - the scale

### b2d.body.get_inertia
*Type:* FUNCTION
Get the rotational inertia of the body about the local origin.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `inertia` (number) - the rotational inertia, usually in kg-m^2.

### b2d.body.get_joints
*Type:* FUNCTION
Get the joints attached to this body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `joints` (table) - array of <code>b2Joint</code> handles created by <code>b2d.joint</code>

### b2d.body.get_joints
*Type:* FUNCTION
Get the joints attached to this body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `joints` (table) - array of <code>b2Joint</code> handles created by <code>b2d.joint</code>

### b2d.body.get_linear_damping
*Type:* FUNCTION
Get the linear damping of the body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `damping` (number) - the damping

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

### b2d.body.get_linear_velocity_from_world_point
*Type:* FUNCTION
Get the world linear velocity of a world point attached to this body.

**Parameters**

- `body` (b2Body) - body
- `world_point` (vector3) - a point in world coordinates.

**Returns**

- `velocity` (vector3) - the world velocity of a point.

### b2d.body.get_local_center
*Type:* FUNCTION
Get the local position of the center of mass.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `center` (vector3) - Get the local position of the center of mass.

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

### b2d.body.get_mass
*Type:* FUNCTION
Get the total mass of the body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `mass` (number) - the mass, usually in kilograms (kg).

### b2d.body.get_mass_data
*Type:* FUNCTION
Get the mass data of the body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `data` (table) - table with <code>mass</code>, <code>center</code> in local coordinates, and <code>inertia</code>.

### b2d.body.get_mass_data
*Type:* FUNCTION
Get the mass data of the body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `data` (b2MassData) - a struct containing the mass, inertia and center of the body.

### b2d.body.get_name
*Type:* FUNCTION
Get the body name.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `name` (string) - body name, or nil if no name is set

### b2d.body.get_next
*Type:* FUNCTION
Get the next body in the world's body list.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `body` (b2Body) - the next body

### b2d.body.get_position
*Type:* FUNCTION
Get the world body origin position.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `position` (vector3) - the world position of the body's origin.

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

### b2d.body.get_shapes
*Type:* FUNCTION
Get the list of all shapes attached to this body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `shapes` (table) - a table of shape info entries. Each entry includes <code>shape_id</code> for use with <code>b2d.shape</code> functions.

### b2d.body.get_sleep_threshold
*Type:* FUNCTION
Get the sleep velocity threshold.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `threshold` (number) - velocity threshold in Defold units per second

### b2d.body.get_transform
*Type:* FUNCTION
Get the body transform for the body's origin.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `transform` (table) - table with <code>position</code> and <code>angle</code> in radians.

### b2d.body.get_transform
*Type:* FUNCTION
Get the body transform for the body's origin.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `transform` (b2Transform) - the world position of the body's origin.

### b2d.body.get_type
*Type:* FUNCTION
Get the type of this body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `type` (b2BodyType) - the body type

### b2d.body.get_type
*Type:* FUNCTION
Get the type of this body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `type` (b2BodyType) - the body type

### b2d.body.get_user_data
*Type:* FUNCTION
Get the user data pointer that was provided in the body definition.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `id` (hash) - the game object id this body is connected to

### b2d.body.get_world
*Type:* FUNCTION
Get the parent world of this body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `world` (b2World)

### b2d.body.get_world
*Type:* FUNCTION
Get the parent world of this body.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `world` (b2World)

### b2d.body.get_world_center
*Type:* FUNCTION
Get the angle in radians.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `angle` (number) - the current world rotation angle in radians.

### b2d.body.get_world_center
*Type:* FUNCTION
Get the world position of the center of mass.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `center` (vector3) - Get the world position of the center of mass.

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

### b2d.body.is_fixed_rotation
*Type:* FUNCTION
Does this body have fixed rotation?

**Parameters**

- `body` (b2Body) - body

**Returns**

- `enabled` (boolean) - is the rotation fixed

### b2d.body.is_sleeping_allowed
*Type:* FUNCTION
Is this body allowed to sleep

**Parameters**

- `body` (b2Body) - body

**Returns**

- `enabled` (boolean) - true if the body is allowed to sleep

### b2d.body.is_sleeping_enabled
*Type:* FUNCTION
Is this body allowed to sleep

**Parameters**

- `body` (b2Body) - body

**Returns**

- `enabled` (boolean) - true if the body is allowed to sleep

### b2d.body.is_valid
*Type:* FUNCTION
Validate a body handle.

**Parameters**

- `body` (b2Body) - body

**Returns**

- `valid` (boolean) - true if the body handle still refers to a live Box2D body

### b2d.body.reset_mass_data
*Type:* FUNCTION
This resets the mass properties to the sum of the mass properties of the fixtures.
This normally does not need to be called unless you called SetMassData to override

**Parameters**

- `body` (b2Body) - body

### b2d.body.reset_mass_data
*Type:* FUNCTION
This resets the mass properties to the sum of the mass properties of the shapes.
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

### b2d.body.set_active
*Type:* FUNCTION
Set the active state of the body. An inactive body is not
simulated and cannot be collided with or woken up.
If you pass a flag of true, all shapes will be added to the
broad-phase.
If you pass a flag of false, all shapes will be removed from
the broad-phase and all contacts will be destroyed.
Shapes and joints are otherwise unaffected. You may continue
to create/destroy shapes and joints on inactive bodies.
Shapes on an inactive body are implicitly inactive and will
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

### b2d.body.set_linear_velocity
*Type:* FUNCTION
Set the linear velocity of the center of mass.

**Parameters**

- `body` (b2Body) - body
- `velocity` (vector3) - the new linear velocity of the center of mass.

### b2d.body.set_mass_data
*Type:* FUNCTION
Set the mass properties to override the mass properties of the fixtures.

**Notes**

- This function has no effect if the body isn't dynamic.
- This changes the center of mass position.
- Creating or destroying fixtures can also alter the mass.

**Parameters**

- `body` (b2Body) - body
- `data` (table) - table with <code>mass</code>, <code>center</code> in local coordinates, and <code>inertia</code>.

### b2d.body.set_mass_data
*Type:* FUNCTION
Set the mass properties to override the mass properties of the shapes.

**Notes**

- This function has no effect if the body isn't dynamic.
- This changes the center of mass position.
- Creating or destroying shapes can also alter the mass.

**Parameters**

- `body` (b2Body) - body
- `data` (b2MassData) - the mass properties.

### b2d.body.set_name
*Type:* FUNCTION
Set the body name.

**Parameters**

- `body` (b2Body) - body
- `name` (string) - body name

### b2d.body.set_sleep_threshold
*Type:* FUNCTION
Set the sleep velocity threshold.

**Parameters**

- `body` (b2Body) - body
- `threshold` (number) - velocity threshold in Defold units per second

### b2d.body.set_sleeping_allowed
*Type:* FUNCTION
You can disable sleeping on this body. If you disable sleeping, the body will be woken.

**Parameters**

- `body` (b2Body) - body
- `enable` (boolean) - if false, the body will never sleep, and consume more CPU

### b2d.body.set_target_transform
*Type:* FUNCTION
Set velocity to reach a target transform.

**Parameters**

- `body` (b2Body) - body
- `position` (vector3) - target world position
- `angle` (number) - target world angle in radians
- `time_step` (number) - time step used to compute velocity

### b2d.body.set_transform
*Type:* FUNCTION
Set the position of the body's origin and rotation.
This breaks any contacts and wakes the other bodies.
Manipulating a body's transform may cause non-physical behavior.

**Parameters**

- `body` (b2Body) - body
- `position` (vector3) - the world position of the body's local origin.
- `angle` (number) - the world position of the body's local origin.

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

### b2d.body.set_type
*Type:* FUNCTION
Set the type of this body. This may alter the mass and velocity.

**Parameters**

- `body` (b2Body) - body
- `type` (b2BodyType) - the body type

### b2d.body.set_user_data
*Type:* FUNCTION
Set the user data. Use this to store your application specific data.

**Parameters**

- `body` (b2Body) - body
- `id` (hash) - the game object id

### b2World
*Type:* TYPEDEF
Box2D world

**Parameters**

- `value` (userdata)
