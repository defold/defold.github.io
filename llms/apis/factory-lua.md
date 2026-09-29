# Factory

**Namespace:** `factory`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_factory.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_factory.cpp`

Functions for controlling factory components which are used to
dynamically spawn game objects into the runtime.

## API

### factory.create
*Type:* FUNCTION
The URL identifies which factory should create the game object.
If the game object is created inside of the frame (e.g. from an update callback), the game object will be created instantly, but none of its component will be updated in the same frame.
Properties defined in scripts in the created game object can be overridden through the properties-parameter below.
See go.property for more information on script properties.
 Calling factory.create on a factory that is marked as dynamic without having loaded resources
using factory.load will synchronously load and create resources which may affect application performance.

**Parameters**

- `url` (string | hash | url) - the factory that should create a game object.
- `position` (vector3) (optional) - the position of the new game object, the position of the game object calling <code>factory.create()</code> is used by default, or if the value is <code>nil</code>.
- `rotation` (quaternion) (optional) - the rotation of the new game object, the rotation of the game object calling <code>factory.create()</code> is used by default, or if the value is <code>nil</code>.
- `properties` (table<string|hash, any>) (optional) - the properties defined in a script attached to the new game object.
- `scale` (number | vector3) (optional) - the scale of the new game object (must be greater than 0), the scale of the game object containing the factory is used by default, or if the value is <code>nil</code>

**Returns**

- `id` (hash) - the global id of the spawned game object

**Examples**

How to create a new game object:
```
function init(self)
    -- create a new game object and provide property values
    self.my_created_object = factory.create("#factory", nil, nil, {my_value = 1})
    -- communicate with the object
    msg.post(self.my_created_object, "hello")
end

```

And then let the new game object have a script attached:
```
go.property("my_value", 0)

function init(self)
    -- do something with self.my_value which is now one
end

```

### factory.get_status
*Type:* FUNCTION
This returns status of the factory.
Calling this function when the factory is not marked as dynamic loading always returns
factory.STATUS_LOADED.

**Parameters**

- `url` (string | hash | url) (optional) - the factory component to get status from

**Returns**

- `status` (factory.STATUS) - status of the factory component

### factory.load
*Type:* FUNCTION
Resources are referenced by the factory component until the existing (parent) collection is destroyed or factory.unload is called.
Calling this function when the factory is not marked as dynamic loading does nothing.

**Parameters**

- `url` (string | hash | url) (optional) - the factory component to load
- `complete_function` (fun(self:script_instance, url:url, result:boolean)) (optional) - function to call when resources are loaded.
<dl>
<dt class="api-lua-v2-type-definition"><code>self:<a href="../builtins-lua/#script_instance">script_instance</a></code></dt>
<dd>The current script instance.</dd>
<dt class="api-lua-v2-type-definition"><code>url:<a href="../msg-lua/#url">url</a></code></dt>
<dd>url of the factory component</dd>
<dt class="api-lua-v2-type-definition"><code>result:<a href="../../../manuals/lua/#variables-and-data-types">boolean</a></code></dt>
<dd>True if resources were loaded successfully</dd>
</dl>

**Examples**

How to load resources of a factory prototype.
```
factory.load("#factory", function(self, url, result) end)

```

### factory.set_prototype
*Type:* FUNCTION
Changes the prototype for the factory.

**Notes**

- - Requires the factory to have the "Dynamic Prototype" set
  - Cannot be set when the state is COMP_FACTORY_STATUS_LOADING
  - Setting the prototype to `nil` will revert back to the original prototype.

**Parameters**

- `url` (string | hash | url) (optional) - the factory component
- `prototype` (string | nil) (optional) - the path to the new prototype, or <code>nil</code>

**Examples**

How to unload the previous prototypes resources, and then spawn a new game object
```
factory.unload("#factory") -- unload the previous resources
factory.set_prototype("#factory", "/main/levels/enemyA.goc")
local id = factory.create("#factory", go.get_world_position(), vmath.quat())

```

### factory.STATUS
*Type:* ENUM
Factory status values

**Members**

- `factory.STATUS_LOADED` - The factory resources are loaded.
- `factory.STATUS_LOADING` - The factory resources are loading.
- `factory.STATUS_UNLOADED` - The factory resources are unloaded.

### factory.unload
*Type:* FUNCTION
This decreases the reference count for each resource loaded with factory.load. If reference is zero, the resource is destroyed.
Calling this function when the factory is not marked as dynamic loading does nothing.

**Parameters**

- `url` (string | hash | url) (optional) - the factory component to unload

**Examples**

How to unload resources of a factory prototype loaded with factory.load
```
factory.unload("#factory")

```
