# Ddf

**Namespace:** `dmDDF`
**Language:** C++
**Type:** Defold C++
**File:** `ddf.h`
**Source:** `engine/ddf/src/dmsdk/ddf/ddf.h`
**Include:** `dmsdk/ddf/ddf.h`

SDK DDF (Defold Data Format) API documentation

## API

### Descriptor
*Type:* TYPEDEF
Opaque pointer that holds info about a message type.

### FreeMessage
*Type:* FUNCTION
Free message

**Parameters**

- `message` (void*) - The message

### GetDescriptorFromHash
*Type:* FUNCTION
Get Descriptor from hash name

**Parameters**

- `hash` (dmhash_t) - hash of type name

**Returns**

- `descriptor` (dmDDF::Descriptor*) - 0 if not found

### LoadMessage
*Type:* FUNCTION
Load/decode a DDF message from buffer

**Parameters**

- `buffer` (const void*) - Input buffer
- `buffer_size` (uint32_t) - Input buffer size in bytes
- `desc` (dmDDF::Descriptor*) - DDF descriptor
- `message` (void**) - (out) Destination pointer to message

**Returns**

- `RESULT_OK` - on success

### LoadMessage
*Type:* FUNCTION
Load/decode a DDF message from buffer

**Parameters**

- `buffer` (const void*) - Input buffer
- `buffer_size` (uint32_t) - Input buffer size in bytes
- `desc` (dmDDF::Descriptor*) - DDF descriptor
- `message` (void**) - (out) Destination pointer to message
- `options` (uint32_t) - options, eg dmDDF::OPTION_OFFSET_POINTERS
- `size` (uint32_t*) - (out) loaded message size

**Returns**

- `RESULT_OK` - on success

### LoadMessage<T>
*Type:* FUNCTION
Load/decode a DDF message from buffer. Template variant

**Template Parameters**

- `T`

**Parameters**

- `buffer` (const void*) - Input buffer
- `buffer_size` (uint32_t) - Input buffer size in bytes
- `message` (T**) - (out) Destination pointer to message

**Returns**

- `RESULT_OK` - on success

### LoadMessageFromFile
*Type:* FUNCTION
Load/decode a DDF message from file

**Parameters**

- `file_name` (const char*) - File name
- `desc` (dmDDF::Descriptor*) - DDF descriptor
- `message` (void**) - (out) Destination pointer to message

**Returns**

- `RESULT_OK` - on success

### OPTION_OFFSET_POINTERS
*Type:* CONSTANT
Store pointers as offset from base address. Needed when serializing entire messages (copy). Value (1 << 0)

### ResolvePointers
*Type:* FUNCTION
If the message was loaded with the flag dmDDF::OPTION_OFFSET_POINTERS, all pointers have their offset stored.
This function resolves those offsets into actual pointers

**Parameters**

- `desc` (dmDDF::Descriptor*) - DDF descriptor
- `message` (void*) - (int/out) The message to patch pointers in

**Returns**

- `RESULT_OK` - on success

### Result
*Type:* ENUM
Result enumeration.

**Members**

- `dmDDF::RESULT_OK` - = 0,
- `dmDDF::RESULT_FIELDTYPE_MISMATCH` - = 1,
- `dmDDF::RESULT_WIRE_FORMAT_ERROR` - = 2,
- `dmDDF::RESULT_IO_ERROR` - = 3,
- `dmDDF::RESULT_VERSION_MISMATCH` - = 4,
- `dmDDF::RESULT_MISSING_REQUIRED` - = 5,
- `dmDDF::RESULT_INTERNAL_ERROR` - = 1000,

### SaveMessageToArray
*Type:* FUNCTION
Save message to array

**Parameters**

- `message` (const void*) - Message
- `desc` (dmDDF::Descriptor*) - DDF descriptor
- `buffer` (dmArray<uint8_t>&) - Buffer to save to

**Returns**

- `RESULT_OK` - on success
