# extension-levelplay

**Namespace:** `levelplay`
**Language:** Lua
**Type:** Extension

Functions and constants for Unity LevelPlay mediation on Android and iOS.

## API

### levelplay.set_callback
*Type:* FUNCTION
Sets the callback used for all LevelPlay events. Pass nil to remove it.

**Parameters**

- `callback` (function)
  - `self` (object) - The script instance that installed the callback.
  - `message_id` (number) - One of MSG_INIT, MSG_INTERSTITIAL, MSG_REWARDED, MSG_BANNER, or MSG_TRACKING.
  - `message` (table) - Event data. Every asynchronous SDK event contains `event`. Events from a created ad object also contain `handle`; pre-creation validation errors do not.
    - `event` (number) - An EVENT_* constant, or a TRACKING_STATUS_* constant for MSG_TRACKING.
    - `handle` (number) - The ad object that emitted the event.
    - `error_code` (number)
    - `error_message` (string)
    - `error_domain` (string) - Native error domain when supplied by iOS.
    - `operation` (string) - Bridge operation associated with a validation error.
    - `error` (string) - Serialization error detail for EVENT_JSON_ERROR.
    - `ad_quality_enabled` (boolean) - Whether Ad Quality is enabled, when reported during initialization.
    - `ad_id` (string)
    - `ad_unit_id` (string)
    - `ad_unit_name` (string)
    - `ad_format` (string)
    - `placement_name` (string)
    - `auction_id` (string)
    - `country` (string)
    - `ab` (string)
    - `segment_name` (string)
    - `ad_network` (string)
    - `instance_name` (string)
    - `instance_id` (string)
    - `revenue` (number)
    - `precision` (string)
    - `encrypted_cpm` (string)
    - `creative_id` (string)
    - `conversion_value` (number) - Conversion value when supplied by iOS.
    - `reward_name` (string)
    - `reward_amount` (number)
    - `ad_width` (number)
    - `ad_height` (number)
    - `ad_size_description` (string)
    - `ad_size_is_adaptive` (boolean)

### levelplay.init
*Type:* FUNCTION
Initializes LevelPlay. Configure privacy before calling this function. Create ad objects only after EVENT_INIT_SUCCEEDED.

**Parameters**

- `app_key` (string) - Application key from the LevelPlay dashboard. This is not an ad-unit ID.
- `user_id` (string) - Stable application user ID included in the initialization request.

### levelplay.get_sdk_version
*Type:* FUNCTION
Returns the native LevelPlay SDK version.

**Returns**

- `string`

### levelplay.set_gdpr_consent
*Type:* FUNCTION
Passes the user's GDPR consent choice to LevelPlay and supported mediated networks. It does not display a consent form or read another extension's private state. For a custom or non-compatible CMP, call it before init with the collected choice. LevelPlay SDK 7.7.0 and newer automatically reads Google UMP and compatible Google Additional Consent signals, so do not also pass the same choice with this function in that setup.

**Parameters**

- `consent` (boolean)

### levelplay.set_ccpa
*Type:* FUNCTION
Passes a US privacy "do not sell or share" choice. True means the user opted out. Call before init.

**Parameters**

- `opted_out` (boolean)

### levelplay.set_coppa
*Type:* FUNCTION
Sets whether the user is child-directed for COPPA treatment. True flags the user as child-directed. Call before init.

**Parameters**

- `child_directed` (boolean)

### levelplay.set_metadata
*Type:* FUNCTION
Sets an SDK or mediated-network metadata value. Set network-required values before init.

**Parameters**

- `key` (string)
- `value` (string)

### levelplay.set_meta_limited_data_use
*Type:* FUNCTION
Configures Meta Audience Network Limited Data Use before init. This calls Meta's SDK directly and returns false if the Meta adapter is not linked or initialization already started.

**Parameters**

- `enabled` (boolean) - True supplies the LDU option; false clears Meta data-processing options.
- `country` (number) - Meta country code. Zero, the default, asks Meta to geolocate.
- `state` (number) - Meta state code. Zero, the default, asks Meta to geolocate.

**Returns**

- `boolean`

### levelplay.set_meta_advertiser_tracking
*Type:* FUNCTION
Sets Meta Audience Network's iOS advertiser-tracking flag before init. Returns false on Android, when Meta is not linked, or after initialization starts.

**Parameters**

- `enabled` (boolean)

**Returns**

- `boolean`

### levelplay.set_dynamic_user_id
*Type:* FUNCTION
Sets the dynamic user ID used by server-to-server rewarded callbacks. The value must contain 1–64 alphanumeric characters. Call before showing the rewarded ad it should apply to.

**Parameters**

- `user_id` (string)

**Returns**

