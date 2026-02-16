# extension-steam

**Namespace:** `steam`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Steamworks.

## API

### steam.init
*Type:* FUNCTION
Initialize Steamworks.

**Returns**

- `boolean` - True if successful

- `string` - Error message if unsuccessful.

### steam.update
*Type:* FUNCTION
Update Steamworks. Call this from a script component.

### steam.restart
*Type:* FUNCTION
Restart Steamworks.

**Parameters**

- `appid` (number)

### steam.final
*Type:* FUNCTION
Finalize Steamworks.

### EFloatingGamepadTextInputModeModeSingleLine
*Type:* VARIABLE
Enter dismisses the keyboard

### EFloatingGamepadTextInputModeModeMultipleLines
*Type:* VARIABLE
User needs to explicitly dismiss the keyboard

### EFloatingGamepadTextInputModeModeEmail
*Type:* VARIABLE
Keyboard is displayed in a special mode that makes it easier to enter emails

### EFloatingGamepadTextInputModeModeNumeric
*Type:* VARIABLE
Numeric keypad is shown

### EGamepadTextInputModeNormal
*Type:* VARIABLE
Normal text input

### EGamepadTextInputModePassword
*Type:* VARIABLE
Password text input

### EGamepadTextInputLineModeSingleLine
*Type:* VARIABLE
Single line text

### EGamepadTextInputLineModeMultipleLines
*Type:* VARIABLE
Multi line text

### ELeaderboardDataRequestGlobal
*Type:* VARIABLE
Requests rows in the leaderboard from the full table.

### ELeaderboardDataRequestGlobalAroundUser
*Type:* VARIABLE
Requests rows in the leaderboard from rows around the user.

### ELeaderboardDataRequestFriends
*Type:* VARIABLE
Requests all the rows for friends of the current user.

### ELeaderboardSortMethodNone
*Type:* VARIABLE

### ELeaderboardSortMethodAscending
*Type:* VARIABLE
Top-score is lowest number.

### ELeaderboardSortMethodDescending
*Type:* VARIABLE
Top-score is highest number.

### ELeaderboardUploadScoreMethodNone
*Type:* VARIABLE

### ELeaderboardUploadScoreMethodKeepBest
*Type:* VARIABLE
Leaderboard will keep user's best score.

### ELeaderboardUploadScoreMethodForceUpdate
*Type:* VARIABLE
Leaderboard will always replace score with specified.

### ELeaderboardDisplayTypeNone
*Type:* VARIABLE

### ELeaderboardDisplayTypeNumeric
*Type:* VARIABLE
Simple numerical score.

### ELeaderboardDisplayTypeTimeSeconds
*Type:* VARIABLE
The score represents a time, in seconds.

### ELeaderboardDisplayTypeTimeMilliSeconds
*Type:* VARIABLE
The score represents a time, in milliseconds.

### EOverlayToStoreFlag_None
*Type:* VARIABLE
Passed as parameter to the store.

### EOverlayToStoreFlag_AddToCart
*Type:* VARIABLE
Passed as parameter to the store.

### EOverlayToStoreFlag_AddToCartAndShow
*Type:* VARIABLE
Passed as parameter to the store.

### EActivateGameOverlayToWebPageMode_Default
*Type:* VARIABLE
Passed as parameter to ActivateGameOverlayToWebPage.

### EActivateGameOverlayToWebPageMode_Modal
*Type:* VARIABLE
Passed as parameter to ActivateGameOverlayToWebPage.

### EPersonaStateOffline
*Type:* VARIABLE
Friend is not currently logged on.

### EPersonaStateOnline
*Type:* VARIABLE
Friend is logged on.

### EPersonaStateBusy
*Type:* VARIABLE
User is on, but busy.

### EPersonaStateAway
*Type:* VARIABLE
Auto-away feature.

### EPersonaStateSnooze
*Type:* VARIABLE
Auto-away for a long time.

### EPersonaStateLookingToTrade
*Type:* VARIABLE
Online, trading.

### EPersonaStateLookingToPlay
*Type:* VARIABLE
Online, wanting to play.

### EPersonaStateInvisible
*Type:* VARIABLE
Online, but appears offline to friends.  This status is never published to clients.

### EFriendFlagNone
*Type:* VARIABLE
EFriendFlagNone

### EFriendFlagBlocked
*Type:* VARIABLE
EFriendFlagBlocked

### EFriendFlagFriendshipRequested
*Type:* VARIABLE
EFriendFlagFriendshipRequested

### EFriendFlagImmediate
*Type:* VARIABLE
EFriendFlagImmediate

### EFriendFlagClanMember
*Type:* VARIABLE
EFriendFlagClanMember

### EFriendFlagOnGameServer
*Type:* VARIABLE
EFriendFlagOnGameServer

### EFriendFlagRequestingFriendship
*Type:* VARIABLE
EFriendFlagRequestingFriendship

### EFriendFlagRequestingInfo
*Type:* VARIABLE
EFriendFlagRequestingInfo

### EFriendFlagIgnored
*Type:* VARIABLE
EFriendFlagIgnored

### EFriendFlagIgnoredFriend
*Type:* VARIABLE
EFriendFlagIgnoredFriend

### EFriendFlagChatMember
*Type:* VARIABLE
EFriendFlagChatMember

### EFriendFlagAll
*Type:* VARIABLE
EFriendFlagAll

### SteamNetworkingSend_Unreliable
*Type:* VARIABLE
SteamNetworkingSend_Unreliable

### SteamNetworkingSend_NoNagle
*Type:* VARIABLE
SteamNetworkingSend_NoNagle

