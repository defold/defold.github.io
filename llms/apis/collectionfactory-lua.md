# Collection factory

**Namespace:** `collectionfactory`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_collection_factory.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_collection_factory.cpp`

Functions for controlling collection factory components which are
used to dynamically spawn collections into the runtime.

## API

### collectionfactory.create
*Type:* FUNCTION
The URL identifies the collectionfactory component that should do the spawning.
Spawning is instant, but spawned game objects get their first update calls the following frame. The supplied parameters for position, rotation and scale
will be applied to the whole collection when spawned.
Script properties in the created game objects can be overridden through
a properties-parameter table. The table should contain game object ids
(hash) as keys and property tables as values to be used when initiating each
spawned game object.
See go.property for more information on script properties.
The function returns a table that contains a key for each game object
id (hash), as addressed if the collection file was top level, and the
corresponding spawned instance id (hash) as value with a unique path
prefix added to each instance.
 Calling collectionfactory.create create on a collection factory that is marked as dynamic without having loaded resources
using collectionfactory.load will synchronously load and create resources which may affect application performance.

**Parameters**

- `url` (string | hash | url) - the collection factory component to be used
- `position` (vector3) (optional) - position to assign to the newly spawned collection
- `rotation` (quaternion) (optional) - rotation to assign to the newly spawned collection
- `properties` (table<hash, table<string|hash, any>>) (optional) - table of script properties to propagate to any new game object instances
- `scale` (number | vector3) (optional) - uniform scaling to apply to the newly spawned collection (must be greater than 0).

**Returns**

- `ids` (table<hash, hash>) - a table mapping the id:s from the collection to the new instance id:s

**Examples**

How to spawn a collection of game objects:
```
function init(self)
  -- Spawn a small group of enemies.
  local pos = vmath.vector3(100, 12.5, 0)
  local rot = vmath.quat_rotation_z(math.pi / 2)
  local scale = 0.5
  local props = {}
  props[hash("/enemy_leader")] = { health = 1000.0 }
  props[hash("/enemy_1")] = { health = 200.0 }
  props[hash("/enemy_2")] = { health = 400.0, color = hash("green") }

  local self.enemy_ids = collectionfactory.create("#enemyfactory", pos, rot, props, scale)
  -- enemy_ids now map to the spawned instance ids:
  --
  -- pprint(self.enemy_ids)
  --
  -- DEBUG:SCRIPT:
  -- {
  --   hash: [/enemy_leader] = hash: [/collection0/enemy_leader],
  --   hash: [/enemy_1] = hash: [/collection0/enemy_1],
  --   hash: [/enemy_2] = hash: [/collection0/enemy_2]
  -- }

  -- Send "attack" message to the leader. First look up its instance id.
  local leader_id = self.enemy_ids[hash("/enemy_leader")]
  msg.post(leader_id, "attack")
end

```

How to delete a spawned collection:
```
go.delete(self.enemy_ids)

```

### collectionfactory.get_status
*Type:* FUNCTION
This returns status of the collection factory.
Calling this function when the factory is not marked as dynamic loading always returns COMP_COLLECTION_FACTORY_STATUS_LOADED.

**Parameters**

- `url` (string | hash | url) (optional) - the collection factory component to get status from

**Returns**

- `status` (collectionfactory.STATUS) - status of the collection factory component

### collectionfactory.load
*Type:* FUNCTION
Resources loaded are referenced by the collection factory component until the existing (parent) collection is destroyed or collectionfactory.unload is called.
Calling this function when the factory is not marked as dynamic loading does nothing.

**Parameters**

- `url` (string | hash | url) (optional) - the collection factory component to load
- `complete_function` (fun(self:script_instance, url:url, result:boolean)) (optional) - function to call when resources are loaded.
<dl>
<dt class="api-lua-v2-type-definition"><code>self:<a href="../builtins-lua/#script_instance">script_instance</a></code></dt>
<dd>The current script instance.</dd>
<dt class="api-lua-v2-type-definition"><code>url:<a href="../msg-lua/#url">url</a></code></dt>
<dd>url of the collection factory component</dd>
<dt class="api-lua-v2-type-definition"><code>result:<a href="../../../manuals/lua/#variables-and-data-types">boolean</a></code></dt>
<dd>True if resource were loaded successfully</dd>
</dl>

**Examples**

How to load resources of a collection factory prototype.
```
collectionfactory.load("#factory", function(self, url, result) end)

```

### collectionfactory.set_prototype
*Type:* FUNCTION
Changes the prototype for the collection factory.
Setting the prototype to "nil" will revert back to the original prototype.

**Notes**

- - Requires the factory to have the "Dynamic Prototype" set
  - Cannot be set when the state is COMP_FACTORY_STATUS_LOADING
  - Setting the prototype to "nil" will revert back to the original prototype.

**Parameters**

- `url` (string | hash | url) (optional) - the collection factory component
- `prototype` (string | nil) (optional) - the path to the new prototype, or <code>nil</code>

**Examples**

How to unload the previous prototypes resources, and then spawn a new collection
```
collectionfactory.unload("#factory") -- unload the previous resources
collectionfactory.set_prototype("#factory", "/main/levels/level1.collectionc")
local ids = collectionfactory.create("#factory", go.get_world_position(), vmath.quat())

```

### collectionfactory.STATUS
*Type:* ENUM
Collection factory status values

**Members**

- `collectionfactory.STATUS_LOADED` - The collection factory resources are loaded.
- `collectionfactory.STATUS_LOADING` - The collection factory resources are loading.
- `collectionfactory.STATUS_UNLOADED` - The collection factory resources are unloaded.

### collectionfactory.unload
*Type:* FUNCTION
This decreases the reference count for each resource loaded with collectionfactory.load. If reference is zero, the resource is destroyed.
Calling this function when the factory is not marked as dynamic loading does nothing.

**Parameters**

- `url` (string | hash | url) (optional) - the collection factory component to unload

**Examples**

How to unload resources of a collection factory prototype loaded with collectionfactory.load
```
collectionfactory.unload("#factory")

```
