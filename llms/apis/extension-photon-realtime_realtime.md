# extension-photon-realtime

**Namespace:** `realtime`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Photon Realtime

## API

### realtime.init
*Type:* FUNCTION
Initialize Realtime by creating a load balanced client

**Parameters**

- `app_id` (string)
- `app_version` (string)
- `listener` (function)

### realtime.connect
*Type:* FUNCTION
Connect to the server.

**Parameters**

- `options` (table) - Table with connection options
  - `username` (string)
  - `use_datagram_encryption` (boolean)
  - `server_type` (number) - See SERVER_TYPE_* enums
  - `server_address` (string) - The IP address or domain name and optionally the port number to connect to. IP addresses can be in IPv4 or IPv6 format
  - `auth_data` (string) - Sets the HTTP POST data, that will be forwarded to the authentication service, to the provided data.
  - `auth_parameters` (string) - The HTTP GET parameters that will be forwarded to the authentication service to the provided parameters.
  - `auth_type` (number) - The type of the &quot;Custom Authentication&quot; service that will be used. See AUTH_* enums

### realtime.update
*Type:* FUNCTION
Update Realtime. Call this from a script component.

### realtime.disconnect
*Type:* FUNCTION
Disconnect from server.

### realtime.join_lobby
*Type:* FUNCTION
Join lobby.

**Parameters**

- `lobby_name` (string)
- `lobby_type` (number)

### realtime.leave_lobby
*Type:* FUNCTION
Leave lobby.

### realtime.create_room
*Type:* FUNCTION
Create room.

**Parameters**

- `game_id` (string) - The name to create a room with. Must be unique and not in use or the room can't be created. If this is an empty string, then the server will assign a GUID as name.
- `room_options` (table)
  - `is_visible` (boolean)
  - `is_open` (boolean)
  - `supress_room_events` (boolean)
  - `max_players` (number)
  - `player_ttl` (number)
  - `empty_room_ttl` (number)
  - `lobby_type` (number) - Realtime.LOBBYTYPE_* enum
  - `lobby_name` (string)
  - `publish_user_id` (string)
  - `direct_mode` (numbmer) - Realtime.DIRECTMODE_* enum
  - `props_listed_in_lobby` (table)
  - `custom_room_properties` (table)
- `expected_users` (table)

### realtime.join_room
*Type:* FUNCTION
Join room.

**Parameters**

- `game_id` (string) - The name to create a room with. Must be unique and not in use or the room can't be created. If this is an empty string, then the server will assign a GUID as name.
- `join_options` (table)
  - `rejoin` (boolean)
  - `cache_slice_index` (number)
  - `expected_users` (table)

### realtime.join_or_create_room
*Type:* FUNCTION
Join or create room.

**Parameters**

- `game_id` (string) - The name to create a room with. Must be unique and not in use or the room can't be created. If this is an empty string, then the server will assign a GUID as name.
- `room_options` (table)
  - `is_visible` (boolean)
  - `is_open` (boolean)
  - `supress_room_events` (boolean)
  - `max_players` (number)
  - `player_ttl` (number)
  - `empty_room_ttl` (number)
  - `lobby_type` (number) - Realtime.LOBBYTYPE_* enum
  - `lobby_name` (string)
  - `publish_user_id` (string)
  - `direct_mode` (numbmer) - Realtime.DIRECTMODE_* enum
  - `props_listed_in_lobby` (table)
  - `custom_room_properties` (table)
- `join_options` (table)
  - `custom_room_properties` (table)
  - `max_players` (number)
  - `matchmaking_mode` (number) - Realtime.MATCHMAKINGMODE_* enum
  - `lobby_name` (string)
  - `lobby_type` (number) - Realtime.LOBBYTYPE_* enum
  - `sql_lobby_filter` (string)
  - `expected_users` (table)

### realtime.join_or_create_random_room
*Type:* FUNCTION
Join or create random room.

**Parameters**

