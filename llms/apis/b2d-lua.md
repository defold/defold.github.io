# b2d

**Namespace:** `b2d`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_box2d.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/box2d/script_box2d.cpp`

Functions for interacting with Box2D.

## API

### b2Body
*Type:* TYPEDEF
An opaque handle to the native Box2D body of a collision-object component.
Obtain it with b2d.get_body and pass it to functions in b2d.body.
The collision object owns the body, so the handle becomes invalid when its
component or game object is deleted.

**Parameters**

- `value` (userdata) - Box2D body handle

**Examples**

```
local body = b2d.get_body("#collisionobject")
if body then
    print(b2d.body.get_position(body))
end

```

### b2d.aabb
*Type:* STRUCT
Box2D axis-aligned bounding box

**Members**

- `lower` (vector3) - Lower bound.
- `upper` (vector3) - Upper bound.

### b2d.chain_definition
*Type:* STRUCT
Box2D 3.x chain definition

**Members**

- `vertices` (vector3[]) - Chain vertices.
- `loop?` (boolean) - Whether the chain is closed.
- `prev_vertex?` (vector3) - Ghost vertex preceding an open chain.
- `next_vertex?` (vector3) - Ghost vertex following an open chain.
- `friction?` (number) - Segment friction.
- `restitution?` (number) - Segment restitution.
- `material?` (integer) - Segment material identifier.
- `filter?` (b2d.filter_options) - Collision filter fields to override.
- `enable_sensor_events?` (boolean) - Whether to enable sensor events.

### b2d.chain_geometry
*Type:* STRUCT
Box2D chain geometry

**Members**

- `loop` (boolean) - Whether the chain is closed.
- `segment_count` (integer) - Number of chain segments.
- `vertices` (vector3[]) - Chain vertices.
- `prev_vertex?` (vector3) - Ghost vertex preceding an open chain.
- `next_vertex?` (vector3) - Ghost vertex following an open chain.

### b2d.contact_data
*Type:* STRUCT
Box2D contact data

**Members**

- `shape_a` (b2d.shape_info) - First contact shape.
- `shape_b` (b2d.shape_info) - Second contact shape.
- `normal` (vector3) - Contact normal.
- `rolling_impulse` (number) - Rolling resistance impulse.
- `point_count` (integer) - Number of manifold points.
- `points` (b2d.contact_point[]) - Contact manifold points.

### b2d.contact_point
*Type:* STRUCT
Box2D contact manifold point

**Members**

- `point` (vector3) - World contact point.
- `anchor_a` (vector3) - Contact anchor on the first body.
- `anchor_b` (vector3) - Contact anchor on the second body.
- `separation` (number) - Contact separation.
- `normal_impulse` (number) - Normal impulse.
- `tangent_impulse` (number) - Tangent impulse.
- `total_normal_impulse` (number) - Total normal impulse.
- `normal_velocity` (number) - Relative normal velocity.
- `id` (integer) - Contact point identifier.
- `persisted` (boolean) - Whether the point persisted from the previous step.

### b2d.explosion_definition
*Type:* STRUCT
Box2D explosion definition

**Members**

- `position` (vector3) - Explosion center.
- `radius` (number) - Explosion radius.
- `falloff` (number) - Distance over which the impulse falls off.
- `impulse_per_length` (number) - Impulse applied per unit length.
- `mask_bits?` (integer) - Optional collision mask.

### b2d.filter
*Type:* STRUCT
Box2D collision filter

**Members**

- `category_bits` (integer) - Collision category bits.
- `mask_bits` (integer) - Collision mask bits.
- `group_index` (integer) - Collision group index.

### b2d.filter_options
*Type:* STRUCT
Partial Box2D collision filter

**Members**

- `category_bits?` (integer) - Collision category bits.
- `mask_bits?` (integer) - Collision mask bits.
- `group_index?` (integer) - Collision group index.

### b2d.fixture_cast_hit
*Type:* STRUCT
Box2D 2.x cast hit

**Members**

- `fixture` (b2d.fixture_info) - Hit fixture.
- `shape` (b2d.fixture_info) - Hit fixture child shape.
- `point` (vector3) - Hit point.
- `normal` (vector3) - Hit normal.
- `fraction` (number) - Hit fraction.
- `node_visits?` (integer) - Number of tree nodes visited by a closest query.
- `leaf_visits?` (integer) - Number of tree leaves visited by a closest query.

### b2d.fixture_definition
*Type:* STRUCT
Box2D 2.x fixture definition

**Members**

- `shape` (b2d.shape.definition) - Shape definition.
- `friction?` (number) - Fixture friction.
- `restitution?` (number) - Fixture restitution.
- `density?` (number) - Fixture density.
- `sensor?` (boolean) - Whether the fixture is a sensor.
- `is_sensor?` (boolean) - Alias for <code>sensor</code>.
- `filter?` (b2d.filter) - Collision filter.

### b2d.fixture_info
*Type:* STRUCT
Box2D 2.x fixture information

**Members**

- `body?` (b2Body) - Owning body, when returned from a world query.
- `index` (integer) - Fixture index on the body.
- `child_index?` (integer) - Child-shape index, when returned from a world query.
- `type` (b2d.shape.SHAPE_TYPE) - Shape type.
- `sensor` (boolean) - Whether the fixture is a sensor.
- `density` (number) - Fixture density.
- `friction` (number) - Fixture friction.
- `restitution` (number) - Fixture restitution.
- `child_count` (integer) - Number of child shapes.

### b2d.get_body
*Type:* FUNCTION
Get the Box2D body from a collision object

**Parameters**

- `url` (string | hash | url) - the url to the game object collision component

**Returns**

- `body` (b2Body | nil) - the body if successful. Otherwise <code>nil</code>.

### b2d.get_version
*Type:* FUNCTION
Get the Box2D version information for the active backend.

**Returns**

- `info` (b2d.version_info) - version information

### b2d.get_world
*Type:* FUNCTION
Get the Box2D world from the current collection

**Returns**

- `world` (b2World | nil) - the world if successful. Otherwise <code>nil</code>.

### b2d.joint.distance_definition
*Type:* STRUCT
Box2D distance-joint definition

**Members**

- `local_anchor_a?` (vector3) - Local anchor on the first body.
- `local_anchor_b?` (vector3) - Local anchor on the second body.
- `length?` (number) - Rest length.
- `min_length?` (number) - Minimum length.
- `max_length?` (number) - Maximum length.
- `enable_spring?` (boolean) - Whether the spring is enabled.
- `hertz?` (number) - Spring frequency in hertz.
- `frequency?` (number) - Legacy spring frequency alias.
- `damping_ratio?` (number) - Spring damping ratio.
- `damping?` (number) - Legacy spring damping-ratio alias.
- `enable_limit?` (boolean) - Whether length limits are enabled.
- `enable_motor?` (boolean) - Whether the motor is enabled.
- `max_motor_force?` (number) - Maximum motor force.
- `motor_speed?` (number) - Motor speed.
- `collide_connected?` (boolean) - Whether connected bodies collide.

### b2d.joint.filter_definition
*Type:* TYPEDEF
The optional definition passed to b2d.joint.create_filter. Filter joints
currently have no configurable fields, so omit the argument or pass an empty
table. The type is reserved for future options.

**Parameters**

- `value` ({}) - empty filter-joint options

**Examples**

```
local body_a = b2d.get_body("#collisionobject_a")
local body_b = b2d.get_body("#collisionobject_b")
local joint = b2d.joint.create_filter(body_a, body_b, {})

