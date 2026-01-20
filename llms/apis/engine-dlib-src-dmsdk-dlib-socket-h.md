# Socket

**Namespace:** `dmSocket`
**Language:** C++
**Type:** Defold C++
**File:** `socket.h`
**Source:** `engine/dlib/src/dmsdk/dlib/socket.h`
**Include:** `dmsdk/dlib/socket.h`

Socket functions.

## API

### Address
*Type:* STRUCT
Network addresses were previously represented as an uint32_t, but in
order to support IPv6 the internal representation was changed to a struct.

### Connect
*Type:* FUNCTION
Initiate a connection on a socket

**Parameters**

- `socket` (Socket) - Socket to initiate connection on
- `address` (Address) - Address to connect to
- `port` (int) - Port to connect to

**Returns**

- `return` (Result) - RESULT_OK on success

### Delete
*Type:* FUNCTION
Delete a socket. Corresponds to BSD socket function close()

**Parameters**

- `socket` (Socket) - Socket to close

**Returns**

- `return` (Result) - RESULT_OK on success

### Domain
*Type:* ENUM
Domain type

**Members**

- `DOMAIN_MISSING`
- `DOMAIN_IPV4`
- `DOMAIN_IPV6`
- `DOMAIN_UNKNOWN`

### GetFD
*Type:* FUNCTION
Get underlying file descriptor

**Parameters**

- `socket` (Socket) - socket to get fd for

**Returns**

- `return` (int) - file-descriptor

### GetHostByName
*Type:* FUNCTION
Get host by name

**Parameters**

- `name` (const char*) - Hostname to resolve
- `address` (Address*) - Host address result
- `ipv4` (bool) - Whether or not to search for IPv4 addresses
- `ipv6` (bool) - Whether or not to search for IPv6 addresses

**Returns**

- `return` (Result) - RESULT_OK on success

### GetHostByName
*Type:* FUNCTION
Get host by name with timeout and cancelability

**Notes**

- On HTML5, this function is a wrapper for dmSocket::GetHostByName

**Parameters**

- `name` (const char*) - Hostname to resolve
- `address` (Address*) - Host address result
- `timeout` (uint64_t) - Timeout in microseconds
- `cancelflag` (int*) - if non null and set, will abort the call
- `ipv4` (bool) - Whether or not to search for IPv4 addresses
- `ipv6` (bool) - Whether or not to search for IPv6 addresses

**Returns**

- `return` (Result) - RESULT_OK on success

### INVALID_SOCKET_HANDLE
*Type:* CONSTANT
Invalid socket handle

### New
*Type:* FUNCTION
Create a new socket. Corresponds to BSD socket function socket().

**Notes**

- SIGPIPE is disabled on applicable platforms. This has the implication
that Receive can return zero bytes when the connection is closed by remote peer.

**Parameters**

- `type` (Type) - Socket type
- `protocol` (Protocol) - Protocol
- `socket` (Socket*) - Pointer to socket

**Returns**

- `return` (Result) - RESULT_OK on succcess

### Protocol
*Type:* ENUM
Network protocol

**Members**

- `PROTOCOL_TCP`
- `PROTOCOL_UDP`

### Receive
*Type:* FUNCTION
Receive data on a socket

**Notes**

- For dmSocket::Recv() and dmSocket::Send() function ETIMEDOUT is translated to EWOULDBLOCK
on win32 for compatibility with BSD sockets.

**Parameters**

- `socket` (Socket) - Socket to receive data on
- `buffer[out]` (void*) - Buffer to receive to
- `length` (int) - Receive buffer length
- `received_bytes[out]` (int*) - Number of received bytes (result)

**Returns**

- `return` (Result) - RESULT_OK on success

### Result
*Type:* ENUM
Socket result

**Members**

- `RESULT_OK` - 0
- `RESULT_ACCES` - -1
- `RESULT_AFNOSUPPORT` - -2
- `RESULT_WOULDBLOCK` - -3
- `RESULT_BADF` - -4
- `RESULT_CONNRESET` - -5
- `RESULT_DESTADDRREQ` - -6
- `RESULT_FAULT` - -7
- `RESULT_HOSTUNREACH` - -8
- `RESULT_INTR` - -9
- `RESULT_INVAL` - -10
- `RESULT_ISCONN` - -11
- `RESULT_MFILE` - -12
- `RESULT_MSGSIZE` - -13
- `RESULT_NETDOWN` - -14
- `RESULT_NETUNREACH` - -15
- `RESULT_NOBUFS` - -17
- `RESULT_NOTCONN` - -20
- `RESULT_NOTSOCK` - -22
- `RESULT_OPNOTSUPP` - -23
- `RESULT_PIPE` - -24
- `RESULT_PROTONOSUPPORT` - -25
- `RESULT_PROTOTYPE` - -26
- `RESULT_TIMEDOUT` - -27
- `RESULT_ADDRNOTAVAIL` - -28
- `RESULT_CONNREFUSED` - -29
- `RESULT_ADDRINUSE` - -30
- `RESULT_CONNABORTED` - -31
- `RESULT_INPROGRESS` - -32
- `RESULT_HOST_NOT_FOUND` - -100
- `RESULT_TRY_AGAIN` - -101
- `RESULT_NO_RECOVERY` - -102
- `RESULT_NO_DATA` - -103
- `RESULT_UNKNOWN` - -1000

### ResultToString
*Type:* FUNCTION
Convert result value to string

**Parameters**

