# PropertyContainer

**Namespace:** `dmGameObject`
**Language:** C++
**Type:** Defold C++
**File:** `gameobject_props.h`
**Source:** `engine/gameobject/src/dmsdk/gameobject/gameobject_props.h`
**Include:** `dmsdk/gameobject/gameobject_props.h`

API for game object property container

## API

### HPropertyContainer
*Type:* TYPEDEF
Opaque handle to a list of properties

### HPropertyContainerBuilder
*Type:* TYPEDEF
Opaque handle to a property container builder

### PropertyContainerBuilderParams
*Type:* STRUCT
PropertyContainerBuilderParams
Helper struct to create a property container builder.
It is required to fill out how many items of each type that is wanted.

**Parameters**

- `m_NumberCount` (int32_t) - Number of items of type float
- `m_HashCount` (int32_t) - Number of items of type dmhash_t
- `m_URLStringCount` (int32_t) - Number of items of type const char*
- `m_URLStringSize` (int32_t) - Size of all url strings combined, including null terminators
- `m_URLCount` (int32_t) - Number of items of type dmMessage::URL
- `m_Vector3Count` (int32_t) - Number of items of type vector3 (float[3])
- `m_Vector4Count` (int32_t) - Number of items of type vector4 (float[4])
- `m_QuatCount` (int32_t) - Number of items of type quaternion (float[4])
- `m_BoolCount` (int32_t) - Number of items of type bool

### PropertyContainerCopy
*Type:* FUNCTION
Allocates and copies a property container

**Parameters**

- `original` (HPropertyContainer) - The original property container

**Returns**

- `container` (HPropertyContainer) - The new property container

### PropertyContainerCreate
*Type:* FUNCTION
Creates the final property container

**Parameters**

- `builder` (HPropertyContainerBuilder) - The property container builder

**Returns**

- `container` (HPropertyContainer) - The property container

### PropertyContainerCreateBuilder
*Type:* FUNCTION
Create a property container builder with memory preallocated

**Parameters**

- `params` (PropertyContainerBuilderParams) - The params holding the memory requirements

**Returns**

- `container` (HPropertyContainerBuilder) - The builder

### PropertyContainerDestroy
*Type:* FUNCTION
Deallocates a property container

**Parameters**

- `container` (HPropertyContainer) - The property container

### PropertyContainerMerge
*Type:* FUNCTION
Merges two containers into a newly allocated container
The properties in the overrides container will take presedence.

**Parameters**

- `original` (HPropertyContainer) - The original property container
- `overrides` (HPropertyContainer) - The container with override properties

**Returns**

- `container` (HPropertyContainer) - The merged property container

### PropertyContainerPushBool
*Type:* FUNCTION
Add a property of type bool to the container

**Parameters**

- `builder` (HPropertyContainerBuilder) - The container builder
- `id` (dmhash_t) - The id of the property
- `value` (bool) - The value of the property

### PropertyContainerPushFloat
*Type:* FUNCTION
Add a property of type float to the container

**Parameters**

- `builder` (HPropertyContainerBuilder) - The container builder
- `id` (dmhash_t) - The id of the property
- `value` (float) - The value of the property

### PropertyContainerPushHash
*Type:* FUNCTION
Add a property of type dmhash_t to the container

**Parameters**

- `builder` (HPropertyContainerBuilder) - The container builder
- `id` (dmhash_t) - The id of the property
- `value` (dmhash_t) - The value of the property

### PropertyContainerPushQuat
*Type:* FUNCTION
Add a property of type float4 to the container

**Parameters**

- `builder` (HPropertyContainerBuilder) - The container builder
- `id` (dmhash_t) - The id of the property
- `values` (float*) - The value of the property (4 floats)

### PropertyContainerPushURL
*Type:* FUNCTION
Add a property of type dmMessage::URL to the container

**Parameters**

- `builder` (HPropertyContainerBuilder) - The container builder
- `id` (dmhash_t) - The id of the property
- `value` (dmMessage::URL) - The value of the property

### PropertyContainerPushURLString
*Type:* FUNCTION
Add a property of type (url) string to the container

**Parameters**

- `builder` (HPropertyContainerBuilder) - The container builder
- `id` (dmhash_t) - The id of the property
- `value` (const char*) - The value of the property

### PropertyContainerPushVector3
*Type:* FUNCTION
Add a property of type float3 to the container

**Parameters**

- `builder` (HPropertyContainerBuilder) - The container builder
- `id` (dmhash_t) - The id of the property
- `values` (float*) - The value of the property (3 floats)

### PropertyContainerPushVector4
*Type:* FUNCTION
Add a property of type float4 to the container

**Parameters**

- `builder` (HPropertyContainerBuilder) - The container builder
- `id` (dmhash_t) - The id of the property
- `values` (float*) - The value of the property (4 floats)
