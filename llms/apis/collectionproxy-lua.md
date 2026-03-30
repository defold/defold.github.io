# Collection proxy

**Namespace:** `collectionproxy`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_collectionproxy.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_collectionproxy.cpp`

Messages for controlling and interacting with collection proxies
which are used to dynamically load collections into the runtime.

## API

### async_load
*Type:* MESSAGE
Post this message to a collection-proxy-component to start background loading of the referenced collection.
When the loading has completed, the message proxy_loaded will be sent back to the script.
A loaded collection must be initialized (message init) and enabled (message enable) in order to be simulated and drawn.

**Examples**

In this example we use a collection proxy to load/unload a level (collection).
The example assume the script belongs to an instance with collection-proxy-component with id "proxy".
```
function on_message(self, message_id, message, sender)
    if message_id == hash("start_level") then
        -- some script tells us to start loading the level
        msg.post("#proxy", "async_load")
        -- store sender for later notification
        self.loader = sender
    elseif message_id == hash("proxy_loaded") then
        -- enable the collection and let the loader know
        msg.post(sender, "enable")
        msg.post(self.loader, message_id)
    end
end

```

### collectionproxy.get_resources
*Type:* FUNCTION
return an indexed table of resources for a collection proxy where the
referenced collection has been excluded using LiveUpdate. Each entry is a
hexadecimal string that represents the data of the specific resource.
This representation corresponds with the filename for each individual
resource that is exported when you bundle an application with LiveUpdate
functionality.

**Parameters**

- `collectionproxy` (url) - the collectionproxy to check for resources.

**Returns**

- `resources` (table) - the resources, or an empty list if the
collection was not excluded.

**Examples**

```
local function print_resources(self, cproxy)
    local resources = collectionproxy.get_resources(cproxy)
    for _, v in ipairs(resources) do
        print("Resource: " .. v)
    end
end

```

### collectionproxy.missing_resources
*Type:* FUNCTION
return an array of missing resources for a collection proxy. Each
entry is a hexadecimal string that represents the data of the specific
resource. This representation corresponds with the filename for each
individual resource that is exported when you bundle an application with
LiveUpdate functionality. It should be considered good practise to always
check whether or not there are any missing resources in a collection proxy
before attempting to load the collection proxy.

**Parameters**

- `collectionproxy` (url) - the collectionproxy to check for missing
resources.

**Returns**

- `resources` (table) - the missing resources

**Examples**

```
function init(self)
end

local function callback(self, id, response)
    local expected = self.resources[id]
    if response ~= nil and response.status == 200 then
        print("Successfully downloaded resource: " .. expected)
        resource.store_resource(response.response)
    else
        print("Failed to download resource: " .. expected)
        -- error handling
    end
end

local function download_resources(self, cproxy)
    self.resources = {}
    local resources = collectionproxy.missing_resources(cproxy)
    for _, v in ipairs(resources) do
        print("Downloading resource: " .. v)

        local uri = "http://example.defold.com/" .. v
        local id = http.request(uri, "GET", callback)
        self.resources[id] = v
    end
end

```

### collectionproxy.RESULT_ALREADY_LOADED
*Type:* CONSTANT
It's impossible to change the collection if the collection is already loaded.

### collectionproxy.RESULT_LOADING
*Type:* CONSTANT
It's impossible to change the collection while the collection proxy is loading.

### collectionproxy.RESULT_NOT_EXCLUDED
*Type:* CONSTANT
It's impossible to change the collection for a proxy that isn't excluded.

### collectionproxy.set_collection
*Type:* FUNCTION
The collection should be loaded by the collection proxy.
Setting the collection to "nil" will revert it back to the original collection.
The collection proxy shouldn't be loaded and should have the 'Exclude' checkbox checked.
This functionality is designed to simplify the management of Live Update resources.

**Parameters**

- `url` (string | hash | url) (optional) - the collection proxy component
- `prototype` (string | nil) (optional) - the path to the new collection, or <code>nil</code>

**Returns**

- `success` (boolean) - collection change was successful
- `code` (number) - one of the collectionproxy.RESULT_* codes if unsuccessful

**Examples**

The example assume the script belongs to an instance with collection-proxy-component with id "proxy".
```
local ok, error = collectionproxy.set_collection("/go#collectionproxy", "/LU/3.collectionc")
 if ok then
     print("The collection has been changed to /LU/3.collectionc")
 else
     print("Error changing collection to /LU/3.collectionc ", error)
 end
 msg.post("/go#collectionproxy", "load")
 msg.post("/go#collectionproxy", "init")
 msg.post("/go#collectionproxy", "enable")

```

### disable
*Type:* MESSAGE
Post this message to a collection-proxy-component to disable the referenced collection, which in turn disables the contained game objects and components.

**Examples**

In this example we use a collection proxy to load/unload a level (collection).
The example assumes the script belongs to an instance with a collection-proxy-component with id "proxy".
```
function on_message(self, message_id, message, sender)
    if message_id == hash("end_level") then
        local proxy = msg.url("#proxy")
        msg.post(proxy, "disable")
        msg.post(proxy, "final")
        msg.post(proxy, "unload")
        -- store sender for later notification
        self.unloader = sender
    elseif message_id == hash("proxy_unloaded") then
        -- let unloader know
        msg.post(self.unloader, "level_ended")
    end
end

