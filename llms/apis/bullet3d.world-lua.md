# bullet3d.world

**Namespace:** `bullet3d.world`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_bullet3d_world.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/bullet3d/script_bullet3d_world.cpp`

Read and tune the Bullet dynamics world owned by the current collection.
Defold remains responsible for world lifetime, stepping, collision objects,
callbacks, and debug drawing.

World and collision-object values returned by this API are borrowed,
generational handles. They become invalid when their collection or owning
game object is deleted and must not be retained as native pointers.

All positions, distances, translations, dimensions and contact distances use
Defold world units. The binding converts them using `physics.scale`. Rotations
and unit normals are not scaled. Query functions refresh Bullet broadphase
AABBs before execution, so collision-object transform changes are visible.

Query filters are optional tables with these fields:

`category_bits`
: [type:integer] unsigned 16-bit category bits, default `65535`

`mask_bits`
: [type:integer] unsigned 16-bit mask bits, default `65535`

`include_triggers`
: [type:boolean] include objects without contact response, default `true`

`ignore`
: [type:btCollisionObject|btCollisionObject[]] one collision-object handle or an array of handles to exclude

`report_initial_overlaps`
: [type:boolean] report shapes overlapping the cast origin as synthesized fraction-zero hits, default `false`

`report_initial_overlaps` is a `bullet3d.world` query option only. It does
not change `physics.raycast()` or either Box2D backend.

Category and mask checks are reciprocal: the query category must match the
object's mask and the object's category must match the query mask.

Temporary query shapes use the same geometry fields as
[ref:bullet3d.shape.get_shape]:
a sphere has `type` and `diameter`, a box has `type` and `dimensions`, a
Y-axis capsule has `type`, `diameter` and `height`, and a convex hull has
`type` and a `vertices` array with at least four `vector3` values. The `type`
is one of the `bullet3d.shape.SHAPE_TYPE_*` constants. Every shape can specify
`position` and `rotation`; their defaults are zero and the identity rotation.
Cast shapes can also specify `target_rotation`, which defaults to `rotation`.
Capsule `height` is the length of the cylindrical middle section; total
end-to-end height is `height + diameter`. Query sizes are always expressed
in Defold world units. Except for triangle meshes, a table returned by
`bullet3d.shape.get_shape` can be reused directly after adding the desired
query transform fields. Queries accept only sphere, box, capsule, and hull.
Hull vertices describe a convex hull; concave input is convexified by Bullet.
All query vectors and scalar sizes must be finite. Diameters, dimensions and
capsule heights must be greater than zero; hulls require at least four finite
vertices. Cast translations must be finite and non-zero. Query rotations
must be finite, non-zero quaternions and are normalized by the binding. AABB
lower bounds must not exceed their corresponding upper bounds.

Overlap and enumeration results are arrays of `btCollisionObject` handles.
Cast results are tables containing `object`, `point`, `normal`, `fraction`,
`initial_overlap`, and `inside`. `shape_index` is present when Bullet reports
a compound child and is one-based. Cast arrays are sorted by ascending
fraction. `fraction` is in `[0, 1]` along the supplied translation. For native
hits, `normal` is the hit object's outward unit surface normal; synthesized
initial-overlap hits use a zero normal. `inside` is true for a synthesized
ray-origin hit when Bullet reports signed contact distance less than or equal
to zero. It denotes initial contact or penetration rather than strict
geometric containment, and exact-surface cases follow Bullet's contact
tolerance. Shape-cast initial overlaps set only `initial_overlap`.

Contact results contain `object_a`, `object_b`, `position_a`, `position_b`,
`normal_on_b`, and signed `distance`. Positions are points on their named
objects, and `normal_on_b` points from object B toward object A. A negative
distance is penetration and a small positive distance is Bullet's contact
margin. Object order is always normalized to the order supplied by the caller.

`max_results` is optional. Zero or omission means unlimited results. A
negative value is an error. Broadphase overlaps, native world enumeration,
contacts, and equal-fraction cast hits have unspecified order. A capped query
can therefore return a different equal-priority subset after world changes.
Synchronous queries execute immediately and do not advance simulation.
Async casts are deferred until after the next physics step. They execute on
the main thread rather than a worker thread, and all queued casts for one
world share one broadphase AABB refresh. Every cast in the batch completes
before any callback runs, so callback mutations cannot affect other query
computations in that batch. Deferral avoids blocking the Lua call site but
does not remove the cast work from the frame.
Native fraction-zero cast callbacks are suppressed. Starting overlaps are
omitted by default, or reported through the exact, deduplicated synthesis
enabled by `report_initial_overlaps`; this avoids direction-dependent Bullet
results for casts that start touching or penetrating another object.

## API

### bullet3d.world.aabb
*Type:* STRUCT
Bullet world axis-aligned bounding box

**Members**

- `lower` (vector3) - lower world-space bound in Defold units
- `upper` (vector3) - upper world-space bound in Defold units

### bullet3d.world.cast_ray
*Type:* FUNCTION
Casts immediately from origin to origin + translation and returns all
matching hits sorted by fraction. Translation must be non-zero.
Bullet's convex ray test normally does not report a ray whose start and end are both inside
the same convex hull. Set filter.report_initial_overlaps = true to perform
an exact point-overlap test at the origin and synthesize one deduplicated hit
per initially touching or overlapping object with fraction = 0, zero normal,
point = origin, initial_overlap = true, and inside = true. The point is
the query origin, not a surface contact. This explicitly supports the
inside-hull behavior requested by issue #5348. Fraction-zero native callbacks
and starting overlaps are suppressed when the option is false.

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle
- `origin` (vector3) - ray origin in world space
- `translation` (vector3) - non-zero ray displacement in world units
- `filter` (bullet3d.world.query_filter) (optional) - query filter
- `max_results` (integer) (optional) - maximum sorted hits, or zero for all

**Returns**

- `hits` (bullet3d.world.cast_result[]) - cast results sorted by ascending fraction

### bullet3d.world.cast_ray_async
*Type:* FUNCTION
Queues the same ray query as bullet3d.world.cast_ray and returns without
executing it. After the next physics step, callback(self, hits) receives the
cast-result array sorted by fraction. The query observes post-step world state.
It is deferred on the main thread, not executed concurrently; use it to move
work out of the current Lua call and to query the stepped state, not as a
guarantee of lower total CPU time. Queued casts for the same world share one
broadphase AABB refresh and all finish before their callbacks begin.

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle
- `origin` (vector3) - ray origin in world space
- `translation` (vector3) - non-zero ray displacement in world units
- `callback` (fun(self:script_instance, hits:bullet3d.world.cast_result[])) - function called as <code>callback(self, hits)</code>
- `filter` (bullet3d.world.query_filter) (optional) - query filter
- `max_results` (integer) (optional) - maximum sorted hits, or zero for all

**Examples**

Queue a downward cast and inspect only the closest non-trigger hit:
```
bullet3d.world.cast_ray_async(
    bullet3d.get_world(),
    go.get_world_position(),
    vmath.vector3(0, -100, 0),
    function(self, hits)
        if hits[1] then
            print("hit", hits[1].object)
        end
    end,
    { include_triggers = false },
    1)

