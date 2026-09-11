# extension-applovin

**Namespace:** `applovin`
**Language:** Lua
**Type:** Extension

Functions and constants for AppLovin MAX SDK 13.6.3 on Android and iOS.

## API

### applovin.initialize
*Type:* FUNCTION
Initializes MAX asynchronously. Install the callback and apply privacy, consent-flow, user, logging, mute, creative-debugger, and test-device settings first. Do not load or show ads until `OnSdkInitializedEvent`. Calling this function with a placeholder or an SDK key that does not belong to the app is an integration error.

**Parameters**

- `sdk_key` (string) - SDK key from MAX Dashboard > Account > General > Keys.

**Examples**

```
local function on_max_event(self, name, params)
    if name == "OnSdkInitializedEvent" then
        applovin.load_interstitial("YOUR_AD_UNIT_ID")
    end
end

function init(self)
    applovin.set_callback(on_max_event)
    applovin.set_test_device_advertising_ids({ "YOUR_IDFA_OR_GAID" })
    applovin.initialize("YOUR_SDK_KEY")
end

```

### applovin.set_callback
*Type:* FUNCTION
Sets the callback that receives all MAX events on the Defold update thread. Replaces any previously installed callback. Pass `nil` to remove it. The callback signature is `function(self, name, params)`. `name` is one of the events below and `params` is a table.
Lifecycle events: `OnSdkInitializedEvent`, `OnCmpCompletedEvent`.
Interstitial events: `OnInterstitialAdLoadedEvent`, `OnInterstitialAdLoadFailedEvent`, `OnInterstitialAdDisplayedEvent`, `OnInterstitialAdDisplayFailedEvent`, `OnInterstitialAdHiddenEvent`, `OnInterstitialAdClickedEvent`, `OnInterstitialAdRevenuePaidEvent`.
Rewarded events: `OnRewardedAdLoadedEvent`, `OnRewardedAdLoadFailedEvent`, `OnRewardedAdDisplayedEvent`, `OnRewardedAdDisplayFailedEvent`, `OnRewardedAdHiddenEvent`, `OnRewardedAdClickedEvent`, `OnRewardedAdReceivedRewardEvent`, `OnRewardedAdRevenuePaidEvent`.
Banner events: `OnBannerAdLoadedEvent`, `OnBannerAdLoadFailedEvent`, `OnBannerAdClickedEvent`, `OnBannerAdExpandedEvent`, `OnBannerAdCollapsedEvent`, `OnBannerAdRevenuePaidEvent`.
MREC events: `OnMRecAdLoadedEvent`, `OnMRecAdLoadFailedEvent`, `OnMRecAdClickedEvent`, `OnMRecAdExpandedEvent`, `OnMRecAdCollapsedEvent`, `OnMRecAdRevenuePaidEvent`.
`OnSdkInitializedEvent` params: `countryCode` (string), `consentFlowUserGeography` (number), `isTestModeEnabled` (boolean), and `appTrackingStatus` (number, iOS only).
`OnCmpCompletedEvent` has an empty params table on success. On failure it contains `code` (number), `message` (string), `cmpCode` (number), and `cmpMessage` (string).
Successful ad, display, click, hide, expand, collapse, reward, and revenue events include ad information: `adUnitIdentifier`, `format`, `networkName`, `networkPlacement`, `creativeIdentifier`, `placement`, `revenue`, `revenuePrecision`, `requestLatencyMillis`, `dspName`, and `dspIdentifier`. Values unavailable from a mediated network may be empty or absent. Revenue is in USD and may be `0`; use `revenuePrecision` before interpreting it.
`OnRewardedAdReceivedRewardEvent` additionally includes `label` (string) and `amount` (number).
Load failures include `adUnitIdentifier`, `code`, `message`, and `requestLatencyMillis`. Display failures include available ad information plus `code`, `message`, `mediatedNetworkErrorCode`, and `mediatedNetworkErrorMessage`; their `requestLatencyMillis` is the ad request latency. Error codes and messages come from MAX and, for display failures, the mediated network.