### SteamNetworkingSend_UnreliableNoNagle
*Type:* VARIABLE
SteamNetworkingSend_UnreliableNoNagle

### SteamNetworkingSend_NoDelay
*Type:* VARIABLE
SteamNetworkingSend_NoDelay

### SteamNetworkingSend_UnreliableNoDelay
*Type:* VARIABLE
SteamNetworkingSend_UnreliableNoDelay

### SteamNetworkingSend_Reliable
*Type:* VARIABLE
SteamNetworkingSend_Reliable

### SteamNetworkingSend_ReliableNoNagle
*Type:* VARIABLE
SteamNetworkingSend_ReliableNoNagle

### SteamNetworkingSend_UseCurrentThread
*Type:* VARIABLE
SteamNetworkingSend_UseCurrentThread

### SteamNetworkingSend_AutoRestartBrokenSession
*Type:* VARIABLE
SteamNetworkingSend_AutoRestartBrokenSession

### ESteamNetConnectionEnd_Invalid
*Type:* VARIABLE
ESteamNetConnectionEnd_Invalid

### ESteamNetConnectionEnd_App_Generic
*Type:* VARIABLE
ESteamNetConnectionEnd_App_Generic

### ESteamNetConnectionEnd_AppException_Generic
*Type:* VARIABLE
ESteamNetConnectionEnd_AppException_Generic

### ESteamNetConnectionEnd_Local_OfflineMode
*Type:* VARIABLE
ESteamNetConnectionEnd_Local_OfflineMode

### ESteamNetConnectionEnd_Local_ManyRelayConnectivity
*Type:* VARIABLE
ESteamNetConnectionEnd_Local_ManyRelayConnectivity

### ESteamNetConnectionEnd_Local_HostedServerPrimaryRelay
*Type:* VARIABLE
ESteamNetConnectionEnd_Local_HostedServerPrimaryRelay

### ESteamNetConnectionEnd_Local_NetworkConfig
*Type:* VARIABLE
ESteamNetConnectionEnd_Local_NetworkConfig

### ESteamNetConnectionEnd_Local_Rights
*Type:* VARIABLE
ESteamNetConnectionEnd_Local_Rights

### ESteamNetConnectionEnd_Local_P2P_ICE_NoPublicAddresses
*Type:* VARIABLE
ESteamNetConnectionEnd_Local_P2P_ICE_NoPublicAddresses

### ESteamNetConnectionEnd_Remote_Timeout
*Type:* VARIABLE
ESteamNetConnectionEnd_Remote_Timeout

### ESteamNetConnectionEnd_Remote_BadCrypt
*Type:* VARIABLE
ESteamNetConnectionEnd_Remote_BadCrypt

### ESteamNetConnectionEnd_Remote_BadCert
*Type:* VARIABLE
ESteamNetConnectionEnd_Remote_BadCert

### ESteamNetConnectionEnd_Remote_BadProtocolVersion
*Type:* VARIABLE
ESteamNetConnectionEnd_Remote_BadProtocolVersion

### ESteamNetConnectionEnd_Remote_P2P_ICE_NoPublicAddresses
*Type:* VARIABLE
ESteamNetConnectionEnd_Remote_P2P_ICE_NoPublicAddresses

### ESteamNetConnectionEnd_Misc_Generic
*Type:* VARIABLE
ESteamNetConnectionEnd_Misc_Generic

### ESteamNetConnectionEnd_Misc_InternalError
*Type:* VARIABLE
ESteamNetConnectionEnd_Misc_InternalError

### ESteamNetConnectionEnd_Misc_Timeout
*Type:* VARIABLE
ESteamNetConnectionEnd_Misc_Timeout

### ESteamNetConnectionEnd_Misc_SteamConnectivity
*Type:* VARIABLE
ESteamNetConnectionEnd_Misc_SteamConnectivity

### ESteamNetConnectionEnd_Misc_NoRelaySessionsToClient
*Type:* VARIABLE
ESteamNetConnectionEnd_Misc_NoRelaySessionsToClient

### ESteamNetConnectionEnd_Misc_P2P_Rendezvous
*Type:* VARIABLE
ESteamNetConnectionEnd_Misc_P2P_Rendezvous

### ESteamNetConnectionEnd_Misc_P2P_NAT_Firewall
*Type:* VARIABLE
ESteamNetConnectionEnd_Misc_P2P_NAT_Firewall

### ESteamNetConnectionEnd_Misc_PeerSentNoConnection
*Type:* VARIABLE
ESteamNetConnectionEnd_Misc_PeerSentNoConnection

### ESteamNetworkingConnectionState_None
*Type:* VARIABLE
ESteamNetworkingConnectionState_None

### ESteamNetworkingConnectionState_Connecting
*Type:* VARIABLE
ESteamNetworkingConnectionState_Connecting

### ESteamNetworkingConnectionState_FindingRoute
*Type:* VARIABLE
ESteamNetworkingConnectionState_FindingRoute

### ESteamNetworkingConnectionState_Connected
*Type:* VARIABLE
ESteamNetworkingConnectionState_Connected

### ESteamNetworkingConnectionState_ClosedByPeer
*Type:* VARIABLE
ESteamNetworkingConnectionState_ClosedByPeer

### ESteamNetworkingConnectionState_ProblemDetectedLocally
*Type:* VARIABLE
ESteamNetworkingConnectionState_ProblemDetectedLocally

### ELobbyTypePrivate
*Type:* VARIABLE
ELobbyTypePrivate only way to join the lobby is to invite to someone else

