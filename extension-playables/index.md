---
brief: This manual covers how to integrate and use the YouTube Playables SDK in Defold.
github: https://github.com/defold/extension-playables
layout: manual
locale: en
title: Defold YouTube Playables SDK extension API documentation
toc:
- Defold YouTube Playables SDK extension
- Installation
- Environment and SDK version
- Game lifecycle
- Load data
- Save data
- System integration
- Audio
- Pause and resume
- Language
- Engagement
- Send a score
- Open YouTube content
- Ads
- Interstitial ads
- Rewarded ads
- Health
---

# Defold YouTube Playables SDK extension

This [Defold native extension](https://defold.com/manuals/extensions/) provides Lua access to the [YouTube Playables SDK](https://developers.google.com/youtube/gaming/playables/reference/sdk).

## Installation

Add a released version of the extension to the dependencies in `game.project`:

```text
https://github.com/defold/extension-playables/archive/refs/tags/<version>.zip
```

Then select **Project → Fetch Libraries** in the Defold editor.

The extension includes the required synchronous SDK import in its HTML5 engine template:

```html
<script src="https://www.youtube.com/game_api/v1"></script>
```

## Environment and SDK version

`playables.is_in_playables_env()` returns the SDK's `IN_PLAYABLES_ENV` flag as a boolean. It returns `false` if the SDK is not loaded or the game is running outside the Playables environment.

`playables.get_sdk_version()` returns the loaded SDK's `SDK_VERSION` string, or `nil` if the SDK or its version is unavailable. Use this value for diagnostics during development.

```lua
local in_playables_env = playables.is_in_playables_env()
local sdk_version = playables.get_sdk_version()
```

Both getters are synchronous and take no arguments or callbacks. The SDK can be loaded outside the Playables environment, so `get_sdk_version()` can return a version even when `is_in_playables_env()` returns `false`.

## Game lifecycle

Call `playables.first_frame_ready()` when the game has begun showing frames. YouTube does not show the game to players until this is reported:

```lua
playables.first_frame_ready()
```

Call `playables.game_ready()` after the game has finished loading, the loading screen is no longer visible, and the player can interact with the game:

```lua
playables.game_ready()
```

This calls `ytgame.game.gameReady()` and does not return a value.

<div class='important' markdown='1'>
`playables.first_frame_ready()` must be called before `playables.game_ready()`.
</div>

## Load data

`playables.load_data(callback)` loads the game's serialized data string from YouTube. The callback receives the data and `nil` on success, or `nil` and an error message on failure:

```lua
playables.load_data(function(self, data, error)
	if error then
		print("Unable to load data:", error)
		return
	end

	print("Loaded data:", data)
end)
```

Only one `load_data()` request may be in progress at a time. The request remains in progress until its callback returns, so the callback cannot start another `load_data()` request.

## Save data

`playables.save_data(data, callback)` saves a serialized string to YouTube. The callback receives `true` and `nil` on success, or `false` and an error message on failure:

```lua
local data = json.encode({ level = 3, score = 1200 })

playables.save_data(data, function(self, success, error)
	if not success then
		print("Unable to save data:", error)
		return
	end

	print("Data saved")
end)
```

The Lua string must contain valid UTF-8 text. The bridge converts it to a well-formed UTF-16 JavaScript string for the SDK, which limits save data to 3 MiB. Invalid UTF-8 is rejected through the callback with `false` and an error message before the SDK is called. Embedded zero bytes are supported.

For binary data such as `sys.serialize()` output, Base64-encode it before saving and decode it after loading, before calling `sys.deserialize()`. The encoded text must fit within the save-data limit.

Only one `save_data()` request may be in progress at a time. The request remains in progress until its callback returns, so the callback cannot start another `save_data()` request.

## System integration

### Audio

Use `playables.is_audio_enabled()` to initialize the game's audio state, then register a handler to keep it synchronized with YouTube:

```lua
local function apply_audio_setting(enabled)
	sound.set_group_gain(hash("master"), enabled and 1 or 0)
end

apply_audio_setting(playables.is_audio_enabled())

playables.on_audio_enabled_change(function(self, enabled)
	apply_audio_setting(enabled)
end)
```

Registering another callback replaces the previous callback. Pass `nil` to unregister it:

```lua
playables.on_audio_enabled_change(nil)
```

Do not call `playables.on_audio_enabled_change()` from inside its callback. Registration, replacement, and unregistration are rejected while the callback is executing.

### Pause and resume

YouTube can pause the game when it is backgrounded or exited. A paused game is not guaranteed to resume, so save important state during the pause callback:

```lua
playables.on_pause(function(self)
	-- Pause gameplay and save important state.
end)

playables.on_resume(function(self)
	-- Resume gameplay.
end)
```

Registering another callback replaces the previous callback. Pass `nil` to the corresponding function to unregister it:

```lua
playables.on_pause(nil)
playables.on_resume(nil)
```

Do not call `playables.on_pause()` from inside its pause callback or `playables.on_resume()` from inside its resume callback. Registration, replacement, and unregistration are rejected while the corresponding callback is executing.

### Language

`playables.get_language(callback)` returns the language from the player's YouTube settings as a BCP-47 language tag:

```lua
playables.get_language(function(self, language, error)
	if error then
		print("Unable to get language:", error)
		return
	end

	print("YouTube language:", language)
end)
```

Only one `get_language()` request may be in progress at a time. The request remains in progress until its callback returns, so the callback cannot start another `get_language()` request. YouTube recommends using this value instead of another locale source or a language stored in cloud save data.

## Engagement

### Send a score

`playables.send_score(score, callback)` sends an integer score to YouTube. Use one consistent score dimension across the game; YouTube sorts scores and displays the highest value:

```lua
playables.send_score(1200, function(self, success, error)
	if not success then
		print("Unable to send score:", error)
	end
end)
```

Scores must be integers no greater than JavaScript's maximum safe integer (`9007199254740991`). Only one score request may be in progress at a time. The request remains in progress until its callback returns, so the callback cannot start another `send_score()` request.

### Open YouTube content

`playables.open_yt_content(id, [content_type], callback)` requests that YouTube open a video or another Playable:

```lua
playables.open_yt_content("VIDEO_ID", playables.CONTENT_TYPE_VIDEO, function(self, success, error)
	if not success then
		print("Unable to open video:", error)
	end
end)

playables.open_yt_content("PLAYABLE_ID", playables.CONTENT_TYPE_PLAYABLE, function(self, success, error)
	if not success then
		print("Unable to open Playable:", error)
	end
end)
```

The content type defaults to `playables.CONTENT_TYPE_VIDEO` when omitted:

```lua
playables.open_yt_content("VIDEO_ID", function(self, success, error)
end)
```

A successful callback means the request succeeded, but does not guarantee that the content opened. Only one open-content request may be in progress at a time. The request remains in progress until its callback returns, so the callback cannot start another `open_yt_content()` request.

## Ads

Before using the ads APIs, enable ads in the YouTube Playables Developer Portal as described in the [monetization requirements](https://developers.google.com/youtube/gaming/playables/certification/requirements_monetization). Continue to handle YouTube audio-setting changes, pause, and resume events during ads. An ad callback reports the request result; resume gameplay in response to `on_resume`.

### Interstitial ads

`playables.request_interstitial_ad(callback)` requests an interstitial ad. The callback receives `true, nil` on success or `false, error` on failure:

```lua
playables.request_interstitial_ad(function(self, success, error)
	if not success then
		print("Unable to request interstitial ad:", error)
	end
end)
```

A successful request does not guarantee that an ad was shown. Do not use this API to grant rewards. Only one interstitial request may be in progress at a time, including while its callback executes.

### Rewarded ads

`playables.request_rewarded_ad(reward_id, callback)` requests an ad for a particular reward type. Use a stable ID for each reward type, reuse it whenever that reward is offered, and do not include user data in the ID.

```lua
playables.request_rewarded_ad("extra_life", function(self, reward_earned, error)
	if error then
		print("Unable to request rewarded ad:", error)
	elseif reward_earned then
		-- Grant the extra life here.
	else
		-- No reward was earned.
	end
end)
```

The callback receives `true, nil` when a reward was earned, `false, nil` when no reward was earned, or `nil, error` when the request failed. Grant rewards only when `reward_earned` is `true`.

Only one rewarded request may be in progress at a time, including while its callback executes. The interstitial and rewarded request limits are tracked separately.

## Health

Use `playables.log_error()` or `playables.log_warning()` when your game detects an error or warning that should be reported to YouTube:

```lua
playables.log_error()
playables.log_warning()
```

These call `ytgame.health.logError()` and `ytgame.health.logWarning()`, respectively. Both functions take no arguments and return no value. They report an occurrence without a message or callback; use your game's own logging for diagnostic details.

The SDK reports these events on a best-effort basis and applies rate limits, so delivery is not guaranteed.
## API reference
[API Reference - playables](/extension-playables/playables_api)