- `game_id` (string) - The name to create a room with. Must be unique and not in use or the room can't be created. If this is an empty string, then the server will assign a GUID as name.
- `room_options` (table)
  - `is_visible` (boolean)
  - `is_open` (boolean)
  - `supress_room_events` (boolean)
  - `max_players` (number)
  - `player_ttl` (number)
  - `empty_room_ttl` (number)
  - `lobby_type` (number) - Realtime.LOBBYTYPE_* enum
  - `lobby_name` (string)
  - `publish_user_id` (string)
  - `direct_mode` (numbmer) - Realtime.DIRECTMODE_* enum
  - `props_listed_in_lobby` (table)
  - `custom_room_properties` (table)
- `join_options` (table)
  - `custom_room_properties` (table)
  - `max_players` (number)
  - `matchmaking_mode` (number) - Realtime.MATCHMAKINGMODE_* enum
  - `lobby_name` (string)
  - `lobby_type` (number) - Realtime.LOBBYTYPE_* enum
  - `sql_lobby_filter` (string)
  - `expected_users` (table)

### realtime.join_random_room
*Type:* FUNCTION
Join random room.

**Parameters**

- `join_options` (table)
  - `custom_room_properties` (table)
  - `max_players` (number)
  - `matchmaking_mode` (number) - Realtime.MATCHMAKINGMODE_* enum
  - `lobby_name` (string)
  - `lobby_type` (number) - Realtime.LOBBYTYPE_* enum
  - `sql_lobby_filter` (string)
  - `expected_users` (table)

### realtime.leave_room
*Type:* FUNCTION
Leave room.

**Parameters**

- `will_come_back` (boolean)
- `send_auth_cookie` (boolean)

### realtime.get_room_list
*Type:* FUNCTION
Get room list.

### realtime.raise_event
*Type:* FUNCTION
Sends in-game data to other players in the game.

**Parameters**

- `reliable` (boolean)
- `parameter` (number)
- `event_code` (number)
- `options` (table) - (channel_id, event_caching, receiver_group, interest_group, cache_slice_index, target_players, web_flags, encrypt)
  - `channel_id` (number)
  - `event_caching` (number)
  - `receiver_group` (number)
  - `interest_group` (number)
  - `cache_slice_index` (number)
  - `target_players` (number)
  - `web_flags` (number)
  - `encrypt` (boolean)

**Returns**

- `boolea`

### realtime.set_auto_join_lobby
*Type:* FUNCTION
Set the auto join lobby flag. The value of the autoJoinLobby flag determines if the client will automatically join the default lobby whenever it has successfully connected and whenever it leaves a game room.

**Parameters**

- `auto_join` (boolean)

### EVENT_CONNECTIONERRORRETURN
*Type:* VARIABLE
EVENT_CONNECTIONERRORRETURN

### EVENT_CLIENTERRORRETURN
*Type:* VARIABLE
EVENT_CLIENTERRORRETURN

### EVENT_WARNINGRETURN
*Type:* VARIABLE
EVENT_WARNINGRETURN

### EVENT_SERVERERRORRETURN
*Type:* VARIABLE
EVENT_SERVERERRORRETURN

### EVENT_JOINROOMEVENTACTION
*Type:* VARIABLE
EVENT_JOINROOMEVENTACTION

### EVENT_LEAVEROOMEVENTACTION
*Type:* VARIABLE
EVENT_LEAVEROOMEVENTACTION

### EVENT_CUSTOMEVENTACTION
*Type:* VARIABLE
EVENT_CUSTOMEVENTACTION

### EVENT_CONNECTRETURN
*Type:* VARIABLE
EVENT_CONNECTRETURN

### EVENT_DISCONNECTRETURN
*Type:* VARIABLE
EVENT_DISCONNECTRETURN

### EVENT_CREATEROOMRETURN
*Type:* VARIABLE
EVENT_CREATEROOMRETURN

### EVENT_JOINORCREATEROOMRETURN
*Type:* VARIABLE
EVENT_JOINORCREATEROOMRETURN