### ELobbyTypeFriendsOnly
*Type:* VARIABLE
ELobbyTypeFriendsOnly shows for friends or invitees, but not in lobby list

### ELobbyTypePublic
*Type:* VARIABLE
ELobbyTypePublic visible for friends and in lobby list

### ELobbyTypeInvisible
*Type:* VARIABLE
ELobbyTypeInvisible returned by search, but not visible to other friends

### ELobbyTypePrivateUnique
*Type:* VARIABLE
ELobbyTypePrivateUnique private, unique and does not delete when empty

### EAuthSessionResponseOK
*Type:* VARIABLE
EAuthSessionResponseOK Steam has verified the user is online, the ticket is valid and ticket has not been reused.

### EAuthSessionResponseUserNotConnectedToSteam
*Type:* VARIABLE
EAuthSessionResponseUserNotConnectedToSteam The user in question is not connected to steam.

### EAuthSessionResponseNoLicenseOrExpired
*Type:* VARIABLE
EAuthSessionResponseNoLicenseOrExpired The user doesn't have a license for this App ID or the ticket has expired.

### EAuthSessionResponseVACBanned
*Type:* VARIABLE
EAuthSessionResponseVACBanned The user is VAC banned for this game.

### EAuthSessionResponseLoggedInElseWhere
*Type:* VARIABLE
EAuthSessionResponseLoggedInElseWhere The user account has logged in elsewhere and the session containing the game instance has been disconnected.

### EAuthSessionResponseVACCheckTimedOut
*Type:* VARIABLE
EAuthSessionResponseVACCheckTimedOut VAC has been unable to perform anti-cheat checks on this user.

### EAuthSessionResponseAuthTicketCanceled
*Type:* VARIABLE
EAuthSessionResponseAuthTicketCanceled The ticket has been canceled by the issuer.

### EAuthSessionResponseAuthTicketInvalidAlreadyUsed
*Type:* VARIABLE
EAuthSessionResponseAuthTicketInvalidAlreadyUsed This ticket has already been used, it is not valid.

### EAuthSessionResponseAuthTicketInvalid
*Type:* VARIABLE
EAuthSessionResponseAuthTicketInvalid This ticket is not from a user instance currently connected to steam.

### EAuthSessionResponsePublisherIssuedBan
*Type:* VARIABLE
EAuthSessionResponsePublisherIssuedBan The user is banned for this game. The ban came via the web api and not VAC.

### EAuthSessionResponseAuthTicketNetworkIdentityFailure
*Type:* VARIABLE
EAuthSessionResponseAuthTicketNetworkIdentityFailure The network identity in the ticket does not match the server authenticating the ticket.

### steam.apps_is_dlc_installed
*Type:* FUNCTION
Takes AppID of DLC and checks if the user owns the DLC & if the DLC is installed.

**Parameters**

- `app_id` (number)

**Returns**

- `boolean`

### steam.friends_get_friend_persona_name
*Type:* FUNCTION
Returns the name of another user. Same rules as GetFriendPersonaState() apply as to whether or not the user knowns the name of the other user note that on first joining a lobby, chat room or game server the local user will not known the name of the other users automatically; that information will arrive asyncronously.

**Parameters**

- `steamIDFriend` (string)

**Returns**

- `string` - Name of user

### steam.friends_get_persona_name
*Type:* FUNCTION
Returns the local players name - guaranteed to not be NULL. This is the same name as on the users community profile page. This is stored in UTF-8 format.

**Returns**

- `string` - Name of user

### steam.friends_get_persona_state
*Type:* FUNCTION
Gets the status of the current user. Returned as EPersonaState.

**Returns**

- `number` - Status of user.

### steam.friends_get_friend_count
*Type:* FUNCTION
Friend iteration. Takes a set of EFriendFlags, and returns the number of users the client knows about who meet that criteria. Then GetFriendByIndex() can then be used to return the id's of each of those users.

**Parameters**

- `iFriendFlags` (number) - Set of friend flags to match friends against.

**Returns**

- `number` - Number of users matching search.

### steam.friends_get_friend_by_index
*Type:* FUNCTION
Returns the steamID of a user. The returned CSteamID can then be used by all the functions below to access details about the user.

**Parameters**

- `iFriend` (number) - Is a index of range [0, GetFriendCount())

- `iFriendsFlags` (number) - Must be the same value as used in GetFriendCount()

**Returns**

- `string` - Steam id of the user

### steam.friends_get_friend_persona_state
*Type:* FUNCTION
Returns the current status of the specified user. This will only be known by the local user if steamIDFriend is in their friends list; on the same game server; in a chat room or lobby; or in a small group with the local user.

**Parameters**

- `steamIDFriend` (string) - Id of friend

**Returns**

- `number` - State of friend

### steam.friends_get_friend_steam_level
*Type:* FUNCTION
Get friends steam level.

**Parameters**

- `steamIDFriend` (string) - Id of friend

**Returns**

- `number` - Steam level of friend

### steam.friends_get_friend_relationship
*Type:* FUNCTION
Returns a relationship to a user.

**Parameters**

- `steamIDFriend` (string) - Id of friend

**Returns**

- `number` - Relationship to the user.

### steam.friends_get_small_friend_avatar
*Type:* FUNCTION
Gets a handle to the small (32*32px) avatar for the specified user. This is a handle to be used in IClientUtils::GetImageRGBA(), or 0 if none set

**Parameters**

- `steamIDFriend` (string) - Id of friend

**Returns**

- `number` - Image handle.

