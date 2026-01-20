# Modifiers

This example shows particle effect modifiers. Modifiers are used to alter the path of emitted particles.

[Project files](https://github.com/defold/examples/tree/master/particles/modifiers)

Here two modifiers are added to the effect in addition to the emitter. It works as follows:

* The wide box emitter emits particles with a low speed.
* The *Acceleration* modifier pushes the particles causing them to continuously speed up.
* The *Vortex* modifier drags the particles into a vortex. Each particle's speed and direction is altered by the direction and magnitude of the vortex.

The particle system features more modifier types so make sure to check them out.

## Scripts

### modifiers.script

```lua
function init(self)
	particlefx.play("#particles") -- <1>
end

--[[
1. Start playing the particle effect in component "particles" in this game object.
--]]
```
