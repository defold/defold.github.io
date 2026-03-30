# LiveUpdate

**Namespace:** `liveupdate`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_liveupdate.h`
**Source:** `engine/liveupdate/src/script_liveupdate.h`

Functions and constants to access resources.

## API

### liveupdate.add_mount
*Type:* FUNCTION
Adds a resource mount to the resource system.
The mounts are persisted between sessions.
After the mount succeeded, the resources are available to load. (i.e. no reboot required)

**Notes**

- The request is asynchronous
- Names cannot start with '_'
- Priority must be >= 0

**Parameters**

- `name` (string) - Unique name of the mount
- `uri` (string) - The uri of the mount, including the scheme. Currently supported schemes are 'zip' and 'archive'.
- `priority` (number) - Priority of mount. Larger priority takes prescedence
- `callback` (function) - Callback after the asynchronous request completed

**Returns**

- `result` (number) - The result of the request

**Examples**

Add multiple mounts. Higher priority takes precedence.
```
liveupdate.add_mount("common", "zip:/path/to/common_stuff.zip", 10, function (result) end) -- base pack
liveupdate.add_mount("levelpack_1", "zip:/path/to/levels_1_to_20.zip", 20, function (result) end) -- level pack
liveupdate.add_mount("season_pack_1", "zip:/path/to/easter_pack_1.zip", 30, function (result) end) -- season pack, overriding content in the other packs

```

### liveupdate.get_current_manifest
*Type:* FUNCTION
Return a reference to the Manifest that is currently loaded.

**Returns**

- `manifest_reference` (number) - reference to the Manifest that is currently loaded

### liveupdate.get_mounts
*Type:* FUNCTION
Get an array of the current mounts
This can be used to determine if a new mount is needed or not

**Returns**

- `mounts` (table) - Array of mounts

**Examples**

Output the current resource mounts
```
pprint("MOUNTS", liveupdate.get_mounts())

```

Give an output like:
```
DEBUG:SCRIPT: MOUNTS,
{ --[[0x119667bf0]]
  1 = { --[[0x119667c50]]
    name = "liveupdate",
    uri = "zip:/device/path/to/acchives/liveupdate.zip",
    priority = 5
  },
  2 = { --[[0x119667d50]]
    name = "_base",
    uri = "archive:build/default/game.dmanifest",
    priority = -10
  }
}

```

### liveupdate.is_using_liveupdate_data
*Type:* FUNCTION
Is any liveupdate data mounted and currently in use?
This can be used to determine if a new manifest or zip file should be downloaded.

**Notes**

- deprecated

**Returns**

- `bool` (boolean) - true if a liveupdate archive (any format) has been loaded

### liveupdate.LIVEUPDATE_BUNDLED_RESOURCE_MISMATCH
*Type:* CONSTANT
Mismatch between between expected bundled resources and actual bundled resources. The manifest expects a resource to be in the bundle, but it was not found in the bundle. This is typically the case when a non-excluded resource was modified between publishing the bundle and publishing the manifest.

### liveupdate.LIVEUPDATE_ENGINE_VERSION_MISMATCH
*Type:* CONSTANT
Mismatch between running engine version and engine versions supported by manifest.

### liveupdate.LIVEUPDATE_FORMAT_ERROR
*Type:* CONSTANT
Failed to parse manifest data buffer. The manifest was probably produced by a different engine version.

### liveupdate.LIVEUPDATE_INVAL
*Type:* CONSTANT
Argument was invalid

### liveupdate.LIVEUPDATE_INVALID_HEADER
*Type:* CONSTANT
The handled resource is invalid.

### liveupdate.LIVEUPDATE_INVALID_RESOURCE
*Type:* CONSTANT
The header of the resource is invalid.

### liveupdate.LIVEUPDATE_IO_ERROR
*Type:* CONSTANT
I/O operation failed

### liveupdate.LIVEUPDATE_MEM_ERROR
*Type:* CONSTANT
Memory wasn't allocated

### liveupdate.LIVEUPDATE_OK
*Type:* CONSTANT
LIVEUPDATE_OK

### liveupdate.LIVEUPDATE_SCHEME_MISMATCH
*Type:* CONSTANT
Mismatch between scheme used to load resources. Resources are loaded with a different scheme than from manifest, for example over HTTP or directly from file. This is typically the case when running the game directly from the editor instead of from a bundle.

### liveupdate.LIVEUPDATE_SIGNATURE_MISMATCH
*Type:* CONSTANT
Mismatch between manifest expected signature and actual signature.

### liveupdate.LIVEUPDATE_UNKNOWN
*Type:* CONSTANT
Unspecified error

### liveupdate.LIVEUPDATE_VERSION_MISMATCH
*Type:* CONSTANT
Mismatch between manifest expected version and actual version.

### liveupdate.remove_mount
*Type:* FUNCTION
Remove a mount the resource system.
The remaining mounts are persisted between sessions.
Removing a mount does not affect any loaded resources.

**Notes**

- The call is synchronous

**Parameters**

- `name` (string) - Unique name of the mount

**Returns**

- `result` (number) - The result of the call

**Examples**

Add multiple mounts. Higher priority takes precedence.
```
liveupdate.remove_mount("season_pack_1")

