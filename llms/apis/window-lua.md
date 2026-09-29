# Window

**Namespace:** `window`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_window.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_window.cpp`

Functions and constants to access the window, window event listeners
and screen dimming.

## API

### window.DIMMING
*Type:* ENUM
Screen-dimming modes

**Members**

- `window.DIMMING_OFF` - dimming mode off Dimming mode is used to control whether or not a mobile device should dim the screen after a period without user interaction.
- `window.DIMMING_ON` - dimming mode on Dimming mode is used to control whether or not a mobile device should dim the screen after a period without user interaction.
- `window.DIMMING_UNKNOWN` - dimming mode unknown Dimming mode is used to control whether or not a mobile device should dim the screen after a period without user interaction. This mode indicates that the dim mode can't be determined, or that the platform doesn't support dimming.

### window.event_data
*Type:* STRUCT
Width and height are present for window.WINDOW_EVENT_RESIZED and
absent for other window events.

**Members**

- `width?` (integer) - Window width after a resize.
- `height?` (integer) - Window height after a resize.

### window.get_dim_mode
*Type:* FUNCTION
Returns the current dimming mode set on a mobile device.
The dimming mode specifies whether or not a mobile device should dim the screen after a period without user interaction.
On platforms that does not support dimming, window.DIMMING_UNKNOWN is always returned.

**Returns**

- `mode` (window.DIMMING) - The mode for screen dimming

### window.get_display_scale
*Type:* FUNCTION
This returns the content scale of the current display.

**Returns**

- `scale` (number) - The display scale

### window.get_mouse_lock
*Type:* FUNCTION
This returns the current lock state of the mouse cursor

**Returns**

- `state` (boolean) - The lock state

### window.get_safe_area
*Type:* FUNCTION
This returns the safe area rectangle (x, y, width, height) and the inset
values relative to the window edges. On platforms without a safe area,
this returns the full window size and zero insets.

**Returns**

- `safe_area` (window.safe_area) - safe area data

### window.get_size
*Type:* FUNCTION
This returns the current window size (width and height).

**Returns**

- `width` (integer) - The window width
- `height` (integer) - The window height

### window.safe_area
*Type:* STRUCT
Window safe-area data

**Members**

- `x` (integer) - Safe-area x-coordinate.
- `y` (integer) - Safe-area y-coordinate.
- `width` (integer) - Safe-area width.
- `height` (integer) - Safe-area height.
- `inset_left` (integer) - Inset from the left window edge.
- `inset_top` (integer) - Inset from the top window edge.
- `inset_right` (integer) - Inset from the right window edge.
- `inset_bottom` (integer) - Inset from the bottom window edge.

### window.set_dim_mode
*Type:* FUNCTION
Sets the dimming mode on a mobile device.
The dimming mode specifies whether or not a mobile device should dim the screen after a period without user interaction. The dimming mode will only affect the mobile device while the game is in focus on the device, but not when the game is running in the background.
This function has no effect on platforms that does not support dimming.

**Parameters**

- `mode` (window.DIMMING) - The mode for screen dimming

### window.set_listener
*Type:* FUNCTION
Sets a window event listener. Only one window event listener can be set at a time.

**Parameters**

- `callback` (fun(self:script_instance, event:window.WINDOW_EVENT, data:window.event_data) | nil) - A callback which receives info about window events. Pass an empty function or <code>nil</code> if you no longer wish to receive callbacks.

**Examples**

```
function window_callback(self, event, data)
    if event == window.WINDOW_EVENT_FOCUS_LOST then
        print("window.WINDOW_EVENT_FOCUS_LOST")
    elseif event == window.WINDOW_EVENT_FOCUS_GAINED then
        print("window.WINDOW_EVENT_FOCUS_GAINED")
    elseif event == window.WINDOW_EVENT_ICONIFIED then
        print("window.WINDOW_EVENT_ICONIFIED")
    elseif event == window.WINDOW_EVENT_DEICONIFIED then
        print("window.WINDOW_EVENT_DEICONIFIED")
    elseif event == window.WINDOW_EVENT_RESIZED then
        print("Window resized: ", data.width, data.height)
    end
end

function init(self)
    window.set_listener(window_callback)
end

```

### window.set_mouse_lock
*Type:* FUNCTION
Set the locking state for current mouse cursor on a PC platform.
This function locks or unlocks the mouse cursor to the center point of the window. While the cursor is locked,
mouse position updates will still be sent to the scripts as usual.

**Parameters**

- `flag` (boolean) - The lock state for the mouse cursor

### window.set_position
*Type:* FUNCTION
Sets the window position.

**Parameters**

- `x` (integer) - Horizontal position of window
- `y` (integer) - Vertical position of window

### window.set_size
*Type:* FUNCTION
Sets the window size. Works on desktop platforms only.

**Parameters**

- `width` (integer) - Width of window
- `height` (integer) - Height of window

### window.set_title
*Type:* FUNCTION
Sets the window title. Works on desktop platforms.

**Parameters**

- `title` (string) - The title, encoded as UTF-8

### window.WINDOW_EVENT
*Type:* ENUM
Window events

**Members**

- `window.WINDOW_EVENT_DEICONIFIED` - deiconified window event <span class="icon-osx"></span> <span class="icon-windows"></span> <span class="icon-linux"></span> This event is sent to a window event listener when the game window or app screen is restored after being iconified.
- `window.WINDOW_EVENT_FOCUS_GAINED` - focus gained window event This event is sent to a window event listener when the game window or app screen has gained focus. This event is also sent at game startup and the engine gives focus to the game.
- `window.WINDOW_EVENT_FOCUS_LOST` - focus lost window event This event is sent to a window event listener when the game window or app screen has lost focus.
- `window.WINDOW_EVENT_ICONIFIED` - iconify window event <span class="icon-osx"></span> <span class="icon-windows"></span> <span class="icon-linux"></span> This event is sent to a window event listener when the game window or app screen is iconified (reduced to an application icon in a toolbar, application tray or similar).
- `window.WINDOW_EVENT_RESIZED` - resized window event This event is sent to a window event listener when the game window or app screen is resized. The new size is passed along in the data field to the event listener.