### steam.friends_get_medium_friend_avatar
*Type:* FUNCTION
Gets a handle to the medium (64*64px) avatar for the specified user. This is a handle to be used in IClientUtils::GetImageRGBA(), or 0 if none set

**Parameters**

- `steamIDFriend` (string) - Id of friend

**Returns**

- `number` - Image handle.

### steam.friends_get_large_friend_avatar
*Type:* FUNCTION
Gets a handle to the large (128*128px) avatar for the specified user. This is a handle to be used in IClientUtils::GetImageRGBA(), or 0 if none set

**Parameters**

- `steamIDFriend` (string) - Id of friend

**Returns**

- `number` - Image handle.

### steam.friends_activate_game_overlay_to_store
*Type:* FUNCTION
Activates game overlay to store page for app.

**Parameters**

- `app_id` (number)
- `flag` (number) - EOverlayToStoreFlag

### steam.friends_activate_game_overlay_to_web_page
*Type:* FUNCTION
Activates game overlay web browser directly to the specified URL. Full address with protocol type is required, e.g. http://www.steamgames.com/

**Parameters**

- `url` (string)
- `mode` (number) - EActivateGameOverlayToWebPageMode

### steam.friends_set_rich_presence
*Type:* FUNCTION
Sets a Rich Presence key/value for the current user.

**Parameters**

- `key` (string)
- `value` (string)

**Returns**

- `boolean` - True if the rich presence was set successfully, otherwise False.

### steam.friends_clear_rich_presence
*Type:* FUNCTION
Clears all of the current user's Rich Presence key/values.

### steam.friends_invite_user_to_game
*Type:* FUNCTION
Invites a friend or clan member to the current game using a special invite string. If the target accepts the invite, a GameRichPresenceJoinRequested_t callback is posted containing the connect string.

**Parameters**

- `steamIDFriend` (string) - Id of friend

- `connect` (string) - String

**Returns**

- `boolean`

### steam.set_listener
*Type:* FUNCTION
Set a listener.

**Parameters**

- `listener` (function) - Listener function to call

### steam.matchmaking_add_request_lobby_list_string_filter
*Type:* FUNCTION
Adds a string comparison filter to the next RequestLobbyList call.

**Parameters**

- `key` (string)
- `value` (number)
- `cmp` (number)

### steam.matchmaking_add_request_lobby_list_numerical_filter
*Type:* FUNCTION
Adds a numerical comparison filter to the next RequestLobbyList call.

**Parameters**

- `key` (string)
- `value` (number)
- `cmp` (number)

### steam.matchmaking_add_request_lobby_list_near_value_filter
*Type:* FUNCTION
Sorts the results closest to the specified value.

**Parameters**

- `key` (string)
- `value` (number)

### steam.matchmaking_add_request_lobby_list_filter_slots_available
*Type:* FUNCTION
Filters to only return lobbies with the specified number of open slots. Available.

**Parameters**

- `slots` (number)

### steam.matchmaking_add_request_lobby_list_distance_filter
*Type:* FUNCTION
Sets the physical distance for which we should search for lobbies, this is. Based on the users IP address and a IP location map on the Steam backed.

**Parameters**

- `dist` (number)

### steam.matchmaking_add_request_lobby_list_result_count_filter
*Type:* FUNCTION
Sets the maximum number of lobbies to return. The lower the count the faster. It is to download the lobby results & details to the client.

**Parameters**

- `max_count` (number)

### steam.matchmaking_add_request_lobby_list_compatible_members_filter
*Type:* FUNCTION
Unused - Checks the player compatibility based on the frenemy system.

**Parameters**

- `steam_id` (string)

### steam.matchmaking_request_lobby_list
*Type:* FUNCTION
Get a filtered list of relevant lobbies. Will return results as a LobbyMatchList_t event

**Returns**

- `string` - Callback id

### steam.matchmaking_get_lobby_by_index
*Type:* FUNCTION
Gets the Steam ID of the lobby at the specified index. This should only be called after a LobbyMatchList_t call result is received

**Parameters**

- `index` (number) - The index of the lobby to get the Steam ID of, from 0 to
LobbyMatchList_t.m_nLobbiesMatching

**Returns**

- `string` - Id of lobby

### steam.matchmaking_create_lobby
*Type:* FUNCTION
Create a new matchmaking lobby. Will generate a LobbyCreated_t, LobbyEnter_t and LobbyDataUpdate_t event

**Parameters**

- `lobby_type` (number) - The type and visibility of this lobby.

- `max_members` (number) - The maximum number of players that can join this lobby.

**Returns**

- `string` - Callback id

### steam.matchmaking_join_lobby
*Type:* FUNCTION
Joins an existing lobby. Will generate a LobbyEnter_t event

**Parameters**

- `lobby_id` (string) - The Steam ID of the lobby to join.

**Returns**

- `string` - Callback id

### steam.matchmaking_leave_lobby
*Type:* FUNCTION
Leave a lobby that the user is currently in. Leave a lobby that the user is currently in; this will take effect immediately on the client side, other users in the lobby will be notified by a LobbyChatUpdate_t callback.

**Parameters**

- `lobby_id` (string) - The lobby to leave

### steam.matchmaking_get_lobby_owner
*Type:* FUNCTION
Returns the current lobby owner. There always one lobby owner - if the current owner leaves, another user in the lobby will become the owner automatically. It is possible (but rare) to join a lobby just as the owner is leaving, thus entering a lobby with self as the owner. You must be a member of the lobby to access this.

**Parameters**

- `lobby_id` (string) - The Steam ID of the lobby to get the owner of.

**Returns**

