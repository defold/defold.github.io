# Unlit

This example demonstrates how to create and apply an custom non-lit material to a 3D model.

Source: [https://github.com/defold/examples/tree/master/material/unlit](https://github.com/defold/examples/tree/master/material/unlit)

In industry-established terms, a material that is not affected by lighting is called "unlit" or "non-lit". It is used to create retro-style graphics or for effects that should not depend on lighting (headlights, lamps).

This example contains a game object with a model that has an `unlit` material applied to it. The material is assigned custom vertex and fragment shaders. The shader is very simple and just transfers the texture color to the model. This is an excellent starting point for creating new materials and for creating effects that do not depend on lighting. The shaders are written in GLSL 1.40, which is available from Defold 1.9.2.

The model used in this example is from Kenney's [Train Pack](https://kenney.nl/assets/train-kit), licensed under CC0.

## Scripts

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