```

### bullet3d.world.cast_ray_closest
*Type:* FUNCTION
Equivalent to bullet3d.world.cast_ray with one result, but returns the
hit table directly or nil on a miss.

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle
- `origin` (vector3) - ray origin in world space
- `translation` (vector3) - non-zero ray displacement in world units
- `filter` (bullet3d.world.query_filter) (optional) - query filter

**Returns**

- `hit` (bullet3d.world.cast_result | nil) - closest cast result, or <code>nil</code> on a miss

**Examples**

Cast downward and report the closest non-trigger hit:
```
function init(self)
    local world = bullet3d.get_world()
    local origin = go.get_world_position()
    local translation = vmath.vector3(0, -100, 0)
    local filter = { include_triggers = false }

    local hit = bullet3d.world.cast_ray_closest(
        world, origin, translation, filter)
    if hit then
        local distance = vmath.length(translation) * hit.fraction
        print("hit", hit.object, "after", distance, "units")
    end
end

```

### bullet3d.world.cast_result
*Type:* STRUCT
Bullet world cast result

**Members**

- `object` (btCollisionObject) - hit collision object
- `point` (vector3) - hit point in world space and Defold units
- `normal` (vector3) - outward unit surface normal
- `fraction` (number) - fraction along the supplied translation in <code>[0, 1]</code>
- `shape_index?` (integer) - one-based compound child index
- `initial_overlap` (boolean) - whether the hit was synthesized from an initial overlap
- `inside` (boolean) - whether a synthesized ray-origin hit starts inside the object

### bullet3d.world.cast_shape
*Type:* FUNCTION
Sweeps the temporary shape from shape.position by translation, while
interpolating from shape.rotation to shape.target_rotation. Translation
must be non-zero. The query executes immediately and returns all matching hits
sorted by fraction. Bullet's convex sweep supports only convex query shapes.
When filter.report_initial_overlaps is true, an exact contact test at the
starting transform synthesizes one deduplicated hit per overlapping object
with fraction = 0, point = shape.position, zero normal,
initial_overlap = true, and inside = false. The point is the query-shape
origin, not a surface contact, and the result does not report penetration depth.

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle
- `shape` (bullet3d.shape.definition) - convex query shape with optional target rotation
- `translation` (vector3) - non-zero sweep displacement in world units
- `filter` (bullet3d.world.query_filter) (optional) - query filter
- `max_results` (integer) (optional) - maximum sorted hits, or zero for all

**Returns**

- `hits` (bullet3d.world.cast_result[]) - cast results sorted by ascending fraction

### bullet3d.world.cast_shape_async
*Type:* FUNCTION
Queues the same convex sweep as bullet3d.world.cast_shape and returns
without executing it. After the next physics step, callback(self, hits)
receives the sorted cast-result array from the post-step world state. The
operation is deferred on the main thread rather than run concurrently. All
queued casts for one world share one broadphase AABB refresh and all finish
before their callbacks begin.

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle
- `shape` (bullet3d.shape.definition) - convex query shape with optional target rotation
- `translation` (vector3) - non-zero sweep displacement in world units
- `callback` (fun(self:script_instance, hits:bullet3d.world.cast_result[])) - function called as <code>callback(self, hits)</code>
- `filter` (bullet3d.world.query_filter) (optional) - query filter
- `max_results` (integer) (optional) - maximum sorted hits, or zero for all

### bullet3d.world.cast_shape_closest
*Type:* FUNCTION
Equivalent to bullet3d.world.cast_shape with one result, but returns
the hit table directly or nil on a miss.

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle
- `shape` (bullet3d.shape.definition) - convex query shape with optional target rotation
- `translation` (vector3) - non-zero sweep displacement in world units
- `filter` (bullet3d.world.query_filter) (optional) - query filter

**Returns**

- `hit` (bullet3d.world.cast_result | nil) - closest cast result, or <code>nil</code> on a miss

### bullet3d.world.contact_pair_test
*Type:* FUNCTION
Runs Bullet's discrete pair contact algorithm without changing the simulation.
Both borrowed handles must belong to world and must identify different
objects. The output preserves the caller's A/B order even when Bullet's
internal manifold order is reversed. Collision filters are not applied to an
explicitly selected pair.

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle
- `object_a` (btCollisionObject) - first collision object in the world
- `object_b` (btCollisionObject) - different second collision object in the world
- `max_results` (integer) (optional) - maximum number of contact points, or zero for all

**Returns**

- `contacts` (bullet3d.world.contact_result[]) - normalized contact results

### bullet3d.world.contact_result
*Type:* STRUCT
Bullet world contact result

**Members**

- `object_a` (btCollisionObject) - first collision object
- `object_b` (btCollisionObject) - second collision object
- `position_a` (vector3) - contact point on object A in world space and Defold units
- `position_b` (vector3) - contact point on object B in world space and Defold units
- `normal_on_b` (vector3) - unit normal pointing from object B toward object A
- `distance` (number) - signed contact distance in Defold units

### bullet3d.world.contact_test
*Type:* FUNCTION
Runs Bullet's discrete contact test between object and matching objects in
the same world. The supplied object is always object_a in returned contacts.
The borrowed collision-object handle must belong to world. Bullet may return
several contact points for one object pair and may include small positive
contact-margin distances.

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle
- `object` (btCollisionObject) - collision object belonging to the world
- `filter` (bullet3d.world.query_filter) (optional) - filter applied to candidate <code>object_b</code> values
- `max_results` (integer) (optional) - maximum number of contact points, or zero for all

**Returns**

- `contacts` (bullet3d.world.contact_result[]) - normalized contact results

**Examples**

Inspect current contacts for this collision object:
```
function update(self, dt)
    local world = bullet3d.get_world()
    local object = bullet3d.get_collision_object("#collisionobject")
    local filter = { include_triggers = false }
    local contacts = bullet3d.world.contact_test(world, object, filter)

    for _, contact in ipairs(contacts) do
        if contact.distance < 0 then
            print("penetration", -contact.distance, "against", contact.object_b)
        end
    end
