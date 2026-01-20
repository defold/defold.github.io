# Message

**Namespace:** `dmMessage`
**Language:** C++
**Type:** Defold C++
**File:** `message.h`
**Source:** `engine/dlib/src/dmsdk/dlib/message.h`
**Include:** `dmsdk/dlib/message.h`

Api for sending messages

## API

### dmMessage::Result
*Type:* ENUM
Result enum

**Members**

- `RESULT_OK` - = 0
- `RESULT_SOCKET_EXISTS` - = -1
- `RESULT_SOCKET_NOT_FOUND` - = -2
- `RESULT_SOCKET_OUT_OF_RESOURCES` - = -3
- `RESULT_INVALID_SOCKET_NAME` - = -4
- `RESULT_MALFORMED_URL` - = -5
- `RESULT_NAME_OK_SOCKET_NOT_FOUND` - = -6

### dmMessage::StringURL
*Type:* STRUCT
Helper struct for parsing a string of the form "socket:path#fragment"

**Notes**

- The sizes do not include the null character. There is no null character since the dmMessage::ParseURL is non destructive.

**Members**

- `m_Socket` (const char*) - The socket
- `m_SocketSize` (uint32_t) - The socket length
- `m_Path` (const char*) - The path
- `m_PathSize` (uint32_t) - The path length
- `m_Fragment` (const char*) - The fragment
- `m_FragmentSize` (uint32_t) - The fragment length

### dmMessage::URL
*Type:* STRUCT
URL specifying a sender/receiver of messages

**Notes**

- Currently has a hard limit of 32 bytes
- This struct is a part of the save file APi (see script_table.cpp)

### dmMMessage::MessageDestroyCallback
*Type:* TYPEDEF
A callback for messages that needs cleanup after being dispatched. E.g. for freeing resources/memory.

### GetFragment
*Type:* FUNCTION
Get the message fragment

**Parameters**

- `url` (dmMessage::URL) - url

**Returns**

- `fragment` (dmhash_t)

### GetPath
*Type:* FUNCTION
Get the message path

**Parameters**

- `url` (dmMessage::URL) - url

**Returns**

- `path` (dmhash_t)

### GetSocket
*Type:* FUNCTION
Get the message socket

**Parameters**

- `url` (dmMessage::URL) - url

**Returns**

- `socket` (dmMessage::HSocket)

### GetSocketName
*Type:* FUNCTION
Get socket name

**Parameters**

- `socket` (dmMessage::HSocket) - Socket

**Returns**

- `name` (const char*) - socket name. 0 if it was not found

### GetSocketNameHash
*Type:* FUNCTION
Get socket name hash

**Parameters**

- `socket` (dmMessage::HSocket) - Socket

**Returns**

- `name_hash` (dmhash_t) - socket name hash. 0 if it was not found

### HSocket
*Type:* TYPEDEF
Socket handle

### IsSocketValid
*Type:* FUNCTION
Tests if a socket is valid (not deleted).

**Parameters**

- `socket` (dmMessage::HSocket) - Socket

**Returns**

- `result` (bool) - if the socket is valid or not

### Message
*Type:* STRUCT

### Message
*Type:* STRUCT
Message data desc used at dispatch callback. When a message is posted,
the actual object is copied into the sockets internal buffer.

**Members**

- `m_Sender` (dmMessage::URL) - Sender uri
- `m_Receiver` (dmMessage::URL) - Receiver uri
- `m_Id` (dmhash_t) - Unique id of message
- `m_UserData1` (uintptr_t) - User data pointer
- `m_UserData2` (uintptr_t) - User data pointer
- `m_Descriptor` (uintptr_t) - User specified descriptor of the message data
- `m_DataSize` (uint32_t) - Size of message data in bytes
- `m_Next` (dmMessage::Message*) - Ptr to next message (or 0 if last)
- `m_DestroyCallback` (dmMessage::MessageDestroyCallback) - If set, will be called after each dispatch
- `m_Data` (uint8_t*) - Payload

### ParseUrl
*Type:* FUNCTION
Convert a string to a URL struct

**Notes**

- No allocation occurs, thus no cleanup is needed.

**Parameters**

- `uri` (const char*) - string of the format <span class="socket">][path</span>[#fragment]
- `out` (dmMessage::StringUrl) - url in string format, must not be 0x0

**Returns**

- `-` - RESULT_OK on success
- RESULT_MALFORMED_URL if the uri could not be parsed

### ResetUrl
*Type:* FUNCTION
Resets the given URL to default values.

**Notes**

- Previously the URL wasn't reset in the constructor and certain calls to ResetURL might currently be redundant

**Parameters**

- `url` (dmMessage::URL) - URL to reset

### SetFragment
*Type:* FUNCTION
Set the message fragment

**Parameters**

- `url` (dmMessage::URL) - url
- `fragment` (dmhash_t)

### SetPath
*Type:* FUNCTION
Set the message path

**Parameters**

- `url` (dmMessage::URL) - url
- `path` (dmhash_t)

### SetSocket
*Type:* FUNCTION
Set the socket

**Parameters**

- `url` (dmMessage::URL) - url
- `socket` (dmMessage::HSocket)
