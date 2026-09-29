# Game object

**Namespace:** `go`
**Language:** Lua
**Type:** Defold Lua
**File:** `gameobject_ddf.proto`
**Source:** `engine/gameobject/proto/gameobject/gameobject_ddf.proto`

Game object API documentation

## API

### acquire_input_focus
*Type:* MESSAGE
Post this message to a game object instance to make that instance acquire the user input focus.
User input is distributed by the engine to every instance that has
requested it. The last instance to request focus will receive it first.
This means that the scripts in the instance will have first-hand-chance
at reacting on user input, possibly consuming it (by returning
true from on_input) so that no other instances
can react on it. The most common case is for a script to send this message
to itself when it needs to respond to user input.
A script belonging to an instance which has the user input focus will
receive the input actions in its on_input callback function.
See on_input for more information on how user input can be
handled.

**Examples**

This example demonstrates how to acquire and act on user input.
```
function init(self)
    -- acquire input focus as soon as the instance has been initialized
    msg.post(".", "acquire_input_focus")
end

function on_input(self, action_id, action)
    -- check which input we received
    if action_id == hash("my_action") then
        -- act on the input
        self.my_action_amount = action.value
    end
end

```

### disable
*Type:* MESSAGE
This message disables the receiving component. All components are enabled by default, which means they will receive input, updates
and be a part of the simulation. A component is disabled when it receives the disable message.
 Components that currently supports this message are:

Camera
Collection Proxy
Collision Object
Gui
Label
Spine Model
Sprite
Tile Grid
Model
Mesh

**Examples**

Disable the component "my_component":
```
msg.post("#my_component", "disable")

```

### enable
*Type:* MESSAGE
This message enables the receiving component. All components are enabled by default, which means they will receive input, updates
and be a part of the simulation. A component is disabled when it receives the disable message.
 Components that currently supports this message are:

Camera
Collection Proxy
Collision Object
Gui
Label
Spine Model
Sprite
Tile Grid
Model
Mesh

**Examples**

Enable the component "my_component":
```
msg.post("#my_component", "enable")

```

### euler
*Type:* PROPERTY
The rotation of the game object expressed in Euler angles.
Euler angles are specified in degrees in the interval (-360, 360).
The type of the property is vector3.

**Examples**

How to set a game object's rotation with euler angles, either as a vector3 or selecting a specific dimension:
```
function init(self)
  -- set "player" euler z rotation component to 45 degrees around z.
  local rotz = 45
  go.set("player", "euler.z", rotz)
  local rot = go.get("player", "euler")
  -- do something useful
  assert(rot.z == rotz)
end

```

### final
*Type:* FUNCTION
This is a callback-function, which is called by the engine when a script component is finalized (destroyed). It can
be used to e.g. take some last action, report the finalization to other game object instances, delete spawned objects
or release user input focus (see release_input_focus).

**Parameters**

- `self` (script_instance) - script instance used for storing state

**Examples**

```
function final(self)
    -- report finalization
    msg.post("my_friend_instance", "im_dead", {my_stats = self.some_value})
end

```

### fixed_update
*Type:* FUNCTION
This is a callback-function, which is called by the engine at fixed intervals to update the state of a script
component. The function will be called if 'Fixed Update Frequency' is enabled in the Engine section of game.project.
It can for instance be used to update game logic with the physics simulation if using a fixed timestep for the
physics (enabled by ticking 'Use Fixed Timestep' in the Physics section of game.project).

**Parameters**

- `self` (script_instance) - script instance used for storing state
- `dt` (number) - the time-step of the frame update

### go.animate
*Type:* FUNCTION
This is only supported for numerical properties. If the node property is already being
animated, that animation will be canceled and replaced by the new one.
If a complete_function (lua function) is specified, that function will be called when the animation has completed.
By starting a new animation in that function, several animations can be sequenced together. See the examples for more information.
 If you call go.animate() from a game object's final() function,
any passed complete_function will be ignored and never called upon animation completion.
See the properties guide for which properties can be animated and the animation guide for how
them.

**Parameters**

- `url` (string | hash | url) - url of the game object or component having the property
- `property` (string | hash) - id of the property to animate
- `playback` (go.PLAYBACK) - playback mode of the animation
<ul>
<li><code>go.PLAYBACK_ONCE_FORWARD</code></li>
<li><code>go.PLAYBACK_ONCE_BACKWARD</code></li>
<li><code>go.PLAYBACK_ONCE_PINGPONG</code></li>
<li><code>go.PLAYBACK_LOOP_FORWARD</code></li>
<li><code>go.PLAYBACK_LOOP_BACKWARD</code></li>
<li><code>go.PLAYBACK_LOOP_PINGPONG</code></li>
</ul>
- `to` (number | vector3 | vector4 | quaternion) - target property value
- `easing` (vector | go.EASING) - easing to use during animation. Either specify a constant, see the <a href="/manuals/animation#_easing">animation guide</a> for a complete list, or a vmath.vector with a curve
- `duration` (number) - duration of the animation in seconds
- `delay` (number) (optional) - delay before the animation starts in seconds
- `complete_function` (fun(self:script_instance, url:url, property:hash)) (optional) - optional function to call when the animation has completed
<dl>
<dt class="api-lua-v2-type-definition"><code>self:<a href="../builtins-lua/#script_instance">script_instance</a></code></dt>
<dd>The current script instance.</dd>
<dt class="api-lua-v2-type-definition"><code>url:<a href="../msg-lua/#url">url</a></code></dt>
<dd>The game object or component instance for which the property is animated.</dd>
<dt class="api-lua-v2-type-definition"><code>property:<a href="../builtins-lua/#hash">hash</a></code></dt>
<dd>The id of the animated property.</dd>
</dl>

