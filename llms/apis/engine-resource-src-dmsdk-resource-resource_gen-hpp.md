# Resource

**Namespace:** `dmResource`
**Language:** C++
**Type:** Defold C++
**File:** `resource_gen.hpp`
**Source:** `engine/resource/src/dmsdk/resource/resource_gen.hpp`
**Include:** `dmsdk/resource/resource_gen.hpp`

Functions for managing resource types.

## API

### AddFile
*Type:* FUNCTION
Adds a file to the resource system
Any request for this path will go through any existing mounts first.
If you wish to provide file overrides, please use the LiveUpdate feature for that.
The file isn't persisted between sessions.

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `path` (const char*) - The path of the resource
- `size` (uint32_t) - The size of the resource (in bytes)
- `resource` (const void*) - The resource payload

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### DM_DECLARE_RESOURCE_TYPE
*Type:* MACRO
Declare and register new resource type to the engine.
This macro is used to declare the resource type callback functions used by the engine to communicate with the extension.

**Examples**

Register a new type:
```
#include
#include

static ResourceResult MyResourceTypeScriptCreate(const ResourceCreateParams* params) {}
static ResourceResult MyResourceTypeScriptDestroy(const ResourceDestroyParams* params) {}
static ResourceResult MyResourceTypeScriptRecreate(const ResourceRereateParams* params) {}

struct MyContext
{
    // ...
};

static ResourceResult RegisterResourceTypeBlob(HResourceTypeRegisterContext ctx, HResourceType type)
{
    // The engine.cpp creates the contexts for our built in types.
    // Here we register a custom type
    MyContext* context = new MyContext;

    ResourceTypeSetContext(type, (void*)context);
    ResourceTypeSetCreateFn(type, MyResourceTypeScriptCreate);
    ResourceTypeSetDestroyFn(type, MyResourceTypeScriptDestroy);
    ResourceTypeSetRecreateFn(type, MyResourceTypeScriptRecreate);
}

static ResourceResult DeregisterResourceTypeBlob(ResourceTypeRegisterContext& ctx)
{
    MyContext** context = (MyContext*)ResourceTypeGetContext(type);
    delete *context;
}

DM_DECLARE_RESOURCE_TYPE(ResourceTypeBlob, "blobc", RegisterResourceTypeBlob, DeregisterResourceTypeBlob);

```

### FReloadedCallback
*Type:* FUNCTION
Function called when a resource has been reloaded.

### FResourceDecrypt
*Type:* TYPEDEF
Encrypts a resource in-place

**Parameters**

- `buffer` (void*) - The input/output buffer
- `buffer_len` (uint32_t) - The size of the buffer (in bytes)

**Returns**

- `RESULT_OK` - on success

### FResourceReloadedCallback
*Type:* FUNCTION
Function called when a resource has been reloaded.

### Get
*Type:* FUNCTION
Get a resource from factory

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `name` (const char*) - Resource name
- `resource` (void**) - Created resource

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### GetByHash
*Type:* FUNCTION
Get a resource from factory

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `name` (dmhash_t) - Resource name
- `resource` (void**) - Created resource

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### GetDescriptor
*Type:* FUNCTION
Get resource descriptor from resource (name)

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `path` (dmhash_t) - Resource path
- `descriptor` (HResourceDescriptor*) - Returned resource descriptor

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### GetDescriptorByHash
*Type:* FUNCTION
Get resource descriptor from resource (name)

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `path_hash` (dmhash_t) - Resource path hash
- `descriptor` (HResourceDescriptor*) - Returned resource descriptor

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### GetPath
*Type:* FUNCTION
Returns the canonical path hash of a resource

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `resource` (void*) - The resource pointer
- `hash` (dmhash_t*) - (out) The path hash of the resource

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### GetRaw
*Type:* FUNCTION
Get raw resource data. Unregistered resources can be loaded with this function.
If successful, the returned resource data must be deallocated with free()

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `name` (dmhash_t) - Resource name
- `resource` (void**) - Created resource
- `resource_size` (uint32_t*) - Resource size

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### HDescriptor
*Type:* TYPEDEF
Holds information about a currently loaded resource.

