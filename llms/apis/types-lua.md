# Types

**Namespace:** `types`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_types.cpp`
**Source:** `engine/script/src/script_types.cpp`

Functions for checking Defold userdata types.

## API

### types.is_hash
*Type:* FUNCTION
Check if passed type is hash.

**Parameters**

- `var` (any) - Variable to check type

**Returns**

- `result` (boolean) - True if passed type is hash

### types.is_matrix4
*Type:* FUNCTION
Check if passed type is matrix4.

**Parameters**

- `var` (any) - Variable to check type

**Returns**

- `result` (boolean) - True if passed type is matrix4

### types.is_quat
*Type:* FUNCTION
Check if passed type is quaternion.

**Parameters**

- `var` (any) - Variable to check type

**Returns**

- `result` (boolean) - True if passed type is quaternion

### types.is_url
*Type:* FUNCTION
Check if passed type is URL.

**Parameters**

- `var` (any) - Variable to check type

**Returns**

- `result` (boolean) - True if passed type is URL

### types.is_vector
*Type:* FUNCTION
Check if passed type is vector.

**Notes**

- 'vector3' and 'vector4' types is not a 'vector' type under the hood.
So if called `types.is_vector(vmath.vector3())` it returns 'false'

**Parameters**

- `var` (any) - Variable to check type

**Returns**

- `result` (boolean) - True if passed type is vector

### types.is_vector3
*Type:* FUNCTION
Check if passed type is vector3.

**Parameters**

- `var` (any) - Variable to check type

**Returns**

- `result` (boolean) - True if passed type is vector3

### types.is_vector4
*Type:* FUNCTION
Check if passed type is vector4.

**Parameters**

- `var` (any) - Variable to check type

**Returns**

- `result` (boolean) - True if passed type is vector4
