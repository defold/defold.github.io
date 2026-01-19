# Screenspace

This example shows how to create a custom material with two textures that blend together to create a pattern effect using screen space coordinates.

Source: [https://github.com/defold/examples/tree/master/material/screenspace](https://github.com/defold/examples/tree/master/material/screenspace)

In this example, we create a new material for 3D models in which we convert vertex coordinates to screenspace to get a special effect. It may be called "surface fill", "screenspace fill" and is used, most often in combination with outlines, to highlight objects in 3D games or indicate their status. 

We added two game objects and two models to which we assigned our new `screenspace` material. The material is based on [`unlit`](/examples/material_unlit/), but in it:
- vertex shader: we added a conversion of the clip space position to the screen position to pass that value to the fragment shader.
- fragment shader: we added sampling the color based on screenspace coordinates and blending into the final output color.
- material properties: we added a new sampler to set a second texture to be used as a pattern, and user-defined uniforms to control the fragment shader.

The last important thing is to pass the screen size to the shader to adjust the aspect ratio:

```lua
local w, h = window.get_size()
go.set("#model", "screen_size", vmath.vector4(w, h, 0, 0))
```

The shaders are written in GLSL 1.40, which is available from Defold 1.9.2. The model used in this example is from Kenney's [Prototype Pack](https://kenney.nl/assets/prototype-kit), licensed under CC0.

## Scripts

### screenspace.script

```lua
function init(self)
	self.time = 0 -- for pattern animation

	-- The model with the pattern - we enabled the effect, 0.5 is the intensity (alpha)
	go.set("/crate_selected#model", "pattern_opts.x", 0.5)
	-- + add 70 degrees to the rotation
	go.set("/crate_selected#model", "pattern_opts.w", math.rad(70))

	-- The normal model - the 0.0 value disables the effect
	go.set("/crate#model", "pattern_opts.x", 0)
end

function update(self, dt)
	-- Animate the pattern by changing the z value
	self.time = self.time - dt
	go.set("/crate_selected#model", "pattern_opts.z", self.time)

	-- The shader uses the screen size to calculate the aspect ratio.
	-- In a real game, you'd set this in the render script globally for all materials.
	local w, h = window.get_size()
	go.set("/crate_selected#model", "screen_size", vmath.vector4(w, h, 0, 0))
end
```

### screenspace.vp

```glsl
#version 140

// The model's vertex position and texture coordinates.
in vec4 position;
in vec2 texcoord0;

// The projection, view and world matrices.
uniform general_vp
{
    mat4 mtx_world;
    mat4 mtx_view;
    mat4 mtx_proj;
};

// The output of a vertex shader are passed to the fragment shader.
// The texture coordinates of the vertex.
out vec2 var_texcoord0;

// The screen texture coordinates of the vertex.
out vec4 var_screen_texcoord;

// Converts the clip space position to the screen position.
vec4 clip_to_screen(vec4 pos)
{
    // Position is [-w,w], convert to [-0.5w,0.5w]
    vec4 o = pos * 0.5;

    // Convert from [-0.5w + 0.5w,0.5w + 0.5w] to [0,w]
    o.xy = vec2(o.x, o.y) + o.w;

    // Keep "zw" as it is
    o.zw = pos.zw;
    return o;
}

void main()
{
    // Pass the texture coordinates to the fragment shader.
    var_texcoord0 = texcoord0;

    // Transform the vertex position to clip space.
    vec4 vertex_pos = mtx_proj * mtx_view * mtx_world * vec4(position.xyz, 1.0);
    gl_Position = vertex_pos;

    // Convert the clip space position to the screen position and pass the value to the fragment shader.
    var_screen_texcoord = clip_to_screen(vertex_pos);
}
```

### screenspace.fp

```glsl
#version 140

// Inputs should match the vertex shader's outputs.
in vec2 var_texcoord0;
in vec4 var_screen_texcoord;

// The color texture.
uniform lowp sampler2D texture0;
// The pattern texture.
uniform lowp sampler2D texture_pattern;

// The user defined uniforms.
uniform user_fp
{
    // pattern_opts.x - alpha, default 1.0 (set 0.0 to disable the screen space effect).
    // pattern_opts.y - scale, default 30.0.
    // pattern_opts.z - offset by x, default 0.0.
    // pattern_opts.w - rotation in radians.
    vec4 pattern_opts;

    // The screen size, used to calculate the aspect ratio.
    vec4 screen_size;
};

// The final color of the fragment.
out lowp vec4 final_color;

// Rotate 2D vector "v" by the "a" angle in radians
vec2 rotate(vec2 v, float a)
{
    float s = sin(a);
    float c = cos(a);
    return mat2(c, s, -s, c) * v;
}

void main()
{
    // Sample the color texture at the fragment's texture coordinates.
    vec4 color = texture(texture0, var_texcoord0.xy);

    // Counteract the perspective correction and scale the coords.
    vec2 pattern_coord = (var_screen_texcoord.xy / var_screen_texcoord.w) * pattern_opts.y;
    // + Correct the aspect ratio
    float aspect = screen_size.x / screen_size.y;
    pattern_coord.x *= aspect;
    // + Offset the grid horizontally
    pattern_coord.x += pattern_opts.z;
    // + Rotate
    pattern_coord = rotate(pattern_coord, pattern_opts.w);

    // Output the sampled color
    if (pattern_opts.x > 0.0)
    {
        // Sample the pattern at the screen space texture coordinates.
        vec4 pattern_color = texture(texture_pattern, pattern_coord);

        // Blend the colors: (sRGBA*1) + (dRGBA*(1-sA))
        final_color = pattern_color * pattern_opts.x + color * (1.0 - (pattern_color.a * pattern_opts.x));
    }
    else
    {
        // No pattern, just output the color.
        final_color = color;
    }
}
```