- `string` - Id of owner

### steam.matchmaking_set_lobby_owner
*Type:* FUNCTION
Changes who the lobby owner is. This can only be set by the owner of the lobby. This will trigger a LobbyDataUpdate_t for all of the users in the lobby, each user should update their local state to reflect the new owner. This is typically accomplished by displaying a crown icon next to the owners name.

**Parameters**

- `lobby_id` (string) - The Steam ID of the lobby to get the owner of.

- `new_owner` (string) - The new owner

### steam.matchmaking_set_lobby_type
*Type:* FUNCTION
Updates what type of lobby this is. This is also set when you create the lobby with CreateLobby. This can only be set by the owner of the lobby.

**Parameters**

- `lobby_id` (string) - The Steam ID of the lobby

- `type` (number) - The lobby type

### steam.matchmaking_set_lobby_joinable
*Type:* FUNCTION
Sets whether or not a lobby is joinable by other players. This always defaults to enabled for a new lobby. If joining is disabled, then no players can join, even if they are a friend or have been invited. Lobbies with joining disabled will not be returned from a lobby search.

**Parameters**

- `lobby_id` (string) - The Steam ID of the lobby

- `joinable` (boolean) - Enable or disable allowing users to join this lobby?

**Returns**

- `boolean` - Success

### steam.matchmaking_set_lobby_member_limit
*Type:* FUNCTION
Set the maximum number of players that can join the lobby. This is also set when you create the lobby with CreateLobby. This can only be set by the owner of the lobby.

**Parameters**

- `lobby_id` (string) - The Steam ID of the lobby to set the member limit for.

- `max_members` (number) - The maximum number of players allowed in this lobby. This
can not be above 250.

**Returns**

- `boolean` - Success

### steam.matchmaking_get_lobby_member_limit
*Type:* FUNCTION
The current limit on the

**Parameters**

- `lobby_id` (string) - The Steam ID of the lobby to get the member limit of.

**Returns**

- `number` - The current limit

### steam.matchmaking_get_num_lobby_members
*Type:* FUNCTION
Gets the number of users in a lobby. This is used for iteration, after calling this then GetLobbyMemberByIndex can be used to get the Steam ID of each person in the lobby. Persona information for other lobby members (name, avatar, etc.) is automatically received and accessible via the ISteamFriends interface. The current user must be in the lobby to retrieve the Steam IDs of other users in that lobby.

**Parameters**

- `lobby_id` (string) - The Steam ID of the lobby to get the owner of.

**Returns**

- `number` - Number of users in the lobby

### steam.matchmaking_get_lobby_member_by_index
*Type:* FUNCTION
Gets the Steam ID of the lobby member at the given index. You must call matchmaking_get_num_lobby_members before calling this. The current user must be in the lobby to retrieve the Steam IDs of other users in that lobby.

**Parameters**

- `lobby_id` (string)
- `index` (number)

**Returns**

- `string` - Id of member

### steam.matchmaking_set_lobby_data
*Type:* FUNCTION
Sets a key/value pair in the lobby metadata.

**Parameters**

- `lobby_id` (string)
- `key` (string)
- `data` (string)

**Returns**

- `boolean`

### steam.matchmaking_set_lobby_member_data
*Type:* FUNCTION
Sets per-user metadata for the local user.

**Parameters**

- `lobby_id` (string)
- `key` (string)
- `data` (string)

### steam.matchmaking_get_lobby_data
*Type:* FUNCTION
Get data associated with this lobby.

**Parameters**

- `lobby_id` (string)
- `key` (string)

**Returns**

- `string` - Data

### steam.matchmaking_get_lobby_member_data
*Type:* FUNCTION
Gets per-user metadata from another player in the specified lobby.

**Parameters**

- `lobby_id` (string)
- `user_id` (string)
- `key` (string)

**Returns**

- `string` - Data

### steam.matchmaking_get_lobby_data_count
*Type:* FUNCTION
Returns the number of metadata keys set on the specified lobby.

**Parameters**

- `lobby_id` (string)

**Returns**

- `number` - Number of keys

### steam.matchmaking_get_lobby_data_by_index
*Type:* FUNCTION
Returns a lobby metadata key/values pair by index.

**Parameters**

- `lobby_id` (string)
- `index` (number)

**Returns**

- `boolean`
- `string`
- `string`

### steam.matchmaking_send_lobby_chat_message
*Type:* FUNCTION
Broadcasts a chat message to the all the users in the lobby.

**Parameters**

- `lobby_id` (string)
- `body` (string)

**Returns**

- `boolean`

### steam.matchmaking_get_lobby_chat_entry
*Type:* FUNCTION
Get a chat message as specified in a LobbyChatMsg_t callback.

**Parameters**

- `lobby_id` (string)
- `index` (number)

**Returns**

- `string`
- `string`
- `number`

### steam.networking_send_message_to_user
*Type:* FUNCTION
Send message.

**Parameters**

- `identity_remote` (string)
- `data` (string)
- `send_flags` (number) - A bitmask of k_nSteamNetworkingSend_xxx options

- `remote_channel` (number) - A routing number you can use to help route message to different systems

### steam.networking_receive_messages_on_channel
*Type:* FUNCTION
Receive message.

**Parameters**

- `localChannel` (number)

**Returns**

- `table`

### steam.networking_accept_session_with_user
*Type:* FUNCTION
Accept session. Call this in response to a SteamNetworkingMessagesSessionRequest_t callback.

**Parameters**

- `identity_remote` (string)

**Returns**

