# extension-firebase-remoteconfig

**Namespace:** `firebase`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Firebase

## API

### firebase.remoteconfig.initialize
*Type:* FUNCTION
Initializes Firebase Remote Config. Generates MSG_INITIALIZED or MSG_ERROR

### firebase.remoteconfig.set_callback
*Type:* FUNCTION
Sets a callback function for receiving events from the SDK. Call `firebase.remoteconfig.set_callback(nil)` to remove callback

**Parameters**

- `callback` (function) - Callback function that is executed on any event in the SDK.
  - `self` (object) - The calling script instance
  - `message_id` (number) - One of message types: `firebase.remoteconfig.MSG_ERROR` `firebase.remoteconfig.MSG_INITIALIZED` `firebase.remoteconfig.MSG_DEFAULTS_SET` `firebase.remoteconfig.MSG_SETTINGS_UPDATED` `firebase.remoteconfig.MSG_FETCHED` `firebase.remoteconfig.MSG_ACTIVATED`
  - `message` (table) - A table holding the data
    - `error` (string) - The error message (if an error occurred or `nil` otherwise)

### firebase.remoteconfig.fetch
*Type:* FUNCTION
Fetches config data from the server. Generates MSG_FETCHED or MSG_ERROR

### firebase.remoteconfig.activate
*Type:* FUNCTION
Asynchronously activates the most recently fetched configs, so that the fetched key value pairs take effect. Generates MSG_ACTIVATED or MSG_ERROR

### firebase.remoteconfig.fetch_and_activate
*Type:* FUNCTION
Asynchronously fetches and then activates the fetched configs. Generates MSG_FETCHED and MSG_ACTIVATED or MSG_ERROR

### firebase.remoteconfig.get_boolean
*Type:* FUNCTION
Returns the value associated with a key, converted to a bool.

**Parameters**

- `key` (string) - Key of the value to be retrieved

### firebase.remoteconfig.get_data
*Type:* FUNCTION
Returns the value associated with a key, as a vector of raw byte-data.

**Parameters**

- `key` (string) - Key of the value to be retrieved

### firebase.remoteconfig.get_number
*Type:* FUNCTION
Returns the value associated with a key, converted to a double.

**Parameters**

- `key` (string) - Key of the value to be retrieved

### firebase.remoteconfig.get_string
*Type:* FUNCTION
Returns the value associated with a key, converted to a string.

**Parameters**

- `key` (string) - Key of the value to be retrieved

### firebase.remoteconfig.get_keys
*Type:* FUNCTION
Gets the set of all keys.

### firebase.remoteconfig.set_defaults
*Type:* FUNCTION
Sets the default values. Generates MSG_DEFAULTS_SET or MSG_ERROR

**Parameters**

- `defaults` (table) - Key-value pairs representing the default values

### firebase.remoteconfig.set_minimum_fetch_interval
*Type:* FUNCTION
Sets the minimum fetch interval. Generates MSG_SETTINGS_UPDATED or MSG_ERROR

**Parameters**

- `minimum_fetch_interval` (number) - The minimum interval in seconds between successive fetch calls

### firebase.remoteconfig.set_timeout
*Type:* FUNCTION
Sets the timeout that specifies how long the client should wait for a connection to the Firebase Remote Config servers. Generates MSG_SETTINGS_UPDATED or MSG_ERROR

**Parameters**

- `timeout` (number) - The timeout interval in seconds

### MSG_INITIALIZED
*Type:* VARIABLE
Event generated when remote config has been initialized and is ready for use

### MSG_ERROR
*Type:* VARIABLE
Event generated when an error occurred.

### MSG_DEFAULTS_SET
*Type:* VARIABLE
Event generated when the default values have been set

### MSG_FETCHED
*Type:* VARIABLE
Event generated when the remote config has been fetched

### MSG_ACTIVATED
*Type:* VARIABLE
Event generated when the remote config has been activated

### MSG_SETTINGS_UPDATED
*Type:* VARIABLE
Event generated when remote config settings have been updated

###
*Type:* TABLE
Functions and constants for interacting with Firebase Remote Config