**Examples**

Animate the position of a game object to x = 10 during 1 second, then y = 20 during 1 second:
```
local function x_done(self, url, property)
    go.animate(go.get_id(), "position.y", go.PLAYBACK_ONCE_FORWARD, 20, go.EASING_LINEAR, 1)
end

function init(self)
    go.animate(go.get_id(), "position.x", go.PLAYBACK_ONCE_FORWARD, 10, go.EASING_LINEAR, 1, 0, x_done)
end

```

Animate the y position of a game object using a crazy custom easing curve:
```
local values = { 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 1, 1, 1, 1,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 1, 1, 1, 1,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 1, 1, 1, 1,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 1, 1, 1, 1, 1, 1, 1, 1 }
local vec = vmath.vector(values)
go.animate("go", "position.y", go.PLAYBACK_LOOP_PINGPONG, 100, vec, 2.0)

```

### go.cancel_animations
*Type:* FUNCTION
By calling this function, all or specified stored property animations of the game object or component will be canceled.
See the properties guide for which properties can be animated and the animation guide for how to animate them.

**Parameters**

- `url` (string | hash | url) - url of the game object or component
- `property` (string | hash) (optional) - optional id of the property to cancel

**Examples**

Cancel the animation of the position of a game object:
```
go.cancel_animations(go.get_id(), "position")

```

Cancel all property animations of the current game object:
```
go.cancel_animations(".")

```

Cancel all property animations of the sprite component of the current game object:
```
go.cancel_animations("#sprite")

```

### go.delete
*Type:* FUNCTION
Delete one or more game objects identified by id. Deletion is asynchronous meaning that
the game object(s) are scheduled for deletion which will happen at the end of the current
frame. Note that game objects scheduled for deletion will be counted against
max_instances in "game.project" until they are actually removed.
 Deleting a game object containing a particle FX component emitting particles will not immediately stop the particle FX from emitting particles. You need to manually stop the particle FX using particlefx.stop().
 Deleting a game object containing a sound component that is playing will not immediately stop the sound from playing. You need to manually stop the sound using sound.stop().

**Parameters**

- `id` (string | hash | url | (string|hash|url)[]) (optional) - optional id or table of id's of the instance(s) to delete, the instance of the calling script is deleted by default
- `recursive` (boolean) (optional) - optional boolean, set to true to recursively delete child hiearchy in child to parent order

**Examples**

This example demonstrates how to delete game objects
```
-- Delete the script game object
go.delete()
-- Delete a game object with the id "my_game_object".
local id = go.get_id("my_game_object") -- retrieve the id of the game object to be deleted
go.delete(id)
-- Delete a list of game objects.
local ids = { hash("/my_object_1"), hash("/my_object_2"), hash("/my_object_3") }
go.delete(ids)

```

This example demonstrates how to delete a game objects and their children (child to parent order)
```
-- Delete the script game object and it's children
go.delete(true)
-- Delete a game object with the id "my_game_object" and it's children.
local id = go.get_id("my_game_object") -- retrieve the id of the game object to be deleted
go.delete(id, true)
-- Delete a list of game objects and their children.
local ids = { hash("/my_object_1"), hash("/my_object_2"), hash("/my_object_3") }
go.delete(ids, true)

```

### go.EASING
*Type:* ENUM
Easing curves

**Members**

- `go.EASING_INBACK` - in-back
- `go.EASING_INBOUNCE` - in-bounce
- `go.EASING_INCIRC` - in-circlic
- `go.EASING_INCUBIC` - in-cubic
- `go.EASING_INELASTIC` - in-elastic
- `go.EASING_INEXPO` - in-exponential
- `go.EASING_INOUTBACK` - in-out-back
- `go.EASING_INOUTBOUNCE` - in-out-bounce
- `go.EASING_INOUTCIRC` - in-out-circlic
- `go.EASING_INOUTCUBIC` - in-out-cubic
- `go.EASING_INOUTELASTIC` - in-out-elastic
- `go.EASING_INOUTEXPO` - in-out-exponential
- `go.EASING_INOUTQUAD` - in-out-quadratic
- `go.EASING_INOUTQUART` - in-out-quartic
- `go.EASING_INOUTQUINT` - in-out-quintic
- `go.EASING_INOUTSINE` - in-out-sine
- `go.EASING_INQUAD` - in-quadratic
- `go.EASING_INQUART` - in-quartic
- `go.EASING_INQUINT` - in-quintic
- `go.EASING_INSINE` - in-sine
- `go.EASING_LINEAR` - linear interpolation
- `go.EASING_OUTBACK` - out-back
- `go.EASING_OUTBOUNCE` - out-bounce
- `go.EASING_OUTCIRC` - out-circlic
- `go.EASING_OUTCUBIC` - out-cubic
- `go.EASING_OUTELASTIC` - out-elastic
- `go.EASING_OUTEXPO` - out-exponential
- `go.EASING_OUTINBACK` - out-in-back
- `go.EASING_OUTINBOUNCE` - out-in-bounce
- `go.EASING_OUTINCIRC` - out-in-circlic
- `go.EASING_OUTINCUBIC` - out-in-cubic
- `go.EASING_OUTINELASTIC` - out-in-elastic
- `go.EASING_OUTINEXPO` - out-in-exponential
- `go.EASING_OUTINQUAD` - out-in-quadratic
- `go.EASING_OUTINQUART` - out-in-quartic
- `go.EASING_OUTINQUINT` - out-in-quintic
- `go.EASING_OUTINSINE` - out-in-sine
- `go.EASING_OUTQUAD` - out-quadratic
- `go.EASING_OUTQUART` - out-quartic
- `go.EASING_OUTQUINT` - out-quintic
- `go.EASING_OUTSINE` - out-sine

