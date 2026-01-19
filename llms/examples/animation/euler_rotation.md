# Euler Rotation

This example shows how to animate the rotation of a game object using the euler game object property.

Source: [https://github.com/defold/examples/tree/master/animation/euler_rotation](https://github.com/defold/examples/tree/master/animation/euler_rotation)

## Scripts

### euler_rotation.script

```lua
function init(self)
	-- rotate clockwise one full revolution in two seconds
	go.animate(".", "euler.z", go.PLAYBACK_LOOP_FORWARD, -360, go.EASING_LINEAR, 2)
end
```
