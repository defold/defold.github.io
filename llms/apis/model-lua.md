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

### material
*Type:* PROPERTY
The material used when rendering the model. The type of the property is hash.

**Examples**

How to set material using a script property (see resource.material):
```
go.property("my_material", resource.material("/material.material"))
function init(self)
  go.set("#model", "material", self.my_material)
end

```

### model.cancel
*Type:* FUNCTION
Cancels all animation on a model component.

**Parameters**

- `url` (string | hash | url) - the model for which to cancel the animation

### model.get_aabb
*Type:* FUNCTION
Get AABB of the whole model in local coordinate space.
AABB information return as a table with min and max fields, where min and max has type vmath.vector3.

**Parameters**

- `url` (string | hash | url) - the model

**Returns**

- `aabb` (table) - A table containing AABB of the model. If model has no meshes - return vmath.vector3(0,0,0) for min and max fields.

**Examples**

```
model.get_aabb("#model") -> { min = vmath.vector3(-2.5, -3.0, 0), max = vmath.vector3(1.5, 5.5, 0) }
model.get_aabb("#empty") -> { min = vmath.vector3(0, 0, 0), max = vmath.vector3(0, 0, 0) }

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
AABB information return as a table with min and max fields, where min and max has type vmath.vector3.

**Parameters**

- `url` (string | hash | url) - the model

**Returns**

- `aabb` (table) - A table containing info about all AABB in the format <hash(mesh_id), aabb_info>

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
- `playback` (constant) - playback mode of the animation
<ul>
<li><code>go.PLAYBACK_ONCE_FORWARD</code></li>
<li><code>go.PLAYBACK_ONCE_BACKWARD</code></li>
<li><code>go.PLAYBACK_ONCE_PINGPONG</code></li>
<li><code>go.PLAYBACK_LOOP_FORWARD</code></li>
<li><code>go.PLAYBACK_LOOP_BACKWARD</code></li>
<li><code>go.PLAYBACK_LOOP_PINGPONG</code></li>
</ul>
- `play_properties` (table) (optional) - optional table with properties
Play properties table:
<dl>
<dt><code>blend_duration</code></dt>
<dd><span class="type">number</span> Duration of a linear blend between the current and new animation.</dd>
<dt><code>offset</code></dt>
<dd><span class="type">number</span> The normalized initial value of the animation cursor when the animation starts playing.</dd>
<dt><code>playback_rate</code></dt>
<dd><span class="type">number</span> The rate with which the animation will be played. Must be positive.</dd>
</dl>
- `complete_function` (function(self, message_id, message, sender)) (optional) - function to call when the animation has completed.
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The current object.</dd>
<dt><code>message_id</code></dt>
<dd><span class="type">hash</span> The name of the completion message, <code>"model_animation_done"</code>.</dd>
<dt><code>message</code></dt>
<dd><span class="type">table</span> Information about the completion:</dd>
</dl>
<ul>
<li><span class="type">hash</span> <code>animation_id</code> - the animation that was completed.</li>
<li><span class="type">constant</span> <code>playback</code> - the playback mode for the animation.</li>
</ul>
<dl>
<dt><code>sender</code></dt>
<dd><span class="type">url</span> The invoker of the callback: the model component.</dd>
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
- `playback` (constant) - the playback mode of the completed animation

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
