# Particle effect

This example shows a simple particle effect. The particlefx component has all the values at default, except the image and animation used.

Source: [https://github.com/defold/examples/tree/master/particles/particlefx](https://github.com/defold/examples/tree/master/particles/particlefx)

## Scripts

### particlefx.script

```lua
function init(self)
	particlefx.play("#particles") -- <1>
end

--[[
1. Start playing the particle effect in component "particles" in this game object.
--]]
```
