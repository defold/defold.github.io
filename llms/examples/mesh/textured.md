# Textured Mesh

This example shows how to create a textured mesh component in the shape of a rectangle.

[Project files](https://github.com/defold/examples/tree/master/mesh/textured)

This example contains a game object with a mesh component in the shape of a rectangle (quad). The quad is defined in `quad.buffer` as the four points (triangle strip) in the `position` stream. The triangle also defines the texture coordinate (UV) at each point.
```
[
    {
        "name": "position",
        "type": "float32",
        "count": 3,
        "data": [
            -0.5, -0.5, 0,
             0.5, -0.5, 0,
            -0.5,  0.5, 0,
             0.5,  0.5, 0
        ]
    },
    {
        "name": "texcoord0",
        "type": "float32",
        "count": 2,
        "data": [
            0.0, 0.0,
            1.0, 0.0,
            0.0, 1.0,
            1.0, 1.0
        ]
    }
]
```

Texture by [Kenney.nl](https://kenney.nl/assets/prototype-textures)

## Scripts

### texturedmesh.fp

```glsl
#version 140

in highp vec4 var_position;
in mediump vec2 var_texcoord0;

out vec4 out_fragColor;

uniform mediump sampler2D tex0;

uniform fs_uniforms
{
	mediump vec4 tint;
};

void main()
{
	// Pre-multiply alpha since all runtime textures already are
	vec4 tint_pm = vec4(tint.xyz * tint.w, tint.w);

	vec4 color = texture(tex0, var_texcoord0) * tint_pm;

	out_fragColor = vec4(color.rgb, 1.0);
}
```

### texturedmesh.vp

```glsl
#version 140

// Positions can be world or local space, since world and normal
// matrices are identity for world vertex space materials.
// If world vertex space is selected, you can remove the
// normal matrix multiplication for optimal performance.

in highp vec4 position;
in mediump vec2 texcoord0;

out highp vec4 var_position;
out mediump vec2 var_texcoord0;

uniform vs_uniforms
{
	uniform mediump mat4 mtx_worldview;
	uniform mediump mat4 mtx_proj;
	uniform mediump mat4 mtx_view;
};

void main()
{
	vec4 p = mtx_worldview * vec4(position.xyz, 1.0);
	var_position = p;
	var_texcoord0 = texcoord0;
	gl_Position = mtx_proj * p;
}
```
