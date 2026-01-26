# extension-rive

**Namespace:** `rive`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Rive models

## API

### rive.play_anim
*Type:* FUNCTION
Plays the specified animation on a Rive model

**Parameters**

- `url` (url) - The Rive model component for which to play an animation
- `anim_id` (hash) - Id of the animation to play
- `playback` (number) - Playback mode of the animation (from go.PLAYBACK_*)
- `options` (table) - Playback options
  - `offset` (number) - The normalized initial value of the animation cursor when the animation starts playing
  - `playback_rate` (constant) - The rate with which the animation will be played. Must be positive.
- `complete_function` (function) - function to call when the animation has completed
  - `self` (object) - The context of the calling script
  - `message_id` (hash) - The name of the completion message ("rive_animation_done")
  - `message` (table) - A table that contains the response
    - `animation_id` (hash) - the animation that was completed
    - `playback` (constant) - the playback mode for the animation
  - `sender` (url) - The invoker of the callback - the Rive model component

### rive.play_state_machine
*Type:* FUNCTION
Plays the specified animation on a Rive model

**Parameters**

- `url` (url) - The Rive model component for which to play an animation
- `state_machine_id` (hash) - Id of the state machine to play
- `options` (table) - Playback options
  - `playback_rate` (constant) - The rate with which the animation will be played. Must be positive.
- `callback_function` (function) - function to call when a playback event occurs
  - `self` (object) - The context of the calling script
  - `message_id` (hash) - The name of the event
  - `message` (table) - A table that contains the event properties

### rive.cancel
*Type:* FUNCTION
Cancels all running animations on a specified spine model component

**Parameters**

- `url` (url) - The Rive model component for which to cancel the animation

### rive.get_go
*Type:* FUNCTION
Returns the id of the game object that corresponds to a specified skeleton bone.

**Parameters**

- `url` (url) - The Rive model component to query
- `bone_id` (hash) - Id of the corresponding bone

### rive.pointer_move
*Type:* FUNCTION
Forward mouse/touch movement to a component

**Parameters**

- `url` (url) - The Rive model component
- `x` (number) - Horizontal position
- `y` (number) - Vertical position

### rive.pointer_up
*Type:* FUNCTION
Forward mouse/touch release event to a component

**Parameters**

- `url` (url) - The Rive model component
- `x` (number) - Horizontal position
- `y` (number) - Vertical position

### rive.pointer_down
*Type:* FUNCTION
Forward mouse/touch press event to a component

**Parameters**

- `url` (url) - The Rive model component
- `x` (number) - Horizontal position
- `y` (number) - Vertical position

### rive.get_text_run
*Type:* FUNCTION
Gets the text run of a specified text component from within the Rive artboard assigned to the component.

**Parameters**

- `url` (url) - The Rive model component for which to get the text run from
- `name` (string) - The name of the text run from the Rive artboard.
- `nested_artboard` (string) - (OPTIONAL) If specified, the text run will be retrieved from the specified nested artboard

### rive.set_text_run
*Type:* FUNCTION
Set the text run of a specified text component from within the Rive artboard assigned to the component.

**Parameters**

- `url` (url) - The Rive model component for which to set the text run for
- `name` (string) - The name of the text run from the Rive artboard.
- `text_run` (string) - The text run contents to update with.
- `nested_artboard` (string) - (OPTIONAL) If specified, the text run will be set in the specified nested artboard

### rive.get_projection_matrix
*Type:* FUNCTION
Get an orthographic projection matrix that can be used to project regular Defold components into the same coordinate space as the rive model when using the 'fullscreen' coordinate space.

### rive.get_state_machine_input
*Type:* FUNCTION
Get the input values from a state machine input, either from the current top-level artboard, or from a nested artboard inside the Rive model artboard. Note that trigger inputs will not generate a value!

**Parameters**

- `url` (url) - The Rive model component
- `name` (string) - The name of the input
- `nested_artboard` (string) - (OPTIONAL) If specified, the input will be queried for the specified nested artboard

