# Resource

**Namespace:** `Resource`
**Language:** C++
**Type:** Defold C++
**File:** `resource.h`
**Source:** `engine/resource/src/dmsdk/resource/resource.h`
**Include:** `dmsdk/resource/resource.h`

Functions for managing resource types.

## API

### DM_DECLARE_RESOURCE_TYPE
*Type:* MACRO
Declare and register new resource type to the engine.
This macro is used to declare the resource type callback functions used by the engine to communicate with the extension.

**Parameters**

- `symbol` (symbol) - external extension symbol description (no quotes).
- `suffix` (const char*) - The file resource suffix, without a ".".
- `register_fn` (function(dmResource::ResourceTypeRegisterContext& ctx)) - type register function
<dl>
<dt><code>ctx</code></dt>
<dd><span class="type">dmResource::ResourceTypeRegisterContext&amp;</span> Reference to an <code>ResourceTypeRegisterContext</code> structure.</dd>
</dl>
- `deregister_fn` (function(dmResource::ResourceTypeRegisterContext& ctx)) - type deregister function. May be null.
<dl>
<dt><code>ctx</code></dt>
<dd><span class="type">dmResource::ResourceTypeRegisterContext&amp;</span> Reference to an <code>ResourceTypeRegisterContext</code> structure.</dd>
</dl>

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

static ResourceResult RegisterResourceTypeBlob(HResourceTypeContext ctx, HResourceType type)
{
    // The engine.cpp creates the contexts for our built in types.
    // Here we register a custom type
    MyContext* context = new MyContext;

    ResourceTypeSetContext(type, (void*)context);
    ResourceTypeSetCreateFn(type, MyResourceTypeScriptCreate);
    ResourceTypeSetDestroyFn(type, MyResourceTypeScriptDestroy);
    ResourceTypeSetRecreateFn(type, MyResourceTypeScriptRecreate);
}

static ResourceResult DeregisterResourceTypeBlob(HResourceTypeContext ctx, HResourceType type)
{
    MyContext* context = (MyContext*)ResourceTypeGetContext(type);
    delete context;
}

DM_DECLARE_RESOURCE_TYPE(ResourceTypeBlob, "blobc", RegisterResourceTypeBlob, DeregisterResourceTypeBlob);