```

### enable
*Type:* MESSAGE
Post this message to a collection-proxy-component to enable the referenced collection, which in turn enables the contained game objects and components.
If the referenced collection was not initialized prior to this call, it will automatically be initialized.

**Examples**

In this example we use a collection proxy to load/unload a level (collection).
The example assume the script belongs to an instance with collection-proxy-component with id "proxy".
```
function on_message(self, message_id, message, sender)
    if message_id == hash("start_level") then
        -- some script tells us to start loading the level
        msg.post("#proxy", "load")
        -- store sender for later notification
        self.loader = sender
    elseif message_id == hash("proxy_loaded") then
        -- enable the collection and let the loader know
        msg.post(sender, "enable")
        msg.post(self.loader, "level_started")
    end
end

```

### final
*Type:* MESSAGE
Post this message to a collection-proxy-component to finalize the referenced collection, which in turn finalizes the contained game objects and components.

**Examples**

In this example we use a collection proxy to load/unload a level (collection).
The example assumes the script belongs to an instance with a collection-proxy-component with id "proxy".
```
function on_message(self, message_id, message, sender)
    if message_id == hash("end_level") then
        local proxy = msg.url("#proxy")
        msg.post(proxy, "disable")
        msg.post(proxy, "final")
        msg.post(proxy, "unload")
        -- store sender for later notification
        self.unloader = sender
    elseif message_id == hash("proxy_unloaded") then
        -- let unloader know
        msg.post(self.unloader, "level_ended")
    end
end

```

### init
*Type:* MESSAGE
Post this message to a collection-proxy-component to initialize the game objects and components in the referenced collection.
Sending enable to an uninitialized collection proxy automatically initializes it.
The init message simply provides a higher level of control.

**Examples**

In this example we use a collection proxy to load/unload a level (collection).
The example assume the script belongs to an instance with collection-proxy-component with id "proxy".
```
function on_message(self, message_id, message, sender)
    if message_id == hash("load_level") then
        -- some script tells us to start loading the level
        msg.post("#proxy", "load")
        -- store sender for later notification
        self.loader = sender
    elseif message_id == hash("proxy_loaded") then
        -- only initialize the proxy at this point since we want to enable it at a later time for some reason
        msg.post(sender, "init")
        -- let loader know
        msg.post(self.loader, message_id)
    end
end

```

### load
*Type:* MESSAGE
Post this message to a collection-proxy-component to start the loading of the referenced collection.
When the loading has completed, the message proxy_loaded will be sent back to the script.
A loaded collection must be initialized (message init) and enabled (message enable) in order to be simulated and drawn.

**Examples**

In this example we use a collection proxy to load/unload a level (collection).
The example assume the script belongs to an instance with collection-proxy-component with id "proxy".
```
function on_message(self, message_id, message, sender)
    if message_id == hash("start_level") then
        -- some script tells us to start loading the level
        msg.post("#proxy", "load")
        -- store sender for later notification
        self.loader = sender
    elseif message_id == hash("proxy_loaded") then
        -- enable the collection and let the loader know
        msg.post(sender, "enable")
        msg.post(self.loader, message_id)
    end
end

```

### proxy_loaded
*Type:* MESSAGE
This message is sent back to the script that initiated a collection proxy load when the referenced
collection is loaded. See documentation for load for examples how to use.

### proxy_unloaded
*Type:* MESSAGE
This message is sent back to the script that initiated an unload with a collection proxy when
the referenced collection is unloaded. See documentation for unload for examples how to use.

### set_time_step
*Type:* MESSAGE
Post this message to a collection-proxy-component to modify the time-step used when updating the collection controlled by the proxy.
The time-step is modified by a scaling factor and can be incremented either continuously or in discrete steps.
The continuous mode can be used for slow-motion or fast-forward effects.
The discrete mode is only useful when scaling the time-step to pass slower than real time (factor is below 1).
The time-step will then be set to 0 for as many frames as the scaling demands and then take on the full real-time-step for one frame,
to simulate pulses. E.g. if factor is set to 0.1 the time-step would be 0 for 9 frames, then be 1/60 for one
frame, 0 for 9 frames, and so on. The result in practice is that the game looks like it's updated at a much lower frequency than 60 Hz,
which can be useful for debugging when each frame needs to be inspected.

**Parameters**

- `factor` (number) - time-step scaling factor
- `mode` (number) - time-step mode: 0 for continuous and 1 for discrete

**Examples**

The examples assumes the script belongs to an instance with a collection-proxy-component with id "proxy".
Update the collection twice as fast:
```
msg.post("#proxy", "set_time_step", {factor = 2, mode = 0})

```

Update the collection twice as slow:
```
msg.post("#proxy", "set_time_step", {factor = 0.5, mode = 0})

```

Simulate 1 FPS for the collection:
```
msg.post("#proxy", "set_time_step", {factor = 1/60, mode = 1})

```

### unload
*Type:* MESSAGE
Post this message to a collection-proxy-component to start the unloading of the referenced collection.
When the unloading has completed, the message proxy_unloaded will be sent back to the script.

**Examples**

In this example we use a collection proxy to load/unload a level (collection).
The example assumes the script belongs to an instance with a collection-proxy-component with id "proxy".
```
function on_message(self, message_id, message, sender)
    if message_id == hash("end_level") then
        local proxy = msg.url("#proxy")
        msg.post(proxy, "disable")
        msg.post(proxy, "final")
        msg.post(proxy, "unload")
        -- store sender for later notification
        self.unloader = sender
    elseif message_id == hash("proxy_unloaded") then
        -- let unloader know
        msg.post(self.unloader, "level_ended")
    end
end

```