end

```

### bullet3d.world.get_collision_object_count
*Type:* FUNCTION
Get the number of collision objects in the world

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle

**Returns**

- `count` (integer) - number of collision objects

### bullet3d.world.get_collision_objects
*Type:* FUNCTION
Returns the Defold-owned collision objects currently registered in the world.
Internal or unmanaged Bullet objects without Defold ownership metadata are
not exposed.

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle
- `max_results` (integer) (optional) - maximum number of results, or zero for all

**Returns**

- `objects` (btCollisionObject[]) - array of collision-object handles

### bullet3d.world.get_gravity
*Type:* FUNCTION
Get world gravity

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle

**Returns**

- `gravity` (vector3) - gravity in Defold units per second squared

### bullet3d.world.is_valid
*Type:* FUNCTION
Test whether a world handle is valid

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle

**Returns**

- `valid` (boolean) - <code>true</code> if the native world still exists

### bullet3d.world.overlap_aabb
*Type:* FUNCTION
Finds collision objects whose Bullet broadphase bounds overlap the supplied
world-space AABB. This is intentionally a broadphase query and can include
objects whose actual collision geometry does not intersect the box. Use
bullet3d.world.overlap_point or
bullet3d.world.overlap_shape for exact narrow-phase overlap tests.

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle
- `aabb` (bullet3d.world.aabb) - world-space bounds
- `filter` (bullet3d.world.query_filter) (optional) - query filter
- `max_results` (integer) (optional) - maximum number of results, or zero for all

**Returns**

- `objects` (btCollisionObject[]) - array of overlapping collision-object handles

### bullet3d.world.overlap_point
*Type:* FUNCTION
Performs an exact narrow-phase test using a temporary zero-radius Bullet
sphere at the world-space point. A result is returned only for a contact with
signed distance less than or equal to zero, so broadphase-only false positives
are removed. Results on an exact surface follow Bullet's contact tolerance.

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle
- `point` (vector3) - point in world space
- `filter` (bullet3d.world.query_filter) (optional) - query filter
- `max_results` (integer) (optional) - maximum number of results, or zero for all

**Returns**

- `objects` (btCollisionObject[]) - array of overlapping collision-object handles

### bullet3d.world.overlap_shape
*Type:* FUNCTION
Performs an exact Bullet contact test for a temporary sphere, box, Y-axis
capsule, or convex hull. Multiple native contact points for the same target
object are deduplicated in the returned overlap array.

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle
- `shape` (bullet3d.shape.definition) - convex query shape
- `filter` (bullet3d.world.query_filter) (optional) - query filter
- `max_results` (integer) (optional) - maximum number of results, or zero for all

**Returns**

- `objects` (btCollisionObject[]) - array of overlapping collision-object handles

**Examples**

Find non-trigger objects overlapping a two-unit sphere around this game object:
```
function init(self)
    local world = bullet3d.get_world()
    local shape = {
        type = bullet3d.shape.SHAPE_TYPE_SPHERE,
        diameter = 2,
        position = go.get_world_position(),
    }
    local filter = { include_triggers = false }
    local overlaps = bullet3d.world.overlap_shape(world, shape, filter)

    for _, object in ipairs(overlaps) do
        print("overlap", object)
    end
