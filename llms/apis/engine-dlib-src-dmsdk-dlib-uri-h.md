# URI

**Namespace:** `dmURI`
**Language:** C++
**Type:** Defold C++
**File:** `uri.h`
**Source:** `engine/dlib/src/dmsdk/dlib/uri.h`
**Include:** `dmsdk/dlib/uri.h`

URI functions.

## API

### dmURI::Decode
*Type:* FUNCTION
Decodes an URL encoded buffer

**Notes**

- The output will never be larger than the input.

**Parameters**

- `src` (const char*) - Input
- `dst` (char*) - Decoded output

### dmURI::Encode
*Type:* FUNCTION
Performs URL encoding of the supplied buffer

**Notes**

- If dst=0 the bytes_written will return the number of required bytes (including null character)

**Parameters**

- `src` (const char*) - string to encode
- `dst` (char*) - the destination buffer
- `dst_size` (uint32_t) - size of the provided out buffer
- `bytes_written[out]` (uint32_t) - number of bytes written

### dmURI::Parse
*Type:* FUNCTION
Parse URI and split in three parts. (scheme, location, path)

**Notes**

- This is a simplified URI parser and does not conform to rfc2396.
      Missing features are: parameters, query, fragment part of URI and support for escaped sequences
- For http m_Port is set to 80 if not specified in uri.

**Parameters**

- `uri` (const char*) - URI to parse
- `parts` (dmURI::Parts) - Result

**Returns**

- `RESULT_OK` - on success

### dmURI::Parts
*Type:* STRUCT
URI parsing result parts

### dmURI::Result
*Type:* FUNCTION
URI parsing result
