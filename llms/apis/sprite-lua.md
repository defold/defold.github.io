# Sprite

**Namespace:** `sprite`
**Language:** Lua
**Type:** Defold Lua
**File:** `sprite_ddf.proto`
**Source:** `engine/gamesys/proto/gamesys/sprite_ddf.proto`

Sprite API documentation

## API

### animation
*Type:* PROPERTY
READ ONLY The current animation id. An animation that plays currently for the sprite. The type of the property is hash.

**Examples**

How to get the animation on component "sprite":
```
function init(self)
  local animation = go.get("#sprite", "animation")
end

```

### animation_done
*Type:* MESSAGE
This message is sent to the sender of a play_animation message when the
animation has completed.
Note that this message is sent only for animations that play with the following
playback modes:

Once Forward
Once Backward
Once Ping Pong

See play_animation for more information and examples of how to use
this message.

**Parameters**

- `current_tile` (number) - the current tile of the sprite
- `id` (hash) - id of the animation that was completed

**Examples**

How to sequence two animations together.
```
function init(self)
  -- play jump animation at init
  msg.post("#sprite", "play_animation", {id = hash("jump")})
end

function on_message(self, message_id, message, sender)
  -- check for animation done response
  if message_id == hash("animation_done") then
    -- start the walk animation
    msg.post("#sprite", "play_animation", { id = hash("walk") })
  end
end

```

### cursor
*Type:* PROPERTY
The normalized animation cursor. The type of the property is number.

**Examples**

How to get the normalized cursor value:
```
function init(self)
  -- Get the cursor value on component "sprite"
  local cursor = go.get("#sprite", "cursor")
end

```

How to animate the cursor from 0.0 to 1.0 using linear easing for 2.0 seconds:
```
function init(self)
  -- Set the cursor on component "sprite" to make the animation go from 0
  go.set("#sprite", "cursor", 0.0)
  -- Animate the cursor value
  go.animate("#sprite", "cursor", go.PLAYBACK_LOOP_FORWARD, 1.0, go.EASING_LINEAR, 2)
end

```

### frame_count
*Type:* PROPERTY
READ ONLY The frame count of the currently playing animation.

**Examples**

How to get the frame_count on component "sprite":
```
function init(self)
  local frame_count = go.get("#sprite", "frame_count")
end

```

### image
*Type:* PROPERTY
The image used when rendering the sprite. The type of the property is hash.

**Examples**

How to set image using a script property (see resource.atlas)
```
go.property("my_image", resource.atlas("/atlas.atlas"))
function init(self)
  go.set("#sprite", "image", self.my_image)
end

```

See resource.set_texture for an example on how to set the texture of an atlas.

### material
*Type:* PROPERTY
The material used when rendering the sprite. The type of the property is hash.

**Examples**

How to set material using a script property (see resource.material)
```
go.property("my_material", resource.material("/material.material"))
function init(self)
  go.set("#sprite", "material", self.my_material)
end

```

### play_animation
*Type:* MESSAGE
Post this message to a sprite component to make it play an animation from its tile set.

**Parameters**

- `id` (hash) - the id of the animation to play
- `offset` (number) - the normalized initial value of the animation cursor when the animation starts playing
- `playback_rate` (number) - the rate with which the animation will be played. Must be positive

**Examples**

In the example, it is assumed that the instance of the script has a sprite-component with id "sprite". The sprite itself is assumed to be bound to a tile set with animations "walk" and "jump".
```
msg.post("#sprite", "play_animation", {id = hash("jump")})

```

### playback_rate
*Type:* PROPERTY
The animation playback rate. A multiplier to the animation playback rate. The type of the property is number.
The playback_rate is a non-negative number, a negative value will be clamped to 0.

**Examples**

How to set the playback_rate on component "sprite" to play at double the current speed:
```
function init(self)
  -- Get the current value on component "sprite"
  playback_rate = go.get("#sprite", "playback_rate")
  -- Set the playback_rate to double the previous value.
  go.set("#sprite", "playback_rate", playback_rate * 2)
end

```

### scale
*Type:* PROPERTY
The non-uniform scale of the sprite. The type of the property is vector3.

**Examples**

How to scale a sprite independently along the X and Y axis:
```
function init(self)
  -- Double the y-axis scaling on component "sprite"
     local yscale = go.get("#sprite", "scale.y")
     go.set("#sprite", "scale.y", yscale * 2)
end

```

### size
*Type:* PROPERTY
The size of the sprite, not allowing for any additional scaling that may be applied.
The type of the property is vector3. It is not possible to set the size if the size mode
of the sprite is set to auto.

