# extension-ironsource

**Namespace:** `ironsource`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with IronSource API

## API

### ironsource.init
*Type:* FUNCTION
Initialize the IronSource SDK

**Parameters**

- `app_key` (string) - App key you can get in the IronSource dashboard

### ironsource.set_callback
*Type:* FUNCTION
Sets a callback function for receiving events from the SDK. Call `ironsource.set_callback(nil)` to remove callback

**Parameters**

- `callback` (function) - Callback function that is executed on any event in the SDK.
  - `self` (object) - The calling script instance
  - `message_id` (number) - One of message types: `ironsource.MSG_INIT` initialization, `ironsource.MSG_INTERSTITIAL` message from Interstitial ad unit, `ironsource.MSG_REWARDED` message from Rewarded ad unit
  - `message` (table) - A table holding the data. It always contains `event`, and also some other values depends on a message
    - `event` (number) - One of event types: `ironsource.EVENT_AD_AVAILABLE`, `ironsource.EVENT_AD_UNAVAILABLE`, `ironsource.EVENT_AD_OPENED`, `ironsource.EVENT_AD_CLOSED`, `ironsource.EVENT_AD_REWARDED`, `ironsource.EVENT_AD_CLICKED`, `ironsource.EVENT_AD_SHOW_FAILED`, `ironsource.EVENT_AD_READY`, `ironsource.EVENT_AD_SHOW_SUCCEEDED`, `ironsource.EVENT_AD_LOAD_FAILED` `ironsource.EVENT_JSON_ERROR` `ironsource.EVENT_INIT_COMPLETE` `ironsource.EVENT_CONSENT_LOADED` `ironsource.EVENT_CONSENT_SHOWN` `ironsource.EVENT_CONSENT_LOAD_FAILED` `ironsource.EVENT_CONSENT_SHOW_FAILED` `ironsource.EVENT_CONSENT_ACCEPTED` `ironsource.EVENT_CONSENT_DISMISSED` `ironsource.EVENT_STATUS_AUTHORIZED` `ironsource.EVENT_STATUS_DENIED` `ironsource.EVENT_STATUS_NOT_DETERMINED` `ironsource.EVENT_STATUS_RESTRICTED`

**Examples**

```
local function ironsource_callback(self, message_id, message)
  callback_logger(self, message_id, message)
  if message_id == ironsource.MSG_INIT then
      if message.event == ironsource.EVENT_INIT_COMPLETE then
          -- ironSource SDK is initialized
          -- massage{}
      end
  elseif message_id == ironsource.MSG_REWARDED then
      if message.event == ironsource.EVENT_AD_AVAILABLE then
          -- Indicates that there's an available ad.
          -- The adInfo object includes information about the ad that was loaded successfully
          -- massage{AdInfo}
      elseif message.event == ironsource.EVENT_AD_UNAVAILABLE then
          -- Indicates that no ads are available to be displayed
          -- massage{}
      elseif message.event == ironsource.EVENT_AD_OPENED then
          -- The Rewarded Video ad view has opened. Your activity will loose focus
          -- massage{AdInfo}
      elseif message.event == ironsource.EVENT_AD_CLOSED then
          -- The Rewarded Video ad view is about to be closed. Your activity will regain its focus
          -- massage{AdInfo}
      elseif message.event == ironsource.EVENT_AD_REWARDED then
          -- The user completed to watch the video, and should be rewarded.
          -- The placement parameter will include the reward data.
          -- When using server-to-server callbacks, you may ignore this event and wait for the ironSource server callback
          -- massage{AdInfo, Placement}
      elseif message.event == ironsource.EVENT_AD_SHOW_FAILED then
          -- The rewarded video ad was failed to show
          -- massage{AdInfo, IronSourceError}
      elseif message.event == ironsource.EVENT_AD_CLICKED then
          -- Invoked when the video ad was clicked.
          -- This callback is not supported by all networks, and we recommend using it
          -- only if it's supported by all networks you included in your build
          -- massage{AdInfo, Placement}
      end
  elseif message_id == ironsource.MSG_INTERSTITIAL then
      if message.event == ironsource.EVENT_AD_READY then
          -- Invoked when the interstitial ad was loaded successfully.
          -- AdInfo parameter includes information about the loaded ad
          -- massage{AdInfo}
      elseif message.event == ironsource.EVENT_AD_LOAD_FAILED then
          -- Indicates that the ad failed to be loaded
          -- massage{IronSourceError}
      elseif message.event == ironsource.EVENT_AD_OPENED then
          -- Invoked when the Interstitial Ad Unit has opened, and user left the application screen.
          -- This is the impression indication.
          -- massage{AdInfo}
      elseif message.event == ironsource.EVENT_AD_CLOSED then
          -- Invoked when the interstitial ad closed and the user went back to the application screen.
          -- massage{AdInfo}
      elseif message.event == ironsource.EVENT_AD_SHOW_FAILED then
          -- Invoked when the ad failed to show
          -- massage{AdInfo, IronSourceError}
      elseif message.event == ironsource.EVENT_AD_CLICKED then
          -- Invoked when end user clicked on the interstitial ad
          -- massage{AdInfo}
      elseif message.event == ironsource.EVENT_AD_SHOW_SUCCEEDED then
          -- Invoked before the interstitial ad was opened, and before the InterstitialOnAdOpenedEvent is reported.
          -- This callback is not supported by all networks, and we recommend using it only if
          -- it's supported by all networks you included in your build.
          -- massage{AdInfo}
      end
  elseif message_id == ironsource.MSG_CONSENT then
      if message.event == ironsource.EVENT_CONSENT_LOADED then
          -- Consent View was loaded successfully
          -- massage.consent_view_type
      elseif message.event == ironsource.EVENT_CONSENT_SHOWN then
          -- Consent view was displayed successfully
          -- massage.consent_view_type
      elseif message.event == ironsource.EVENT_CONSENT_LOAD_FAILED then
          -- Consent view was failed to load
          -- massage.consent_view_type, massage.error_code, massage.error_message
      elseif message.event == ironsource.EVENT_CONSENT_SHOW_FAILED then
          -- Consent view was not displayed, due to error
          -- massage.consent_view_type, massage.error_code, massage.error_message
      elseif message.event == ironsource.EVENT_CONSENT_ACCEPTED then
          -- The user pressed the Settings or Next buttons
          -- massage.consent_view_type
      elseif message.event == ironsource.EVENT_CONSENT_DISMISSED then
          -- The user dismiss consent
          -- massage.consent_view_type
      end
  elseif message_id == ironsource.MSG_IDFA then
      if message.event == ironsource.EVENT_STATUS_AUTHORIZED then
          -- ATTrackingManagerAuthorizationStatusAuthorized
      elseif message.event == ironsource.EVENT_STATUS_DENIED then
          -- ATTrackingManagerAuthorizationStatusDenied
      elseif message.event == ironsource.EVENT_STATUS_NOT_DETERMINED then
          -- ATTrackingManagerAuthorizationStatusNotDetermined
      elseif message.event == ironsource.EVENT_STATUS_RESTRICTED then
          -- ATTrackingManagerAuthorizationStatusRestricted
      end
  end
end

```

