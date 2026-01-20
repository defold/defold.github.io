# extension-crazygames

**Namespace:** `crazygames`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with the CrazyGames SDK APIs

## API

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

### crazygames.is_ad_blocked
*Type:* FUNCTION
Detect if the user has an adblocker.

**Parameters**

- `callback` (function)

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
Display a button in the game footer, that opens a popup containing an invite link.

**Parameters**

- `params` (table)

**Returns**

- `string`

### crazygames.hide_invite_button
*Type:* FUNCTION
Hide the invite button when it is no longer necessary.

### crazygames.get_invite_param
*Type:* FUNCTION
Get an invite link parameters.

**Parameters**

- `key` (string)

**Returns**

- `string`

### crazygames.is_instant_multiplayer
*Type:* FUNCTION
For multiplayer games, if is_instant_multiplayer() returns true, you should instantly create a new room/lobby for the user.

**Returns**

- `boolean`

### crazygames.clear_data
*Type:* FUNCTION
Remove all data items from the local storage.

### crazygames.get_item
*Type:* FUNCTION
Get a data item from the local storage.

**Parameters**

- `key` (string)

**Returns**

- `string`

### crazygames.remove_item
*Type:* FUNCTION
Remove a data item from the local storage.

**Parameters**

- `key` (string)

### crazygames.set_item
*Type:* FUNCTION
Add a data item to the local storage.

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
Retrieve the user currently logged in CrazyGames. If the user is not logged in CrazyGames, the returned user will be null. Will call the provided callback with the logged in user account.

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
Show an account linking prompt to link a CrazyGames account to the in-game account.
