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

- `handle` (number) - the timer handle returned by timer.delay()

**Returns**

- `true` (boolean) - if the timer was active, false if the timer is already cancelled / complete

**Examples**

```
self.handle = timer.delay(1, true, function() print("print every second") end)
...
local result = timer.cancel(self.handle)
if not result then
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
- `callback` (function(self, handle, time_elapsed)) - timer callback function
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The current object</dd>
<dt><code>handle</code></dt>
<dd><span class="type">number</span> The handle of the timer</dd>
<dt><code>time_elapsed</code></dt>
<dd><span class="type">number</span> The elapsed time - on first trigger it is time since timer.delay call, otherwise time since last trigger</dd>
</dl>

**Returns**

- `handle` (number) - identifier for the create timer, returns timer.INVALID_TIMER_HANDLE if the timer can not be created

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

- `handle` (number) - the timer handle returned by timer.delay()

**Returns**

- `data` (table | nil) - table or <code>nil</code> if timer is cancelled/completed. table with data in the following fields:
<dl>
<dt><code>time_remaining</code></dt>
<dd><span class="type">number</span> Time remaining until the next time a timer.delay() fires.</dd>
<dt><code>delay</code></dt>
<dd><span class="type">number</span> Time interval.</dd>
<dt><code>repeating</code></dt>
<dd><span class="type">boolean</span> true = repeat timer until cancel, false = one-shot timer.</dd>
</dl>

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

### timer.INVALID_TIMER_HANDLE
*Type:* CONSTANT
Indicates an invalid timer handle

### timer.trigger
*Type:* FUNCTION
Manual triggering a callback for a timer.

**Parameters**

- `handle` (number) - the timer handle returned by timer.delay()

**Returns**

- `true` (boolean) - if the timer was active, false if the timer is already cancelled / complete

**Examples**

```
self.handle = timer.delay(1, true, function() print("print every second or manually by timer.trigger") end)
...
local result = timer.trigger(self.handle)
if not result then
   print("the timer is already cancelled or complete")
end

```
