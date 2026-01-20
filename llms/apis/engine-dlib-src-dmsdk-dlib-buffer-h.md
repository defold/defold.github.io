# Buffer

**Namespace:** `dmBuffer`
**Language:** C++
**Type:** Defold C++
**File:** `buffer.h`
**Source:** `engine/dlib/src/dmsdk/dlib/buffer.h`
**Include:** `dmsdk/dlib/buffer.h`

Buffer API for data buffers as the main way to communicate between systems.

## API

### dmBuffer::Copy
*Type:* FUNCTION
Copies the data from one buffer to another buffer. The stream declaration needs to be the same in both buffers.

**Parameters**

- `dst_buffer_handle` (dmBuffer::HBuffer*) - Pointer to HBuffer from where to copy buffer data.
- `src_buffer_handle` (dmBuffer::HBuffer*) - Pointer to HBuffer where to copy the buffer data.

**Returns**

- `result` (dmBuffer::Result) - BUFFER_OK if buffer was copied successfully

**Examples**

```
dmBuffer::Result r = dmBuffer::Copy(buffer_a, buffer_b);

if (r == dmBuffer::RESULT_OK) {
    // success
} else {
    // handle error
}

```

### dmBuffer::Create
*Type:* FUNCTION
Creates a new HBuffer with a number of different streams.

**Parameters**

- `count` (uint32_t) - The number of "structs" the buffer should hold (e.g. vertex count)
- `streams_decl` (const dmBuffer::StreamDeclaration*) - Array of stream declarations
- `streams_decl_count` (uint8_t) - Number of stream declarations inside the decl array (max 256)
- `out_buffer` (dmBuffer::HBuffer*) - Pointer to HBuffer where to store the newly allocated buffer

**Returns**

- `result` (dmBuffer::Result) - BUFFER_OK if buffer was allocated successfully

**Examples**

```
const dmBuffer::StreamDeclaration streams_decl[] = {
    {dmHashString64("position"), dmBuffer::VALUE_TYPE_FLOAT32, 3},
    {dmHashString64("texcoord0"), dmBuffer::VALUE_TYPE_UINT16, 2},
    {dmHashString64("color"), dmBuffer::VALUE_TYPE_UINT8, 4},
};
dmBuffer::HBuffer buffer = 0x0;
dmBuffer::Result r = dmBuffer::Create(1024, streams_decl, 3, &buffer);

if (r == dmBuffer::RESULT_OK) {
    // success
} else {
    // handle error
}

```

### dmBuffer::Destroy
*Type:* FUNCTION
Destroys a HBuffer and it's streams.

**Parameters**

- `buffer` (dmBuffer::HBuffer) - Buffer handle to the buffer to free

**Examples**

```
const dmBuffer::StreamDeclaration streams_decl[] = {
    {dmHashString64("position"), dmBuffer::VALUE_TYPE_FLOAT32, 3},
};
dmBuffer::HBuffer buffer = 0x0;
dmBuffer::Result r = dmBuffer::Create(4, streams_decl, 1, &buffer);

if (r == dmBuffer::RESULT_OK) {
    dmBuffer::Destroy(buffer);
} else {
    // handle error
}

```

### dmBuffer::GetBytes
*Type:* FUNCTION
Gets the buffer as a byte array. If the buffer is interleaved (default), a pointer to the whole memory is returned.

**Parameters**

- `buffer` (dmBuffer::HBuffer) - buffer handle.
- `out_bytes` (void**) - Pointer to void* where to store the bytes
- `out_size` (uint32_t*) - Pointer to uint32_t where to store the array size

**Returns**

- `result` (dmBuffer::Result) - BUFFER_OK if the buffer was successfully accessed

**Examples**

```
uint8_t* bytes = 0x0;
uint32_t size = 0;

dmBuffer::Result r = dmBuffer::GetBytes(buffer, (void**)&bytes, &size);

if (r == dmBuffer::RESULT_OK) {
    for (int i = 0; i < size; ++i)
    {
        stream[i] = (uint8_t)(i & 0xFF);
    }
} else {
    // handle error
}

```

