# Built-ins

**Namespace:** `builtins`
**Language:** Lua
**Type:** Defold Lua
**File:** `script.cpp`
**Source:** `engine/script/src/script.cpp`

Built-in scripting functions.

## API

### hash
*Type:* FUNCTION
All ids in the engine are represented as hashes, so a string needs to be hashed
before it can be compared with an id.

**Parameters**

- `s` (string) - string to hash

**Returns**

- `hash` (hash) - a hashed string

**Examples**

To compare a message_id in an on-message callback function:
```
function on_message(self, message_id, message, sender)
    if message_id == hash("my_message") then
        -- Act on the message here
    end
end

```

### hash_to_hex
*Type:* FUNCTION
Returns a hexadecimal representation of a hash value.
The returned string is always padded with leading zeros.

**Parameters**

- `h` (hash) - hash value to get hex string for

**Returns**

- `hex` (string) - hex representation of the hash

**Examples**

```
local h = hash("my_hash")
local hexstr = hash_to_hex(h)
print(hexstr) --> a2bc06d97f580aab

```

### pprint
*Type:* FUNCTION
Pretty printing of Lua values. This function prints Lua values
in a manner similar to +print()+, but will also recurse into tables
and pretty print them. There is a limit to how deep the function
will recurse.

**Parameters**

- `v` (any) - value to print

**Examples**

Pretty printing a Lua table with a nested table:
```
local t2 = { 1, 2, 3, 4 }
local t = { key = "value", key2 = 1234, key3 = t2 }
pprint(t)

```

Resulting in the following output (note that the key order in non array
Lua tables is undefined):
```
{
  key3 = {
    1 = 1,
    2 = 2,
    3 = 3,
    4 = 4,
  }
  key2 = 1234,
  key = value,
}

```
