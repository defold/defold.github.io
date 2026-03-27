# ParticleFX emitter properties

This example shows how to get and set ParticleFX emitter image, animation, and material at runtime.

[Project files](https://github.com/defold/examples/tree/master/particles/particlefx_set_get)

Since Defold 1.12.2 you can use `go.get()` and `go.set()` on individual ParticleFX emitters by passing `keys = { "..." }`.

This example focuses on this feature. It toggles a ParticleFX between two setups and shows the properties of the active emitters in the labels.

## Setup

1. Example consists of one game object in the collection having:

   - script `particlefx_set_get.script`
   - ParticleFX component named `#particles`
   - 2 label components: `#label_core` and `#label_spark`

2. The ParticleFX:

   - has two emitters: `emitter_top` and `emitter_bottom`

3. The script has the resources exposed as properties:

   - `particles_atlas`
   - `sprites_atlas`
   - `default_material`
   - `glow_material`

   This makes it easy to switch the emitter `image` and `material` directly from code.

4. The example uses 2 atlases with given animations:

   - the `particles.atlas` with `coin` and `smoke` animations
   - the `sprites.atlas` with `ship_red` and `ship_dark` animations

The atlases are set up to contain the animation ids used by the script, so the example can switch between the two setups without extra transition logic.

## How it works

The script keeps two hardcoded setups and toggles between them whenever you click or tap:

1. `particles.atlas` + glow material
   `emitter_top` uses `coin`
   `emitter_bottom` uses `smoke`
2. `sprites.atlas` + default particle material
   `emitter_top` uses `ship_red`
   `emitter_bottom` uses `ship_dark`

When the setup changes, the script:

1. stops the ParticleFX
2. calls `set_emitter_properties()` for each emitter to set `image`, `animation`, and `material`
3. calls `get_emitter_properties()` to read the current values back with `go.get()`
4. writes the values into the two labels
5. plays the ParticleFX again

The helper function `set_emitter_properties()` applies properties per emitter by passing the emitter id in `keys`:
```lua
go.set("#particles", "image", image, { keys = { "emitter_top" } })
go.set("#particles", "animation", animation, { keys = { "emitter_top" } })
go.set("#particles", "material", material, { keys = { "emitter_top" } })
```

The helper function `get_emitter_properties()` uses the same `keys` pattern with `go.get()` and writes the result into the labels, so the example shows which values are currently active for each emitter.

One important limitation: **emitter property changes only affect the next play**. That is why the script stops and plays the ParticleFX around each property update.

## Scripts

### particlefx_set_get.script

```lua
-- Properties - 2 atlases:
go.property("particles_atlas", resource.atlas("/assets/particles.atlas"))
go.property("sprites_atlas", resource.atlas("/assets/sprites.atlas"))

-- Properties - 2 materials:
go.property("default_material", resource.material("/builtins/materials/particlefx.material"))
go.property("glow_material", resource.material("/example/particlefx_glow.material"))

-- Address of the particlefx component:
local PARTICLEFX = "#particles"

-- The example only switches between two simple atlas setups,
-- so each atlas gets one animation per emitter.
local ANIMATIONS = {
	["particles_atlas"] = { hash("coin"), hash("smoke") },
	["sprites_atlas"] = { hash("ship_red"), hash("ship_dark") }
}

-- Read the current emitter properties back from the particlefx component
-- and show them in the on-screen labels.
local function get_emitter_properties(emitter, url)
	local image = go.get(PARTICLEFX, "image", { keys = { emitter } })
	local animation = go.get(PARTICLEFX, "animation", { keys = { emitter } })
	local material = go.get(PARTICLEFX, "material", { keys = { emitter } })

	-- Show the properties in the label:
	label.set_text(url, emitter .. ":\nimage: " .. image
		.. "\nanimation: " .. animation .. "\nmaterial: " .. material )
end

-- Apply one full property set to a single emitter.
local function set_emitter_properties(emitter, image, animation, material)
	go.set(PARTICLEFX, "image", image, { keys = { emitter } })
	go.set(PARTICLEFX, "animation", animation, { keys = { emitter } })
	go.set(PARTICLEFX, "material", material, { keys = { emitter } })
end

-- Toggle between the two hardcoded setups:
-- particles atlas + glow material, or sprites atlas + default material.
local function change_particlefx_properties(self)
	particlefx.stop(PARTICLEFX)

	local core_animation = ANIMATIONS["particles_atlas"][1]
	local spark_animation = ANIMATIONS["particles_atlas"][2]

	if self.atlas == self.particles_atlas then
		self.atlas = self.sprites_atlas
		self.material = self.default_material
		core_animation = ANIMATIONS["sprites_atlas"][1]
		spark_animation = ANIMATIONS["sprites_atlas"][2]
	else
		self.atlas = self.particles_atlas
		self.material = self.glow_material
	end

	pprint(core_animation, spark_animation, self.atlas, self.material)

	-- Both emitters use the same atlas/material for a given setup,
	-- but each emitter gets its own animation.
	set_emitter_properties("emitter_top", self.atlas, core_animation, self.material)
	set_emitter_properties("emitter_bottom", self.atlas, spark_animation, self.material)

	get_emitter_properties("emitter_top", "#label_core")
	get_emitter_properties("emitter_bottom", "#label_spark")

	particlefx.play(PARTICLEFX)
end

function init(self)
	msg.post(".", "acquire_input_focus")

	-- Start with sprites/default so the first click flips to particles/glow.
	self.atlas = self.sprites_atlas
	self.material = self.default_material

	change_particlefx_properties(self)
end

function on_input(self, action_id, action)
	-- Toggle the setup on touch release.
	if action_id == hash("touch") and action.released then
		change_particlefx_properties(self)
	end
end
```

### particlefx_glow.fp

```glsl
#version 140

in mediump vec2 var_texcoord0;
in mediump vec4 var_color;

out vec4 out_fragColor;

uniform mediump sampler2D texture_sampler;

uniform fs_uniforms
{
    mediump vec4 tint;
};

void main()
{
    mediump vec4 tint_pm = vec4(tint.xyz * tint.w, tint.w);
    mediump vec4 base = texture(texture_sampler, var_texcoord0.xy) * var_color * tint_pm;
    mediump float energy = max(max(base.r, base.g), base.b);
    mediump vec3 glow = vec3(0.9, 1.4, 1.8) * energy;
    out_fragColor = vec4(base.rgb * 0.2 + glow, base.a);
}
```
