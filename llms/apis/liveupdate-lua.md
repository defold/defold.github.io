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
Mismatch between expected and actual integrity data for legacy liveupdate verification.

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