```

### FResourceCreate
*Type:* TYPEDEF
Resource create function

**Parameters**

- `param` (const dmResource::ResourceCreateParams*) - Resource parameters

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

### FResourceDecrypt
*Type:* TYPEDEF
Encrypts a resource in-place

**Parameters**

- `buffer` (void*) - The input/output buffer
- `buffer_len` (uint32_t) - The size of the buffer (in bytes)

**Returns**

- `RESULT_OK` - on success

### FResourceDestroy
*Type:* TYPEDEF
Resource destroy function

**Parameters**

- `param` (const dmResource::ResourceDestroyParams*) - Resource parameters

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

### FResourcePostCreate
*Type:* TYPEDEF
Resource postcreate function

**Notes**

- returning RESOURCE_CREATE_RESULT_PENDING will result in a repeated callback the following update.

**Parameters**

- `param` (const dmResource::ResourcePostCreateParams*) - Resource parameters

**Returns**

- `result` (ResourceResult) - RESOURCE_CREATE_RESULT_OK on success or RESOURCE_CREATE_RESULT_PENDING when pending

### FResourcePreload
*Type:* TYPEDEF
Resource preloading function. This may be called from a separate loading thread
but will not keep any mutexes held while executing the call. During this call
PreloadHint can be called with the supplied hint_info handle.
If RESULT_OK is returned, the resource Create function is guaranteed to be called
with the preload_data value supplied.

**Parameters**

- `param` (const dmResource::ResourcePreloadParams*) - Resource parameters

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

### FResourceRecreate
*Type:* TYPEDEF
Resource recreate function. Recreate resource in-place.

**Notes**

- Beware that any "in flight" resource pointers to the actual resource must remain valid after this call.

**Parameters**

- `param` (const dmResource::ResourceRecreateParams*) - Resource parameters

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

### FResourceReloadedCallback
*Type:* TYPEDEF
Function called when a resource has been reloaded.

**Parameters**

- `params` (ResourceReloadedParams*) - Parameters

### FResourceTypeDeregister
*Type:* TYPEDEF
Resource type destroy function. Generally used to destroy the registered resource type context.

**Returns**

- `RESOURCE_RESULT_OK` - on success

### FResourceTypeRegister
*Type:* TYPEDEF
Resource type setup function.

**Notes**

- The type is already cerate, and name and name hash properties are valid to get using the RsourceTypeGetName()/RsourceTypeGetNameHash() functions

**Returns**

- `RESOURCE_RESULT_OK` - on success

### GetDescriptor
*Type:* FUNCTION
Get resource descriptor from resource (name)

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `path` (dmhash_t) - Resource path
- `descriptor` (HResourceDescriptor*) - Returned resource descriptor

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

### GetDescriptorByHash
*Type:* FUNCTION
Get resource descriptor from resource (name)

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `path_hash` (dmhash_t) - Resource path hash
- `descriptor` (HResourceDescriptor*) - Returned resource descriptor

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

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

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

### ResourceCreateParams
*Type:* FUNCTION
Parameters to ResourceCreate function of the resource type

**Members**

- `m_Factory` (HResourceFactory)
- `m_Context` (void*) - The context registered with the resource type
- `m_Filename` (const char*) - Path of the loaded file
- `m_Buffer` (const void*) - Buffer containing the loaded file
- `m_BufferSize` (uint32_t) - Size of data buffer (in bytes)
- `m_PreloadData` (void*) - Preloaded data from Preload phase.
- `m_Resource` (HResourceDescriptor) - The resource descriptor to update.
- `m_Type` (HResourceType) - The resource type

### ResourceCreateResource
*Type:* FUNCTION
Creates and inserts a resource into the factory

**Notes**

- The input data pointer is not stored
- The reference count is 1, so make sure it's destruction is handled

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `name` (const char*) - Resource name
- `data` (void*) - Resource data
- `data_size` (uint32_t) - Resource data size
- `resource` (void**) - (out) Stores the created resource

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

### ResourceDescriptorGetNameHash
*Type:* FUNCTION
get path hash of resource

**Parameters**

- `rd` (HResourceDescriptor) - The resource

**Returns**

- `hash` (dmhash_t) - The path hash

### ResourceDescriptorGetPrevResource
*Type:* FUNCTION
get the previous resource data

**Notes**

- only used when recreating a resource

**Parameters**

- `rd` (HResourceDescriptor) - The resource handle

**Returns**

- `resource` (void*) - The resource data

### ResourceDescriptorGetResource
*Type:* FUNCTION
get the resource data

**Parameters**

- `rd` (HResourceDescriptor) - The resource handle

**Returns**

- `resource` (void*) - The resource data

### ResourceDescriptorGetResourceSize
*Type:* FUNCTION
get the resource data size

**Parameters**

- `rd` (HResourceDescriptor) - The resource handle

**Returns**

- `size` (uint32_t) - The resource data size (in bytes)

### ResourceDescriptorGetType
*Type:* FUNCTION
get the resource type

**Parameters**

- `rd` (HResourceDescriptor) - The resource handle

**Returns**

- `resource` (HResourceType) - The resource type

### ResourceDescriptorSetPrevResource
*Type:* FUNCTION
set the previous resource data

**Notes**

- only used when recreating a resource

**Parameters**

- `rd` (HResourceDescriptor) - The resource handle
- `resource` (void*) - The resource data

### ResourceDescriptorSetResource
*Type:* FUNCTION
set the resource data

**Parameters**

- `rd` (HResourceDescriptor) - The resource handle
- `resource` (void*) - The resource data

### ResourceDescriptorSetResourceSize
*Type:* FUNCTION
set the resource data size

**Parameters**

- `rd` (HResourceDescriptor) - The resource handle
- `size` (uint32_t) - The resource data size (in bytes)

### ResourceDestroyParams
*Type:* FUNCTION
Parameters to ResourceDestroy function of the resource type

**Members**

- `m_Factory` (HResourceFactory)
- `m_Context` (void*) - The context registered with the resource type
- `m_Resource` (HResourceDescriptor) - The resource descriptor to destroy
- `m_Type` (HResourceType) - The resource type

### ResourceGet
*Type:* FUNCTION
Get (load) a resource from factory

**Notes**

- if successful, it increments the ref count by one

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `path` (const char*) - Resource path
- `resource` (void**) - Created resource

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

### ResourceGetByHash
*Type:* FUNCTION
Get a loaded resource from factory

**Notes**

- this currently doesn't load a resource
- if successful, it increments the ref count by one

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `path_hash` (dmhash_t) - Resource path hash
- `resource` (void**) - Created resource

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

### ResourceGetByHashAndExt
*Type:* FUNCTION
Get a loaded resource from factory and also verifying that it's the expected file type

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `path_hash` (dmhash_t) - Resource path hash
- `ext_hash` (dmhash_t) - Resource extension hash (e.g. "texturec", "ttf"). Must match the extension of the path.
- `resource` (void**) - Created resource

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success.
                                      RESOURCE_RESULT_INVALID_FILE_EXTENSION if the path extension doesn't match the required extension.

### ResourceGetCanonicalPath
*Type:* FUNCTION
Gets the normalized resource path: "/my//icon.texturec" -> "/my/icon.texturec". "my/icon.texturec" -> "/my/icon.texturec".

**Parameters**

- `path` (const char*) - the relative dir of the resource
- `buf` (const char*) - the output of the normalization
- `buf_len` (uint32_t) - the size of the output buffer

**Returns**

- `length` (uint32_t) - the length of the output string

### ResourceGetExtFromPath
*Type:* FUNCTION
Get a resource extension from a path, i.e "resource.ext" will return "ext".

**Parameters**

- `path` (const char*) - The path to the resource

**Returns**

- `extension` (const char*) - Pointer to extension string if an extension was found, 0 otherwise

### ResourceGetPath
*Type:* FUNCTION
Returns the canonical path hash of a resource

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `resource` (void*) - The resource pointer
- `hash` (dmhash_t*) - (out) The path hash of the resource

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

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

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

### ResourceGetTypeFromExtension
*Type:* FUNCTION
Get type from extension

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `extension` (const char*) - File extension, without leading "." character. E.g. "ttf"
- `type` (HResourceType*) - (out) returned type if successful

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

### ResourceGetTypeFromExtensionHash
*Type:* FUNCTION
Get type from extension hash

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `extension_hash` (dmhash_t) - Hash of file extension, without leading "." character. E.g. hash("ttf")
- `type` (HResourceType*) - (out) returned type if successful

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

### ResourceGetWithExt
*Type:* FUNCTION
Get (load) a resource from factory

**Notes**

- if successful, it increments the ref count by one

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `path` (const char*) - Resource path
- `ext` (const char*) - Resource extension (e.g. "texturec", "ttf"). Must match the extension of the path.
- `resource` (void**) - Created resource

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success.
                                      RESOURCE_RESULT_INVALID_FILE_EXTENSION if the path extension doesn't match the required extension.

### ResourcePostCreateParams
*Type:* FUNCTION
Parameters to ResourcePostCreate function of the resource type

**Members**

- `m_Factory` (HResourceFactory)
- `m_Context` (void*) - The context registered with the resource type
- `m_Filename` (const char*) - Path of the loaded file
- `m_PreloadData` (void*) - Preloaded data from Preload phase.
- `m_Resource` (HResourceDescriptor) - The resource descriptor to update.
- `m_Type` (HResourceType) - The resource type

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

**Members**

- `m_Factory` (HResourceFactory)
- `m_Context` (void*) - The context registered with the resource type
- `m_Filename` (const char*) - Path of the loaded file
- `m_Buffer` (const void*) - Buffer containing the loaded file
- `m_BufferSize` (uint32_t) - Size of data buffer (in bytes)
- `m_HintInfo` (HResourcePreloadHintInfo) - Hinter info. Use this when calling [ref:ResourcePreloadHint]
- `m_PreloadData` (void**) - User data that is set during the Preload phase, and passed to the Create function.
- `m_Type` (HResourceType) - The resource type

### ResourceRecreateParams
*Type:* FUNCTION
Parameters to ResourceRecreate function of the resource type

**Members**

- `m_Factory` (HResourceFactory)
- `m_Context` (void*) - The context registered with the resource type
- `m_FilenameHash` (dmhash_t) - File name hash of the data
- `m_Filename` (const char*) - Path of the loaded file
- `m_Buffer` (const void*) - Buffer containing the loaded file
- `m_BufferSize` (uint32_t) - Size of data buffer (in bytes)
- `m_Message` (const void*) - Pointer holding a precreated message
- `m_Resource` (HResourceDescriptor) - The resource descriptor to update
- `m_Type` (HResourceType) - The resource type

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

**Members**

- `m_UserData` (void*) - User data supplied when the callback was registered
- `m_FilenameHash` (dmhash_t) - File name hash of the data
- `m_Filename` (const char*) - Path of the resource, same as provided to Get() when the resource was obtained
- `m_Resource` (HResourceDescriptor) - The resource descriptor to update
- `m_Type` (HResourceType) - The resource type

### ResourceRemoveFile
*Type:* FUNCTION
Removes a previously registered file from the resource system

**Parameters**

- `factory` (HResourceFactory) - Factory handle
- `path` (const char*) - The path of the resource

**Returns**

- `result` (ResourceResult) - RESOURCE_RESULT_OK on success

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
*Type:* VARIABLE
Resource type creator desc byte size declaration.
The registered description data passeed to ResourceRegisterTypeCreatorDesc must be of at least this size.

### ResourceTypeGetContext
*Type:* FUNCTION
get context from type

**Parameters**

- `type` (HResourceType) - The type

**Returns**

- `context` (void*) - 0 if no context was registered

### ResourceTypeGetName
*Type:* FUNCTION
get registered extension name of the type

**Parameters**

- `type` (HResourceType) - The type

**Returns**

- `name` (const char*) - The name of the type (e.g. "collectionc")

### ResourceTypeGetNameHash
*Type:* FUNCTION
get registered extension name hash of the type

**Parameters**

- `type` (HResourceType) - The type

**Returns**

- `hash` (dmhash_t) - The name hash of the type (e.g. "collectionc")

### ResourceTypeSetContext
*Type:* FUNCTION
set context from type

**Parameters**

- `type` (HResourceType) - The type
- `context` (void*) - The context to associate with the type

### ResourceTypeSetCreateFn
*Type:* FUNCTION
set create function for type

**Parameters**

- `type` (HResourceType) - The type
- `fn` (FResourceCreate) - Function to be called to creating the resource

### ResourceTypeSetDestroyFn
*Type:* FUNCTION
set destroy function for type

**Parameters**

- `type` (HResourceType) - The type
- `fn` (FResourceDestroy) - Function to be called to destroy the resource

### ResourceTypeSetPostCreateFn
*Type:* FUNCTION
set post create function for type

**Parameters**

- `type` (HResourceType) - The type
- `fn` (FResourcePostCreate) - Function to be called after creating the resource

### ResourceTypeSetPreloadFn
*Type:* FUNCTION
set preload function for type

**Parameters**

- `type` (HResourceType) - The type
- `fn` (FResourcePreload) - Function to be called when loading of the resource starts

### ResourceTypeSetRecreateFn
*Type:* FUNCTION
set recreate function for type

**Parameters**

- `type` (HResourceType) - The type
- `fn` (FResourceRecreate) - Function to be called when recreating the resource
