# Particle effects

**Namespace:** `particlefx`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_particlefx.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_particlefx.cpp`

Functions and properties for controlling particle effect component playback and
shader constants.

## API

### animation
*Type:* PROPERTY
The animation used during rendering by an emitter in a particle FX component.
The property type is a hash and refers to a valid animation in an atlas or a tile source resource.
If the animation isn't found, and error will be thrown.

**Examples**

How to set and get the animation of an emitter in a particle FX.
```
local current_animation = go.get("#particlefx", "animation", { keys = { "explosion" } })
go.set("#particlefx", "animation", hash("explode_large"), { keys = { "explosion" } })

```

### image
*Type:* PROPERTY
The image used during rendering by an emitter in a particle FX component.
The property type is a hash and refers to an image resource (atlas or tile source).
Note: When setting the image, if the currently playing animation of the emitter
isn't found in the new image, the animation will be set to the first animation found.

**Examples**

How to set and get the image of an emitter in a particle FX.
```
go.property("my_atlas", resource.atlas())
function init(self)
    go.set("#particlefx", "image", self.my_atlas, { keys = { "explosion" } })
    local emitter_img = go.get("#particlefx", "image", { keys = { "explosion" } })
    assert(emitter_img == self.my_atlas)
end

```

### material
*Type:* PROPERTY
The material used during rendering by an emitter in a particle FX component.
The property type is a hash and refers to a material resource.

**Examples**

How to set and get the material of an emitter in a particle FX.
```
go.property("my_material", resource.material())
function init(self)
    go.set("#particlefx", "material", self.my_material, { keys = { "explosion" } })
    local emitter_mat = go.get("#particlefx", "material", { keys = { "explosion" } })
    assert(emitter_mat == self.my_material)
end

```

### particlefx.EMITTER_STATE
*Type:* ENUM
Emitter states

**Members**

- `particlefx.EMITTER_STATE_POSTSPAWN` - postspawn state The emitter is not spawning any particles, but has particles that are still alive.
- `particlefx.EMITTER_STATE_PRESPAWN` - prespawn state The emitter will be in this state when it has been started but before spawning any particles. Normally the emitter is in this state for a short time, depending on if a start delay has been set for this emitter or not.
- `particlefx.EMITTER_STATE_SLEEPING` - sleeping state The emitter does not have any living particles and will not spawn any particles in this state.
- `particlefx.EMITTER_STATE_SPAWNING` - spawning state The emitter is spawning particles.

### particlefx.play
*Type:* FUNCTION
Starts playing a particle FX component.
Particle FX started this way need to be manually stopped through particlefx.stop().
Which particle FX to play is identified by the URL.
 A particle FX will continue to emit particles even if the game object the particle FX component belonged to is deleted. You can call particlefx.stop() to stop it from emitting more particles.

**Parameters**

- `url` (string | hash | url) - the particle fx that should start playing.
- `emitter_state_function` (fun(self:script_instance, id:hash, emitter:hash, state:particlefx.EMITTER_STATE)) (optional) - optional callback function that will be called when an emitter attached to this particlefx changes state.

**Examples**

How to play a particle fx when a game object is created.
The callback receives the hash of the path to the particlefx, the hash of the id
of the emitter, and the new state of the emitter as particlefx.EMITTER_STATE_.
```
local function emitter_state_change(self, id, emitter, state)
  if emitter == hash("exhaust") and state == particlefx.EMITTER_STATE_POSTSPAWN then
    -- exhaust is done spawning particles...
  end
end

function init(self)
    particlefx.play("#particlefx", emitter_state_change)
end

```

### particlefx.reset_constant
*Type:* FUNCTION
Resets a shader constant for a particle FX component emitter.
The constant must be defined in the material assigned to the emitter.
Resetting a constant through this function implies that the value defined in the material will be used.
Which particle FX to reset a constant for is identified by the URL.

**Parameters**

- `url` (string | hash | url) - the particle FX that should have a constant reset
- `emitter` (string | hash) - the id of the emitter
- `constant` (string | hash) - the name of the constant

**Examples**

The following examples assumes that the particle FX has id "particlefx", it
contains an emitter with the id "emitter" and that the default-material in builtins is used, which defines the constant "tint".
If you assign a custom material to the sprite, you can reset the constants defined there in the same manner.
How to reset the tinting of particles from an emitter:
```
function init(self)
    particlefx.reset_constant("#particlefx", "emitter", "tint")
end

```

### particlefx.set_constant
*Type:* FUNCTION
Sets a shader constant for a particle FX component emitter.
The constant must be defined in the material assigned to the emitter.
Setting a constant through this function will override the value set for that constant in the material.
The value will be overridden until particlefx.reset_constant is called.
Which particle FX to set a constant for is identified by the URL.

**Parameters**

- `url` (string | hash | url) - the particle FX that should have a constant set
- `emitter` (string | hash) - the id of the emitter
- `constant` (string | hash) - the name of the constant
- `value` (vector4) - the value of the constant

**Examples**

The following examples assumes that the particle FX has id "particlefx", it
contains an emitter with the id "emitter" and that the default-material in builtins is used, which defines the constant "tint".
If you assign a custom material to the sprite, you can reset the constants defined there in the same manner.
How to tint particles from an emitter red:
```
function init(self)
    particlefx.set_constant("#particlefx", "emitter", "tint", vmath.vector4(1, 0, 0, 1))
end

```

### particlefx.stop
*Type:* FUNCTION
Stops a particle FX component from playing.
Stopping a particle FX does not remove already spawned particles.
Which particle FX to stop is identified by the URL.

**Parameters**

- `url` (string | hash | url) - the particle fx that should stop playing
- `options` (particlefx.stop_options) (optional) - options used when stopping the particle fx

**Examples**

How to stop a particle fx when a game object is deleted and immediately also clear
any spawned particles:
```
function final(self)
    particlefx.stop("#particlefx", { clear = true })
end

```

### particlefx.stop_options
*Type:* STRUCT
Options used when stopping particle effects.

**Members**

- `clear?` (boolean) - Instantly clear spawned particles.
