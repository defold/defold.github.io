# Morph Target Animation

Shows how to play glTF morph target animations with a morph-capable model material.

[Project files](https://github.com/defold/examples/tree/master/model/morph-target)

This example plays morph target animations from a glTF model. The model uses a small custom material based on Defold's built-in model material, with the extra shader bindings needed to render morph target deformation.

## What You'll Learn

- How to use a glTF file that contains morph targets and weight animations
- How to play a named model animation with `model.play_anim()`
- How to cycle between several morph target animations with input
- How to create a model material to apply morph target data

## Setup

The collection contains one camera and one `morph_target` game object.

`morph_target`
: Contains a Model component, `morph_target.script`, and `info.gui`. The Model component uses `/assets/models/MorphStressTest.glb` for mesh, skeleton, and animation data. The glTF file contains eight morph targets and three animations: `TheWave`, `Pulse`, and `Individuals`.

`camera`
: Contains a perspective Camera component positioned above and in front of the model.

`info`
: Contains a GUI component with instructions for the example.

The glTF model has two material slots, `Base` and `TestMaterial`. Both slots use `/assets/materials/morph_target.material`; the blue and orange textures only make the two parts of the model easier to distinguish. Custom material has vertex constants `morph_targets_weights` of type `User` for applying weighted morph targets.

## How It Works

`morph_target.script` stores the animation names in a small table. In `init()`, it acquires input focus and starts `TheWave` with:
```lua
model.play_anim("#model", "TheWave", go.PLAYBACK_LOOP_FORWARD)
```

The animations in the glTF file target the model's morph weights. As the animation plays, Defold updates the material constant named `morph_targets_weights` and binds the model's morph target texture to the material sampler named `morph_targets`.

The stock model material is useful as a starting point, but it does not apply morph target deltas by itself. This example therefore uses `/assets/materials/morph_target.material`, which declares the expected morph target bindings and uses `/assets/materials/morph_target.vp` to sample the morph target texture. The vertex shader reads the active weights, samples the position delta for each target, and adds the weighted result to the base vertex position before projection.

When you click or touch the screen, `on_input()` advances to the next animation name and calls `model.play_anim()` again. The example loops through `TheWave`, `Pulse`, and `Individuals`.

## Credits

The `MorphStressTest.glb` asset is CC-BY 4.0, Copyright 2021 Analytical Graphics, Inc. Model by Ed Mackey.
[https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main/Models/MorphStressTest](https://github.com/KhronosGroup/glTF-Sample-Assets/tree/main/Models/MorphStressTest)

## Scripts

### morph_target.script

```lua
local ANIMATIONS = {
	"TheWave",
	"Pulse",
	"Individuals"
}

function init(self)
	self.animation = 1
	msg.post("#", "acquire_input_focus")
	model.play_anim("#model", ANIMATIONS[self.animation], go.PLAYBACK_LOOP_FORWARD) -- <1>
end

function on_input(self, action_id, action)
	if action.pressed then
		self.animation = self.animation + 1
		if self.animation > 3 then
			self.animation = 1
		end
		model.play_anim("#model", ANIMATIONS[self.animation], go.PLAYBACK_LOOP_FORWARD)
	end
end

--[[
1. Play the morph target animation named "TheWave" from the glTF file in a loop.
]]
```

### morph_target.vp

```glsl
#version 140

in highp vec4 position;
in mediump vec2 texcoord0;
in mediump vec3 normal;

out highp vec4 var_position;
out mediump vec3 var_normal;
out mediump vec2 var_texcoord0;
out mediump vec4 var_light;

uniform vs_uniforms
{
    mediump mat4 mtx_worldview;
    mediump mat4 mtx_view;
    mediump mat4 mtx_proj;
    mediump mat4 mtx_normal;
    mediump vec4 light;
    mediump vec4 morph_targets_weights[2];
};

uniform sampler2DArray morph_targets;

vec2 get_morph_uv(int index, int width, int height)
{
    int x = index % width;
    int y = index / width;

    return vec2(
        (float(x) + 0.5) / float(width),
        (float(y) + 0.5) / float(height)
    );
}

void apply_weighted_morph_target(in vec2 uv, in float weight, inout vec3 p, in int target)
{
    if (weight == 0.0) {
        return;
    }

    int pos_layer = target * 3;
    p += weight * texture(morph_targets, vec3(uv, pos_layer)).xyz;
}

vec3 get_morph_position_delta(int vertex_index)
{
    vec3 position_delta = vec3(0.0);

#ifndef EDITOR
    ivec3 morph_texture_size = textureSize(morph_targets, 0);
    vec2 uv = get_morph_uv(vertex_index, morph_texture_size.x, morph_texture_size.y);

    apply_weighted_morph_target(uv, morph_targets_weights[0].x, position_delta, 0);
    apply_weighted_morph_target(uv, morph_targets_weights[0].y, position_delta, 1);
    apply_weighted_morph_target(uv, morph_targets_weights[0].z, position_delta, 2);
    apply_weighted_morph_target(uv, morph_targets_weights[0].w, position_delta, 3);
    apply_weighted_morph_target(uv, morph_targets_weights[1].x, position_delta, 4);
    apply_weighted_morph_target(uv, morph_targets_weights[1].y, position_delta, 5);
    apply_weighted_morph_target(uv, morph_targets_weights[1].z, position_delta, 6);
    apply_weighted_morph_target(uv, morph_targets_weights[1].w, position_delta, 7);
#endif

    return position_delta;
}

void main()
{
    vec3 morphed_position = position.xyz + get_morph_position_delta(gl_VertexIndex);
    vec4 p = mtx_worldview * vec4(morphed_position, 1.0);

    var_light = mtx_view * vec4(light.xyz, 1.0);
    var_position = p;
    var_texcoord0 = texcoord0;
    var_normal = normalize((mtx_normal * vec4(normal, 0.0)).xyz);
    gl_Position = mtx_proj * p;
}
```
