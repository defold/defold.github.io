# Render

**Namespace:** `dmRender`
**Language:** C++
**Type:** Defold C++
**File:** `render.h`
**Source:** `engine/render/src/dmsdk/render/render.h`
**Include:** `dmsdk/render/render.h`

Api for render specific data

## API

### AddToRender
*Type:* FUNCTION
Adds a render object to the current render frame

**Parameters**

- `context` (dmRender::HRenderContext) - the context
- `ro` (dmRender::RenderObject*) - the render object

**Returns**

- `result` (dmRender::Result) - the result

### ApplyMaterialConstants
*Type:* FUNCTION

**Parameters**

- `render_context` (dmRender::HRenderContext) - Render context
- `material` (dmRender::Material)
- `render_object` (const dmRender::RenderObject*)

### ApplyMaterialSampler
*Type:* FUNCTION

**Parameters**

- `render_context` (dmRender::HRenderContext)
- `material` (dmRender::HMaterial)
- `sampler` (dmRender::HSampler)
- `value_index` (uint8_t)
- `texture` (dmGraphics::HTexture)

### ClearMaterialTags
*Type:* FUNCTION

**Parameters**

- `material` (dmRender::HMaterial)

### ClearNamedConstantBuffer
*Type:* FUNCTION
Clears a named constant buffer from any constants.

**Parameters**

- `buffer` (dmRender::HNamedConstantBuffer) - the constants buffer

### DeleteConstant
*Type:* FUNCTION
Deletes a shader program constant

**Parameters**

- `constant` (dmRender::HConstant) - The shader constant

### DeleteMaterial
*Type:* FUNCTION

**Parameters**

- `render_context` (dmRender::HRenderContext) - Render context
- `material` (dmRender::Material)

### DeleteNamedConstantBuffer
*Type:* FUNCTION
Deletes a named constant buffer

**Parameters**

- `buffer` (dmRender::HNamedConstantBuffer) - the constants buffer

### dmRender::GetMaterialVertexSpace
*Type:* FUNCTION
Get the vertex space (local or world)

**Parameters**

- `material` (dmRender::HMaterial) - the material

**Returns**

- `vertex_space` (dmRenderDDF::MaterialDesc::VertexSpace) - the vertex space

### dmRender::RenderObject::MAX_TEXTURE_COUNT
*Type:* CONSTANT
The maximum number of textures the render object can hold (currently 8)

### FrustumOptions
*Type:* STRUCT
Frustum options used when setting up a draw call

**Members**

- `m_FrustumMatrix` (matrix4) - the frustum matrix
- `m_SkipNearFarPlanes` (bool) - should the frustum culling use the near and far planes

### FrustumPlanes
*Type:* ENUM
Frustum planes to use in a frustum

**Members**

- `FRUSTUM_PLANES_SIDES`
- `FRUSTUM_PLANES_ALL`

### GetConstantLocation
*Type:* FUNCTION
Gets the shader program constant location

**Parameters**

- `constant` (dmRender::HConstant) - The shader constant

**Returns**

- `location` (int32_t) - the location

### GetConstantName
*Type:* FUNCTION
Gets the shader program constant name

**Parameters**

- `constant` (dmRender::HConstant) - The shader constant

**Returns**

- `name` (dmhash_t) - the hash name

### GetConstantName
*Type:* FUNCTION
Gets the shader program constant name

**Parameters**

- `constant` (dmRender::HConstant) - The shader constant
- `name` (dmhash_t) - the hash name

### GetConstantType
*Type:* FUNCTION
Gets the type of the constant

**Parameters**

- `constant` (dmRender::HConstant) - The shader constant

**Returns**

- `type` (dmRenderDDF::MaterialDesc::ConstantType) - the type of the constant

### GetConstantValues
*Type:* FUNCTION
Gets the shader program constant values

**Parameters**

- `constant` (dmRender::HConstant) - The shader constant
- `num_values` (uint32_t*) - (out) the array num_values

**Returns**

- `values` (dmVMath::Vector4*) - the uniform values

### GetMaterialSampler
*Type:* FUNCTION

### GetMaterialSamplerNameHash
*Type:* FUNCTION

**Parameters**

- `material` (dmRender::HMaterial)
- `unit` (uint32_t)

**Returns**

- `name_hash` (dmhash_t)

### GetMaterialSamplerUnit
*Type:* FUNCTION

**Parameters**

- `material` (dmRender::HMaterial)
- `name_hash` (dmhash_t)

**Returns**

- `sampler_unit` (uint32_t)

