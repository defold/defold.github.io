# Model

**Namespace:** `model`
**Language:** Lua
**Type:** Defold Lua
**File:** `model_ddf.proto`
**Source:** `engine/gamesys/proto/gamesys/model_ddf.proto`

Model API documentation

## API

### animation
*Type:* PROPERTY
The current animation set on the component. The type of the property is hash.

**Examples**

How to read the current animation from a model component:
```
function init(self)
  -- Get the current animation on component "model"
  local animation = go.get("#model", "animation")
  if animation == hash("run_left") then
    -- Running left. Do something...
  end
end

```

### cursor
*Type:* PROPERTY
The normalized animation cursor. The type of the property is number.
 Please note that model events may not fire as expected when the cursor is manipulated directly.

**Examples**

How to get the normalized cursor value:
```
function init(self)
  -- Get the cursor value on component "model"
  cursor = go.get("#model", "cursor")
end

```

How to animate the cursor from 0.0 to 1.0 using linear easing for 2.0 seconds:
```
function init(self)
  -- Get the current value on component "model"
  go.set("#model", "cursor", 0.0)
  -- Animate the cursor value
  go.animate("#model", "cursor", go.PLAYBACK_LOOP_FORWARD, 1.0, go.EASING_LINEAR, 2)
end

```

### model.aabb
*Type:* STRUCT
Axis-aligned bounding box

**Members**

- `min` (vector3) - minimum local-space bounds
- `max` (vector3) - maximum local-space bounds

### model.cancel
*Type:* FUNCTION
Cancels all animation on a model component.

**Parameters**

- `url` (string | hash | url) - the model for which to cancel the animation

### model.get_aabb
*Type:* FUNCTION
Get AABB of the whole model in local coordinate space.

**Parameters**

- `url` (string | hash | url) - the model

**Returns**

- `aabb` (model.aabb) - model bounds; an empty model returns zero vectors

**Examples**

```
model.get_aabb("#model") -> { min = vmath.vector3(-2.5, -3.0, 0), max = vmath.vector3(1.5, 5.5, 0) }
model.get_aabb("#empty") -> { min = vmath.vector3(0, 0, 0), max = vmath.vector3(0, 0, 0) }

```

### model.get_blend_weights
*Type:* FUNCTION
Returns a table of numbers with one entry per morph target on the first mesh of the model that has morph targets.
Values reflect the rig state at call time (after animation, and any active script override from model.set_blend_weights).

**Parameters**

- `url` (string | hash | url) - the model component

**Returns**

- `weights` (number[]) - array of weight values, or empty table if the model has no morph targets

**Examples**

```
local w = model.get_blend_weights("#model")
for i = 1, #w do
  print(i, w[i])
end
-- change the data in the table and then set the weights again
w[1] = 0.75
w[2] = 0.25
model.set_blend_weights("#model", w)

```

### model.get_go
*Type:* FUNCTION
Gets the id of the game object that corresponds to a model skeleton bone.
The returned game object can be used for parenting and transform queries.
This function has complexity O(n), where n is the number of bones in the model skeleton.
Game objects corresponding to a model skeleton bone can not be individually deleted.

**Parameters**

- `url` (string | hash | url) - the model to query
- `bone_id` (string | hash) - id of the corresponding bone

**Returns**

- `id` (hash) - id of the game object

**Examples**

The following examples assumes that the model component has id "model".
How to parent the game object of the calling script to the "right_hand" bone of the model in a player game object:
```
function init(self)
    local parent = model.get_go("player#model", "right_hand")
    msg.post(".", "set_parent", {parent_id = parent})
end

```

### model.get_mesh_aabb
*Type:* FUNCTION
Get AABB of all meshes.

**Parameters**

- `url` (string | hash | url) - the model

**Returns**

- `aabb` (table<hash, model.aabb>) - mesh bounds keyed by mesh identifier

**Examples**

```
model.get_mesh_aabb("#model") -> { hash("Sword") = { min = vmath.vector3(-0.5, -0.5, 0), max = vmath.vector3(0.5, 0.5, 0) }, hash("Shield") = { min = vmath.vector3(-0.5, -0.5, -0.5), max = vmath.vector3(0.5, 0.5, 0.5) } }

```

### model.get_mesh_enabled
*Type:* FUNCTION
Get the enabled state of a mesh

**Parameters**

- `url` (string | hash | url) - the model
- `mesh_id` (string | hash | url) - the id of the mesh

**Returns**

- `enabled` (boolean) - true if the mesh is visible, false otherwise

**Examples**

```
function init(self)
    if model.get_mesh_enabled("#model", "Sword") then
       -- set properties specific for the sword
       self.weapon_properties = game.data.weapons["Sword"]
    end
end

```

### model.play_anim
*Type:* FUNCTION
Plays an animation on a model component with specified playback
mode and parameters.
An optional completion callback function can be provided that will be called when
the animation has completed playing. If no function is provided,
a model_animation_done message is sent to the script that started the animation.
 The callback is not called (or message sent) if the animation is
cancelled with model.cancel. The callback is called (or message sent) only for
animations that play with the following playback modes:

go.PLAYBACK_ONCE_FORWARD
go.PLAYBACK_ONCE_BACKWARD
go.PLAYBACK_ONCE_PINGPONG

**Parameters**

