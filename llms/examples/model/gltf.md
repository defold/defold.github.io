# GLTF - Infinite Track

This example shows how to use glTF models to build an infinite scrolling track.

[Project files](https://github.com/defold/examples/tree/master/model/gltf)

This example uses three glTF model assets from Kenney's Toy Car Kit to build a small endless road scene. The car stays in place while the road segments move forward and loop behind it.

## What You'll Learn

- How to place multiple glTF model components in one collection
- How to loop repeated road segments to fake an infinite track
- How the unlit material works

## Setup

The collection contains three game objects: `car`, `camera`, and `track`.

`car` uses `vehicle-racer.glb` with the unlit material and the shared `colormap.png` texture.

`camera` is a perspective camera positioned so the car and road stay in view.

`track` contains six copies of `track-road-wide-straight.glb` and a `gate.glb` model. `gltf.script` moves the whole game object along the Z axis and wraps it back to the start once the last road section passes the camera.

## How It Works

The script keeps a single Z position in `self.current_z`. Every frame it advances that value by `self.speed * dt`, then applies it to the `track` game object.

Once the track reaches the loop point, the script subtracts the loop length and starts again. That creates the illusion of a long road without needing to spawn or destroy any models.

The unlit material using two shaders `unlit.vp` and `unlit.fp`.

This gives a unique look to the models by omitting any lighting calculations and showing just the albedo color from the textures for the models, check out the comparison with a default built-in model material (on the left):

## Credits

The models used in this example are from Kenney's [Toy Car Kit](https://kenney.nl/assets/toy-car-kit), licensed under CC0.

## Scripts

### gltf.script

```lua
local TRACK_PART_COUNT = 6
local TRACK_PART_SIZE = 4

function init(self)
	self.current_z = 0 -- <1>
	self.loop_at_z = TRACK_PART_SIZE * (TRACK_PART_COUNT - 2) -- <2>
	self.speed = 5 -- <3>
end

function update(self, dt)
	self.current_z = self.current_z + self.speed * dt -- <4>
	if self.current_z > self.loop_at_z then -- <5>
		self.current_z = self.current_z - self.loop_at_z
	end
	go.set("/track", "position.z", self.current_z) -- <6>
end

--[[
1. Start the track at Z = 0.
2. Precompute the distance before the road should loop back.
3. Set the scrolling speed of the whole track.
4. Move the track forward every frame using delta time.
5. Wrap the track when it reaches the end of the visible road.
6. Apply the updated position to the `track` game object.
]]
```

### unlit.fp

```glsl
#version 140

// Inputs should match the vertex shader's outputs.
in vec2 var_texcoord0;

// The texture to sample.
uniform lowp sampler2D texture0;

// The final color of the fragment.
out lowp vec4 final_color;

uniform fs_uniforms
{
    mediump vec4 tint;
};

void main()
{
    // Pre-multiply alpha since all runtime textures already are
    vec4 tint_pm = vec4(tint.xyz * tint.w, tint.w);

    // Sample the texture at the fragment's texture coordinates.
    vec4 color = texture(texture0, var_texcoord0.xy) * tint_pm;

    // Output the sampled color.
    final_color = color;
}
```

### unlit.vp

```glsl
#version 140

// The model's vertex position and texture coordinates.
in vec4 position;
in vec2 texcoord0;

// The model's world matrix.
in mat4 mtx_world;

// The projection and view matrices.
uniform general_vp
{
    mat4 mtx_view;
    mat4 mtx_proj;
};

// The output of a vertex shader are passed to the fragment shader.
// The texture coordinates of the vertex.
out vec2 var_texcoord0;

void main()
{
    // Pass the texture coordinates to the fragment shader.
    var_texcoord0 = texcoord0;

    // Transform the vertex position to clip space.
    gl_Position = mtx_proj * mtx_view * mtx_world * vec4(position.xyz, 1.0);
}
```
