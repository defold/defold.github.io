# extension-photon-fusion

**Namespace:** `fusion`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Photon Fusion

## API

### fusion.init
*Type:* FUNCTION
Initialize Fusion.

**Parameters**

- `app_id` (string)
- `app_version` (string)

### fusion.init_from_settings
*Type:* FUNCTION
Initialize Fusion from game.project settings.

### fusion.connect
*Type:* FUNCTION
Connect Fusion.

**Parameters**

- `user` (string)
- `server` (string)

### fusion.disconnect
*Type:* FUNCTION
Disonnect Fusion.

### fusion.reconnect
*Type:* FUNCTION
Reconnect Fusion.

### fusion.start
*Type:* FUNCTION
Start Fusion sync.

### fusion.stop
*Type:* FUNCTION
Stop Fusion sync.

### fusion.get_state
*Type:* FUNCTION
Get connection state.

**Returns**

- `number` - State

### fusion.get_disconnect_cause
*Type:* FUNCTION
Get disconnect cause.

**Returns**

- `number` - Cause

### fusion.join_or_create_room_random
*Type:* FUNCTION
Join or create random room.

**Parameters**

- `create_room_options` (table)
- `matchmaking_options` (table)

### fusion.join_room_random
*Type:* FUNCTION
Join random room.

**Parameters**

- `matchmaking_options` (table)

### fusion.join_room
*Type:* FUNCTION
Join room.

**Parameters**

- `room_name` (string)
- `join_room_options` (table)

### fusion.join_or_create_room
*Type:* FUNCTION
Join or create room.

**Parameters**

- `room_name` (string)
- `create_room_options` (table)
- `join_room_options` (table)

### fusion.create_room
*Type:* FUNCTION
Create room.

**Parameters**

- `room_name` (string)
- `create_room_options` (table)

### fusion.leave_room
*Type:* FUNCTION
Leave room.

**Parameters**

- `will_come_back` (boolean)
- `send_auth_cookie` (boolean)

### fusion.is_connected
*Type:* FUNCTION
Check if Fusion is connected.

**Returns**

- `boolean`

### fusion.is_running
*Type:* FUNCTION
Check if Fusion has config and is connected.

**Returns**

- `boolean`

### fusion.is_started
*Type:* FUNCTION
Check if Fusion is started. Fusion is considered started after a call to.
`fusion.start()` has received a `EventOnFusionStart` event.

**Returns**

- `boolean`

### fusion.is_in_room
*Type:* FUNCTION
Check if Fusion is in a room.

**Returns**

- `boolean`

### fusion.enable_debug
*Type:* FUNCTION
Enable/disable debugging.

**Parameters**

- `enable` (boolean)

### fusion.register_scene_object
*Type:* FUNCTION
Register a scene object.

**Parameters**

- `scene` (number)
- `factory_url` (string)
- `owner_mode` (number)
- `id` (string)

### fusion.spawn
*Type:* FUNCTION
Create a networked game object. This will spawn a game object in the same.
Way as when calling factory.create(). The function will also register the spawned object with Fusion as if manually calling register_object()

**Parameters**

- `factory_url` (string)
- `position` (vector3) - Initial position of created game object

- `rotation` (quat) - Initial rotation of created game object

- `scene` (number) - The scene to which this object belongs

- `owner_mode` (number) - Owner mode of spawned object

**Returns**

- `hash` - Of the spawned game object

### fusion.despawn
*Type:* FUNCTION
Destroy a networked object.

**Parameters**

- `id` (string)

### fusion.register_object
*Type:* FUNCTION
Register an object.

**Parameters**

- `scene` (number)
- `factory_url` (string)
- `owner_mode` (number)
- `id` (string)

### fusion.unregister_object
*Type:* FUNCTION
Unregister a previously registered object.

**Parameters**

- `id` (string)

### fusion.scene_change
*Type:* FUNCTION
Change scene.

**Parameters**

- `index` (number)
- `sequence` (number)
- `data` (string)

### fusion.rpc
*Type:* FUNCTION
Send RPC.

**Parameters**

- `target_player` (number) - 0 = all, specific PlayerId = targeted

- `data` (string)

**Returns**

- `boolean`

### fusion.on_event
*Type:* FUNCTION
Set event listener.

**Parameters**

- `listener` (function)

### fusion.get_local_player_id
*Type:* FUNCTION
Get the player id of the local client

**Returns**

- `number` - Player id of the local client

### fusion.get_owner_id
*Type:* FUNCTION
Get the player id of the current owner of an object

**Parameters**

- `id` (string) - Id of the object to get the owner for

**Returns**

- `number` - Player id of the object's owner

