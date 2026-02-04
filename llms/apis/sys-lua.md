# System

**Namespace:** `sys`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_engine.cpp`
**Source:** `engine/engine/src/script/script_engine.cpp`

Functions and messages for using system resources, controlling the engine,
error handling and debugging.

## API

### exit
*Type:* MESSAGE
Terminates the game application and reports the specified code to the OS.
This message can only be sent to the designated @system socket.

**Parameters**

- `code` (number) - exit code to report to the OS, 0 means clean exit

**Examples**

This examples demonstrates how to exit the application when some kind of quit messages is received (maybe from gui or similar):
```
function on_message(self, message_id, message, sender)
    if message_id == hash("quit") then
        msg.post("@system:", "exit", {code = 0})
    end
end

```

### reboot
*Type:* MESSAGE
Reboots the game engine with a specified set of arguments.
Arguments will be translated into command line arguments. Sending the reboot
command is equivalent to starting the engine with the same arguments.
On startup the engine reads configuration from "game.project" in the
project root.
This message can only be sent to the designated @system socket.

**Parameters**

- `arg1` (string) - argument 1
- `arg2` (string) - argument 2
- `arg3` (string) - argument 3
- `arg4` (string) - argument 4
- `arg5` (string) - argument 5
- `arg6` (string) - argument 6

**Examples**

How to reboot engine with a specific bootstrap collection.
```
local arg1 = '--config=bootstrap.main_collection=/my.collectionc'
local arg2 = 'build/game.projectc'
msg.post("@system:", "reboot", {arg1 = arg1, arg2 = arg2})

```

### resume_rendering
*Type:* MESSAGE
Resume rendering.
This message can only be sent to the designated @system socket.

**Examples**

msg.post("@system:", "resume_rendering")

### set_update_frequency
*Type:* MESSAGE
Set game update-frequency (frame cap). This option is equivalent to display.update_frequency in
the "game.project" settings but set in run-time. If Vsync checked in "game.project", the rate will
be clamped to a swap interval that matches any detected main monitor refresh rate. If Vsync is
unchecked the engine will try to respect the rate in software using timers. There is no
guarantee that the frame cap will be achieved depending on platform specifics and hardware settings.
This message can only be sent to the designated @system socket.

**Parameters**

- `frequency` (number) - target frequency. 60 for 60 fps

**Examples**

msg.post("@system:", "set_update_frequency", { frequency = 60 } )

### set_vsync
*Type:* MESSAGE
Set the vsync swap interval. The interval with which to swap the front and back buffers
in sync with vertical blanks (v-blank), the hardware event where the screen image is updated
with data from the front buffer. A value of 1 swaps the buffers at every v-blank, a value of
2 swaps the buffers every other v-blank and so on. A value of 0 disables waiting for v-blank
before swapping the buffers. Default value is 1.
When setting the swap interval to 0 and having vsync disabled in
"game.project", the engine will try to respect the set frame cap value from
"game.project" in software instead.
This setting may be overridden by driver settings.
This message can only be sent to the designated @system socket.

**Parameters**

- `swap_interval` (number) - target swap interval.

**Examples**

msg.post("@system:", "set_vsync", { swap_interval = 1 } )

### start_record
*Type:* MESSAGE
Starts video recording of the game frame-buffer to file. Current video format is the
open vp8 codec in the ivf container. It's possible to upload this format directly
to YouTube. The VLC video player has native support but with the known issue that
not the entire file is played back. It's probably an issue with VLC.
The Miro Video Converter has support for vp8/ivf.
   Video recording is only supported on desktop platforms.
 Audio is currently not supported
 Window width and height must be a multiple of 8 to be able to record video.
This message can only be sent to the designated @system socket.

**Parameters**

- `file_name` (string) - file name to write the video to
- `frame_period` (number) - frame period to record, ie write every nth frame. Default value is <code>2</code>
- `fps` (number) - frames per second. Playback speed for the video. Default value is <code>30</code>. The fps value doens't affect the recording. It's only meta-data in the written video file.

**Examples**

Record a video in 30 fps given that the native game fps is 60:
```
msg.post("@system:", "start_record", { file_name = "test_rec.ivf" } )