- `boolean` - Returns false if there is no session with the user
pending or otherwise. If there is an existing active session, this function
will return true, even if it is not pending.

### steam.networking_close_session_with_user
*Type:* FUNCTION
Close sesssion. Call this when you're done talking to a user to immediately free up resources under-the-hood

**Parameters**

- `identity_remote` (string)

**Returns**

- `boolean`

### steam.networking_close_channel_with_user
*Type:* FUNCTION
Close channel. Call this when you're done talking to a user on a specific channel.

**Parameters**

- `identity_remote` (string)
- `local_channel` (number)

**Returns**

- `boolean`

### steam.networking_get_session_connection_info
*Type:* FUNCTION
Get connection info. Returns information about the latest state of a connection, if any, with the given peer.

**Parameters**

- `identity_remote` (string)

**Returns**

- `table` - Connection info (state, info, status)

### steam.remote_storage_file_share
*Type:* FUNCTION
Share a file.

**Parameters**

- `filename` (string) - Name of file to share

**Returns**

- `string`

### steam.remote_storage_get_file_count
*Type:* FUNCTION
Get number of uploaded files.

**Returns**

- `number` - File count

### steam.remote_storage_get_file_name_and_size
*Type:* FUNCTION
Get file information.

**Returns**

- `number` - File count

### steam.remote_storage_get_quota
*Type:* FUNCTION
Get storage quota.

**Returns**

- `number` - Available bytes

- `number` - Total bytes

### steam.remote_storage_file_write
*Type:* FUNCTION
Creates a new file, writes the bytes to the file, and then closes the file. If the target file already exists, it is overwritten.

**Parameters**

- `filename` (string) - The name of the file to write to.

- `data` (string)

**Returns**

- `boolean` - Success

### steam.remote_storage_file_read
*Type:* FUNCTION
Opens a binary file, reads the contents of the file into a byte array,. And then closes the file.

**Parameters**

- `filename` (string) - Name of the file to read from

**Returns**

- `string`

### steam.user_get_steam_id
*Type:* FUNCTION
Returns the CSteamID of the account currently logged into the Steam client. A CSteamID is a unique identifier for an account, and used to differentiate users in all parts of the Steamworks API.

**Returns**

- `string`

### steam.user_get_player_steam_level
*Type:* FUNCTION
Gets the Steam Level of the user, as shown on their profile.

**Returns**

- `number`

### steam.user_get_game_badge_level
*Type:* FUNCTION
Trading Card badges data access. If you only have one set of cards, the series will be 1. The user has can have two different badges for a series; the regular (max level 5) and the foil (max level 1).

**Returns**

- `number`
- `boolean`

### steam.user_logged_on
*Type:* FUNCTION
Returns true if the Steam client current has a live connection to the Steam. Servers.

**Returns**

- `boolean`

### steam.user_is_behind_nat
*Type:* FUNCTION
Returns true if this users looks like they are behind a NAT device. Only valid once the user has connected to steam .

**Returns**

- `boolean`

### steam.user_is_phone_verified
*Type:* FUNCTION
Gets whether the users phone number is verified.

**Returns**

- `boolean`

### steam.user_is_phone_identifying
*Type:* FUNCTION
Gets whether the users phone number is identifying.

**Returns**

- `boolean`

### steam.user_is_phone_requiring_verification
*Type:* FUNCTION
Gets whether the users phone number is awaiting (re)verification.

**Returns**

- `boolean`

### steam.user_is_two_factor_enabled
*Type:* FUNCTION
Gets whether the user has two factor enabled on their account.

**Returns**

- `boolean`

### steam.user_get_auth_session_ticket
*Type:* FUNCTION
Get an authentication ticket. Retrieve an authentication ticket to be sent to the entity who wishes to authenticate you.

**Returns**

- `string` - Auth ticket or null

- `number` - Ticket handle or null

- `string` - Error message or null

### steam.user_begin_auth_session
*Type:* FUNCTION
Validate an authentication ticket. Authenticate the ticket from the entity Steam ID to be sure it is valid and isn't reused. Note that identity is not confirmed until the callback ValidateAuthTicketResponse_t is received and the return value in that callback is checked for success.

**Parameters**

- `ticket` (string) - The auth ticket to validate

- `steamId` (string) - The entity's Steam ID that sent this ticket.

**Returns**

- `number`

### steam.user_cancel_auth_ticket
*Type:* FUNCTION
Cancels an auth ticket. Cancels an auth ticket received from GetAuthSessionTicket or GetAuthTicketForWebApi. This should be called when no longer playing with the specified entity.

**Parameters**

- `ticket` (number) - The active auth ticket to cancel.

### steam.user_end_auth_session
*Type:* FUNCTION
Ends an auth session. Ends an auth session that was started with BeginAuthSession. This should be called when no longer playing with the specified entity.

**Parameters**

- `steamId` (string) - The entity to end the active auth session with.

### steam.user_get_auth_ticket_for_web_api
*Type:* FUNCTION
Get an authentication ticket for web API. Request an authentication ticket suitable to authenticated in a web backend. Will trigger a GetTicketForWebApiResponse_t callback when the ticket is ready.

**Parameters**

- `identity` (string) - Optional identity string to associate with the ticket

**Returns**

- `number` - The handle of the requested ticket

- `string` - Error message or null

### steam.user_stats_get_stat_int
*Type:* FUNCTION
Get user stat as an integer. Https://partner.steamgames.com/doc/api/ISteamUserStats#GetStat

**Parameters**

- `id` (string) - Id of the stat to get

**Returns**

- `boolean`
- `number` - The stat or nil

