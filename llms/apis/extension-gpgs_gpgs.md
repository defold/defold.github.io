# extension-gpgs

**Namespace:** `gpgs`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Google Play Game Services (GPGS) APIs

## API

### gpgs.is_supported
*Type:* FUNCTION
Check if Google Play Services are available & ready on the device.

**Returns**

- `boolean` - Status of Google Play Services on the device.

**Examples**

```
if gpgs then
  local is_supported = gpgs.is_supported()
end

```

### gpgs.login
*Type:* FUNCTION
Login to GPGS using a button.

**Examples**

Log in to GPGS using a button:
```
if gpgs then
  gpgs.login()
end

```

### gpgs.silent_login
*Type:* FUNCTION
Silent login to GPGS.
This function is trying to retrieve the currently signed-in player’s account.

**Examples**

```
function init(self)
  if gpgs then
    gpgs.silent_login()
  end
end

```

### gpgs.get_display_name
*Type:* FUNCTION
Get the current GPGS player display name.

**Returns**

- `string` - The player's display name.

**Examples**

```
if gpgs then
  local name = gpgs.get_display_name()
end

```

### gpgs.get_id
*Type:* FUNCTION
Get the current GPGS player id.

**Returns**

- `string` - The player ID.

**Examples**

```
if gpgs then
  local id = gpgs.get_id()
end

```

### gpgs.get_server_auth_code
*Type:* FUNCTION
Returns a one-time server auth code to send to your web server which can be exchanged for access token
Token can be retrieved only if `gpgs.request_server_auth_code` set to 1 and `gpgs.client` is set.

**Returns**

- `string` - The server auth code for logged in account. Can be nil if operation is not completed yet.
Auth token is avaliable after receiving message with id `gpgs.MSG_GET_SERVER_TOKEN` in callback set via `gpgs.set_callback`.

**Examples**

```
if gpgs then
  local server_auth_code = gpgs.get_server_auth_code()
end

```

### gpgs.is_logged_in
*Type:* FUNCTION
Check if a user is logged in currently.

**Returns**

- `boolean` - Current login state.

**Examples**

```
if gpgs then
  local is_loggedin = gpgs.is_logged_in()
end

```

### gpgs.set_callback
*Type:* FUNCTION
Set callback for receiving messages from GPGS.

**Parameters**

- `callback` (function) - A callback taking the following parameters
  - `self` (object) - The calling script
  - `message_id` (number) - An message_id can be one of the predefined constants below
- `gpgs.MSG_SIGN_IN`
- `gpgs.MSG_SILENT_SIGN_IN`
- `gpgs.MSG_SHOW_SNAPSHOTS`
- `gpgs.MSG_LOAD_SNAPSHOT`
- `gpgs.MSG_SAVE_SNAPSHOT`
  - `message` (table) - Contains information that depends on message_id.
    - `status` (number) - Status of the current operation. It can be one of the predefined constants below
- `gpgs.STATUS_SUCCESS`
- `gpgs.STATUS_FAILED`
- `gpgs.STATUS_CREATE_NEW_SAVE`
- `gpgs.STATUS_CONFLICT`
    - `error` (string) - The error message. Available only if `status` is `gpgs.STATUS_FAILED`.
    - `error_status` (number) - The error code. Available only if `status` is `gpgs.STATUS_FAILED` and GPGS provide this code. It can be one of the predefined constants below
- `gpgs.ERROR_STATUS_SNAPSHOT_COMMIT_FAILED`
- `gpgs.ERROR_STATUS_SNAPSHOT_CONFLICT_MISSING`
- `gpgs.ERROR_STATUS_SNAPSHOT_CONTENTS_UNAVAILABLE`
- `gpgs.ERROR_STATUS_SNAPSHOT_CREATION_FAILED`
- `gpgs.ERROR_STATUS_SNAPSHOT_FOLDER_UNAVAILABLE`
- `gpgs.ERROR_STATUS_SNAPSHOT_NOT_FOUND`
Or it can be ApiException.getStatusCode() (if ApiException was thrown)
    - `metadata` (table) - Metadata of the loaded save. Available only if `message_id` is `gpgs.MSG_LOAD_SNAPSHOT`.
    - `conflictId` (string) - The conflict id. Available only if `status` is `gpgs.STATUS_CONFLICT`.
    - `conflictMetadata` (table) - The conflicting metadata. Available only if `status` is `gpgs.STATUS_CONFLICT`.