```

### b2d.joint.friction_definition
*Type:* STRUCT
Box2D friction-joint definition

**Members**

- `local_anchor_a?` (vector3) - Local anchor on the first body.
- `local_anchor_b?` (vector3) - Local anchor on the second body.
- `max_force?` (number) - Maximum friction force.
- `max_torque?` (number) - Maximum friction torque.
- `collide_connected?` (boolean) - Whether connected bodies collide.

### b2d.joint.gear_definition
*Type:* STRUCT
Box2D gear-joint definition

**Members**

- `ratio?` (number) - Gear ratio.
- `collide_connected?` (boolean) - Whether connected bodies collide.

### b2d.joint.motor_definition
*Type:* STRUCT
Box2D motor-joint definition

**Members**

- `linear_offset?` (vector3) - Linear target offset.
- `angular_offset?` (number) - Angular target offset.
- `max_force?` (number) - Maximum motor force.
- `max_torque?` (number) - Maximum motor torque.
- `correction_factor?` (number) - Position correction factor.
- `collide_connected?` (boolean) - Whether connected bodies collide.

### b2d.joint.mouse_definition
*Type:* STRUCT
Box2D mouse-joint definition

**Members**

- `target?` (vector3) - Target position.
- `max_force?` (number) - Maximum force.
- `hertz?` (number) - Spring frequency in hertz.
- `frequency?` (number) - Legacy spring frequency alias.
- `damping_ratio?` (number) - Spring damping ratio.
- `damping?` (number) - Legacy spring damping-ratio alias.
- `collide_connected?` (boolean) - Whether connected bodies collide.

### b2d.joint.prismatic_definition
*Type:* STRUCT
Box2D prismatic-joint definition

**Members**

- `local_anchor_a?` (vector3) - Local anchor on the first body.
- `local_anchor_b?` (vector3) - Local anchor on the second body.
- `local_axis_a?` (vector3) - Local translation axis on the first body.
- `reference_angle?` (number) - Reference angle.
- `enable_spring?` (boolean) - Whether the spring is enabled.
- `hertz?` (number) - Spring frequency in hertz.
- `frequency?` (number) - Legacy spring frequency alias.
- `damping_ratio?` (number) - Spring damping ratio.
- `damping?` (number) - Legacy spring damping-ratio alias.
- `enable_limit?` (boolean) - Whether translation limits are enabled.
- `lower_translation?` (number) - Lower translation limit.
- `upper_translation?` (number) - Upper translation limit.
- `enable_motor?` (boolean) - Whether the motor is enabled.
- `max_motor_force?` (number) - Maximum motor force.
- `motor_speed?` (number) - Motor speed.
- `collide_connected?` (boolean) - Whether connected bodies collide.

### b2d.joint.pulley_definition
*Type:* STRUCT
Box2D pulley-joint definition

**Members**

- `ground_anchor_a?` (vector3) - First ground anchor.
- `ground_anchor_b?` (vector3) - Second ground anchor.
- `local_anchor_a?` (vector3) - Local anchor on the first body.
- `local_anchor_b?` (vector3) - Local anchor on the second body.
- `length_a?` (number) - First segment length.
- `length_b?` (number) - Second segment length.
- `ratio?` (number) - Pulley ratio.
- `collide_connected?` (boolean) - Whether connected bodies collide.

### b2d.joint.revolute_definition
*Type:* STRUCT
Box2D revolute-joint definition

**Members**

- `local_anchor_a?` (vector3) - Local anchor on the first body.
- `local_anchor_b?` (vector3) - Local anchor on the second body.
- `reference_angle?` (number) - Reference angle.
- `enable_spring?` (boolean) - Whether the spring is enabled.
- `hertz?` (number) - Spring frequency in hertz.
- `frequency?` (number) - Legacy spring frequency alias.
- `damping_ratio?` (number) - Spring damping ratio.
- `damping?` (number) - Legacy spring damping-ratio alias.
- `enable_limit?` (boolean) - Whether angular limits are enabled.
- `lower_angle?` (number) - Lower angular limit.
- `upper_angle?` (number) - Upper angular limit.
- `enable_motor?` (boolean) - Whether the motor is enabled.
- `max_motor_torque?` (number) - Maximum motor torque.
- `motor_speed?` (number) - Motor speed.
- `collide_connected?` (boolean) - Whether connected bodies collide.

### b2d.joint.rope_definition
*Type:* STRUCT
Box2D rope-joint definition

**Members**

- `local_anchor_a?` (vector3) - Local anchor on the first body.
- `local_anchor_b?` (vector3) - Local anchor on the second body.
- `max_length?` (number) - Maximum rope length.
- `collide_connected?` (boolean) - Whether connected bodies collide.

### b2d.joint.weld_definition
*Type:* STRUCT
Box2D weld-joint definition

**Members**

- `local_anchor_a?` (vector3) - Local anchor on the first body.
- `local_anchor_b?` (vector3) - Local anchor on the second body.
- `reference_angle?` (number) - Reference angle.
- `hertz?` (number) - Legacy spring frequency in hertz.
- `frequency?` (number) - Legacy spring frequency.
- `damping_ratio?` (number) - Legacy spring damping ratio.
- `damping?` (number) - Legacy spring damping-ratio alias.
- `linear_hertz?` (number) - Linear spring frequency in hertz.
- `angular_hertz?` (number) - Angular spring frequency in hertz.
- `linear_damping_ratio?` (number) - Linear damping ratio.
- `angular_damping_ratio?` (number) - Angular damping ratio.
- `collide_connected?` (boolean) - Whether connected bodies collide.

### b2d.joint.wheel_definition
*Type:* STRUCT
Box2D wheel-joint definition

**Members**

- `local_anchor_a?` (vector3) - Local anchor on the first body.
- `local_anchor_b?` (vector3) - Local anchor on the second body.
- `local_axis_a?` (vector3) - Local suspension axis on the first body.
- `enable_spring?` (boolean) - Whether the spring is enabled.
- `hertz?` (number) - Spring frequency in hertz.
- `frequency?` (number) - Legacy spring frequency alias.
- `damping_ratio?` (number) - Spring damping ratio.
- `damping?` (number) - Legacy spring damping-ratio alias.
- `enable_limit?` (boolean) - Whether translation limits are enabled.
- `lower_translation?` (number) - Lower translation limit.
- `upper_translation?` (number) - Upper translation limit.
- `enable_motor?` (boolean) - Whether the motor is enabled.
- `max_motor_torque?` (number) - Maximum motor torque.
- `motor_speed?` (number) - Motor speed.
- `collide_connected?` (boolean) - Whether connected bodies collide.

### b2d.mass_data
*Type:* STRUCT
Mass properties for a Box2D body or shape.

**Members**

- `mass` (number) - Body mass, usually in kilograms.
- `center` (vector3) - Local center of mass.
- `inertia` (number) - Rotational inertia about the local origin.

### b2d.mover_capsule
*Type:* STRUCT
Box2D mover capsule

**Members**

- `center1` (vector3) - First capsule center.
- `center2` (vector3) - Second capsule center.
- `radius` (number) - Capsule radius.

### b2d.mover_plane
*Type:* STRUCT
Box2D mover collision plane

**Members**

- `shape` (b2d.shape_info) - Colliding shape.
- `normal` (vector3) - Plane normal.
- `offset` (number) - Plane offset.
- `hit` (boolean) - Whether the mover hit the plane.

### b2d.query_filter
*Type:* STRUCT
Box2D world-query filter

**Members**

- `category_bits?` (integer) - Optional collision category bits.
- `mask_bits?` (integer) - Optional collision mask bits.
- `group_index?` (integer) - Optional collision group index. Supported by the Box2D 2.x backend.

### b2d.shape_cast_hit
*Type:* STRUCT
Box2D 3.x cast hit

**Members**

- `shape` (b2d.shape_info) - Hit shape.
- `point` (vector3) - Hit point.
- `normal` (vector3) - Hit normal.
- `fraction` (number) - Hit fraction.
- `node_visits?` (integer) - Number of tree nodes visited by a closest query.
- `leaf_visits?` (integer) - Number of tree leaves visited by a closest query.

### b2d.shape_cast_output
*Type:* STRUCT
Direct Box2D shape cast result

**Members**

- `point` (vector3) - Hit point.
- `normal` (vector3) - Hit normal.
- `fraction` (number) - Hit fraction.
- `iterations` (integer) - Number of cast iterations.

### b2d.shape_create_definition
*Type:* TYPEDEF
Geometry and material properties accepted by b2d.body.create_shape. The
geometry can be supplied in the shape field as a b2d.shape.definition,
or its fields can be placed directly in this table. Material properties such
as density, friction, restitution, and filter are optional.

**Parameters**

- `value` ({ shape:b2d.shape.definition, density?:number, friction?:number, restitution?:number, material?:integer, sensor?:boolean, is_sensor?:boolean, filter?:b2d.filter } | { type:b2d.shape.SHAPE_TYPE, radius?:number, center?:vector3, center1?:vector3, center2?:vector3, v0?:vector3, v1?:vector3, v2?:vector3, v3?:vector3, hx?:number, hy?:number, angle?:number, vertices?:vector3[], density?:number, friction?:number, restitution?:number, material?:integer, sensor?:boolean, is_sensor?:boolean, filter?:b2d.filter })

**Examples**

Create a circular shape using an inline geometry definition:
```
local body = b2d.get_body("#collisionobject")
local shape = b2d.body.create_shape(body, {
    type = b2d.shape.SHAPE_TYPE_CIRCLE,
    radius = 16,
    density = 1,
    friction = 0.4,
})