### EVENT_JOINRANDOMORCREATEROOMRETURN
*Type:* VARIABLE
EVENT_JOINRANDOMORCREATEROOMRETURN

### EVENT_JOINROOMRETURN
*Type:* VARIABLE
EVENT_JOINROOMRETURN

### EVENT_JOINRANDOMROOMRETURN
*Type:* VARIABLE
EVENT_JOINRANDOMROOMRETURN

### EVENT_LEAVEROOMRETURN
*Type:* VARIABLE
EVENT_LEAVEROOMRETURN

### EVENT_JOINLOBBYRETURN
*Type:* VARIABLE
EVENT_JOINLOBBYRETURN

### EVENT_LEAVELOBBYRETURN
*Type:* VARIABLE
EVENT_LEAVELOBBYRETURN

### EVENT_ONFINDFRIENDSRESPONSE
*Type:* VARIABLE
EVENT_ONFINDFRIENDSRESPONSE

### EVENT_ONLOBBYSTATSRESPONSE
*Type:* VARIABLE
EVENT_ONLOBBYSTATSRESPONSE

### EVENT_WEBRPCRETURN
*Type:* VARIABLE
EVENT_WEBRPCRETURN

### EVENT_ONROOMLISTUPDATE
*Type:* VARIABLE
EVENT_ONROOMLISTUPDATE

### EVENT_ONROOMPROPERTIESCHANGE
*Type:* VARIABLE
EVENT_ONROOMPROPERTIESCHANGE

### EVENT_ONPLAYERPROPERTIESCHANGE
*Type:* VARIABLE
EVENT_ONPLAYERPROPERTIESCHANGE

### EVENT_ONAPPSTATSUPDATE
*Type:* VARIABLE
EVENT_ONAPPSTATSUPDATE

### EVENT_ONLOBBYSTATSUPDATE
*Type:* VARIABLE
EVENT_ONLOBBYSTATSUPDATE

### EVENT_ONCACHESLICECHANGED
*Type:* VARIABLE
EVENT_ONCACHESLICECHANGED

### EVENT_ONMASTERCLIENTCHANGED
*Type:* VARIABLE
EVENT_ONMASTERCLIENTCHANGED

### EVENT_ONCUSTOMAUTHENTICATIONINTERMEDIATESTEP
*Type:* VARIABLE
EVENT_ONCUSTOMAUTHENTICATIONINTERMEDIATESTEP

### EVENT_ONAVAILABLEREGIONS
*Type:* VARIABLE
EVENT_ONAVAILABLEREGIONS

### EVENT_ONSECRETRECEIVAL
*Type:* VARIABLE
EVENT_ONSECRETRECEIVAL

### EVENT_ONDIRECTCONNECTIONESTABLISHED
*Type:* VARIABLE
EVENT_ONDIRECTCONNECTIONESTABLISHED

### EVENT_ONDIRECTCONNECTIONFAILEDTOESTABLISH
*Type:* VARIABLE
EVENT_ONDIRECTCONNECTIONFAILEDTOESTABLISH

### EVENT_ONDIRECTMESSAGE
*Type:* VARIABLE
EVENT_ONDIRECTMESSAGE

### EVENT_ONCUSTOMOPERATIONRESPONSE
*Type:* VARIABLE
EVENT_ONCUSTOMOPERATIONRESPONSE

### EVENT_ONGETROOMLISTRESPONSE
*Type:* VARIABLE
EVENT_ONGETROOMLISTRESPONSE

### AUTH_CUSTOM
*Type:* VARIABLE
Use a custom authentication service.

### AUTH_STEAM
*Type:* VARIABLE
Authenticates users by their Steam Account. Pass L"ticket=[ticket]" to setParameters().

### AUTH_FACEBOOK
*Type:* VARIABLE
Authenticates users by their Facebook Account. Pass L"token=[token]" to setParameters().

