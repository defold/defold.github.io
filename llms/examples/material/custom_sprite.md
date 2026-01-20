# Custom Sprite

This example demonstrates a simple way to create and apply a custom sprite shader for changing colors and customizing an outline.

[Project files](https://github.com/defold/examples/tree/master/material/custom_sprite)

If your game requires a sprite that can be recolored and reused, a custom shader will be needed. Your sprite's artwork can be composed in such a way that will help achieve things you may want to do. For example an outline around your sprite that can be turned off/on and color changed. When creating your artwork if your sprite's green-channel is shifted slightly below 1.0 and you add an outline around your sprite with full green color equal to 1.0 then in the shader you can manage the green channel values that match 1.0 and change the color or completely hide these values thus removing the outline altogether. Recoloring sprites to be used throughout a game is pretty common. One way to achieve re-coloring with a range of values instead of a single color is to de-saturate a part of the sprite you want to recolor. When you de-saturate an image it will even out the red, green and blue channel values to a grey-scale. You can then check in the shader for these grey-scale values and change the colors. To check for these values you can add 2 or 3 channels together as a float value and then with another float multiply a single channel by 2 or 3, we then compare these values when valid use a new color.

In the example the custom sprite material has 2 vertex attributes each is a vector 4 of float values. The values are used for coloring the fluid and the outline from a script to the shader. The script has a function for creating a random color and also sets the color vertex properties

## Scripts

### set_color.script

```lua
local sprite_to_color = "/new#sprite" local brightness = 0.3

local function random_color(self) -- create a new_color of random-ish float values (0.3 or 1.3)
	local random_number_r = math.random(0, 1)+brightness
	local random_number_b = math.random(0, 1)+brightness
	local random_number_g = math.random(0, 1)+brightness
	local new_color = vmath.vector4(random_number_r, random_number_g, random_number_b, self.outline_io)
	return new_color
end

function init(self)
	msg.post("@render:", "clear_color", { color = vmath.vector4(0.25960784,0.2315686274509804,0.229607843, 1.0) } )
	
	self.outline_io = 0.0 -- float is used when setting the w value of the material vertex attribute "outline" 0.0 = off 1.0 = on
	
	math.randomseed(socket.gettime()*10000)

end

function on_message(self, message_id, message)

	if message_id == hash("outline_io") then

		if self.outline_io <= 0.0 then
			self.outline_io = 1.0 
		else 
			self.outline_io = 0.0 
		end
		go.set(sprite_to_color, "outline.w", self.outline_io)

	elseif message_id == hash("outline_color") then

		go.set(sprite_to_color, "outline", random_color(self)) -- set color for outline

	elseif	message_id == hash("fluid_color") then

		go.set(sprite_to_color, "newcolor", random_color(self)) -- set color for potion fluid

	end

end
```

### recolor.fp

```glsl
#version 140

uniform sampler2D texture_sampler;
uniform f_uniform
{
    vec4 tint;
};

in vec2 var_texcoord0;
// custom vertex attributes
in vec4 new_color;
in vec4 new_outline;

out vec4 final_color;

void main()
{
    lowp vec4 tint_pm = vec4(tint.xyz * tint.w, tint.w);
    lowp vec4 sprite = texture(texture_sampler, var_texcoord0.xy);

    // float values used for comparing
    lowp float combine = (sprite.r + sprite.g);
    lowp float greenmul = sprite.g * 2;

    // when 2 channels added together equal the same as a single channel multipled then we have desaturated values
    if(combine == greenmul){
        sprite = vec4(sprite.rgb*new_color.rgb,sprite.a);
    }

    // when the green channel has a value of 1.0 and the w value is 1.0(on) then we color the outline
    if(new_outline.w >= 1.0 && sprite.g >= 1.0){
        sprite = vec4(new_outline.rgb,1.0);
    }
    else if (sprite.g >= 1.0){ //when the w value is not 1.0 we remove all values. turning the outline off
        sprite = vec4(0.0, 0.0, 0.0, 0.0);
    }
    
    final_color = vec4(sprite * tint);
}
```

### recolor.vp

```glsl
#version 140

uniform v_inputs
{
    mat4 view_proj;
};
// positions are in world space
in vec4 position;
in vec2 texcoord0;
// custom vertex attributes from material
in vec4 newcolor;
in vec4 outline;

out vec2 var_texcoord0;
// custom vertex attributes sent to fragment program
out vec4 new_color;
out vec4 new_outline;

void main()
{
    gl_Position = view_proj * vec4(position.xyz, 1.0);
    var_texcoord0 = texcoord0;
    new_color = newcolor;
    new_outline = outline;
}
```
