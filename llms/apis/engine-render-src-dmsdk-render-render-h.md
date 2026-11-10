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

### DeleteRenderItem
*Type:* FUNCTION
Disables the item, invalidates its handle and releases its slot for reuse.
Call before subsequent draws and outside dispatch callbacks. User data is not
released.

**Parameters**

- `context` (dmRender::HRenderContext) - the render context
- `item` (dmRender::HRenderItem) - an item created in this context

**Returns**

- `result` (bool) - true on success, or false if the item handle is invalid or deleted

### dmRender::GetMaterialVertexSpace
*Type:* FUNCTION
Get the vertex space (local or world)

**Parameters**

- `material` (dmRender::HMaterial) - the material

**Returns**

- `vertex_space` (dmRenderDDF::MaterialDesc::VertexSpace) - the vertex space

### dmRender::RenderObject::MAX_TEXTURE_COUNT
*Type:* CONSTANT
The maximum number of textures the render object can hold (16)

### Enable
*Type:* FUNCTION
Changes draw eligibility without releasing the handle or its data. Repeating
the current enabled state has no effect. The dispatch must also be submitted
for the item to participate in the current frame.

**Parameters**

- `context` (dmRender::HRenderContext) - the render context
- `item` (dmRender::HRenderItem) - an item created in this context
- `enabled` (bool) - true to enable the item, or false to disable it

**Returns**

- `result` (bool) - true on success, or false if the item handle is invalid or deleted

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

### HLightPrototype
*Type:* TYPEDEF
Light prototype handle. Used to create light instances.

### HMaterial
*Type:* TYPEDEF
Material instance handle

### HNamedConstantBuffer
*Type:* TYPEDEF
Shader constant buffer handle. Holds name and values for a constant.

### HRenderContext
*Type:* TYPEDEF
The render context

### HRenderItem
*Type:* TYPEDEF
Identifies a renderer-owned item until DeleteRenderItem() invalidates it.
Zero is invalid. Use the handle only with the context that created it.
Create and update items before the draw that consumes them, outside render
dispatch callbacks. Item setters return false for invalid or deleted handles.

### HRenderItemDispatch
*Type:* TYPEDEF
Identifies a registration created by RegisterRenderListDispatch(). Use it
only with its creating context, and never after UnregisterRenderListDispatch().
This handle is separate from the frame-local HRenderListDispatch used in
RenderListEntry. Zero is invalid.

### HRenderListDispatch
*Type:* TYPEDEF
Render dispatch function handle.

### HSampler
*Type:* TYPEDEF
Sampler handle

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

### NewRenderItem
*Type:* FUNCTION
The new item is disabled, with an identity transform, no material tags or bounds,
and world-position ordering. Its dispatch and user data are fixed
for its lifetime. Any data referenced by user_data must outlive the item.
Creating an item does not invalidate outstanding RenderListAlloc() ranges.
Delete the item before unregistering its dispatch.

**Parameters**

- `context` (dmRender::HRenderContext) - the render context
- `dispatch` (dmRender::HRenderItemDispatch) - a registration created in this context
- `user_data` (uint64_t) - item data exposed as RenderListEntry::m_UserData in callbacks

**Returns**

- `item` (dmRender::HRenderItem) - the item handle

**Examples**

```
#include

// context, dispatch and material are owned by the component or its world.
dmRender::HRenderItem item = dmRender::NewRenderItem(context, dispatch, user_data);
dmRender::SetMaterial(context, item, material);
dmRender::SetWorldTransform(context, item, world_transform);
dmRender::SetBoundingOBB(context, item, local_min, local_max);
dmRender::Enable(context, item, true);

// In the component render callback each frame:
dmRender::SubmitRenderListDispatch(context, dispatch);

// When the component is destroyed, outside dispatch callbacks:
dmRender::DeleteRenderItem(context, item);

```

### RegisterRenderListDispatch
*Type:* FUNCTION
Callbacks and user data remain caller-owned and must stay valid until
unregistration. Register before submitting. Delete all associated items before
unregistering, after the current render list has finished drawing.

**Parameters**

- `context` (dmRender::HRenderContext) - the render context
- `dispatch_fn` (dmRender::RenderListDispatchFn) - the render batch callback
- `visibility_fn` (dmRender::RenderListVisibilityFn) - visibility callback for items without typed bounds, or 0 for always visible
- `user_data` (void*) - user data passed to both callbacks

**Returns**

- `dispatch` (dmRender::HRenderItemDispatch) - the registration, or 0 if the registration limit is reached

### RemoveNamedConstant
*Type:* FUNCTION
Removes a named constant from the buffer

**Parameters**

- `buffer` (dmRender::HNamedConstantBuffer) - the constants buffer
- `name_hash` (dmhash_t) - the name of the constant

### RENDER_CONTEXT_NAME
*Type:* CONSTANT
Name used when registering the render context with the engine context registry.

