# Multiple Sprite Samplers

This example shows how to sample from more than one image when drawing a sprite

Source: [https://github.com/defold/examples/tree/master/sprite/samplers](https://github.com/defold/examples/tree/master/sprite/samplers)

The example uses a sprite with a material with two samplers:



The samplers are assigned to two atlases, `one.atlas` and `two.atlas`:



Each atlas contains a Defold logo:





Note the rename pattern in `two.atlas`. The rename pattern is required so that it is possible to sample from the same location in both atlases. 

The color data from the two samplers is mixed/interpolated in the fragment program to produce a final color. The amount of interpolation is controlled in the `mix_amount` fragment constant. The `mix_amount` is animated between 0.0 and 1.0 in the `multi_sample.script`

## Scripts

### multi_sample.script

```lua
function init(self)
	go.animate("logo#sprite", "mix_amount.x", go.PLAYBACK_LOOP_PINGPONG, 1.0, go.EASING_INOUTQUAD, 2)
end
```

### multi_sample_sprite.fp

```glsl
varying mediump vec2 var_texcoord0;

uniform lowp sampler2D texture1_sampler;
uniform lowp sampler2D texture2_sampler;
uniform lowp vec4 tint;
uniform lowp vec4 mix_amount;

void main()
{
    // Pre-multiply alpha since all runtime textures already are
    lowp vec4 tint_pm = vec4(tint.xyz * tint.w, tint.w);
    // sample from both textures
    lowp vec4 color1 = texture2D(texture1_sampler, var_texcoord0.xy);
    lowp vec4 color2 = texture2D(texture2_sampler, var_texcoord0.xy);
    // mix (interpolate) the colors by the mix_amount
    lowp vec4 colormix = mix(color1, color2, mix_amount.x);
    // apply tint
    gl_FragColor = colormix * tint_pm;
}
```