### rive.set_state_machine_input
*Type:* FUNCTION
Set the input values from a state machine input, either from the current top-level artboard, or from a nested artboard inside the Rive model artboard. Note - To set input for a trigger, use a bool value.

**Parameters**

- `url` (url) - The Rive model component
- `name` (string) - The name of the input
- `value` (number | bool) - The value of the input to set
- `nested_artboard` (string) - (OPTIONAL) If specified, the input will be queried for the specified nested artboard

### rive.riv_swap_asset
*Type:* FUNCTION
Replace an asset in runtime.

**Parameters**

- `riv_path` (string,hash) - The Rive (.rivc) path. E.g. "/path/to/file.rivc"
- `asset_name` (string) - The name of the FileAsset inside the .riv file
- `options` (table) - A table of options containing
  - `path` (string) - The path of the asset file to replace with. E.g. "/path/to/file.png"
  - `payload` (string) - The payload of the asset file to replace with. E.g. a .png binary file. Takes precedence over the `path` option.

### rive.set_font_fallback_path
*Type:* FUNCTION
Register a fallback font from a file path. This font will be used if glyphs are missing in the current font. Note that only one font fallback can be active at any time.

**Parameters**

- `path` (string) - The resource path to the font file.

### rive.set_font_fallback_memory
*Type:* FUNCTION
Register a fallback font from a memory payload. This font will be used if glyphs are missing in the current font. Note that only one font fallback can be active at any time.

**Parameters**

- `payload` (string) - The font file contents.

### rive.clear_font_fallback
*Type:* FUNCTION
Clear any registered fallback font.

### rive.databind.create_view_model_instance_runtime
*Type:* FUNCTION
Creates a ViewModelInstanceRuntime

**Parameters**

- `url` (url) - The Rive model component
- `name` (string, hash) - The name of the view model to instantiate

### rive.databind.destroy_view_model_instance_runtime
*Type:* FUNCTION
Releases the previously created ViewModelInstanceRuntime

**Parameters**

- `url` (url) - The Rive model component
- `handle` (integer) - The handle to the ViewModelInstanceRuntime instance

### rive.databind.set_view_model_instance_runtime
*Type:* FUNCTION
Sets the current ViewModelInstanceRuntime

**Parameters**

- `url` (url) - The Rive model component
- `handle` (integer) - The handle to the ViewModelInstanceRuntime instance

### rive.databind.get_view_model_instance_runtime
*Type:* FUNCTION
Gets the current ViewModelInstanceRuntime

**Parameters**

- `url` (url) - The Rive model component

### rive.databind.set_properties
*Type:* FUNCTION
Sets properties to the ViewModelInstanceRuntime instance

**Parameters**

- `url` (url) - The Rive model component
- `handle` (integer) - The handle to the ViewModelInstanceRuntime instance
- `properties` (table) - A table of properties, where each key is a Rive "path", and the values are mapped to the corresponding property value type.

### rive.databind.get_property
*Type:* FUNCTION
Gets a property from the ViewModelInstanceRuntime instance

**Parameters**

- `url` (url) - The Rive model component
- `handle` (integer) - The handle to the ViewModelInstanceRuntime instance
- `path` (string) - The path to the property

### rive.databind.list_add_instance
*Type:* FUNCTION
Add a ViewModelInstanceRuntime instance to a list property

**Parameters**

- `url` (url) - The Rive model component
- `handle` (integer) - The handle to the ViewModelInstanceRuntime instance
- `path` (string) - The path to the list property
- `instance_handle` (integer) - The handle to the ViewModelInstanceRuntime instance to add to the list

### rive.databind.list_remove_instance
*Type:* FUNCTION
Remove a ViewModelInstanceRuntime instance from a list property

**Parameters**

- `url` (url) - The Rive model component
- `handle` (integer) - The handle to the ViewModelInstanceRuntime instance
- `path` (string) - The path to the list property
- `instance_handle` (integer) - The handle to the ViewModelInstanceRuntime instance to add to the list

###
*Type:* TABLE
Functions and constants for interacting with Rive data bindings
