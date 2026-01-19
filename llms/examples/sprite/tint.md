# Sprite tint

This example shows how tint a sprite at run-time

Source: [https://github.com/defold/examples/tree/master/sprite/tint](https://github.com/defold/examples/tree/master/sprite/tint)

The example uses a script to tint (color) sprites in a couple of different ways. The tint is a fragment constant on the sprite material and it is used in the sprite.fp fragment shader program to modify the color sampled from the texture.

It is important to keep in mind that each tinted sprite generates a new draw call since a modified tint value will break the built in draw call batching in Defold.

## Scripts

### tint.script

```lua
function init(self)
	go.set("logo1#sprite", "tint", vmath.vector4(1, 0, 0, 1)) -- <1>
	go.set("logo2#sprite", "tint.x", 0) -- <2>
	go.set("logo3#sprite", "tint.w", 0.3) -- <3>
	go.animate("logo4#sprite", "tint", go.PLAYBACK_LOOP_PINGPONG, vmath.vector4(0, 0.5, 0.8, 1), go.EASING_INOUTQUAD, 2) -- <4>
	go.animate("logo5#sprite", "tint.w", go.PLAYBACK_LOOP_PINGPONG, 0, go.EASING_INOUTQUAD, 3) -- <4>
end

--[[
1. x,y,z,w -> r,g,b,a. Keep red and alpha. Remove green and blue.
2. x = red. Remove the red color component completely
3. w = alpha. Make the sprite semi-transparent
4. The tint property can be animated, either as a whole or each individual value
--]]
```
