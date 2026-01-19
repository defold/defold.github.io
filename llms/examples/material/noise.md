# Noise shader

This example shows how to use a noise function to generate clouds, smoke or similar effect using a shader.

Source: [https://github.com/defold/examples/tree/master/material/noise](https://github.com/defold/examples/tree/master/material/noise)

This example contains a game object with a model component. The model component uses the `/builtins/assets/meshes/quad.dae` mesh, which is a rectangle 1 by 1 unit large. The game object is scaled to the dimensions of the screen so that the mesh covers the entire screen.



The shader applies multiple layers of noise to the uv coordinate to create a two dimensional flowing cloud or smoke like look. The shader also receives a time value from `noise.script` and applies this in the calculation to apply movement to the visual effect.

## Scripts

### noise.script

```lua
function init(self)
	self.time = 0
end

function update(self, dt)
	self.time = self.time + dt
	-- set the x component of the 'time' fragment constant in the material
	go.set("#model", "time.x", self.time)
end
```

### noise.fp

```glsl
#version 140

in mediump vec2 var_texcoord0;

uniform fs_uniforms
{
    mediump vec4 time;
};

out mediump vec4 out_fragColor;

// noise shader from https://www.shadertoy.com/view/XXBcDz

// pseudo random generator (white noise)
float rand(vec2 n)
{ 
    return fract(sin(dot(n, vec2(12.9898, 78.233))) * 43758.5453);
}

// value noise
float noise(vec2 p)
{
    vec2 ip = floor(p);
    vec2 u = fract(p);
    u = u * u * (3.0 - 2.0 * u);

    float x = mix(rand(ip),                  rand(ip + vec2(1.0, 0.0)), u.x);
    float y = mix(rand(ip + vec2(0.0, 1.0)), rand(ip + vec2(1.0, 1.0)), u.x);
    float a = u.y;
    float res = mix(x, y, a);
    return res * res;
}

// used to rotate domain of noise function
const mat2 rot = mat2( 0.80,  0.60, -0.60,  0.80 );

// fast implementation
float fbm( vec2 p )
{
    float f = 0.0;
    f += 0.500000 * noise( p ); p = rot * p * 2.02;
    f += 0.031250 * noise( p ); p = rot * p * 2.01;
    f += 0.250000 * noise( p ); p = rot * p * 2.03;
    f += 0.125000 * noise( p + 0.1 * sin(time.x) + 0.8 * time.x ); p = rot * p * 2.01;
    f += 0.062500 * noise( p + 0.3 * sin(time.x) ); p = rot * p * 2.04;
    f += 0.015625 * noise( p );
    return f / 0.96875;
}
    
void main()
{  
    float n = fbm(var_texcoord0.xy);
    out_fragColor = vec4(n, n, n, 1.0);
}
```