### fusion.has_authority
*Type:* FUNCTION
Check if this client has authority over a game object. Use this to decide if user input should be handled or not.

**Parameters**

- `id` (string)

**Returns**

- `boolean` - Returns true if the client has authority

### fusion.has_owner
*Type:* FUNCTION
Check if an object has an owner

**Parameters**

- `id` (string) - Id of the object

**Returns**

- `boolean` - If the object has an owner

### fusion.want_authority
*Type:* FUNCTION
Signal desire for the local client to own an object

**Parameters**

- `claim_ownership` (boolean)
- `id` (string) - Id of the object to own

### fusion.clear_owner_cooldown
*Type:* FUNCTION
Explicitly clear the ownership cooldown

**Parameters**

- `id` (string) - Id of the object to clear cooldown for

### fusion.set_send_rate
*Type:* FUNCTION
Set the send rate of an object. This decided how much bandwidth to allocate

**Parameters**

- `send_rate` (number)
- `id` (string) - Id of the object to send rate for

### fusion.set_local_send_rate
*Type:* FUNCTION
Set the local send rate divisor for an object. A value of `1` means the object sends every tick (highest rate). A value of `16` means it sends every 16th tick (lowest rate). This is a client-side optimization -- the object still exists on all clients but consumes less bandwidth when you are not the active authority.

**Parameters**

- `send_rate` (number)
- `id` (string) - Id of the object to send rate for

### fusion.reset_send_rate
*Type:* FUNCTION
Reset the send rate of an object.

**Parameters**

- `id` (string) - Id of the object to reset send rate for

### fusion.player_count
*Type:* FUNCTION
Get player count

**Returns**

- `number` - Number of players

### fusion.is_master_client
*Type:* FUNCTION
Get if this client is the room's master

**Returns**

- `boolean` - True if this client is the room's master

### fusion.get_rtt
*Type:* FUNCTION
Get round trip time

**Returns**

- `number` - Round trip time in seconds

### fusion.network_time_diff
*Type:* FUNCTION
Get raw offset between server time and local time. A positive value means the server clock is ahead of the local clock.

**Returns**

- `number` - Time diff

### fusion.set_global_interest_key
*Type:* FUNCTION
Set global visibility key for an object

### fusion.set_area_interest_key
*Type:* FUNCTION
Set area visibility key for an object

### fusion.set_user_interest_key
*Type:* FUNCTION
Set user visibility key for an object

### fusion.set_area_keys
*Type:* FUNCTION
Set area visibility keys

**Parameters**

- `keys` (table) - Area keys to set. Stored as a table of key value pairs (area_key->send_rate)

### fusion.add_user_key
*Type:* FUNCTION
Add a user visibility key

### fusion.remove_user_key
*Type:* FUNCTION
Remove a user visibility key from an object

### OWNERMODE_TRANSACTION
*Type:* VARIABLE
OWNERMODE_TRANSACTION

### OWNERMODE_PLAYERATTACHED
*Type:* VARIABLE
OWNERMODE_PLAYERATTACHED

### OWNERMODE_DYNAMIC
*Type:* VARIABLE
OWNERMODE_DYNAMIC

### OWNERMODE_MASTERCLIENT
*Type:* VARIABLE
OWNERMODE_MASTERCLIENT

### OWNERMODE_GAMEGLOBAL
*Type:* VARIABLE
OWNERMODE_GAMEGLOBAL

### STATE_DISCONNECTED
*Type:* VARIABLE
STATE_DISCONNECTED

### STATE_CONNECTING
*Type:* VARIABLE
STATE_CONNECTING

### STATE_CONNECTED
*Type:* VARIABLE
STATE_CONNECTED

### STATE_JOININGROOM
*Type:* VARIABLE
STATE_JOININGROOM

### STATE_INROOM
*Type:* VARIABLE
STATE_INROOM

### STATE_LEAVINGROOM
*Type:* VARIABLE
STATE_LEAVINGROOM

### STATE_DISCONNECTING
*Type:* VARIABLE
STATE_DISCONNECTING

### DISCONNECT_CAUSE_NONE
*Type:* VARIABLE
DISCONNECT_CAUSE_NONE

### DISCONNECT_CAUSE_DISCONNECTBYSERVERUSERLIMIT
*Type:* VARIABLE
DISCONNECT_CAUSE_DISCONNECTBYSERVERUSERLIMIT

### DISCONNECT_CAUSE_EXCEPTIONONCONNECT
*Type:* VARIABLE
DISCONNECT_CAUSE_EXCEPTIONONCONNECT