```

To write a video in 60 fps given that the native game fps is 60:
```
msg.post("@system:", "start_record", { file_name = "test_rec.ivf", frame_period = 1, fps = 60 } )

```

### stop_record
*Type:* MESSAGE
Stops the currently active video recording.
   Video recording is only supported on desktop platforms.
This message can only be sent to the designated @system socket.

**Examples**

```
msg.post("@system:", "stop_record")

```

### sys.deserialize
*Type:* FUNCTION
This function will raise a Lua error if an error occurs while deserializing the buffer.

**Parameters**

- `buffer` (string) - buffer to deserialize from

**Returns**

- `table` (table) - lua table with deserialized data

**Examples**

Deserialize a lua table that was previously serialized:
```
local buffer = sys.serialize(my_table)
local table = sys.deserialize(buffer)

```

### sys.exists
*Type:* FUNCTION
Check if a path exists
Good for checking if a file exists before loading a large file

**Parameters**

- `path` (string) - path to check

**Returns**

- `result` (boolean) - <code>true</code> if the path exists, <code>false</code> otherwise

**Examples**

Load data but return nil if path didn't exist
```
if not sys.exists(path) then
    return nil
end
return sys.load(path) -- returns {} if it failed

```

### sys.exit
*Type:* FUNCTION
Terminates the game application and reports the specified code to the OS.

**Parameters**

- `code` (number) - exit code to report to the OS, 0 means clean exit

**Examples**

This examples demonstrates how to exit the application when some kind of quit messages is received (maybe from gui or similar):
```
function on_message(self, message_id, message, sender)
    if message_id == hash("quit") then
        sys.exit(0)
    end
end

```

### sys.get_application_info
*Type:* FUNCTION
Returns a table with application information for the requested app.
 On iOS, the app_string is an url scheme for the app that is queried. Your
game needs to list the schemes that are queried in an LSApplicationQueriesSchemes array
in a custom "Info.plist".
 On Android, the app_string is the package identifier for the app.

**Parameters**

- `app_string` (string) - platform specific string with application package or query, see above for details.

**Returns**

- `app_info` (table) - table with application information in the following fields:
<dl>
<dt><code>installed</code></dt>
<dd><span class="type">boolean</span> <code>true</code> if the application is installed, <code>false</code> otherwise.</dd>
</dl>

**Examples**

Check if twitter is installed:
```
sysinfo = sys.get_sys_info()
twitter = {}

if sysinfo.system_name == "Android" then
  twitter = sys.get_application_info("com.twitter.android")
elseif sysinfo.system_name == "iPhone OS" then
  twitter = sys.get_application_info("twitter:")
end

if twitter.installed then
  -- twitter is installed!
end

```

 Info.plist for the iOS app needs to list the schemes that are queried:
```
...
LSApplicationQueriesSchemes

   twitter

...

```

### sys.get_application_path
*Type:* FUNCTION
The path from which the application is run.
This function will raise a Lua error if unable to get the application support path.

**Returns**

- `path` (string) - path to application executable

**Examples**

Find a path where we can store data (the example path is on the macOS platform):
```
-- macOS: /Applications/my_game.app
local application_path = sys.get_application_path()
print(application_path) --> /Applications/my_game.app

-- Windows: C:\Program Files\my_game\my_game.exe
print(application_path) --> C:\Program Files\my_game

-- Linux: /home/foobar/my_game/my_game
print(application_path) --> /home/foobar/my_game

-- Android package name: com.foobar.my_game
print(application_path) --> /data/user/0/com.foobar.my_game

-- iOS: my_game.app
print(application_path) --> /var/containers/Bundle/Applications/123456AB-78CD-90DE-12345678ABCD/my_game.app

