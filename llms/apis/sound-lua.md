# Sound

**Namespace:** `sound`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_sound.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_sound.cpp`

Functions and messages for controlling sound components and
mixer groups.

## API

### gain
*Type:* PROPERTY
The gain on the sound-component. Note that gain is in linear scale,
between 0 and 1.

**Examples**

```
function init(self)
  local gain = go.get("#sound", "gain")
  go.set("#sound", "gain", gain * 1.5)
end

```

### pan
*Type:* PROPERTY
The pan on the sound-component. The valid range is from -1.0 to 1.0,
representing -45 degrees left, to +45 degrees right.

**Examples**

```
function init(self)
  local pan = go.get("#sound", "pan")
  go.set("#sound", "pan", pan * -1)
end

```

### play_sound
*Type:* MESSAGE
Post this message to a sound-component to make it play its sound. Multiple voices is supported. The limit is set to 32 voices per sound component.
 Note that gain is in linear scale, between 0 and 1.
To get the dB value from the gain, use the formula 20 * log(gain).
Inversely, to find the linear value from a dB value, use the formula
10db/20.
 A sound will continue to play even if the game object the sound component belonged to is deleted. You can send a stop_sound to stop the sound.
 play_id should be specified in case you want to receive sound_done or sound_stopped in on_message().

**Parameters**

- `delay` (number) (optional) - delay in seconds before the sound starts playing, default is 0.
- `gain` (number) (optional) - sound gain between 0 and 1, default is 1.
- `play_id` (number) (optional) - the identifier of the sound, can be used to distinguish between consecutive plays from the same component.
- `start_time` (number) (optional) - optional start offset (seconds). Mutually exclusive with <code>start_frame</code>.
- `start_frame` (number) (optional) - optional start offset (frames). If both are provided, <code>start_frame</code> is used.

**Examples**

Assuming the script belongs to an instance with a sound-component with id "sound", this will make the component play its sound after 1 second:
```
msg.post("#sound", "play_sound", {delay = 1, gain = 0.5})

```

```
-- use `play_id` and `msg.post()` if you want to recieve `sound_done` or `sound_stopped` in on_message()
function init()
 msg.post("#sound", "play_sound", {play_id = 1, delay = 1, gain = 0.5})
end

function on_message(self, message_id, message)
 if message_id == hash("sound_done") then
     print("Sound play id: "..message.play_id)
 end
end

```

### set_gain
*Type:* MESSAGE
Post this message to a sound-component to set gain on all active playing voices.
 Note that gain is in linear scale, between 0 and 1.
To get the dB value from the gain, use the formula 20 * log(gain).
Inversely, to find the linear value from a dB value, use the formula
10db/20.

**Parameters**

- `gain` (number) (optional) - sound gain between 0 and 1, default is 1.

**Examples**

Assuming the script belongs to an instance with a sound-component with id "sound", this will set the gain to 0.5
```
msg.post("#sound", "set_gain", {gain = 0.5})

```

### sound
*Type:* PROPERTY
The sound data used when playing the sound. The type of the property is hash.

**Examples**

How to change the sound:
```
function init(self)
  -- load a wav file bundled as a custom resource
  local wav = sys.load_resource("foo.wav")
  -- get resource path to the sound component
  local resource_path = go.get("#sound", "sound")
  -- update the resource with the loaded wav file
  resource.set_sound(resource_path, wav)
  -- play the updated sound
  sound.play("#sound")
end

```

### sound.get_group_gain
*Type:* FUNCTION
Get mixer group gain

**Parameters**

- `group` (string | hash) - group name

**Returns**

- `gain` (number) - gain in [0 1] range ([-60dB.. 0dB])

**Examples**

Get the mixer group gain for the "soundfx" and convert to dB:
```
local gain = sound.get_group_gain("soundfx")
local gain_db = 60 * gain

```

### sound.get_group_name
*Type:* FUNCTION
Get a mixer group name as a string.
 This function is to be used for debugging and
development tooling only. The function does a reverse hash lookup, which does not
return a proper string value when the game is built in release mode.

**Parameters**

- `group` (string | hash) - group name

**Returns**

- `name` (string) - group name

**Examples**

Get the mixer group string names so we can show them as labels on a dev mixer overlay:
```
local groups = sound.get_groups()
for _,group in ipairs(groups) do
    local name = sound.get_group_name(group)
    msg.post("/mixer_overlay#gui", "set_mixer_label", { group = group, label = name})
end

```

### sound.get_groups
*Type:* FUNCTION
Get a table of all mixer group names (hashes).

**Returns**

- `groups` (table) - table of mixer group names

**Examples**

Get the mixer groups, set all gains to 0 except for "master" and "soundfx"
where gain is set to 1:
```
local groups = sound.get_groups()
for _,group in ipairs(groups) do
    if group == hash("master") or group == hash("soundfx") then
        sound.set_group_gain(group, 1)
    else
        sound.set_group_gain(group, 0)
    end
end

