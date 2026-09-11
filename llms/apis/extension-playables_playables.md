# extension-playables

**Namespace:** `playables`
**Language:** Lua
**Type:** Extension

Functions for interacting with the YouTube Playables SDK.

## API

### playables.is_in_playables_env
*Type:* FUNCTION
Returns whether the SDK reports that the game is running in the Playables environment. Returns false if the SDK is not loaded.

**Returns**

- `boolean` - True when the SDK is loaded and IN_PLAYABLES_ENV is true, otherwise false.

### playables.get_sdk_version
*Type:* FUNCTION
Returns the loaded YouTube Playables SDK version, or nil if it is unavailable.

**Returns**

- `['string', 'nil']` - The value of SDK_VERSION, or nil if the SDK or its version is unavailable.

### playables.first_frame_ready
*Type:* FUNCTION
Notifies YouTube that the game has begun showing frames. This must be called before game_ready().

### playables.game_ready
*Type:* FUNCTION
Notifies YouTube that the loading screen is gone and the game is ready for players to interact with. YouTube requires firstFrameReady() to be called before this function.

### playables.load_data
*Type:* FUNCTION
Loads serialized game data from YouTube. Only one load request may be in progress at a time. The request remains in progress until its callback returns, so the callback cannot start another load_data() request.

**Parameters**

- `callback` (function)
  - `self` (object) - The calling script instance.
  - `data` (string | nil) - The serialized game data on success, otherwise nil.
  - `error` (string | nil) - The SDK error message on failure, otherwise nil.

### playables.save_data
*Type:* FUNCTION
Saves valid UTF-8 text to YouTube, with a maximum size of 3 MiB. Invalid UTF-8 returns false and an error through the callback before the SDK is called. Base64-encode binary data such as sys.serialize() output before saving. Only one save request may be in progress at a time. The request remains in progress until its callback returns, so the callback cannot start another save_data() request.

**Parameters**

- `data` (string) - The serialized game data as valid UTF-8 text. Embedded zero bytes are supported.
- `callback` (function)
  - `self` (object) - The calling script instance.
  - `success` (boolean) - True when the save completed successfully.
  - `error` (string | nil) - The UTF-8 decoding or SDK error message on failure, otherwise nil.

### playables.is_audio_enabled
*Type:* FUNCTION
Returns whether game audio is enabled in the player's YouTube settings. Use this to initialize the game audio state.

**Returns**

- `boolean` - True when game audio is enabled.

### playables.on_audio_enabled_change
*Type:* FUNCTION
Registers a callback for YouTube audio-setting changes. A new callback replaces the previous one. Pass nil to unregister it. This function cannot be called from its own callback.

**Parameters**

- `callback` (function | nil) - The event callback, or nil to unregister the current callback.
  - `self` (object) - The calling script instance.
  - `is_audio_enabled` (boolean) - True when game audio should be enabled.

### playables.on_pause
*Type:* FUNCTION
Registers a callback for YouTube pause events. A new callback replaces the previous one. Pass nil to unregister it. This function cannot be called from its own callback. A paused game is not guaranteed to resume.

**Parameters**

- `callback` (function | nil) - The event callback, or nil to unregister the current callback.
  - `self` (object) - The calling script instance.

### playables.on_resume
*Type:* FUNCTION
Registers a callback for YouTube resume events. A new callback replaces the previous one. Pass nil to unregister it. This function cannot be called from its own callback.

**Parameters**

- `callback` (function | nil) - The event callback, or nil to unregister the current callback.
  - `self` (object) - The calling script instance.

### playables.get_language
*Type:* FUNCTION
Gets the language in the player's YouTube settings as a BCP-47 language tag. Only one request may be in progress at a time. The request remains in progress until its callback returns, so the callback cannot start another get_language() request.

**Parameters**

- `callback` (function)
  - `self` (object) - The calling script instance.
  - `language` (string | nil) - The BCP-47 language tag on success, otherwise nil.
  - `error` (string | nil) - The SDK error message on failure, otherwise nil.

### playables.send_score
*Type:* FUNCTION
Sends an integer score to YouTube. Use one consistent score dimension across the game. Only one request may be in progress at a time. The request remains in progress until its callback returns, so the callback cannot start another send_score() request.

**Parameters**

- `score` (number) - An integer no greater than JavaScript's maximum safe integer.
- `callback` (function)
  - `self` (object) - The calling script instance.
  - `success` (boolean) - True when the request succeeded.
  - `error` (string | nil) - The SDK error message on failure, otherwise nil.

### playables.open_yt_content
*Type:* FUNCTION
Requests that YouTube open a video or another Playable. The content type is optional and defaults to CONTENT_TYPE_VIDEO. Only one request may be in progress at a time. The request remains in progress until its callback returns, so the callback cannot start another open_yt_content() request.

**Parameters**

- `content_id` (string) - The YouTube video or Playable ID.
- `content_type` (number) - CONTENT_TYPE_VIDEO or CONTENT_TYPE_PLAYABLE.
- `callback` (function)
  - `self` (object) - The calling script instance.
  - `success` (boolean) - True when the request succeeded. This does not guarantee that the content opened.
  - `error` (string | nil) - The SDK error message on failure, otherwise nil.

### playables.request_interstitial_ad
*Type:* FUNCTION
Requests an interstitial ad. Success does not guarantee that an ad was shown. Do not use this API to grant rewards. Only one interstitial request may be in progress at a time. The request remains in progress until its callback returns, so the callback cannot start another request_interstitial_ad() request. Keep handling YouTube audio, pause, and resume events during ads.

**Parameters**

- `callback` (function)
  - `self` (object) - The calling script instance.
  - `success` (boolean) - True when the request succeeded. This does not guarantee that an ad was shown.
  - `error` (string | nil) - The SDK error message on failure, otherwise nil.

### playables.request_rewarded_ad
*Type:* FUNCTION
Requests a rewarded ad. Grant a reward only when reward_earned is true. Only one rewarded request may be in progress at a time. The request remains in progress until its callback returns, so the callback cannot start another request_rewarded_ad() request. Keep handling YouTube audio, pause, and resume events during ads.

**Parameters**

- `reward_id` (string) - A stable ID unique to the reward type. Reuse it for each offer of that reward and do not include user data.
- `callback` (function)
  - `self` (object) - The calling script instance.
  - `reward_earned` (boolean | nil) - True if a reward was earned, false if no reward was earned, or nil if the request failed.
  - `error` (string | nil) - The SDK error message on failure, otherwise nil.

### playables.log_error
*Type:* FUNCTION
Reports an error occurrence to YouTube. Takes no arguments and returns no value. Reporting is best-effort and rate-limited, so delivery is not guaranteed.

### playables.log_warning
*Type:* FUNCTION
Reports a warning occurrence to YouTube. Takes no arguments and returns no value. Reporting is best-effort and rate-limited, so delivery is not guaranteed.

### CONTENT_TYPE_VIDEO
*Type:* VARIABLE
Opens a YouTube video.

### CONTENT_TYPE_PLAYABLE
*Type:* VARIABLE
Opens another YouTube Playable.
