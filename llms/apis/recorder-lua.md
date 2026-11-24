# Video recording

**Namespace:** `recorder`
**Language:** Lua
**Type:** Defold Lua
**File:** `record_script_extension.cpp`
**Source:** `engine/record/src/record/record_script_extension.cpp`

Record the game window to an MP4 file. One recording may run at a time,
shared with the engine's HTTP recording service.

Recording is supported by desktop debug engines. The module is omitted from
release, headless, mobile and web builds, and when recording is excluded through
an app manifest. Unsupported desktop operating systems or capture environments
return an error from [ref:recorder.start].
Application audio support depends on the platform; audio is disabled by default.

## API

### recorder.EVENT
*Type:* ENUM
recording events

**Members**

- `recorder.EVENT_STARTED` - Recording has started.
- `recorder.EVENT_STOPPED` - Recording has stopped and the MP4 is ready to read.
- `recorder.EVENT_ERROR` - Recording failed; result.error contains the reason.

### recorder.options
*Type:* STRUCT
recording options

**Members**

- `path` (string) - Writable MP4 output path, for example from <a href="/ref/sys#sys.get_save_file">sys.get_save_file</a>. Uses the host path encoding (Windows ANSI code page; UTF-8 elsewhere). The parent directory must exist.
- `fps?` (integer) - Capture rate from 1 to 60; defaults to 30.
- `audio?` (boolean) - Record application audio; defaults to false.

### recorder.result
*Type:* STRUCT
recording event result

**Members**

- `path` (string) - Output file path, preserving the path supplied to <a href="/ref/recorder#recorder.start">recorder.start</a>.
- `width` (integer) - Recorded video width in pixels.
- `height` (integer) - Recorded video height in pixels.
- `fps` (integer) - Capture rate.
- `audio` (boolean) - Whether application audio is included.
- `error?` (string) - Failure reason, present for <a href="/ref/recorder#recorder.EVENT_ERROR">recorder.EVENT_ERROR</a>.

### recorder.start
*Type:* FUNCTION
Starts an asynchronous recording of the game window at its native pixel size.
The caller owns the output file, which remains on disk after engine shutdown.
An existing file at the specified path may be overwritten.
A successful return only means the request was accepted. The callback receives
recorder.EVENT_STARTED when capture starts, followed by
recorder.EVENT_STOPPED or recorder.EVENT_ERROR. Startup failure produces
only EVENT_ERROR. Callbacks run during engine update, never inside start/stop.
Window resizing stops and finalizes the recording. Deleting the calling script
discards its callback but does not stop recording. Engine shutdown finalizes
recording without invoking callbacks.

**Parameters**

- `options` (recorder.options) - recording options
- `callback` (fun(self:script_instance, event:recorder.EVENT, result:recorder.result)) - recording event callback

**Returns**

- `accepted` (boolean | nil) - true if accepted, otherwise nil
- `error` (string | nil) - reason the request was rejected

**Examples**

```
local ok, err = recorder.start({
    path = sys.get_save_file("my_game", "capture.mp4"),
    fps = 30,
    audio = false,
}, function(self, event, result)
    if event == recorder.EVENT_STOPPED then
        print("Saved:", result.path)
    elseif event == recorder.EVENT_ERROR then
        print(result.error)
    end
end)
if not ok then print(err) end

```

### recorder.stop
*Type:* FUNCTION
Requests finalization of the current recording, including one started through
HTTP. Wait for recorder.EVENT_STARTED before calling stop for a Lua recording.
The original start callback receives recorder.EVENT_STOPPED only after the
MP4 is finalized and ready to read, or recorder.EVENT_ERROR on failure.
Returns an error if no recording is active or an operation is pending.

**Returns**

- `accepted` (boolean | nil) - true if accepted, otherwise nil
- `error` (string | nil) - reason the request was rejected