**Examples**

```
function callback(self, message_id, message)
  if message_id == gpgs.MSG_SIGN_IN or message_id == gpgs.MSG_SILENT_SIGN_IN then
    if message.status == gpgs.STATUS_SUCCESS then
    -- do something after login
    end
  elseif message_id == gpgs.MSG_LOAD_SNAPSHOT then
  -- do something when a save was loaded
  end
end

function init(self)
  gpgs.set_callback(callback)
end

function init(self)
  gpgs.set_callback(nil) -- remove callback
end

```

### gpgs.snapshot_display_saves
*Type:* FUNCTION
Provides a default saved games selection user interface.

**Parameters**

- `popupTitle` (string) - The title to display in the action bar. By default "Game Saves".
- `allowAddButton` (boolean) - Whether or not to display a "create new snapshot" option in the selection UI. By default `true`.
- `allowDelete` (boolean) - Whether or not to provide a delete overflow menu option for each snapshot in the selection UI. By default `true`.
- `maxNumberOfSavedGamesToShow` (number) - The maximum number of snapshots to display in the UI. By default 5.

**Examples**

```
if gpgs then
  gpgs.snapshot_display_saves("Choose the save of the game", false, true, 10)
end

```

### gpgs.snapshot_open
*Type:* FUNCTION
Opens a snapshot with the given `saveName`. If `createIfNotFound` is set to `true`, the specified snapshot will be created if it does not already exist.

**Parameters**

- `saveName` (string) - The name of the snapshot file to open. Must be between 1 and 100 non-URL-reserved characters (a-z, A-Z, 0-9, or the symbols "-", ".", "_", or "~").
- `createIfNotFound` (boolean) - If `true`, the snapshot will be created if one cannot be found.
- `conflictPolicy` (number) - The conflict resolution policy to use for this snapshot that can be one of the predefined constants below
- `gpgs.RESOLUTION_POLICY_MANUAL`
- `gpgs.RESOLUTION_POLICY_LONGEST_PLAYTIME`
- `gpgs.RESOLUTION_POLICY_LAST_KNOWN_GOOD`
- `gpgs.RESOLUTION_POLICY_MOST_RECENTLY_MODIFIED`
- `gpgs.RESOLUTION_POLICY_HIGHEST_PROGRESS`

Default value is `gpgs.RESOLUTION_POLICY_LAST_KNOWN_GOOD`

**Examples**

```
if gpgs then
  gpgs.snapshot_open("my_save_1", true, gpgs.RESOLUTION_POLICY_LONGEST_PLAYTIME)
end

```

### gpgs.snapshot_commit_and_close
*Type:* FUNCTION
Save the currently opened save on the server and close it.

**Parameters**

- `metadata` (table) - A table with metadata for a save. It contains the fields below
  - `playedTime` (number) - The new played time to set for the snapshot in ms.
  - `progressValue` (number) - The new progress value to set for the snapshot.
  - `description` (string) - The new description to set for the snapshot.
  - `coverImage` (object) - The new cover image to set for the snapshot in `png`.

**Examples**

```
if gpgs then
  local png_img, w, h = screenshot.png()
  gpgs.snapshot_commit_and_close({
      coverImage = png_img,
      description = "LEVEL 31, CAVE",
      playedTime = 12345667,
      progressValue = 657
  })
end

```

### gpgs.snapshot_get_data
*Type:* FUNCTION
Returns the currently opened snapshot data.

**Returns**

- `string` - The byte array data of the currently opened snapshot. `nil` if something goes wrong.
- `string` - An error message if something goes wrong.

**Examples**

```
if gpgs then
  local bytes, error_message = gpgs.snapshot_get_data()
  if not bytes then
      print("snapshot_get_data ERROR:", error_message)
  else
      print("snapshot_get_data",bytes)
      -- Do something with your data
  end
end

```

### gpgs.snapshot_set_data
*Type:* FUNCTION
Sets the data for the currently opened snapshot.

**Parameters**

- `data` (string) - The data to set.

**Returns**

