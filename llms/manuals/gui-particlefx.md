# GUI ParticleFX nodes {#manuals:gui-particlefx}

A particle effect node is used to play particle effect systems in the GUI screen space.

## Adding Particle FX nodes

Add new particle nodes by either `right clicking` in the *Outline* and selecting `Add ▸ ParticleFX`, or press `A` and select `ParticleFX`.

You can use particle effects that you have added to the GUI as source for the effect. Add particle effects by `right clicking` the *Particle FX* folder icon in the *Outline* and selecting `Add ▸ Particle FX...`. Then set the *Particlefx* property on the node:

## Controlling the effect

You can start and stop the effect by controlling the node from a script:
```lua
-- start the particle effect
local particles_node = gui.get_node("particlefx")
gui.play_particlefx(particles_node)
```
```lua
-- stop the particle effect
local particles_node = gui.get_node("particlefx")
gui.stop_particlefx(particles_node)
```

See the [Particle FX manual](particlefx.md) for details on how particle effects work.