### steam.user_stats_set_stat_int
*Type:* FUNCTION
Set user stat. Https://partner.steamgames.com/doc/api/ISteamUserStats#SetStat

**Parameters**

- `id` (string) - Id of the stat to set

- `stat` (number) - Number to set

**Returns**

- `boolean`

### steam.user_stats_get_stat_float
*Type:* FUNCTION
Get user stat as a floating point number. Https://partner.steamgames.com/doc/api/ISteamUserStats#GetStat

**Parameters**

- `id` (string) - Id of the stat to get

**Returns**

- `boolean`
- `number` - The stat

### steam.user_stats_set_stat_float
*Type:* FUNCTION
Set user stat. Https://partner.steamgames.com/doc/api/ISteamUserStats#SetStat

**Parameters**

- `id` (string) - Id of the stat to set

- `stat` (number) - Number to set

**Returns**

- `boolean`

### steam.user_stats_request_global_stats
*Type:* FUNCTION
Requests global stats data, which is available for stats marked as "aggregated". This call is asynchronous, with the results returned in GlobalStatsReceived_t. nHistoryDays specifies how many days of day-by-day history to retrieve in addition to the overall totals. The limit is 60. https://partner.steamgames.com/doc/api/ISteamUserStats#RequestGlobalStats

**Parameters**

- `history_days` (number)

**Returns**

- `boolean`

### steam.user_stats_store_stats
*Type:* FUNCTION
Store the current data on the server. Will get a callback when set and one callback for every new achievement  If the callback has a result of k_EResultInvalidParam, one or more stats uploaded has been rejected, either because they broke constraints or were out of date. In this case the server sends back updated values. The stats should be re-iterated to keep in sync. https://partner.steamgames.com/doc/api/ISteamUserStats#StoreStats

**Returns**

- `boolean`

### steam.user_stats_reset_all_stats
*Type:* FUNCTION
Reset stats. Https://partner.steamgames.com/doc/api/ISteamUserStats#ResetAllStats

**Parameters**

- `achievements` (boolean) - True if achievements should be reset as well.

**Returns**

- `boolean`

### steam.user_stats_set_achievement
*Type:* FUNCTION
Set achievement. Https://partner.steamgames.com/doc/api/ISteamUserStats#SetAchievement

**Parameters**

- `name` (string)

**Returns**

- `boolean`

### steam.user_stats_get_achievement
*Type:* FUNCTION
Get achievement. Https://partner.steamgames.com/doc/api/ISteamUserStats#GetAchievement

**Parameters**

- `name` (string)

**Returns**

- `boolean`
- `boolean`

### steam.user_stats_clear_achievement
*Type:* FUNCTION
Clear achievement. Https://partner.steamgames.com/doc/api/ISteamUserStats#ClearAchievement

**Parameters**

- `name` (string)

**Returns**

- `boolean`

### steam.user_stats_get_num_achievements
*Type:* FUNCTION
Used for iterating achievements. In general games should not need these functions because they should have a list of existing achievements compiled into them. https://partner.steamgames.com/doc/api/ISteamUserStats#GetNumAchievements

**Returns**

- `number` - Number of achievements.

### steam.user_stats_get_achievement_name
*Type:* FUNCTION
Get achievement name iAchievement in [0,GetNumAchievements). Https://partner.steamgames.com/doc/api/ISteamUserStats#GetAchievementName

**Parameters**

- `index` (number)

**Returns**

- `string`

### steam.user_stats_get_achievement_display_attribute
*Type:* FUNCTION
Get general attributes for an achievement. Accepts the following keys * "name" and "desc" for retrieving the localized achievement name and description (returned in UTF8) * "hidden" for retrieving if an achievement is hidden (returns "0" when not hidden, "1" when hidden) https://partner.steamgames.com/doc/api/ISteamUserStats#GetAchievementDisplayAttribute

**Parameters**

- `name` (string)
- `key` (string) - Either "name", "desc" or "hidden"

**Returns**

- `string`

### steam.user_stats_get_achievement_achieved_percent
*Type:* FUNCTION
Returns the percentage of users who have achieved the specified achievement. Https://partner.steamgames.com/doc/api/ISteamUserStats#GetAchievementAchievedPercent

**Returns**

- `boolean`
- `number`

### steam.user_stats_find_leaderboard
*Type:* FUNCTION
Find a leaderboard. Will return leaderboard asynchronously. https://partner.steamgames.com/doc/api/ISteamUserStats#FindLeaderboard

**Parameters**

- `name` (string)

### steam.user_stats_find_or_create_leaderboard
*Type:* FUNCTION
Gets a leaderboard by name, it will create it if it's not yet created. This call is asynchronous, with the result returned in a listener callback with event set to LeaderboardFindResult_t. https://partner.steamgames.com/doc/api/ISteamUserStats#FindOrCreateLeaderboard

**Parameters**

- `leaderboard_name` (string) - The name of the leaderboard to find or create.

- `eLeaderboardSortMethod` (ELeaderboardSortMethod) - The sort order of the new leaderboard if it's created.

- `eLeaderboardDisplayType` (ELeaderboardDisplayType) - The display type (used by the Steam Community web site) of the new leaderboard if it's created.

### steam.user_stats_get_leaderboard_name
*Type:* FUNCTION
Get the name of a leaderboard. Https://partner.steamgames.com/doc/api/ISteamUserStats#GetLeaderboardName

**Parameters**

- `leaderboard` (string)

**Returns**

- `string`