### RenderListAlloc
*Type:* FUNCTION
Allocate frame-local render entries
Deprecated: use NewRenderItem() and the render item setters. Emits a warning
once per process. Do not retain pointers across frames; another allocation
can also invalidate the returned range.

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
- `m_UserData` (void*) - the callback user data supplied to RegisterRenderListDispatch() or RenderListMakeDispatch()
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
- `m_UserData` (uint64_t) - user data (available in the render dispatch callback)
- `m_Order` (uint32_t) - the order to sort on (used if m_MajorOrder != RENDER_ORDER_WORLD)
- `m_BatchKey` (uint32_t) - the batch key to sort on (note: only 48 bits are currently used by renderer)
- `m_TagListKey` (uint32_t) - the key to the list of material tags
- `m_FrustumHash` (uint32_t) - Last combined frustum cull key (note: engine internal use only!)
- `m_MinorOrder` (uint32_t:4) - used to sort within a batch
- `m_MajorOrder` (uint32_t:2) - If RENDER_ORDER_WORLD, then sorting is done based on the world position.
Otherwise the sorting uses the m_Order value directly.
- `m_Dispatch` (uint32_t:8) - The dispatch function callback (dmRender::HRenderListDispatch)
- `m_Visibility` (uint32_t:1) - Visibility flag. Used for frustrum culling. See enum Visibility

### RenderListMakeDispatch
*Type:* FUNCTION
Register a frame-local render dispatch function
Deprecated: use RegisterRenderListDispatch() and SubmitRenderListDispatch().
Emits a warning once per process. The overload without a visibility
callback is also deprecated.

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
Submit frame-local render entries
Deprecated: use Enable() and SubmitRenderListDispatch(). Emits a warning
once per process. The range must come from a single RenderListAlloc() call.

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

- `m_UserData` (void*) - the callback user data supplied to RegisterRenderListDispatch() or RenderListMakeDispatch()
- `m_Entries` (dmRender::RenderListEntry) - the render entry array
- `m_NumEntries` (uint32_t) - the number of render entries in the array

### RenderObject
*Type:* STRUCT
Render objects represent an actual draw call

**Members**

- `m_Constants` (dmRender::HConstant[]) - the shader constants
- `m_WorldTransform` (dmVMath::Matrix4) - the world transform (usually identity for batched objects)
- `m_TextureTransform` (dmVMath::Matrix4) - the texture transform
- `m_VertexBuffer` (dmGraphics::HVertexBuffer) - the vertex buffer
- `m_VertexDeclaration` (dmGraphics::HVertexDeclaration) - the vertex declaration
- `m_IndexBuffer` (dmGraphics::HIndexBuffer) - the index buffer
- `m_Material` (dmRender::HMaterial) - the material
- `m_Textures` (dmGraphics::HTexture[]) - the textures
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

- `RENDER_ORDER_BEFORE_WORLD` - Drawn before world-sorted items
- `RENDER_ORDER_WORLD` - <div class="codehilite"><pre><span></span><code>      Used by game objects
</code></pre></div>
- `RENDER_ORDER_AFTER_WORLD` - <div class="codehilite"><pre><span></span><code>Used by gui
</code></pre></div>

### Result
*Type:* ENUM

**Members**

- `RESULT_OK`
- `RESULT_INVALID_CONTEXT`
- `RESULT_OUT_OF_RESOURCES`
- `RESULT_BUFFER_IS_FULL`
- `RESULT_INVALID_PARAMETER`

### SetBatchKey
*Type:* FUNCTION
Sets the caller's batch compatibility key. Equal keys allow batching only when
the remaining state is compatible. The renderer also separates batches by
dispatch and ordering.

**Parameters**

- `context` (dmRender::HRenderContext) - the render context
- `item` (dmRender::HRenderItem) - an item created in this context
- `key` (uint32_t) - the batch compatibility key

**Returns**

- `result` (bool) - true on success, or false if the item handle is invalid or deleted

### SetBoundingAABB
*Type:* FUNCTION
Replaces the previous volume. If any minimum coordinate exceeds its maximum,
removes typed bounds and restores the registration's visibility callback, or
always-visible behavior when no callback is registered. Equal corners define
a valid point. SetWorldTransform() does not transform this box.
Visibility is invalidated only when the volume type or values change.

**Parameters**

- `context` (dmRender::HRenderContext) - the render context
- `item` (dmRender::HRenderItem) - an item created in this context
- `world_min` (dmVMath::Vector3) - the world-space minimum corner
- `world_max` (dmVMath::Vector3) - the world-space maximum corner

**Returns**

- `result` (bool) - true on success, or false if the item handle is invalid or deleted

