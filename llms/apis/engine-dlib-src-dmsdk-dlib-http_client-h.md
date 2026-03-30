# Http Client

**Namespace:** `dmHttpClient`
**Language:** C++
**Type:** Defold C++
**File:** `http_client.h`
**Source:** `engine/dlib/src/dmsdk/dlib/http_client.h`
**Include:** `dmsdk/dlib/http_client.h`

Http client functions.

## API

### ParseHeader
*Type:* FUNCTION
Parse the header data and make callbacks for each header/version entry and the start of the body.

**Notes**

- This function is destructive to the input data.

**Parameters**

- `header_str` (char*) - http response headers. Must be a null terminated string.
- `user_data` (const void*) - user data to the callbacks.
- `end_of_receive` (bool) - true if there is no more data
- `version_cbk` (function) - callback for the http version
    void (<em>version_cbk)(void</em> user_data, int major, int minor, int status, const char* status_str);
- `header_cbk` (function) - callback for each header/value pair
    void (<em>header_cbk)(void</em> user_data, const char<em> key, const char</em> value);
- `body_cbk` (function) - callback to note the start offset of the body data.
    void (<em>body_cbk)(void</em> user_data, int offset)

**Returns**

- `result` (dmHttpClient::ParseResult) - the parse result

### ParseResult
*Type:* ENUM
Header parse result enumeration.

**Members**

- `dmHttpClient::PARSE_RESULT_NEED_MORE_DATA` - = 1
- `dmHttpClient::PARSE_RESULT_OK` - = 0
- `dmHttpClient::PARSE_RESULT_SYNTAX_ERROR` - = -1