**Examples**

How to query a sprite's size, either as a vector or selecting a specific dimension:
```
function init(self)
  -- get size from component "sprite"
  local size = go.get("#sprite", "size")
  local sx = go.get("#sprite", "size.x")
  -- do something useful
  assert(size.x == sx)
end

```

### slice
*Type:* PROPERTY
The slice values of the sprite. The type of the property is a vector4 that corresponds to
the left, top, right, bottom values of the sprite in the editor.
It is not possible to set the slice property if the size mode of the sprite is set to auto.

**Examples**

How to query a sprite's slice values, either as a vector or selecting a specific dimension:
```
function init(self)
  local slice = go.get("#sprite", "slice")
  local slicex = go.get("#sprite", "slice.x")
  assert(slice.x == slicex)
end

```

Animate the slice property with go.animate:
```
function init(self)
  -- animate the entire slice vector at once
  go.animate("#sprite", "slice", go.PLAYBACK_LOOP_PINGPONG, vmath.vector4(96, 96, 96, 96), go.EASING_INCUBIC, 2)
  -- or animate a single component
  go.animate("#sprite", "slice.y", go.PLAYBACK_LOOP_PINGPONG, 32, go.EASING_INCUBIC, 8)
end

```

### sprite.play_flipbook
*Type:* FUNCTION
Play an animation on a sprite component from its tile set
An optional completion callback function can be provided that will be called when
the animation has completed playing. If no function is provided,
a animation_done message is sent to the script that started the animation.

**Parameters**

- `url` (string | hash | url) - the sprite that should play the animation
- `id` (string | hash) - hashed id of the animation to play
- `complete_function` (function(self, message_id, message, sender)) (optional) - function to call when the animation has completed.
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The current object.</dd>
<dt><code>message_id</code></dt>
<dd><span class="type">hash</span> The name of the completion message, <code>"animation_done"</code>.</dd>
<dt><code>message</code></dt>
<dd><span class="type">table</span> Information about the completion:</dd>
</dl>
<ul>
<li><span class="type">number</span> <code>current_tile</code> - the current tile of the sprite.</li>
<li><span class="type">hash</span> <code>id</code> - id of the animation that was completed.</li>
</ul>
<dl>
<dt><code>sender</code></dt>
<dd><span class="type">url</span> The invoker of the callback: the sprite component.</dd>
</dl>
- `play_properties` (table) (optional) - optional table with properties:
<dl>
<dt><code>offset</code></dt>
<dd><span class="type">number</span> the normalized initial value of the animation cursor when the animation starts playing.</dd>
<dt><code>playback_rate</code></dt>
<dd><span class="type">number</span> the rate with which the animation will be played. Must be positive.</dd>
</dl>

**Examples**

The following examples assumes that the model has id "sprite".
How to play the "jump" animation followed by the "run" animation:
```
local function anim_done(self, message_id, message, sender)
  if message_id == hash("animation_done") then
    if message.id == hash("jump") then
      -- jump animation done, chain with "run"
      sprite.play_flipbook(url, "run")
    end
  end
end

```

```
function init(self)
  local url = msg.url("#sprite")
  sprite.play_flipbook(url, "jump", anim_done)
end

```

### sprite.set_hflip
*Type:* FUNCTION
Sets horizontal flipping of the provided sprite's animations.
The sprite is identified by its URL.
If the currently playing animation is flipped by default, flipping it again will make it appear like the original texture.

**Parameters**

- `url` (string | hash | url) - the sprite that should flip its animations
- `flip` (boolean) - <code>true</code> if the sprite should flip its animations, <code>false</code> if not

**Examples**

How to flip a sprite so it faces the horizontal movement:
```
function update(self, dt)
  -- calculate self.velocity somehow
  sprite.set_hflip("#sprite", self.velocity.x < 0)
end

```

It is assumed that the sprite component has id "sprite" and that the original animations faces right.

### sprite.set_vflip
*Type:* FUNCTION
Sets vertical flipping of the provided sprite's animations.
The sprite is identified by its URL.
If the currently playing animation is flipped by default, flipping it again will make it appear like the original texture.

**Parameters**

- `url` (string | hash | url) - the sprite that should flip its animations
- `flip` (boolean) - <code>true</code> if the sprite should flip its animations, <code>false</code> if not

**Examples**

How to flip a sprite in a game which negates gravity as a game mechanic:
```
function update(self, dt)
  -- calculate self.up_side_down somehow, then:
  sprite.set_vflip("#sprite", self.up_side_down)
end

```

It is assumed that the sprite component has id "sprite" and that the original animations are up-right.