### SetBoundingOBB
*Type:* FUNCTION
Replaces the previous volume. Each minimum coordinate must be no greater than
its maximum coordinate. The item's world transform supplies position,
orientation and scale, including reflection and shear. Visibility is
invalidated only when the volume type or values change.

**Parameters**

- `context` (dmRender::HRenderContext) - the render context
- `item` (dmRender::HRenderItem) - an item created in this context
- `local_min` (dmVMath::Vector3) - the local-space minimum corner
- `local_max` (dmVMath::Vector3) - the local-space maximum corner

**Returns**

- `result` (bool) - true on success, or false if the item handle is invalid or deleted

### SetBoundingSphere
*Type:* FUNCTION
Replaces the previous volume. The radius is a non-negative distance, not a
squared radius. SetWorldTransform() does not move or scale this sphere.
Visibility is invalidated only when the volume type or values change.

**Parameters**

- `context` (dmRender::HRenderContext) - the render context
- `item` (dmRender::HRenderItem) - an item created in this context
- `world_center` (dmVMath::Point3) - the world-space sphere center
- `radius` (float) - the non-negative sphere radius in world units

**Returns**

- `result` (bool) - true on success, or false if the item handle is invalid or deleted

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

### SetMaterial
*Type:* FUNCTION
Copies the material's predicate tags. Call again after changing material tags
to refresh cached metadata. A null material clears the tags. The material is
not retained. Ordering is unchanged; use SetOrder() to configure it.

**Parameters**

- `context` (dmRender::HRenderContext) - the render context
- `item` (dmRender::HRenderItem) - an item created in this context
- `material` (dmRender::HMaterial) - the material supplying predicate tags, or 0 to clear them

**Returns**

- `result` (bool) - true on success, or false if the item handle is invalid or deleted

### SetMaterialSampler
*Type:* FUNCTION

**Parameters**

- `material` (dmRender::HMaterial)
- `name_hash` (dmhash_t)
- `unit` (uint32_t)
- `u_wrap` (dmGraphics::TextureWrap)
- `v_wrap` (dmGraphics::TextureWrap)
- `w_wrap` (dmGraphics::TextureWrap)
- `min_filter` (dmGraphics::TextureFilter)
- `mag_filter` (dmGraphics::TextureFilter)
- `max_anisotropy` (float)

**Returns**

- `is_succeed` (bool)

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
Currently only dmRenderDDF::MaterialDesc::CONSTANT_TYPE_USER, dmRenderDDF::MaterialDesc::CONSTANT_TYPE_USER_COLOR
and dmRenderDDF::MaterialDesc::CONSTANT_TYPE_USER_MATRIX4 are supported.

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

### SetOrder
*Type:* FUNCTION
Overrides the default world-position ordering. World order sorts by position.
Before-world and after-world order use the supplied order value; only its low
24 bits are retained. Material changes and render-script material overrides
preserve this ordering.

**Parameters**

- `context` (dmRender::HRenderContext) - the render context
- `item` (dmRender::HRenderItem) - an item created in this context
- `render_order` (dmRender::RenderOrder) - the major rendering order
- `order` (uint32_t) - the 24-bit order value, ignored for world-position sorting

**Returns**

- `result` (bool) - true on success, or false if the item handle is invalid or deleted

### SetWorldTransform
*Type:* FUNCTION
Copies the local-to-world affine transform. Its translation supplies the sort
position, and it transforms local OBB bounds. World-space sphere and AABB
bounds are unaffected. Every call invalidates cached visibility; also call
when callback-owned visibility data changes without a transform change.

**Parameters**

- `context` (dmRender::HRenderContext) - the render context
- `item` (dmRender::HRenderItem) - an item created in this context
- `world_transform` (dmVMath::Matrix4) - the affine local-to-world transform to copy

**Returns**

- `result` (bool) - true on success, or false if the item handle is invalid or deleted

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

### SubmitRenderListDispatch
*Type:* FUNCTION
Makes the registration's enabled items eligible for this frame. Call between
RenderListBegin() and RenderListEnd(), before render-script draws. Repeated
submission in one frame has no effect. Only submitted registrations consume
frame dispatch IDs; at most 255 are available, shared with legacy dispatches.
If that limit is reached, an error is logged and this submission is skipped.

**Parameters**

- `context` (dmRender::HRenderContext) - the render context
- `dispatch` (dmRender::HRenderItemDispatch) - a registration created in this context

### UnregisterRenderListDispatch
*Type:* FUNCTION
Delete all items belonging to this registration first. Call only after all
draws using the current render list have finished, before the next render list
is submitted. The registration handle becomes invalid. This does not release
caller-owned callbacks or user data.

**Parameters**

- `context` (dmRender::HRenderContext) - the render context
- `dispatch` (dmRender::HRenderItemDispatch) - a registration created in this context

### Visibility
*Type:* ENUM
Visibility status

**Members**

- `VISIBILITY_NONE`
- `VISIBILITY_FULL`