-- HTML5: http://www.foobar.com/my_game/
print(application_path) --> http://www.foobar.com/my_game

```

### sys.get_config_boolean
*Type:* FUNCTION
Get boolean config value from the game.project configuration file with optional default value

**Parameters**

- `key` (string) - key to get value for. The syntax is SECTION.KEY
- `default_value` (boolean) (optional) - (optional) default value to return if the value does not exist

**Returns**

- `value` (boolean) - config value as a boolean. default_value if the config key does not exist. false if no default value was supplied.

**Examples**

Get user config value
```
local vsync = sys.get_config_boolean("display.vsync", false)

```

### sys.get_config_int
*Type:* FUNCTION
Get integer config value from the game.project configuration file with optional default value

**Parameters**

- `key` (string) - key to get value for. The syntax is SECTION.KEY
- `default_value` (number) (optional) - (optional) default value to return if the value does not exist

**Returns**

- `value` (number) - config value as an integer. default_value if the config key does not exist. 0 if no default value was supplied.

**Examples**

Get user config value
```
local speed = sys.get_config_int("my_game.speed", 20) -- with default value

```

```
local testmode = sys.get_config_int("my_game.testmode") -- without default value
if testmode ~= nil then
    -- do stuff
end

```

### sys.get_config_number
*Type:* FUNCTION
Get number config value from the game.project configuration file with optional default value

**Parameters**

- `key` (string) - key to get value for. The syntax is SECTION.KEY
- `default_value` (number) (optional) - (optional) default value to return if the value does not exist

**Returns**

- `value` (number) - config value as an number. default_value if the config key does not exist. 0 if no default value was supplied.

**Examples**

Get user config value
```
local speed = sys.get_config_number("my_game.speed", 20.0)

```

### sys.get_config_string
*Type:* FUNCTION
Get string config value from the game.project configuration file with optional default value

**Parameters**

- `key` (string) - key to get value for. The syntax is SECTION.KEY
- `default_value` (string) (optional) - (optional) default value to return if the value does not exist

**Returns**

- `value` (string) - config value as a string. default_value if the config key does not exist. nil if no default value was supplied.

**Examples**

Get user config value
```
local text = sys.get_config_string("my_game.text", "default text"))

```

Start the engine with a bootstrap config override and add a custom config value
```
$ dmengine --config=bootstrap.main_collection=/mytest.collectionc --config=mygame.testmode=1

```

Read the custom config value from the command line
```
local testmode = sys.get_config_int("mygame.testmode")

```

### sys.get_connectivity
*Type:* FUNCTION
Returns the current network connectivity status
on mobile platforms.
On desktop, this function always return sys.NETWORK_CONNECTED.

**Returns**

- `status` (constant) - network connectivity status:
<ul>
<li><code>sys.NETWORK_DISCONNECTED</code> (no network connection is found)</li>
<li><code>sys.NETWORK_CONNECTED_CELLULAR</code> (connected through mobile cellular)</li>
<li><code>sys.NETWORK_CONNECTED</code> (otherwise, Wifi)</li>
</ul>

**Examples**

Check if we are connected through a cellular connection
```
if (sys.NETWORK_CONNECTED_CELLULAR == sys.get_connectivity()) then
  print("Connected via cellular, avoid downloading big files!")
end

```

### sys.get_engine_info
*Type:* FUNCTION
Returns a table with engine information.

**Returns**

- `engine_info` (table) - table with engine information in the following fields:
<dl>
<dt><code>version</code></dt>
<dd><span class="type">string</span> The current Defold engine version, i.e. "1.2.96"</dd>
<dt><code>version_sha1</code></dt>
<dd><span class="type">string</span> The SHA1 for the current engine build, i.e. "0060183cce2e29dbd09c85ece83cbb72068ee050"</dd>
<dt><code>is_debug</code></dt>
<dd><span class="type">boolean</span> If the engine is a debug or release version</dd>
</dl>

**Examples**

How to retrieve engine information:
```
-- Update version text label so our testers know what version we're running
local engine_info = sys.get_engine_info()
local version_str = "Defold " .. engine_info.version .. "\n" .. engine_info.version_sha1
gui.set_text(gui.get_node("version"), version_str)

