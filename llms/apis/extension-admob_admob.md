# extension-admob

**Namespace:** `admob`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with [Google AdMob APIs](https://developers.google.com/admob)

## API

### admob.initialize
*Type:* FUNCTION
Initialize the Mobile Ads SDK. Warning: If you need to obtain consent from users in the European Economic Area (EEA), set any request-specific flags, or otherwise take action before loading ads, ensure you do so before initializing the Mobile Ads SDK.
Original docs [Android](https://developers.google.com/admob/android/quick-start#initialize_the_mobile_ads_sdk), [iOS](https://developers.google.com/admob/ios/quick-start#initialize_the_mobile_ads_sdk)

### admob.set_callback
*Type:* FUNCTION
Sets a callback function for receiving events from the SDK. Call `admob.set_callback(nil)` to remove callback

**Parameters**

- `callback` (function) - Callback function that is executed on any event in the SDK.
  - `self` (object) - The calling script instance
  - `message_id` (number) - One of message types: `admob.MSG_INITIALIZATION` initialization, `admob.MSG_INTERSTITIAL` message from Interstitial ad unit, `admob.MSG_REWARDED` message from Rewarded ad unit, `admob.MSG_BANNER` message from Banner ad unit
  - `message` (table) - A table holding the data
    - `event` (number) - One of event types: `admob.EVENT_CLOSED`, `admob.EVENT_FAILED_TO_SHOW`, `admob.EVENT_OPENING`, `admob.EVENT_FAILED_TO_LOAD`, `admob.EVENT_LOADED`, `admob.EVENT_NOT_LOADED`, `admob.EVENT_EARNED_REWARD`, `admob.EVENT_COMPLETE`, `admob.EVENT_CLICKED`, `admob.EVENT_DESTROYED`, `admob.EVENT_IMPRESSION_RECORDED`, `admob.EVENT_JSON_ERROR`
    - `code` (number) - The error code (if an error occurred or `nil` otherwise)
    - `message` (string) - The error message (if an error occurred or `nil` otherwise)

**Examples**

```
local function admob_callback(self, message_id, message)
    pprint(message_id, message)
    if message_id == admob.MSG_INITIALIZATION then
       if message.event == admob.EVENT_COMPLETE then
           print("EVENT_COMPLETE: Initialization complete")
       elseif message.event == admob.EVENT_JSON_ERROR then
           print("EVENT_JSON_ERROR: Internal NE json error "..message.error)
       end
   elseif message_id == admob.MSG_IDFA then
       if message.event == admob.EVENT_STATUS_AUTHORIZED then
           print("EVENT_STATUS_AUTHORIZED: ATTrackingManagerAuthorizationStatusAuthorized")
       elseif message.event == admob.EVENT_STATUS_DENIED then
           print("EVENT_STATUS_DENIED: ATTrackingManagerAuthorizationStatusDenied")
       elseif message.event == admob.EVENT_STATUS_NOT_DETERMINED then
           print("EVENT_STATUS_NOT_DETERMINED: ATTrackingManagerAuthorizationStatusNotDetermined")
       elseif message.event == admob.EVENT_STATUS_RESTRICTED then
           print("EVENT_STATUS_RESTRICTED: ATTrackingManagerAuthorizationStatusRestricted")
       elseif message.event == admob.EVENT_NOT_SUPPORTED then
           print("EVENT_NOT_SUPPORTED: IDFA request not supported on this platform or OS version")
       end
   elseif message_id == admob.MSG_INTERSTITIAL then
       if message.event == admob.EVENT_CLOSED then
           print("EVENT_CLOSED: Interstitial AD closed")
       elseif message.event == admob.EVENT_FAILED_TO_SHOW then
           print("EVENT_FAILED_TO_SHOW: Interstitial AD failed to show\nCode: "..message.code.."\nError: "..message.error)
       elseif message.event == admob.EVENT_OPENING then
           print("EVENT_OPENING: Interstitial AD is opening")
       elseif message.event == admob.EVENT_FAILED_TO_LOAD then
           print("EVENT_FAILED_TO_LOAD: Interstitial AD failed to load\nCode: "..message.code.."\nError: "..message.error)
       elseif message.event == admob.EVENT_LOADED then
           print("EVENT_LOADED: Interstitial AD loaded")
       elseif message.event == admob.EVENT_NOT_LOADED then
           print("EVENT_NOT_LOADED: can't call show_interstitial() before EVENT_LOADED\nError: "..message.error)
       elseif message.event == admob.EVENT_IMPRESSION_RECORDED then
           print("EVENT_IMPRESSION_RECORDED: Interstitial did record impression")
       elseif message.event == admob.EVENT_JSON_ERROR then
           print("EVENT_JSON_ERROR: Internal NE json error: "..message.error)
       end
   elseif message_id == admob.MSG_REWARDED then
       if message.event == admob.EVENT_CLOSED then
           print("EVENT_CLOSED: Rewarded AD closed")
       elseif message.event == admob.EVENT_FAILED_TO_SHOW then
           print("EVENT_FAILED_TO_SHOW: Rewarded AD failed to show\nCode: "..message.code.."\nError: "..message.error)
       elseif message.event == admob.EVENT_OPENING then
           print("EVENT_OPENING: Rewarded AD is opening")
       elseif message.event == admob.EVENT_FAILED_TO_LOAD then
           print("EVENT_FAILED_TO_LOAD: Rewarded AD failed to load\nCode: "..message.code.."\nError: "..message.error)
       elseif message.event == admob.EVENT_LOADED then
           print("EVENT_LOADED: Rewarded AD loaded")
       elseif message.event == admob.EVENT_NOT_LOADED then
           print("EVENT_NOT_LOADED: can't call show_rewarded() before EVENT_LOADED\nError: "..message.error)
       elseif message.event == admob.EVENT_EARNED_REWARD then
           print("EVENT_EARNED_REWARD: Reward: " .. tostring(message.amount) .. " " .. tostring(message.type))
       elseif message.event == admob.EVENT_IMPRESSION_RECORDED then
           print("EVENT_IMPRESSION_RECORDED: Rewarded did record impression")
       elseif message.event == admob.EVENT_JSON_ERROR then
           print("EVENT_JSON_ERROR: Internal NE json error: "..message.error)
       end
   elseif message_id == admob.MSG_BANNER then
       if message.event == admob.EVENT_LOADED then
           print("EVENT_LOADED: Banner AD loaded. Height: "..message.height.."px Width: "..message.width.."px")
       elseif message.event == admob.EVENT_OPENING then
           print("EVENT_OPENING: Banner AD is opening")
       elseif message.event == admob.EVENT_FAILED_TO_LOAD then
           print("EVENT_FAILED_TO_LOAD: Banner AD failed to load\nCode: "..message.code.."\nError: "..message.error)
       elseif message.event == admob.EVENT_CLICKED then
           print("EVENT_CLICKED: Banner AD loaded")
       elseif message.event == admob.EVENT_CLOSED then
           print("EVENT_CLOSED: Banner AD closed")
       elseif message.event == admob.EVENT_DESTROYED then
           print("EVENT_DESTROYED: Banner AD destroyed")
       elseif message.event == admob.EVENT_IMPRESSION_RECORDED then
           print("EVENT_IMPRESSION_RECORDED: Banner did record impression")
       elseif message.event == admob.EVENT_JSON_ERROR then
           print("EVENT_JSON_ERROR: Internal NE json error: "..message.error)
       end
   end
end

function init(self)
    if admob then
        admob.set_callback(admob_callback)
        admob.initialize()
    end
end

```

### admob.set_privacy_settings
*Type:* FUNCTION
Sets user privacy preferences (must be called before `admob.initialize()`). Original docs [Android](https://developers.google.com/admob/android/ccpa), [iOS](https://developers.google.com/admob/ios/ccpa)

**Parameters**

- `bool` (boolean)

### admob.request_idfa
*Type:* FUNCTION
Display the App Tracking Transparency authorization request for accessing the IDFA. Original docs [iOS](https://developers.google.com/admob/ios/ios14#request)

### admob.show_ad_inspector
*Type:* FUNCTION
Show Ad Inspector. This is an in-app overlay that enables authorized devices to perform realtime analysis of test ad requests directly within a mobile app. Ad Inspector only launces on [test devices](https://support.google.com/admob/answer/9691433). Original docs [Android](https://developers.google.com/admob/android/ad-inspector), [iOS](https://developers.google.com/admob/ios/ad-inspector)

### admob.load_appopen
*Type:* FUNCTION
Starts loading an AppOpen Ad, can only be called after `admob.MSG_INITIALIZATION` event Original docs [Android](https://developers.google.com/admob/android/app-open), [iOS](https://developers.google.com/admob/ios/app-open)

**Parameters**

- `ad_unit_id` (string) - Ad unit ID, for test ads use on Android `"ca-app-pub-3940256099942544/9257395921"`, or on iOS `"ca-app-pub-3940256099942544/5575463023"` Original docs [Android](https://developers.google.com/admob/android/app-open), [iOS](https://developers.google.com/admob/ios/app-open)

### admob.show_appopen
*Type:* FUNCTION
Shows loaded AppOpen Ad, can only be called after `admob.EVENT_LOADED` Original docs [Android](https://developers.google.com/admob/android/app-open), [iOS](https://developers.google.com/admob/ios/app-open)

**Examples**

```
if admob and admob.is_appopen_loaded() then
    admob.show_appopen()
end

```

### admob.is_appopen_loaded
*Type:* FUNCTION
Checks if AppOpen Ad is loaded and ready to show Original docs [Android](https://developers.google.com/admob/android/app-open), [iOS](https://developers.google.com/admob/ios/app-open)

**Returns**

- `boolean`

### admob.load_interstitial
*Type:* FUNCTION
Starts loading an Interstitial Ad, can only be called after `admob.MSG_INITIALIZATION` event Original docs [Android](https://developers.google.com/admob/android/interstitial-fullscreen), [iOS](https://developers.google.com/admob/ios/interstitial)

**Parameters**

- `ad_unit_id` (string) - Ad unit ID, for test ads use on Android `"ca-app-pub-3940256099942544/1033173712"`, or on iOS `"ca-app-pub-3940256099942544/4411468910"` Original docs [Android](https://developers.google.com/admob/android/interstitial-fullscreen), [iOS](https://developers.google.com/admob/ios/interstitial)

### admob.show_interstitial
*Type:* FUNCTION
Shows loaded Interstitial Ad, can only be called after `admob.EVENT_LOADED` Original docs [Android](https://developers.google.com/admob/android/interstitial-fullscreen), [iOS](https://developers.google.com/admob/ios/interstitial)

**Examples**

```
if admob and admob.is_interstitial_loaded() then
    admob.show_interstitial()
end

```

### admob.is_interstitial_loaded
*Type:* FUNCTION
Checks if Interstitial Ad is loaded and ready to show Original docs [Android](https://developers.google.com/admob/android/interstitial-fullscreen), [iOS](https://developers.google.com/admob/ios/interstitial)

**Returns**

- `boolean`

### admob.load_rewarded
*Type:* FUNCTION
Starts loading a Rewarded Ad, can only be called after `admob.MSG_INITIALIZATION` event Original docs [Android](https://developers.google.com/admob/android/rewarded-fullscreen), [iOS](https://developers.google.com/admob/ios/rewarded-ads)

**Parameters**

- `ad_unit_id` (string) - Ad unit ID, for test ads use on Android `"ca-app-pub-3940256099942544/1712485313"`, or on iOS `"ca-app-pub-3940256099942544/4411468910"` Original docs [Android](https://developers.google.com/admob/android/rewarded-fullscreen), [iOS](https://developers.google.com/admob/ios/rewarded-ads)
- `options` (table) - ServerSideVerificationOptions [Android](https://developers.google.com/admob/android/rewarded#validate-ssv), [iOS](https://developers.google.com/admob/ios/rewarded#validate-ssv)
  - `user_id` (string) - A unique identifier assigned to each user.
  - `custom_data` (string) - Custom Data attached to server-side reward callbacks.

### admob.show_rewarded
*Type:* FUNCTION
Shows loaded Rewarded Ad, can only be called after `admob.EVENT_LOADED` Original docs [Android](https://developers.google.com/admob/android/rewarded-fullscreen), [iOS](https://developers.google.com/admob/ios/rewarded-ads)

**Examples**

```
if admob and admob.is_rewarded_loaded() then
    admob.show_rewarded()
end

```

### admob.is_rewarded_loaded
*Type:* FUNCTION
Checks if Rewarded Ad is loaded and ready to show Original docs [Android](https://developers.google.com/admob/android/rewarded-fullscreen), [iOS](https://developers.google.com/admob/ios/rewarded-ads)

**Returns**

- `boolean`

### admob.load_rewarded_interstitial
*Type:* FUNCTION
Starts loading a Rewarded Interstitial Ad, can only be called after `admob.MSG_INITIALIZATION` event Original docs [Android](https://developers.google.com/admob/android/rewarded-interstitial#load_an_ad), [iOS](https://developers.google.com/admob/ios/rewarded-interstitial#load_an_ad)

**Parameters**

- `ad_unit_id` (string) - Ad unit ID, for test ads use on Android `"ca-app-pub-3940256099942544/5354046379"`, or on iOS `"ca-app-pub-3940256099942544/6978759866"` Original docs [Android](https://developers.google.com/admob/android/rewarded-interstitial#load_an_ad), [iOS](https://developers.google.com/admob/ios/rewarded-interstitial#load_an_ad)

### admob.show_rewarded_interstitial
*Type:* FUNCTION
Shows loaded Rewarded Interstitial Ad, can only be called after `admob.EVENT_LOADED` Original docs [Android](https://developers.google.com/admob/android/rewarded-interstitial#show_the_ad), [iOS](https://developers.google.com/admob/ios/rewarded-interstitial#display_the_ad_and_handle_the_reward_event)

**Examples**

```
if admob and admob.is_rewarded_interstitial_loaded() then
    admob.show_rewarded_interstitial()
end

```

### admob.is_rewarded_interstitial_loaded
*Type:* FUNCTION
Checks if Rewarded Interstitial Ad is loaded and ready to show Original docs [Android](https://developers.google.com/admob/android/rewarded-interstitial), [iOS](https://developers.google.com/admob/ios/rewarded-interstitial)

**Returns**

- `boolean`

### admob.load_banner
*Type:* FUNCTION
Starts loading a Banner Ad, can only be called after `admob.MSG_INITIALIZATION` event Original docs [Android](https://developers.google.com/admob/android/banner), [iOS](https://developers.google.com/admob/ios/banner)

**Parameters**

- `ad_unit_id` (string) - Ad unit ID, for test ads use on Android `"ca-app-pub-3940256099942544/6300978111"`, or on iOS `"ca-app-pub-3940256099942544/2934735716"` Original docs [Android](https://developers.google.com/admob/android/banner), [iOS](https://developers.google.com/admob/ios/banner)
- `size` (number) - Requested Banner Ad size, possible values: `admob.SIZE_ADAPTIVE_BANNER` (default), `admob.SIZE_BANNER`, `admob.SIZE_FLUID`, `admob.SIZE_FULL_BANNER`, `admob.SIZE_LARGE_BANNER`, `admob.SIZE_LEADEARBOARD`, `admob.SIZE_MEDIUM_RECTANGLE`, `admob.SIZE_SMART_BANNER`, `admob.SIZE_LARGE_ADAPTIVE_BANNER` Original docs [Android](https://developers.google.com/admob/android/banner#banner_sizes), [iOS](https://developers.google.com/admob/ios/banner#banner_sizes)

### admob.show_banner
*Type:* FUNCTION
Shows loaded Banner Ad, can only be called after `admob.EVENT_LOADED` Original docs [Android](https://developers.google.com/admob/android/banner), [iOS](https://developers.google.com/admob/ios/banner)

**Parameters**

- `position` (number) - Banner Ad position, possible values: `admob.POS_NONE` (default), `admob.POS_TOP_LEFT`, `admob.POS_TOP_CENTER`, `admob.POS_TOP_RIGHT`, `admob.POS_BOTTOM_LEFT`, `admob.POS_BOTTOM_CENTER`, `admob.POS_BOTTOM_RIGHT`, `admob.POS_CENTER`

**Examples**

```
if admob and admob.is_banner_loaded() then
    admob.show_banner(admob.POS_TOP_CENTER)
end

```

### admob.set_max_ad_content_rating
*Type:* FUNCTION
Sets a maximum ad content rating. AdMob ads returned for your app will have a content rating at or below that level. Original docs [Android](https://developers.google.com/admob/android/targeting#ad_content_filtering), [iOS](https://developers.google.com/admob/ios/targeting#ad_content_filtering)

**Parameters**

- `max_ad_rating` (number) - Max Ad Rating, possible values: `admob.MAX_AD_CONTENT_RATING_G`, `admob.MAX_AD_CONTENT_RATING_PG`, `admob.MAX_AD_CONTENT_RATING_T`, `admob.MAX_AD_CONTENT_RATING_MA`

**Examples**

```
  admob.set_max_ad_content_rating(admob.MAX_AD_CONTENT_RATING_PG)

```

### admob.hide_banner
*Type:* FUNCTION
Temporarily hides Banner Ad, banner can be shown again using `admob.show_banner()` Original docs [Android](https://developers.google.com/admob/android/banner), [iOS](https://developers.google.com/admob/ios/banner)

### admob.is_banner_loaded
*Type:* FUNCTION
Checks if Banner Ad is loaded and ready to show Original docs [Android](https://developers.google.com/admob/android/banner), [iOS](https://developers.google.com/admob/ios/banner)

**Returns**

- `boolean`

### admob.destroy_banner
*Type:* FUNCTION
Hides and unloads Banner Ad (needs to call `admob.load_banner()` later to show Banner Ad) Original docs [Android](https://developers.google.com/admob/android/banner), [iOS](https://developers.google.com/admob/ios/banner)

### MSG_INITIALIZATION
*Type:* VARIABLE

### MSG_INTERSTITIAL
*Type:* VARIABLE

### MSG_REWARDED
*Type:* VARIABLE

### MSG_BANNER
*Type:* VARIABLE

### MSG_IDFA
*Type:* VARIABLE

### MSG_REWARDED_INTERSTITIAL
*Type:* VARIABLE

### MSG_APPOPEN
*Type:* VARIABLE

### EVENT_CLOSED
*Type:* VARIABLE

### EVENT_FAILED_TO_SHOW
*Type:* VARIABLE

### EVENT_OPENING
*Type:* VARIABLE

### EVENT_FAILED_TO_LOAD
*Type:* VARIABLE

### EVENT_LOADED
*Type:* VARIABLE

### EVENT_NOT_LOADED
*Type:* VARIABLE

### EVENT_EARNED_REWARD
*Type:* VARIABLE

### EVENT_COMPLETE
*Type:* VARIABLE

### EVENT_CLICKED
*Type:* VARIABLE

### EVENT_DESTROYED
*Type:* VARIABLE

### EVENT_JSON_ERROR
*Type:* VARIABLE

### EVENT_IMPRESSION_RECORDED
*Type:* VARIABLE

### EVENT_STATUS_AUTHORIZED
*Type:* VARIABLE

### EVENT_STATUS_DENIED
*Type:* VARIABLE

### EVENT_STATUS_NOT_DETERMINED
*Type:* VARIABLE

### EVENT_STATUS_RESTRICTED
*Type:* VARIABLE

### EVENT_NOT_SUPPORTED
*Type:* VARIABLE

### SIZE_ADAPTIVE_BANNER
*Type:* VARIABLE

### SIZE_LARGE_ADAPTIVE_BANNER
*Type:* VARIABLE

### SIZE_BANNER
*Type:* VARIABLE

### SIZE_FLUID
*Type:* VARIABLE

### SIZE_FULL_BANNER
*Type:* VARIABLE

### SIZE_LARGE_BANNER
*Type:* VARIABLE

### SIZE_LEADEARBOARD
*Type:* VARIABLE

### SIZE_MEDIUM_RECTANGLE
*Type:* VARIABLE

### SIZE_SMART_BANNER
*Type:* VARIABLE

### POS_NONE
*Type:* VARIABLE

### POS_TOP_LEFT
*Type:* VARIABLE

### POS_TOP_CENTER
*Type:* VARIABLE

### POS_TOP_RIGHT
*Type:* VARIABLE

### POS_BOTTOM_LEFT
*Type:* VARIABLE

### POS_BOTTOM_CENTER
*Type:* VARIABLE

### POS_BOTTOM_RIGHT
*Type:* VARIABLE

### POS_CENTER
*Type:* VARIABLE

### MAX_AD_CONTENT_RATING_G
*Type:* VARIABLE

### MAX_AD_CONTENT_RATING_PG
*Type:* VARIABLE

### MAX_AD_CONTENT_RATING_T
*Type:* VARIABLE

### MAX_AD_CONTENT_RATING_MA
*Type:* VARIABLE