**Parameters**

- `callback` (function) - Event callback, or `nil` to remove the callback.
  - `self` (object) - Script instance that installed the callback.
  - `name` (string) - Event name.
  - `params` (table) - Event payload.

### applovin.is_initialized
*Type:* FUNCTION
Returns whether asynchronous SDK initialization has completed.

**Returns**

- `boolean`

### applovin.show_mediation_debugger
*Type:* FUNCTION
Shows the MAX Mediation Debugger. Use this only after SDK initialization and from a user action.

### applovin.set_has_user_consent
*Type:* FUNCTION
Sets the user's legally obtained consent state for interest-based advertising. Apply the value before `initialize()`. This API does not collect consent.

**Parameters**

- `has_user_consent` (boolean)

### applovin.has_user_consent
*Type:* FUNCTION
Returns the current user-consent value. The API cannot distinguish an explicit `false` from a value your application never set, so persist and apply your consent decision.

**Returns**

- `boolean`

### applovin.set_do_not_sell
*Type:* FUNCTION
Sets whether the user opted out of sale or sharing of personal information. Apply the legally obtained value before `initialize()`.

**Parameters**

- `do_not_sell` (boolean)

### applovin.is_do_not_sell
*Type:* FUNCTION
Returns the current do-not-sell value. The API cannot distinguish an explicit `false` from a value your application never set.

**Returns**

- `boolean`

### applovin.set_terms_and_privacy_policy_flow_enabled
*Type:* FUNCTION
Enables or disables MAX's Terms and Privacy Policy Flow. Configure the required CMP dependencies, dashboard message, privacy-policy URL, and iOS/Android app metadata first. Set this before `initialize()`.

**Parameters**

- `enabled` (boolean)

### applovin.set_privacy_policy_url
*Type:* FUNCTION
Sets the public HTTPS privacy-policy URL used by the MAX consent flow before initialization.

**Parameters**

- `url` (string)

### applovin.set_terms_of_service_url
*Type:* FUNCTION
Sets the optional public HTTPS Terms of Service URL used by the MAX consent flow before initialization.

**Parameters**

- `url` (string)

### applovin.set_consent_flow_debug_user_geography
*Type:* FUNCTION
Overrides geography for consent-flow testing. Pass `"GDPR"` or `"OTHER"`. Use only in development and set it before initialization.

**Parameters**

- `geography` (string)

### applovin.show_cmp_for_existing_user
*Type:* FUNCTION
Shows the integrated CMP for an existing user. Offer this from a privacy-settings action only when `has_supported_cmp()` is true; completion arrives as `OnCmpCompletedEvent`.

### applovin.has_supported_cmp
*Type:* FUNCTION
Returns whether a supported CMP is integrated and available.

**Returns**

- `boolean`

### applovin.is_tablet
*Type:* FUNCTION
Returns whether the current device uses the SDK's tablet classification.

**Returns**

- `boolean`

### applovin.set_user_id
*Type:* FUNCTION
Sets your internal user identifier. Do not use personally identifiable information. Set it before initialization when it must be available to mediated networks.

**Parameters**

- `user_id` (string)

### applovin.set_muted
*Type:* FUNCTION
Requests muted audio for mediated networks that support the setting.

**Parameters**

- `muted` (boolean)

### applovin.is_muted
*Type:* FUNCTION
Returns the current mute setting.

**Returns**

- `boolean`

### applovin.set_verbose_logging_enabled
*Type:* FUNCTION
Enables or disables verbose MAX logging. Enable it for integration testing, not production.

**Parameters**

- `enabled` (boolean)

### applovin.is_verbose_logging_enabled
*Type:* FUNCTION
Returns the current verbose-logging setting.

**Returns**

- `boolean`