- `boolean`

### levelplay.set_adapters_debug
*Type:* FUNCTION
Enables or disables mediated-network debug logging. Disable it in production.

**Parameters**

- `enabled` (boolean)

### levelplay.validate_integration
*Type:* FUNCTION
Runs the native LevelPlay integration validator.

### levelplay.launch_test_suite
*Type:* FUNCTION
Opens the LevelPlay integration test suite after initialization succeeds. Enable the is_test_suite metadata before init and call this before creating ad objects or invoking other LevelPlay SDK operations.

### levelplay.request_tracking_authorization
*Type:* FUNCTION
Requests App Tracking Transparency authorization on iOS 14 or newer. Request it before init when mediation partners should receive the IDFA. The result is sent through MSG_TRACKING. It is a no-op on Android and unsupported iOS versions.

### levelplay.get_tracking_authorization_status
*Type:* FUNCTION
Returns the current App Tracking Transparency state on iOS, or nil when unsupported.

**Returns**

- `number` - One of TRACKING_STATUS_NOT_DETERMINED, TRACKING_STATUS_RESTRICTED, TRACKING_STATUS_DENIED, or TRACKING_STATUS_AUTHORIZED.

### levelplay.create_interstitial_ad
*Type:* FUNCTION
Creates a reusable interstitial ad object after successful initialization. Its ad-unit ID and optional bid floor are fixed for the object's lifetime. Create it once, then use the returned handle for multiple load/show cycles with the same ad-unit ID and creation configuration.

**Parameters**

- `ad_unit_id` (string) - Interstitial ad-unit ID from the LevelPlay dashboard.
- `bid_floor` (number) - Optional minimum eCPM in USD. It applies to every load by this object; changing it requires destroying the handle and creating a new object.

**Returns**

- `number` - Positive handle, or nil when native creation is rejected.

### levelplay.destroy_interstitial_ad
*Type:* FUNCTION
Permanently releases an interstitial ad object, invalidates its handle, and stops callbacks for it. Do not destroy between ordinary impressions or during load/display when terminal callbacks are still required.

**Parameters**

- `handle` (number)

### levelplay.load_interstitial_ad
*Type:* FUNCTION
Loads the next interstitial impression into an existing object. After an impression closes, call this again on the same handle instead of creating another object.

**Parameters**

- `handle` (number)

### levelplay.is_interstitial_ad_ready
*Type:* FUNCTION
Returns whether the interstitial object has an ad ready to display.

**Parameters**

- `handle` (number)

**Returns**

- `boolean`

### levelplay.show_interstitial_ad
*Type:* FUNCTION
Shows one loaded interstitial impression. The optional placement is a dashboard presentation point, not an ad object, and can be selected separately on every show.

**Parameters**

- `handle` (number)
- `placement` (string)

### levelplay.is_interstitial_placement_capped
*Type:* FUNCTION
Returns whether the named interstitial placement has reached its configured cap.

**Parameters**

- `placement` (string)

**Returns**

- `boolean`

### levelplay.create_rewarded_ad
*Type:* FUNCTION
Creates a reusable rewarded ad object after successful initialization. Its ad-unit ID and optional bid floor are fixed for the object's lifetime. Create it once, then use the returned handle for multiple load/show cycles with the same ad-unit ID and creation configuration.

**Parameters**

- `ad_unit_id` (string) - Rewarded ad-unit ID from the LevelPlay dashboard.
- `bid_floor` (number) - Optional minimum eCPM in USD. It applies to every load by this object; changing it requires destroying the handle and creating a new object.

**Returns**

- `number` - Positive handle, or nil when native creation is rejected.

### levelplay.destroy_rewarded_ad
*Type:* FUNCTION
Permanently releases a rewarded ad object, invalidates its handle, and stops callbacks for it. Do not destroy between ordinary impressions, and never destroy a displayed rewarded ad before its reward and close callbacks are received.

**Parameters**

- `handle` (number)

### levelplay.load_rewarded_ad
*Type:* FUNCTION
Loads the next rewarded impression into an existing object. After reward and close callbacks complete, call this again on the same handle instead of creating another object.

**Parameters**

- `handle` (number)

### levelplay.is_rewarded_ad_ready
*Type:* FUNCTION
Returns whether the rewarded object has an ad ready to display.

**Parameters**

- `handle` (number)

**Returns**

- `boolean`

### levelplay.show_rewarded_ad
*Type:* FUNCTION
Shows one loaded rewarded impression. The optional placement is a dashboard presentation point, not an ad object, and can be selected separately on every show.

**Parameters**

- `handle` (number)
- `placement` (string)

### levelplay.is_rewarded_placement_capped
*Type:* FUNCTION
Returns whether the named rewarded placement has reached its configured cap.

