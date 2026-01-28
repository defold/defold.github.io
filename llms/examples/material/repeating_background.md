# Repeating Background

Create a scrolling background using a repeating texture on a model quad.

[Project files](https://github.com/defold/examples/tree/master/material/repeating_background)

A repeating, scrolling texture can add visual interest to a static background. This example demonstrates how to create an infinitely tiling background using a model quad with a repeating texture. The effect is achieved by scrolling the UV coordinates over time, creating smooth, continuous motion.

The script driving the effect works as follows:

* Each frame it reads the current window size and scales the `background` game object so the quad covers the full viewport. The rotation is set via `euler.z` (Rotation Z in the IDE).
* It converts the window size into a UV repeat scale (`uv_params.x/y`) so the texture tiles across the screen.
* It advances a scrolling offset based on `scroll_speed` and `tile_size`, wraps it to the 0..1 range, and sends `uv_params` to the model material.

The asset used in this example is from Kenney's [Puzzle Pack 2](https://www.kenney.nl/assets/puzzle-pack-2), licensed under CC0.

## Scripts

### repeating_background.script

```lua
-- Size of a single tile in pixels
go.property("tile_size", 128)
-- Scroll speed vector (x, y, z) in pixels per second
go.property("scroll_speed", vmath.vector3(50, 0, 0))

-- Applies layout based on current window size
-- Scales the game object to fill the entire window and calculates UV scale
local function apply_layout(self)
	local width, height = window.get_size()
	-- Scale the game object to match window dimensions
	go.set(".", "scale", vmath.vector3(width, height, 1))

	-- Calculate how many tiles fit in the window (for UV tiling)
	self.uv_scale = vmath.vector3(width / self.tile_size, height / self.tile_size, 0)

	-- Send UV parameters to the shader: scale (x, y) and offset (z, w)
	local uv_params = vmath.vector4(self.uv_scale.x, self.uv_scale.y, self.offset.x, self.offset.y)
	go.set("#model", "uv_params", uv_params)
end

-- Updates UV offset for scrolling animation
-- Moves the texture offset based on scroll speed and wraps it using modulo
local function update_uv_params(self, dt)
	-- Calculate offset delta in tile units (0-1 range)
	local delta = self.scroll_speed * dt / self.tile_size
	-- Update offset (subtract because we want to scroll in the direction of scroll_speed)
	self.offset = self.offset - delta
	-- Wrap offset to 0-1 range to create seamless repeating
	self.offset.x = self.offset.x % 1
	self.offset.y = self.offset.y % 1

	-- Send updated UV parameters to the shader
	local uv_params = vmath.vector4(self.uv_scale.x, self.uv_scale.y, self.offset.x, self.offset.y)
	go.set("#model", "uv_params", uv_params)
end

-- Initialize the script
-- Sets up the initial UV offset to zero
function init(self)
	self.offset = vmath.vector3(0)
end

function final(self)
end

-- Update function called every frame
-- Applies layout and updates UV parameters for scrolling
function update(self, dt)
	apply_layout(self)
	update_uv_params(self, dt)
end
```

### repeating_background.vp

```glsl
#version 140

in vec4 position;
in vec2 texcoord0;
uniform vp_uniforms
{
    mat4 mtx_worldview;
    mat4 mtx_proj;
    vec4 uv_params;
};

out vec2 var_texcoord0;

void main()
{
    // uv_params.x = repeat scale on U axis (tiles across width)
    // uv_params.y = repeat scale on V axis (tiles across height)
    // uv_params.z = scroll offset on U axis (normalized 0..1)
    // uv_params.w = scroll offset on V axis (normalized 0..1)
    var_texcoord0 = texcoord0 * uv_params.xy + uv_params.zw;
    gl_Position = mtx_proj * mtx_worldview * vec4(position.xyz, 1.0);
}
```

### repeating_background.fp

```glsl
#version 140

in mediump vec2 var_texcoord0;

out vec4 out_fragColor;

uniform mediump sampler2D texture0;

void main()
{
    out_fragColor = texture(texture0, var_texcoord0);
}
```