### applovin.set_creative_debugger_enabled
*Type:* FUNCTION
Enables or disables the MAX Creative Debugger for QA builds.

**Parameters**

- `enabled` (boolean)

### applovin.set_test_device_advertising_ids
*Type:* FUNCTION
Sets devices that should receive test ads. Pass an array of IDFAs on iOS or GAIDs on Android before `initialize()`. Never ship another user's advertising identifier.

**Parameters**

- `advertising_ids` (array) - Array of advertising-identifier strings.

### applovin.track_event
*Type:* FUNCTION
Tracks a custom AppLovin event after SDK initialization with JSON string parameters. `event_name` must be non-empty. Invalid JSON or a non-object value is logged and sent as an empty parameter map.

**Parameters**

- `event_name` (string) - Non-empty event name.
- `parameters` (string) - JSON object encoded as a string, for example `"{\"level\":\"5\"}"`.

### applovin.load_interstitial
*Type:* FUNCTION
Starts loading an interstitial. Call only after `OnSdkInitializedEvent`.

**Parameters**

- `ad_unit_id` (string)

### applovin.is_interstitial_ready
*Type:* FUNCTION
Returns whether an interstitial is ready for the ad unit.

**Parameters**

- `ad_unit_id` (string)

**Returns**

- `boolean`

### applovin.show_interstitial
*Type:* FUNCTION
Shows a loaded interstitial, optionally attributing it to a placement.

**Parameters**

- `ad_unit_id` (string)
- `placement` (string) - MAX placement name.

### applovin.set_interstitial_extra_parameter
*Type:* FUNCTION
Sets a MAX-supported extra parameter on an interstitial ad object.

**Parameters**

- `ad_unit_id` (string)
- `key` (string)
- `value` (string)

### applovin.load_rewarded_ad
*Type:* FUNCTION
Starts loading a rewarded ad. Call only after `OnSdkInitializedEvent`.

**Parameters**

- `ad_unit_id` (string)

### applovin.is_rewarded_ad_ready
*Type:* FUNCTION
Returns whether a rewarded ad is ready for the ad unit.

**Parameters**

- `ad_unit_id` (string)

**Returns**

- `boolean`

### applovin.show_rewarded_ad
*Type:* FUNCTION
Shows a loaded rewarded ad, optionally attributing it to a placement.

**Parameters**

- `ad_unit_id` (string)
- `placement` (string) - MAX placement name.

### applovin.set_rewarded_ad_extra_parameter
*Type:* FUNCTION
Sets a MAX-supported extra parameter on a rewarded ad object.

**Parameters**

- `ad_unit_id` (string)
- `key` (string)
- `value` (string)

### applovin.create_banner
*Type:* FUNCTION
Creates and starts loading a banner at the requested screen position.

**Parameters**

- `ad_unit_id` (string)
- `position` (string) - `top_left`, `top_center`, `top_right`, `centered`, `bottom_left`, `bottom_center`, or `bottom_right`.

### applovin.set_banner_background_color
*Type:* FUNCTION
Sets a banner's background color.

**Parameters**

- `ad_unit_id` (string)
- `hex_color` (string) - Color in `#RRGGBB` or `#AARRGGBB` form.

### applovin.set_banner_placement
*Type:* FUNCTION
Sets the MAX placement name for a banner ad unit. Call this before `create_banner()` so the placement is attached to the first load; calling it later updates the existing view.

**Parameters**

- `ad_unit_id` (string)
- `placement` (string)

### applovin.set_banner_extra_parameter
*Type:* FUNCTION
Sets a MAX-supported extra parameter on an existing banner.

**Parameters**

- `ad_unit_id` (string)
- `key` (string)
- `value` (string)

### applovin.update_banner_position
*Type:* FUNCTION
Moves an existing banner to a supported screen position.

**Parameters**

- `ad_unit_id` (string)
- `position` (string) - `top_left`, `top_center`, `top_right`, `centered`, `bottom_left`, `bottom_center`, or `bottom_right`.