### HFactory
*Type:* TYPEDEF
Resource factory handle. Holds references to all currently loaded resources.

### HPreloadHintInfo
*Type:* TYPEDEF
Holds information about preloading resources

### HResourceDescriptor
*Type:* TYPEDEF
Holds information about a currently loaded resource.

### HResourceFactory
*Type:* TYPEDEF
Resource factory handle. Holds references to all currently loaded resources.

### HResourcePreloadHintInfo
*Type:* TYPEDEF
Holds information about preloading resources

### HResourceType
*Type:* TYPEDEF
Represents a resource type, with a context and type functions for creation and destroying a resource.

### HResourceTypeContext
*Type:* TYPEDEF
Holds the resource types, as well as extra in engine contexts that can be shared across type functions.

### PreloadHint
*Type:* FUNCTION
Hint the preloader what to load before Create is called on the resource.
The resources are not guaranteed to be loaded before Create is called.
This function can be called from a worker thread.

**Parameters**

- `preloader` (dmResource::HResourcePreloadHintInfo) - Preloader handle
- `path` (const char*) - Resource path

**Returns**

- `result` (bool) - if successfully invoking preloader.

### Release
*Type:* FUNCTION
Release resource

**Notes**

- Decreases ref count by 1. If it reaches 0, the resource destroy function is called.

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `resource` (void*) - Resource pointer

### RemoveFile
*Type:* FUNCTION
Removes a previously registered file from the resource system

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `path` (const char*) - The path of the resource

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### ResourceAddFile
*Type:* FUNCTION
Adds a file to the resource system
Any request for this path will go through any existing mounts first.
If you wish to provide file overrides, please use the LiveUpdate feature for that.
The file isn't persisted between sessions.

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `path` (const char*) - The path of the resource
- `size` (uint32_t) - The size of the resource (in bytes)
- `resource` (const void*) - The resource payload

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### ResourceCreateParams
*Type:* FUNCTION
Parameters to ResourceCreate function of the resource type

### ResourceDestroyParams
*Type:* FUNCTION
Parameters to ResourceDestroy function of the resource type

### ResourceGet
*Type:* FUNCTION
Get a resource from factory

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `name` (const char*) - Resource name
- `resource` (void**) - Created resource

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### ResourceGetByHash
*Type:* FUNCTION
Get a resource from factory

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `name` (dmhash_t) - Resource name
- `resource` (void**) - Created resource

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### ResourceGetPath
*Type:* FUNCTION
Returns the canonical path hash of a resource

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `resource` (void*) - The resource pointer
- `hash` (dmhash_t*) - (out) The path hash of the resource

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### ResourceGetRaw
*Type:* FUNCTION
Get raw resource data. Unregistered resources can be loaded with this function.
If successful, the returned resource data must be deallocated with free()

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `name` (dmhash_t) - Resource name
- `resource` (void**) - Created resource
- `resource_size` (uint32_t*) - Resource size

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### ResourcePostCreateParams
*Type:* FUNCTION
Parameters to ResourcePostCreate function of the resource type

### ResourcePreloadHint
*Type:* FUNCTION
Hint the preloader what to load before Create is called on the resource.
The resources are not guaranteed to be loaded before Create is called.
This function can be called from a worker thread.

**Parameters**

- `preloader` (dmResource::HResourcePreloadHintInfo) - Preloader handle
- `path` (const char*) - Resource path

**Returns**

- `result` (bool) - if successfully invoking preloader.

### ResourcePreloadParams
*Type:* FUNCTION
Parameters to ResourcePreload function of the resource type

### ResourceRecreateParams
*Type:* FUNCTION
Parameters to ResourceRecreate function of the resource type

### ResourceRegisterDecryptionFunction
*Type:* FUNCTION
Registers a custom resource decryption function

**Parameters**

- `decrypt_resource` (dmResource::FDecryptResource) - The decryption function

