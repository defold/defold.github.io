# UV Gradient

This example shows how to apply a basic shader to a full screen quad.

Source: [https://github.com/defold/examples/tree/master/material/uvgradient](https://github.com/defold/examples/tree/master/material/uvgradient)

This example contains a game object with a model component. The model component uses the `/builtins/assets/meshes/quad.dae` mesh, which is a rectangle 1 by 1 unit large. The game object is scaled to the dimensions of the screen so that the mesh covers the entire screen.



The shader is very basic and sets the fragment color based on the UV position, thus creating a color gradient. This is a good starting point when experimenting with graphical effects using a shader.

## Scripts

### uvgradient.fp

```glsl
varying mediump vec2 var_texcoord0;

void main()
{  
    gl_FragColor = vec4(var_texcoord0.x, var_texcoord0.y, 0.5, 1.0f);
}
```
