# extension-permissions

**Namespace:** `permissions`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with permissions related APIs

## API

### permissions.check
*Type:* FUNCTION
Determine whether you have been granted a particular permission.

**Parameters**

- `permission` (string) - A constant that represent permission, for example `android.permission.ACCESS_NETWORK_STATE`

**Returns**

- `number` - A result can be one of the predefined constants below
- `permissions.PERMISSION_GRANTED`
- `permissions.PERMISSION_DENIED`
- `permissions.PERMISSION_SHOW_RATIONALE`

**Examples**

```
local result = permissions.check("android.permission.ACCESS_NETWORK_STATE")
if result == permissions.PERMISSION_DENIED then
    -- You can directly ask for the permission.
elseif result == permissions.PERMISSION_GRANTED then
    -- You can use the API that requires the permission.
elseif result == permissions.PERMISSION_SHOW_RATIONALE then
    -- In an educational UI, explain to the user why your app requires this
    -- permission for a specific feature to behave as expected, and what
    -- features are disabled if it's declined. In this UI, include a
    -- "cancel" or "no thanks" button that lets the user continue
    -- using your app without granting the permission.
end

```

### permissions.request
*Type:* FUNCTION
Requests permissions to be granted to this application.

**Parameters**

- `request_tbl` (table) - An array with constants that represent permissions.
- `callback` (function) - A callback taking the following parameters
  - `self` (object) - The calling script
  - `result` (table) - A table where key is permission string and key is one of the following constants
- `permissions.PERMISSION_GRANTED`
- `permissions.PERMISSION_DENIED`

**Examples**

```
local permissions_table = {"android.permission.WRITE_EXTERNAL_STORAGE", "android.permission.READ_CONTACTS"}
permissions.request(permissions_table,
    function(self, result)
        for permission, result in pairs(result) do
          if result == permissions.PERMISSION_DENIED then
              -- You can directly ask for the permission.
          elseif result == permissions.PERMISSION_GRANTED then
              -- You can use the API that requires the permission.
          elseif result == permissions.PERMISSION_SHOW_RATIONALE then
              -- In an educational UI, explain to the user why your app requires this
              -- permission for a specific feature to behave as expected, and what
              -- features are disabled if it's declined. In this UI, include a
              -- "cancel" or "no thanks" button that lets the user continue
              -- using your app without granting the permission.
          end
        end
    end)

```

### PERMISSION_GRANTED
*Type:* VARIABLE
The permission has been granted to the given package.

### PERMISSION_DENIED
*Type:* VARIABLE
The permission has not been granted to the given package.

### PERMISSION_SHOW_RATIONALE
*Type:* VARIABLE
Explain why your app needs the permission [Android doc](https://developer.android.com/training/permissions/requesting#explain)
