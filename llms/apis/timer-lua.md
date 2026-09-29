# Timer

**Namespace:** `timer`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_timer.cpp`
**Source:** `engine/script/src/script_timer.cpp`

Timers allow you to set a delay and a callback to be called when the timer completes.

The timers created with this API are updated with the collection timer where they
are created. If you pause or speed up the collection (using `set_time_step`) it will
also affect the new timer.

## API

### timer.cancel
*Type:* FUNCTION
You may cancel a timer from inside a timer callback.
Cancelling a timer that is already executed or cancelled is safe.

**Parameters**

- `handle` (timer_handle) - the timer handle returned by timer.delay()

**Returns**

- `cancelled` (boolean) - <code>true</code> if the timer was active and cancelled, <code>false</code> if the timer was already cancelled or complete

**Examples**

```
self.handle = timer.delay(1, true, function() print("print every second") end)
...
local cancelled = timer.cancel(self.handle)
if not cancelled then
   print("the timer is already cancelled")
end

```

### timer.delay
*Type:* FUNCTION
Adds a timer and returns a unique handle.
You may create more timers from inside a timer callback.
Using a delay of 0 will result in a timer that triggers at the next frame just before
script update functions.
If you want a timer that triggers on each frame, set delay to 0.0f and repeat to true.
Timers created within a script will automatically die when the script is deleted.

**Parameters**

- `delay` (number) - time interval in seconds
- `repeating` (boolean) - true = repeat timer until cancel, false = one-shot timer
- `callback` (fun(self:script_instance, handle:timer_handle, time_elapsed:number)) - timer callback function
<dl>
<dt class="api-lua-v2-type-definition"><code>self:<a href="../builtins-lua/#script_instance">script_instance</a></code></dt>
<dd>The current script instance</dd>
<dt class="api-lua-v2-type-definition"><code>handle:<a href="#timer_handle">timer_handle</a></code></dt>
<dd>The handle of the timer</dd>
<dt class="api-lua-v2-type-definition"><code>time_elapsed:<a href="../../../manuals/lua/#variables-and-data-types">number</a></code></dt>
<dd>The elapsed time - on first trigger it is time since timer.delay call, otherwise time since last trigger</dd>
</dl>

**Returns**

- `handle` (timer_handle) - identifier for the create timer, returns timer.INVALID_TIMER_HANDLE if the timer can not be created

**Examples**

A simple one-shot timer
```
timer.delay(1, false, function() print("print in one second") end)

```

Repetitive timer which canceled after 10 calls
```
local function call_every_second(self, handle, time_elapsed)
  self.counter = self.counter + 1
  print("Call #", self.counter)
  if self.counter == 10 then
    timer.cancel(handle) -- cancel timer after 10 calls
  end
end

self.counter = 0
timer.delay(1, true, call_every_second)

```

### timer.get_info
*Type:* FUNCTION
Get information about timer.

**Parameters**

- `handle` (timer_handle) - the timer handle returned by timer.delay()

**Returns**

- `data` (timer.info | nil) - timer information, or <code>nil</code> if the timer is cancelled or complete

**Examples**

```
self.handle = timer.delay(1, true, function() print("print every second") end)
...
local result = timer.get_info(self.handle)
if not result then
   print("the timer is already cancelled or complete")
else
   pprint(result) -- delay, time_remaining, repeating
end

```

### timer.info
*Type:* STRUCT
Timer information

**Members**

- `time_remaining` (number) - Time remaining until the next callback.
- `delay` (number) - Timer interval.
- `repeating` (boolean) - Whether the timer repeats until cancelled.

### timer.INVALID_TIMER_HANDLE
*Type:* CONSTANT
Indicates an invalid timer handle

**Parameters**

- `value` (timer_handle)

### timer.trigger
*Type:* FUNCTION
Manual triggering a callback for a timer.

**Parameters**

- `handle` (timer_handle) - the timer handle returned by timer.delay()

**Returns**

- `triggered` (boolean) - <code>true</code> if the timer was active and triggered, <code>false</code> if the timer was already cancelled or complete

**Examples**

```
self.handle = timer.delay(1, true, function() print("print every second or manually by timer.trigger") end)
...
local triggered = timer.trigger(self.handle)
if not triggered then
   print("the timer is already cancelled or complete")
end

```

### timer_handle
*Type:* TYPEDEF
An opaque numeric identifier returned by timer.delay. Pass it to
timer.cancel, timer.trigger, or timer.get_info to control
the timer. Timers are owned by the script that created them and are removed
automatically when the script is deleted. A failed creation returns
timer.INVALID_TIMER_HANDLE.

**Parameters**

- `value` (number) - timer identifier

**Examples**

```
local handle = timer.delay(1, true, function()
    print("tick")
end)

timer.cancel(handle)

```
