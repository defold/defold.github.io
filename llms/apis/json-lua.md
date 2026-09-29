# JSON

**Namespace:** `json`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_json.cpp`
**Source:** `engine/script/src/script_json.cpp`

Manipulation of JSON data strings.

## API

### json.decode
*Type:* FUNCTION
Decode a string of JSON data into a Lua table.
A Lua error is raised for syntax errors.

**Parameters**

- `json` (string) - json data
- `options` (json.decode_options) (optional) - optional decoding options

**Returns**

- `data` (any) - decoded JSON value

**Examples**

Converting a string containing JSON data into a Lua table:
```
function init(self)
    local jsonstring = '{"persons":[{"name":"John Doe"},{"name":"Darth Vader"}]}'
    local data = json.decode(jsonstring)
    pprint(data)
end

```

Results in the following printout:
```
{
  persons = {
    1 = {
      name = John Doe,
    }
    2 = {
      name = Darth Vader,
    }
  }
}

```

### json.decode_options
*Type:* STRUCT
JSON decoding options

**Members**

- `decode_null_as_userdata?` (boolean) - Decode JSON <code>null</code> as <a href="/ref/json#json.null">json.null</a> instead of <code>nil</code>.

### json.encode
*Type:* FUNCTION
Encode a lua table to a JSON string.
A Lua error is raised for syntax errors.

**Parameters**

- `tbl` (any) - Lua value to encode
- `options` (json.encode_options) (optional) - optional encoding options

**Returns**

- `json` (string) - encoded json

**Examples**

Convert a lua table to a JSON string:
```
function init(self)
     local tbl = {
          persons = {
               { name = "John Doe"},
               { name = "Darth Vader"}
          }
     }
     local jsonstring = json.encode(tbl)
     pprint(jsonstring)
end

```

Results in the following printout:
```
{"persons":[{"name":"John Doe"},{"name":"Darth Vader"}]}

```

### json.encode_options
*Type:* STRUCT
JSON encoding options

**Members**

- `encode_empty_table_as_object?` (boolean) - Encode an empty table as an object instead of an array. The default is true.

### json.null
*Type:* VARIABLE
Represents the null primitive from a json file