### GetMaterialTagListKey
*Type:* FUNCTION
Gets the key to the material tag list

**Parameters**

- `material` (dmGraphics::HMaterial) - the material

**Returns**

- `listkey` (uint32_t) - the list key

### GetNamedConstant
*Type:* FUNCTION
Gets a named constant from the buffer

**Notes**

- This give access to the internal memory of the constant

**Parameters**

- `buffer` (dmRender::HNamedConstantBuffer) - the constants buffer
- `name_hash` (dmhash_t) - the name of the constant
- `values` (dmVMath::Vector4**) - (out) the values. May not be null.
- `num_values` (uint32_t*) - (out) the number of values. May not be null.

**Returns**

- `ok` (bool) - true if constant existed.

### GetNamedConstant
*Type:* FUNCTION
Gets a named constant from the buffer - with type information

**Notes**

- This give access to the internal memory of the constant

**Parameters**

- `buffer` (dmRender::HNamedConstantBuffer) - the constants buffer
- `name_hash` (dmhash_t) - the name of the constant
- `values` (dmVMath::Vector4**) - (out) the values. May not be null.
- `num_values` (uint32_t*) - (out) the number of values. May not be null.
- `constant_type` (dmRenderDDF::MaterialDesc::ConstantType*) - (out) the constant type.

**Returns**

- `ok` (bool) - true if constant existed.

### GetNamedConstantCount
*Type:* FUNCTION
Gets number of constants in the buffer

**Parameters**

- `buffer` (dmRender::HNamedConstantBuffer) - the constants buffer

**Returns**

- `ok` (bool) - true if constant existed.

### GetViewMatrix
*Type:* FUNCTION

**Parameters**

- `render_context` (dmRender::HRenderContext) - Render context

**Returns**

- `view_matrix` (const dmVMath::Matrix4&)

### HConstant
*Type:* TYPEDEF
Shader constant handle

### HFont
*Type:* TYPEDEF
Font map handle

### HMaterial
*Type:* TYPEDEF
Material instance handle

### HNamedConstantBuffer
*Type:* TYPEDEF
Shader constant buffer handle. Holds name and values for a constant.

### HRenderContext
*Type:* TYPEDEF
The render context

### HRenderListDispatch
*Type:* TYPEDEF
Render dispatch function handle.

### IterateNamedConstants
*Type:* FUNCTION
Iterates over the constants

**Parameters**

- `buffer` (dmRender::HNamedConstantBuffer) - the constants buffer
- `callback` (IterateNamedConstantsFn) - the callback function
- `ctx` (void*) - the callback context

### IterateNamedConstantsFn
*Type:* TYPEDEF

**Parameters**

- `name_hash` (dmhash_t)
- `ctx` (void*)

### NewConstant
*Type:* FUNCTION
Creates a shader program constant

**Parameters**

- `name_hash` (dmhash_t) - the name of the material constant

**Returns**

- `constant` (dmRender::HConstant) - the constant

### NewMaterial
*Type:* FUNCTION

**Parameters**

- `render_context` (dmRender::HContext) - Render context
- `program` (dmGraphics::HProgram)

**Returns**

- `new_material` (dmRender::HMaterial)

### NewNamedConstantBuffer
*Type:* FUNCTION
Allocates a named constant buffer

**Returns**

- `buffer` (dmRender::HNamedConstantBuffer) - the constants buffer

### RemoveNamedConstant
*Type:* FUNCTION
Removes a named constant from the buffer

**Parameters**

- `buffer` (dmRender::HNamedConstantBuffer) - the constants buffer
- `name_hash` (dmhash_t) - the name of the constant

### RenderListAlloc
*Type:* FUNCTION
Allocates an array of render entries

**Notes**

- Do not store a pointer into this array, as they're reused next frame

**Parameters**

- `context` (dmRender::HRenderContext) - the context
- `entries` (uint32_t) - the number of entries to allocate

**Returns**

- `array` (dmRender::RenderListEntry*) - the render list entry array

### RenderListDispatchFn
*Type:* TYPEDEF
Render dispatch function callback.

**Parameters**

- `params` (dmRender::RenderListDispatchParams) - the params

### RenderListDispatchParams
*Type:* STRUCT
Render dispatch function callback.

**Members**

- `m_Context` (dmRender::HRenderContext) - the context
- `m_UserData` (void*) - the callback user data (registered with RenderListMakeDispatch())
- `m_Operation` (dmRender::RenderListOperation) - the operation
- `m_Buf` (dmRender::RenderListEntry) - the render entry array
- `m_Begin` (uint32_t*) - the start of the render batch. contains index into the m_Buf array
- `m_End` (uint32_t*) - the end of the render batch. Loop while "m_Begin != m_End"

