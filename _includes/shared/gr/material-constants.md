
The default {% raw %}{{ include.component }}{% endraw %} material has the following constants that can be changed using [go.set()](/ref/stable/go/#go.set) or [go.animate()](/ref/stable/go/#go.animate) (refer to the [Material manual for more details](/manuals/material/#vertex-and-fragment-constants)). Examples:
```lua
go.set("#{% raw %}{{ include.component }}{% endraw %}", "{% raw %}{{ include.variable }}{% endraw %}", vmath.vector4(1,0,0,1))
go.animate("#{% raw %}{{ include.component }}{% endraw %}", "{% raw %}{{ include.variable }}{% endraw %}", go.PLAYBACK_LOOP_PINGPONG, vmath.vector4(1,0,0,1), go.EASING_LINEAR, 2)
```
