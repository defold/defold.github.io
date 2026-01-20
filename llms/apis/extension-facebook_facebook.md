# extension-facebook

**Namespace:** `facebook`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with Facebook APIs

## API

### facebook.login_with_permissions
*Type:* FUNCTION
Login to Facebook and request a set of publish permissions.
The user is prompted to authorize the application using the login dialog of the specific platform. Even if the user is already logged in to Facebook this function can still be used to request additional publish permissions.
A comprehensive list of permissions can be found in the [Facebook permissions](https://developers.facebook.com/docs/facebook-login/permissions) documentation, as well as in their [guide to best practices for login management](https://developers.facebook.com/docs/facebook-login/best-practices).

**Parameters**

- `permissions` (table) - table with the requested publish permission strings.
- `audience` (number) - The audience that should be able to see the publications. Can be any of
- `facebook.AUDIENCE_NONE`
- `facebook.AUDIENCE_ONLYME`
- `facebook.AUDIENCE_FRIENDS`
- `facebook.AUDIENCE_EVERYONE`
- `callback` (function) - Callback function that is executed when the permission request dialog is closed.
  - `self` (object) - The context of the calling script
  - `data` (table) - A table that contains the response

**Examples**

Log in to Facebook with a set of publish permissions
```
local permissions = {"publish_actions"}
facebook.login_with_permissions(permissions, facebook.AUDIENCE_FRIENDS, function(self, data)
    if (data.status == facebook.STATE_OPEN and data.error == nil) then
        print("Successfully logged into Facebook")
        pprint(facebook.permissions())
    else
        print("Failed to get permissions (" .. data.status .. ")")
        pprint(data)
    end
end)

```

Log in to Facebook with a set of read permissions
```
local permissions = {"public_profile", "email", "user_friends"}
facebook.login_with_read_permissions(permissions, facebook.AUDIENCE_EVERYONE, function(self, data)
    if (data.status == facebook.STATE_OPEN and data.error == nil) then
        print("Successfully logged into Facebook")
        pprint(facebook.permissions())
    else
        print("Failed to get permissions (" .. data.status .. ")")
        pprint(data)
    end
end)

```

### facebook.login_with_tracking_preference
*Type:* FUNCTION
iOS ONLY. Login to Facebook and request a set of permissions. Allows developers to signal that a login is limited in terms of tracking users.
The user is prompted to authorize the application using the login dialog of the specific platform. Even if the user is already logged in to Facebook this function can still be used to request additional publish permissions.
A comprehensive list of permissions can be found in the [Facebook permissions](https://developers.facebook.com/docs/facebook-login/permissions) documentation, as well as in their [guide to best practices for login management](https://developers.facebook.com/docs/facebook-login/best-practices). For Limited Login the list of permissions can be found in the [Permissions in Limited Login](https://developers.facebook.com/docs/facebook-login/limited-login/permissions) documentation.

**Parameters**

- `login_tracking` (number) - The tracking type for the login. Can be any of
- `facebook.LOGIN_TRACKING_LIMITED`
- `facebook.LOGIN_TRACKING_ENABLED`
- `permissions` (table) - table with the requested publish permission strings.
- `crypto_nonce` (string) - Nonce that the configuration was created with. A unique nonce will be used if none is provided to the factory method.
- `callback` (function) - Callback function that is executed when the permission request dialog is closed.
  - `self` (object) - The context of the calling script
  - `data` (table) - A table that contains the response

**Examples**

Log in to Facebook with a set of publish permissions
```
local permissions = {"publish_actions"}
facebook.login_with_permissions(permissions, facebook.AUDIENCE_FRIENDS, function(self, data)
    if (data.status == facebook.STATE_OPEN and data.error == nil) then
        print("Successfully logged into Facebook")
        pprint(facebook.permissions())
    else
        print("Failed to get permissions (" .. data.status .. ")")
        pprint(data)
    end
end)

```

Log in to Facebook with a set of read permissions
```
local permissions = {"public_profile", "email", "user_friends"}
facebook.login_with_tracking_preference(facebook.LOGIN_TRACKING_LIMITED, permissions, "customcryptononce", function(self, data)
    if (data.status == facebook.STATE_OPEN and data.error == nil) then
        print("Successfully logged into Facebook")
        pprint(facebook.permissions())
    else
        print("Failed to get permissions (" .. data.status .. ")")
        pprint(data)
    end
end)

```

### facebook.logout
*Type:* FUNCTION
Logout from Facebook

### facebook.set_default_audience
*Type:* FUNCTION
iOS ONLY. The audience that should be able to see the publications. Should be called before `facebook.login_with_tracking_preference()`; Can be any of
- `facebook.AUDIENCE_NONE`
- `facebook.AUDIENCE_ONLYME`
- `facebook.AUDIENCE_FRIENDS`
- `facebook.AUDIENCE_EVERYONE`

### facebook.get_current_authentication_token
*Type:* FUNCTION
iOS ONLY. Get the current AuthenticationToken.
This function returns the currently stored authentication token after a previous successful login. If it returns nil no access token exists and you need to perform a login to get the wanted permissions.

**Returns**

- `string` - the authentication token or nil if the user is not logged in

### facebook.get_current_profile
*Type:* FUNCTION
iOS ONLY. Get the users [FBSDKProfile.currentProfile](https://developers.facebook.com/docs/facebook-login/limited-login/ios/). [Reading From Profile Helper Class](https://developers.facebook.com/docs/facebook-login/limited-login/permissions/profile-helper)

**Returns**

- `table` - After your application receives the logged-in user’s authentication token, you can use this function to read information that user has granted to your application.

### facebook.init
*Type:* FUNCTION
Initialize Facebook SDK (if facebook.autoinit is 0 in game.project)

### facebook.access_token
*Type:* FUNCTION
Get the current Facebook access token.
This function returns the currently stored access token after a previous successful login. If it returns nil no access token exists and you need to perform a login to get the wanted permissions.

**Returns**

- `string` - the access token or nil if the user is not logged in

**Examples**

Get the current access token, then use it to perform a graph API request.
```
local function get_name_callback(self, id, response)
    -- do something with the response
end
function init(self)
    -- assuming we are already logged in.
    local token = facebook.access_token()
    if token then
        local url = "https://graph.facebook.com/me/?access_token=".. token
        http.request(url, "GET", get_name_callback)
    end
end

```

### facebook.permissions
*Type:* FUNCTION
Get the currently granted permissions.
This function returns a table with all the currently granted permission strings.

**Returns**

- `table` - The permissions

**Examples**

Check the currently granted permissions for a particular permission
```
for _,permission in ipairs(facebook.permissions()) do
    if permission == "user_likes" then
        -- "user_likes" granted...
        break
    end
end

```

### facebook.post_event
*Type:* FUNCTION
Post an event to Facebook Analytics
This function will post an event to Facebook Analytics where it can be used in the Facebook Insights system.

**Parameters**

- `event` (number | string) - An event can either be one of the predefined constants below or a text string which can be used to define a custom event that is registered with Facebook Analytics.
- `facebook.EVENT_ACHIEVED_LEVEL` - `facebook.EVENT_ADDED_PAYMENT_INFO` - `facebook.EVENT_ADDED_TO_CART` - `facebook.EVENT_ADDED_TO_WISHLIST` - `facebook.EVENT_COMPLETED_REGISTRATION` - `facebook.EVENT_COMPLETED_TUTORIAL` - `facebook.EVENT_INITIATED_CHECKOUT` - `facebook.EVENT_PURCHASED` - `facebook.EVENT_RATED` - `facebook.EVENT_SEARCHED` - `facebook.EVENT_SPENT_CREDITS` - `facebook.EVENT_TIME_BETWEEN_SESSIONS` - `facebook.EVENT_UNLOCKED_ACHIEVEMENT` - `facebook.EVENT_VIEWED_CONTENT`
- `value` (number) - A numeric value for the event. This should represent the value of the event, such as the level achieved, price for an item or number of orcs killed.
- `params` (table) - Optional table with parameters and their values. A key in the table can either be one of the predefined constants below or a text which can be used to define a custom parameter.
- `facebook.PARAM_CONTENT_ID` - `facebook.PARAM_CONTENT_TYPE` - `facebook.PARAM_CURRENCY` - `facebook.PARAM_DESCRIPTION` - `facebook.PARAM_LEVEL` - `facebook.PARAM_MAX_RATING_VALUE` - `facebook.PARAM_NUM_ITEMS` - `facebook.PARAM_PAYMENT_INFO_AVAILABLE` - `facebook.PARAM_REGISTRATION_METHOD` - `facebook.PARAM_SEARCH_STRING` - `facebook.PARAM_SOURCE_APPLICATION` - `facebook.PARAM_SUCCESS`

**Examples**

Post a spent credits event to Facebook Analytics
```
params = {[facebook.PARAM_LEVEL] = 30, [facebook.PARAM_NUM_ITEMS] = 2}
facebook.post_event(facebook.EVENT_SPENT_CREDITS, 25, params)

```

### facebook.enable_event_usage
*Type:* FUNCTION
Enable event usage with Facebook Analytics This function will enable event usage for Facebook Analytics which means that Facebook will be able to use event data for ad-tracking.
[icon:attention] Event usage cannot be controlled and is always enabled for the Facebook Canvas platform, therefore this function has no effect on Facebook Canvas.

### facebook.disable_event_usage
*Type:* FUNCTION
Disable event usage with Facebook Analytics This function will disable event usage for Facebook Analytics which means that Facebook won't be able to use event data for ad-tracking. Events will still be sent to Facebook for insights.
[icon:attention] Event usage cannot be controlled and is always enabled for the Facebook Canvas platform, therefore this function has no effect on Facebook Canvas.

### facebook.enable_advertiser_tracking
*Type:* FUNCTION
Enable advertiser tracking This function will set AdvertiserTrackingEnabled (the 'ATE' flag) to true on iOS, to inform Audience Network to use the data to deliver personalized ads for users on iOS 14 and above.

### facebook.disable_advertiser_tracking
*Type:* FUNCTION
Disable advertiser tracking This function will set AdvertiserTrackingEnabled (the 'ATE' flag) to false on iOS, to inform Audience Network not to use the data to deliver personalized ads for users on iOS 14 and above.

### facebook.show_dialog
*Type:* FUNCTION
Show facebook web dialog
Display a Facebook web dialog of the type specified in the `dialog` parameter.

The `param` table should be set up according to the requirements of each dialog type. Note that some parameters are mandatory. Below is the list of available dialogs and where to find Facebook's developer documentation on parameters and response data.

`"apprequests"`
Shows a Game Request dialog. Game Requests allows players to invite their friends to play a game. Available parameters
- [type:string] `title`
- [type:string] `message`
- [type:number] `action_type`
- [type:number] `filters`
- [type:string] `data`
- [type:string] `object_id`
- [type:table] `suggestions`
- [type:table] `recipients`
- [type:string] `to`

On success, the "result" table parameter passed to the callback function will include the following fields
- [type:string] `request_id`
- [type:table] `to`

[Details for each parameter](https://developers.facebook.com/docs/games/services/gamerequests/v2.6#dialogparameters)

`"feed"`
The Feed Dialog allows people to publish individual stories to their timeline.

- [type:string] `caption`
- [type:string] `description`
- [type:string] `picture`
- [type:string] `link`
- [type:table] `people_ids`
- [type:string] `place_id`
- [type:string] `ref`

On success, the "result" table parameter passed to the callback function will include the following fields
- [type:string] `post_id`

[Details for each parameter](https://developers.facebook.com/docs/sharing/reference/feed-dialog/v2.6#params)

`"appinvite"`
The App Invite dialog is available only on iOS and Android. Note that the `url` parameter corresponds to the appLinkURL (iOS) and setAppLinkUrl (Android) properties.
- [type:string] `url`
- [type:string] `preview_image`
[Details for each parameter](https://developers.facebook.com/docs/reference/ios/current/class/FBSDKAppInviteContent)

**Parameters**

- `dialog` (string) - Dialog to show
- `"apprequests"`
- `"feed"`
- `"appinvite"`
- `param` (table) - table with dialog parameters
- `callback` (function) - Callback function that is called when the dialog is closed.
  - `self` (object) - The context of the calling script
  - `result` (table) - table with dialog specific results. See above.
  - `error` (table) - Error message. If there is no error, `error` is `nil`.

**Examples**

Show a dialog allowing the user to share a post to their timeline
```
local function fb_share(self, result, error)
    if error then
        -- something did not go right...
    else
        -- do something sensible
    end
end
function init(self)
    -- assuming we have logged in with publish permissions
    local param = { link = "http://www.mygame.com",picture="http://www.mygame.com/image.jpg" }
    facebook.show_dialog("feed", param, fb_share)
end

```

### facebook.get_version
*Type:* FUNCTION
Get the version of the Facebook SDK used by the extension.

**Returns**

- `string` - The Facebook SDK version

### facebook.deferred_deep_link
*Type:* FUNCTION
Allows receiving deferred deep link URL and parameters.
[More info about Referred Deep Links](https://developers.facebook.com/docs/app-ads/deep-linking/)

**Parameters**

- `callback` (function) - Callback function that is called when information is ready.
  - `self` (object) - The context of the calling script
  - `result` (table) - table with a deferred deep link information
    - `ref` (string) - ref for this App Link.
    - `extras` (table) - the full set of arguments for this app link. Properties like target uri & ref are typically picked out of this set of arguments.
    - `target_url` (string) - target uri for this App Link.
  - `error` (table) - Error message. If there is no error, `error` is `nil`.

**Examples**

Show a dialog allowing the user to share a post to their timeline
```
local function deferred_deep_link_callback(self, result, error)
  if error then
    print(error.error)
  else
    pprint(result)
  end
end

function init(self)
  facebook.deferred_deep_link(deferred_deep_link_callback)
end

```

### STATE_OPEN
*Type:* VARIABLE
The Facebook login session is open

### STATE_CLOSED_LOGIN_FAILED
*Type:* VARIABLE
The Facebook login session has closed because login failed

### GAMEREQUEST_ACTIONTYPE_NONE
*Type:* VARIABLE
Game request action type "none" for "apprequests" dialog

### GAMEREQUEST_ACTIONTYPE_SEND
*Type:* VARIABLE
Game request action type "send" for "apprequests" dialog

### GAMEREQUEST_ACTIONTYPE_ASKFOR
*Type:* VARIABLE
Game request action type "askfor" for "apprequests" dialog

### GAMEREQUEST_ACTIONTYPE_TURN
*Type:* VARIABLE
Game request action type "turn" for "apprequests" dialog

### GAMEREQUEST_FILTER_NONE
*Type:* VARIABLE
Game request filter type "none" for "apprequests" dialog

### GAMEREQUEST_FILTER_APPUSERS
*Type:* VARIABLE
Game request filter type "app_users" for "apprequests" dialog

### GAMEREQUEST_FILTER_APPNONUSERS
*Type:* VARIABLE
Game request filter type "app_non_users" for "apprequests" dialog

### EVENT_ACHIEVED_LEVEL
*Type:* VARIABLE
Log this event when the user has achieved a level

### EVENT_ADDED_PAYMENT_INFO
*Type:* VARIABLE
Log this event when the user has entered their payment info

### EVENT_ADDED_TO_CART
*Type:* VARIABLE
Log this event when the user has added an item to their cart The value_to_sum passed to facebook.post_event should be the item's price.

### EVENT_ADDED_TO_WISHLIST
*Type:* VARIABLE
Log this event when the user has added an item to their wish list The value_to_sum passed to facebook.post_event should be the item's price.

### EVENT_COMPLETED_REGISTRATION
*Type:* VARIABLE
Log this event when a user has completed registration with the app

### EVENT_COMPLETED_TUTORIAL
*Type:* VARIABLE
Log this event when the user has completed a tutorial in the app

### EVENT_INITIATED_CHECKOUT
*Type:* VARIABLE
Log this event when the user has entered the checkout process The value_to_sum passed to facebook.post_event should be the total price in the cart.

### EVENT_PURCHASED
*Type:* VARIABLE
Log this event when the user has completed a purchase. The value_to_sum passed to facebook.post_event should be the numeric rating.

### EVENT_RATED
*Type:* VARIABLE
Log this event when the user has rated an item in the app

### EVENT_SEARCHED
*Type:* VARIABLE
Log this event when a user has performed a search within the app

### EVENT_SPENT_CREDITS
*Type:* VARIABLE
Log this event when the user has spent app credits The value_to_sum passed to facebook.post_event should be the number of credits spent.

### EVENT_TIME_BETWEEN_SESSIONS
*Type:* VARIABLE
Log this event when measuring the time between user sessions

### EVENT_UNLOCKED_ACHIEVEMENT
*Type:* VARIABLE
Log this event when the user has unlocked an achievement in the app

### EVENT_VIEWED_CONTENT
*Type:* VARIABLE
Log this event when a user has viewed a form of content in the app

### PARAM_CONTENT_ID
*Type:* VARIABLE
Parameter key used to specify an ID for the content being logged about
The parameter key could be an EAN, article identifier, etc., depending on the nature of the app.

### PARAM_CONTENT_TYPE
*Type:* VARIABLE
Parameter key used to specify a generic content type/family for the logged event
The key is an arbitrary type/family (e.g. "music", "photo", "video") depending on the nature of the app.

### PARAM_CURRENCY
*Type:* VARIABLE
Parameter key used to specify currency used with logged event
Use a currency value key, e.g. "USD", "EUR", "GBP" etc. See See ISO-4217 for specific values.

### PARAM_DESCRIPTION
*Type:* VARIABLE
Parameter key used to specify a description appropriate to the event being logged
Use this for app specific event description, for instance the name of the achievement unlocked in the facebook.EVENT_UNLOCKED_ACHIEVEMENT event.

### PARAM_LEVEL
*Type:* VARIABLE
Parameter key used to specify the level achieved

### PARAM_MAX_RATING_VALUE
*Type:* VARIABLE
Parameter key used to specify the maximum rating available
Set to specify the max rating available for the facebook.EVENT_RATED event. E.g., "5" or "10".

### PARAM_NUM_ITEMS
*Type:* VARIABLE
Parameter key used to specify how many items are being processed
Set to specify the number of items being processed for an facebook.EVENT_INITIATED_CHECKOUT or facebook.EVENT_PURCHASED event.

### PARAM_PAYMENT_INFO_AVAILABLE
*Type:* VARIABLE
Parameter key used to specify whether payment info is available
Set to specify if payment info is available for the facebook.EVENT_INITIATED_CHECKOUT event.

### PARAM_REGISTRATION_METHOD
*Type:* VARIABLE
Parameter key used to specify method user has used to register for the app
Set to specify what registation method a user used for the app, e.g. "Facebook", "email", "Twitter", etc.

### PARAM_SEARCH_STRING
*Type:* VARIABLE
Parameter key used to specify user search string
Set this to the the string that the user provided for a search operation.

### PARAM_SOURCE_APPLICATION
*Type:* VARIABLE
Parameter key used to specify source application package

### PARAM_SUCCESS
*Type:* VARIABLE
Parameter key used to specify activity success
Set this key to indicate whether the activity being logged about was successful or not.

### AUDIENCE_NONE
*Type:* VARIABLE
Publish permission to reach no audience

### AUDIENCE_ONLYME
*Type:* VARIABLE
Publish permission to reach only me (private to current user)

### AUDIENCE_FRIENDS
*Type:* VARIABLE
Publish permission to reach user friends

### AUDIENCE_EVERYONE
*Type:* VARIABLE
Publish permission to reach everyone

### LOGIN_TRACKING_LIMITED
*Type:* VARIABLE
Login tracking Limited

### LOGIN_TRACKING_ENABLED
*Type:* VARIABLE
Login tracking enabled
