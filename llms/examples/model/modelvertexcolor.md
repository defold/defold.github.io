# Model Vertex Color

This example demonstrates how to apply a vertex color shader using exported attributes from a 3D model.

Source: [https://github.com/defold/examples/tree/master/model/modelvertexcolor](https://github.com/defold/examples/tree/master/model/modelvertexcolor)

Vertex color attributes are usually made up as a vector4 of floats represented as rgba(red, green, blue, alpha) channels. They can be applied to 3d models and exported from many 3d editor applications and are commonly used in games for many effects. This example we are displaying a 3d model with vertex color attribute through a shader. No textures or uv's are used to display the colors.

A game object with a model that has a `vertexcolor` material applied to it. The material is assigned custom vertex and fragment shaders. The shader is very simple and just transfers the vertex color data from the model to the vertex and fragment program to display them. The shaders are written in GLSL 1.40, which is available from Defold 1.9.2.

## Scripts

### vertexcolor.vp

```glsl
#version 140

// Models vertex color attribute comes in as rgba floats (vec4)
in vec4 color;

// The model's vertex position.
in vec4 position;

// The model's world matrix.
in mat4 mtx_world;

// The projection and view matrices.
uniform general_vp
{
    mat4 mtx_view;
    mat4 mtx_proj;
};

// The output of a vertex shader are passed to the fragment shader.
out vec4 vertex_color;

void main()
{
    // Setting the vertex colors to the passed varying.
    vertex_color = color;

    // Transform the vertex position to clip space.
    gl_Position = mtx_proj * mtx_view * mtx_world * vec4(position.xyz, 1.0);
}
```

### vertexcolor.fp

```glsl
#version 140

// Inputs should match the vertex shader's outputs.
in vec4 vertex_color;

// The final color of the fragment.
out lowp vec4 final_color;

uniform fs_uniforms
{
    mediump vec4 tint;
};

void main()
{
    // brightening up the displayed vertex colors
    lowp float brightness = 0.1;
    // Pre-multiply alpha for tint
    vec4 tint_pm = vec4(tint.xyz * tint.w, tint.w);

    // Sample the vertex color from vertices, add a little brightness with tint.
    vec4 color = vertex_color + brightness * tint_pm ;

    // Output the sampled color.
    final_color = color;
}
```
