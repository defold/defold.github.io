# Flip

This example demonstrates flipping a sprite animation vertically and horizontally.

Source: [https://github.com/defold/examples/tree/master/sprite/flip](https://github.com/defold/examples/tree/master/sprite/flip)

Overview :  [sprite.set_hflip](https://defold.com/ref/beta/sprite/#sprite.set_hflip:url-flip) & [sprite.set_vflip](https://defold.com/ref/beta/sprite/#sprite.set_vflip:url-flip) uses a boolean to set if a sprite animation should be flipped.



The setup consists of 2 bee game object's, another game object for text labels and a single script.

2 Game Object's
: containing:
  - A sprite with default animation set to bee
  
1 Game object
: contains:
 - A script
 - 2 text labels

Script
: use:
  - Sets sprite flip and go.animation for bee game objects.

## Scripts

### flip.script

```lua
local horizontal = "bee1" -- < 1 >
local vertical = "bee2"

local function bee_flip(go_id) -- < 2 >
	if go_id == horizontal then
		local bee_position = go.get_position(horizontal)
		if bee_position.x == 400 then
			sprite.set_hflip("bee1#sprite", false)
			go.animate(horizontal,"position.x",go.PLAYBACK_ONCE_FORWARD,120,go.EASING_INOUTCUBIC,3.5,0,function()bee_flip(horizontal)end)
		else
			sprite.set_hflip("bee1#sprite", true)
			go.animate(horizontal,"position.x",go.PLAYBACK_ONCE_FORWARD,400,go.EASING_INOUTCUBIC,3.5,0,function()bee_flip(horizontal)end)
		end
	else
		local bee_position = go.get_position(vertical)
		if bee_position.y == 520 then
			sprite.set_vflip("bee2#sprite", true)
			go.animate(vertical,"position.y",go.PLAYBACK_ONCE_FORWARD,200,go.EASING_INOUTCUBIC,3.5,0.6,function()bee_flip(vertical)end)
		else
			sprite.set_vflip("bee2#sprite", false)
			go.animate(vertical,"position.y",go.PLAYBACK_ONCE_FORWARD,520,go.EASING_INOUTCUBIC,3.5,0.6,function()bee_flip(vertical)end)
		end
	end
end

function init(self) -- < 3 >
	bee_flip(horizontal)
	bee_flip(vertical)
end

--[[

1. 2 game object id's are set as local strings for horizontal and vertical examples.

2. bee_flip() function takes in the go's id then an if statement is used to determine go's
	position and sets horizontal or vertical flip to sprite accordingly. Then go.animate is
	used and a callback to bee_flip() occurs at the end of the animation.

3. In the initialize function we call bee_flip() for both horizontal and vertical bee 
	game objects.

--]]
```