end

```

### bullet3d.world.query_filter
*Type:* STRUCT
Bullet world query filter

**Members**

- `category_bits?` (integer) - unsigned 16-bit category bits; defaults to <code>65535</code>
- `mask_bits?` (integer) - unsigned 16-bit mask bits; defaults to <code>65535</code>
- `include_triggers?` (boolean) - whether to include objects without contact response; defaults to <code>true</code>
- `ignore?` (btCollisionObject|btCollisionObject[]) - one collision object or an array of collision objects to exclude
- `report_initial_overlaps?` (boolean) - whether casts synthesize fraction-zero hits for initial overlaps; defaults to <code>false</code>

### bullet3d.world.set_gravity
*Type:* FUNCTION
Bullet propagates the new value to active dynamic bodies unless they have
bullet3d.rigid_body.BT_DISABLE_WORLD_GRAVITY set. Such bodies retain their
custom body gravity.

**Parameters**

- `world` (btDiscreteDynamicsWorld) - world handle
- `gravity` (vector3) - finite gravity in Defold units per second squared

**Examples**

Set gravity for the current collection's physics world:
```
function init(self)
    local world = bullet3d.get_world()
    if world then
        bullet3d.world.set_gravity(world, vmath.vector3(0, -9.81, 0))
    end
end

```
