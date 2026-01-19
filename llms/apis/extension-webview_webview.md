# extension-webview

**Namespace:** `webview`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with webview APIs

## API

### webview.create
*Type:* FUNCTION
Creates a webview instance. It can show HTML pages as well as evaluate Javascript. The view remains hidden until the first call. There can exist a maximum of 4 webviews at the same time.
On iOS, the callback will never get a `webview.CALLBACK_RESULT_EVAL_ERROR`, due to the iOS SDK implementation."

**Parameters**

- `callback` (function) - A callback which receives info about finished requests taking the following parameters:
  - `self` (object) - The calling script
  - `webview_id` (number) - The webview id
  - `request_id` (number) - The request id
  - `type` (enum) - The type of callback
- `webview.CALLBACK_RESULT_URL_OK`
- `webview.CALLBACK_RESULT_URL_ERROR`
- `webview.CALLBACK_RESULT_URL_LOADING`
- `webview.CALLBACK_RESULT_EVAL_OK`
- `webview.CALLBACK_RESULT_EVAL_ERROR`
  - `data` (table) - A table holding the data
    - `url` (string) - The url used in the `webview.open()` call. `nil` otherwise.
    - `result` (string) - Holds the result of either: a failed url open, a successful eval request or a failed eval. `nil` otherwise.

**Examples**

```
local function webview_callback(self, webview_id, request_id, type, data)
    if type == webview.CALLBACK_RESULT_URL_OK then
        -- the page is now loaded, let's show it
        webview.set_visible(webview_id, 1)
    elseif type == webview.CALLBACK_RESULT_URL_ERROR then
        print("Failed to load url: " .. data["url"])
        print("Error: " .. data["error"])
    elseif type == webview.CALLBACK_RESULT_URL_LOADING then
        -- a page is loading
        -- return false to prevent it from loading
        -- return true or nil to continue loading the page
        if data.url ~= "https://www.defold.com/" then
            return false
        end
    elseif type == webview.CALLBACK_RESULT_EVAL_OK then
        print("Eval ok. Result: " .. data['result'])
    elseif type == webview.CALLBACK_RESULT_EVAL_ERROR then
        print("Eval not ok. Request # " .. request_id)
    end
end
local webview_id = webview.create(webview_callback)

```

### webview.destroy
*Type:* FUNCTION
Destroys an instance of a webview.

**Parameters**

- `webview_id` (number) - The webview id (returned by the `webview.create()` call)

### webview.open
*Type:* FUNCTION
Opens a web page in the webview, using an URL. Once the request is done, the callback (registered in `webview.create()`) is invoked.

**Parameters**

- `webview_id` (number) - The webview id
- `url` (string) - The URL to open
- `options` (table) - A table of options for the request. Currently it holds these options:
  - `hidden` (boolean) - If true, the webview will stay hidden (default=false)
  - `headers` (table) - A table of header keys and values
  - `transparent` (boolean) - If true, the webview background will be transparent (default=false)

**Examples**

```
local request_id = webview.open(webview_id, "http://www.defold.com", {hidden = true})

```

### webview.open_raw
*Type:* FUNCTION
Opens a web page in the webview, using HTML data. Once the request is done, the callback (registered in `webview.create()`) is invoked.

**Parameters**

- `webview_id` (number) - The webview id
- `html` (string) - The HTML data to display
- `options` (table) - A table of options for the request. See `webview.open()`

**Examples**

```
local html = sys.load_resource("/main/data/test.html")
local request_id = webview.open_raw(webview_id, html, {hidden = true})

```

### webview.eval
*Type:* FUNCTION
Evaluates JavaScript within the context of the currently loaded page (if any). Once the request is done, the callback (registered in `webview.create()`) is invoked. The callback will get the result in the `data["result"]` field.

**Parameters**

- `webview_id` (number) - The webview id
- `code` (string) - The JavaScript code to evaluate

**Examples**

```
local request_id = webview.eval(webview_id, "GetMyFormData()")

```

### webview.set_transparent
*Type:* FUNCTION
Set transparency of webview background

**Parameters**

- `webview_id` (number) - The webview id
- `transparent` (boolean) - If `true`, the webview background becomes transparent, otherwise opaque.

### webview.set_visible
*Type:* FUNCTION
Shows or hides a webview

**Parameters**

- `webview_id` (number) - The webview id
- `visible` (number) - If `0`, hides the webview. If non zero, shows the view

### webview.is_visible
*Type:* FUNCTION
Returns the visibility state of the webview.

**Parameters**

- `webview_id` (number) - The webview id

### webview.set_position
*Type:* FUNCTION
Sets the position and size of the webview

**Parameters**

- `webview_id` (number) - The webview id
- `x` (number) - The x position of the webview
- `y` (number) - The y position of the webview
- `width` (number) - The width of the webview (-1 to match screen width)
- `height` (number) - The height of the webview (-1 to match screen height)

### CALLBACK_RESULT_URL_OK
*Type:* VARIABLE

### CALLBACK_RESULT_URL_ERROR
*Type:* VARIABLE

### CALLBACK_RESULT_URL_LOADING
*Type:* VARIABLE

### CALLBACK_RESULT_EVAL_OK
*Type:* VARIABLE

### CALLBACK_RESULT_EVAL_ERROR
*Type:* VARIABLE
