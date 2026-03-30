# Sound

**Namespace:** `dmSound`
**Language:** C++
**Type:** Defold C++
**File:** `sound.h`
**Source:** `engine/sound/src/dmsdk/sound/sound.h`
**Include:** `dmsdk/sound/sound.h`

Functions for controlling the engine sound mixer from native extensions.

## API

### IsGroupMuted
*Type:* FUNCTION
Query group mute state

**Parameters**

- `group` (dmhash_t) - hash of the mixer group (e.g. <code>hash("master")</code>)

**Returns**

- `muted` (bool) - <code>true</code> if the mixer group is muted

### Result
*Type:* ENUM

**Members**

- `RESULT_OK`
- `RESULT_PARTIAL_DATA`
- `RESULT_OUT_OF_SOURCES`
- `RESULT_EFFECT_NOT_FOUND`
- `RESULT_OUT_OF_INSTANCES`
- `RESULT_RESOURCE_LEAK`
- `RESULT_OUT_OF_BUFFERS`
- `RESULT_INVALID_PROPERTY`
- `RESULT_UNKNOWN_SOUND_TYPE`
- `RESULT_INVALID_STREAM_DATA`
- `RESULT_OUT_OF_MEMORY`
- `RESULT_UNSUPPORTED`
- `RESULT_DEVICE_NOT_FOUND`
- `RESULT_OUT_OF_GROUPS`
- `RESULT_NO_SUCH_GROUP`
- `RESULT_NOTHING_TO_PLAY`
- `RESULT_INIT_ERROR`
- `RESULT_FINI_ERROR`
- `RESULT_NO_DATA`
- `RESULT_END_OF_STREAM`
- `RESULT_DEVICE_LOST`
- `RESULT_UNKNOWN_ERROR`

### SetGroupMute
*Type:* FUNCTION
Temporarily mute or restore an individual mixer group.

**Parameters**

- `group` (dmhash_t) - hash of the mixer group (e.g. <code>hash("master")</code>)
- `mute` (bool) - <code>true</code> to mute, <code>false</code> to restore audio

**Returns**

- `result` (Result) - RESULT_OK on success

### ToggleGroupMute
*Type:* FUNCTION
Convenience toggle for SetGroupMute.

**Parameters**

- `group` (dmhash_t) - hash of the mixer group (e.g. <code>hash("master")</code>)

**Returns**

- `result` (Result) - RESULT_OK on success
