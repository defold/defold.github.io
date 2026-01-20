# extension-spine

**Namespace:** `spine`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Spine models

## API

### spine.play_anim
*Type:* FUNCTION
Plays the specified animation on a Spine model. A [ref:spine_animation_done] message is sent to the callback (or message handler). Any spine events will also be handled in the same way. [icon:attention] The callback is not called (or message sent) if the animation is cancelled with [ref:spine.cancel]. The callback is called (or message sent) only for animations that play with the following playback modes * `go.PLAYBACK_ONCE_FORWARD` * `go.PLAYBACK_ONCE_BACKWARD` * `go.PLAYBACK_ONCE_PINGPONG`

**Parameters**

- `url` (string | hash | url) - The Spine model for which to play an animation
- `anim_id` (string | hash) - Id of the animation to play
- `playback` (number) - Playback mode of the animation (from go.PLAYBACK_*)
- `options` (table) - Playback options
  - `blend_duration` (number) - Duration of a linear blend between the current and new animation.
  - `offset` (number) - The normalized initial value of the animation cursor when the animation starts playing.
  - `playback_rate` (constant) - The rate with which the animation will be played. Must be positive.
  - `track` (number) - The track index of the animation. Defaults to 1. Animations on different tracks play in parallel.
  - `mix_blend` (constant) - The mix blend mode for the animation (from spine.MIX_BLEND_*). Defaults to `spine.MIX_BLEND_REPLACE`. Ignored for animations on the first track.
- `callback_function` (function) - function to call when the animation has completed or a Spine event occured
  - `self` (object) - The context of the calling script
  - `message_id` (hash) - The name of the message ("spine_animation_done" or "spine_event")
  - `message` (table) - A table that contains the response
    - `animation_id` (hash) - The animation that was completed
    - `track` (number) - The track index of the animation
    - `playback` (constant) - (spine_animation_done only!) The playback mode for the animation
    - `event_id` (hash) - (spine_event only!) the event that was triggered.
    - `t` (float) - (spine_event only!) the time at which the event occurred (seconds)
    - `integer` (int) - (spine_event only!) a custom integer associated with the event (0 by default).
    - `float` (float) - (spine_event only!) a custom float associated with the event (0 by default)
    - `string` (hash) - (spine_event only!) a custom string associated with the event (hash("") by default)
  - `sender` (url) - The invoker of the callback - the Spine model component

### spine.cancel
*Type:* FUNCTION
Cancels all running animations on a specified spine model component

**Parameters**

- `url` (string | hash | url) - The Spine model for which to cancel the animation
- `options` (table) - Cancel options
  - `track` (number) - The index of the track which to cancel the animation on. Defaults to all animations on all tracks.

### spine.get_go
*Type:* FUNCTION
Returns the id of the game object that corresponds to a specified skeleton bone.

**Parameters**

- `url` (string | hash | url) - The Spine model to query
- `bone_id` (hash) - Id of the corresponding bone

### spine.set_skin
*Type:* FUNCTION
Sets the spine skin on a spine model.

**Parameters**

- `url` (string | hash | url) - The Spine model to query
- `skin` (string | hash) - Id of the corresponding skin

### spine.add_skin
*Type:* FUNCTION
Adds one spine skin on a spine model to another on the same model.

**Parameters**

- `url` (string | hash | url) - The Spine model to query
- `skin_a` (string | hash) - Id of the corresponding skin that will recieve the added skin
- `skin_b` (string | hash) - Id of the corresponding skin to add

### spine.copy_skin
*Type:* FUNCTION
Copies one spine skin on a spine model to another on the same model.

**Parameters**

- `url` (string | hash | url) - The Spine model to query
- `skin_a` (string | hash) - Id of the corresponding skin that will recieve the copied skin
- `skin_b` (string | hash) - Id of the corresponding skin to copy.

### spine.clear_skin
*Type:* FUNCTION
Clear all attachments and constraints from a skin on a spine model

**Parameters**

- `url` (string | hash | url) - The Spine model to query
- `skin` (string | hash) - Id of the corresponding skin

### spine.set_attachment
*Type:* FUNCTION
Set the attachment of a slot on a spine model.

**Parameters**

- `url` (string | hash | url) - The Spine model to query
- `slot` (string | hash) - Id of the slot
- `attachment` (string | hash | nil) - Id of the attachment. May be nil to reset to default attachment.

### spine.set_slot_color
*Type:* FUNCTION
Set the color a slot will tint its attachments on a spine model.

**Parameters**

- `url` (string | hash | url) - The Spine model to query
- `slot` (string | hash) - Id of the slot
- `color` (vector4) - Tint applied to attachments in a slot

### spine.reset_constant
*Type:* FUNCTION
Resets a shader constant for a spine model component. (Previously set with `go.set()`)

**Parameters**

- `url` (string | hash | url) - The Spine model to query
- `constant` (string | hash) - name of the constant

### spine.reset_ik_target
*Type:* FUNCTION
reset the IK constraint target position to default of a spinemodel.

**Parameters**

- `url` (string | hash | url) - The Spine model
- `ik_constraint_id` (string | hash) - id of the corresponding IK constraint

### spine.set_ik_target_position
*Type:* FUNCTION
set the target position of an IK constraint object.

**Parameters**

- `url` (string | hash | url) - The Spine model
- `ik_constraint_id` (string | hash) - id of the corresponding IK constraint
- `position` (vector3) - target position

### spine.set_ik_target
*Type:* FUNCTION
set the IK constraint object target position to follow position.

**Parameters**

- `url` (string | hash | url) - The Spine model to query
- `ik_constraint_id` (string | hash) - id of the corresponding IK constraint
- `target_url` (string | hash | url) - target game object

### spine.physics_translate
*Type:* FUNCTION
Apply a physics-based translation to the Spine model.

**Parameters**

- `url` (string | hash | url) - The Spine model component to translate.
- `translation` (vector3) - The translation vector to apply to the Spine model.

### spine.physics_rotate
*Type:* FUNCTION
Apply a physics-based rotation to the Spine model.

**Parameters**

- `url` (string | hash | url) - The Spine model component to rotate.
- `center` (vector3) - The center point around which to rotate.
- `degrees` (number) - The rotation angle in degrees.