### DISCONNECT_CAUSE_DISCONNECTBYSERVER
*Type:* VARIABLE
DISCONNECT_CAUSE_DISCONNECTBYSERVER

### DISCONNECT_CAUSE_DISCONNECTBYSERVERLOGIC
*Type:* VARIABLE
DISCONNECT_CAUSE_DISCONNECTBYSERVERLOGIC

### DISCONNECT_CAUSE_TIMEOUTDISCONNECT
*Type:* VARIABLE
DISCONNECT_CAUSE_TIMEOUTDISCONNECT

### DISCONNECT_CAUSE_EXCEPTION
*Type:* VARIABLE
DISCONNECT_CAUSE_EXCEPTION

### DISCONNECT_CAUSE_INVALIDAUTHENTICATION
*Type:* VARIABLE
DISCONNECT_CAUSE_INVALIDAUTHENTICATION

### DISCONNECT_CAUSE_MAXCCUREACHED
*Type:* VARIABLE
DISCONNECT_CAUSE_MAXCCUREACHED

### DISCONNECT_CAUSE_INVALIDREGION
*Type:* VARIABLE
DISCONNECT_CAUSE_INVALIDREGION

### DISCONNECT_CAUSE_OPERATIONNOTALLOWEDINCURRENTSTATE
*Type:* VARIABLE
DISCONNECT_CAUSE_OPERATIONNOTALLOWEDINCURRENTSTATE

### DISCONNECT_CAUSE_CUSTOMAUTHENTICATIONFAILED
*Type:* VARIABLE
DISCONNECT_CAUSE_CUSTOMAUTHENTICATIONFAILED

### DISCONNECT_CAUSE_CLIENTVERSIONTOOOLD
*Type:* VARIABLE
DISCONNECT_CAUSE_CLIENTVERSIONTOOOLD

### DISCONNECT_CAUSE_CLIENTVERSIONINVALID
*Type:* VARIABLE
DISCONNECT_CAUSE_CLIENTVERSIONINVALID

### DISCONNECT_CAUSE_DASHBOARDVERSIONINVALID
*Type:* VARIABLE
DISCONNECT_CAUSE_DASHBOARDVERSIONINVALID

### DISCONNECT_CAUSE_AUTHENTICATIONTICKETEXPIRED
*Type:* VARIABLE
DISCONNECT_CAUSE_AUTHENTICATIONTICKETEXPIRED

### DISCONNECT_CAUSE_DISCONNECTBYOPERATIONLIMIT
*Type:* VARIABLE
DISCONNECT_CAUSE_DISCONNECTBYOPERATIONLIMIT

### EVENT_OBJECT_READY
*Type:* VARIABLE
EVENT_OBJECT_READY

### EVENT_SUB_OBJECT_CREATED
*Type:* VARIABLE
EVENT_SUB_OBJECT_CREATED

### EVENT_OBJECT_DESTROYED
*Type:* VARIABLE
EVENT_OBJECT_DESTROYED

### EVENT_SUB_OBJECT_DESTROYED
*Type:* VARIABLE
EVENT_SUB_OBJECT_DESTROYED

### EVENT_OBJECT_OWNER_CHANGED
*Type:* VARIABLE
EVENT_OBJECT_OWNER_CHANGED

### EVENT_OBJECT_PREDICTION_OVERRIDE
*Type:* VARIABLE
EVENT_OBJECT_PREDICTION_OVERRIDE

### EVENT_LOBBY_STATS
*Type:* VARIABLE
EVENT_LOBBY_STATS

### EVENT_ROOM_JOINED
*Type:* VARIABLE
EVENT_ROOM_JOINED

### EVENT_ROOM_LEFT
*Type:* VARIABLE
EVENT_ROOM_LEFT

### EVENT_RPC
*Type:* VARIABLE
EVENT_RPC

### EVENT_SCENE_CHANGE
*Type:* VARIABLE
EVENT_SCENE_CHANGE

### EVENT_DESTROYED_MAP_ACTOR
*Type:* VARIABLE
EVENT_DESTROYED_MAP_ACTOR

### EVENT_INTEREST_ENTER
*Type:* VARIABLE
EVENT_INTEREST_ENTER

### EVENT_INTEREST_EXIT
*Type:* VARIABLE
EVENT_INTEREST_EXIT

### EVENT_FORCED_DISCONNECT
*Type:* VARIABLE
EVENT_FORCED_DISCONNECT

### EVENT_FUSION_START
*Type:* VARIABLE
EVENT_FUSION_START

### EVENT_CONNECTED
*Type:* VARIABLE
EVENT_CONNECTED

### EVENT_DISCONNECTED
*Type:* VARIABLE
EVENT_DISCONNECTED
