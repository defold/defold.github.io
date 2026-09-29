# bullet3d.constraint

**Namespace:** `bullet3d.constraint`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_bullet3d_constraint.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/bullet3d/script_bullet3d_constraint.cpp`

Creates and controls Bullet constraints between Defold rigid bodies. A
constraint belongs to the supplied world and is destroyed automatically
with either body, with the world, or when the module is finalized. It is
temporarily removed from the native world while either linked body is
disabled and is restored when both bodies are enabled again. Dropping its
Lua userdata does not destroy the native constraint; call `destroy` for
early release.

Creator positions and all other linear values use Defold units and are
converted with `physics.scale`. Angles are radians. Axes are one-based in
Lua: axes 1-3 are linear and axes 4-6 are angular. Mutating functions cannot
be called while the physics world is stepping. Floating-point and vector
inputs must be finite. Axis vectors must be non-zero and are normalized.
Input rotations must be finite, non-zero quaternions and are normalized by
the binding.

`CONSTRAINT_TYPE_*` values identify the concrete constraint exposed by this
binding. This deliberately distinguishes universal, hinge2, and spring 6-DOF
constraints independently of Bullet's internal constraint type hierarchy.

## API

### btTypedConstraint
*Type:* TYPEDEF
Bullet typed constraint

**Parameters**

- `value` (userdata) - opaque constraint handle

### bullet3d.constraint.anchor_axes_params
*Type:* STRUCT
Universal and hinge2 constraint parameters

**Members**

- `anchor` (vector3) - world-space anchor
- `axis1` (vector3) - first non-zero world-space axis
- `axis2` (vector3) - second non-zero world-space axis, orthogonal to <code>axis1</code>
- `collide_connected?` (boolean) - whether connected bodies can collide; defaults to <code>false</code>

### bullet3d.constraint.cone_twist_params
*Type:* STRUCT
The frame-B fields are required for a two-body constraint.

**Members**

- `frame_a_position` (vector3) - local body-A frame position
- `frame_a_rotation` (quaternion) - local body-A frame rotation
- `frame_b_position?` (vector3) - local body-B frame position
- `frame_b_rotation?` (quaternion) - local body-B frame rotation
- `angular_only?` (boolean) - whether to constrain angular motion only
- `collide_connected?` (boolean) - whether connected bodies can collide; defaults to <code>false</code>

### bullet3d.constraint.CONSTRAINT_TYPE
*Type:* ENUM
Constraint types

**Members**

- `bullet3d.constraint.CONSTRAINT_TYPE_CONE_TWIST` - Cone-twist constraint type
- `bullet3d.constraint.CONSTRAINT_TYPE_GENERIC_6DOF` - Generic 6-DOF constraint type
- `bullet3d.constraint.CONSTRAINT_TYPE_GENERIC_6DOF_SPRING` - Generic spring 6-DOF constraint type
- `bullet3d.constraint.CONSTRAINT_TYPE_HINGE` - Hinge constraint type
- `bullet3d.constraint.CONSTRAINT_TYPE_HINGE2` - Hinge2 constraint type
- `bullet3d.constraint.CONSTRAINT_TYPE_POINT_TO_POINT` - Point-to-point constraint type
- `bullet3d.constraint.CONSTRAINT_TYPE_SLIDER` - Slider constraint type
- `bullet3d.constraint.CONSTRAINT_TYPE_UNIVERSAL` - Universal constraint type

### bullet3d.constraint.create_cone_twist
*Type:* FUNCTION
The world is derived from body_a.

**Parameters**

- `body_a` (btRigidBody) - first body
- `body_b` (btRigidBody | nil) - second body or world
- `params` (bullet3d.constraint.cone_twist_params) - local frames and options

**Returns**

- `constraint` (btTypedConstraint) - cone-twist constraint

### bullet3d.constraint.create_generic_6dof
*Type:* FUNCTION
The params table requires local frame A and, for a two-body constraint,
local frame B. It optionally accepts collide_connected. The world is
derived from body_a. The active 6-DOF solver ignores its legacy
linear-reference-frame selector, so that field is rejected rather than
silently accepted.

**Parameters**

- `body_a` (btRigidBody) - first body
- `body_b` (btRigidBody | nil) - second body or world
- `params` (bullet3d.constraint.generic_6dof_params) - local frames and options

**Returns**

- `constraint` (btTypedConstraint) - generic 6-DOF constraint

### bullet3d.constraint.create_generic_6dof_spring
*Type:* FUNCTION
Both bodies and both local frames are required. The params table optionally
accepts collide_connected. The world is derived from body_a. The active
spring 6-DOF solver ignores its legacy linear-reference-frame selector, so
that field is rejected rather than silently accepted.

**Parameters**

- `body_a` (btRigidBody) - first body
- `body_b` (btRigidBody) - second body
- `params` (bullet3d.constraint.generic_6dof_spring_params) - local frames and options

**Returns**

- `constraint` (btTypedConstraint) - spring 6-DOF constraint

**Examples**

Create a spring that moves along its first linear axis:
```
function init(self)
    local body_a = bullet3d.get_rigid_body("/body_a#collisionobject")
    local body_b = bullet3d.get_rigid_body("/body_b#collisionobject")
    self.spring = bullet3d.constraint.create_generic_6dof_spring(body_a, body_b, {
        frame_a_position = vmath.vector3(),
        frame_a_rotation = vmath.quat(),
        frame_b_position = vmath.vector3(),
        frame_b_rotation = vmath.quat(),
    })
    bullet3d.constraint.set_limit(self.spring, 1, -1, 1)
    bullet3d.constraint.enable_spring(self.spring, 1, true)
    bullet3d.constraint.set_spring_stiffness(self.spring, 1, 20)
    bullet3d.constraint.set_spring_damping(self.spring, 1, 0.5)
    bullet3d.constraint.set_spring_equilibrium_point(self.spring, 1, 0)
