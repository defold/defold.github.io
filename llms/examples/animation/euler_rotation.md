# Euler Rotation

Shows how to animate Euler rotation.

[Project files](https://github.com/defold/examples/tree/master/animation/euler_rotation)

This example rotates a spinner sprite continuously by tweening one Euler angle. It uses the Z axis because that is the axis pointing out of the screen in a 2D scene.

## What You'll Learn

- How to animate a game object's Euler rotation
- Why `euler.z` is the useful axis for 2D rotation
- How looping playback and linear easing create constant motion

## Setup

The collection contains two game objects:

`go`
: Contains the sprite and `euler_rotation.script`. The sprite uses the `spinner` image from `sprites.atlas`, and the script animates only the game object's `euler.z` property.

`description`
: Contains the bottom description label. The label uses `/assets/text32.font`, a 32 px distance-field font, with `/builtins/fonts/label-df.material`.

## How It Works

`go.animate()` can animate numeric game object properties and sub-properties. Here it targets `"."`, the current game object, and `"euler.z"`, the Z component of the Euler rotation vector.

Euler angles are expressed in degrees, so the target value `-360` is one full clockwise turn. `go.PLAYBACK_LOOP_FORWARD` restarts the same two-second linear tween every time it finishes, keeping the spinner rotating at a constant speed.

## Scripts

### euler_rotation.script

```lua
function init(self)
	go.animate(".", "euler.z", go.PLAYBACK_LOOP_FORWARD, -360, go.EASING_LINEAR, 2) -- <1>
end

--[[
1. Animate the current game object's `euler.z` sub-property from its starting rotation to -360 degrees. The forward looping playback repeats the two-second linear tween, so the sprite keeps rotating clockwise.
]]
```
