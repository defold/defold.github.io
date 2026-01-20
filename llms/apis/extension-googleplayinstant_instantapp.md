# extension-googleplayinstant

**Namespace:** `instantapp`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with InstantApp APIs

## API

### instantapp.show_install_prompt
*Type:* FUNCTION
Shows a dialog that allows the user to install the current instant app.

### instantapp.is_instant_app
*Type:* FUNCTION
Checks if application loaded as instant experience.

**Returns**

- `boolean` - Returns true if this application is an instant app.

### instantapp.get_cookie_max_size
*Type:* FUNCTION
Gets the maximum size in bytes of the cookie data an instant app can store on the device.

**Returns**

- `number` - The maximum size in bytes of the cookie data an instant app can store on the device.

### instantapp.get_cookie
*Type:* FUNCTION
Load byte array from cookies that were saved in instant application.

**Returns**

- `string` - The byte array data of cookies saved in instant application.

### instantapp.set_cookie
*Type:* FUNCTION
Save byte array in cookies to be able get access to this data in installable application.

**Parameters**

- `bytes` (string) - The byte array data will be saved in cookies for access in installable application.
