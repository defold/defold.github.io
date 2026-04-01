# extension-rive

**Namespace:** `rive`
**Language:** Lua
**Type:** Extension

Rive animation helpers exposed to Lua scripts

## API

### rive.pointer_move
*Type:* FUNCTION
Lua wrapper for pointer movement.

**Parameters**

- `url` (url) - Component receiving the pointer move.
- `x` (number) - Pointer x coordinate in component space.
- `y` (number) - Pointer y coordinate in component space.

### rive.pointer_up
*Type:* FUNCTION
Lua wrapper for pointer up events.

**Parameters**

- `url` (url) - Component receiving the pointer release.
- `x` (number) - Pointer x coordinate.
- `y` (number) - Pointer y coordinate.

### rive.pointer_down
*Type:* FUNCTION
Lua wrapper for pointer down events.

**Parameters**

- `url` (url) - Component receiving the pointer press.
- `x` (number) - Pointer x coordinate.
- `y` (number) - Pointer y coordinate.

### rive.pointer_exit
*Type:* FUNCTION
Lua wrapper for pointer exit events.

**Parameters**

- `url` (url) - Component receiving the pointer leave.
- `x` (number) - Pointer x coordinate.
- `y` (number) - Pointer y coordinate.

### rive.get_projection_matrix
*Type:* FUNCTION
Returns the projection matrix in render coordinates.

### rive.set_file_listener
*Type:* FUNCTION
Sets or clears the global file listener callback.

**Parameters**

- `callback` (function(self, event, data) | nil) - Callback invoked for file system events; pass nil to disable.
  - `self` (object) - The calling script instance.
  - `event` (string) - One of onFileLoaded, onFileDeleted, onFileError, onArtboardsListed, onViewModelsListed, onViewModelInstanceNamesListed, onViewModelPropertiesListed, onViewModelEnumsListed
  - `data` (table) - Additional fields vary by event. Common keys include
    - `file` (FileHandle) - File handle involved in the event.
    - `viewModelName` (string) - View model name for the request, when applicable.
    - `instanceNames` (table) - Array of instance name strings.
    - `artboardNames` (table) - Array of artboard name strings.
    - `properties` (table) - Array of property metadata tables.
    - `enums` (table) - Array of enum definitions.
    - `error` (string) - Error message when a failure occurs.

### rive.get_file
*Type:* FUNCTION
Returns the Rive file handle tied to the component.

**Parameters**

- `url` (url) - Component whose file handle to query.

### rive.set_artboard
*Type:* FUNCTION
Switches the active artboard for the component.

**Parameters**

- `url` (url) - Component using the artboard.
- `name` (string | nil) - Name of the artboard to create and set. Pass nil to create a default artboard.

### rive.get_artboard
*Type:* FUNCTION
Queries the current artboard handle for the component.

**Parameters**

- `url` (url) - Component whose artboard handle to return.

### rive.set_state_machine
*Type:* FUNCTION
Selects a state machine by name on the component.

**Parameters**

- `url` (url) - Component owning the state machine.
- `name` (string | nil) - Name of the state machine to create and set. Pass nil to create a default state machine.

### rive.get_state_machine
*Type:* FUNCTION
Returns the active state machine handle for the component.

**Parameters**

- `url` (url) - Component whose active state machine to query.

### rive.set_view_model_instance
*Type:* FUNCTION
Selects a default view model instance by name.

**Parameters**

- `url` (url) - Component owning the view model instance.
- `name` (string) - View model name whose default instance should be activated.

### rive.get_view_model_instance
*Type:* FUNCTION
Returns the handle of the currently bound view model instance.

**Parameters**

- `url` (url) - Component whose view model instance handle to query.