- `url` (string | hash | url) - the model for which to play the animation
- `anim_id` (string | hash) - id of the animation to play
- `playback` (go.PLAYBACK) - playback mode of the animation
- `play_properties` (model.play_properties) (optional) - optional playback properties
- `complete_function` (fun(self:script_instance, message_id:hash, message:message.model.model_animation_done, sender:url)) (optional) - function to call when the animation has completed.
<dl>
<dt class="api-lua-v2-type-definition"><code>self:<a href="../builtins-lua/#script_instance">script_instance</a></code></dt>
<dd>The current script instance.</dd>
<dt class="api-lua-v2-type-definition"><code>message_id:<a href="../builtins-lua/#hash">hash</a></code></dt>
<dd>The name of the completion message, <code>"model_animation_done"</code>.</dd>
<dt class="api-lua-v2-type-definition"><code>message:<a href="#model_animation_done">message.model.model_animation_done</a></code></dt>
<dd>Information about the completion.</dd>
<dt class="api-lua-v2-type-definition"><code>sender:<a href="../msg-lua/#url">url</a></code></dt>
<dd>The invoker of the callback: the model component.</dd>
</dl>

**Examples**

The following examples assumes that the model has id "model".
How to play the "jump" animation followed by the "run" animation:
```
local function anim_done(self, message_id, message, sender)
  if message_id == hash("model_animation_done") then
    if message.animation_id == hash("jump") then
      -- open animation done, chain with "run"
      local properties = { blend_duration = 0.2 }
      model.play_anim(url, "run", go.PLAYBACK_LOOP_FORWARD, properties, anim_done)
    end
  end
end

function init(self)
    local url = msg.url("#model")
    local play_properties = { blend_duration = 0.1 }
    -- first blend during 0.1 sec into the jump, then during 0.2 s into the run animation
    model.play_anim(url, "jump", go.PLAYBACK_ONCE_FORWARD, play_properties, anim_done)
end

```

### model.play_properties
*Type:* STRUCT
Model animation playback properties

**Members**

- `blend_duration?` (number) - duration of a linear blend from the current animation
- `offset?` (number) - normalized initial animation cursor
- `playback_rate?` (number) - positive animation playback rate

### model.reset_constant
*Type:* FUNCTION
Resets a shader constant for a model component.
The constant must be defined in the material assigned to the model.
Resetting a constant through this function implies that the value defined in the material will be used.
Which model to reset a constant for is identified by the URL.

**Parameters**

- `url` (string | hash | url) - the model that should have a constant reset.
- `constant` (string | hash) - name of the constant.

**Examples**

The following examples assumes that the model has id "model" and that the default-material in builtins is used, which defines the constant "tint".
If you assign a custom material to the model, you can reset the constants defined there in the same manner.
How to reset the tinting of a model:
```
function init(self)
    model.reset_constant("#model", "tint")
end

```

### model.set_blend_weights
*Type:* FUNCTION
Copies numeric values from weights into each morph target slot for every mesh on the model that has morph targets.
At most as many weights are applied as each mesh has morph targets; extra entries in the table are ignored.
Missing weights leave the tail zero-filled for meshes with more targets than entries.
The override is re-applied every frame after animations run, until cleared by omitting weights or passing nil.
To reset the weights, use model.set_blend_weights(url) or model.set_blend_weights(url, nil).

**Parameters**

- `url` (string | hash | url) - the model component
- `weights` (number[] | nil) (optional) - array of weight values (1-based indices). Omit or pass <code>nil</code> to clear the override and return morphs to animation only

**Examples**

```
-- set the weights for the first 4 morph targets
model.set_blend_weights("#model", { 0, 1, 0.5, 0 })
-- clear the override, animation will continue if the weights are driven by an animation
model.set_blend_weights("#model") -- clear script override

```

### model.set_mesh_enabled
*Type:* FUNCTION
Enable or disable visibility of a mesh

**Parameters**

- `url` (string | hash | url) - the model
- `mesh_id` (string | hash | url) - the id of the mesh
- `enabled` (boolean) - true if the mesh should be visible, false if it should be hideen

**Examples**

```
function init(self)
    model.set_mesh_enabled("#model", "Sword", false) -- hide the sword
    model.set_mesh_enabled("#model", "Axe", true)    -- show the axe
end

```

### model_animation_done
*Type:* MESSAGE
This message is sent when a Model animation has finished playing back to the script
that started the animation.
 No message is sent if a completion callback function was supplied
when the animation was started. No message is sent if the animation is cancelled with
model.cancel(). This message is sent only for animations that play with
the following playback modes:

go.PLAYBACK_ONCE_FORWARD
go.PLAYBACK_ONCE_BACKWARD
go.PLAYBACK_ONCE_PINGPONG

**Parameters**

- `animation_id` (hash) - the id of the completed animation
- `playback` (go.PLAYBACK) - the playback mode of the completed animation

**Examples**

```
function on_message(self, message_id, message, sender)
  if message_id == hash("model_animation_done") then
    if message.animation_id == hash("run") and message.playback == go.PLAYBACK_ONCE_FORWARD then
      -- The animation "run" has finished running forward.
    end
  end
end

```

### playback_rate
*Type:* PROPERTY
The animation playback rate. A multiplier to the animation playback rate. The type of the property is number.

**Examples**

How to set the playback_rate on component "model" to play at double the current speed:
```
function init(self)
  -- Get the current value on component "model"
  playback_rate = go.get("#model", "playback_rate")
  -- Set the playback_rate to double the previous value.
  go.set("#model", "playback_rate", playback_rate * 2)
end

```

The playback_rate is a non-negative number, a negative value will be clamped to 0.

### textureN
*Type:* PROPERTY
The texture hash id of the model. Used for getting/setting model texture for unit 0-7

**Examples**

How to set texture using a script property (see resource.texture):
```
go.property("my_texture", texture("/texture.png"))
function init(self)
  go.set("#model", "texture0", self.my_texture)
end

```

See resource.set_texture for an example on how to set the texture of an atlas.