### RenderListEntry
*Type:* FUNCTION
Represents a renderable object (e.g. a single sprite)
The renderer will (each frame) collect all entries with the current material tag, then batch these objects together.
Batching is done based on the batch key and Z value (or order for GUI nodes)
The caller will also register a callback function where the batched entries will be returned.
Each callback then represents a draw call, and will register a RenderObject

**Parameters**

- `m_WorldPosition` (dmVMath::Point3) - the world position of the object
- `m_Order` (uint32_t) - the order to sort on (used if m_MajorOrder != RENDER_ORDER_WORLD)
- `m_BatchKey` (uint32_t) - the batch key to sort on (note: only 48 bits are currently used by renderer)
- `m_TagListKey` (uint32_t) - the key to the list of material tags
- `m_UserData` (uint64_t) - user data (available in the render dispatch callback)
- `m_MinorOrder` (uint32_t:4) - used to sort within a batch
- `m_MajorOrder` (uint32_t:2) - If RENDER_ORDER_WORLD, then sorting is done based on the world position.
Otherwise the sorting uses the m_Order value directly.
- `m_Dispatch` (uint32_t:8) - The dispatch function callback (dmRender::HRenderListDispatch)
- `m_Visibility` (uint32_t:1) - Visibility flag. Used for frustrum culling. See enum Visibility

### RenderListMakeDispatch
*Type:* FUNCTION
Register a render dispatch function

**Parameters**

- `context` (dmRender::HRenderContext) - the context
- `dispatch_fn` (dmRender::RenderListDispatchFn) - the render batch callback function
- `visibility_fn` (dmRender::RenderListVisibilityFn) - the render list visibility callback function. May be 0
- `user_data` (void*) - userdata to the callback

**Returns**

- `dispatch` (dmRender::HRenderListDispatch) - the render dispatch function handle

### RenderListOperation
*Type:* ENUM
Render batch callback states

**Members**

- `RENDER_LIST_OPERATION_BEGIN`
- `RENDER_LIST_OPERATION_BATCH`
- `RENDER_LIST_OPERATION_END`

### RenderListSubmit
*Type:* FUNCTION
Adds a render object to the current render frame

**Parameters**