### ironsource.set_consent
*Type:* FUNCTION
If the user provided consent, set the following flag to true (must be called before `ironsource.init()`). [Original docs](https://developers.is.com/ironsource-mobile/general/making-sure-youre-compliant-post-gdpr/#step-2) [Android](https://developers.is.com/ironsource-mobile/android/regulation-advanced-settings/), [iOS](https://developers.is.com/ironsource-mobile/ios/regulation-advanced-settings/)

**Parameters**

- `is_consent_provided` (boolean)

### ironsource.validate_integration
*Type:* FUNCTION
The ironSource SDK provides an easy way to verify that you’ve successfully integrated the ironSource SDK and any additional adapters; it also makes sure all required dependencies and frameworks were added for the various mediated ad networks. The Integration Helper will now also portray the compatibility between the SDK and adapter versions. Original docs [Android](https://developers.is.com/ironsource-mobile-android/integration-helper-android/), [iOS](https://developers.is.com/ironsource-mobile/ios/integration-helper-ios/)

### ironsource.set_metadata
*Type:* FUNCTION
Function used for setting different parameterd for adapters and the SDK itself.

**Parameters**

- `key` (String)
- `value` (String)

### ironsource.set_user_id
*Type:* FUNCTION
If you’re serving the offerwall ad unit or using server-to-server callbacks to reward your users with ironSource SDK rewarded ad units, you must define a unique identifier for each user (“UserID”), using the setUserID method.
Set the UserID before the init request, to make sure you avoid any data loses, related to the user. Use a unique identifier, with up to 64 alphanumeric characters.
Original docs [Android](https://developers.is.com/ironsource-mobile/android/advanced-settings/), [iOS](https://developers.is.com/ironsource-mobile/ios/advanced-settings-2/)

**Parameters**

- `user_id` (string)

### ironsource.launch_test_suite
*Type:* FUNCTION
The LevelPlay integration test suite enables you to quickly and easily test your app’s integration, verify platform setup and review ads related to your configured networks. Original docs [Android](https://developers.is.com/ironsource-mobile/android/unity-levelplay-test-suite/#step-1), [iOS](https://developers.is.com/ironsource-mobile/ios/unity-levelplay-test-suite/)

### ironsource.request_idfa
*Type:* FUNCTION
iOS Only. Display the App Tracking Transparency authorization request for accessing the IDFA. Original docs [iOS](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/3547037-requesttrackingauthorization)

### ironsource.get_idfa_status
*Type:* FUNCTION
iOS Only. Returns current authorization status for the IDFA One of event types: `ironsource.EVENT_STATUS_AUTHORIZED` `ironsource.EVENT_STATUS_DENIED` `ironsource.EVENT_STATUS_NOT_DETERMINED` `ironsource.EVENT_STATUS_RESTRICTED` or nil if not supported Original docs [iOS](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/3547037-requesttrackingauthorization)

### ironsource.set_adapters_debug
*Type:* FUNCTION
Manage the debug logs for your integrated mediation ad networks with this boolean. When set to TRUE it enables debug logs to help you troubleshoot issues with all of the mediation ad networks that permit to do so. Remove this code before your app goes live with our ad units!

**Returns**

- `boolean`

### ironsource.load_consent_view
*Type:* FUNCTION
iOS Only. Load the IronSource permission pop-up. [iOS](https://developers.is.com/ironsource-mobile/ios/permission-popup-ios/#step-1)

**Returns**

- `string` - one of the folowing values "pre" or "post"

### ironsource.show_consent_view
*Type:* FUNCTION
iOS Only. Display the IronSource permission pop-up. [iOS](https://developers.is.com/ironsource-mobile/ios/permission-popup-ios/#step-1)

**Returns**

- `string` - one of the folowing values "pre" or "post"

### ironsource.should_track_network_state
*Type:* FUNCTION
You can determine and monitor the internet connection on the user’s device through the ironSource Network Change Status function. This enables the SDK to change its availability according to network modifications, i.e. in the case of no network connection, the availability will turn to FALSE. The default of this function is false; if you’d like to listen to it for changes in connectivity, activate it in the SDK initialization [Android shouldTrackNetworkState](https://developers.is.com/ironsource-mobile/android/rewarded-video-integration-android/#step-1), [iOS shouldTrackReachability](https://developers.is.com/ironsource-mobile/ios/rewarded-video-integration-ios/#step-1)

**Parameters**

- `should_track` (boolean)

### ironsource.is_rewarded_video_available
*Type:* FUNCTION
You can receive the availability status of the AD Unit through the callback. Alternatively, ask for ad availability directly by calling this function. [Android](https://developers.is.com/ironsource-mobile/android/rewarded-video-integration-android/#step-1), [iOS](https://developers.is.com/ironsource-mobile/ios/rewarded-video-integration-ios/#step-1)

**Returns**

- `boolean`

### ironsource.show_rewarded_video
*Type:* FUNCTION
You can show a video ad to your users and define the exact Placement you want to show an ad. The Reward settings of this Placement will be pulled from the ironSource server. Original docs [Android](https://developers.is.com/ironsource-mobile/android/rewarded-video-integration-android/#step-1), [iOS](https://developers.is.com/ironsource-mobile/ios/rewarded-video-integration-ios/#step-1)

**Parameters**

- `placement_name` (String) - maybe nil - then default placement used

### ironsource.get_rewarded_video_placement_info
*Type:* FUNCTION
Get details about the specific Reward associated with each Ad Placement. Original docs [Android](https://developers.is.com/ironsource-mobile/android/rewarded-video-integration-android/#step-1), [iOS](https://developers.is.com/ironsource-mobile/ios/rewarded-video-integration-ios/#step-1)

**Parameters**

- `placement_name` (String)

### ironsource.get_rewarded_video_placement_info
*Type:* FUNCTION
Get details about the specific Reward associated with each Ad Placement. Original docs [Android](https://developers.is.com/ironsource-mobile/android/rewarded-video-integration-android/#step-1), [iOS](https://developers.is.com/ironsource-mobile/ios/rewarded-video-integration-ios/#step-1)

**Parameters**

- `placement_name` (String)

**Returns**

- `table` - contains the following fields `placement_id`, `placement_name`, `is_default`, `reward_name`, `reward_amount`

### ironsource.is_rewarded_video_placement_capped
*Type:* FUNCTION
To ensure you don’t show the traffic driver (Rewarded Video button) to prompt the user to watch an ad when the placement is capped, you must call the below method to verify if a specific placement has reached its ad limit. When requesting availability, you might receive a TRUE response but in the case your placement has reached its capping limit, the ad will not be served to the user. Original docs [Android isRewardedVideoPlacementCapped](https://developers.is.com/ironsource-mobile/android/rewarded-video-integration-android/#step-2), [iOS isRewardedVideoCappedForPlacement](https://developers.is.com/ironsource-mobile/ios/rewarded-video-integration-ios/#step-2)

**Parameters**

- `placement_name` (String)

**Returns**

- `boolean`

### ironsource.set_dynamic_user_id
*Type:* FUNCTION
The Dynamic UserID is a parameter to verify AdRewarded transactions and can be changed throughout the session. To receive this parameter through the server to server callbacks, it must be set before calling showRewardedVideo. You will receive a dynamicUserId parameter in the callback URL with the reward details. [Android](https://developers.is.com/ironsource-mobile/android/rewarded-video-integration-android/#step-2), [iOS](https://developers.is.com/ironsource-mobile/ios/rewarded-video-integration-ios/#step-2)

**Parameters**

- `dynamic_user_id` (String)

### ironsource.load_interstitial
*Type:* FUNCTION
We recommend requesting an Interstitial Ad a short while before you plan on showing it to your users as the loading process can take time. [Android](https://developers.is.com/ironsource-mobile/android/interstitial-mediation-integration-android/#step-2), [iOS](https://developers.is.com/ironsource-mobile/ios/interstitial-integration-ios/#step-2)

### ironsource.is_interstitial_ready
*Type:* FUNCTION
You can receive the availability status of the AD Unit through the callback. Alternatively, ask for ad availability directly by calling this function. [Android](https://developers.is.com/ironsource-mobile/android/interstitial-mediation-integration-android/#step-2), [iOS](https://developers.is.com/ironsource-mobile/ios/interstitial-integration-ios/#step-2)

**Returns**

- `boolean`

### ironsource.get_interstitial_placement_info
*Type:* FUNCTION
Android Only. Get details about the specific Ad Placement. Original docs [Android](https://developers.is.com/ironsource-mobile/android/interstitial-mediation-integration-android/#step-3), [iOS](https://developers.is.com/ironsource-mobile/ios/interstitial-integration-ios/#step-3)

**Parameters**

- `placement_name` (String)

**Returns**

- `table` - contains the following fields `placement_id`, `placement_name`, `is_default`

### ironsource.is_interstitial_placement_capped
*Type:* FUNCTION
In addition to LevelPlay‘s Ad Placements, you can now configure capping and pacing settings for selected placements. Capping and pacing improve the user experience in your app by limiting the number of ads served within a defined timeframe. Original docs [Android](https://developers.is.com/ironsource-mobile/android/interstitial-mediation-integration-android/#step-3), [iOS](https://developers.is.com/ironsource-mobile/ios/interstitial-integration-ios/#step-3)

**Parameters**

- `placement_name` (String)

**Returns**

- `boolean`

### ironsource.show_interstitial
*Type:* FUNCTION
Serve an Interstitial ad to your users. Call it once you receive the ironsource.EVENT_AD_READY callback, you are ready to show an Interstitial Ad to your users. To provide the best experience for your users, make sure to pause any game action, including audio, during the time the ad is displayed. Original docs [Android](https://developers.is.com/ironsource-mobile/android/rewarded-video-integration-android/#step-1), [iOS](https://developers.is.com/ironsource-mobile/ios/rewarded-video-integration-ios/#step-1)

**Parameters**

- `placement_name` (String) - maybe nil - then default placement used

### MSG_INTERSTITIAL
*Type:* VARIABLE

### MSG_REWARDED
*Type:* VARIABLE

### MSG_CONSENT
*Type:* VARIABLE

### MSG_INIT
*Type:* VARIABLE

### MSG_IDFA
*Type:* VARIABLE

### EVENT_AD_AVAILABLE
*Type:* VARIABLE

### EVENT_AD_UNAVAILABLE
*Type:* VARIABLE

### EVENT_AD_OPENED
*Type:* VARIABLE

### EVENT_AD_CLOSED
*Type:* VARIABLE

### EVENT_AD_REWARDED
*Type:* VARIABLE

### EVENT_AD_CLICKED
*Type:* VARIABLE

### EVENT_AD_SHOW_FAILED
*Type:* VARIABLE

### EVENT_AD_READY
*Type:* VARIABLE

### EVENT_AD_SHOW_SUCCEEDED
*Type:* VARIABLE

### EVENT_AD_LOAD_FAILED
*Type:* VARIABLE

### EVENT_JSON_ERROR
*Type:* VARIABLE

### EVENT_INIT_COMPLETE
*Type:* VARIABLE

### EVENT_CONSENT_LOADED
*Type:* VARIABLE

### EVENT_CONSENT_SHOWN
*Type:* VARIABLE

### EVENT_CONSENT_LOAD_FAILED
*Type:* VARIABLE

### EVENT_CONSENT_SHOW_FAILED
*Type:* VARIABLE

### EVENT_CONSENT_ACCEPTED
*Type:* VARIABLE

### EVENT_CONSENT_DISMISSED
*Type:* VARIABLE

### EVENT_STATUS_AUTHORIZED
*Type:* VARIABLE

### EVENT_STATUS_DENIED
*Type:* VARIABLE

### EVENT_STATUS_NOT_DETERMINED
*Type:* VARIABLE

### EVENT_STATUS_RESTRICTED
*Type:* VARIABLE
