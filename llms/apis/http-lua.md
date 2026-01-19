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
- `callback` (function(self, id, response)) - response callback function
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The script instance</dd>
<dt><code>id</code></dt>
<dd><span class="type">hash</span> Internal message identifier. Do not use!</dd>
<dt><code>response</code></dt>
<dd><span class="type">table</span> The response data. Contains the fields:</dd>
</dl>
<ul>
<li><span class="type">number</span> <code>status</code>: the status of the response</li>
<li><span class="type">string</span> <code>response</code>: the response data (if not saved on disc)</li>
<li><span class="type">table</span> <code>headers</code>: all the returned headers (if status is 200 or 206)</li>
<li><span class="type">string</span> <code>path</code>: the stored path (if saved to disc)</li>
<li><span class="type">string</span> <code>error</code>: if any unforeseen errors occurred (e.g. file I/O)</li>
<li><span class="type">number</span> <code>bytes_received</code>: the amount of bytes received/sent for a request, only if option <code>report_progress</code> is true</li>
<li><span class="type">number</span> <code>bytes_total</code>: the total amount of bytes for a request, only if option <code>report_progress</code> is true</li>
<li><span class="type">number</span> <code>range_start</code>: the start offset into the requested file</li>
<li><span class="type">number</span> <code>range_end</code>: the end offset into the requested file (inclusive)</li>
<li><span class="type">number</span> <code>document_size</code>: the full size of the requested file</li>
</ul>
- `headers` (table) (optional) - optional table with custom headers
- `post_data` (string) (optional) - optional data to send
- `options` (table) (optional) - optional table with request parameters. Supported entries:
<ul>
<li><span class="type">number</span> <code>timeout</code>: timeout in seconds</li>
<li><span class="type">string</span> <code>path</code>: path on disc where to download the file. Only overwrites the path if status is 200. <span class="icon-attention"></span> Path should be absolute</li>
<li><span class="type">boolean</span> <code>ignore_cache</code>: don't return cached data if we get a 304. <span class="icon-attention"></span> Not available in HTML5 build</li>
<li><span class="type">boolean</span> <code>chunked_transfer</code>: use chunked transfer encoding for https requests larger than 16kb. Defaults to true. <span class="icon-attention"></span> Not available in HTML5 build</li>
<li><span class="type">boolean</span> <code>report_progress</code>: when it is true, the amount of bytes sent and/or received for a request will be passed into the callback function</li>
</ul>

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