### go.exists
*Type:* FUNCTION
This function can check for game objects in any collection by specifying
the collection name in the URL.

**Parameters**

- `url` (string | hash | url) - url of the game object to check

**Returns**

- `exists` (boolean) - true if the game object exists

**Examples**

Check if game object "my_game_object" exists in the current collection
```
go.exists("/my_game_object")

```

Check if game object exists in another collection
```
go.exists("other_collection:/my_game_object")

```

### go.get
*Type:* FUNCTION
gets a named property of the specified game object or component

**Parameters**

- `url` (string | hash | url) - url of the game object or component having the property
- `property` (string | hash) - id of the property to retrieve
- `options` (go.property_options) (optional) - optional property access options

**Returns**

- `value` (number | boolean | hash | string | url | vector3 | vector4 | quaternion | resource_data) - the value of the specified property

**Examples**

Get a property "speed" from a script "player", the property must be declared in the player-script:
```
go.property("speed", 50)

```

Then in the calling script (assumed to belong to the same game object, but does not have to):
```
local speed = go.get("#player", "speed")

```

Get a value in a material property array
```
-- get the first vector4 in the array: example[0] (the glsl indices are 0-based)
go.get(url, "example", {index=1})

-- get the last vector4 in the array: example[15] (the glsl indices are 0-based)
go.get(url, "example", {index=16})

-- get an element of a vector4 in the array: example[0].x (the glsl indices are 0-based)
go.get(url, "example.x", {index=1})

```

Getting all values in a material property array as a table
```
-- get all vector4's in the constant array
go.get(url, "example")
-- result: { vector4, vector4, ... }

-- get all elements of the vector4's from an array
go.get(url, "example.x")
-- result: { number1, number2, ... }

```

Get a named property
```
-- get the resource of a certain gui font
local font_hash = go.get("#gui", "fonts", {key = "system_font_BIG"})

```

Get a property from a sub-component, using the "keys" options table
```
-- Addressing the first level of a component:
go.get("#particlefx", "material", { keys = { "cone_emitter" } })

```

Get a property into a deeper sub-hierarchy (if the component supports it).
```
-- Note: There is currently no component that supports this, but a custom component could.
go.get("#my_component", "some_property", { keys = { "root", "child_node" } })

```

### go.get_id
*Type:* FUNCTION
Returns or constructs an instance identifier. The instance id is a hash
of the absolute path to the instance.

If path is specified, it can either be absolute or relative to the instance of the calling script.
If path is not specified, the id of the game object instance the script is attached to will be returned.

**Parameters**

- `path` (string) (optional) - path of the instance for which to return the id

**Returns**

- `id` (hash) - instance id

**Examples**

For the instance with path /my_sub_collection/my_instance, the following calls are equivalent:
```
local id = go.get_id() -- no path, defaults to the instance containing the calling script
print(id) --> hash: [/my_sub_collection/my_instance]

local id = go.get_id("/my_sub_collection/my_instance") -- absolute path
print(id) --> hash: [/my_sub_collection/my_instance]

local id = go.get_id("my_instance") -- relative path
print(id) --> hash: [/my_sub_collection/my_instance]

```

### go.get_parent
*Type:* FUNCTION
Get the parent for a game object instance.

**Parameters**

- `id` (string | hash | url) (optional) - optional id of the game object instance to get parent for, defaults to the instance containing the calling script

**Returns**

- `parent_id` (hash | nil) - parent instance or <code>nil</code>

**Examples**

Get parent of the instance containing the calling script:
```
local parent_id = go.get_parent()

```

Get parent of the instance with id "x":
```
local parent_id = go.get_parent("x")

```

### go.get_position
*Type:* FUNCTION
The position is relative the parent (if any). Use go.get_world_position to retrieve the global world position.

**Parameters**

- `id` (string | hash | url) (optional) - optional id of the game object instance to get the position for, by default the instance of the calling script

**Returns**

- `position` (vector3) - instance position

**Replaces:** request_transform transform_response

