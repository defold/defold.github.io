# HTML5

**Namespace:** `html5`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_html5_js.cpp`
**Source:** `engine/script/src/script_html5_js.cpp`

HTML5 platform specific functions.

[icon:html5] The following functions are only available on HTML5 builds, the `html5.*` Lua namespace will not be available on other platforms.

## API

### html5.run
*Type:* FUNCTION
Executes the supplied string as JavaScript inside the browser.
A call to this function is blocking, the result is returned as-is, as a string.
(Internally this will execute the string using the eval() JavaScript function.)

**Parameters**

- `code` (string) - Javascript code to run

**Returns**

- `result` (string) - result as string

**Examples**

```
local res = html5.run("10 + 20") -- returns the string "30"
print(res)
local res_num = tonumber(res) -- convert to number
print(res_num - 20) -- prints 10

```

### html5.set_interaction_listener
*Type:* FUNCTION
Set a JavaScript interaction listener callaback from lua that will be
invoked when a user interacts with the web page by clicking, touching or typing.
The callback can then call DOM restricted actions like requesting a pointer lock,
or start playing sounds the first time the callback is invoked.

**Parameters**

- `callback` (function(self) | nil) - The interaction callback. Pass an empty function or <code>nil</code> if you no longer wish to receive callbacks.
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The calling script</dd>
</dl>

**Examples**

```
local function on_interaction(self)
    print("on_interaction called")
    html5.set_interaction_listener(nil)
end

function init(self)
    html5.set_interaction_listener(on_interaction)
end

```
