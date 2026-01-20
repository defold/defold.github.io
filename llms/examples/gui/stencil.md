# Stencil

A GUI box node with "Clipping mode" set to "STENCIL". This makes it mask its child node (which is called "bunny").

[Project files](https://github.com/defold/examples/tree/master/gui/stencil)

## Scripts

### stencil.gui_script

```lua
function init(self)
	local bunny = gui.get_node("bunny")
	gui.animate(bunny, "position.x", 150, gui.EASING_INOUTSINE, 3, 0, null, gui.PLAYBACK_LOOP_PINGPONG)
end
```
