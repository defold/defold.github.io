# extension-push

**Namespace:** `push`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with local, as well as Apple''s and Google''s push notification services. These API's only exist on mobile platforms. [icon:ios] [icon:android]

## API

### push.register
*Type:* FUNCTION
Send a request for push notifications. Note that the notifications table parameter is iOS only and will be ignored on Android.

**Parameters**

- `notifications` (table) - The types of notifications to listen to. [icon:ios]
- `callback` (function) - Register callback function.
  - `self` (object) - The current object.
  - `token` (string) - The returned push token if registration is successful.
  - `error` (table) - A table containing eventual error information.

**Examples**

Register for push notifications on iOS. Note that the token needs to be converted on this platform.
```
local function push_listener(self, payload, origin)
     -- The payload arrives here.
end

function init(self)
     local alerts = {push.NOTIFICATION_BADGE, push.NOTIFICATION_SOUND, push.NOTIFICATION_ALERT}
     push.register(alerts, function (self, token, error)
     if token then
          -- NOTE: %02x to pad byte with leading zero
          local token_string = ""
          for i = 1,#token do
              token_string = token_string .. string.format("%02x", string.byte(token, i))
          end
          print(token_string)
          push.set_listener(push_listener)
     else
          -- Push registration failed.
          print(error.error)
     end
end

```

Register for push notifications on Android.
```
local function push_listener(self, payload, origin)
     -- The payload arrives here.
end

function init(self)
     push.register({}, function (self, token, error)
         if token then
              print(token)
              push.set_listener(push_listener)
         else
              -- Push registration failed.
              print(error.error)
         end
    end)
end

```

### push.set_listener
*Type:* FUNCTION
Sets a listener function to listen to push notifications.

**Parameters**

- `listener` (function) - Listener callback function.
  - `self` (object) - The current object.
  - `payload` (table) - The push payload
  - `origin` (constant) - Origin of the push that can be one of the predefined constants below
- `push.ORIGIN_LOCAL`
- `push.ORIGIN_REMOTE`
  - `activated` (boolean) - If the application was activated via the notification.

**Examples**

Set the push notification listener.
```
local function push_listener(self, payload, origin, activated)
     -- The payload arrives here.
     pprint(payload)
     if origin == push.ORIGIN_LOCAL then
         -- This was a local push
         ...
     end

     if origin == push.ORIGIN_REMOTE then
         -- This was a remote push
         ...
     end
end

local init(self)
     ...
     -- Assuming that push.register() has been successfully called earlier
     push.set_listener(push_listener)
end

```

### push.set_badge_count
*Type:* FUNCTION
Set the badge count for application icon. This function is only available on iOS. [icon:ios]

**Parameters**

- `count` (number) - Badge count

### push.schedule
*Type:* FUNCTION
Local push notifications are scheduled with this function.
The returned `id` value is uniquely identifying the scheduled notification and can be stored for later reference.

**Parameters**

- `time` (number) - Number of seconds into the future until the notification should be triggered.
- `title` (string) - Localized title to be displayed to the user if the application is not running.
- `alert` (string) - Localized body message of the notification to be displayed to the user if the application is not running.
- `payload` (string) - JSON string to be passed to the registered listener function.
- `notification_settings` (table) - Table with notification and platform specific fields
  - `action` (string) - The alert action string to be used as the title of the right button of the alert or the value of the unlock slider, where the value replaces "unlock" in "slide to unlock" text. [icon:ios]
  - `badge_count` (number) - The numeric value of the icon badge. [icon:ios]
  - `priority` (number) - The priority is a hint to the device UI about how the notification should be displayed. There are five priority levels, from -2 to 2 where -1 is the lowest priority and 2 the highest. Unless specified, a default priority level of 2 is used. [icon:android]

**Returns**

- `number` - Unique id that can be used to cancel or inspect the notification
- `string` - Error string if something went wrong, otherwise nil

**Examples**

This example demonstrates how to schedule a local notification:
```
-- Schedule a local push in 3 seconds
local payload = '{ "data" : { "field" : "Some value", "field2" : "Other value" } }'
id, err = push.schedule(3, "Update!", "There are new stuff in the app", payload, { action = "check it out" })
if err then
     -- Something went wrong
     ...
end

```

### push.cancel
*Type:* FUNCTION
Use this function to cancel a previously scheduled local push notification.
The notification is identified by a numeric id as returned by `push.schedule()`.

**Parameters**

- `id` (number) - The numeric id of the local push notification

### push.cancel_all_issued
*Type:* FUNCTION
Use this function to cancel a previously issued local push notifications.

### push.get_scheduled
*Type:* FUNCTION
Returns a table with all data associated with a specified local push notification.
The notification is identified by a numeric id as returned by `push.schedule()`.

**Parameters**

- `id` (number) - The numeric id of the local push notification.

**Returns**

- `table` - Table with all data associated with the notification.

### push.get_all_scheduled
*Type:* FUNCTION
Returns a table with all data associated with all scheduled local push notifications.
The table contains key, value pairs where the key is the push notification id and the value is a table with the notification data, corresponding to the data given by `push.get_scheduled(id)`.

**Returns**

- `table` - Table with all data associated with all scheduled notifications.

### NOTIFICATION_BADGE
*Type:* VARIABLE
Badge notification type.

### NOTIFICATION_SOUND
*Type:* VARIABLE
Sound notification type.

### NOTIFICATION_ALERT
*Type:* VARIABLE
Alert notification type.

### ORIGIN_LOCAL
*Type:* VARIABLE
Local push origin.

### ORIGIN_REMOTE
*Type:* VARIABLE
Remote push origin.

### PRIORITY_MIN
*Type:* VARIABLE
This priority is for items might not be shown to the user except under special circumstances, such as detailed notification logs. Only available on Android. [icon:android]

### PRIORITY_LOW
*Type:* VARIABLE
Priority for items that are less important. Only available on Android. [icon:android]

### PRIORITY_DEFAULT
*Type:* VARIABLE
The default notification priority. Only available on Android. [icon:android]

### PRIORITY_HIGH
*Type:* VARIABLE
Priority for more important notifications or alerts. Only available on Android. [icon:android]

### PRIORITY_MAX
*Type:* VARIABLE
Set this priority for your application's most important items that require the user's prompt attention or input. Only available on Android. [icon:android]