**Examples**

Get the position of the game object instance the script is attached to:
```
local p = go.get_position()

```

Get the position of another game object instance "my_gameobject":
```
local pos = go.get_position("my_gameobject")

```

### go.get_rotation
*Type:* FUNCTION
The rotation is relative to the parent (if any). Use go.get_world_rotation to retrieve the global world rotation.

**Parameters**

- `id` (string | hash | url) (optional) - optional id of the game object instance to get the rotation for, by default the instance of the calling script

**Returns**

- `rotation` (quaternion) - instance rotation

**Examples**

Get the rotation of the game object instance the script is attached to:
```
local r = go.get_rotation()

```

Get the rotation of another game object instance with id "x":
```
local r = go.get_rotation("x")

```

### go.get_scale
*Type:* FUNCTION
The scale is relative the parent (if any). Use go.get_world_scale to retrieve the global world 3D scale factor.

**Parameters**

- `id` (string | hash | url) (optional) - optional id of the game object instance to get the scale for, by default the instance of the calling script

**Returns**

- `scale` (vector3) - instance scale factor

**Examples**

Get the scale of the game object instance the script is attached to:
```
local s = go.get_scale()

```

Get the scale of another game object instance with id "x":
```
local s = go.get_scale("x")

```

### go.get_scale_uniform
*Type:* FUNCTION
The uniform scale is relative the parent (if any). If the underlying scale vector is non-uniform the min element of the vector is returned as the uniform scale factor.

**Parameters**

- `id` (string | hash | url) (optional) - optional id of the game object instance to get the uniform scale for, by default the instance of the calling script

**Returns**

- `scale` (number) - uniform instance scale factor

**Examples**

Get the scale of the game object instance the script is attached to:
```
local s = go.get_scale_uniform()

```

Get the uniform scale of another game object instance with id "x":
```
local s = go.get_scale_uniform("x")

```

### go.get_world_position
*Type:* FUNCTION
The function will return the world position calculated at the end of the previous frame.
To recalculate it within the current frame, use go.update_world_transform on the instance before calling this.
Use go.get_position to retrieve the position relative to the parent.

**Parameters**

- `id` (string | hash | url) (optional) - optional id of the game object instance to get the world position for, by default the instance of the calling script

**Returns**

- `position` (vector3) - instance world position

**Examples**

Get the world position of the game object instance the script is attached to:
```
local p = go.get_world_position()

```

Get the world position of another game object instance with id "x":
```
local p = go.get_world_position("x")

```

### go.get_world_rotation
*Type:* FUNCTION
The function will return the world rotation calculated at the end of the previous frame.
To recalculate it within the current frame, use go.update_world_transform on the instance before calling this.
Use go.get_rotation to retrieve the rotation relative to the parent.

**Parameters**

- `id` (string | hash | url) (optional) - optional id of the game object instance to get the world rotation for, by default the instance of the calling script

**Returns**

- `rotation` (quaternion) - instance world rotation

**Examples**

Get the world rotation of the game object instance the script is attached to:
```
local r = go.get_world_rotation()

```

Get the world rotation of another game object instance with id "x":
```
local r = go.get_world_rotation("x")

```

### go.get_world_scale
*Type:* FUNCTION
The function will return the world 3D scale factor calculated at the end of the previous frame.
To recalculate it within the current frame, use go.update_world_transform on the instance before calling this.
Use go.get_scale to retrieve the 3D scale factor relative to the parent.
This vector is derived by decomposing the transformation matrix and should be used with care.
For most cases it should be fine to use go.get_world_scale_uniform instead.

**Parameters**

- `id` (string | hash | url) (optional) - optional id of the game object instance to get the world scale for, by default the instance of the calling script

**Returns**

- `scale` (vector3) - instance world 3D scale factor

**Examples**

Get the world 3D scale of the game object instance the script is attached to:
```
local s = go.get_world_scale()

```

Get the world scale of another game object instance "x":
```
local s = go.get_world_scale("x")

```

### go.get_world_scale_uniform
*Type:* FUNCTION
The function will return the world scale factor calculated at the end of the previous frame.
To recalculate it within the current frame, use go.update_world_transform on the instance before calling this.
Use go.get_scale_uniform to retrieve the scale factor relative to the parent.

**Parameters**

- `id` (string | hash | url) (optional) - optional id of the game object instance to get the world scale for, by default the instance of the calling script

**Returns**

- `scale` (number) - instance world scale factor

**Examples**

Get the world scale of the game object instance the script is attached to:
```
local s = go.get_world_scale_uniform()

```

Get the world scale of another game object instance with id "x":
```
local s = go.get_world_scale_uniform("x")

```

### go.get_world_transform
*Type:* FUNCTION
The function will return the world transform matrix calculated at the end of the previous frame.
To recalculate it within the current frame, use go.update_world_transform on the instance before calling this.

**Parameters**

- `id` (string | hash | url) (optional) - optional id of the game object instance to get the world transform for, by default the instance of the calling script

**Returns**

- `transform` (matrix4) - instance world transform

**Examples**

Get the world transform of the game object instance the script is attached to:
```
local m = go.get_world_transform()

```