- `boolean` - True if data was set for the currently opened snapshot.
- `string` - An error message if something goes wrong.

**Examples**

```
  if gpgs then
    local success, error_message = gpgs.snapshot_set_data(my_data)
    if not success then
        print("snapshot_set_data ERROR:", error_message)
    end
  end

```

### gpgs.snapshot_is_opened
*Type:* FUNCTION
Check if a snapshot was opened.

**Returns**

- `boolean` - A current snapshot state.

**Examples**

```
if gpgs then
  local is_opened = gpgs.snapshot_is_opened()
end

```

### gpgs.snapshot_get_max_image_size
*Type:* FUNCTION
Returns the maximum data size per snapshot cover image in bytes.

**Returns**

- `number` - The maximum data size per snapshot cover image in bytes.

**Examples**

```
if gpgs then
  local image_size = gpgs.snapshot_get_max_image_size()
end

```

### gpgs.snapshot_get_max_save_size
*Type:* FUNCTION
Returns the maximum data size per snapshot in bytes.

**Returns**

- `number` - The maximum data size per snapshot in bytes.

**Examples**

```
if gpgs then
  local data_size = gpgs.snapshot_get_max_save_size()
end

```

### gpgs.snapshot_get_conflicting_data
*Type:* FUNCTION
Returns the conflicting snapshot data.

**Returns**

- `string` - The byte array data of the conflicting snapshot. `nil` if something goes wrong.
- `boolean` - An error message if something goes wrong.

**Examples**

```
if gpgs then
  local bytes, error_message = gpgs.snapshot_get_conflicting_data()
  if not bytes then
      print("snapshot_get_conflicting_data ERROR:", error_message)
  else
      print("snapshot_get_conflicting_data:",bytes)
      -- Do something with conflicting data data
  end
end

```

### gpgs.snapshot_resolve_conflict
*Type:* FUNCTION
Resolves a conflict using the data from the provided snapshot.

**Parameters**

- `conflictId` (string) - The conflict id that you want to resolve. Provided in `message` table with `STATUS_CONFLICT` message type.
- `snapshotId` (number) - Type of the snapshot you want to use for conflict solving that can be one of the predefined constants below
- `gpgs.SNAPSHOT_CURRENT`
- `gpgs.SNAPSHOT_CONFLICTING`

**Examples**

```
if gpgs then
  gpgs.snapshot_resolve_conflict(self.conflictId, gpgs.SNAPSHOT_CONFLICTING)
end

```

### gpgs.leaderboard_submit_score
*Type:* FUNCTION
Submit a score to a leaderboard for the currently signed-in player.

**Parameters**

- `leaderboardId` (string)
- `score` (number)

### gpgs.leaderboard_get_top_scores
*Type:* FUNCTION
Asynchronously gets the top page of scores for a leaderboard.

**Parameters**

- `leaderboardId` (string)
- `time_span` (number) - One of the gpgs.TIME_SPAN_ constants
- `collection` (number) - One of the gpgs.COLLECTION_ constants
- `max_results` (number) - Between 1-25

### gpgs.leaderboard_get_player_centered_scores
*Type:* FUNCTION
Asynchronously gets a player-centered page of scores for a leaderboard.

**Parameters**

- `leaderboardId` (string)
- `time_span` (number) - One of the gpgs.TIME_SPAN_ constants
- `collection` (number) - One of the gpgs.COLLECTION_ constants
- `max_results` (number) - Between 1-25
- `force_reload` (boolean) - If true, this call will clear any locally cached data and attempt to fetch the latest data from the server

### gpgs.leaderboard_show
*Type:* FUNCTION
Show a leaderboard for a game specified by a leaderboardId.

**Parameters**

- `leaderboardId` (string)
- `time_span` (number) - One of the gpgs.TIME_SPAN_ constants
- `collection` (number) - One of the gpgs.COLLECTION_ constants

### gpgs.leaderboard_list
*Type:* FUNCTION
Show the list of leaderboards.

### gpgs.leaderboard_get_player_score
*Type:* FUNCTION
Asynchronously gets a player-centered page of scores for a leaderboard.

**Parameters**

- `leaderboardId` (string)
- `time_span` (number) - One of the gpgs.TIME_SPAN_ constants
- `collection` (number) - One of the gpgs.COLLECTION_ constants