### AUTH_OCULUS
*Type:* VARIABLE
Authenticates users by their Oculus Account. Pass L"userid=[userid]&nonce=[nonce]" to setParameters().

### AUTH_PLAYSTATION_4
*Type:* VARIABLE
Authenticates users by their PSN Account. Pass L"token=[token]&env=[env]&userName=[userName]" to setParameters().

### AUTH_XBOX
*Type:* VARIABLE
Authenticates users by their XBox Network Account. Pass the XSTS token to setData().

### AUTH_VIVEPORT
*Type:* VARIABLE
Authenticates users by their HTC Viveport Account and user token. Pass L"userToken=[userToken]" to setParameters().

### AUTH_NINTENDO_SWITCH
*Type:* VARIABLE
Authenticates users by their Nintendo Account. Pass L"token=[token]&appversion=[appversion]" to setParameters(). The appversion is optional.

### AUTH_PLAYSTATION_5
*Type:* VARIABLE
Authenticates users by their PSN Account. Pass L"token=[token]&env=[env]&userName=[userName]" to setParameters().

### AUTH_EPIC
*Type:* VARIABLE
Authenticates users by their Epic Online Services (EOS) Account. Pass L"token=[token]&ownershipToken=[ownershipToken]" to setParameters(). The ownershipToken is optional.

### AUTH_FACEBOOK_GAMING
*Type:* VARIABLE
Authenticates users by their Facebook Account. Pass L"token=[token]" to setParameters().

### AUTH_NONE
*Type:* VARIABLE
Disables custom authentication.

### SERVER_TYPE_NAME_SERVER
*Type:* VARIABLE
Photon Cloud and for self-hosted Photon 5 or higher Server instances

### SERVER_TYPE_MASTER_SERVER
*Type:* VARIABLE
Self-hosted Photon 4 Server instances

### MATCHMAKINGMODE_FILL_ROOM
*Type:* VARIABLE
Fills up rooms (oldest first) to get players together as fast as possible. Default. Makes most sense with MaxPlayers > 0 and games that can only start with more players.

### MATCHMAKINGMODE_SERIAL_MATCHING
*Type:* VARIABLE
Distributes players across available rooms sequentially but takes filters into account. Without filters, rooms get players evenly distributed.

### MATCHMAKINGMODE_RANDOM_MATCHING
*Type:* VARIABLE
Joins a (fully) random room. Expected properties must match, but aside from this, any available room might be selected.

### LOBBYTYPE_DEFAULT
*Type:* VARIABLE
This lobby type is used unless another lobby type is specified. Room lists will be sent and Client::opJoinRandomRoom() can filter by matching properties.

### LOBBYTYPE_SQL_LOBBY
*Type:* VARIABLE
This lobby type lists rooms like type DEFAULT but  SQL-like "where" clauses for filtering can be used with Client::opJoinRandomRoom(). This allows 'bigger', 'less', 'or' and 'and' combinations.

### LOBBYTYPE_ASYNC_RANDOM_LOBBY
*Type:* VARIABLE
This lobby does not send room lists. It is only used for Client::opJoinRandomRoom(). It keeps rooms available for matchmaking for a while even when there are only inactive users left.

### DIRECTMODE_NONE
*Type:* VARIABLE
Do not create any 2p2 connections between the clients. This is the default.

### DIRECTMODE_ALL_TO_OTHERS
*Type:* VARIABLE
Each client establishes a direct connection with every other client inside the room.

### DIRECTMODE_MASTER_TO_OTHERS
*Type:* VARIABLE
The master client establishes a direct connection with every other client inside the room. All other clients only establish a direct connection with the master client but not with each other.

### DIRECTMODE_ALL_TO_ALL
*Type:* VARIABLE
Each client establishes a direct connection with every client inside the room, including itself.

### DIRECTMODE_MASTER_TO_ALL
*Type:* VARIABLE
The master client establishes a direct connection with every client inside the room, including itself. All other clients only establish a direct connection with the master client but not with each other.