```

### liveupdate.store_archive
*Type:* FUNCTION
Stores a zip file and uses it for live update content. The contents of the
zip file will be verified against the manifest to ensure file integrity.
It is possible to opt out of the resource verification using an option passed
to this function.
The path is stored in the (internal) live update location.

**Notes**

- deprecated

**Parameters**

- `path` (string) - the path to the original file on disc
- `callback` (function(self, status)) - the callback function
executed after the storage has completed
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The current object.</dd>
<dt><code>status</code></dt>
<dd><span class="type">constant</span> the status of the store operation (See liveupdate.store_manifest)</dd>
</dl>
- `options` (table) (optional) - optional table with extra parameters. Supported entries:
<ul>
<li><span class="type">boolean</span> <code>verify</code>: if archive should be verified as well as stored (defaults to true)</li>
</ul>

**Examples**

How to download an archive with HTTP and store it on device.
```
local LIVEUPDATE_URL =

-- This can be anything, but you should keep the platform bundles apart
local ZIP_FILENAME = 'defold.resourcepack.zip'

local APP_SAVE_DIR = "LiveUpdateDemo"

function init(self)
    self.proxy = "levels#level1"

    print("INIT: is_using_liveupdate_data:", liveupdate.is_using_liveupdate_data())
    -- let's download the archive
    msg.post("#", "attempt_download_archive")
end

-- helper function to store headers from the http request (e.g. the ETag)
local function store_http_response_headers(name, data)
    local path = sys.get_save_file(APP_SAVE_DIR, name)
    sys.save(path, data)
end

local function load_http_response_headers(name)
    local path = sys.get_save_file(APP_SAVE_DIR, name)
    return sys.load(path)
end

-- returns headers that can potentially generate a 304
-- without redownloading the file again
local function get_http_request_headers(name)
    local data = load_http_response_headers(name)
    local headers = {}
    for k, v in pairs(data) do
        if string.lower(k) == 'etag' then
            headers['If-None-Match'] = v
        elseif string.lower(k) == 'last-modified' then
            headers['If-Modified-Since'] = v
        end
    end
    return headers
end

local function store_archive_cb(self, path, status)
    if status == true then
        print("Successfully stored live update archive!", path)
        sys.reboot()
    else
        print("Failed to store live update archive, ", path)
        -- remove the path
    end
end

function on_message(self, message_id, message, sender)
    if message_id == hash("attempt_download_archive") then

        -- by supplying the ETag, we don't have to redownload the file again
        -- if we already have downloaded it.
        local headers = get_http_request_headers(ZIP_FILENAME .. '.json')
        if not liveupdate.is_using_liveupdate_data() then
            headers = {} -- live update data has been purged, and we need do a fresh download
        end

        local path = sys.get_save_file(APP_SAVE_DIR, ZIP_FILENAME)
        local options = {
            path = path,        -- a temporary file on disc. will be removed upon successful liveupdate storage
            ignore_cache = true -- we don't want to store a (potentially large) duplicate in our http cache
        }

        local url = LIVEUPDATE_URL .. ZIP_FILENAME
        print("Downloading", url)
        http.request(url, "GET", function(self, id, response)
            if response.status == 304 then
                print(string.format("%d: Archive zip file up-to-date", response.status))
            elseif response.status == 200 and response.error == nil then
                -- register the path to the live update system
                liveupdate.store_archive(response.path, store_archive_cb)
                -- at this point, the "path" has been moved internally to a different location

                -- save the ETag for the next run
                store_http_response_headers(ZIP_FILENAME .. '.json', response.headers)
            else
                print("Error when downloading", url, "to", path, ":", response.status, response.error)
            end

            -- If we got a 200, we would call store_archive_cb() then reboot
            -- Second time, if we get here, it should be after a 304, and then
            -- we can load the missing resources from the liveupdate archive
            if liveupdate.is_using_liveupdate_data() then
                msg.post(self.proxy, "load")
            end
        end,
        headers, nil, options)