```

### sound.get_peak
*Type:* FUNCTION
Get peak value from mixer group.
 Note that gain is in linear scale, between 0 and 1.
To get the dB value from the gain, use the formula 20 * log(gain).
Inversely, to find the linear value from a dB value, use the formula
10db/20.
Also note that the returned value might be an approximation and in particular
the effective window might be larger than specified.

**Parameters**

- `group` (string | hash) - group name
- `window` (number) - window length in seconds

**Returns**

- `peak_l` (number) - peak value for left channel
- `peak_r` (number) - peak value for right channel

**Examples**

Get the peak gain from the "master" group and convert to dB for displaying:
```
local left_p, right_p = sound.get_peak("master", 0.1)
left_p_db = 20 * log(left_p)
right_p_db = 20 * log(right_p)

```

### sound.get_rms
*Type:* FUNCTION
Get RMS (Root Mean Square) value from mixer group. This value is the
square root of the mean (average) value of the squared function of
the instantaneous values.
For instance: for a sinewave signal with a peak gain of -1.94 dB (0.8 linear),
the RMS is 0.8 × 1/sqrt(2) which is about 0.566.
 Note the returned value might be an approximation and in particular
the effective window might be larger than specified.

**Parameters**

- `group` (string | hash) - group name
- `window` (number) - window length in seconds

**Returns**

- `rms_l` (number) - RMS value for left channel
- `rms_r` (number) - RMS value for right channel

**Examples**

Get the RMS from the "master" group where a mono -1.94 dB sinewave is playing:
```
local rms = sound.get_rms("master", 0.1) -- throw away right channel.
print(rms) --> 0.56555819511414

```

### sound.is_music_playing
*Type:* FUNCTION
Checks if background music is playing, e.g. from iTunes.
 On non mobile platforms,
this function always return false.
 On Android you can only get a correct reading
of this state if your game is not playing any sounds itself. This is a limitation
in the Android SDK. If your game is playing any sounds, even with a gain of zero, this
function will return false.
The best time to call this function is:

In the init function of your main collection script before any sounds are triggered
In a window listener callback when the window.WINDOW_EVENT_FOCUS_GAINED event is received

Both those times will give you a correct reading of the state even when your application is
swapped out and in while playing sounds and it works equally well on Android and iOS.

**Returns**

- `playing` (boolean) - <code>true</code> if music is playing, otherwise <code>false</code>.

**Examples**

If music is playing, mute "master":
```
if sound.is_music_playing() then
    -- mute "master"
    sound.set_group_gain("master", 0)
end

```

### sound.is_phone_call_active
*Type:* FUNCTION
Checks if a phone call is active. If there is an active phone call all
other sounds will be muted until the phone call is finished.
 On non mobile platforms,
this function always return false.

**Returns**

- `call_active` (boolean) - <code>true</code> if there is an active phone call, <code>false</code> otherwise.

**Examples**

Test if a phone call is on-going:
```
if sound.is_phone_call_active() then
    -- do something sensible.
end

```

### sound.pause
*Type:* FUNCTION
Pause all active voices

**Parameters**

- `url` (string | hash | url) - the sound that should pause
- `pause` (boolean) - true if the sound should pause

**Examples**

Assuming the script belongs to an instance with a sound-component with id "sound", this will make the component pause all playing voices:
```
sound.pause("#sound", true)

```

### sound.play
*Type:* FUNCTION
Make the sound component play its sound. Multiple voices are supported. The limit is set to 32 voices per sound component.
 A sound will continue to play even if the game object the sound component belonged to is deleted. You can call sound.stop() to stop the sound.

**Notes**

- Sounds are panned using a constant power panning (non linear fade). 0 means left/right channels are balanced at 71%/71% each.
At -1 (full left) the channels are at 100%/0%, and 1 they're at 0%/100%.

**Parameters**

- `url` (string | hash | url) - the sound that should play
- `play_properties` (table) (optional) - <dl>
<dt>optional table with properties:</dt>
<dt><code>delay</code></dt>
<dd><span class="type">number</span> delay in seconds before the sound starts playing, default is 0.</dd>
<dt><code>gain</code></dt>
<dd><span class="type">number</span> sound gain between 0 and 1, default is 1. The final gain of the sound will be a combination of this gain, the group gain and the master gain.</dd>
<dt><code>pan</code></dt>
<dd><span class="type">number</span> sound pan between -1 and 1, default is 0. The final pan of the sound will be an addition of this pan and the sound pan.</dd>
<dt><code>speed</code></dt>
<dd><span class="type">number</span> sound speed where 1.0 is normal speed, 0.5 is half speed and 2.0 is double speed. The final speed of the sound will be a multiplication of this speed and the sound speed.</dd>
<dt><code>start_time</code></dt>
<dd><span class="type">number</span> start playback offset (seconds). Optional, mutually exclusive with <code>start_frame</code>.</dd>
<dt><code>start_frame</code></dt>
<dd><span class="type">number</span> start playback offset (frames/samples). Optional, mutually exclusive with <code>start_time</code>. If both are provided, <code>start_frame</code> is used.</dd>
</dl>
- `complete_function` (function(self, message_id, message, sender)) (optional) - function to call when the sound has finished playing or stopped manually via <a href="/ref/sound#sound.stop">sound.stop</a>.
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The current object.</dd>
<dt><code>message_id</code></dt>
<dd><span class="type">hash</span> The name of the completion message, which can be either <code>"sound_done"</code> if the sound has finished playing, or <code>"sound_stopped"</code> if it was stopped manually.</dd>
<dt><code>message</code></dt>
<dd><span class="type">table</span> Information about the completion:</dd>
</dl>
<ul>
<li><span class="type">number</span> <code>play_id</code> - the sequential play identifier that was given by the sound.play function.</li>
</ul>
<dl>
<dt><code>sender</code></dt>
<dd><span class="type">url</span> The invoker of the callback: the sound component.</dd>
</dl>

**Returns**

- `play_id` (number) - The identifier for the sound voice

**Examples**

Assuming the script belongs to an instance with a sound-component with id "sound", this will make the component play its sound after 1 second:
```
sound.play("#sound", { delay = 1, gain = 0.9, pan = -1.0 } )