```

### sys.get_host_path
*Type:* FUNCTION
Create a path to the host device for unit testing
Useful for saving logs etc during development

**Notes**

- Only enabled in debug builds. In release builds returns the string unchanged

**Parameters**

- `filename` (string) - file to read from

**Returns**

- `host_path` (string) - the path prefixed with the proper host mount

**Examples**

Save data on the host
```
local host_path = sys.get_host_path("logs/test.txt")
sys.save(host_path, mytable)

```

Load data from the host
```
local host_path = sys.get_host_path("logs/test.txt")
local table = sys.load(host_path)

```

### sys.get_ifaddrs
*Type:* FUNCTION
Returns an array of tables with information on network interfaces.

**Returns**

- `ifaddrs` (table) - an array of tables. Each table entry contain the following fields:
<dl>
<dt><code>name</code></dt>
<dd><span class="type">string</span> Interface name</dd>
<dt><code>address</code></dt>
<dd><span class="type">string</span> IP address. <span class="icon-attention"></span> might be <code>nil</code> if not available.</dd>
<dt><code>mac</code></dt>
<dd><span class="type">string</span> Hardware MAC address. <span class="icon-attention"></span> might be nil if not available.</dd>
<dt><code>up</code></dt>
<dd><span class="type">boolean</span> <code>true</code> if the interface is up (available to transmit and receive data), <code>false</code> otherwise.</dd>
<dt><code>running</code></dt>
<dd><span class="type">boolean</span> <code>true</code> if the interface is running, <code>false</code> otherwise.</dd>
</dl>

**Examples**

How to get the IP address of interface "en0":
```
ifaddrs = sys.get_ifaddrs()
for _,interface in ipairs(ifaddrs) do
  if interface.name == "en0" then
    local ip = interface.address
  end
end

```

### sys.get_save_file
*Type:* FUNCTION
The save-file path is operating system specific and is typically located under the user's home directory.
This function will raise a Lua error if unable to get the save file path.

**Notes**

- Setting the environment variable `DM_SAVE_HOME` overrides the default application support path.

**Parameters**

- `application_id` (string) - user defined id of the application, which helps define the location of the save-file
- `file_name` (string) - file-name to get path for

**Returns**

- `path` (string) - path to save-file

**Examples**

Find a path where we can store data:
```
local my_file_path = sys.get_save_file("my_game", "my_file")
-- macOS: /Users/foobar/Library/Application Support/my_game/my_file
print(my_file_path) --> /Users/foobar/Library/Application Support/my_game/my_file

-- Windows: C:\Users\foobar\AppData\Roaming\my_game\my_file
print(my_file_path) --> C:\Users\foobar\AppData\Roaming\my_game\my_file

-- Linux: $XDG_DATA_HOME/my_game/my_file or /home/foobar/.my_game/my_file
-- Linux: Defaults to /home/foobar/.local/share/my_game/my_file if neither exist.
print(my_file_path) --> /home/foobar/.local/share/my_game/my_file

-- Android package name: com.foobar.packagename
print(my_file_path) --> /data/data/0/com.foobar.packagename/files/my_file

-- iOS: my_game.app
print(my_file_path) --> /var/mobile/Containers/Data/Application/123456AB-78CD-90DE-12345678ABCD/my_game/my_file

-- HTML5 path inside the IndexedDB: /data/.my_game/my_file or /.my_game/my_file
print(my_file_path) --> /data/.my_game/my_file

