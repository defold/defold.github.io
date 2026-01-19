# Sprite size

This example shows how to get the size of a sprite at run-time

Source: [https://github.com/defold/examples/tree/master/sprite/size](https://github.com/defold/examples/tree/master/sprite/size)

The example uses two game objects, each with a sprite component and a label (to show the size). One of game objects contains the script that reads the size and shows it on the labels:

## Scripts

### size.script

```lua
function init(self)
	local rectangle_size = go.get("#stone", "size") -- <1>
	local square_size = go.get("square#stone", "size") -- <2>
	label.set_text("#info", "" .. rectangle_size.x .. "x" .. rectangle_size.y) -- <3>
	label.set_text("square#info", "" .. square_size.x .. "x" .. square_size.y) -- <4>
end

--[[
1. Read the size of the sprite with id `stone` on the same game object as this script (the game object with id `rectangle`).
2. Read the size of the sprite with id `stone` on the game object with id `square`.
3. Set the text of the label with id `info` on the same game object as this script (the game object with id `rectangle`).
4. Set the text of the label with id `info` on the game object with id `square`.
--]]
```
