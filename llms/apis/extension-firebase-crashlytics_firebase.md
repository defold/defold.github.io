# extension-firebase-crashlytics

**Namespace:** `firebase`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Firebase

## API

### firebase.crashlytics.initialize
*Type:* FUNCTION
Initializes Crashlytics and returns true if the core Firebase extension is available and the default FirebaseApp has been initialized.

**Returns**

- `boolean` - True if Crashlytics was initialized.

### firebase.crashlytics.set_enabled
*Type:* FUNCTION
Sets whether Crashlytics collection is enabled for this app on this device.

**Parameters**

- `enabled` (boolean) - True to enable Crashlytics collection.

### firebase.crashlytics.is_enabled
*Type:* FUNCTION
Returns whether Crashlytics collection is enabled.

**Returns**

- `boolean` - True if Crashlytics collection is enabled.

### firebase.crashlytics.did_crash_on_previous_execution
*Type:* FUNCTION
Returns whether the app crashed during the previous execution.

**Returns**

- `boolean` - True if a crash was recorded during the previous execution.

### firebase.crashlytics.send_unsent_reports
*Type:* FUNCTION
Sends queued crash reports when automatic collection is disabled.

### firebase.crashlytics.delete_unsent_reports
*Type:* FUNCTION
Deletes queued crash reports when automatic collection is disabled.

### firebase.crashlytics.set_user_id
*Type:* FUNCTION
Sets the user ID associated with subsequent fatal, non-fatal, and ANR reports.

**Parameters**

- `user_id` (string) - User identifier.

### firebase.crashlytics.set_custom_key
*Type:* FUNCTION
Sets a string, number, or boolean custom key for subsequent fatal, non-fatal, and ANR reports.

**Parameters**

- `key` (string) - Custom key name.
- `value` (string | number | boolean) - String, number, or boolean value.

### firebase.crashlytics.log
*Type:* FUNCTION
Logs a message that is included in the next fatal, non-fatal, or ANR report.

**Parameters**

- `message` (string) - Log message.

### firebase.crashlytics.record_exception
*Type:* FUNCTION
Records a non-fatal exception with the supplied message.

**Parameters**

- `message` (string) - Exception message.

### firebase.crashlytics.record_lua_error
*Type:* FUNCTION
Records a Lua runtime error as a non-fatal exception with parsed Lua stack frames when a traceback is supplied.

**Parameters**

- `message` (string) - Lua error message.
- `traceback` (string | nil) - Lua traceback string, typically supplied by sys.set_error_handler. May be nil or omitted.

### firebase.crashlytics.test_java_crash
*Type:* FUNCTION
Forces a Java crash for Crashlytics setup testing. Android only.

### firebase.crashlytics.test_native_crash
*Type:* FUNCTION
Forces a native crash for Crashlytics setup testing.

###
*Type:* TABLE
Functions for interacting with Firebase Crashlytics