- `result` (Result) - Result to convert

**Returns**

- `return` (const char*) - Result as string

### Select
*Type:* FUNCTION
Select for pending data

**Parameters**

- `selector` (Selector*) - Selector
- `timeout` (int) - Timeout. For blocking pass -1. (microseconds)

**Returns**

- `return` (Result) - RESULT_OK on success

### Selector
*Type:* STRUCT
Selector

### SelectorClear
*Type:* FUNCTION
Clear selector for socket. Similar to FD_CLR

**Parameters**

- `selector` (Selector*) - Selector
- `selector_kind` (SelectorKind) - Kind to clear
- `socket` (Socket) - Socket to clear

**Returns**

- `return` (void)

### SelectorIsSet
*Type:* FUNCTION
Check if selector is set. Similar to FD_ISSET

**Parameters**

- `selector` (Selector*) - Selector
- `selector_kind` (SelectorKind) - Selector kind
- `socket` (Socket) - Socket to check for

**Returns**

- `return` (bool) - True if set.

### SelectorKind
*Type:* ENUM
Selector kind

**Members**

- `SELECTOR_KIND_READ`
- `SELECTOR_KIND_WRITE`
- `SELECTOR_KIND_EXCEPT`

### SelectorSet
*Type:* FUNCTION
Set selector for socket. Similar to FD_SET

**Parameters**

- `selector` (Selector*) - Selector
- `selector_kind` (SelectorKind) - Kind to clear
- `socket` (Socket) - Socket to set

**Returns**

- `return` (void)

### SelectorZero
*Type:* FUNCTION
Clear selector (all kinds). Similar to FD_ZERO

**Parameters**

- `selector` (Selector*) - Selector

**Returns**

- `return` (void)

### Send
*Type:* FUNCTION
Send a message on a socket

**Notes**

- For dmSocket::Recv() and dmSocket::Send() function ETIMEDOUT is translated to EWOULDBLOCK
on win32 for compatibility with BSD sockets.

**Parameters**

- `socket` (Socket) - Socket to send a message on
- `buffer` (void*) - Buffer to send
- `length` (int) - Length of buffer to send
- `sent_bytes[out]` (int*) - Number of bytes sent (result)

**Returns**

- `return` (Result) - RESULT_OK on success

### SetBlocking
*Type:* FUNCTION
Set blocking option on a socket

**Parameters**

- `socket` (Socket) - Socket to set blocking on
- `blocking` (bool) - True to block

**Returns**

- `return` (Result) - RESULT_OK on success

### SetBroadcast
*Type:* FUNCTION
Set broadcast address option on socket. Socket option SO_BROADCAST on most platforms.

**Parameters**

- `socket` (Socket) - Socket to set reuse address to
- `broadcast` (bool) - True if broadcast

**Returns**

- `return` (Result) - RESULT_OK on success

### SetNoDelay
*Type:* FUNCTION
Set TCP_NODELAY on socket

**Parameters**

- `socket` (Socket) - Socket to set TCP_NODELAY on
- `no_delay` (bool) - True for no delay

**Returns**

- `return` (Result) - RESULT_OK on success

### SetQuickAck
*Type:* FUNCTION
Set TCP_QUICKACK on socket

**Notes**

- This is a no op on platforms that doesn't support it

**Parameters**

- `socket` (Socket) - Socket to set TCP_QUICKACK on
- `use_quick_ack` (bool) - False to disable quick ack

**Returns**

- `return` (Result) - RESULT_OK on success

### SetReceiveTimeout
*Type:* FUNCTION
Set socket receive timeout

**Notes**

- Timeout resolution might be in milliseconds, e.g. windows. Use values
      larger than or equal to 1000

**Parameters**

- `socket` (Socket) - socket
- `timeout` (uint64_t) - timeout in microseconds

**Returns**

- `return` (Result) - RESULT_OK on success

### SetReuseAddress
*Type:* FUNCTION
Set reuse socket address option on socket. Socket option SO_REUSEADDR on most platforms

**Parameters**

- `socket` (Socket) - Socket to set reuse address to
- `reuse` (bool) - True if reuse

**Returns**

- `return` (Result) - RESULT_OK on success

### SetSendTimeout
*Type:* FUNCTION
Set socket send timeout

**Notes**

- Timeout resolution might be in milliseconds, e.g. windows. Use values
      larger than or equal to 1000.

**Parameters**

- `socket` (Socket) - socket
- `timeout` (uint64_t) - timeout in microseconds

**Returns**

- `return` (Result) - RESULT_OK on success

### Shutdown
*Type:* FUNCTION
Shutdown part of a socket connection

**Parameters**

- `socket` (Socket) - Socket to shutdown connection ow
- `how` (ShutdownType) - Shutdown type

**Returns**

- `return` (Result) - RESULT_OK on success

### ShutdownType
*Type:* ENUM
Socket shutdown type

**Members**

- `SHUTDOWNTYPE_READ`
- `SHUTDOWNTYPE_WRITE`
- `SHUTDOWNTYPE_READWRITE`

### Socket
*Type:* TYPEDEF
Socket type definition

**Notes**

- Use dmSocket::INVALID_SOCKET_HANDLE instead of zero for unset values. This is an exception
from all other handles.

### SOCKET_TIMEOUT
*Type:* CONSTANT
Socket default timeout value

### Type
*Type:* ENUM
Socket type

**Members**

- `TYPE_STREAM`
- `TYPE_DGRAM`
