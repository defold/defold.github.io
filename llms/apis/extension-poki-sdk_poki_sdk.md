# extension-poki-sdk

**Namespace:** `poki_sdk`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Poki SDK APIs

## API

### poki_sdk.gameplay_start
*Type:* FUNCTION
Signals that gameplay has started.

### poki_sdk.gameplay_stop
*Type:* FUNCTION
Signals that gameplay has stopped.

### poki_sdk.commercial_break
*Type:* FUNCTION
Requests a commercial break. The callback reports START if an ad starts and SUCCESS when Poki's commercial-break promise resolves.

**Parameters**

- `callback` (function)
  - `self` (object) - The calling script instance
  - `status` (number) - One of the statuses: `poki_sdk.COMMERCIAL_BREAK_START`, `poki_sdk.COMMERCIAL_BREAK_SUCCESS`

### poki_sdk.rewarded_break
*Type:* FUNCTION
Requests a rewarded break. The size argument is optional and defaults to small. Call it as rewarded_break(callback) or rewarded_break(size, callback).

**Parameters**

- `size` (string | nil) - Optional reward size. Accepted values are small, medium, and large. Defaults to small.
- `callback` (function)
  - `self` (object) - The calling script instance
  - `status` (number) - One of the statuses: `poki_sdk.REWARDED_BREAK_ERROR`, `poki_sdk.REWARDED_BREAK_START`, `poki_sdk.REWARDED_BREAK_SUCCESS`

### poki_sdk.set_debug
*Type:* FUNCTION
Enables or disables Poki SDK debug mode.

**Parameters**

- `is_debug` (boolean)

### poki_sdk.capture_error
*Type:* FUNCTION
Captures and reports an error to Poki.

**Parameters**

- `error` (string)

### poki_sdk.is_ad_blocked
*Type:* FUNCTION
Deprecated: Poki no longer exposes ad-block detection. This compatibility function always returns false.

**Returns**

- `boolean` - Always false.

### poki_sdk.shareable_url
*Type:* FUNCTION
Generates a shareable URL with the supplied parameters.

**Parameters**

- `params` (table) - String or number values to include in the generated URL.
- `callback` (function)
  - `self` (object) - The calling script instance
  - `url` (string) - The generated shareable URL.

### poki_sdk.get_url_param
*Type:* FUNCTION
Returns the URL parameter value provided by Poki. The Defold bridge maps a null or undefined result to nil.

**Parameters**

- `key` (string)

**Returns**

- `['string', 'nil']` - The parameter value, or nil when the Poki result is null or undefined.

### poki_sdk.measure
*Type:* FUNCTION
Sends a custom analytics event to Poki. Use start/complete/fail for progress, visible/interact for offer and UI engagement, or a custom action for other events. Do not duplicate commercial or rewarded ad playback and outcomes; Poki tracks those through the ad calls. The binding defaults omitted `what` and `action` to empty strings for compatibility.

**Parameters**

- `category` (string)
- `what` (string | nil) - Optional event subject. Defaults to an empty string when omitted.
- `action` (string | nil) - Optional event action. Defaults to an empty string when omitted.

### poki_sdk.move_pill
*Type:* FUNCTION
Moves the Poki pill to a different vertical position.

**Parameters**

- `topPercent` (number) - Position from the top in percent.
- `topPx` (number) - Additional position offset in pixels.

### poki_sdk.get_user
*Type:* FUNCTION
Retrieves the currently logged-in Poki user.

**Parameters**

- `callback` (function)
  - `self` (object) - The calling script instance
  - `user` (table | nil) - A table with username and avatar_url, or nil if no user is logged in.
  - `error` (string | nil) - The rejection message, or nil if the request completed normally.

### poki_sdk.get_token
*Type:* FUNCTION
Retrieves the Poki auth token for the currently logged-in user.

**Parameters**

- `callback` (function)
  - `self` (object) - The calling script instance
  - `token` (string | nil) - The short-lived Poki auth token, or nil if no user is logged in.
  - `error` (string | nil) - The rejection message, or nil if the request completed normally.

### poki_sdk.login
*Type:* FUNCTION
Prompts the player to log in to their Poki account.

**Parameters**

- `callback` (function)
  - `self` (object) - The calling script instance
  - `success` (boolean) - `true` if the login promise resolved, otherwise `false`.
  - `error` (string | nil) - The rejection message on failure, or nil on success.

### poki_sdk.open_external_link
*Type:* FUNCTION
Opens an external link in a new browser tab for user-initiated external navigation.

**Parameters**

- `url` (string)

### COMMERCIAL_BREAK_SUCCESS
*Type:* VARIABLE
A commercial break finished or did not display.

### COMMERCIAL_BREAK_START
*Type:* VARIABLE
A commercial break started.

### REWARDED_BREAK_ERROR
*Type:* VARIABLE
A rewarded break failed or the reward should not be granted.

### REWARDED_BREAK_SUCCESS
*Type:* VARIABLE
A rewarded break completed and the reward may be granted.

### REWARDED_BREAK_START
*Type:* VARIABLE
A rewarded break started.