### applovin.start_banner_auto_refresh
*Type:* FUNCTION
Starts auto-refresh on an existing banner.

**Parameters**

- `ad_unit_id` (string)

### applovin.stop_banner_auto_refresh
*Type:* FUNCTION
Stops auto-refresh on an existing banner.

**Parameters**

- `ad_unit_id` (string)

### applovin.show_banner
*Type:* FUNCTION
Shows an existing banner.

**Parameters**

- `ad_unit_id` (string)

### applovin.hide_banner
*Type:* FUNCTION
Hides an existing banner without destroying it.

**Parameters**

- `ad_unit_id` (string)

### applovin.destroy_banner
*Type:* FUNCTION
Destroys a banner and releases its native view.

**Parameters**

- `ad_unit_id` (string)

### applovin.create_mrec
*Type:* FUNCTION
Creates and starts loading an MREC at the requested screen position.

**Parameters**

- `ad_unit_id` (string)
- `position` (string) - `top_left`, `top_center`, `top_right`, `centered`, `bottom_left`, `bottom_center`, or `bottom_right`.

### applovin.set_mrec_placement
*Type:* FUNCTION
Sets the MAX placement name for an MREC ad unit. Call this before `create_mrec()` so the placement is attached to the first load; calling it later updates the existing view.

**Parameters**

- `ad_unit_id` (string)
- `placement` (string)

### applovin.set_mrec_extra_parameter
*Type:* FUNCTION
Sets a MAX-supported extra parameter on an existing MREC.

**Parameters**

- `ad_unit_id` (string)
- `key` (string)
- `value` (string)

### applovin.update_mrec_position
*Type:* FUNCTION
Moves an existing MREC to a supported screen position.

**Parameters**

- `ad_unit_id` (string)
- `position` (string) - `top_left`, `top_center`, `top_right`, `centered`, `bottom_left`, `bottom_center`, or `bottom_right`.

### applovin.start_mrec_auto_refresh
*Type:* FUNCTION
Starts auto-refresh on an existing MREC.

**Parameters**

- `ad_unit_id` (string)

### applovin.stop_mrec_auto_refresh
*Type:* FUNCTION
Stops auto-refresh on an existing MREC.

**Parameters**

- `ad_unit_id` (string)

### applovin.show_mrec
*Type:* FUNCTION
Shows an existing MREC.

**Parameters**

- `ad_unit_id` (string)

### applovin.hide_mrec
*Type:* FUNCTION
Hides an existing MREC without destroying it.

**Parameters**

- `ad_unit_id` (string)

### applovin.destroy_mrec
*Type:* FUNCTION
Destroys an MREC and releases its native view.

**Parameters**

- `ad_unit_id` (string)

### CONSENT_FLOW_USER_GEOGRAPHY_UNKNOWN
*Type:* VARIABLE
Consent-flow geography is unknown.

### CONSENT_FLOW_USER_GEOGRAPHY_GDPR
*Type:* VARIABLE
User is in a GDPR-region geography.

### CONSENT_FLOW_USER_GEOGRAPHY_OTHER
*Type:* VARIABLE
User is outside the GDPR-region geography.

### APP_TRACKING_TRANSPARENCY_STATUS_UNAVAILABLE
*Type:* VARIABLE
ATT status is unavailable on this platform or OS version.

### APP_TRACKING_TRANSPARENCY_STATUS_NOT_DETERMINED
*Type:* VARIABLE
User has not yet chosen an ATT authorization state.

### APP_TRACKING_TRANSPARENCY_STATUS_RESTRICTED
*Type:* VARIABLE
Device policy restricts ATT authorization.

### APP_TRACKING_TRANSPARENCY_STATUS_DENIED
*Type:* VARIABLE
User denied ATT authorization.

### APP_TRACKING_TRANSPARENCY_STATUS_AUTHORIZED
*Type:* VARIABLE
User authorized ATT tracking access.