```

### b2d.shape_info
*Type:* STRUCT
Box2D 3.x shape information

**Members**

- `index` (integer) - Shape index on the body.
- `shape_id` (b2Shape) - Shape handle.
- `type` (b2d.shape.SHAPE_TYPE) - Shape type.
- `sensor` (boolean) - Whether the shape is a sensor.
- `density` (number) - Shape density.
- `friction` (number) - Shape friction.
- `restitution` (number) - Shape restitution.
- `material` (integer) - Shape material identifier.
- `child_count` (integer) - Number of child shapes.
- `is_chain_segment` (boolean) - Whether the shape belongs to a chain.

### b2d.transform
*Type:* STRUCT
World transform for a Box2D body.

**Members**

- `position` (vector3) - World position of the body origin.
- `angle` (number) - World rotation angle in radians.

### b2d.tree_stats
*Type:* STRUCT
Box2D broad-phase query statistics

**Members**

- `node_visits` (integer) - Number of tree nodes visited.
- `leaf_visits` (integer) - Number of tree leaves visited.

### b2d.version_info
*Type:* STRUCT
Box2D version information

**Members**

- `version` (string) - Full Box2D version string.
- `major` (integer) - Major version number.
- `middle` (integer) - Middle version number.
- `minor` (integer) - Minor version number.

### b2d.world_counters
*Type:* STRUCT
Box2D world counters

**Members**

- `body_count` (integer) - Number of bodies.
- `shape_count` (integer) - Number of shapes.
- `contact_count` (integer) - Number of contacts.
- `joint_count` (integer) - Number of joints.
- `island_count` (integer) - Number of islands.
- `stack_used` (integer) - Stack bytes in use.
- `static_tree_height` (integer) - Static broad-phase tree height.
- `tree_height` (integer) - Dynamic broad-phase tree height.
- `byte_count` (integer) - Allocated byte count.
- `task_count` (integer) - Number of tasks.
- `color_counts` (integer[]) - Constraint graph color counts.

### b2d.world_profile
*Type:* STRUCT
Box2D world profiling data

**Members**

- `step` (number) - Total step time.
- `pairs` (number) - Pair update time.
- `collide` (number) - Collision time.
- `solve` (number) - Solver time.
- `merge_islands` (number) - Island merge time.
- `prepare_stages` (number) - Stage preparation time.
- `solve_constraints` (number) - Constraint solver time.
- `prepare_constraints` (number) - Constraint preparation time.
- `integrate_velocities` (number) - Velocity integration time.
- `warm_start` (number) - Warm-start time.
- `solve_impulses` (number) - Impulse solver time.
- `integrate_positions` (number) - Position integration time.
- `relax_impulses` (number) - Impulse relaxation time.
- `apply_restitution` (number) - Restitution time.
- `store_impulses` (number) - Impulse storage time.
- `split_islands` (number) - Island splitting time.
- `transforms` (number) - Transform update time.
- `hit_events` (number) - Hit-event generation time.
- `refit` (number) - Tree refit time.
- `bullets` (number) - Bullet processing time.
- `sleep_islands` (number) - Island sleeping time.
- `sensors` (number) - Sensor processing time.

### b2World
*Type:* TYPEDEF
An opaque handle to the Box2D physics world owned by the current collection.
Obtain it with b2d.get_world and pass it to functions in b2d.world.
The engine creates and destroys the world together with the collection; it
cannot be constructed directly from Lua.

**Parameters**

- `value` (userdata) - Box2D world handle

**Examples**

```
local world = b2d.get_world()
if world then
    pprint(world)
end

```