```

### sys.get_sys_info
*Type:* FUNCTION
Returns a table with system information.

**Parameters**

- `options` (table) (optional) - optional options table
- ignore_secure <span class="type">boolean</span> this flag ignores values might be secured by OS e.g. <code>device_ident</code>

**Returns**

- `sys_info` (table) - table with system information in the following fields:
<dl>
<dt><code>device_model</code></dt>
<dd><span class="type">string</span> <span class="icon-ios"></span><span class="icon-android"></span> Only available on iOS and Android.</dd>
<dt><code>manufacturer</code></dt>
<dd><span class="type">string</span> <span class="icon-ios"></span><span class="icon-android"></span> Only available on iOS and Android.</dd>
<dt><code>system_name</code></dt>
<dd><span class="type">string</span> The system name: "Darwin", "Linux", "Windows", "HTML5", "Android" or "iPhone OS"</dd>
<dt><code>system_version</code></dt>
<dd><span class="type">string</span> The system OS version.</dd>
<dt><code>api_version</code></dt>
<dd><span class="type">string</span> The API version on the system.</dd>
<dt><code>language</code></dt>
<dd><span class="type">string</span> Two character ISO-639 format, i.e. "en".</dd>
<dt><code>device_language</code></dt>
<dd><span class="type">string</span> Two character ISO-639 format (i.e. "sr") and, if applicable, followed by a dash (-) and an ISO 15924 script code (i.e. "sr-Cyrl" or "sr-Latn"). Reflects the device preferred language.</dd>
<dt><code>territory</code></dt>
<dd><span class="type">string</span> Two character ISO-3166 format, i.e. "US".</dd>
<dt><code>gmt_offset</code></dt>
<dd><span class="type">number</span> The current offset from GMT (Greenwich Mean Time), in minutes.</dd>
<dt><code>device_ident</code></dt>
<dd><span class="type">string</span> This value secured by OS. <span class="icon-ios"></span> "identifierForVendor" on iOS. <span class="icon-android"></span> "android_id" on Android. On Android, you need to add <code>READ_PHONE_STATE</code> permission to be able to get this data. We don't use this permission in Defold.</dd>
<dt><code>user_agent</code></dt>
<dd><span class="type">string</span> <span class="icon-html5"></span> The HTTP user agent, i.e. "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8"</dd>
</dl>

**Examples**

How to get system information:
```
local info = sys.get_sys_info()
if info.system_name == "HTML5" then
  -- We are running in a browser.
end

```

### sys.load
*Type:* FUNCTION
If the file exists, it must have been created by sys.save to be loaded.
This function will raise a Lua error if an error occurs while loading the file.

**Parameters**

- `filename` (string) - file to read from

**Returns**

- `loaded` (table) - lua table, which is empty if the file could not be found

**Examples**

Load data that was previously saved, e.g. an earlier game session:
```
local my_file_path = sys.get_save_file("my_game", "my_file")
local my_table = sys.load(my_file_path)
if not next(my_table) then
  -- empty table
end

```

### sys.load_buffer
*Type:* FUNCTION
The sys.load_buffer function will first try to load the resource
from any of the mounted resource locations and return the data if
any matching entries found. If not, the path will be tried
as is from the primary disk on the device.
In order for the engine to include custom resources in the build process, you need
to specify them in the "custom_resources" key in your "game.project" settings file.
You can specify single resource files or directories. If a directory is included
in the resource list, all files and directories in that directory is recursively
included:
For example "main/data/,assets/level_data.json".

**Parameters**

- `path` (string) - the path to load the buffer from

**Returns**

- `buffer` (buffer) - the buffer with data

**Examples**

Load binary data from a custom project resource:
```
local my_buffer = sys.load_buffer("/assets/my_level_data.bin")
local data_str = buffer.get_bytes(my_buffer, "data")
local has_my_header = string.sub(data_str,1,6) == "D3F0LD"

```

Load binary data from non-custom resource files on disk:
```
local asset_1 = sys.load_buffer("folder_next_to_binary/my_level_asset.txt")
local asset_2 = sys.load_buffer("/my/absolute/path")

