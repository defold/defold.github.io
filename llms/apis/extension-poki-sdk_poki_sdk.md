# extension-poki-sdk

**Namespace:** `poki_sdk`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Poki SDK APIs

## API

### poki_sdk.gameplay_start
*Type:* FUNCTION

### poki_sdk.gameplay_stop
*Type:* FUNCTION

### poki_sdk.commercial_break
*Type:* FUNCTION

**Parameters**

- `callback` (function)

### poki_sdk.rewarded_break
*Type:* FUNCTION

**Parameters**

- `size` (string) - The size of the reward. Accepted values are small, medium and large. Optional. Default is small.
- `callback` (function)
  - `self` (object) - The calling script instance
  - `status` (number) - One of the statuses: `poki_sdk.REWARDED_BREAK_ERROR`, `poki_sdk.REWARDED_BREAK_START`, `poki_sdk.REWARDED_BREAK_SUCCESS`

### poki_sdk.set_debug
*Type:* FUNCTION

**Parameters**

- `is_debug` (boolean)

### poki_sdk.capture_error
*Type:* FUNCTION

**Parameters**

- `error` (string)

### poki_sdk.shareable_url
*Type:* FUNCTION

**Parameters**

- `params` (table)
- `callback` (function)

### poki_sdk.get_url_param
*Type:* FUNCTION

**Parameters**

- `key` (string)

### poki_sdk.measure
*Type:* FUNCTION

**Parameters**

- `category` (string)
- `what` (string)
- `action` (string)

### poki_sdk.move_pill
*Type:* FUNCTION

**Parameters**

- `topPercent` (number)
- `topPx` (number)

### REWARDED_BREAK_ERROR
*Type:* VARIABLE

### REWARDED_BREAK_SUCCESS
*Type:* VARIABLE

### REWARDED_BREAK_START
*Type:* VARIABLE