end

function final(self)
    if self.spring and bullet3d.constraint.is_valid(self.spring) then
        bullet3d.constraint.destroy(self.spring)
    end
end

```

### bullet3d.constraint.create_hinge
*Type:* FUNCTION
The world is derived from body_a.

**Parameters**

- `body_a` (btRigidBody) - first body
- `body_b` (btRigidBody | nil) - second body or world
- `params` (bullet3d.constraint.hinge_params) - local frames and options

**Returns**

- `constraint` (btTypedConstraint) - hinge constraint

**Examples**

Create a motorized hinge with a 90-degree range:
```
function init(self)
    local body_a = bullet3d.get_rigid_body("/door#collisionobject")
    local body_b = bullet3d.get_rigid_body("/frame#collisionobject")
    self.hinge = bullet3d.constraint.create_hinge(body_a, body_b, {
        frame_a_position = vmath.vector3(-0.5, 0, 0),
        frame_a_rotation = vmath.quat(),
        frame_b_position = vmath.vector3(0.5, 0, 0),
        frame_b_rotation = vmath.quat(),
    })
    bullet3d.constraint.set_hinge_limits(self.hinge, -math.pi / 4, math.pi / 4)
    bullet3d.constraint.set_hinge_motor(self.hinge, true, 1.5, 2.5)
end

function final(self)
    if self.hinge and bullet3d.constraint.is_valid(self.hinge) then
        bullet3d.constraint.destroy(self.hinge)
    end
end

```

### bullet3d.constraint.create_hinge2
*Type:* FUNCTION
Both bodies are required. Its initial linear suspension travel is one Defold
unit in either direction. The world is derived from body_a.

**Parameters**

- `body_a` (btRigidBody) - first body
- `body_b` (btRigidBody) - second body
- `params` (bullet3d.constraint.anchor_axes_params) - anchor, axes, and options

**Returns**

- `constraint` (btTypedConstraint) - hinge2 constraint

### bullet3d.constraint.create_point_to_point
*Type:* FUNCTION
The world is derived from body_a; both bodies must belong to that same world.

**Parameters**

- `body_a` (btRigidBody) - first body
- `body_b` (btRigidBody | nil) - second body or world
- `params` (bullet3d.constraint.point_to_point_params) - pivots and options

**Returns**

- `constraint` (btTypedConstraint) - point-to-point constraint

**Examples**

Join two bodies at matching local pivots and explicitly destroy the
constraint when the script is finalized:
```
function init(self)
    local body_a = bullet3d.get_rigid_body("/body_a#collisionobject")
    local body_b = bullet3d.get_rigid_body("/body_b#collisionobject")
    self.constraint = bullet3d.constraint.create_point_to_point(body_a, body_b, {
        pivot_a = vmath.vector3(0.5, 0, 0),
        pivot_b = vmath.vector3(-0.5, 0, 0),
    })
end

