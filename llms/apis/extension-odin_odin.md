# extension-odin

**Namespace:** `odin`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with ODIN Voice

## API

### odin.init
*Type:* FUNCTION
Initialize ODIN Voice

**Parameters**

- `listener` (function)

**Returns**

- `boolean`

### odin.create_room
*Type:* FUNCTION
Create or join a room.

**Parameters**

- `room_id` (string) - Id of the room to join
- `user_id` (string) - Id of the user
- `access_key` (string) - The access key used when generating a token for room access. Will use odin.access_key if none is provided.

**Returns**

- `boolean`

### odin.close_room
*Type:* FUNCTION
Close/leave a previously created/joined room.

**Returns**

- `boolean`

### odin.send
*Type:* FUNCTION
Send a message to the current room.

**Parameters**

- `data` (string) - Data to send.
- `target_peer_ids` (table) - Optional table with peers to send message to. Nil to send to all.
- `msgid` (number) - Optional message id to identify message by. The id will be used in the response.

**Returns**

- `boolean`
