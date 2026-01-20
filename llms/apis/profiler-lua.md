# Profiler

**Namespace:** `profiler`
**Language:** Lua
**Type:** Defold Lua
**File:** `profiler.cpp`
**Source:** `engine/profiler/src/profiler.cpp`

Functions for getting profiling data in runtime.
More detailed [profiling](https://www.defold.com/manuals/profiling/) and [debugging](http://www.defold.com/manuals/debugging/) information available in the manuals.

## API

### profiler.dump_frame
*Type:* FUNCTION
logs the current frame to the console

**Examples**

```
profiler.dump_frame()

```

### profiler.enable
*Type:* FUNCTION
The profiler is a real-time tool that shows the numbers of milliseconds spent
in each scope per frame as well as counters. The profiler is very useful for
tracking down performance and resource problems.

**Parameters**

- `enabled` (boolean) - true to enable, false to disable

**Examples**

```
-- Show the profiler UI
profiler.enable(true)

```

### profiler.enable_ui
*Type:* FUNCTION
Creates and shows or hides and destroys the on-sceen profiler ui
The profiler is a real-time tool that shows the numbers of milliseconds spent
in each scope per frame as well as counters. The profiler is very useful for
tracking down performance and resource problems.

**Parameters**

- `enabled` (boolean) - true to enable, false to disable

**Examples**

```
-- Show the profiler UI
profiler.enable_ui(true)

```

### profiler.get_cpu_usage
*Type:* FUNCTION
Get the percent of CPU usage by the application, as reported by the OS.
 This function is not available on  HTML5.
For some platforms ( Android,  Linux and  Windows), this information is only available
by default in the debug version of the engine. It can be enabled in release version as well
by checking track_cpu under profiler in the game.project file.
(This means that the engine will sample the CPU usage in intervalls during execution even in release mode.)

**Returns**

- `percent` (number) - of CPU used by the application

### profiler.get_memory_usage
*Type:* FUNCTION
Get the amount of memory used (resident/working set) by the application in bytes, as reported by the OS.
 This function is not available on  HTML5.
The values are gathered from internal OS functions which correspond to the following;

OS
Value

 iOS MacOSAndroid Linux
Resident memory

 Windows
Working set

 HTML5
 Not available

**Returns**

- `bytes` (number) - used by the application

**Examples**

Get memory usage before and after loading a collection:
```
print(profiler.get_memory_usage())
msg.post("#collectionproxy", "load")
...
print(profiler.get_memory_usage()) -- will report a higher number than the initial call

```

### profiler.log_text
*Type:* FUNCTION
Send a text to the connected profiler

**Parameters**

- `text` (string) - the string to send to the connected profiler

**Examples**

```
profiler.log_text("Event: " .. name)

```

### profiler.MODE_PAUSE
*Type:* CONSTANT
pause on current frame

### profiler.MODE_RECORD
*Type:* CONSTANT
start recording

### profiler.MODE_RUN
*Type:* CONSTANT
continously show latest frame

### profiler.MODE_SHOW_PEAK_FRAME
*Type:* CONSTANT
pause at peak frame

### profiler.recorded_frame_count
*Type:* FUNCTION
Get the number of recorded frames in the on-screen profiler ui recording buffer

**Returns**

- `frame_count` (number) - the number of recorded frames, zero if on-screen profiler is disabled

**Examples**

```
-- Show the last recorded frame
local recorded_frame_count = profiler.recorded_frame_count()
profiler.view_recorded_frame(recorded_frame_count)

```

### profiler.scope_begin
*Type:* FUNCTION
Starts a profile scope.

**Notes**

- Must be correctly matched with a corresponding call to `profiler.scope_end()`

**Parameters**

- `name` (string) - The name of the scope

**Examples**

```
-- Go back one frame
profiler.scope_begin("test_function")
  test_function()
profiler.scope_end()

```

### profiler.scope_end
*Type:* FUNCTION
End the current profile scope.

### profiler.set_ui_mode
*Type:* FUNCTION
Set the on-screen profile mode - run, pause, record or show peak frame

**Parameters**

- `mode` (constant) - the mode to set the ui profiler in
<ul>
<li><code>profiler.MODE_RUN</code> This is default mode that continously shows the last frame</li>
<li><code>profiler.MODE_PAUSE</code> Pauses on the currently displayed frame</li>
<li><code>profiler.MODE_SHOW_PEAK_FRAME</code> Pauses on the currently displayed frame but shows a new frame if that frame is slower</li>
<li><code>profiler.MODE_RECORD</code> Records all incoming frames to the recording buffer</li>
</ul>
To stop recording, switch to a different mode such as <code>MODE_PAUSE</code> or <code>MODE_RUN</code>.
You can also use the <code>view_recorded_frame</code> function to display a recorded frame. Doing so stops the recording as well.
Every time you switch to recording mode the recording buffer is cleared.

**Examples**

```
function start_recording()
     profiler.set_ui_mode(profiler.MODE_RECORD)
end

function stop_recording()
     profiler.set_ui_mode(profiler.MODE_PAUSE)
end

```

### profiler.set_ui_view_mode
*Type:* FUNCTION
Set the on-screen profile view mode - minimized or expanded

**Parameters**

- `mode` (constant) - the view mode to set the ui profiler in
<ul>
<li><code>profiler.VIEW_MODE_FULL</code> The default mode which displays all the ui profiler details</li>
<li><code>profiler.VIEW_MODE_MINIMIZED</code> Minimized mode which only shows the top header (fps counters and ui profiler mode)</li>
</ul>

**Examples**

```
-- Minimize the profiler view
profiler.set_ui_view_mode(profiler.VIEW_MODE_MINIMIZED)

```

### profiler.set_ui_vsync_wait_visible
*Type:* FUNCTION
Shows or hides the time the engine waits for vsync in the on-screen profiler
Each frame the engine waits for vsync and depending on your vsync settings and how much time
your game logic takes this time can dwarf the time in the game logic making it hard to
see details in the on-screen profiler graph and lists.
Also, by hiding this the FPS times in the header show the time spent each time excuding the
time spent waiting for vsync. This shows you how long time your game is spending actively
working each frame.
This setting also effects the display of recorded frames but does not affect the actual
recorded frames so it is possible to toggle this on and off when viewing recorded frames.
By default the vsync wait times is displayed in the profiler.

**Parameters**

- `visible` (boolean) - true to include it in the display, false to hide it.

**Examples**

```
-- Exclude frame wait time form the profiler ui
profiler.set_ui_vsync_wait_visible(false)

```

### profiler.VIEW_MODE_FULL
*Type:* CONSTANT
show full profiler ui

### profiler.VIEW_MODE_MINIMIZED
*Type:* CONSTANT
show mimimal profiler ui

### profiler.view_recorded_frame
*Type:* FUNCTION
Pauses and displays a frame from the recording buffer in the on-screen profiler ui
The frame to show can either be an absolute frame or a relative frame to the current frame.

**Parameters**

- `frame_index` (table) - a table where you specify one of the following parameters:
<ul>
<li><code>distance</code> The offset from the currently displayed frame (this is truncated between zero and the number of recorded frames)</li>
<li><code>frame</code> The frame index in the recording buffer (1 is first recorded frame)</li>
</ul>

**Examples**

```
-- Go back one frame
profiler.view_recorded_frame({distance = -1})

```
