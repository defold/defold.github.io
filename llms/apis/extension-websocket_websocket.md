# extension-websocket

**Namespace:** `websocket`
**Language:** Lua
**Type:** Extension

Functions and constants for using websockets. Supported on all platforms.

## API

### websocket.connect
*Type:* FUNCTION
Connects to a remote address

**Parameters**

- `url` (string) - url of the remote connection
- `params` (table) - optional parameters as properties. The following parameters can be set
  - `timeout` (number) - Timeout for the connection sequence (milliseconds). Not used on HTML5. (Default is 3000)
  - `protocol` (string) - the protocol to use (e.g. 'chat'). If not set, no `Sec-WebSocket-Protocol` header is sent.
  - `headers` (string) - list of http headers. Each pair is separated with "\r\n". Not used on HTML5.
- `callback` (function) - callback that receives all messages from the connection
  - `self` (object) - The script instance that was used to register the callback
  - `connection` (object) - the connection
  - `data` (table) - the event payload
    - `event` (number) - The current event. One of the following
- `websocket.EVENT_CONNECTED`
- `websocket.EVENT_DISCONNECTED`
- `websocket.EVENT_ERROR`
- `websocket.EVENT_MESSAGE`
    - `message` (string) - The received data if event is `websocket.EVENT_MESSAGE`. Error message otherwise
    - `handshake_response` (table) - Handshake response information (status, headers etc)
    - `code` (number) - Status code received from the server if the server closed the connection. Only present if event is `EVENT_DISCONNECTED`.

**Returns**

- `object` - the connection

**Examples**

```
  local function websocket_callback(self, conn, data)
    if data.event == websocket.EVENT_DISCONNECTED then
      log("Disconnected: " .. tostring(conn))
      self.connection = nil
      update_gui(self)
    elseif data.event == websocket.EVENT_CONNECTED then
      update_gui(self)
      log("Connected: " .. tostring(conn))
    elseif data.event == websocket.EVENT_ERROR then
      log("Error: '" .. data.message .. "'")
    elseif data.event == websocket.EVENT_MESSAGE then
      log("Receiving: '" .. tostring(data.message) .. "'")
    end
  end

  function init(self)
    self.url = "ws://echo.websocket.events"
    local params = {
      timeout = 3000,
      headers = "Sec-WebSocket-Protocol: chat\r\nOrigin: mydomain.com\r\n"
    }
    self.connection = websocket.connect(self.url, params, websocket_callback)
  end

  function finalize(self)
      if self.connection ~= nil then
        websocket.disconnect(self.connection)
      end
  end

```

### websocket.disconnect
*Type:* FUNCTION
Explicitly close a websocket

**Parameters**

- `connection` (object) - the websocket connection

### websocket.send
*Type:* FUNCTION
Send data on a websocket

**Parameters**

- `connection` (object) - the websocket connection
- `message` (string) - the message to send
- `options` (table) - options for this particular message. May be `nil`
  - `type` (number) - The data type of the message
- `websocket.DATA_TYPE_BINARY` (default)
- `websocket.DATA_TYPE_TEXT`

**Examples**

```
  local function websocket_callback(self, conn, data)
    if data.event == websocket.EVENT_CONNECTED then
      websocket.send(conn, "Hello from the other side")
    end
  end

  function init(self)
    self.url = "ws://echo.websocket.org"
    local params = {}
    self.connection = websocket.connect(self.url, params, websocket_callback)
  end

```

### EVENT_CONNECTED
*Type:* VARIABLE
The websocket was connected

### EVENT_DISCONNECTED
*Type:* VARIABLE
The websocket disconnected

### EVENT_MESSAGE
*Type:* VARIABLE
The websocket received data

### EVENT_ERROR
*Type:* VARIABLE
The websocket encountered an error
