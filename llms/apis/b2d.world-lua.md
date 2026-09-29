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
The return value is the fraction of translation that can be traveled before collision,
or 1 if there is no hit.

**Parameters**

- `world` (b2World) - world
- `capsule` (b2d.mover_capsule) - mover capsule
- `translation` (vector3) - capsule displacement
- `filter` (b2d.query_filter) (optional) - optional query filter

**Returns**

- `fraction` (number) - travel fraction before collision

### b2d.world.cast_ray
*Type:* FUNCTION
Cast a ray.

**Parameters**

- `world` (b2World) - world from <a href="/ref/b2d#b2d.get_world">b2d.get_world</a> or <a href="#b2d">b2d.body.get_world</a>
- `origin` (vector3) - world ray origin
- `translation` (vector3) - world ray translation
- `filter` (b2d.query_filter) (optional) - optional query filter
- `max_results` (integer) (optional) - optional maximum result count

**Returns**

- `hits` (b2d.fixture_cast_hit[]) - ray-cast hits
- `stats` (b2d.tree_stats) - broad-phase query statistics

### b2d.world.cast_ray
*Type:* FUNCTION
The translation is the ray displacement from origin. Result order is not
guaranteed by Box2D.

**Parameters**

- `world` (b2World) - world
- `origin` (vector3) - ray start position
- `translation` (vector3) - ray displacement
- `filter` (b2d.query_filter) (optional) - optional query filter
- `max_results` (integer) (optional) - optional maximum result count. Omit or pass 0 for unlimited results.

**Returns**

- `hits` (b2d.shape_cast_hit[]) - ray-cast hits
- `stats` (b2d.tree_stats) - broad-phase query statistics

### b2d.world.cast_ray_closest
*Type:* FUNCTION
Cast a ray and return the closest hit.

**Parameters**

- `world` (b2World) - world from <a href="/ref/b2d#b2d.get_world">b2d.get_world</a> or <a href="#b2d">b2d.body.get_world</a>
- `origin` (vector3) - world ray origin
- `translation` (vector3) - world ray translation
- `filter` (b2d.query_filter) (optional) - optional query filter

**Returns**

- `hit` (b2d.fixture_cast_hit | nil) - closest hit, or <code>nil</code>

### b2d.world.cast_ray_closest
*Type:* FUNCTION
The translation is the ray displacement from origin.

**Parameters**

- `world` (b2World) - world
- `origin` (vector3) - ray start position
- `translation` (vector3) - ray displacement
- `filter` (b2d.query_filter) (optional) - optional query filter

**Returns**

- `hit` (b2d.shape_cast_hit | nil) - closest hit, or <code>nil</code>

### b2d.world.cast_shape
*Type:* FUNCTION
Uses Box2D v2 time-of-impact for fixture child shapes that support distance proxies.
Grid fixture children are skipped.

**Parameters**

- `world` (b2World) - world from <a href="/ref/b2d#b2d.get_world">b2d.get_world</a> or <a href="#b2d">b2d.body.get_world</a>
- `shape` (b2d.shape.definition) - query shape
- `translation` (vector3) - world shape translation
- `filter` (b2d.query_filter) (optional) - optional query filter
- `max_results` (integer) (optional) - optional maximum result count

**Returns**

- `hits` (b2d.fixture_cast_hit[]) - shape-cast hits
- `stats` (b2d.tree_stats) - broad-phase query statistics

### b2d.world.cast_shape
*Type:* FUNCTION
The translation is the shape displacement.

**Parameters**

- `world` (b2World) - world
- `shape` (b2d.shape.definition) - cast shape
- `translation` (vector3) - shape displacement
- `filter` (b2d.query_filter) (optional) - optional query filter
- `max_results` (integer) (optional) - optional maximum result count. Omit or pass 0 for unlimited results.

**Returns**

- `hits` (b2d.shape_cast_hit[]) - shape-cast hits
- `stats` (b2d.tree_stats) - broad-phase query statistics

### b2d.world.collide_mover
*Type:* FUNCTION
Collide a mover capsule against the world.

**Parameters**

- `world` (b2World) - world
- `capsule` (b2d.mover_capsule) - mover capsule
- `filter` (b2d.query_filter) (optional) - optional query filter
- `max_results` (integer) (optional) - optional maximum result count. Omit or pass 0 for unlimited results.

**Returns**

- `planes` (b2d.mover_plane[]) - collision planes

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
Apply an explosion impulse.

**Parameters**

- `world` (b2World) - world
- `definition` (b2d.explosion_definition) - explosion definition

### b2d.world.get_awake_body_count
*Type:* FUNCTION
Get the number of awake bodies.

**Parameters**

- `world` (b2World) - world

**Returns**

- `count` (integer) - awake body count

### b2d.world.get_counters
*Type:* FUNCTION
Get world counters.

**Parameters**

- `world` (b2World) - world

**Returns**

- `counters` (b2d.world_counters) - world counters

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
Get world profiling data.

**Parameters**

- `world` (b2World) - world

**Returns**

- `profile` (b2d.world_profile) - world profiling data

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

- `world` (b2World) - world from <a href="/ref/b2d#b2d.get_world">b2d.get_world</a> or <a href="#b2d">b2d.body.get_world</a>
- `aabb` (b2d.aabb) - query bounds
- `filter` (b2d.query_filter) (optional) - optional query filter
- `max_results` (integer) (optional) - optional maximum result count

**Returns**

- `fixtures` (b2d.fixture_info[]) - overlapping fixtures
- `stats` (b2d.tree_stats) - broad-phase query statistics

### b2d.world.overlap_aabb
*Type:* FUNCTION
Find shapes overlapping an AABB.

**Parameters**

- `world` (b2World) - world
- `aabb` (b2d.aabb) - query bounds
- `filter` (b2d.query_filter) (optional) - optional query filter
- `max_results` (integer) (optional) - optional maximum result count. Omit or pass 0 for unlimited results.

**Returns**

- `hits` (b2d.shape_info[]) - overlapping shapes
- `stats` (b2d.tree_stats) - broad-phase query statistics

### b2d.world.overlap_shape
*Type:* FUNCTION
Overlap a shape.

**Parameters**

- `world` (b2World) - world from <a href="/ref/b2d#b2d.get_world">b2d.get_world</a> or <a href="#b2d">b2d.body.get_world</a>
- `shape` (b2d.shape.definition) - query shape
- `filter` (b2d.query_filter) (optional) - optional query filter
- `max_results` (integer) (optional) - optional maximum result count

**Returns**

- `fixtures` (b2d.fixture_info[]) - overlapping fixtures
- `stats` (b2d.tree_stats) - broad-phase query statistics

### b2d.world.overlap_shape
*Type:* FUNCTION
Find shapes overlapping a shape proxy.

**Parameters**

- `world` (b2World) - world
- `shape` (b2d.shape.definition) - query shape
- `filter` (b2d.query_filter) (optional) - optional query filter
- `max_results` (integer) (optional) - optional maximum result count. Omit or pass 0 for unlimited results.

**Returns**

- `hits` (b2d.shape_info[]) - overlapping shapes
- `stats` (b2d.tree_stats) - broad-phase query statistics

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