### steam.user_stats_get_leaderboard_entry_count
*Type:* FUNCTION
Get the total number of entries in a leaderboard, as of the last request. Https://partner.steamgames.com/doc/api/ISteamUserStats#GetLeaderboardEntryCount

**Parameters**

- `leaderboard` (string)

**Returns**

- `number`

### steam.user_stats_get_leaderboard_sort_method
*Type:* FUNCTION
Returns the sort method of the leaderboard. Https://partner.steamgames.com/doc/api/ISteamUserStats#GetLeaderboardSortMethod

**Parameters**

- `leaderboard` (string)

**Returns**

- `number`

### steam.user_stats_get_leaderboard_display_type
*Type:* FUNCTION
Returns the display type of a leaderboard handle. Https://partner.steamgames.com/doc/api/ISteamUserStats#GetLeaderboardDisplayType

**Parameters**

- `leaderboard` (string)

**Returns**

- `number`

### steam.user_stats_download_leaderboard_entries
*Type:* FUNCTION
Asks the Steam back-end for a set of rows in the leaderboard. This call is asynchronous, with the result returned in a listener callback with event set to LeaderboardScoresDownloaded_t. LeaderboardScoresDownloaded_t will contain a handle to pull the results from GetDownloadedLeaderboardEntries(). You can ask for more entries than exist, and it will return as many as do exist. * k_ELeaderboardDataRequestGlobal requests rows in the leaderboard from the full table, with nRangeStart & nRangeEnd in the range [1, TotalEntries] * k_ELeaderboardDataRequestGlobalAroundUser requests rows around the current user, nRangeStart being negate e.g. DownloadLeaderboardEntries( hLeaderboard, k_ELeaderboardDataRequestGlobalAroundUser, -3, 3 ) will return 7 rows, 3 before the user, 3 after * k_ELeaderboardDataRequestFriends requests all the rows for friends of the current user https://partner.steamgames.com/doc/api/ISteamUserStats#DownloadLeaderboardEntries

**Parameters**

- `leaderboard` (string)
- `request` (ELeaderboardDataRequest)
- `start` (number)
- `end` (number)

### steam.user_stats_get_downloaded_leaderboard_entry
*Type:* FUNCTION
Returns data about a single leaderboard entry. Https://partner.steamgames.com/doc/api/ISteamUserStats#GetDownloadedLeaderboardEntry

**Parameters**

- `hSteamLeaderboardEntries` (string) - Leaderboard entries handle

- `index` (number) - Which entry to get

**Returns**

- `boolean`
- `table` - The requested leaderboard entry.

### steam.user_stats_upload_leaderboard_score
*Type:* FUNCTION
Uploads a user score to a specified leaderboard. This call is asynchronous, with the result returned in a listener callback with event set to LeaderboardScoreUploaded_t. https://partner.steamgames.com/doc/api/ISteamUserStats#UploadLeaderboardScore

**Parameters**

- `leaderboard` (string)
- `eLeaderboardUploadScoreMethod` (ELeaderboardUploadScoreMethod)
- `nScore` (number)

### steam.user_stats_attach_leadboard_ugc
*Type:* FUNCTION
Attaches a piece of user generated content the current user's entry on a. Leaderboard. https://partner.steamgames.com/doc/api/ISteamUserStats#AttachLeaderboardUGC

**Parameters**

- `leaderboard` (string)
- `ugc_handle` (string)

**Returns**

- `string` - API call id

### steam.utils_get_app_id
*Type:* FUNCTION
Returns the appID of the current process.

**Returns**

- `number`

### steam.utils_get_seconds_since_app_active
*Type:* FUNCTION
Return the number of seconds since the user.

**Returns**

- `number`

### steam.utils_is_steam_running_on_steam_deck
*Type:* FUNCTION
Returns true if currently running on the Steam Deck device.

**Returns**

- `boolean`

### steam.utils_is_steam_overlay_available
*Type:* FUNCTION
Returns true if the Steam Overlay is running and the user can access it.

**Returns**

- `boolean`

### steam.utils_get_image_size
*Type:* FUNCTION
Get size of image.

**Parameters**

- `image` (number) - Image handle

**Returns**

- `boolean` - True if size of image was read successfully

- `number` - Image width or nil

- `number` - Image height or nil

### steam.utils_get_image_rgba
*Type:* FUNCTION
Get image in RGBA format.

**Parameters**

- `image` (number) - Image handle

- `size` (number) - Size of image

**Returns**

- `boolean` - True if size of image was read successfully

- `string`

### steam.utils_get_server_real_time
*Type:* FUNCTION
Returns the Steam server time in Unix epoch format. (Number of seconds since Jan 1, 1970 UTC).

**Returns**

- `number` - Time

### steam.utils_show_floating_gamepad_text_input
*Type:* FUNCTION
Opens a floating keyboard over the game content and sends OS keyboard keys directly to the game.

**Parameters**

- `mode` (number) - EFloatingGamepadTextInputMode

- `x` (number) - Text field x position

- `y` (number) - Text field y position

- `width` (number) - Text field width

- `height` (number) - Text field height

**Returns**

- `boolean` - True if the floating keyboard was shown, otherwise, false.

### steam.utils_show_gamepad_text_input
*Type:* FUNCTION
Activates the Big Picture text input dialog which only supports gamepad input.

**Parameters**

- `input_mode` (number) - EGamepadTextInputMode

- `line_input_mode` (number) - EGamepadTextInputLineMode

- `description` (string) - Sets the description that should inform the user what the input dialog is for

- `existing_text` (string) - Sets the preexisting text which the user can edit.

**Returns**

- `boolean` - True if the big picture overlay is running; otherwise, false
