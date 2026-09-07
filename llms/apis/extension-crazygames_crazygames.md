# extension-crazygames

**Namespace:** `crazygames`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with the CrazyGames SDK APIs

## API

### crazygames.get_environment
*Type:* FUNCTION
Get the CrazyGames SDK environment. SDK functionality should only be used when the result is "local" or "crazygames".

**Returns**

- `string`

### crazygames.get_game_settings
*Type:* FUNCTION
Get the current CrazyGames game settings, including muteAudio and disableChat.

**Returns**

- `table` - The current settings table, or nil if settings are unavailable.

### crazygames.add_settings_change_listener
*Type:* FUNCTION
Register a listener that is called whenever the CrazyGames game settings change. Registering again replaces the previous listener.

**Parameters**

- `callback` (function) - The function takes two arguments, self and the updated settings table.

### crazygames.remove_settings_change_listener
*Type:* FUNCTION
Remove the currently registered game-settings listener.

### crazygames.gameplay_start
*Type:* FUNCTION
The gameplayStart() function has to be called whenever the player starts playing or resumes playing after a break (menu/loading/achievement screen, game paused, etc.)

### crazygames.gameplay_stop
*Type:* FUNCTION
The gameplayStop() function has to be called on every game break (entering a menu, switching level, pausing the game, ...) don't forget to call gameplayStart() when the gameplay resumes

### crazygames.loading_start
*Type:* FUNCTION
The loadingStart() function has to be called whenever you start loading your game.

### crazygames.loading_stop
*Type:* FUNCTION
The loadingStop() function has to be called when the loading is complete and eventually the gameplay starts.

### crazygames.happytime
*Type:* FUNCTION
Celebrate a major player achievement, such as beating a boss or reaching a high score.

### crazygames.show_rewarded_ad
*Type:* FUNCTION
Show a rewarded ad.

**Parameters**

- `callback` (function)

### crazygames.show_midgame_ad
*Type:* FUNCTION
Show a midgame ad.

**Parameters**

- `callback` (function)

### crazygames.has_ad_block
*Type:* FUNCTION
Detect if the user has an adblocker.

**Parameters**

- `callback` (function) - The function takes two arguments, self and a boolean indicating whether an adblocker was detected.

### crazygames.request_banner
*Type:* FUNCTION
Request a banner. The container will be resized to the specified width.

**Parameters**

- `div` (string)
- `width` (number)
- `height` (number)

### crazygames.request_responsive_banner
*Type:* FUNCTION
The responsive banners feature will request ads that fit into your container, without the need to specify or select a size beforehand.

**Parameters**

- `div` (string)

### crazygames.clear_banner
*Type:* FUNCTION
Clear a banner. Will also hide it.

**Parameters**

- `div` (string)

### crazygames.clear_all_banners
*Type:* FUNCTION
Clear all banners.

### crazygames.invite_link
*Type:* FUNCTION
Create a link to your game to invite others to join a multiplayer game.

**Parameters**

- `params` (table)

**Returns**

- `string`

### crazygames.show_invite_button
*Type:* FUNCTION
Display a button in the game footer that opens a popup containing an invite link. This CrazyGames feature is deprecated in favor of Room Data, but remains available for existing integrations.

**Parameters**

- `params` (table)

**Returns**

- `string`

### crazygames.hide_invite_button
*Type:* FUNCTION
Hide the invite button when it is no longer necessary.

### crazygames.get_invite_param
*Type:* FUNCTION
Get an invite link parameter.

**Parameters**

- `key` (string)

**Returns**

- `string` - The parameter value, or nil if the parameter is missing.

### crazygames.get_invite_params
*Type:* FUNCTION
Get all invite parameters supplied when the game was opened from an invite link.

**Returns**

- `table` - The invite parameters, or nil if the game was not opened from an invite link.

### crazygames.is_instant_multiplayer
*Type:* FUNCTION
For multiplayer games, if is_instant_multiplayer() returns true, you should instantly create a new room/lobby for the user.

**Returns**

- `boolean`

### crazygames.update_room
*Type:* FUNCTION
Update the current multiplayer room. The table can contain roomId (string), isJoinable (boolean), and inviteParams (a table of string, number, or boolean values). Only supplied fields are updated.

**Parameters**

- `room` (table)

### crazygames.left_room
*Type:* FUNCTION
Notify CrazyGames that the player has left the current multiplayer room.

### crazygames.add_join_room_listener
*Type:* FUNCTION
Register a listener for requests to join a multiplayer room. Registering again replaces the previous listener.

**Parameters**

- `callback` (function) - The function takes two arguments, self and the invite parameters table.

### crazygames.remove_join_room_listener
*Type:* FUNCTION
Remove the currently registered join-room listener.

### crazygames.clear_data
*Type:* FUNCTION
Remove all stored game data from the CrazyGames data module.

### crazygames.get_item
*Type:* FUNCTION
Get a stored value from the CrazyGames data module.

**Parameters**

- `key` (string)

**Returns**

- `string` - The stored value, or nil if the key does not exist.

### crazygames.remove_item
*Type:* FUNCTION
Remove a stored value from the CrazyGames data module.

**Parameters**

- `key` (string)

### crazygames.set_item
*Type:* FUNCTION
Store a value in the CrazyGames data module.

**Parameters**

- `key` (string)
- `value` (string)

### crazygames.is_user_account_available
*Type:* FUNCTION
Before using any user account features, you should always ensure that the user account system is available.

**Returns**

- `boolean`

### crazygames.get_user
*Type:* FUNCTION
Retrieve the user currently logged in CrazyGames. If the user is not logged in CrazyGames, the callback receives nil. Will call the provided callback with the logged in user account.

**Parameters**

- `callback` (function) - The function takes two arguments, self and the user table

### crazygames.get_user_token
*Type:* FUNCTION
The user token is in JWT format and contains the userId of the player that is currently logged in to CrazyGames, as well as other useful information. You should send it to your server when required, and verify/decode it there to extract the userId. Will call the provided callback with the token.

**Parameters**

- `callback` (function) - The function takes two arguments, self and the token

### crazygames.get_xsolla_user_token
*Type:* FUNCTION
Generates a custom Xsolla token that you use with the Xsolla SDK. Will call the provided callback with the token.

**Parameters**

- `callback` (function) - The function takes two arguments, self and the xsolla token

### crazygames.show_auth_prompt
*Type:* FUNCTION
By calling this method, the log in or register popup will be displayed on CrazyGames. The user can log in their existing account, or create a new account. Will call the provided callback on log in.

**Parameters**

- `callback` (function) - The function takes two arguments, self and the user table

### crazygames.set_auth_listener
*Type:* FUNCTION
You can register a user auth listener that is triggered when the player logs in to CrazyGames. A log out doesn't trigger the auth listener, since the entire page is refreshed when the player logs out.

**Parameters**

- `callback` (function) - The function takes two arguments, self and the user table

### crazygames.remove_auth_listener
*Type:* FUNCTION
Remove any previously set auth listener.

### crazygames.show_account_link_prompt
*Type:* FUNCTION
Show an account linking prompt to link a CrazyGames account to the in-game account. Will call the provided callback with a response table containing either response = "yes" or response = "no". The response is nil if the prompt fails.

**Parameters**

- `callback` (function) - The function takes two arguments, self and the response table