### dmBuffer::GetContentVersion
*Type:* FUNCTION
Gets the current update number

**Parameters**

- `type` (dmBuffer::HBuffer) - The value type
- `version` (uint32_t*) - The current version number

**Returns**

- `result` (dmBuffer::Result) - Returns BUFFER_OK if all went ok

### dmBuffer::GetCount
*Type:* FUNCTION
Get (struct) count for a buffer.

**Parameters**

- `buffer` (dmBuffer::HBuffer) - buffer handle.
- `count` (uint32_t*) - Pointer to uint32_t where to store the element count

**Returns**

- `result` (dmBuffer::Result) - BUFFER_OK if the element count was successfully accessed

**Examples**

```
uint32_t count = 0;
dmBuffer::Result r = dmBuffer::GetCount(buffer, &count);

if (r == dmBuffer::RESULT_OK) {
    printf("buffer %p has %d number of elements", buffer, count);
} else {
    // handle error
}

```

### dmBuffer::GetMetaData
*Type:* FUNCTION
Retrieve metadata entry information

**Parameters**

- `hbuffer` (dmBuffer::HBuffer) - A buffer handle
- `name_hash` (dmhash_t) - The entry name as a hash
- `data` (void**) - Gets the internal address of metadata values
- `count` (uint32_t) - Gets the number of metadata values stored
- `type` (dmBuffer::ValueType) - Gets the type of values of the metadata

### dmBuffer::GetResultString
*Type:* FUNCTION
Converts result to string

**Parameters**

- `result` (dmBuffer::Result) - The result

**Returns**

- `result` (const char*) - The result as a string

### dmBuffer::GetSizeForValueType
*Type:* FUNCTION
Gets the size of a value type

**Parameters**

- `type` (dmBuffer::ValueType) - The value type

**Returns**

- `size` (uint32_t) - The size in bytes

### dmBuffer::GetStream
*Type:* FUNCTION
Get a stream from a buffer. Output stream is 16 byte aligned.

**Parameters**

- `buffer` (dmBuffer::HBuffer) - buffer handle.
- `stream_name` (dmhash_t) - Hash of stream name to get
- `stream` (void**) - Where to store the stream
- `count` (uint32_t*) - Where to store the count (e.g. vertex count). May be null.
- `components` (uint32_t*) - Where to store the number of components (e.g. 3 for a Vector3). May be null.
- `stride` (uint32_t*) - Where to store the (struct) stride. The stride can be added to the value pointer. May be null.
E.g. for a float array, the stride is (sizeof(Struct) / sizeof(float))

**Returns**

- `result` (dmBuffer::Result) - BUFFER_OK if the stream was successfully accessed

**Examples**

```
float* positions = 0x0;
uint32_t size = 0;
uint32_t components = 0;
uint32_t stride = 0;
dmBuffer::Result r = dmBuffer::GetStream(buffer, dmHashString64("position"), (void**)&positions, &count, &components, &stride);

if (r == dmBuffer::RESULT_OK) {
    for (int i = 0; i < count; ++i)
    {
        for (int c = 0; c < components; ++c)
        {
             positions[c] *= 1.1f;
        }
        positions += stride;
    }
} else {
    // handle error
}

```

### dmBuffer::GetStreamType
*Type:* FUNCTION
Gets the stream type

**Parameters**

- `buffer` (dmBuffer::HBuffer) - Pointer to a buffer.
- `stream_name` (dmhash_t) - Hash of stream name to get
- `type` (dmBuffer::ValueType*) - The value type
- `components` (uint32_t*) - The number of values (E.g. 3 for a Vector3)

**Returns**

- `result` (dmBuffer::Result) - Returns BUFFER_OK if all went ok

### dmBuffer::GetValueTypeString
*Type:* FUNCTION
Converts a value type to string

**Parameters**

- `result` (dmBuffer::ValueType) - The value type

**Returns**

- `result` (const char*) - The value type as a string

