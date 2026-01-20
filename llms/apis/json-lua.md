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
- `options` (table) (optional) - table with decode options
<ul>
<li><span class="type">boolean</span> <code>decode_null_as_userdata</code>: wether to decode a JSON null value as json.null or nil (default is nil)</li>
</ul>

**Returns**

- `data` (table) - decoded json

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

### json.encode
*Type:* FUNCTION
Encode a lua table to a JSON string.
A Lua error is raised for syntax errors.

**Parameters**

- `tbl` (table) - lua table to encode
- `options` (table) (optional) - table with encode options
<ul>
<li><span class="type">string</span> <code>encode_empty_table_as_object</code>: wether to encode an empty table as an JSON object or array (default is object)</li>
</ul>

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

### json.null
*Type:* VARIABLE
Represents the null primitive from a json file
