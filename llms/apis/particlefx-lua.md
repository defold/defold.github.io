# Particle effects

**Namespace:** `particlefx`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_particlefx.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_particlefx.cpp`

Functions for controlling particle effect component playback and
shader constants.

## API

### particlefx.EMITTER_STATE_POSTSPAWN
*Type:* CONSTANT
The emitter is not spawning any particles, but has particles that are still alive.

### particlefx.EMITTER_STATE_PRESPAWN
*Type:* CONSTANT
The emitter will be in this state when it has been started but before spawning any particles. Normally the emitter is in this state for a short time, depending on if a start delay has been set for this emitter or not.

### particlefx.EMITTER_STATE_SLEEPING
*Type:* CONSTANT
The emitter does not have any living particles and will not spawn any particles in this state.

### particlefx.EMITTER_STATE_SPAWNING
*Type:* CONSTANT
The emitter is spawning particles.

### particlefx.play
*Type:* FUNCTION
Starts playing a particle FX component.
Particle FX started this way need to be manually stopped through particlefx.stop().
Which particle FX to play is identified by the URL.
 A particle FX will continue to emit particles even if the game object the particle FX component belonged to is deleted. You can call particlefx.stop() to stop it from emitting more particles.

**Parameters**

- `url` (string | hash | url) - the particle fx that should start playing.
- `emitter_state_function` (function(self, id, emitter, state)) (optional) - optional callback function that will be called when an emitter attached to this particlefx changes state.
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The current object</dd>
<dt><code>id</code></dt>
<dd><span class="type">hash</span> The id of the particle fx component</dd>
<dt><code>emitter</code></dt>
<dd><span class="type">hash</span> The id of the emitter</dd>
<dt><code>state</code></dt>
<dd><span class="type">constant</span> the new state of the emitter:</dd>
</dl>
<ul>
<li><code>particlefx.EMITTER_STATE_SLEEPING</code></li>
<li><code>particlefx.EMITTER_STATE_PRESPAWN</code></li>
<li><code>particlefx.EMITTER_STATE_SPAWNING</code></li>
<li><code>particlefx.EMITTER_STATE_POSTSPAWN</code></li>
</ul>

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
- `options` (table) (optional) - Options when stopping the particle fx. Supported options:
<ul>
<li><span class="type">boolean</span> <code>clear</code>: instantly clear spawned particles</li>
</ul>

**Examples**

How to stop a particle fx when a game object is deleted and immediately also clear
any spawned particles:
```
function final(self)
    particlefx.stop("#particlefx", { clear = true })
end

```
