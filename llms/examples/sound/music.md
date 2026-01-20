# Music

This example shows how to play a piece of music, stored as an .OGG file, with a sound component. The sound component is set to "looping" causing the music to never, ever stop.

[Project files](https://github.com/defold/examples/tree/master/sound/music)

## Scripts

### music.script

```lua
function init(self)
    sound.play("#music", { gain = 1.0, pan = 0 }) -- <1>
end

--[[
1. Tell the component "#music" to start playing its sound. The sound will be played with gain 1.0 (max volume) and pan 0.0 (equal left-right channel)
--]]
```
