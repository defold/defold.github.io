# Window

**Namespace:** `window`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_window.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_window.cpp`

Functions and constants to access the window, window event listeners
and screen dimming.

## API

### window.DIMMING_OFF
*Type:* CONSTANT
Dimming mode is used to control whether or not a mobile device should dim the screen after a period without user interaction.

### window.DIMMING_ON
*Type:* CONSTANT
Dimming mode is used to control whether or not a mobile device should dim the screen after a period without user interaction.

### window.DIMMING_UNKNOWN
*Type:* CONSTANT
Dimming mode is used to control whether or not a mobile device should dim the screen after a period without user interaction.
This mode indicates that the dim mode can't be determined, or that the platform doesn't support dimming.

### window.get_dim_mode
*Type:* FUNCTION
Returns the current dimming mode set on a mobile device.
The dimming mode specifies whether or not a mobile device should dim the screen after a period without user interaction.
On platforms that does not support dimming, window.DIMMING_UNKNOWN is always returned.

**Returns**

- `mode` (constant) - The mode for screen dimming
<ul>
<li><code>window.DIMMING_UNKNOWN</code></li>
<li><code>window.DIMMING_ON</code></li>
<li><code>window.DIMMING_OFF</code></li>
</ul>

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

- `safe_area` (table) - safe area data
<dl>
<dt><code>safe_area</code></dt>
<dd><span class="type">table</span> table containing these keys:</dd>
</dl>
<ul>
<li><span class="type">number</span> <code>x</code></li>
<li><span class="type">number</span> <code>y</code></li>
<li><span class="type">number</span> <code>width</code></li>
<li><span class="type">number</span> <code>height</code></li>
<li><span class="type">number</span> <code>inset_left</code></li>
<li><span class="type">number</span> <code>inset_top</code></li>
<li><span class="type">number</span> <code>inset_right</code></li>
<li><span class="type">number</span> <code>inset_bottom</code></li>
</ul>

### window.get_size
*Type:* FUNCTION
This returns the current window size (width and height).

**Returns**

- `width` (number) - The window width
- `height` (number) - The window height

### window.set_dim_mode
*Type:* FUNCTION
Sets the dimming mode on a mobile device.
The dimming mode specifies whether or not a mobile device should dim the screen after a period without user interaction. The dimming mode will only affect the mobile device while the game is in focus on the device, but not when the game is running in the background.
This function has no effect on platforms that does not support dimming.

**Parameters**

- `mode` (constant) - The mode for screen dimming
<ul>
<li><code>window.DIMMING_ON</code></li>
<li><code>window.DIMMING_OFF</code></li>
</ul>

### window.set_listener
*Type:* FUNCTION
Sets a window event listener. Only one window event listener can be set at a time.

**Parameters**

- `callback` (function(self, event, data) | nil) - A callback which receives info about window events. Pass an empty function or <code>nil</code> if you no longer wish to receive callbacks.
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The calling script</dd>
<dt><code>event</code></dt>
<dd><span class="type">constant</span> The type of event. Can be one of these:</dd>
</dl>
<ul>
<li><code>window.WINDOW_EVENT_FOCUS_LOST</code></li>
<li><code>window.WINDOW_EVENT_FOCUS_GAINED</code></li>
<li><code>window.WINDOW_EVENT_RESIZED</code></li>
<li><code>window.WINDOW_EVENT_ICONIFIED</code></li>
<li><code>window.WINDOW_EVENT_DEICONIFIED</code></li>
</ul>
<dl>
<dt><code>data</code></dt>
<dd><span class="type">table</span> The callback value <code>data</code> is a table which currently holds these values</dd>
</dl>
<ul>
<li><span class="type">number</span> <code>width</code>: The width of a resize event. nil otherwise.</li>
<li><span class="type">number</span> <code>height</code>: The height of a resize event. nil otherwise.</li>
</ul>

**Examples**

```
function window_callback(self, event, data)
    if event == window.WINDOW_EVENT_FOCUS_LOST then
        print("window.WINDOW_EVENT_FOCUS_LOST")
    elseif event == window.WINDOW_EVENT_FOCUS_GAINED then
        print("window.WINDOW_EVENT_FOCUS_GAINED")
    elseif event == window.WINDOW_EVENT_ICONFIED then
        print("window.WINDOW_EVENT_ICONFIED")
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

- `x` (number) - Horizontal position of window
- `y` (number) - Vertical position of window

### window.set_size
*Type:* FUNCTION
Sets the window size. Works on desktop platforms only.

**Parameters**

- `width` (number) - Width of window
- `height` (number) - Height of window

### window.set_title
*Type:* FUNCTION
Sets the window title. Works on desktop platforms.

**Parameters**

- `title` (string) - The title, encoded as UTF-8

### window.WINDOW_EVENT_DEICONIFIED
*Type:* CONSTANT
This event is sent to a window event listener when the game window or app screen is
restored after being iconified.

### window.WINDOW_EVENT_FOCUS_GAINED
*Type:* CONSTANT
This event is sent to a window event listener when the game window or app screen has
gained focus.
This event is also sent at game startup and the engine gives focus to the game.

### window.WINDOW_EVENT_FOCUS_LOST
*Type:* CONSTANT
This event is sent to a window event listener when the game window or app screen has lost focus.

### window.WINDOW_EVENT_ICONFIED
*Type:* CONSTANT
This event is sent to a window event listener when the game window or app screen is
iconified (reduced to an application icon in a toolbar, application tray or similar).

### window.WINDOW_EVENT_RESIZED
*Type:* CONSTANT
This event is sent to a window event listener when the game window or app screen is resized.
The new size is passed along in the data field to the event listener.
