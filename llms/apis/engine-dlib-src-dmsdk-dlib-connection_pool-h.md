# Connection Pool

**Namespace:** `dmConnectionPool`
**Language:** C++
**Type:** Defold C++
**File:** `connection_pool.h`
**Source:** `engine/dlib/src/dmsdk/dlib/connection_pool.h`
**Include:** `dmsdk/dlib/connection_pool.h`

Connection pool

## API

### Close
*Type:* FUNCTION
Close connection. Use this function whenever an error occur in eg http.

**Parameters**

- `pool` (dmConnectionPool::HPool) - pool
- `connection` (dmConnectionPool::HConnection)

### Delete
*Type:* FUNCTION
Delete connnection pool

**Parameters**

- `pool` (dmConnectionPool::HPool) - pool

**Returns**

- `dmConnectionPool::RESULT_OK` - on success

### Dial
*Type:* FUNCTION
Connection to a host/port

**Parameters**

- `pool` (dmConnectionPool::HPool) - pool
- `host` (const char*) - host
- `port` (uint16_t) - port
- `ssl` (bool) - true for ssl connection
- `timeout` (int) - The timeout (micro seconds) for the connection and ssl handshake
- `connection` (dmConnectionPool::HConnection*) - connection (out)
- `sock_res` (dmSocket::Result*) - socket-result code on failure

**Returns**

- `dmConnectionPool::RESULT_OK` - on success

### Dial
*Type:* FUNCTION
Connection to a host/port

**Parameters**

- `pool` (dmConnectionPool::HPool) - pool
- `host` (const char*) - host
- `port` (uint16_t) - port
- `ssl` (bool) - true for ssl connection
- `timeout` (int) - The timeout (micro seconds) for the connection and ssl handshake
- `cancelflag` (int*) - If set and not null, will make the request early out
- `connection` (dmConnectionPool::HConnection*) - connection (out)
- `sock_res` (dmSocket::Result*) - socket-result code on failure

**Returns**

- `dmConnectionPool::RESULT_OK` - on success

### dmConnectionPool::Result
*Type:* ENUM
Result enumeration.

**Members**

- `dmConnectionPool::RESULT_OK` - 0
- `dmConnectionPool::RESULT_OUT_OF_RESOURCES` - -1
- `dmConnectionPool::RESULT_SOCKET_ERROR` - -2
- `dmConnectionPool::RESULT_HANDSHAKE_FAILED` - -3
- `dmConnectionPool::RESULT_SHUT_DOWN` - -4

### GetSocket
*Type:* FUNCTION
Get socket for connection

**Parameters**

- `pool` (dmConnectionPool::HPool) - pool
- `connection` (dmConnectionPool::HConnection)

**Returns**

- `return` (dmSocket::Socket) - on success

### GetSSLSocket
*Type:* FUNCTION
Get secure socket.

**Parameters**

- `pool` (dmConnectionPool::HPool) - pool
- `connection` (dmConnectionPool::HConnection)

**Returns**

- `return` (dmSSLSocket::Socket) - on success

### HConnection
*Type:* TYPEDEF
Connection handle

### HPool
*Type:* TYPEDEF
Connection pool handle

### New
*Type:* FUNCTION
Create a new connection pool

**Parameters**

- `params` (dmConnectionPool::Params*)
- `pool` (dmConnectionPool::HPool*) - pool (out)

**Returns**

- `dmConnectionPool::RESULT_OK` - on success

### Params
*Type:* STRUCT
Creation parameters

**Members**

- `m_MaxConnections` (int) - Max connection in pool
- `m_MaxKeepAlive` (int) - Default max-keep-alive time in seconds

### Return
*Type:* FUNCTION
Return connection to pool

**Parameters**

- `pool` (dmConnectionPool::HPool) - pool
- `connection` (dmConnectionPool::HConnection)

### Shutdown
*Type:* FUNCTION
Shuts down all open sockets in the pool and block new connection attempts. The function can be
called repeatedly on the same pool until it returns no more connections in use.

**Parameters**

- `pool` (dmConnectionPool::HPool) - pool
- `how` (dmSocket::ShutdownType) - shutdown type to pass to socket shutdown function

**Returns**

- `current` - number of connections in use