Get the world transform of another game object instance with id "x":
```
local m = go.get_world_transform("x")

```

### go.PLAYBACK
*Type:* ENUM
Playback modes

**Members**

- `go.PLAYBACK_LOOP_BACKWARD` - loop backward
- `go.PLAYBACK_LOOP_FORWARD` - loop forward
- `go.PLAYBACK_LOOP_PINGPONG` - ping pong loop
- `go.PLAYBACK_NONE` - no playback
- `go.PLAYBACK_ONCE_BACKWARD` - once backward
- `go.PLAYBACK_ONCE_FORWARD` - once forward
- `go.PLAYBACK_ONCE_PINGPONG` - once ping pong

### go.property
*Type:* FUNCTION
This function defines a property which can then be used in the script through the self-reference.
The properties defined this way are automatically exposed in the editor in game objects and collections which use the script.
Note that you can only use this function outside any callback-functions like init and update.

**Parameters**

- `name` (string) - the id of the property
- `value` (number | hash | string | url | vector3 | vector4 | quaternion | resource_data | boolean) - default value of the property. In the case of a url, only the empty constructor msg.url() is allowed. In the case of a resource one of the resource constructors (eg resource.atlas(), resource.font() etc) is expected.

**Examples**

This example demonstrates how to define a property called "health" in a script.
The health is decreased whenever someone sends a message called "take_damage" to the script.
```
go.property("health", 100)

function init(self)
    -- prints 100 to the output
    print(self.health)
end

function on_message(self, message_id, message, sender)
    if message_id == hash("take_damage") then
        self.health = self.health - message.damage
        print("Ouch! My health is now: " .. self.health)
    end
end

```

Text properties can contain UTF-8 and newline characters:
```
go.property("player_name", "Player One")
go.property("dialogue", "First line\nSecond line")

```

### go.property_options
*Type:* STRUCT
Options for accessing indexed or internal component properties with go.get and go.set.

**Members**

- `index?` (integer) - Index into an array property, starting at one.
- `key?` (hash) - Name of an internal property.
- `keys?` (hash[]) - Internal component resources identified by key, such as particle FX emitters.

### go.set
*Type:* FUNCTION
sets a named property of the specified game object or component, or a material constant

**Parameters**

- `url` (string | hash | url) - url of the game object or component having the property
- `property` (string | hash) - id of the property to set
- `value` (number | boolean | hash | string | url | vector3 | vector4 | quaternion | resource_data) - the value to set
- `options` (go.property_options) (optional) - optional property access options

**Examples**

Set a property "speed" of a script "player", the property must be declared in the player-script:
```
go.property("speed", 50)

```

Then in the calling script (assumed to belong to the same game object, but does not have to):
```
go.set("#player", "speed", 100)

```

Set a vector4 in a material property array
```
-- set the first vector4 in the array: example[0] = v (the glsl indices are 0-based)
go.set(url, "example", vmath.vector4(1,1,1,1), {index=1})

-- set the last vector4 in the array: example[15] = v (the glsl indices are 0-based)
go.set(url, "example", vmath.vector4(2,2,2,2), {index=16})

-- set an element of a vector4 in the array: example[0].x = 7 (the glsl indices are 0-based)
go.set(url, "example.x", 7, {index=1})

```

Set a material property array by a table of vector4
```
-- set the first two vector4's in the array
-- if the array has more than two elements in the array they will not be set
go.set(url, "example", { vmath.vector4(1,1,1,1), vmath.vector4(2,2,2,2) })

```

Set a named property
```
go.property("big_font", resource.font())

function init(self)
    go.set("#gui", "fonts", self.big_font, {key = "system_font_BIG"})
end

```

Set a property on a sub-component, using the "keys" options table
```
go.property("my_material", resource.material)
function init(self)
    go.set("#particlefx", "material", self.my_material, { keys = { "cone_emitter" } })
end

```

Set a property in a deeper sub-hierarchy (if the component supports it).
```
-- Note: There is currently no component that supports this, but a custom component could.
go.set("#my_component", "some_property", some_value, { keys = { "root", "child_node" } })

```

### go.set_parent
*Type:* FUNCTION
Sets the parent for a game object instance. This means that the instance will exist in the geometrical space of its parent,
like a basic transformation hierarchy or scene graph. If no parent is specified, the instance will be detached from any parent and exist in world
space.
This function will generate a set_parent message. It is not until the message has been processed that the change actually takes effect. This
typically happens later in the same frame or the beginning of the next frame. Refer to the manual to learn how messages are processed by the
engine.

**Parameters**

- `id` (string | hash | url) (optional) - optional id of the game object instance to set parent for, defaults to the instance containing the calling script
- `parent_id` (string | hash | url) (optional) - optional id of the new parent game object, defaults to detaching game object from its parent
- `keep_world_transform` (boolean) (optional) - optional boolean, set to true to maintain the world transform when changing spaces. Defaults to false.

**Examples**

Attach myself to another instance "my_parent":
```
go.set_parent(go.get_id(),go.get_id("my_parent"))

```

Attach an instance "my_instance" to another instance "my_parent":
```
go.set_parent(go.get_id("my_instance"),go.get_id("my_parent"))

```

