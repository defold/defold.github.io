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

- `dst` (buffer_data) - the destination buffer
- `dstoffset` (number) - the offset to start copying data to
- `src` (buffer_data) - the source data buffer
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

- `dst` (buffer_stream) - the destination stream
- `dstoffset` (number) - the offset to start copying data to (measured in value type)
- `src` (buffer_stream) - the source data stream
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
- `declaration` (({ name:hash|string, type:buffer.VALUE_TYPE, count:number })[]) - A table where each entry (table) describes a stream
<ul>
<li><span class="type"><a href="../builtins-lua/#hash">hash</a> | <a href="../../../manuals/lua/#variables-and-data-types">string</a></span> <code>name</code>: The name of the stream</li>
<li><span class="type"><a href="#buffer.VALUE_TYPE">buffer.VALUE_TYPE</a></span> <code>type</code>: The data type of the stream</li>
<li><span class="type"><a href="../../../manuals/lua/#variables-and-data-types">number</a></span> <code>count</code>: The number of values each element should hold</li>
</ul>

**Returns**

- `buffer` (buffer_data) - the new buffer

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

- `buffer` (buffer_data) - the source buffer
- `stream_name` (hash) - the name of the stream

**Returns**

- `data` (string) - the buffer data as a Lua string

### buffer.get_metadata
*Type:* FUNCTION
Get a named metadata entry from a buffer along with its type.

**Parameters**

- `buf` (buffer_data) - the buffer to get the metadata from
- `metadata_name` (hash | string) - name of the metadata entry

**Returns**

- `values` (number[] | nil) - table of metadata values or <code>nil</code> if the entry does not exist
- `value_type` (buffer.VALUE_TYPE | nil) - numeric type of values or <code>nil</code>

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

- `buffer` (buffer_data) - the buffer to get the stream from
- `stream_name` (hash | string) - the stream name

**Returns**

- `stream` (buffer_stream) - the data stream

### buffer.set_metadata
*Type:* FUNCTION
Creates or updates a metadata array entry on a buffer.
 The value type and count given when updating the entry should match those used when first creating it.

**Parameters**

- `buf` (buffer_data) - the buffer to set the metadata on
- `metadata_name` (hash | string) - name of the metadata entry
- `values` (number[]) - actual metadata, an array of numeric values
- `value_type` (buffer.VALUE_TYPE) - type of values when stored

**Examples**

How to set a metadata entry on a buffer
```
-- create a new metadata entry with three floats
buffer.set_metadata(buf, hash("somefloats"), {1.5, 3.2, 7.9}, buffer.VALUE_TYPE_FLOAT32)
-- ...
-- update to a new set of values
buffer.set_metadata(buf, hash("somefloats"), {-2.5, 10.0, 32.2}, buffer.VALUE_TYPE_FLOAT32)

```

### buffer.VALUE_TYPE
*Type:* ENUM
Buffer value types

**Members**

- `buffer.VALUE_TYPE_FLOAT32` - float32 Float, single precision, 4 bytes
- `buffer.VALUE_TYPE_INT16` - int16 Signed integer, 2 bytes
- `buffer.VALUE_TYPE_INT32` - int32 Signed integer, 4 bytes
- `buffer.VALUE_TYPE_INT64` - int64 Signed integer, 8 bytes
- `buffer.VALUE_TYPE_INT8` - int8 Signed integer, 1 byte
- `buffer.VALUE_TYPE_UINT16` - uint16 Unsigned integer, 2 bytes
- `buffer.VALUE_TYPE_UINT32` - uint32 Unsigned integer, 4 bytes
- `buffer.VALUE_TYPE_UINT64` - uint64 Unsigned integer, 8 bytes
- `buffer.VALUE_TYPE_UINT8` - uint8 Unsigned integer, 1 byte

### buffer_data
*Type:* TYPEDEF
A buffer stores one or more named streams of typed values. Create a buffer
with buffer.create, or obtain one from APIs such as
resource.get_buffer, sys.load_buffer, or image.load. Use
buffer.get_stream to access the values in an individual stream.

**Parameters**

- `value` (userdata) - typed data buffer

**Examples**

```
local vertices = buffer.create(3, {
    { name = hash("position"), type = buffer.VALUE_TYPE_FLOAT32, count = 3 }
})

```

### buffer_stream
*Type:* TYPEDEF
An indexable view of one named stream in a buffer_data. Obtain a
stream with buffer.get_stream. Reading or writing the stream accesses
the values in its underlying buffer.

**Parameters**

- `value` (userdata) - named buffer stream

**Examples**

```
local vertices = buffer.create(1, {
    { name = hash("position"), type = buffer.VALUE_TYPE_FLOAT32, count = 3 }
})
local positions = buffer.get_stream(vertices, "position")
positions[1] = 10
positions[2] = 20
positions[3] = 0

```
