# Model

**Namespace:** `dmGameSystem`
**Language:** C++
**Type:** Defold C++
**File:** `comp_model.h`
**Source:** `engine/gamesys/src/dmsdk/gamesys/components/comp_model.h`
**Include:** `dmsdk/gamesys/components/comp_model.h`

API for interacting with model components.

## API

### CompModelPlayAnimation
*Type:* FUNCTION
Play a model animation.

**Parameters**

- `world` (HModelWorld) - Model world.
- `component` (HModelComponent) - Model component.
- `anim_id` (dmhash_t) - Animation to play.
- `playback` (dmRig::RigPlayback) - Playback mode.
- `blend_duration` (float) - Duration of a linear blend between the current and new animation.
- `offset` (float) - The normalized initial value of the animation cursor when the animation starts playing.
- `playback_rate` (float) - The rate with which the animation will be played. Must be positive.
- `callback` (FModelAnimationCallback) - Optional function callback to send play events to.
- `callback_ctx` (void*) - Optional function callback context (only when callback is set)

**Returns**

- `result` (dmRig::Result) - Result of the operation.

### FModelAnimationCallback
*Type:* FUNCTION
Model animation callback function.

**Parameters**

- `user_ctx` (void*) - User context
- `event_type` (dmRig::RigEventType) - Animation event type
- `event_data` (void*) - Animation event data
