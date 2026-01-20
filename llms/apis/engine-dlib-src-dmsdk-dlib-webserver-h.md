# WebServer

**Namespace:** `dmWebServer`
**Language:** C++
**Type:** Defold C++
**File:** `webserver.h`
**Source:** `engine/dlib/src/dmsdk/dlib/webserver.h`
**Include:** `dmsdk/dlib/webserver.h`

Simple high-level single-threaded Web server based on dmHttpServer
The web-server has a handler concept similar to servlets in Java

## API

### AddHandler
*Type:* FUNCTION
Add a new handler

**Parameters**

- `server` (HServer) - Server handle
- `prefix` (const char*) - Location prefix for which locations this handler should handle
- `handler_params` (HandlerParams) - Handler parameters

**Returns**

- `return` (Result) - RESULT_OK on success

### GetHeader
*Type:* FUNCTION
Get http header value for key

**Parameters**

- `request` (Request*) - Request
- `name` (const char*) - Header key

**Returns**

- `return` (const char*) - Header value. NULL if the key doesn't exists

### Handler
*Type:* TYPEDEF
Web request handler callback

**Parameters**

- `user_data` (void*) - User  data
- `request` (Request*) - Request

**Returns**

- `return` (void)

### HandlerParams
*Type:* STRUCT
handler parameters

**Members**

- `m_UserData` (void*) - The user data
- `m_Handler` (Handler) - The callback

### HServer
*Type:* TYPEDEF
web server handle

### Receive
*Type:* FUNCTION
Receive data

**Parameters**

- `request` (Request*) - Request
- `buffer` (void*) - Data buffer to receive to
- `buffer_size` (uint32_t) - Buffer size
- `received_bytes` (uint32_t*) - Number of bytes received

**Returns**

- `return` (Result) - RESULT_OK on success

### RemoveHandler
*Type:* FUNCTION
Remove handle

**Parameters**

- `server` (HServer) - Server handle
- `prefix` (const char*) - Prefix for handle to remove

**Returns**

- `return` (Result) - RESULT_OK on success

### Request
*Type:* STRUCT
web server request

**Members**

- `m_Method` (const char*) - Request method
- `m_Method` (const char*) - Request resource
- `m_Method` (const char*) - Content-Length header
- `m_Method` (const char*) - Internal data

### Result
*Type:* ENUM
result codes

**Members**

- `RESULT_OK`
- `RESULT_SOCKET_ERROR`
- `RESULT_INVALID_REQUEST`
- `RESULT_ERROR_INVAL`
- `RESULT_HANDLER_ALREADY_REGISTRED`
- `RESULT_HANDLER_NOT_REGISTRED`
- `RESULT_INTERNAL_ERROR`
- `RESULT_UNKNOWN`

### Send
*Type:* FUNCTION
Send response data

**Parameters**

- `request` (Request) - Request handle
- `data` (void*) - Data to send
- `data_length` (uint32_t) - Data-lenght to send

**Returns**

- `return` (Result) - RESULT_OK on success

### SendAttribute
*Type:* FUNCTION
Sends a header attribute

**Parameters**

- `request` (Request*) - Request
- `key` (const char*) - the header name
- `value` (const char*) - the header value

**Returns**

- `return` (Result) - RESULT_OK on success

### SetStatusCode
*Type:* FUNCTION
Set response status code.

**Notes**

- Only valid to invoke before #Send is invoked

**Parameters**

- `request` (Request*) - Request
- `status_code` (int) - Status code to set

**Returns**

- `return` (Result) - RESULT_OK on success
