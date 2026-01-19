# Utf8

**Namespace:** `dmUtf8`
**Language:** C++
**Type:** Defold C++
**File:** `utf8.h`
**Source:** `engine/dlib/src/dmsdk/dlib/utf8.h`
**Include:** `dmsdk/dlib/utf8.h`

SDK Utf8 API documentation

## API

### IsBreaking
*Type:* FUNCTION
Checks if a codepoint is a breaking whitespace

**Parameters**

- `c` (uint32_t) - the codepoint

**Returns**

- `result` (bool) - true if it's a breaking whitespace

### IsWhiteSpace
*Type:* FUNCTION
Checks if a codepoint is a whitespace

**Parameters**

- `c` (uint32_t) - the codepoint

**Returns**

- `result` (bool) - true if it's a whitespace

### NextChar
*Type:* FUNCTION
Get next unicode character in utf-8 string. Iteration terminates at '\0' and repeated invocations will return '\0'

**Parameters**

- `str` (const char**) - Pointer to string. The pointer value is updated

**Returns**

- `chr` (uint32_t) - Decoded unicode character

**Examples**

```
const char* s = "åäöÅÄÖ";
char* cursor = s;
uint32_t codepoint = 0;
while (codepoint = dmUtf8::NextChar(&cursor))
{
    // ...
}

```

### StrLen
*Type:* FUNCTION
Get number of unicode characters in utf-8 string

**Parameters**

- `str` (const char*) - Utf8 string

**Returns**

- `length` (uint32_t) - Number of characters

**Examples**

```
const char* s = "åäöÅÄÖ";
uint32_t count = dmUtf8::StrLen(s);

```

### ToUtf8
*Type:* FUNCTION
Convert a 16-bit unicode character to utf-8

**Notes**

- Buffer must be of at least 4 characters. The string is *not* NULL-terminated

**Parameters**

- `chr` (uint16_t) - Character to convert
- `buf` (char*) - output Buffer (at least 4 bytes)

**Returns**

- `length` (uint32_t) - Number of characters in buffer