```

Using the callback argument, you can chain several sounds together:
```
local function sound_done(self, message_id, message, sender)
  -- play 'boom' sound fx when the countdown has completed
  if message_id == hash("sound_done") and message.play_id == self.countdown_id then
    sound.play("#boom", nil, sound_done)
  end
end

function init(self)
  self.countdown_id = sound.play("#countdown", nil, sound_done)
end

```

### sound.set_gain
*Type:* FUNCTION
Set gain on all active playing voices of a sound.

**Parameters**

- `url` (string | hash | url) - the sound to set the gain of
- `gain` (number) (optional) - sound gain between 0 and 1 [-60dB .. 0dB]. The final gain of the sound will be a combination of this gain, the group gain and the master gain.

**Examples**

Assuming the script belongs to an instance with a sound-component with id "sound", this will set the gain to 0.9
```
sound.set_gain("#sound", 0.9)

```

### sound.set_group_gain
*Type:* FUNCTION
Set mixer group gain

**Parameters**

- `group` (string | hash) - group name
- `gain` (number) - gain in range [0..1] mapped to [0 .. -60dB]

**Examples**

Set mixer group gain on the "soundfx" group to 50% (-30dB):
```
sound.set_group_gain("soundfx", 0.5)

```

### sound.set_pan
*Type:* FUNCTION
Set panning on all active playing voices of a sound.
The valid range is from -1.0 to 1.0, representing -45 degrees left, to +45 degrees right.

**Notes**

- Sounds are panned using a constant power panning (non linear fade). 0 means left/right channels are balanced at 71%/71% each.
At -1 (full left) the channels are at 100%/0%, and 1 they're at 0%/100%.

**Parameters**

- `url` (string | hash | url) - the sound to set the panning value to
- `pan` (number) (optional) - sound panning between -1.0 and 1.0

**Examples**

Assuming the script belongs to an instance with a sound-component with id "sound", this will set the gain to 0.5
```
sound.set_pan("#sound", 0.5) -- pan to the right

```

### sound.stop
*Type:* FUNCTION
Stop playing all active voices or just one voice if play_id provided

**Parameters**

- `url` (string | hash | url) - the sound component that should stop
- `stop_properties` (table) (optional) - <dl>
<dt>optional table with properties:</dt>
<dt><code>play_id</code></dt>
<dd><span class="type">number</span> the sequential play identifier that should be stopped (was given by the sound.play() function)</dd>
</dl>

**Examples**

Assuming the script belongs to an instance with a sound-component with id "sound", this will make the component stop all playing voices:
```
sound.stop("#sound")
local id = sound.play("#sound")
sound.stop("#sound", {play_id = id})

```

### sound_done
*Type:* MESSAGE
This message is sent back to the sender of a play_sound message
if the sound could be played to completion and a play_id was provided with the play_sound message.

**Parameters**

- `play_id` (number) (optional) - id number supplied when the message was posted.

### sound_stopped
*Type:* MESSAGE
This message is sent back to the sender of a play_sound message, if the sound
has been manually stopped and a play_id was provided with the play_sound message.

**Parameters**

- `play_id` (number) (optional) - id number supplied when the message was posted.

### speed
*Type:* PROPERTY
The speed on the sound-component where 1.0 is normal speed, 0.5 is half
speed and 2.0 is double speed.

**Examples**

```
function init(self)
  local speed = go.get("#sound", "speed")
  go.set("#sound", "speed", speed * 0.5)
end

```

### stop_sound
*Type:* MESSAGE
Post this message to a sound-component to make it stop playing all active voices

**Examples**

Assuming the script belongs to an instance with a sound-component with id "sound", this will make the component stop all playing voices:
```
msg.post("#sound", "stop_sound")

```