```

### sys.load_buffer_async
*Type:* FUNCTION
The sys.load_buffer function will first try to load the resource
from any of the mounted resource locations and return the data if
any matching entries found. If not, the path will be tried
as is from the primary disk on the device.
In order for the engine to include custom resources in the build process, you need
to specify them in the "custom_resources" key in your "game.project" settings file.
You can specify single resource files or directories. If a directory is included
in the resource list, all files and directories in that directory is recursively
included:
For example "main/data/,assets/level_data.json".
Note that issuing multiple requests of the same resource will yield
individual buffers per request. There is no implic caching of the buffers
based on request path.

**Parameters**

- `path` (string) - the path to load the buffer from
- `status_callback` (function(self, request_id, result)) - A status callback that will be invoked when a request has been handled, or an error occured. The result is a table containing:
<dl>
<dt><code>status</code></dt>
<dd><span class="type">number</span> The status of the request, supported values are:</dd>
</dl>
<ul>
<li><code>resource.REQUEST_STATUS_FINISHED</code></li>
<li><code>resource.REQUEST_STATUS_ERROR_IO_ERROR</code></li>
<li><code>resource.REQUEST_STATUS_ERROR_NOT_FOUND</code></li>
</ul>
<dl>
<dt><code>buffer</code></dt>
<dd><span class="type">buffer</span> If the request was successfull, this will contain the request payload in a buffer object, and nil otherwise. Make sure to check the status before doing anything with the buffer value!</dd>
</dl>

**Returns**

- `handle` (number) - a handle to the request

**Examples**

Load binary data from a custom project resource and update a texture resource:
```
function my_callback(self, request_id, result)
  if result.status == resource.REQUEST_STATUS_FINISHED then
     resource.set_texture("/my_texture", { ... }, result.buf)
  end
end

local my_request = sys.load_buffer_async("/assets/my_level_data.bin", my_callback)

```

Load binary data from non-custom resource files on disk:
```
function my_callback(self, request_id, result)
  if result.status ~= sys.REQUEST_STATUS_FINISHED then
    -- uh oh! File could not be found, do something graceful
  elseif request_id == self.first_asset then
    -- result.buffer contains data from my_level_asset.bin
  elif request_id == self.second_asset then
    -- result.buffer contains data from 'my_level.bin'
  end
end

function init(self)
  self.first_asset = hash("folder_next_to_binary/my_level_asset.bin")
  self.second_asset = hash("/some_absolute_path/my_level.bin")
  self.first_request = sys.load_buffer_async(self.first_asset, my_callback)
  self.second_request = sys.load_buffer_async(self.second_asset, my_callback)
end

```

### sys.load_resource
*Type:* FUNCTION
Loads a custom resource. Specify the full filename of the resource that you want
to load. When loaded, the file data is returned as a string.
If loading fails, the function returns nil plus the error message.
In order for the engine to include custom resources in the build process, you need
to specify them in the "custom_resources" key in your "game.project" settings file.
You can specify single resource files or directories. If a directory is included
in the resource list, all files and directories in that directory is recursively
included:
For example "main/data/,assets/level_data.json".

**Parameters**

- `filename` (string) - resource to load, full path

**Returns**

- `data` (string | nil) - loaded data, or <code>nil</code> if the resource could not be loaded
- `error` (string | nil) - the error message, or <code>nil</code> if no error occurred

**Examples**

```
-- Load level data into a string
local data, error = sys.load_resource("/assets/level_data.json")
-- Decode json string to a Lua table
if data then
  local data_table = json.decode(data)
  pprint(data_table)
else
  print(error)
end

