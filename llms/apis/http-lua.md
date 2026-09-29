# HTTP

**Namespace:** `http`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_http.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_http.cpp`

Functions for performing HTTP and HTTPS requests.

## API

### http.request
*Type:* FUNCTION
Perform a HTTP/HTTPS request.
 If no timeout value is passed, the configuration value "network.http_timeout" is used. If that is not set, the timeout value is 0 (which blocks indefinitely).

**Parameters**

- `url` (string) - target url
- `method` (string) - HTTP/HTTPS method, e.g. "GET", "PUT", "POST" etc.
- `callback` (fun(self:script_instance, id:hash, response:http.response)) - response callback function
<dl>
<dt class="api-lua-v2-type-definition"><code>self:<a href="../builtins-lua/#script_instance">script_instance</a></code></dt>
<dd>The current script instance</dd>
<dt class="api-lua-v2-type-definition"><code>id:<a href="../builtins-lua/#hash">hash</a></code></dt>
<dd>Internal message identifier. Do not use!</dd>
</dl>
- `headers` (table<string, string>) (optional) - optional table with custom headers
- `post_data` (string) (optional) - optional data to send
- `options` (http.request_options) (optional) - optional request options

**Examples**

Basic HTTP-GET request. The callback receives a table with the response
in the fields status, the response (the data) and headers (a table).
```
local function http_result(self, _, response)
    if response.bytes_total ~= nil then
        update_my_progress_bar(self, response.bytes_received / response.bytes_total)
    else
        print(response.status)
        print(response.response)
        pprint(response.headers)
    end
end

function init(self)
    http.request("http://www.google.com", "GET", http_result, nil, nil, { report_progress = true })
end

```

### http.request_options
*Type:* STRUCT
HTTP request options

**Members**

- `timeout?` (number) - timeout in seconds
- `path?` (string) - absolute destination path; overwritten only for status 200
- `ignore_cache?` (boolean) - do not return cached data for status 304; unavailable on HTML5
- `chunked_transfer?` (boolean) - use chunked transfer encoding for HTTPS requests larger than 16 KB; defaults to true and is unavailable on HTML5
- `report_progress?` (boolean) - report transferred and total byte counts to the callback

### http.response
*Type:* STRUCT
HTTP response data

**Members**

- `status` (integer) - response status
- `response?` (string) - response data when it is not saved to disk
- `headers?` (table<string, string>) - response headers for status 200 or 206
- `path?` (string) - destination path when the response is saved to disk
- `error?` (string) - unexpected error, such as a file I/O error
- `bytes_received?` (integer) - bytes transferred when progress reporting is enabled
- `bytes_total?` (integer) - total request size when progress reporting is enabled
- `range_start?` (integer) - requested-file start offset
- `range_end?` (integer) - requested-file end offset, inclusive
- `document_size?` (integer) - full requested-file size