function final(self)
    if self.constraint and bullet3d.constraint.is_valid(self.constraint) then
        bullet3d.constraint.destroy(self.constraint)
    end
end

```

### bullet3d.constraint.create_slider
*Type:* FUNCTION
The world is derived from body_a.

**Parameters**

- `body_a` (btRigidBody) - first body
- `body_b` (btRigidBody | nil) - second body or world
- `params` (bullet3d.constraint.slider_params) - local frames and options

**Returns**

- `constraint` (btTypedConstraint) - slider constraint

### bullet3d.constraint.create_universal
*Type:* FUNCTION
Both bodies are required. The world is derived from body_a.

**Parameters**

- `body_a` (btRigidBody) - first body
- `body_b` (btRigidBody) - second body
- `params` (bullet3d.constraint.anchor_axes_params) - anchor, axes, and options

**Returns**

- `constraint` (btTypedConstraint) - universal constraint

### bullet3d.constraint.destroy
*Type:* FUNCTION
Destroy a constraint

**Parameters**

- `constraint` (btTypedConstraint) - constraint

### bullet3d.constraint.enable_cone_twist_motor
*Type:* FUNCTION
Enable or disable the cone-twist motor

**Parameters**

- `constraint` (btTypedConstraint) - cone-twist constraint
- `enabled` (boolean) - motor state

### bullet3d.constraint.enable_spring
*Type:* FUNCTION
Enable or disable a spring axis

**Parameters**

- `constraint` (btTypedConstraint) - spring 6-DOF or hinge2 constraint
- `axis` (integer) - one-based axis from 1 to 6
- `enabled` (boolean) - spring state

### bullet3d.constraint.generic_6dof_params
*Type:* STRUCT
The frame-B fields are required for a two-body constraint.

**Members**

- `frame_a_position` (vector3) - local body-A frame position
- `frame_a_rotation` (quaternion) - local body-A frame rotation
- `frame_b_position?` (vector3) - local body-B frame position
- `frame_b_rotation?` (quaternion) - local body-B frame rotation
- `collide_connected?` (boolean) - whether connected bodies can collide; defaults to <code>false</code>

### bullet3d.constraint.generic_6dof_spring_params
*Type:* STRUCT
Generic spring 6-DOF constraint parameters

**Members**

- `frame_a_position` (vector3) - local body-A frame position
- `frame_a_rotation` (quaternion) - local body-A frame rotation
- `frame_b_position` (vector3) - local body-B frame position
- `frame_b_rotation` (quaternion) - local body-B frame rotation
- `collide_connected?` (boolean) - whether connected bodies can collide; defaults to <code>false</code>

### bullet3d.constraint.get_6dof_angle
*Type:* FUNCTION
Get a current 6-DOF angle

**Parameters**

- `constraint` (btTypedConstraint) - 6-DOF-derived constraint
- `axis` (integer) - one-based angular-axis index from 1 to 3

**Returns**

- `angle` (number) - current angle in radians

### bullet3d.constraint.get_6dof_axis
*Type:* FUNCTION
Get a current 6-DOF angular axis

**Parameters**

- `constraint` (btTypedConstraint) - 6-DOF-derived constraint
- `axis` (integer) - one-based angular-axis index from 1 to 3

**Returns**

- `direction` (vector3) - world-space unit axis

### bullet3d.constraint.get_6dof_motor
*Type:* FUNCTION
Axes 1-3 are linear and axes 4-6 are angular. Generic 6-DOF, generic spring
6-DOF, and universal constraints support bounce only on angular axes; hinge2
supports it on every axis. Linear target velocity uses Defold units per
second and angular target velocity uses radians per second. max_force is a
force for linear axes and a torque in Defold squared units for angular axes.

**Parameters**

- `constraint` (btTypedConstraint) - 6-DOF-derived constraint
- `axis` (integer) - one-based axis from 1 to 6

**Returns**

- `enabled` (boolean) - motor state
- `target_velocity` (number) - linear or angular target velocity
- `max_force` (number) - maximum motor force for linear axes or torque for angular axes
- `bounce` (number) - bounce from 0 to 1

### bullet3d.constraint.get_6dof_position
*Type:* FUNCTION
Get a current 6-DOF linear position

**Parameters**

- `constraint` (btTypedConstraint) - 6-DOF-derived constraint
- `axis` (integer) - one-based linear-axis index from 1 to 3

**Returns**

- `position` (number) - relative position in Defold units

### bullet3d.constraint.get_anchors
*Type:* FUNCTION
Get universal or hinge2 anchors

**Parameters**

- `constraint` (btTypedConstraint) - universal or hinge2 constraint

**Returns**

- `anchor_a` (vector3) - world-space anchor on body A
- `anchor_b` (vector3) - world-space anchor on body B

### bullet3d.constraint.get_angles
*Type:* FUNCTION
Get universal or hinge2 angles

**Parameters**

- `constraint` (btTypedConstraint) - universal or hinge2 constraint

**Returns**

- `angle_1` (number) - first angle in radians
- `angle_2` (number) - second angle in radians

### bullet3d.constraint.get_axes
*Type:* FUNCTION
Get universal or hinge2 axes

**Parameters**

- `constraint` (btTypedConstraint) - universal or hinge2 constraint

**Returns**

- `axis_1` (vector3) - first world-space unit axis
- `axis_2` (vector3) - second world-space unit axis

### bullet3d.constraint.get_body_a
*Type:* FUNCTION
Get the first linked body

**Parameters**

- `constraint` (btTypedConstraint) - constraint

**Returns**

- `body` (btRigidBody) - first body

### bullet3d.constraint.get_body_b
*Type:* FUNCTION
Get the second linked body

**Parameters**

- `constraint` (btTypedConstraint) - constraint

**Returns**

- `body` (btRigidBody | nil) - second body, or nil for a world constraint

### bullet3d.constraint.get_collide_connected
*Type:* FUNCTION
Get whether connected bodies can collide

**Parameters**

- `constraint` (btTypedConstraint) - constraint

**Returns**

- `collide` (boolean) - whether connected bodies can collide

### bullet3d.constraint.get_cone_twist_limits
*Type:* FUNCTION
Get cone-twist angular spans

**Parameters**

- `constraint` (btTypedConstraint) - cone-twist constraint

**Returns**

- `swing_span_1` (number) - first swing span in radians
- `swing_span_2` (number) - second swing span in radians
- `twist_span` (number) - twist span in radians

### bullet3d.constraint.get_frame_a
*Type:* FUNCTION
Supported constraint types are hinge, cone-twist, generic 6-DOF, generic
spring 6-DOF, slider, universal, and hinge2. Point-to-point constraints use
get_pivots instead.
Returns position and rotation. For one-body generic 6-DOF and slider
constraints this is the user-body frame, despite Bullet storing it as its
native frame B.

**Parameters**

- `constraint` (btTypedConstraint) - framed constraint

**Returns**

- `position` (vector3) - local position
- `rotation` (quaternion) - local rotation

### bullet3d.constraint.get_frame_b
*Type:* FUNCTION
Supports the same constraint types as get_frame_a. For a one-body
constraint, this is the frame attached to the fixed world body.

**Parameters**

- `constraint` (btTypedConstraint) - framed constraint

**Returns**

- `position` (vector3) - local position or world frame position
- `rotation` (quaternion) - local rotation or world frame rotation

### bullet3d.constraint.get_hinge_angle
*Type:* FUNCTION
Get the current hinge angle

**Parameters**

- `constraint` (btTypedConstraint) - hinge constraint

**Returns**

- `angle` (number) - angle in radians

### bullet3d.constraint.get_hinge_limits
*Type:* FUNCTION
Get hinge angular limits

**Parameters**

- `constraint` (btTypedConstraint) - hinge constraint

**Returns**

- `lower` (number) - lower angle in radians
- `upper` (number) - upper angle in radians

### bullet3d.constraint.get_hinge_motor
*Type:* FUNCTION
Get hinge motor settings

**Parameters**

- `constraint` (btTypedConstraint) - hinge constraint

**Returns**

- `enabled` (boolean) - motor state
- `target_velocity` (number) - angular target velocity in radians per second
- `max_impulse` (number) - maximum angular motor impulse in Defold squared units

### bullet3d.constraint.get_limit
*Type:* FUNCTION
Axes 1-3 return linear limits in Defold units. Axes 4-6 return angular
limits in radians.

**Parameters**

- `constraint` (btTypedConstraint) - 6-DOF-derived constraint
- `axis` (integer) - one-based axis from 1 to 6

**Returns**

- `lower` (number) - lower limit
- `upper` (number) - upper limit

### bullet3d.constraint.get_pivots
*Type:* FUNCTION
Get point-to-point pivots

**Parameters**

- `constraint` (btTypedConstraint) - point-to-point constraint

**Returns**

- `pivot_a` (vector3) - local body-A pivot
- `pivot_b` (vector3) - local body-B pivot or world anchor

### bullet3d.constraint.get_slider_limits
*Type:* FUNCTION
Get slider limits

**Parameters**

- `constraint` (btTypedConstraint) - slider constraint

**Returns**

- `lower_linear` (number) - lower linear limit in Defold units
- `upper_linear` (number) - upper linear limit in Defold units
- `lower_angular` (number) - lower angular limit in radians
- `upper_angular` (number) - upper angular limit in radians

### bullet3d.constraint.get_slider_motor
*Type:* FUNCTION
The linear motor uses Defold units per second and maximum force. The angular
motor uses radians per second and maximum torque in Defold squared units.

**Parameters**

- `constraint` (btTypedConstraint) - slider constraint
- `motor` (string) - <code>linear</code> or <code>angular</code>

**Returns**

- `enabled` (boolean) - motor state
- `target_velocity` (number) - linear or angular target velocity
- `max_force` (number) - maximum linear force or angular torque

### bullet3d.constraint.get_slider_position
*Type:* FUNCTION
Get the current slider position

**Parameters**

- `constraint` (btTypedConstraint) - slider constraint

**Returns**

- `position` (number) - current linear position in Defold units

### bullet3d.constraint.get_twist_angle
*Type:* FUNCTION
Get the current cone-twist twist angle

**Parameters**

- `constraint` (btTypedConstraint) - cone-twist constraint

**Returns**

- `angle` (number) - twist angle in radians

### bullet3d.constraint.get_type
*Type:* FUNCTION
Get the constraint type

**Parameters**

- `constraint` (btTypedConstraint) - constraint

**Returns**

- `type` (bullet3d.constraint.CONSTRAINT_TYPE) - constraint type

### bullet3d.constraint.get_type_name
*Type:* FUNCTION
Returns a stable lowercase diagnostic name such as "hinge" or
"generic_6dof_spring".

**Parameters**

- `constraint` (btTypedConstraint) - constraint

**Returns**

- `name` (string) - constraint type name

### bullet3d.constraint.get_use_linear_reference_frame_a
*Type:* FUNCTION
Get the slider linear reference-frame choice

**Parameters**

- `constraint` (btTypedConstraint) - slider constraint

**Returns**

- `use_frame_a` (boolean) - true when linear calculations reference frame A

### bullet3d.constraint.get_world
*Type:* FUNCTION
Get the owning world

**Parameters**

- `constraint` (btTypedConstraint) - constraint

**Returns**

- `world` (btDiscreteDynamicsWorld) - owning world

### bullet3d.constraint.hinge_params
*Type:* STRUCT
The frame-B fields are required for a two-body constraint.

**Members**

- `frame_a_position` (vector3) - local body-A frame position
- `frame_a_rotation` (quaternion) - local body-A frame rotation
- `frame_b_position?` (vector3) - local body-B frame position
- `frame_b_rotation?` (quaternion) - local body-B frame rotation
- `use_reference_frame_a?` (boolean) - whether angular calculations reference frame A
- `angular_only?` (boolean) - whether to constrain angular motion only
- `collide_connected?` (boolean) - whether connected bodies can collide; defaults to <code>false</code>

### bullet3d.constraint.is_active
*Type:* FUNCTION
Test whether a constraint is active in its world

**Parameters**

- `constraint` (btTypedConstraint) - constraint

**Returns**

- `active` (boolean) - false while a linked body is disabled

### bullet3d.constraint.is_angular_only
*Type:* FUNCTION
Test angular-only mode

**Parameters**

- `constraint` (btTypedConstraint) - hinge or cone-twist constraint

**Returns**

- `angular_only` (boolean) - angular-only state

### bullet3d.constraint.is_limited
*Type:* FUNCTION
Both a ranged and a locked axis are considered limited; a free axis is not.

**Parameters**

- `constraint` (btTypedConstraint) - 6-DOF-derived constraint
- `axis` (integer) - one-based axis from 1 to 6

**Returns**

- `limited` (boolean) - limit state

### bullet3d.constraint.is_past_swing_limit
*Type:* FUNCTION
Test whether a cone-twist is past its swing limit

**Parameters**

- `constraint` (btTypedConstraint) - cone-twist constraint

**Returns**

- `past_limit` (boolean) - swing-limit state

### bullet3d.constraint.is_valid
*Type:* FUNCTION
Test whether a constraint handle is valid

**Parameters**

- `constraint` (btTypedConstraint) - constraint handle

**Returns**

- `valid` (boolean) - true while the native constraint exists

### bullet3d.constraint.point_to_point_params
*Type:* STRUCT
pivot_b is required for a two-body constraint. For a one-body constraint,
it is an optional world-space anchor.

**Members**

- `pivot_a` (vector3) - local body-A pivot
- `pivot_b?` (vector3) - local body-B pivot or world-space anchor
- `collide_connected?` (boolean) - whether connected bodies can collide; defaults to <code>false</code>

### bullet3d.constraint.set_6dof_motor
*Type:* FUNCTION
Linear and angular values use the units described by get_6dof_motor.

**Parameters**

- `constraint` (btTypedConstraint) - 6-DOF-derived constraint
- `axis` (integer) - one-based axis from 1 to 6
- `enabled` (boolean) - motor state
- `target_velocity` (number) - linear or angular target velocity
- `max_force` (number) - non-negative maximum motor force for linear axes or torque for angular axes
- `bounce` (number | nil) (optional) - optional bounce from 0 to 1; defaults to <code>0</code>

### bullet3d.constraint.set_angular_only
*Type:* FUNCTION
Set angular-only mode

**Parameters**

- `constraint` (btTypedConstraint) - hinge or cone-twist constraint
- `angular_only` (boolean) - angular-only state

### bullet3d.constraint.set_cone_twist_limits
*Type:* FUNCTION
Set cone-twist angular spans

**Parameters**

- `constraint` (btTypedConstraint) - cone-twist constraint
- `swing_span_1` (number) - non-negative first swing span in radians
- `swing_span_2` (number) - non-negative second swing span in radians
- `twist_span` (number) - non-negative twist span in radians
- `softness` (number | nil) (optional) - optional softness from 0 to 1; defaults to <code>1</code>
- `bias` (number | nil) (optional) - optional bias from 0 to 1; defaults to <code>0.3</code>
- `relaxation` (number | nil) (optional) - optional relaxation from 0 to 1; defaults to <code>1</code>

### bullet3d.constraint.set_cone_twist_motor_target
*Type:* FUNCTION
By default, target is the desired rotation of body A relative to body B.
With constraint_space set, it is the desired rotation of frame A relative
to frame B in constraint space.

**Parameters**

- `constraint` (btTypedConstraint) - cone-twist constraint
- `target` (quaternion) - finite, non-zero target orientation; normalized by the binding
- `constraint_space` (boolean | nil) (optional) - optional target-is-in-constraint-space flag; defaults to <code>false</code>

### bullet3d.constraint.set_frame_a
*Type:* FUNCTION
Frame mutation is supported for hinge, generic 6-DOF, generic spring 6-DOF,
and slider constraints. Cone-twist, universal, and hinge2 frames are
read-only through this API.

**Parameters**

- `constraint` (btTypedConstraint) - mutable framed constraint
- `position` (vector3) - finite local position
- `rotation` (quaternion) - finite, non-zero local rotation; normalized by the binding

### bullet3d.constraint.set_frame_b
*Type:* FUNCTION
Supports the same constraint types as set_frame_a. For a one-body
constraint, this changes the frame attached to the fixed world body.

**Parameters**

- `constraint` (btTypedConstraint) - mutable framed constraint
- `position` (vector3) - finite local position or world frame position
- `rotation` (quaternion) - finite, non-zero local or world frame rotation; normalized by the binding

### bullet3d.constraint.set_hinge_axis
*Type:* FUNCTION
This function only supports hinges attached to the world. For a two-body
hinge, change both local frames with set_frame_a and set_frame_b.

**Parameters**

- `constraint` (btTypedConstraint) - one-body hinge constraint
- `axis` (vector3) - non-zero axis in body-A space

### bullet3d.constraint.set_hinge_limits
*Type:* FUNCTION
Set hinge angular limits

**Parameters**

- `constraint` (btTypedConstraint) - hinge constraint
- `lower` (number) - lower angle in radians
- `upper` (number) - upper angle in radians
- `bias` (number | nil) (optional) - optional limit bias from 0 to 1; defaults to <code>0.3</code>
- `relaxation` (number | nil) (optional) - optional relaxation from 0 to 1; defaults to <code>1</code>

### bullet3d.constraint.set_hinge_motor
*Type:* FUNCTION
Set hinge motor settings

**Parameters**

- `constraint` (btTypedConstraint) - hinge constraint
- `enabled` (boolean) - motor state
- `target_velocity` (number) - angular target velocity in radians per second
- `max_impulse` (number) - non-negative maximum angular motor impulse in Defold squared units

### bullet3d.constraint.set_hinge_motor_target
*Type:* FUNCTION
Set a hinge motor angle target

**Parameters**

- `constraint` (btTypedConstraint) - hinge constraint
- `target_angle` (number) - target angle in radians
- `time_step` (number) - positive step duration in seconds

### bullet3d.constraint.set_limit
*Type:* FUNCTION
Axes 1-3 use Defold units and axes 4-6 use radians. A lower value less than
the upper value creates a limited range, equal values lock the axis, and a
lower value greater than the upper value makes the axis free.

**Parameters**

- `constraint` (btTypedConstraint) - 6-DOF-derived constraint
- `axis` (integer) - one-based axis from 1 to 6
- `lower` (number) - lower limit
- `upper` (number) - upper limit

### bullet3d.constraint.set_pivots
*Type:* FUNCTION
Set point-to-point pivots

**Parameters**

- `constraint` (btTypedConstraint) - point-to-point constraint
- `pivot_a` (vector3) - local body-A pivot
- `pivot_b` (vector3) - local body-B pivot or world anchor

### bullet3d.constraint.set_slider_limits
*Type:* FUNCTION
Each lower/upper pair follows Bullet's limit convention: lower less than
upper creates a limited range, equal values lock that axis, and lower greater
than upper makes it free. Bullet normalizes the angular limits.

**Parameters**

- `constraint` (btTypedConstraint) - slider constraint
- `lower_linear` (number) - lower linear limit in Defold units
- `upper_linear` (number) - upper linear limit in Defold units
- `lower_angular` (number) - lower angular limit in radians
- `upper_angular` (number) - upper angular limit in radians

### bullet3d.constraint.set_slider_motor
*Type:* FUNCTION
Linear and angular values use the units described by get_slider_motor.

**Parameters**

- `constraint` (btTypedConstraint) - slider constraint
- `motor` (string) - <code>linear</code> or <code>angular</code>
- `enabled` (boolean) - motor state
- `target_velocity` (number) - linear or angular target velocity
- `max_force` (number) - non-negative maximum linear force or angular torque

### bullet3d.constraint.set_spring_damping
*Type:* FUNCTION
Generic spring 6-DOF constraints use a scale-independent damping factor from
0 to 1, where 1 means no damping. Hinge2 constraints use a damping coefficient
where 0 means no damping and any non-negative value is accepted. Hinge2
angular damping is automatically converted using physics.scale squared.

**Parameters**

- `constraint` (btTypedConstraint) - spring 6-DOF or hinge2 constraint
- `axis` (integer) - one-based axis from 1 to 6
- `damping` (number) - damping value in the range required by the constraint type

### bullet3d.constraint.set_spring_equilibrium_point
*Type:* FUNCTION
With no axis, captures all current transforms. With an axis and no value,
captures that axis. Linear values use Defold units and angular values use
radians.

**Parameters**

- `constraint` (btTypedConstraint) - spring 6-DOF or hinge2 constraint
- `axis` (integer | nil) (optional) - optional one-based axis from 1 to 6
- `value` (number | nil) (optional) - optional explicit equilibrium value

### bullet3d.constraint.set_spring_stiffness
*Type:* FUNCTION
Linear stiffness values are independent of physics.scale. Angular
stiffness values are automatically converted using physics.scale squared.

**Parameters**

- `constraint` (btTypedConstraint) - spring 6-DOF or hinge2 constraint
- `axis` (integer) - one-based axis from 1 to 6
- `stiffness` (number) - non-negative stiffness

### bullet3d.constraint.slider_params
*Type:* STRUCT
The frame-B fields are required for a two-body constraint.

**Members**

- `frame_a_position` (vector3) - local body-A frame position
- `frame_a_rotation` (quaternion) - local body-A frame rotation
- `frame_b_position?` (vector3) - local body-B frame position
- `frame_b_rotation?` (quaternion) - local body-B frame rotation
- `use_linear_reference_frame_a?` (boolean) - whether linear calculations reference frame A
- `collide_connected?` (boolean) - whether connected bodies can collide; defaults to <code>false</code>