- `context` (dmRender::HRenderContext) - the context
- `begin` (dmRender::RenderListEntry*) - the start of the array
- `end` (dmRender::RenderListEntry*) - the end of the array (i.e. "while begin!=end: *begin ..."")

### RenderListVisibilityFn
*Type:* TYPEDEF
Render visibility function callback.

**Parameters**

- `params` (dmRender::RenderListVisibilityParams) - the params

### RenderListVisibilityParams
*Type:* STRUCT
Visibility dispatch function callback.

**Members**

- `m_UserData` (void*) - the callback user data (registered with RenderListMakeDispatch())
- `m_Entries` (dmRender::RenderListEntry) - the render entry array
- `m_NumEntries` (uint32_t) - the number of render entries in the array

### RenderObject
*Type:* STRUCT
Render objects represent an actual draw call

**Members**

- `m_Constants` (dmRender::HConstant[) - ] the shader constants
- `m_WorldTransform` (dmVMath::Matrix4) - the world transform (usually identity for batched objects)
- `m_TextureTransform` (dmVMath::Matrix4) - the texture transform
- `m_VertexBuffer` (dmGraphics::HVertexBuffer) - the vertex buffer
- `m_VertexDeclaration` (dmGraphics::HVertexDeclaration) - the vertex declaration
- `m_IndexBuffer` (dmGraphics::HIndexBuffer) - the index buffer
- `m_Material` (dmRender::HMaterial) - the material
- `m_Textures` (dmGraphics::HTexture[) - ] the textures
- `m_PrimitiveType` (dmGraphics::PrimitiveType) - the primitive type
- `m_IndexType` (dmGraphics::Type) - the index type (16/32 bit)
- `m_SourceBlendFactor` (dmGraphics::BlendFactor) - the source blend factor
- `m_DestinationBlendFactor` (dmGraphics::BlendFactor) - the destination blend factor
- `m_StencilTestParams` (dmRender::StencilTestParams) - the stencil test params
- `m_VertexStart` (uint32_t) - the vertex start
- `m_VertexCount` (uint32_t) - the vertex count
- `m_SetBlendFactors` (uint8_t:1) - use the blend factors
- `m_SetStencilTest` (uint8_t:1) - use the stencil test

### RenderOrder
*Type:* ENUM
Render order

**Members**

- `RENDER_ORDER_WORLD` -           Used by game objects
- `RENDER_ORDER_AFTER_WORLD` -     Used by gui

### Result
*Type:* ENUM

**Members**

- `RESULT_OK`
- `RESULT_INVALID_CONTEXT`
- `RESULT_OUT_OF_RESOURCES`
- `RESULT_BUFFER_IS_FULL`
- `RESULT_INVALID_PARAMETER`

### SetConstantLocation
*Type:* FUNCTION
Sets the shader program constant location

**Parameters**

- `constant` (dmRender::HConstant) - The shader constant
- `location` (dmGraphics::HUniformLocation) - the location

### SetConstantType
*Type:* FUNCTION
Sets the type of the constant

**Parameters**

- `constant` (dmRender::HConstant) - The shader constant
- `type` (dmRenderDDF::MaterialDesc::ConstantType) - the type of the constant

### SetConstantValues
*Type:* FUNCTION
Sets the shader program constant values

**Parameters**

- `constant` (dmRender::HConstant) - The shader constant
- `values` (dmVMath::Vector4*) - the array values
- `num_values` (uint32_t) - the array size (number of Vector4's)

**Returns**

- `result` (dmRender::Result) - the result

### SetMaterialSampler
*Type:* FUNCTION

**Parameters**

- `material` (dmRender::HMaterial)
- `name_hash` (dmhash_t)
- `unit` (uint32_t)
- `u_wrap` (dmGraphics::TextureWrap)
- `v_wrap` (dmGraphics::TextureWrap)
- `min_filter` (dmGraphics::TextureFilter)
- `mag_filter` (dmGraphics::TextureFilter)
- `max_anisotropy` (float)

**Returns**

- `is_succeed` (bool)

### SetMaterialTags
*Type:* FUNCTION

**Parameters**

- `material` (dmRender::Material)
- `tag_count` (uint32_t)
- `tags` (const dmhash_t*)

### SetNamedConstant
*Type:* FUNCTION
Sets one or more named constants to the buffer

**Parameters**

- `buffer` (dmRender::HNamedConstantBuffer) - the constants buffer
- `name_hash` (dmhash_t) - the name of the constant
- `values` (dmVMath::Vector4*) - the values
- `num_values` (uint32_t) - the number of values

### SetNamedConstant
*Type:* FUNCTION
Sets one or more named constants to the buffer with a specified data type.
Currently only dmRenderDDF::MaterialDesc::CONSTANT_TYPE_USER and dmRenderDDF::MaterialDesc::CONSTANT_TYPE_USER_MATRIX4
are supported.

**Parameters**

- `buffer` (dmRender::HNamedConstantBuffer) - the constants buffer
- `name_hash` (dmhash_t) - the name of the constant
- `values` (dmVMath::Vector4*) - the values
- `num_values` (uint32_t) - the number of values
- `constant_type` (dmRenderDDF::MaterialDesc::ConstantType) - The constant type

### SetNamedConstantAtIndex
*Type:* FUNCTION
Sets a named constant in the buffer at a specific index

**Parameters**

- `buffer` (dmRender::HNamedConstantBuffer) - the constants buffer
- `name_hash` (dmhash_t) - the name of the constant
- `value` (dmVMath::Vector4) - the value
- `value_index` (uint32_t) - the index of the value to set

**Returns**

- `result` (Result) - the result

### SetNamedConstants
*Type:* FUNCTION
Sets a list of named constants to the buffer

**Parameters**

- `buffer` (dmRender::HNamedConstantBuffer) - the constants buffer
- `constants` (dmRender::HConstant*) - the constants
- `num_constants` (uint32_t) - the number of constants

### StencilTestParams
*Type:* STRUCT
Struct holding stencil operation setup

**Members**

- `m_Func` (dmGraphics::CompareFunc) - the compare function
- `m_OpSFail` (dmGraphics::StencilOp) - the stencil fail operation
- `m_OpDPFail` (dmGraphics::StencilOp) - the depth pass fail operation
- `m_OpDPPass` (dmGraphics::StencilOp) - the depth pass pass operation
- `m_Ref` (uint8_t)
- `m_RefMask` (uint8_t)
- `m_BufferMask` (uint8_t)
- `m_ColorBufferMask` (uint8_t:4)
- `m_ClearBuffer` (uint8_t:1)

### Visibility
*Type:* ENUM
Visibility status

**Members**

- `VISIBILITY_NONE`
- `VISIBILITY_FULL`