### gpgs.achievement_reveal
*Type:* FUNCTION
Reveals a hidden achievement to the current player.

**Parameters**

- `achievementId` (string) - Achievement id (from GP console)

### gpgs.achievement_unlock
*Type:* FUNCTION
Unlocks an achievement for the current player.

**Parameters**

- `achievementId` (string) - Achievement id (from GP console)

### gpgs.achievement_set
*Type:* FUNCTION
Sets an achievement to have at least the given number of steps completed.

**Parameters**

- `achievementId` (string) - Achievement id (from GP console)
- `steps` (number) - The number of steps to set the achievement to. Must be greater than 0.

### gpgs.achievement_increment
*Type:* FUNCTION
Increments an achievement by the given number of steps.

**Parameters**

- `achievementId` (string) - Achievement id (from GP console)
- `steps` (number) - The number of steps to increment by. Must be greater than 0.

### gpgs.achievement_show
*Type:* FUNCTION
Show achivements

### gpgs.achievement_get
*Type:* FUNCTION
Get information about all achievement's state asynchronously. Result return to callback previously set by `gpgs.set_callback` with `message_id == gpgs.MSG_ACHIEVEMENTS`. Result is array of tables which contain following fields
- `id` - achievement id (from GP console)
- `name` - achievement name
- `description` - achievement description
- `xp` - how much experience points will be added when achievement will be unlocked
- `steps` - current step of incremental achievement
- `total_steps` - total amount of steps of incremental achievement
- `unlocked` - set to `true` if achievement is unlocked. Otherwise field is missed.
- `hidden` - set to `true if achievement is hidden. Otherwise field is missed.
- `revealed` - set to `true` if achievement is revealed. Otherwise field is missed.

### gpgs.event_increment
*Type:* FUNCTION
Increments an event specified by `eventId` by the given number of steps

**Parameters**

- `eventId` (string) - Event id (from GP console)
- `amount` (number) - The amount increment by. Must be greater than or equal to 0

### gpgs.event_get
*Type:* FUNCTION
Get information about all events asynchronously. Result returns to callback previously set by `gpgs.set_callback` with `message_id == gpgs.MSG_GET_EVENTS`. Result is array of tables which contain following fields
- `id` - event id
- `formatted_value` - sum of all increments have been made to this event
- `value` - the number of increments this user has made to this event
- `description` - event's description
- `image` - URI that can be used to load the event's image icon
- `name` - event's name
- `visible` - whether the event should be displayed to the user in any event related UIs

### RESOLUTION_POLICY_MANUAL
*Type:* VARIABLE
Official [GPGS documentation](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.html#RESOLUTION_POLICY_MANUAL) for this constant

### RESOLUTION_POLICY_LONGEST_PLAYTIME
*Type:* VARIABLE
Official [GPGS documentation](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.html#RESOLUTION_POLICY_LONGEST_PLAYTIME) for this constant

### RESOLUTION_POLICY_LAST_KNOWN_GOOD
*Type:* VARIABLE
Official [GPGS documentation](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.html#RESOLUTION_POLICY_LAST_KNOWN_GOOD) for this constant

### RESOLUTION_POLICY_MOST_RECENTLY_MODIFIED
*Type:* VARIABLE
Official [GPGS documentation](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.html#RESOLUTION_POLICY_MOST_RECENTLY_MODIFIED) for this constant

### RESOLUTION_POLICY_HIGHEST_PROGRESS
*Type:* VARIABLE
Official [GPGS documentation](https://developers.google.com/android/reference/com/google/android/gms/games/SnapshotsClient.html#RESOLUTION_POLICY_HIGHEST_PROGRESS) for this constant

### MSG_SIGN_IN
*Type:* VARIABLE
The message type that GPGS sends when finishing the asynchronous operation after calling `gpgs.login()`

### MSG_SILENT_SIGN_IN
*Type:* VARIABLE
The message type that GPGS sends when finishing the asynchronous operation after calling `gpgs.silent_login()`

### MSG_SHOW_SNAPSHOTS
*Type:* VARIABLE
The message type that GPGS sends when finishing the asynchronous operation after calling `gpgs.snapshot_display_saves()`

### MSG_LOAD_SNAPSHOT
*Type:* VARIABLE
The message type that GPGS sends when finishing the asynchronous operation after calling `gpgs.snapshot_open()`

### MSG_SAVE_SNAPSHOT
*Type:* VARIABLE
The message type that GPGS sends when finishing the asynchronous operation after calling `gpgs.snapshot_commit_and_close()`

### MSG_GET_SERVER_TOKEN
*Type:* VARIABLE
The message type that GPGS sends when finishing the asynchronous operation of server token retrieval

### STATUS_SUCCESS
*Type:* VARIABLE
An operation success.

### STATUS_FAILED
*Type:* VARIABLE
An operation failed. Check the error field in the massage table.

### STATUS_CREATE_NEW_SAVE
*Type:* VARIABLE
A user wants to create new save as a result of `gpgs.snapshot_display_saves()` method. Turn off this button in `gpgs.snapshot_display_saves()` if you don't want to have this functionality.

### STATUS_CONFLICT
*Type:* VARIABLE
The result of the calling `gpgs.snapshot_open()` or 'gpgs.snapshot_resolve_conflict()' is a conflict. You need to make decision on how to solve this conflict using 'gpgs.snapshot_resolve_conflict()'.

### SNAPSHOT_CURRENT
*Type:* VARIABLE
The second parameter for 'gpgs.snapshot_resolve_conflict()' method, which means that you want to choose the current snapshot as a snapshot for conflict solving.

### SNAPSHOT_CONFLICTING
*Type:* VARIABLE
The second parameter for 'gpgs.snapshot_resolve_conflict()' method, which means that you want to choose the conflicting snapshot as a snapshot for conflict solving.

### ERROR_STATUS_SNAPSHOT_NOT_FOUND
*Type:* VARIABLE
This constant is used in `message.error_status` table when `MSG_LOAD_SNAPSHOT` is `STATUS_FAILED`. [Official GPGS documentation](https://developers.google.com/android/reference/com/google/android/gms/games/GamesStatusCodes.html#STATUS_SNAPSHOT_NOT_FOUND) for this constant

### ERROR_STATUS_SNAPSHOT_CREATION_FAILED
*Type:* VARIABLE
This constant is used in `message.error_status` table when `MSG_LOAD_SNAPSHOT` is `STATUS_FAILED`. [Official GPGS documentation](https://developers.google.com/android/reference/com/google/android/gms/games/GamesStatusCodes.html#STATUS_SNAPSHOT_CREATION_FAILED) for this constant

### ERROR_STATUS_SNAPSHOT_CONTENTS_UNAVAILABLE
*Type:* VARIABLE
This constant is used in `message.error_status` table when `MSG_LOAD_SNAPSHOT` is `STATUS_FAILED`. [Official GPGS documentation](https://developers.google.com/android/reference/com/google/android/gms/games/GamesStatusCodes.html#STATUS_SNAPSHOT_CONTENTS_UNAVAILABLE) for this constant

### ERROR_STATUS_SNAPSHOT_COMMIT_FAILED
*Type:* VARIABLE
This constant is used in `message.error_status` table when `MSG_LOAD_SNAPSHOT` is `STATUS_FAILED`. [Official GPGS documentation](https://developers.google.com/android/reference/com/google/android/gms/games/GamesStatusCodes.html#STATUS_SNAPSHOT_COMMIT_FAILED) for this constant

### ERROR_STATUS_SNAPSHOT_FOLDER_UNAVAILABLE
*Type:* VARIABLE
This constant is used in `message.error_status` table when `MSG_LOAD_SNAPSHOT` is `STATUS_FAILED`. [Official GPGS documentation](https://developers.google.com/android/reference/com/google/android/gms/games/GamesStatusCodes.html#STATUS_SNAPSHOT_FOLDER_UNAVAILABLE) for this constant

### ERROR_STATUS_SNAPSHOT_CONFLICT_MISSING
*Type:* VARIABLE
This constant is used in `message.error_status` table when `MSG_LOAD_SNAPSHOT` is `STATUS_FAILED`. [Official GPGS documentation](https://developers.google.com/android/reference/com/google/android/gms/games/GamesStatusCodes.html#STATUS_SNAPSHOT_CONFLICT_MISSING) for this constant
