# Z-order

This example shows how to put sprites in front and behind of eachother

Source: [https://github.com/defold/examples/tree/master/basics/z_order](https://github.com/defold/examples/tree/master/basics/z_order)

There is one game object containing the logo sprite. It is set at Z position 0.
The green spaceship is another game object containing a sprite. It is set at Z position 0.5.
The pink spaceship is another game object containing a sprite. It is set at Z position -0.5.

## Scripts

### z_order.script

```lua
function init(self)
	go.animate(".", "position.x", go.PLAYBACK_LOOP_PINGPONG, 600, go.EASING_INOUTSINE, 3) -- <1>
end

--[[
1. Animate the game object's ("." is shorthand for the current game object) x position between
   start position and 600.
--]]
```
