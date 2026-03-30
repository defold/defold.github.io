# SSLSocket

**Namespace:** `dmSSLSocket`
**Language:** C++
**Type:** Defold C++
**File:** `sslsocket.h`
**Source:** `engine/dlib/src/dmsdk/dlib/sslsocket.h`
**Include:** `dmsdk/dlib/sslsocket.h`

Secure socket functions.

## API

### Delete
*Type:* FUNCTION
Delete a secure socket. Does not close the underlying socket

**Parameters**

- `socket` (Socket) - Secure socket to close

**Returns**

- `result` (Result) - RESULT_OK on success

**Examples**

```
dmSSLSocket::Delete(sslsocket);

```

### dmSocket::SetReceiveTimeout
*Type:* FUNCTION
Set socket receive timeout

**Notes**

- Timeout resolution might be in milliseconds, e.g. windows. Use values
      larger than or equal to 1000

**Parameters**

- `socket` (Socket) - socket
- `timeout` (uint64_t) - timeout in microseconds

**Returns**

- `result` (dmSocket::Result) - RESULT_OK on success

### INVALID_SOCKET_HANDLE
*Type:* CONSTANT
SSLSocket socket handle

### New
*Type:* FUNCTION
Create a new secure socket

**Parameters**

- `socket` (dmSocket::Socket) - The socket to wrap
- `host` (const char*) - The name of the host (e.g. "httpbin.org")
- `timeout` (uint64_t) - The timeout for the handshake procedure. (microseconds)
- `sslsocket` (Socket*) - Pointer to a secure socket

**Returns**

- `result` (Result) - RESULT_OK on success

**Examples**

```
dmSSLSocket::Result result;
dmSSLSocket::Socket sslsocket;
result = dmSSLSocket::New(socket, "httpbin.org", 500*1000, &sslsocket);
if (dmSSLSocket::RESULT_OK == result)
{
    // ...
} else {
    // ...
}

```

### Receive
*Type:* FUNCTION
Receive data on a secure socket

**Parameters**

- `socket` (Socket) - Socket to receive data on
- `buffer` (void*) - Buffer to receive to
- `length` (int) - Receive buffer length
- `received_bytes` (int*) - Number of received bytes (result)

**Returns**

- `result` (dmSocket::Result) - RESULT_OK on success

### Result
*Type:* ENUM
Result enumeration.

**Members**

- `dmSSLSocket::RESULT_OK` - (0)
- `dmSSLSocket::RESULT_SSL_INIT_FAILED` - (-2000)
- `dmSSLSocket::RESULT_HANDSHAKE_FAILED` - (-2001)
- `dmSSLSocket::RESULT_WOULDBLOCK` - (-2002)
- `dmSSLSocket::RESULT_CONNREFUSED` - (-2003)

### Send
*Type:* FUNCTION
Send a message on a secure socket

**Parameters**

- `socket` (Socket) - SSL socket to send a message on
- `buffer` (void*) - Buffer to send
- `length` (int) - Length of buffer to send
- `sent_bytes` (int*) - Number of bytes sent (result)

**Returns**

- `result` (dmSocket::Result) - RESULT_OK on success

### Socket
*Type:* TYPEDEF
Socket type definition
