# Mesh

This example shows how to create a basic mesh component in the shape of a triangle.

Source: [https://github.com/defold/examples/tree/master/mesh/triangle](https://github.com/defold/examples/tree/master/mesh/triangle)

This example contains a game object with a mesh component in the shape of a triangle. The triangle is defined in `triangle.buffer` as the three points of the triangle in the `position` stream. The triangle also defines the colors at each point. The colors get mixed automatically when the triangle is drawn by the shader.

```
[
    {
        "name": "position",
        "type": "float32",
        "count": 3,
        "data": [
            -0.5, -0.5, 0,
            0.5, -0.5, 0,
            0.0, 0.5, 0
        ]
    },
    {
        "name": "color0",
        "type": "float32",
        "count": 4,
        "data": [
            0, 1, 0, 1,
            1, 0, 0, 1,
            0, 0, 1, 1
        ]
    }
]
```

## Scripts

### mesh.fp

```glsl
varying mediump vec4 var_color;

void main()
{
	gl_FragColor = var_color;
}
```

### mesh.vp

```glsl
uniform mediump mat4 mtx_worldview;
uniform mediump mat4 mtx_proj;

attribute mediump vec4 position;
attribute mediump vec4 color0;

varying mediump vec4 var_color;

void main()
{
	gl_Position = mtx_proj * mtx_worldview * vec4(position.xyz, 1.0);
	var_color = color0;
}
```
