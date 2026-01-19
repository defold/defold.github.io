# Buffer

**Namespace:** `buffer`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_buffer.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_buffer.cpp`

Functions for manipulating buffers and streams

## API

### buffer.copy_buffer
*Type:* FUNCTION
Copy all data streams from one buffer to another, element wise.
 Each of the source streams must have a matching stream in the
destination buffer. The streams must match in both type and size.
The source and destination buffer can be the same.

**Parameters**

- `dst` (buffer) - the destination buffer
- `dstoffset` (number) - the offset to start copying data to
- `src` (buffer) - the source data buffer
- `srcoffset` (number) - the offset to start copying data from
- `count` (number) - the number of elements to copy

**Examples**

How to copy elements (e.g. vertices) from one buffer to another
```
-- copy entire buffer
buffer.copy_buffer(dstbuffer, 0, srcbuffer, 0, #srcbuffer)

-- copy last 10 elements to the front of another buffer
buffer.copy_buffer(dstbuffer, 0, srcbuffer, #srcbuffer - 10, 10)

```

### buffer.copy_stream
*Type:* FUNCTION
Copy a specified amount of data from one stream to another.
 The value type and size must match between source and destination streams.
The source and destination streams can be the same.

**Parameters**

- `dst` (bufferstream) - the destination stream
- `dstoffset` (number) - the offset to start copying data to (measured in value type)
- `src` (bufferstream) - the source data stream
- `srcoffset` (number) - the offset to start copying data from (measured in value type)
- `count` (number) - the number of values to copy (measured in value type)

**Examples**

How to update a texture of a sprite:
```
-- copy entire stream
local srcstream = buffer.get_stream(srcbuffer, hash("xyz"))
local dststream = buffer.get_stream(dstbuffer, hash("xyz"))
buffer.copy_stream(dststream, 0, srcstream, 0, #srcstream)

```

### buffer.create
*Type:* FUNCTION
Create a new data buffer containing a specified set of streams. A data buffer
can contain one or more streams with typed data. This is useful for managing
compound data, for instance a vertex buffer could contain separate streams for
vertex position, color, normal etc.

**Parameters**

- `element_count` (number) - The number of elements the buffer should hold
- `declaration` (table) - A table where each entry (table) describes a stream
<ul>
<li><span class="type">hash | string</span> <code>name</code>: The name of the stream</li>
<li><span class="type">constant</span> <code>type</code>: The data type of the stream</li>
<li><span class="type">number</span> <code>count</code>: The number of values each element should hold</li>
</ul>

**Returns**

- `buffer` (buffer) - the new buffer

**Examples**

How to create and initialize a buffer
```
function init(self)
  local size = 128
  self.image = buffer.create( size * size, { {name=hash("rgb"), type=buffer.VALUE_TYPE_UINT8, count=3 } })
  self.imagestream = buffer.get_stream(self.image, hash("rgb"))

  for y=0,self.height-1 do
     for x=0,self.width-1 do
         local index = y * self.width * 3 + x * 3 + 1
         self.imagestream[index + 0] = self.r
         self.imagestream[index + 1] = self.g
         self.imagestream[index + 2] = self.b
     end
  end

```

### buffer.get_bytes
*Type:* FUNCTION
Get a copy of all the bytes from a specified stream as a Lua string.

**Parameters**

- `buffer` (buffer) - the source buffer
- `stream_name` (hash) - the name of the stream

**Returns**

- `data` (string) - the buffer data as a Lua string

### buffer.get_metadata
*Type:* FUNCTION
Get a named metadata entry from a buffer along with its type.

**Parameters**

- `buf` (buffer) - the buffer to get the metadata from
- `metadata_name` (hash | string) - name of the metadata entry

**Returns**

- `values` (table | nil) - table of metadata values or <code>nil</code> if the entry does not exist
- `value_type` (constant | nil) - numeric type of values or <code>nil</code>

**Examples**

How to get a metadata entry from a buffer
```
-- retrieve a metadata entry named "somefloats" and its nomeric type
local values, type = buffer.get_metadata(buf, hash("somefloats"))
if metadata then print(#metadata.." values in 'somefloats'") end

```

### buffer.get_stream
*Type:* FUNCTION
Get a specified stream from a buffer.

**Parameters**

- `buffer` (buffer) - the buffer to get the stream from
- `stream_name` (hash | string) - the stream name

**Returns**

- `stream` (bufferstream) - the data stream

### buffer.set_metadata
*Type:* FUNCTION
Creates or updates a metadata array entry on a buffer.
 The value type and count given when updating the entry should match those used when first creating it.

**Parameters**

- `buf` (buffer) - the buffer to set the metadata on
- `metadata_name` (hash | string) - name of the metadata entry
- `values` (table) - actual metadata, an array of numeric values
- `value_type` (constant) - type of values when stored

**Examples**

How to set a metadata entry on a buffer
```
-- create a new metadata entry with three floats
buffer.set_metadata(buf, hash("somefloats"), {1.5, 3.2, 7.9}, buffer.VALUE_TYPE_FLOAT32)
-- ...
-- update to a new set of values
buffer.set_metadata(buf, hash("somefloats"), {-2.5, 10.0, 32.2}, buffer.VALUE_TYPE_FLOAT32)

```

### buffer.VALUE_TYPE_FLOAT32
*Type:* CONSTANT
Float, single precision, 4 bytes

### buffer.VALUE_TYPE_INT16
*Type:* CONSTANT
Signed integer, 2 bytes

### buffer.VALUE_TYPE_INT32
*Type:* CONSTANT
Signed integer, 4 bytes

### buffer.VALUE_TYPE_INT64
*Type:* CONSTANT
Signed integer, 8 bytes

### buffer.VALUE_TYPE_INT8
*Type:* CONSTANT
Signed integer, 1 byte

### buffer.VALUE_TYPE_UINT16
*Type:* CONSTANT
Unsigned integer, 2 bytes

### buffer.VALUE_TYPE_UINT32
*Type:* CONSTANT
Unsigned integer, 4 bytes

### buffer.VALUE_TYPE_UINT64
*Type:* CONSTANT
Unsigned integer, 8 bytes

### buffer.VALUE_TYPE_UINT8
*Type:* CONSTANT
Unsigned integer, 1 byte
