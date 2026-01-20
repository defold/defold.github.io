# extension-safearea

**Namespace:** `safearea`
**Language:** Lua
**Type:** Extension

Defold native extension that will change the view/render of a game to fit into the safe area on iPhones and Android(API 28+) with notch.

## API

### safearea.set_background_color
*Type:* FUNCTION
set background color in runtime

**Parameters**

- `color` (vector4) - Color will be used as background color.

### safearea.get_insets
*Type:* FUNCTION
returns table with top, left, right, bottom values of insets and status

**Returns**

- `table`

### safearea.get_corners_radius
*Type:* FUNCTION
returns a table with `top_left`, `top_right`, `bottom_left`, and `bottom_right` values of rounded corners and status.

**Returns**

- `table`

### STATUS_OK
*Type:* VARIABLE

### STATUS_NOT_AVAILABLE
*Type:* VARIABLE

### STATUS_NOT_READY_YET
*Type:* VARIABLE
