# Sprite Vertex Color Attribute

This example shows how to set and animate a vertex attribute

Source: [https://github.com/defold/examples/tree/master/material/vertexcolor](https://github.com/defold/examples/tree/master/material/vertexcolor)

The `vertexcolor.script` sets the vertex attribute "mycolor", which has been specified in the material.



The shaders specified by the material also makes use of the `mycolor` attribute to colorize the sprites.

The vertex attributes can also be animated. Click the image for an animation effect.

## Scripts

### vertexcolor.script

```lua
function init(self)
	msg.post(".", "acquire_input_focus")
	
	local scale = 0.75
	local spacingx = 160 * scale + 10
	local spacingy = 190 * scale + 10
	local startx = 40 + spacingx*0.5
	local starty = 40 + spacingy*0.5

	local maxy = 3
	local maxx = 4

	self.urls = {}

	-- 1. For all sprites in the example we set a slightly different `mycolor` vertex attribute:
	for y = 0, maxy do
		for x = 0, maxx do
			local p = vmath.vector3(startx + x*spacingx, starty + y*spacingy, 0.5)
			local id = factory.create("#factory", p, nil, nil, vmath.vector3(0.8, 0.8, 1))
			local url = msg.url(nil, id, "sprite")
			table.insert(self.urls, url)

			-- set vertex attribute:
			go.set(url, "mycolor", vmath.vector4(x/maxx, y/maxy, 0, 1))
		end
	end

	self.updated = false
	self.animation_finished = true
end

function update(self, dt)
	self.updated = true
end

function on_input(self, action_id, action)

	-- 2. On click we animate the `mycolor` vertex attribute of each of the sprites to blue and back.
	if action_id == hash("touch") and action.pressed and self.updated and self.animation_finished then
		for _, url in ipairs(self.urls) do
			self.animation_finished = false

			-- animate vertex attribute:
			go.animate(url, "mycolor", go.PLAYBACK_ONCE_PINGPONG, vmath.vector4(0, 0, 1, 1), go.EASING_LINEAR, 1, 0, function()
				self.animation_finished = true
			end)
		end
	end
end
```

### vertexcolor.vp

```glsl
#version 140

// positions are in world space
in highp vec4 position;
in mediump vec2 texcoord0;
in mediump vec4 mycolor; // 1. Add attribute definition

out mediump vec2 var_texcoord0;
out mediump vec4 var_mycolor; // 2. Add output variable to pass color to fp

uniform vs_uniforms
{
    highp mat4 view_proj;
};

void main()
{
    gl_Position = view_proj * vec4(position.xyz, 1.0);
    var_texcoord0 = texcoord0;
    var_mycolor = mycolor; // 3. Pass mycolor attribute value to fp.
}
```

### vertexcolor.fp

```glsl
#version 140

in mediump vec2 var_texcoord0;
in mediump vec4 var_mycolor; // 4. Add var_mycolor definition

out vec4 out_fragColor;

uniform mediump sampler2D texture_sampler;

void main()
{
    // Pre-multiply color to match premultiplied textures
    mediump vec4 tint_pm = vec4(var_mycolor.rgb * var_mycolor.a, var_mycolor.a);
    out_fragColor = texture(texture_sampler, var_texcoord0.xy) * tint_pm;
}
```