Detach an instance "my_instance" from its parent (if any):
```
go.set_parent(go.get_id("my_instance"))

```

### go.set_position
*Type:* FUNCTION
The position is relative to the parent (if any). The global world position cannot be manually set.

**Parameters**

- `position` (vector3) - position to set
- `id` (string | hash | url) (optional) - optional id of the game object instance to set the position for, by default the instance of the calling script

**Examples**

Set the position of the game object instance the script is attached to:
```
local p = ...
go.set_position(p)

```

Set the position of another game object instance with id "x":
```
local p = ...
go.set_position(p, "x")

```

### go.set_rotation
*Type:* FUNCTION
The rotation is relative to the parent (if any). The global world rotation cannot be manually set.

**Parameters**

- `rotation` (quaternion) - rotation to set
- `id` (string | hash | url) (optional) - optional id of the game object instance to get the rotation for, by default the instance of the calling script

**Examples**

Set the rotation of the game object instance the script is attached to:
```
local r = ...
go.set_rotation(r)

```

Set the rotation of another game object instance with id "x":
```
local r = ...
go.set_rotation(r, "x")

```

### go.set_scale
*Type:* FUNCTION
The scale factor is relative to the parent (if any). The global world scale factor cannot be manually set.
 See manual to know how physics affected when setting scale from this function.

**Parameters**

- `scale` (number | vector3) - vector or uniform scale factor, must be greater than 0
- `id` (string | hash | url) (optional) - optional id of the game object instance to get the scale for, by default the instance of the calling script

**Examples**

Set the scale of the game object instance the script is attached to:
```
local s = vmath.vector3(2.0, 1.0, 1.0)
go.set_scale(s)

```

Set the scale of another game object instance with id "obj_id":
```
local s = 1.2
go.set_scale(s, "obj_id")

```

### go.set_scale_xy
*Type:* FUNCTION
The scale factor is relative to the parent (if any). The global world scale factor cannot be manually set.
 See manual to know how physics affected when setting scale from this function.

**Parameters**

- `scale` (number | vector3) - vector or uniform scale factor, must be greater than 0
- `id` (string | hash | url) (optional) - optional id of the game object instance to get the scale for, by default the instance of the calling script

**Examples**

Set the scale of the game object instance the script is attached to:
```
local s = vmath.vector3(2.0, 1.0, 5.0)
go.set_scale_xy(s) -- z will not be set here, only x and y

```

Set the scale of another game object instance with id "obj_id":
```
local s = 1.2
go.set_scale_xy(s, "obj_id") -- z will not be set here, only x and y

```

### go.update_world_transform
*Type:* FUNCTION
Recalculates and updates the cached world transform immediately for the target instance
and its ancestors (parent chain up to the collection root). Descendants (children) are
not updated by this function.
If no id is provided, the instance of the calling script is used.
 Use this after changing local transform mid-frame when you need the
new world transform right away (e.g. before end-of-frame updates). Note that child
instances will still have last-frame world transforms until the regular update.

**Parameters**

- `id` (string | hash | url) (optional) - optional id of the game object instance to update

**Examples**

Update this game object's world transform:
```
go.update_world_transform()

```

Update another game object's world transform:
```
go.update_world_transform("/other")

```

### go.world_to_local_position
*Type:* FUNCTION
The function uses world transformation calculated at the end of previous frame.

**Parameters**

- `position` (vector3) - position which need to be converted
- `url` (string | hash | url) - url of the game object which coordinate system convert to

**Returns**

- `converted_postion` (vector3) - converted position

**Examples**

Convert position of "test" game object into coordinate space of "child" object.
```
  local test_pos = go.get_world_position("/test")
  local child_pos = go.get_world_position("/child")
  local new_position = go.world_to_local_position(test_pos, "/child")

```

### go.world_to_local_transform
*Type:* FUNCTION
The function uses world transformation calculated at the end of previous frame.

**Parameters**

- `transformation` (matrix4) - transformation which need to be converted
- `url` (string | hash | url) - url of the game object which coordinate system convert to

**Returns**

- `converted_transform` (matrix4) - converted transformation

**Examples**

Convert transformation of "test" game object into coordinate space of "child" object.
```
   local test_transform = go.get_world_transform("/test")
   local child_transform = go.get_world_transform("/child")
   local result_transform = go.world_to_local_transform(test_transform, "/child")

```

### init
*Type:* FUNCTION
This is a callback-function, which is called by the engine when a script component is initialized. It can be used
to set the initial state of the script.

**Parameters**

- `self` (script_instance) - script instance used for storing state

**Examples**

```
function init(self)
    -- set up useful data
    self.my_value = 1
end

```

### late_update
*Type:* FUNCTION
This is a callback-function, which is called by the engine at the end of the frame to update the state of a script
component. Use it to make final adjustments to the game object instance.

**Parameters**

- `self` (script_instance) - script instance used for storing state
- `dt` (number) - the time-step of the frame update

