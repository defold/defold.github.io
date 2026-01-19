# extension-iac

**Namespace:** `iac`
**Language:** Lua
**Type:** Extension

Functions and constants for doing inter-app communication. Supported on iOS and Android. [icon:ios] [icon:android]

## API

### iac.set_listener
*Type:* FUNCTION
Sets the listener function for inter-app communication events.

**Parameters**

- `self` (object) - The current object.
- `payload` (table) - The iac payload.
- `type` (number) - The type of iac, an iac.TYPE_ enumeration. It can be one of the predefined constants below
- `iac.TYPE_INVOCATION`

**Examples**

```
  local function iac_listener(self, payload, type)
       if type == iac.TYPE_INVOCATION then
           -- This was an invocation
           print(payload.origin) -- origin may be empty string if it could not be resolved
           print(payload.url)
       end
  end

  function init(self)
       iac.set_listener(iac_listener)
  end

```

### TYPE_INVOCATION
*Type:* VARIABLE
iac type
