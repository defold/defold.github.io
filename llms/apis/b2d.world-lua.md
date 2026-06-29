# b2d.world

**Namespace:** `b2d.world`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_box2d_world_v2.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/box2d/v2/script_box2d_world_v2.cpp`

Query and cast functions for the Defold-owned Box2D v2 world.

## API

### b2d.world.cast_mover
*Type:* FUNCTION
The capsule table has center1, center2, and radius fields. The return
value is the fraction of translation that can be traveled before collision,
or 1 if there is no hit.

**Parameters**

- `world` (b2World) - world
- `capsule` (table) - capsule table with <code>center1</code>, <code>center2</code>, and <code>radius</code>
- `translation` (vector3) - capsule displacement
- `filter` (table) (optional) - optional query filter with <code>category_bits</code> and <code>mask_bits</code>

**Returns**

- `fraction` (number) - travel fraction before collision

### b2d.world.cast_ray
*Type:* FUNCTION
Cast a ray.

**Parameters**

- `world` (b2World) - world from <code>b2d.get_world</code> or <code>b2d.body.get_world</code>
- `origin` (vector3) - world ray origin
- `translation` (vector3) - world ray translation
- `filter` (table) - optional query filter with <code>category_bits</code>, <code>mask_bits</code>, and optional <code>group_index</code>
- `max_results` (number) - optional maximum result count

**Returns**

- `hits` (table) - array of hit tables with <code>fixture</code>, <code>shape</code>, <code>point</code>, <code>normal</code>, and <code>fraction</code>
- `stats` (table) - table with <code>node_visits</code> and <code>leaf_visits</code>

### b2d.world.cast_ray
*Type:* FUNCTION
The translation is the ray displacement from origin. Result order is not
guaranteed by Box2D.

**Parameters**

- `world` (b2World) - world
- `origin` (vector3) - ray start position
- `translation` (vector3) - ray displacement
- `filter` (table) (optional) - optional query filter with <code>category_bits</code> and <code>mask_bits</code>
- `max_results` (number) (optional) - optional maximum result count. Omit or pass 0 for unlimited results.

**Returns**

- `hits` (table) - array of cast hit tables
- `stats` (table) - tree stats table

### b2d.world.cast_ray_closest
*Type:* FUNCTION
Cast a ray and return the closest hit.

**Parameters**

- `world` (b2World) - world from <code>b2d.get_world</code> or <code>b2d.body.get_world</code>
- `origin` (vector3) - world ray origin
- `translation` (vector3) - world ray translation
- `filter` (table) - optional query filter with <code>category_bits</code>, <code>mask_bits</code>, and optional <code>group_index</code>

**Returns**

- `hit` (table) - hit table with <code>fixture</code>, <code>shape</code>, <code>point</code>, <code>normal</code>, <code>fraction</code>, <code>node_visits</code>, and <code>leaf_visits</code>, or nil

### b2d.world.cast_ray_closest
*Type:* FUNCTION
The translation is the ray displacement from origin.

**Parameters**

- `world` (b2World) - world
- `origin` (vector3) - ray start position
- `translation` (vector3) - ray displacement
- `filter` (table) (optional) - optional query filter with <code>category_bits</code> and <code>mask_bits</code>

**Returns**

- `hit` (table | nil) - closest cast hit table with <code>node_visits</code> and <code>leaf_visits</code>, or <code>nil</code> on miss

### b2d.world.cast_shape
*Type:* FUNCTION
Uses Box2D v2 time-of-impact for fixture child shapes that support distance proxies.
Grid fixture children are skipped.

**Parameters**

- `world` (b2World) - world from <code>b2d.get_world</code> or <code>b2d.body.get_world</code>
- `shape` (table) - shape table using the same format as the <code>shape</code> field in <code>b2d.body.create_fixture</code>
- `translation` (vector3) - world shape translation
- `filter` (table) - optional query filter with <code>category_bits</code>, <code>mask_bits</code>, and optional <code>group_index</code>
- `max_results` (number) - optional maximum result count

**Returns**

- `hits` (table) - array of hit tables with <code>fixture</code>, <code>shape</code>, <code>point</code>, <code>normal</code>, and <code>fraction</code>
- `stats` (table) - table with <code>node_visits</code> and <code>leaf_visits</code>

### b2d.world.cast_shape
*Type:* FUNCTION
The shape table uses the same circle, capsule, segment, polygon, and box formats
as b2d.body.create_shape. The translation is the shape displacement.

**Parameters**

- `world` (b2World) - world
- `shape` (table) - shape table
- `translation` (vector3) - shape displacement
- `filter` (table) (optional) - optional query filter with <code>category_bits</code> and <code>mask_bits</code>
- `max_results` (number) (optional) - optional maximum result count. Omit or pass 0 for unlimited results.

**Returns**

- `hits` (table) - array of cast hit tables
- `stats` (table) - tree stats table

### b2d.world.collide_mover
*Type:* FUNCTION
The capsule table has center1, center2, and radius fields. Plane result
tables include shape, normal, offset, and hit.

**Parameters**

- `world` (b2World) - world
- `capsule` (table) - capsule table with <code>center1</code>, <code>center2</code>, and <code>radius</code>
- `filter` (table) (optional) - optional query filter with <code>category_bits</code> and <code>mask_bits</code>
- `max_results` (number) (optional) - optional maximum result count. Omit or pass 0 for unlimited results.

**Returns**

- `planes` (table) - array of plane result tables

### b2d.world.enable_continuous
*Type:* FUNCTION
Enable or disable continuous collision.

**Parameters**

- `world` (b2World) - world
- `enable` (boolean) - true to enable continuous collision

### b2d.world.enable_sleeping
*Type:* FUNCTION
Enable or disable world sleeping.

**Parameters**

- `world` (b2World) - world
- `enable` (boolean) - true to allow sleeping

### b2d.world.enable_speculative
*Type:* FUNCTION
Enable or disable speculative collision.

**Parameters**

- `world` (b2World) - world
- `enable` (boolean) - true to enable speculative collision

### b2d.world.enable_warm_starting
*Type:* FUNCTION
Enable or disable warm starting.

**Parameters**

- `world` (b2World) - world
- `enable` (boolean) - true to enable warm starting

### b2d.world.explode
*Type:* FUNCTION
The definition table requires position, radius, falloff, and
impulse_per_length. It may also include mask_bits.

**Parameters**

- `world` (b2World) - world
- `definition` (table) - explosion definition

### b2d.world.get_awake_body_count
*Type:* FUNCTION
Get the number of awake bodies.

**Parameters**

- `world` (b2World) - world

**Returns**

- `count` (number) - awake body count

### b2d.world.get_counters
*Type:* FUNCTION
The returned table contains body_count, shape_count, contact_count,
joint_count, island_count, stack_used, static_tree_height,
tree_height, byte_count, task_count, and color_counts.

**Parameters**

- `world` (b2World) - world

**Returns**

- `counters` (table) - world counters

### b2d.world.get_gravity
*Type:* FUNCTION
Get world gravity.

**Parameters**

- `world` (b2World) - world

**Returns**

- `gravity` (vector3) - gravity vector

### b2d.world.get_hit_event_threshold
*Type:* FUNCTION
Get the hit event threshold.

**Parameters**

- `world` (b2World) - world

**Returns**

- `threshold` (number) - hit event threshold in project units per second

### b2d.world.get_maximum_linear_speed
*Type:* FUNCTION
Get the maximum linear speed.

**Parameters**

- `world` (b2World) - world

**Returns**

- `speed` (number) - maximum linear speed in project units per second

### b2d.world.get_profile
*Type:* FUNCTION
The returned table contains Box2D timing fields including step, pairs,
collide, solve, merge_islands, prepare_stages, solve_constraints,
prepare_constraints, integrate_velocities, warm_start,
solve_impulses, integrate_positions, relax_impulses,
apply_restitution, store_impulses, split_islands, transforms,
hit_events, refit, bullets, sleep_islands, and sensors.

**Parameters**

- `world` (b2World) - world

**Returns**

- `profile` (table) - world profiling data

### b2d.world.get_restitution_threshold
*Type:* FUNCTION
Get the restitution threshold.

**Parameters**

- `world` (b2World) - world

**Returns**

- `threshold` (number) - restitution threshold in project units per second

### b2d.world.is_continuous_enabled
*Type:* FUNCTION
Get whether continuous collision is enabled.

**Parameters**

- `world` (b2World) - world

**Returns**

- `enabled` (boolean) - true if continuous collision is enabled

### b2d.world.is_locked
*Type:* FUNCTION
The world is locked during callbacks and some simulation phases. Functions
marked as locked during callbacks cannot be called while this returns true.

**Parameters**

- `world` (b2World) - world

**Returns**

- `locked` (boolean) - true if the world is locked

### b2d.world.is_sleeping_enabled
*Type:* FUNCTION
Get whether world sleeping is enabled.

**Parameters**

- `world` (b2World) - world

**Returns**

- `enabled` (boolean) - true if sleeping is enabled

### b2d.world.is_valid
*Type:* FUNCTION
Check whether a world handle is valid.

**Parameters**

- `world` (b2World) - world

**Returns**

- `valid` (boolean) - true if the world handle is valid

### b2d.world.is_warm_starting_enabled
*Type:* FUNCTION
Get whether warm starting is enabled.

**Parameters**

- `world` (b2World) - world

**Returns**

- `enabled` (boolean) - true if warm starting is enabled

### b2d.world.overlap_aabb
*Type:* FUNCTION
Overlap an AABB.

**Parameters**

- `world` (b2World) - world from <code>b2d.get_world</code> or <code>b2d.body.get_world</code>
- `aabb` (table) - table with <code>lower</code> and <code>upper</code> vector3 fields
- `filter` (table) - optional query filter with <code>category_bits</code>, <code>mask_bits</code>, and optional <code>group_index</code>
- `max_results` (number) - optional maximum result count

**Returns**

- `fixtures` (table) - array of fixture info tables
- `stats` (table) - table with <code>node_visits</code> and <code>leaf_visits</code>

### b2d.world.overlap_aabb
*Type:* FUNCTION
The AABB table has lower and upper vector3 fields.

**Parameters**

- `world` (b2World) - world
- `aabb` (table) - AABB table with <code>lower</code> and <code>upper</code>
- `filter` (table) (optional) - optional query filter with <code>category_bits</code> and <code>mask_bits</code>
- `max_results` (number) (optional) - optional maximum result count. Omit or pass 0 for unlimited results.

**Returns**

- `hits` (table) - array of shape info tables
- `stats` (table) - tree stats table

### b2d.world.overlap_shape
*Type:* FUNCTION
Overlap a shape.

**Parameters**

- `world` (b2World) - world from <code>b2d.get_world</code> or <code>b2d.body.get_world</code>
- `shape` (table) - shape table using the same format as the <code>shape</code> field in <code>b2d.body.create_fixture</code>
- `filter` (table) - optional query filter with <code>category_bits</code>, <code>mask_bits</code>, and optional <code>group_index</code>
- `max_results` (number) - optional maximum result count

**Returns**

- `fixtures` (table) - array of fixture info tables
- `stats` (table) - table with <code>node_visits</code> and <code>leaf_visits</code>

### b2d.world.overlap_shape
*Type:* FUNCTION
The shape table uses the same circle, capsule, segment, polygon, and box formats
as b2d.body.create_shape.

**Parameters**

- `world` (b2World) - world
- `shape` (table) - shape table
- `filter` (table) (optional) - optional query filter with <code>category_bits</code> and <code>mask_bits</code>
- `max_results` (number) (optional) - optional maximum result count. Omit or pass 0 for unlimited results.

**Returns**

- `hits` (table) - array of shape info tables
- `stats` (table) - tree stats table

### b2d.world.rebuild_static_tree
*Type:* FUNCTION
Rebuild the static broad-phase tree.

**Parameters**

- `world` (b2World) - world

### b2d.world.set_contact_tuning
*Type:* FUNCTION
Set contact solver tuning.

**Parameters**

- `world` (b2World) - world
- `hertz` (number) - contact stiffness frequency in hertz
- `damping_ratio` (number) - contact damping ratio
- `pushout` (number) - pushout velocity in project units per second

### b2d.world.set_gravity
*Type:* FUNCTION
Set world gravity.

**Parameters**

- `world` (b2World) - world
- `gravity` (vector3) - gravity vector

### b2d.world.set_hit_event_threshold
*Type:* FUNCTION
Set the hit event threshold.

**Parameters**

- `world` (b2World) - world
- `threshold` (number) - hit event threshold in project units per second

### b2d.world.set_joint_tuning
*Type:* FUNCTION
Set joint solver tuning.

**Parameters**

- `world` (b2World) - world
- `hertz` (number) - joint stiffness frequency in hertz
- `damping_ratio` (number) - joint damping ratio

### b2d.world.set_maximum_linear_speed
*Type:* FUNCTION
Set the maximum linear speed.

**Parameters**

- `world` (b2World) - world
- `speed` (number) - maximum linear speed in project units per second

### b2d.world.set_restitution_threshold
*Type:* FUNCTION
Collisions below this relative speed use inelastic collision response.

**Parameters**

- `world` (b2World) - world
- `threshold` (number) - restitution threshold in project units per second
