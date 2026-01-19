# Sprite local UV

This example shows how to get local UV coordinates of a sprite regardless of sprite size

Source: [https://github.com/defold/examples/tree/master/material/sprite_local_uv](https://github.com/defold/examples/tree/master/material/sprite_local_uv)

The example uses two game objects, each with a sprite component and a script.



The sprite component uses a custom sprite material `sprite_local_uv.material` with `local_position` and `sprite_size` as two vertex attributes. The `local_position` attribute is of semantic type "Position" and coordinate space "Local" while the `sprite_size` attribute is of semantic type "User" and will be set by the script.



The script gets the size of the sprite and sets it as the `sprite_size` vertex attribute.

## Scripts

### sprite_local_uv.script

```lua
function init(self)
	-- get the sprite size from the sprite component propertry 'size'
	local size = go.get("#sprite", "size")

	-- set the size on the sprite material in the custom vertex attribute 'sprite_size'
	go.set("#sprite", "sprite_size", size)

	-- rotate the sprite
	go.animate(".", "euler.z", go.PLAYBACK_LOOP_FORWARD, 360, go.EASING_LINEAR, 5)
end
```

### sprite_local_uv.vp

```glsl
#version 140

// positions are in world space
in highp vec4 position;
in mediump vec2 texcoord0;

// position in local space
in highp vec2 position_local;
// size of sprite in pixels
in mediump vec2 sprite_size;

out mediump vec2 var_texcoord0;
out highp vec2 var_position_local;

uniform vs_uniforms
{
    highp mat4 view_proj;
};

void main()
{
    gl_Position = view_proj * vec4(position.xyz, 1.0);
    var_texcoord0 = texcoord0;
    // calculate normalized local position and pass it on to the fragment program
    var_position_local = (position_local + sprite_size * 0.5) / sprite_size;
}
```

### sprite_local_uv.fp

```glsl
#version 140

// from sprite_local_uv.vp
in mediump vec2 var_texcoord0;
in highp vec2 var_position_local;

out vec4 out_fragColor;

uniform mediump sampler2D texture_sampler;
uniform fs_uniforms
{
    mediump vec4 tint;
};

void main()
{
    // Pre-multiply alpha since all runtime textures already are
    mediump vec4 tint_pm = vec4(tint.xyz * tint.w, tint.w);

    // sample color from sprite texture
    vec4 color = texture(texture_sampler, var_texcoord0.xy) * tint_pm;

    // mix local position with red and green color of sprite to
    // create a gradient across the entire sprite
    out_fragColor.rg = mix(color.rg, var_position_local.xy, 0.3);
    // use blue and alpha from the sprite
    out_fragColor.b = color.b;
    out_fragColor.a = color.a;
}
```