**Parameters**

- `placement` (string)

**Returns**

- `boolean`

### levelplay.get_reward
*Type:* FUNCTION
Returns the configured reward for the object's default placement or for the supplied placement.

**Parameters**

- `handle` (number)
- `placement` (string)

**Returns**

- `table`

### levelplay.create_banner_ad
*Type:* FUNCTION
Creates a reusable banner ad view after successful initialization. Its ad-unit ID and all options are fixed for the view's lifetime. Create it once, then load, hide, show, and auto-refresh the same handle until it is permanently destroyed.

**Parameters**

- `ad_unit_id` (string) - Banner ad-unit ID from the LevelPlay dashboard.
- `options` (table) - Creation-time banner configuration. These fields apply to every load and show; changing one requires destroying the handle and creating a new banner.
  - `size` (number) - A BANNER_SIZE_* constant. Defaults to BANNER_SIZE_ADAPTIVE.
  - `position` (number) - BANNER_POSITION_TOP or BANNER_POSITION_BOTTOM. Defaults to BANNER_POSITION_BOTTOM.
  - `placement` (string) - Dashboard placement used for reporting by this banner object.
  - `bid_floor` (number) - Minimum eCPM in USD applied to every load by this banner object.
  - `respect_safe_area` (boolean) - Whether the banner avoids system bars and display cutouts. Defaults to true.

**Returns**

- `number` - Positive handle, or nil when native creation is rejected.

### levelplay.load_banner_ad
*Type:* FUNCTION
Loads and displays a banner because the native LevelPlay banner view is visible by default.

**Parameters**

- `handle` (number)

### levelplay.show_banner_ad
*Type:* FUNCTION
Makes the banner view visible.

**Parameters**

- `handle` (number)

### levelplay.hide_banner_ad
*Type:* FUNCTION
Hides the banner without destroying it.

**Parameters**

- `handle` (number)

### levelplay.pause_banner_auto_refresh
*Type:* FUNCTION
Pauses automatic refresh for the banner.

**Parameters**

- `handle` (number)

### levelplay.resume_banner_auto_refresh
*Type:* FUNCTION
Resumes automatic refresh for the banner.

**Parameters**

- `handle` (number)

### levelplay.destroy_banner_ad
*Type:* FUNCTION
Removes and destroys the banner view and invalidates its handle.

**Parameters**

- `handle` (number)

### MSG_INIT
*Type:* VARIABLE
Initialization events.

### MSG_INTERSTITIAL
*Type:* VARIABLE
Interstitial-object events.

### MSG_REWARDED
*Type:* VARIABLE
Rewarded-object events.

### MSG_BANNER
*Type:* VARIABLE
Banner-object events.

### MSG_TRACKING
*Type:* VARIABLE
App Tracking Transparency status events.

### EVENT_INIT_SUCCEEDED
*Type:* VARIABLE

### EVENT_INIT_FAILED
*Type:* VARIABLE

### EVENT_AD_LOADED
*Type:* VARIABLE

### EVENT_AD_LOAD_FAILED
*Type:* VARIABLE

### EVENT_AD_INFO_CHANGED
*Type:* VARIABLE

### EVENT_AD_DISPLAYED
*Type:* VARIABLE

### EVENT_AD_DISPLAY_FAILED
*Type:* VARIABLE

### EVENT_AD_CLICKED
*Type:* VARIABLE

### EVENT_AD_CLOSED
*Type:* VARIABLE

### EVENT_AD_REWARDED
*Type:* VARIABLE

### EVENT_AD_EXPANDED
*Type:* VARIABLE

### EVENT_AD_COLLAPSED
*Type:* VARIABLE

### EVENT_AD_LEFT_APPLICATION
*Type:* VARIABLE

### EVENT_JSON_ERROR
*Type:* VARIABLE

### TRACKING_STATUS_NOT_DETERMINED
*Type:* VARIABLE

### TRACKING_STATUS_RESTRICTED
*Type:* VARIABLE

### TRACKING_STATUS_DENIED
*Type:* VARIABLE

### TRACKING_STATUS_AUTHORIZED
*Type:* VARIABLE

### BANNER_SIZE_BANNER
*Type:* VARIABLE

### BANNER_SIZE_LARGE
*Type:* VARIABLE

### BANNER_SIZE_MEDIUM_RECTANGLE
*Type:* VARIABLE

### BANNER_SIZE_LEADERBOARD
*Type:* VARIABLE

### BANNER_SIZE_ADAPTIVE
*Type:* VARIABLE

### BANNER_POSITION_TOP
*Type:* VARIABLE

### BANNER_POSITION_BOTTOM
*Type:* VARIABLE
