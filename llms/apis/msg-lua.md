# Message

**Namespace:** `msg`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_msg.cpp`
**Source:** `engine/script/src/script_msg.cpp`

Functions for passing messages and constructing URL objects.

## API

### msg.post
*Type:* FUNCTION
Post a message to a receiving URL. The most common case is to send messages
to a component. If the component part of the receiver is omitted, the message
is broadcast to all components in the game object.
The following receiver shorthands are available:

"." the current game object
"#" the current component

 There is a 2 kilobyte limit to the message parameter table size.

**Parameters**

- `receiver` (string | url | hash) - The receiver must be a string in URL-format, a URL object or a hashed string.
- `message_id` (string | hash) - The id must be a string or a hashed string.
- `message` (table | nil) (optional) - a lua table with message parameters to send.

**Examples**

Send "enable" to the sprite "my_sprite" in "my_gameobject":
```
msg.post("my_gameobject#my_sprite", "enable")

```

Send a "my_message" to an url with some additional data:
```
local params = {my_parameter = "my_value"}
msg.post(my_url, "my_message", params)

```

### msg.url
*Type:* FUNCTION
This is equivalent to msg.url(nil) or msg.url("#"), which creates an url to the current
script component.

**Returns**

- `url` (url) - a new URL

**Examples**

Create a new URL which will address the current script:
```
local my_url = msg.url()
print(my_url) --> url: [current_collection:/my_instance#my_component]

```

### msg.url
*Type:* FUNCTION
The format of the string must be [socket:][path][#fragment], which is similar to a HTTP URL.
When addressing instances:

socket is the name of a valid world (a collection)
path is the id of the instance, which can either be relative the instance of the calling script or global
fragment would be the id of the desired component

In addition, the following shorthands are available:

"." the current game object
"#" the current component

**Parameters**

- `urlstring` (string) - string to create the url from

**Returns**

- `url` (url) - a new URL

**Examples**

```
local my_url = msg.url("#my_component")
print(my_url) --> url: [current_collection:/my_instance#my_component]

local my_url = msg.url("my_collection:/my_sub_collection/my_instance#my_component")
print(my_url) --> url: [my_collection:/my_sub_collection/my_instance#my_component]

local my_url = msg.url("my_socket:")
print(my_url) --> url: [my_collection:]

```

### msg.url
*Type:* FUNCTION
creates a new URL from separate arguments

**Parameters**

- `socket` (string | hash) (optional) - socket of the URL
- `path` (string | hash) (optional) - path of the URL
- `fragment` (string | hash) (optional) - fragment of the URL

**Returns**

- `url` (url) - a new URL

**Examples**

```
local my_socket = "main" -- specify by valid name
local my_path = hash("/my_collection/my_gameobject") -- specify as string or hash
local my_fragment = "component" -- specify as string or hash
local my_url = msg.url(my_socket, my_path, my_fragment)

print(my_url) --> url: [main:/my_collection/my_gameobject#component]
print(my_url.socket) --> 786443 (internal numeric value)
print(my_url.path) --> hash: [/my_collection/my_gameobject]
print(my_url.fragment) --> hash: [component]

```