### dmBuffer::HBuffer
*Type:* TYPEDEF
```
typedef uint32_t HBuffer;

```

### dmBuffer::IsBufferValid
*Type:* FUNCTION
Checks if a handle is still valid

**Parameters**

- `buffer` (dmBuffer::HBuffer) - The buffer

**Returns**

- `result` (bool) - True if the handle is valid

### dmBuffer::SetMetaData
*Type:* FUNCTION
Create or update a new metadata entry with a number of values of a specific type.
It will allocate space to store these values.

**Parameters**

- `hbuffer` (dmBuffer::HBuffer) - A buffer handle
- `name_hash` (dmhash_t) - The entry name as a hash
- `data` (void*) - A pointer to an array of the values
- `count` (uint32_t) - Number of values in the array
- `type` (dmBuffer::ValueType) - The type of the values

**Returns**

- `result` (dmBuffer::Result) - RESULT_OK if the metadata entry was successfully stored

### dmBuffer::StreamDeclaration
*Type:* STRUCT
Buffer stream declaration structure

**Members**

- `m_Name` (dmhash_t) - Hash of stream name
- `m_Type` (dmBuffer::ValueType) - Stream ValueType type
- `m_Count` (uint8_t) - Component count of stream type. E.g. 3 for a Vector3
- `m_Flags` (uint32_t) - Flags for a stream.
- `m_Reserved` (uint32_t) - Reserved for future use.

**Examples**

Declare a typical position stream:
```
const dmBuffer::StreamDeclaration streams_decl[] = {
    {dmHashString64("position"), dmBuffer::VALUE_TYPE_FLOAT32, 3}
};

```

### dmBuffer::UpdateContentVersion
*Type:* FUNCTION
Used to know if a buffer has been updated.

**Parameters**

- `type` (dmBuffer::HBuffer) - The value type

**Returns**

- `result` (dmBuffer::Result) - Returns BUFFER_OK if all went ok

### dmBuffer::ValidateBuffer
*Type:* FUNCTION
Validate a buffer and it's streams.

**Parameters**

- `buffer` (dmBuffer::HBuffer) - Buffer handle to the buffer to validate

**Examples**

```
// Pass buffer to third party library that does operations on the buffer or streams.
ThirdPartyLib::PerformOperation(buffer);

r = dmBuffer::ValidateBuffer(buffer);
if (r == dmBuffer::RESULT_OK) {
    // buffer and streams are valid
} else {
    // the third party lib made the buffer invalid
}

```

### Result
*Type:* ENUM
Result enumeration.

**Members**

- `dmBuffer::RESULT_OK`
- `dmBuffer::RESULT_GUARD_INVALID`
- `dmBuffer::RESULT_ALLOCATION_ERROR`
- `dmBuffer::RESULT_BUFFER_INVALID`
- `dmBuffer::RESULT_BUFFER_SIZE_ERROR`
- `dmBuffer::RESULT_STREAM_SIZE_ERROR`
- `dmBuffer::RESULT_STREAM_MISSING`
- `dmBuffer::RESULT_STREAM_TYPE_MISMATCH`
- `dmBuffer::RESULT_STREAM_COUNT_MISMATCH`
- `dmBuffer::RESULT_METADATA_INVALID`
- `dmBuffer::RESULT_METADATA_MISSING`

### ValueType
*Type:* ENUM
ValueType enumeration.

**Members**

- `dmBuffer::VALUE_TYPE_UINT8`
- `dmBuffer::VALUE_TYPE_UINT16`
- `dmBuffer::VALUE_TYPE_UINT32`
- `dmBuffer::VALUE_TYPE_UINT64`
- `dmBuffer::VALUE_TYPE_INT8`
- `dmBuffer::VALUE_TYPE_INT16`
- `dmBuffer::VALUE_TYPE_INT32`
- `dmBuffer::VALUE_TYPE_INT64`
- `dmBuffer::VALUE_TYPE_FLOAT32`
- `dmBuffer::MAX_VALUE_TYPE_COUNT`
