# Resource

**Namespace:** `dmResource`
**Language:** C++
**Type:** Defold C++
**File:** `resource.hpp`
**Source:** `engine/resource/src/dmsdk/resource/resource.hpp`
**Include:** `dmsdk/resource/resource.hpp`

Functions for managing resource types.

## API

### AddFile
*Type:* FUNCTION
Adds a file to the resource system
Any request for this path will go through any existing mounts first.
If you wish to provide file overrides, please use the LiveUpdate feature for that.
The file isn't persisted between sessions.

**Parameters**

- `factory` (dmResource::HFactory) - Factory handle
- `path` (const char*) - The path of the resource
- `size` (uint32_t) - The size of the resource (in bytes)
- `resource` (const void*) - The resource payload

**Returns**

- `RESULT_OK` (dmResource::Result) - on success.

### CreateResource
*Type:* FUNCTION
Creates and inserts a resource into the factory

**Notes**

- The input data pointer is not stored
- The reference count is 1, so make sure it's destruction is handled

**Parameters**

- `factory` (dmResource::HFactory) - Factory handle
- `name` (dmhash_t) - Resource name
- `data` - Resource data
- `data_size` - Resource data size
- `resource` (void**) - (out) Created resource

**Returns**

- `result` (dmResource::Result) - RESULT_OK on success

### FDecryptResource
*Type:* TYPEDEF
Decrypts a file

**Notes**

- Currently, the function requires the final resource to be the same length (or less)

**Parameters**

- `buffer` (void*) - The input/output buffer
- `buffer_len` (uint32_t) - The size of the buffer (in bytes)

**Returns**

- `RESULT_OK` - on success

### Get
*Type:* FUNCTION
Get a resource from factory

**Parameters**

- `factory` (dmResource::HFactory) - Factory handle
- `path` (const char*) - Resource path
- `resource` (void**) - (out) Created resource

**Returns**

- `result` (dmResource::Result) - RESULT_OK on success

### Get
*Type:* FUNCTION
Get a loaded resource from factory

**Parameters**

- `factory` (dmResource::HFactory) - Factory handle
- `path_hash` (const char*) - Resource path hash
- `resource` (void**) - (out) Created resource

**Returns**

- `result` (dmResource::Result) - RESULT_OK on success

### GetCanonicalPath
*Type:* FUNCTION
Gets the normalized resource path: "/my//icon.texturec" -> "/my/icon.texturec". "my/icon.texturec" -> "/my/icon.texturec".

**Parameters**

- `path` (const char*) - the relative dir of the resource
- `buf` (char*) - (out) the output of the normalization
- `buf_len` (uint32_t) - the size of the output buffer

**Returns**

- `length` (uint32_t) - the length of the output string

### GetPath
*Type:* FUNCTION
Returns the canonical path hash of a resource

**Parameters**

- `factory` (dmResource::HFactory) - Factory handle
- `resource` (const void*) - Resource
- `hash` (uint64_t*) - Returned hash

**Returns**

- `RESULT_OK` - on success

### GetTypeFromExtension
*Type:* FUNCTION
Get type from extension

**Parameters**

- `factory` (dmResource::HFactory) - Factory handle
- `extension` (const char*) - File extension, without leading "." character. E.g. "ttf"
- `type` (HResourceType*) - returned type is successful

**Returns**

- `result` (dmResult::Result) - RESULT_OK on success

### GetTypeFromExtensionHash
*Type:* FUNCTION
Get type from extension hash

**Parameters**

- `factory` (dmResource::HFactory) - Factory handle
- `extension_hash` (const char*) - Hash of file extension, without leading "." character. E.g. hash("ttf")
- `type` (HResourceType*) - returned type is successful

**Returns**

- `result` (dmResult::Result) - RESULT_OK on success

### GetWithExt
*Type:* FUNCTION
Get (load) a resource from factory

**Parameters**

- `factory` (dmResource::HFactory) - Factory handle
- `path` (const char*) - Resource path
- `ext` (const char*) - Resource extension. Must match the extension of the path
- `resource` (void**) - (out) Created resource

**Returns**

- `result` (dmResource::Result) - RESULT_OK on success.
                                           RESULT_INVALID_FILE_EXTENSION if the path extension doesn't match the required extension.

### GetWithExt
*Type:* FUNCTION
Get a loaded resource from factory

**Parameters**

- `factory` (dmResource::HFactory) - Factory handle
- `path_hash` (const char*) - Resource path hash
- `ext_hash` (const char*) - Resource extension hash. Must match the extension of the path.
- `resource` (void**) - (out) Created resource

**Returns**

- `result` (dmResource::Result) - RESULT_OK on success.
                                           RESULT_INVALID_FILE_EXTENSION if the path extension doesn't match the required extension.

### PreloadHint
*Type:* FUNCTION
Hint the preloader what to load before Create is called on the resource.
The resources are not guaranteed to be loaded before Create is called.
This function can be called from a worker thread.

**Parameters**

- `factory` (dmResource::HResourcePreloadHintInfo) - Preloader handle
- `name` (const char*) - Resource name

**Returns**

- `result` (bool) - if successfully invoking preloader.

### RegisterResourceDecryptionFunction
*Type:* FUNCTION
Registers a custom resource decryption function

**Parameters**

- `decrypt_resource` (dmResource::FDecryptResource) - The decryption function

### RegisterResourceReloadedCallback
*Type:* FUNCTION
Function called when a resource has been reloaded.

**Parameters**

- `factory` (dmResource::HFactory) - Handle of the factory to which the callback will be registered
- `callback` (dmResource::FResourceReloadedCallback) - Callback function to register
- `user_data` (void*) - User data that to

### RegisterType
*Type:* FUNCTION

**Notes**

- Deprecated in favor of ResourceRegisterTypeCreatorDesc

### Release
*Type:* FUNCTION
Release resource

**Parameters**

- `factory` (dmResource::HFactory) - Factory handle
- `resource` (void*) - Resource pointer

### RemoveFile
*Type:* FUNCTION
Removes a previously registered file from the resource system

**Parameters**

- `factory` (dmResource::HFactory) - Factory handle
- `path` (const char*) - The path of the resource

**Returns**

- `RESULT_OK` (dmResource::Result) - on success.

### SetupType
*Type:* FUNCTION
Setup function pointers and context for a resource type

**Notes**

- C++ Helper function. Deprecated in favor of ResourceRegisterTypeCreatorDesc et al