```

### sys.NETWORK_CONNECTED
*Type:* CONSTANT
network connected through other, non cellular, connection

### sys.NETWORK_CONNECTED_CELLULAR
*Type:* CONSTANT
network connected through mobile cellular

### sys.NETWORK_DISCONNECTED
*Type:* CONSTANT
no network connection found

### sys.open_url
*Type:* FUNCTION
Open URL in default application, typically a browser

**Parameters**

- `url` (string) - url to open
- `attributes` (table) (optional) - table with attributes
<code>target</code>
- <span class="type">string</span> <span class="icon-html5"></span>: Optional. Specifies the target attribute or the name of the window. The following values are supported:
- <code>_self</code> - (default value) URL replaces the current page.
- <code>_blank</code> - URL is loaded into a new window, or tab.
- <code>_parent</code> - URL is loaded into the parent frame.
- <code>_top</code> - URL replaces any framesets that may be loaded.
- <code>name</code> - The name of the window (Note: the name does not specify the title of the new window).

**Returns**

- `success` (boolean) - a boolean indicating if the url could be opened or not

**Examples**

Open an URL:
```
local success = sys.open_url("http://www.defold.com", {target = "_blank"})
if not success then
  -- could not open the url...
end

```

### sys.reboot
*Type:* FUNCTION
Reboots the game engine with a specified set of arguments.
Arguments will be translated into command line arguments. Calling reboot
function is equivalent to starting the engine with the same arguments.
On startup the engine reads configuration from "game.project" in the
project root.

**Parameters**

- `arg1` (string) (optional) - argument 1
- `arg2` (string) (optional) - argument 2
- `arg3` (string) (optional) - argument 3
- `arg4` (string) (optional) - argument 4
- `arg5` (string) (optional) - argument 5
- `arg6` (string) (optional) - argument 6

**Examples**

How to reboot engine with a specific bootstrap collection.
```
local arg1 = '--config=bootstrap.main_collection=/my.collectionc'
local arg2 = 'build/game.projectc'
sys.reboot(arg1, arg2)

```

### sys.REQUEST_STATUS_ERROR_IO_ERROR
*Type:* CONSTANT
an asyncronous request is unable to read the resource

### sys.REQUEST_STATUS_ERROR_NOT_FOUND
*Type:* CONSTANT
an asyncronous request is unable to locate the resource

### sys.REQUEST_STATUS_FINISHED
*Type:* CONSTANT
an asyncronous request has finished successfully

### sys.save
*Type:* FUNCTION
The table can later be loaded by sys.load.
Use sys.get_save_file to obtain a valid location for the file.
Internally, this function uses a workspace buffer sized output file sized 512kb.
This size reflects the output file size which must not exceed this limit.
Additionally, the total number of rows that any one table may contain is limited to 65536
(i.e. a 16 bit range). When tables are used to represent arrays, the values of
keys are permitted to fall within a 32 bit range, supporting sparse arrays, however
the limit on the total number of rows remains in effect.
This function will raise a Lua error if an error occurs while saving the table.

**Parameters**

- `filename` (string) - file to write to
- `table` (table) - lua table to save

**Examples**

Save data:
```
local my_table = {}
table.insert(my_table, "my_value")
local my_file_path = sys.get_save_file("my_game", "my_file")
sys.save(my_file_path, my_table)

```

### sys.serialize
*Type:* FUNCTION
The buffer can later deserialized by sys.deserialize.
This function has all the same limitations as sys.save.
This function will raise a Lua error if an error occurs while serializing the table.

**Parameters**

- `table` (table) - lua table to serialize

**Returns**

- `buffer` (string) - serialized data buffer

**Examples**

Serialize table:
```
local my_table = {}
table.insert(my_table, "my_value")
local buffer = sys.serialize(my_table)

```

### sys.set_connectivity_host
*Type:* FUNCTION
Sets the host that is used to check for network connectivity against.

**Parameters**

- `host` (string) - hostname to check against

**Examples**

```
sys.set_connectivity_host("www.google.com")

```

### sys.set_engine_throttle
*Type:* FUNCTION
Enables engine throttling.

**Notes**

- It will automatically wake up on input events
- It will automatically throttle again after the cooldown period
- It skips entire update+render loop on the main thread. E.g loading of assets, callbacks from threads (http)
- On threaded systems, Sound will continue to play any started non-streaming sounds. (e.g. looping background music)

**Parameters**

- `enable` (boolean) - true if throttling should be enabled
- `cooldown` (number) - the time period to do update + render for (seconds)

**Examples**

Disable throttling
```
sys.set_engine_throttle(false)

