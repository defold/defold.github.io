# extension-firebase

**Namespace:** `firebase`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Firebase

## API

### firebase.initialize
*Type:* FUNCTION
Initialise Firebase

**Parameters**

- `options` (table) - Optional table with initialisation parameters to use instead of those specified in google-services.xml/plist When passing this, disable creation of the default Firebase App by specifying firebase.no_auto_init in game.project Valid keys in the table are api_key, app_id, database_url, messaging_sender_id, project_id, storage_bucket. All values are strings.

### firebase.get_installation_auth_token
*Type:* FUNCTION
Get the Firebase Installation auth token

### firebase.set_callback
*Type:* FUNCTION
Sets a callback function for receiving events from the SDK. Call `firebase.set_callback(nil)` to remove callback

**Parameters**

- `callback` (function) - Callback function that is executed on any event in the SDK.
  - `self` (object) - The calling script instance
  - `message_id` (number) - One of message types: `firebase.MSG_INITIALIZED` `firebase.MSG_INSTALLATION_AUTH_TOKEN` `firebase.MSG_INSTALLATION_ID` `firebase.MSG_ERROR`
  - `message` (table) - A table holding the data
    - `token` (number) - for MSG_INSTALLATION_AUTH_TOKEN
    - `id` (number) - for MSG_INSTALLATION_ID
    - `error` (string) - The error message (if an error occurred or `nil` otherwise)

### firebase.get_installation_id
*Type:* FUNCTION
Get the Firebase Installation id

### MSG_ERROR
*Type:* VARIABLE

### MSG_INITIALIZED
*Type:* VARIABLE

### MSG_INSTALLATION_AUTH_TOKEN
*Type:* VARIABLE

### MSG_INSTALLATION_ID
*Type:* VARIABLE