### on_input
*Type:* FUNCTION
This is a callback-function, which is called by the engine when user input is sent to the game object instance of the script.
It can be used to take action on the input, e.g. move the instance according to the input.
For an instance to obtain user input, it must first acquire input focus
through the message acquire_input_focus.
Any instance that has obtained input will be put on top of an
input stack. Input is sent to all listeners on the stack until the
end of stack is reached, or a listener returns true
to signal that it wants input to be consumed.
See the documentation of acquire_input_focus for more
information.

**Parameters**

- `self` (script_instance) - script instance used for storing state
- `action_id` (hash | nil) - id of the received input action, as mapped in the input_binding-file, or <code>nil</code> for mouse movement
- `action` (on_input.action) - input data for the action

**Returns**

- `consume` (boolean | nil) - optional boolean to signal if the input should be consumed (not passed on to others) or not, default is false

**Examples**

This example demonstrates how a game object instance can be moved as a response to user input.
```
function init(self)
    -- acquire input focus
    msg.post(".", "acquire_input_focus")
    -- maximum speed the instance can be moved
    self.max_speed = 2
    -- velocity of the instance, initially zero
    self.velocity = vmath.vector3()
end

function update(self, dt)
    -- move the instance
    go.set_position(go.get_position() + dt * self.velocity)
end

function on_input(self, action_id, action)
    -- check for movement input
    if action_id == hash("right") then
        if action.released then -- reset velocity if input was released
            self.velocity = vmath.vector3()
        else -- update velocity
            self.velocity = vmath.vector3(action.value * self.max_speed, 0, 0)
        end
    end
end

```

### on_input.action
*Type:* STRUCT
Data supplied to the global on_input lifecycle function.

**Members**

- `value?` (number) - Amount of input, usually 1 for buttons or between 0 and 1 for analogue input; absent for pointer movement and text input.
- `pressed?` (boolean) - Whether the input was pressed this frame; absent for pointer movement and text input.
- `released?` (boolean) - Whether the input was released this frame; absent for pointer movement and text input.
- `repeated?` (boolean) - Whether the input was repeated this frame; absent for pointer movement and text input.
- `x?` (number) - Pointer x-coordinate; absent for gamepad, key, and text input.
- `y?` (number) - Pointer y-coordinate; absent for gamepad, key, and text input.
- `screen_x?` (number) - Pointer x-coordinate in screen space; absent for gamepad, key, and text input.
- `screen_y?` (number) - Pointer y-coordinate in screen space; absent for gamepad, key, and text input.
- `dx?` (number) - Change in the pointer x-coordinate; absent for gamepad, key, and text input.
- `dy?` (number) - Change in the pointer y-coordinate; absent for gamepad, key, and text input.
- `screen_dx?` (number) - Change in the pointer x-coordinate in screen space; absent for gamepad, key, and text input.
- `screen_dy?` (number) - Change in the pointer y-coordinate in screen space; absent for gamepad, key, and text input.
- `acc_x?` (number) - Accelerometer x value, when present.
- `acc_y?` (number) - Accelerometer y value, when present.
- `acc_z?` (number) - Accelerometer z value, when present.
- `gamepad?` (integer) - Index of the gamepad that provided the input.
- `userid?` (integer) - Id of the user associated with the controller.
- `gamepad_guid?` (string) - SDL-compatible guid, supplied with a gamepad-connected action.
- `gamepad_guid_info?` (on_input.gamepad_guid_info) - Parsed guid information, supplied with a gamepad-connected action.
- `gamepad_unknown?` (boolean) - Whether the input originated from an unknown or unmapped gamepad.
- `gamepad_name?` (string) - Name of a connected gamepad.
- `gamepad_axis?` (number[]) - Axis values, supplied only for raw gamepad input.
- `gamepad_hats?` (number[]) - Hat values, supplied only for raw gamepad input.
- `gamepad_buttons?` (number[]) - Button values, supplied only for raw gamepad input.
- `touch?` (on_input.touch[]) - Touch inputs, one entry per finger.
- `text?` (string) - Text entered by a text action, or the current sequence for marked-text composition such as Japanese Kana.

### on_input.gamepad_guid_info
*Type:* STRUCT
Parsed fields from a connected gamepad guid.

**Members**

- `vendor` (integer) - USB vendor id.
- `product` (integer) - USB product id.
- `bus` (integer) - Bus used to communicate with the device.
- `crc` (integer) - SDL CRC16 signature.
- `version` (integer) - Device or firmware version.

### on_input.touch
*Type:* STRUCT
One touch entry in on_input.action.

**Members**

- `id` (integer) - Identifier for the touch during its lifetime.
- `pressed` (boolean) - Whether the finger was pressed this frame.
- `released` (boolean) - Whether the finger was released this frame.
- `tap_count` (integer) - Number of taps, such as one for a single tap and two for a double tap.
- `x` (number) - Touch x-coordinate.
- `y` (number) - Touch y-coordinate.
- `screen_x` (number) - Touch x-coordinate in screen space.
- `screen_y` (number) - Touch y-coordinate in screen space.
- `dx` (number) - Change in the touch x-coordinate.
- `dy` (number) - Change in the touch y-coordinate.
- `screen_dx` (number) - Change in the touch x-coordinate in screen space.
- `screen_dy` (number) - Change in the touch y-coordinate in screen space.

