# Custom easing - square wave

This example shows how to define a custom easing curve and use it when animating with `go.animate()` instead of a built-in easing constant.

[Project files](https://github.com/defold/examples/tree/master/animation/custom_easing)

This example uses the square-wave easing curve. The logo alternates between its starting height and the target height, and the animation system interpolates the positions between the low and high positions when animating.

## Setup

The collection contains one game object with one sprite and one script. The script animates only the `position.y` property with the custom easing.

## How It Works

The script stores the custom easing samples in a plain Lua table and turns that table into a `vmath.vector`. Defold accepts that vector anywhere `go.animate()` (or `gui.animate()` in case of GUI animations) expects an easing value.

Because the vector is made of repeated blocks of `0` and `1`, the animation keeps snapping between the start value (start y position) and the target value (520 on Y axis, which is above the start value). That makes the easing behave like a square wave instead of a continuous curve. Note that the animation system still interpolates between the frames, so depending on time, the animation can be more trapezoidal or more square wave.

## Scripts

### custom_easing.script

```lua
local VALUES = { -- <1>
	0, 0, 0, 0, 0, 0,
	1, 1, 1, 1, 1, 1,
	1, 1, 1, 1, 1, 1,
	0, 0, 0, 0, 0, 0,
}
local SQUARE_EASING = vmath.vector(VALUES) -- <2>

function init(self)
	go.animate(".", "position.y", go.PLAYBACK_LOOP_FORWARD, 520, SQUARE_EASING, 4.0) -- <3>
end

--[[
1. This table defines a custom easing curve with normalized samples between 0 and 1. Repeating blocks of zeroes and ones create a square-wave pattern.
2. Convert the Lua table into a `vmath.vector`, which `go.animate()` accepts as a custom easing value.
3. Animate the current game object's `position.y` sub-property. The custom curve makes the sprite move between its starting y position and 520 instead with interpolated in-between positions.
]]
```