```

### liveupdate.store_manifest
*Type:* FUNCTION
Create a new manifest from a buffer. The created manifest is verified
by ensuring that the manifest was signed using the bundled public/private
key-pair during the bundle process and that the manifest supports the current
running engine version. Once the manifest is verified it is stored on device.
The next time the engine starts (or is rebooted) it will look for the stored
manifest before loading resources. Storing a new manifest allows the
developer to update the game, modify existing resources, or add new
resources to the game through LiveUpdate.

**Notes**

- deprecated

**Parameters**

- `manifest_buffer` (string) - the binary data that represents the manifest
- `callback` (function(self, status)) - the callback function
executed once the engine has attempted to store the manifest.
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The current object.</dd>
<dt><code>status</code></dt>
<dd><span class="type">constant</span> the status of the store operation:</dd>
</dl>
<ul>
<li><code>liveupdate.LIVEUPDATE_OK</code></li>
<li><code>liveupdate.LIVEUPDATE_INVALID_RESOURCE</code></li>
<li><code>liveupdate.LIVEUPDATE_VERSION_MISMATCH</code></li>
<li><code>liveupdate.LIVEUPDATE_ENGINE_VERSION_MISMATCH</code></li>
<li><code>liveupdate.LIVEUPDATE_SIGNATURE_MISMATCH</code></li>
<li><code>liveupdate.LIVEUPDATE_BUNDLED_RESOURCE_MISMATCH</code></li>
<li><code>liveupdate.LIVEUPDATE_FORMAT_ERROR</code></li>
</ul>

**Examples**

How to download a manifest with HTTP and store it on device.
```
local function store_manifest_cb(self, status)
  if status == liveupdate.LIVEUPDATE_OK then
    pprint("Successfully stored manifest. This manifest will be loaded instead of the bundled manifest the next time the engine starts.")
  else
    pprint("Failed to store manifest")
  end
end

local function download_and_store_manifest(self)
  http.request(MANIFEST_URL, "GET", function(self, id, response)
      if response.status == 200 then
        liveupdate.store_manifest(response.response, store_manifest_cb)
      end
    end)
end

```

### liveupdate.store_resource
*Type:* FUNCTION
add a resource to the data archive and runtime index. The resource will be verified
internally before being added to the data archive.

**Notes**

- deprecated

**Parameters**

- `manifest_reference` (number) - The manifest to check against.
- `data` (string) - The resource data that should be stored.
- `hexdigest` (string) - The expected hash for the resource,
retrieved through collectionproxy.missing_resources.
- `callback` (function(self, hexdigest, status)) - The callback
function that is executed once the engine has been attempted to store
the resource.
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The current object.</dd>
<dt><code>hexdigest</code></dt>
<dd><span class="type">string</span> The hexdigest of the resource.</dd>
<dt><code>status</code></dt>
<dd><span class="type">boolean</span> Whether or not the resource was successfully stored.</dd>
</dl>

**Examples**

```
function init(self)
    self.manifest = liveupdate.get_current_manifest()
end

local function callback_store_resource(self, hexdigest, status)
     if status == true then
          print("Successfully stored resource: " .. hexdigest)
     else
          print("Failed to store resource: " .. hexdigest)
     end
end

local function load_resources(self, target)
     local resources = collectionproxy.missing_resources(target)
     for _, resource_hash in ipairs(resources) do
          local baseurl = "http://example.defold.com:8000/"
          http.request(baseurl .. resource_hash, "GET", function(self, id, response)
               if response.status == 200 then
                    liveupdate.store_resource(self.manifest, response.response, resource_hash, callback_store_resource)
               else
                    print("Failed to download resource: " .. resource_hash)
               end
          end)
     end
end

```