```

Enable throttling
```
sys.set_engine_throttle(true, 1.5)

```

### sys.set_error_handler
*Type:* FUNCTION
Set the Lua error handler function.
The error handler is a function which is called whenever a lua runtime error occurs.

**Parameters**

- `error_handler` (function(source, message, traceback)) - the function to be called on error
<dl>
<dt><code>source</code></dt>
<dd><span class="type">string</span> The runtime context of the error. Currently, this is always <code>"lua"</code>.</dd>
<dt><code>message</code></dt>
<dd><span class="type">string</span> The source file, line number and error message.</dd>
<dt><code>traceback</code></dt>
<dd><span class="type">string</span> The stack traceback.</dd>
</dl>

**Examples**

Install error handler that just prints the errors
```
local function my_error_handler(source, message, traceback)
  print(source)    --> lua
  print(message)   --> main/my.script:10: attempt to perform arithmetic on a string value
  print(traceback) --> stack traceback:
                   -->         main/test.script:10: in function 'boom'
                   -->         main/test.script:15: in function
end

local function boom()
  return 10 + "string"
end

function init(self)
  sys.set_error_handler(my_error_handler)
  boom()
end

```

### sys.set_render_enable
*Type:* FUNCTION
Disables rendering

**Notes**

- It will will leave the back buffer as-is

**Parameters**

- `enable` (boolean) - true if throttling should be enabled

**Examples**

Disable rendering
```
sys.set_render_enable(false)

```

### sys.set_update_frequency
*Type:* FUNCTION
Set game update-frequency (frame cap). This option is equivalent to display.update_frequency in
the "game.project" settings but set in run-time. If Vsync checked in "game.project", the rate will
be clamped to a swap interval that matches any detected main monitor refresh rate. If Vsync is
unchecked the engine will try to respect the rate in software using timers. There is no
guarantee that the frame cap will be achieved depending on platform specifics and hardware settings.

**Parameters**

- `frequency` (number) - target frequency. 60 for 60 fps

**Examples**

Setting the update frequency to 60 frames per second
```
sys.set_update_frequency(60)

```

### sys.set_vsync_swap_interval
*Type:* FUNCTION
Set the vsync swap interval. The interval with which to swap the front and back buffers
in sync with vertical blanks (v-blank), the hardware event where the screen image is updated
with data from the front buffer. A value of 1 swaps the buffers at every v-blank, a value of
2 swaps the buffers every other v-blank and so on. A value of 0 disables waiting for v-blank
before swapping the buffers. Default value is 1.
When setting the swap interval to 0 and having vsync disabled in
"game.project", the engine will try to respect the set frame cap value from
"game.project" in software instead.
This setting may be overridden by driver settings.

**Parameters**

- `swap_interval` (number) - target swap interval.

**Examples**

Setting the swap intervall to swap every v-blank
```
sys.set_vsync_swap_interval(1)

```

### toggle_physics_debug
*Type:* MESSAGE
Toggles the on-screen physics visual debugging mode which is very useful for
tracking down issues related to physics. This mode visualizes
all collision object shapes and normals at detected contact points. Toggling
this mode on is equal to setting physics.debug in the "game.project" settings,
but set in run-time.
This message can only be sent to the designated @system socket.

**Examples**

```
msg.post("@system:", "toggle_physics_debug")

```

### toggle_profile
*Type:* MESSAGE
Toggles the on-screen profiler.
The profiler is a real-time tool that shows the numbers of milliseconds spent
in each scope per frame as well as counters. The profiler is very useful for
tracking down performance and resource problems.
In addition to the on-screen profiler, Defold includes a web-based profiler that
allows you to sample a series of data points and then analyze them in detail.
The web profiler is available at http://:8002 where  is
the IP address of the device you are running your game on.
This message can only be sent to the designated @system socket.

**Examples**

```
msg.post("@system:", "toggle_profile")

```