### on_message
*Type:* FUNCTION
This is a callback-function, which is called by the engine whenever a message has been sent to the script component.
It can be used to take action on the message, e.g. send a response back to the sender of the message.
The message parameter is a table containing the message data. If the message is sent from the engine, the
documentation of the message specifies which data is supplied.

**Parameters**

- `self` (script_instance) - script instance used for storing state
- `message_id` (hash) - id of the received message
- `message` (table<any, any>) - a table containing the message data
- `sender` (url) - address of the sender

**Examples**

This example demonstrates how a game object instance, called "a", can communicate with another instance, called "b". It
is assumed that both script components of the instances has id "script".
Script of instance "a":
```
function init(self)
    -- let b know about some important data
    msg.post("b#script", "my_data", {important_value = 1})
end

```

Script of instance "b":
```
function init(self)
    -- store the url of instance "a" for later use, by specifying nil as socket we
    -- automatically use our own socket
    self.a_url = msg.url(nil, go.get_id("a"), "script")
end

function on_message(self, message_id, message, sender)
    -- check message and sender
    if message_id == hash("my_data") and sender == self.a_url then
        -- use the data in some way
        self.important_value = message.important_value
    end
end

```

### on_reload
*Type:* FUNCTION
This is a callback-function, which is called by the engine when the script component is reloaded, e.g. from the editor.
It can be used for live development, e.g. to tweak constants or set up the state properly for the instance.

**Parameters**

- `self` (script_instance) - script instance used for storing state

**Examples**

This example demonstrates how to tweak the speed of a game object instance that is moved on user input.
```
function init(self)
    -- acquire input focus
    msg.post(".", "acquire_input_focus")
    -- maximum speed the instance can be moved, this value is tweaked in the on_reload function below
    self.max_speed = 2
    -- velocity of the instance, initially zero
    self.velocity = vmath.vector3()
end

function update(self, dt)
    -- move the instance
    go.set_position(go.get_position() + dt * self.velocity)
end

function on_input(self, action_id, action)
    -- check for movement input
    if action_id == hash("right") then
        if action.released then -- reset velocity if input was released
            self.velocity = vmath.vector3()
        else -- update velocity
            self.velocity = vmath.vector3(action.value * self.max_speed, 0, 0)
        end
    end
end

function on_reload(self)
    -- edit this value and reload the script component
    self.max_speed = 100
end

```

### position
*Type:* PROPERTY
The position of the game object.
The type of the property is vector3.

**Examples**

How to query a game object's position, either as a vector3 or selecting a specific dimension:
```
function init(self)
  -- get position from "player"
  local pos = go.get("player", "position")
  local posx = go.get("player", "position.x")
  -- do something useful
  assert(pos.x == posx)
end

```

### release_input_focus
*Type:* MESSAGE
Post this message to an instance to make that instance release the user input focus.
See acquire_input_focus for more information on how the user input handling
works.

**Examples**

How to make a game object stop receiving input:
```
msg.post(".", "release_input_focus")

```

### rotation
*Type:* PROPERTY
The rotation of the game object.
The type of the property is quaternion.

**Examples**

How to set a game object's rotation:
```
function init(self)
  -- set "player" rotation to 45 degrees around z.
  local rotz = vmath.quat_rotation_z(3.141592 / 4)
  go.set("player", "rotation", rotz)
end

```

### scale
*Type:* PROPERTY
The uniform scale of the game object. The type of the property is number.

**Examples**

How to scale a game object:
```
function init(self)
  -- Double the scaling on "player"
  local scale = go.get("player", "scale")
  go.set("player", "scale", scale * 2)
end

```

### set_parent
*Type:* MESSAGE
When this message is sent to an instance, it sets the parent of that instance. This means that the instance will exist
in the geometrical space of its parent, like a basic transformation hierarchy or scene graph. If no parent is specified,
the instance will be detached from any parent and exist in world space. A script can send this message to itself to set
the parent of its instance.

**Parameters**

- `parent_id` (hash) - the id of the new parent
- `keep_world_transform` (number) - if the world transform of the instance should be preserved when changing spaces, 0 for false and 1 for true. The default value is 1.

**Examples**

Attach myself to another instance "my_parent":
```
msg.post(".", "set_parent", {parent_id = go.get_id("my_parent")})

```

Attach an instance "my_instance" to another instance "my_parent":
```
msg.post("my_instance", "set_parent", {parent_id = go.get_id("my_parent")})

```

Detach an instance "my_instance" from its parent (if any):
```
msg.post("my_instance", "set_parent")

```

### update
*Type:* FUNCTION
This is a callback-function, which is called by the engine every frame to update the state of a script component.
It can be used to perform any kind of game related tasks, e.g. moving the game object instance.

**Parameters**

- `self` (script_instance) - script instance used for storing state
- `dt` (number) - the time-step of the frame update

**Examples**

This example demonstrates how to move a game object instance through the script component:
```
function init(self)
    -- set initial velocity to be 1 along world x-axis
    self.my_velocity = vmath.vector3(1, 0, 0)
end

function update(self, dt)
    -- move the game object instance
    go.set_position(go.get_position() + dt * self.my_velocity)
end

```