### ResourceRelease
*Type:* FUNCTION
Release resource

**Notes**

- Decreases ref count by 1. If it reaches 0, the resource destroy function is called.

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `resource` (void*) - Resource pointer

### ResourceReloadedParams
*Type:* FUNCTION
Parameters to ResourceReloaded function of the resource type

### ResourceReloadedParams
*Type:* FUNCTION
Parameters to ResourceReloaded function of the resource type

### ResourceRemoveFile
*Type:* FUNCTION
Removes a previously registered file from the resource system

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `path` (const char*) - The path of the resource

**Returns**

- `result` (ResourceResult) - RESULT_OK on success

### ResourceResult
*Type:* ENUM
ResourceResult

**Members**

- `RESOURCE_RESULT_OK`
- `RESOURCE_RESULT_INVALID_DATA`
- `RESOURCE_RESULT_DDF_ERROR`
- `RESOURCE_RESULT_RESOURCE_NOT_FOUND`
- `RESOURCE_RESULT_MISSING_FILE_EXTENSION`
- `RESOURCE_RESULT_ALREADY_REGISTERED`
- `RESOURCE_RESULT_INVAL`
- `RESOURCE_RESULT_UNKNOWN_RESOURCE_TYPE`
- `RESOURCE_RESULT_OUT_OF_MEMORY`
- `RESOURCE_RESULT_IO_ERROR`
- `RESOURCE_RESULT_NOT_LOADED`
- `RESOURCE_RESULT_OUT_OF_RESOURCES`
- `RESOURCE_RESULT_STREAMBUFFER_TOO_SMALL`
- `RESOURCE_RESULT_FORMAT_ERROR`
- `RESOURCE_RESULT_CONSTANT_ERROR`
- `RESOURCE_RESULT_NOT_SUPPORTED`
- `RESOURCE_RESULT_RESOURCE_LOOP_ERROR`
- `RESOURCE_RESULT_PENDING`
- `RESOURCE_RESULT_INVALID_FILE_EXTENSION`
- `RESOURCE_RESULT_VERSION_MISMATCH`
- `RESOURCE_RESULT_SIGNATURE_MISMATCH`
- `RESOURCE_RESULT_UNKNOWN_ERROR`

### ResourceTypeCreatorDescBufferSize
*Type:* FUNCTION
Resource type creator desc byte size declaration.
The registered description data passeed to ResourceRegisterTypeCreatorDesc must be of at least this size.

### Result
*Type:* ENUM
ResourceResult

**Members**

- `RESOURCE_RESULT_OK`
- `RESOURCE_RESULT_INVALID_DATA`
- `RESOURCE_RESULT_DDF_ERROR`
- `RESOURCE_RESULT_RESOURCE_NOT_FOUND`
- `RESOURCE_RESULT_MISSING_FILE_EXTENSION`
- `RESOURCE_RESULT_ALREADY_REGISTERED`
- `RESOURCE_RESULT_INVAL`
- `RESOURCE_RESULT_UNKNOWN_RESOURCE_TYPE`
- `RESOURCE_RESULT_OUT_OF_MEMORY`
- `RESOURCE_RESULT_IO_ERROR`
- `RESOURCE_RESULT_NOT_LOADED`
- `RESOURCE_RESULT_OUT_OF_RESOURCES`
- `RESOURCE_RESULT_STREAMBUFFER_TOO_SMALL`
- `RESOURCE_RESULT_FORMAT_ERROR`
- `RESOURCE_RESULT_CONSTANT_ERROR`
- `RESOURCE_RESULT_NOT_SUPPORTED`
- `RESOURCE_RESULT_RESOURCE_LOOP_ERROR`
- `RESOURCE_RESULT_PENDING`
- `RESOURCE_RESULT_INVALID_FILE_EXTENSION`
- `RESOURCE_RESULT_VERSION_MISMATCH`
- `RESOURCE_RESULT_SIGNATURE_MISMATCH`
- `RESOURCE_RESULT_UNKNOWN_ERROR`
