# Graphics

**Namespace:** `dmGraphics`
**Language:** C++
**Type:** Defold C++
**File:** `graphics.h`
**Source:** `engine/graphics/src/dmsdk/graphics/graphics.h`
**Include:** `dmsdk/graphics/graphics.h`

Graphics API

## API

### AdapterFamily
*Type:* ENUM
Graphics adapter family.
Identifies the type of graphics backend used by the rendering system

**Members**

- `ADAPTER_FAMILY_NONE` -      No adapter detected. Used as an error state or uninitialized value
- `ADAPTER_FAMILY_NULL` -      Null (dummy) backend. Used for headless operation, testing, or environments where rendering output is not required
- `ADAPTER_FAMILY_OPENGL` -    OpenGL desktop backend. Common on Windows, macOS and Linux systems
- `ADAPTER_FAMILY_OPENGLES` -  OpenGL ES backend. Primarily used on mobile devices (Android, iOS), as well as WebGL (browser)
- `ADAPTER_FAMILY_VULKAN` -    Vulkan backend. Cross-platform modern graphics API with explicit control over GPU resources and multithreading
- `ADAPTER_FAMILY_VENDOR` -    Vendor-specific backend. A placeholder for proprietary or experimental APIs tied to a particular GPU vendor.
- `ADAPTER_FAMILY_WEBGPU` -    WebGPU backend. Modern web graphics API designed as the successor to WebGL
- `ADAPTER_FAMILY_DIRECTX` -   DirectX backend. Microsoft’s graphics API used on Windows and Xbox

### AddVertexStream
*Type:* FUNCTION
Adds a stream to a vertex stream declaration

**Parameters**

- `name` (const char*) - the name of the stream
- `size` (uint32_t) - the size of the stream, i.e number of components
- `type` (dmGraphics::Type) - the data type of the stream
- `normalize` (bool) - true if the stream should be normalized in the 0..1 range

### AddVertexStream
*Type:* FUNCTION
Adds a stream to a vertex stream declaration

**Parameters**

- `name_hash` (dmhash_t) - the name hash of the stream
- `size` (uint32_t) - the size of the stream, i.e number of components
- `type` (dmGraphics::Type) - the data type of the stream
- `normalize` (bool) - true if the stream should be normalized in the 0..1 range

### AttachmentOp
*Type:* ENUM
Defines how an attachment should be treated at the start and end of a render pass

**Members**

- `ATTACHMENT_OP_DONT_CARE` - Ignore existing content, no guarantees about the result
- `ATTACHMENT_OP_LOAD` -      Preserve the existing contents of the attachment
- `ATTACHMENT_OP_STORE` -     Store the attachment’s results after the pass finishes
- `ATTACHMENT_OP_CLEAR` -     Clear the attachment to a predefined value at the beginning of the pass

### BlendFactor
*Type:* ENUM
Blend factors for color blending.
Defines how source and destination colors are combined

**Members**

- `BLEND_FACTOR_ZERO` -                        Always use 0.0
- `BLEND_FACTOR_ONE` -                         Always use 1.0
- `BLEND_FACTOR_SRC_COLOR` -                   Use source color
- `BLEND_FACTOR_ONE_MINUS_SRC_COLOR` -         Use (1 - source color)
- `BLEND_FACTOR_DST_COLOR` -                   Use destination color
- `BLEND_FACTOR_ONE_MINUS_DST_COLOR` -         Use (1 - destination color)
- `BLEND_FACTOR_SRC_ALPHA` -                   Use source alpha
- `BLEND_FACTOR_ONE_MINUS_SRC_ALPHA` -         Use (1 - source alpha)
- `BLEND_FACTOR_DST_ALPHA` -                   Use destination alpha
- `BLEND_FACTOR_ONE_MINUS_DST_ALPHA` -         Use (1 - destination alpha)
- `BLEND_FACTOR_SRC_ALPHA_SATURATE` -          Use min(srcAlpha, 1 - dstAlpha)
- `BLEND_FACTOR_CONSTANT_COLOR`
- `BLEND_FACTOR_ONE_MINUS_CONSTANT_COLOR`
- `BLEND_FACTOR_CONSTANT_ALPHA`
- `BLEND_FACTOR_ONE_MINUS_CONSTANT_ALPHA`

### BufferAccess
*Type:* ENUM

**Members**

- `BUFFER_ACCESS_READ_ONLY`
- `BUFFER_ACCESS_WRITE_ONLY`
- `BUFFER_ACCESS_READ_WRITE`

### BufferUsage
*Type:* ENUM
Buffer usage hints.
Indicates how often the data in a buffer will be updated.
Helps the driver optimize memory placement

**Members**

- `BUFFER_USAGE_STREAM_DRAW` -     Updated every frame, used once (e.g. dynamic geometry)
- `BUFFER_USAGE_DYNAMIC_DRAW` -    Updated occasionally, used many times
- `BUFFER_USAGE_STATIC_DRAW` -     Set once, used many times (e.g. meshes, textures). Preferred for buffers that never change

### CompareFunc
*Type:* ENUM
Depth and alpha test comparison functions.
Defines how incoming values are compared against stored ones

**Members**

- `COMPARE_FUNC_NEVER` -        Never passes.
- `COMPARE_FUNC_LESS` -         Passes if incoming < stored
- `COMPARE_FUNC_LEQUAL` -       Passes if incoming <= stored
- `COMPARE_FUNC_GREATER` -      Passes if incoming > stored
- `COMPARE_FUNC_GEQUAL` -       Passes if incoming >= stored
- `COMPARE_FUNC_EQUAL` -        Passes if incoming == stored
- `COMPARE_FUNC_NOTEQUAL` -     Passes if incoming != stored
- `COMPARE_FUNC_ALWAYS` -       Always passes (ignores stored values)

### DeleteIndexBuffer
*Type:* FUNCTION
Delete the index buffer

**Parameters**

- `buffer` (dmGraphics::HIndexBuffer) - the index buffer

### DeleteRenderTarget
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `render_target` (dmGraphics::HRenderTarget)

### DeleteTexture
*Type:* FUNCTION
Delete texture

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle

### DeleteVertexBuffer
*Type:* FUNCTION
Delete vertex buffer

**Parameters**

- `buffer` (dmGraphics::HVertexBuffer) - the buffer

### DeleteVertexDeclaration
*Type:* FUNCTION
Delete vertex declaration

**Parameters**

- `vertex_declaration` (dmGraphics::HVertexDeclaration) - the vertex declaration

### DeleteVertexStreamDeclaration
*Type:* FUNCTION
Delete vertex stream declaration

**Parameters**

- `stream_declaration` (dmGraphics::HVertexStreamDeclaration) - the vertex stream declaration

### DisableState
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `state` (dmGraphics::State) - Render state

### DisableTexture
*Type:* FUNCTION
Disable a texture bound to a texture unit.
Unbinds the given texture handle from the specified unit,
releasing the association in the graphics pipeline.
This is useful to prevent unintended reuse of textures,
or to free up texture units for other bindings.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `unit` (uint32_t) - Texture unit index to disable. Must match the one previously used in <code>dmGraphics::EnableTexture</code>
- `texture` (dmGraphics::HTexture) - Handle to the texture object to disable

### EnableState
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `state` (dmGraphics::State) - Render state

### EnableTexture
*Type:* FUNCTION
Enable and bind a texture to a texture unit.
Associates a texture object with a specific texture unit in the
graphics context, making it available for sampling in shaders.
Multiple textures can be active simultaneously by binding them
to different units. The shader must reference the correct unit
(via sampler uniform) to access the bound texture

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `unit` (uint32_t) - Texture unit index to bind the texture to. Valid range depends on GPU capabilities (commonly 0–15 for at least 16 texture units)
- `id_index` (uint8_t) - Index for internal tracking or binding variation. Typically used when multiple texture IDs are managed within the same unit (e.g. array textures or multi-bind)
- `texture` (dmGraphics::HTexture) - Handle to the texture object to enable and bind

### FaceWinding
*Type:* ENUM

**Members**

- `FACE_WINDING_CCW`
- `FACE_WINDING_CW`

### GetDisplayScaleFactor
*Type:* FUNCTION
Get the scale factor of the display.
The display scale factor is usally 1.0 but will for instance be 2.0 on a macOS Retina display.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context

**Returns**

- `scale_factor` (float) - Display scale factor

### GetHeight
*Type:* FUNCTION
Returns the specified height of the opened window, which might differ from the actual window width.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context

**Returns**

- `height` (uint32_t) - Specified height of the window. If no window is opened, 0 is always returned.

### GetInstalledAdapterFamily
*Type:* FUNCTION
Get installed graphics adapter family

**Returns**

- `family` (dmGraphics::AdapterFamily) - Installed adapter family

### GetInstalledContext
*Type:* FUNCTION

**Returns**

- `context` (dmGraphics::HContext) - Installed graphics context

### GetMaxElementsIndices
*Type:* FUNCTION
Get the max number of indices allowed by the system in an index buffer

**Parameters**

- `context` (dmGraphics::HContext) - the context

**Returns**

- `count` (uint32_t) - the count

### GetMaxElementsVertices
*Type:* FUNCTION
Get the max number of vertices allowed by the system in a vertex buffer

**Parameters**

- `context` (dmGraphics::HContext) - the context

**Returns**

- `count` (uint32_t) - the count

### GetMaxTextureSize
*Type:* FUNCTION
Get maximum supported size in pixels of non-array texture

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context

**Returns**

- `max_texture_size` (uint32_t) - Maximum texture size supported by GPU

### GetNumSupportedExtensions
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - the context

**Returns**

- `count` (uint32_t) - the number of supported extensions

### GetNumTextureHandles
*Type:* FUNCTION
Get how many platform-dependent texture handle used for engine texture handle.
Applicable only for OpenGL/ES backend. All other backends return 1.

**Parameters**

- `context` (dmGraphics::Context) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle

**Returns**

- `handles_amount` (uint8_t) - Platform-dependent handles amount

### GetOriginalTextureHeight
*Type:* FUNCTION
Get texture original (before uploading to GPU) height

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle

**Returns**

- `original_height` (uint16_t)

### GetOriginalTextureWidth
*Type:* FUNCTION
Get texture original (before uploading to GPU) width

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle

**Returns**

- `original_width` (uin16_t) - Texture's original width

### GetPipelineState
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context

**Returns**

- `pipeline_state` (dmGraphics::PipelineState)

### GetRenderTargetAttachment
*Type:* FUNCTION
Get the attachment texture from a render target. Returns zero if no such attachment texture exists.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `render_target` (dmGraphics::HRenderTarget) - the render target
- `attachment_type` (dmGraphics::RenderTargetAttachment) - the attachment to get

**Returns**

- `attachment` (dmGraphics::HTexture) - the attachment texture

### GetRenderTargetSize
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `render_target` (dmGraphics::HRenderTarget)
- `buffer_type` (dmGraphics::BufferType)
- `width` (uint32_t&)
- `height` (uint32_t&)

### GetRenderTargetTexture
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `render_target` (dmGraphics::HRenderTarget)
- `buffer_type` (dmGraphics::BufferType)

**Returns**

- `render_target_texture` (dmGraphics::HTexture)

### GetSupportedExtension
*Type:* FUNCTION
get the supported extension

**Parameters**

- `context` (dmGraphics::HContext) - the context
- `index` (uint32_t) - the index of the extension

**Returns**

- `extension` (const char*) - the extension. 0 if index was out of bounds

### GetTextureDepth
*Type:* FUNCTION
Get texture depth. applicable for 3D and cube map textures

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle

**Returns**

- `depth` (uint16_t) - Texture's depth

### GetTextureFormatLiteral
*Type:* FUNCTION
Get string representation of texture format

**Parameters**

- `format` (dmGraphics::TextureFormat) - Texture format

**Returns**

- `literal_format` (const char*) - String representation of format

### GetTextureHandle
*Type:* FUNCTION
Get the native graphics API texture object from an engine texture handle. This depends on the graphics backend and is not
guaranteed to be implemented on the currently running adapter.

**Parameters**

- `texture` (dmGraphics::HTexture) - the texture handle
- `out_handle` (void**) - a pointer to where the raw object should be stored

**Returns**

- `handle_result` (dmGraphics::HandleResult) - the result of the query

### GetTextureHeight
*Type:* FUNCTION
Get texture height

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle

**Returns**

- `height` (uint16_t) - Texture's height

### GetTextureMipmapCount
*Type:* FUNCTION
Get texture mipmap count

**Parameters**

- `context` (dmGraphice::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle

**Returns**

- `count` (uint8_t) - Texture mipmap count

### GetTextureResourceSize
*Type:* FUNCTION
Get approximate size of how much memory texture consumes

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle

**Returns**

- `data_size` (uint32_t) - Resource data size in bytes

### GetTextureStatusFlags
*Type:* FUNCTION
Get status of texture

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle

**Returns**

- `flags` (dmGraphics::TextureStatusFlags) - Enumerated status bit flags

### GetTextureType
*Type:* FUNCTION
Get texture type

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle

**Returns**

- `type` (dmGraphics::TextureType) - Texture type

### GetTextureTypeLiteral
*Type:* FUNCTION
Get string representation of texture type

**Parameters**

- `texture_type` (dmGraphics::TextureType) - Texture type

**Returns**

- `literal_type` (const char*) - String representation of type

### GetTextureUsageHintFlags
*Type:* FUNCTION
Query usage hint flags for a texture.
Retrieves the bitwise usage flags that were assigned to a texture
when it was created. These flags indicate the intended role(s) of
the texture in the rendering pipeline and allow the graphics
backend to apply optimizations or enforce restrictions

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle

**Returns**

- `flags` (uint32_t) - A bitwise OR of usage flags describing how the texture may be used. Applications can test specific flags using bitmask operations

### GetTextureWidth
*Type:* FUNCTION
Get texture width

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle

**Returns**

- `width` (uint16_t) - Texture's width

### GetVertexStreamOffset
*Type:* FUNCTION
Get the physical offset into the vertex data for a particular stream

**Parameters**

- `vertex_declaration` (dmGraphics::HVertexDeclaration) - the vertex declaration
- `name_hash` (dmhash_t) - the name hash of the vertex stream (as passed into AddVertexStream())

**Returns**

- `Offset` - in bytes into the vertex or INVALID_STREAM_OFFSET if not found

### GetViewport
*Type:* FUNCTION
Get viewport's parameters

**Parameters**

- `context` (dmGraphics::HContext) - the context
- `x` (int32_t) - x-coordinate of the viewport's origin
- `y` (int32_t) - y-coordinate of the viewport's origin
- `width` (uint32_t) - viewport's width
- `height` (uint32_t) - viewport's height

### GetWidth
*Type:* FUNCTION
Returns the specified width of the opened window, which might differ from the actual window width.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context

**Returns**

- `width` (uint32_t) - Specified width of the window. If no window is opened, 0 is always returned.

### GetWindowHeight
*Type:* FUNCTION
Return the height of the opened window, if any.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context

**Returns**

- `window_height` (uint32_t) - Height of the window. If no window is opened, 0 is always returned

### GetWindowWidth
*Type:* FUNCTION
Return the width of the opened window, if any.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context

**Returns**

- `window_width` (uint32_t) - Width of the window. If no window is opened, 0 is always returned

### HandleResult
*Type:* ENUM
Function's call result code

**Members**

- `HANDLE_RESULT_OK` -             The function's call succeeded and returned a valid result
- `HANDLE_RESULT_NOT_AVAILABLE` -  The function is not supported by the current graphics backend
- `HANDLE_RESULT_ERROR` -          An error occurred while function call

### HContext
*Type:* TYPEDEF
Context handle

### HIndexBuffer
*Type:* TYPEDEF
Index buffer handle

### HPipelineState
*Type:* TYPEDEF
PipelineState handle

### HProgram
*Type:* TYPEDEF
Program handle

### HRenderTarget
*Type:* TYPEDEF
Rendertarget handle

### HStorageBuffer
*Type:* TYPEDEF
Storage buffer handle

### HTexture
*Type:* TYPEDEF
Texture handle

### HUniformLocation
*Type:* TYPEDEF
Uniform location handle

### HVertexBuffer
*Type:* TYPEDEF
Vertex buffer handle

### HVertexDeclaration
*Type:* TYPEDEF
Vertex declaration handle

### HVertexStreamDeclaration
*Type:* TYPEDEF
Vertex stream declaration handle

### IndexBufferFormat
*Type:* ENUM
Index buffer element types.
Defines the integer size used for vertex indices

**Members**

- `INDEXBUFFER_FORMAT_16` -    16-bit unsigned integers (max 65535 vertices)
- `INDEXBUFFER_FORMAT_32` -    32-bit unsigned integers (supports larger meshes)

### INVALID_STREAM_OFFSET
*Type:* CONSTANT
Invalid stream offset

### IsExtensionSupported
*Type:* FUNCTION
check if an extension is supported

**Parameters**

- `context` (dmGraphics::HContext) - the context
- `extension` (const char*) - the extension.

**Returns**

- `result` (bool) - true if the extension was supported

### IsIndexBufferFormatSupported
*Type:* FUNCTION
Check if the index format is supported

**Parameters**

- `context` (dmGraphics::HContext) - the context
- `format` (dmGraphics::IndexBufferFormat) - the format
- `result` (bool) - true if the format is supoprted

### IsTextureFormatSupported
*Type:* FUNCTION
check if a specific texture format is supported

**Parameters**

- `context` (dmGraphics::HContext) - the context
- `format` (dmGraphics::TextureFormat) - the texture format.

**Returns**

- `result` (bool) - true if the texture format was supported

### MAX_BUFFER_COLOR_ATTACHMENTS
*Type:* CONSTANT
Max buffer color attachments

### NewIndexBuffer
*Type:* FUNCTION
Create new index buffer with initial data

**Notes**

- The caller need to track if the indices are 16 or 32 bit.

**Parameters**

- `context` (dmGraphics::HContext) - the context
- `size` (uint32_t) - the size of the buffer (in bytes). May be 0
- `data` (void*) - the data
- `buffer_usage` (dmGraphics::BufferUsage) - the usage

**Returns**

- `buffer` (dmGraphics::HIndexBuffer) - the index buffer

### NewRenderTarget
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `buffer_type_flags` (uint32_t)
- `params` (dmGraphics::const RenderTargetCreationParams)

**Returns**

- `render_target` (dmGraphics::HRenderTarget) - Newly created render target

### NewTexture
*Type:* FUNCTION
Create new texture

**Parameters**

- `context` (HContext) - Graphics context
- `params` (const dmGraphics::TextureCreationParams&) - Creation parameters

**Returns**

- `texture_handle` (dmGraphics::HTexture) - Opaque texture handle

### NewVertexBuffer
*Type:* FUNCTION
Create new vertex buffer with initial data

**Parameters**

- `context` (dmGraphics::HContext) - the context
- `size` (uint32_t) - the size of the buffer (in bytes). May be 0
- `data` (void*) - the data
- `buffer_usage` (dmGraphics::BufferUsage) - the usage

**Returns**

- `buffer` (dmGraphics::HVertexBuffer) - the vertex buffer

### NewVertexDeclaration
*Type:* FUNCTION
Create new vertex declaration from a vertex stream declaration

**Parameters**

- `context` (dmGraphics::HContext) - the context
- `stream_declaration` (dmGraphics::HVertexStreamDeclaration) - the vertex stream declaration

**Returns**

- `declaration` (dmGraphics::HVertexDeclaration) - the vertex declaration

### NewVertexDeclaration
*Type:* FUNCTION
Create new vertex declaration from a vertex stream declaration and an explicit stride value,
where the stride is the number of bytes between each consecutive vertex in a vertex buffer

**Parameters**

- `context` (dmGraphics::HContext) - the context
- `stream_declaration` (dmGraphics::HVertexStreamDeclaration) - the vertex stream declaration
- `stride` (uint32_t) - the stride between the start of each vertex (in bytes)

**Returns**

- `declaration` (dmGraphics::HVertexDeclaration) - the vertex declaration

### NewVertexStreamDeclaration
*Type:* FUNCTION
Create new vertex stream declaration. A stream declaration contains a list of vertex streams
that should be used to create a vertex declaration from.

**Parameters**

- `context` (dmGraphics::HContext) - the context

**Returns**

- `declaration` (dmGraphics::HVertexStreamDeclaration) - the vertex declaration

### NewVertexStreamDeclaration
*Type:* FUNCTION
Create new vertex stream declaration. A stream declaration contains a list of vertex streams
that should be used to create a vertex declaration from.

**Parameters**

- `context` (dmGraphics::HContext) - the context
- `step_function` (dmGraphics::VertexStepFunction) - the vertex step function to use

**Returns**

- `declaration` (dmGraphics::HVertexStreamDeclaration) - the vertex declaration

### PrimitiveType
*Type:* ENUM
Primitive drawing modes.
Defines how vertex data is assembled into primitives

**Members**

- `PRIMITIVE_LINES` -          Each pair of vertices forms a line
- `PRIMITIVE_TRIANGLES` -      Each group of 3 vertices forms a triangle
- `PRIMITIVE_TRIANGLE_STRIP` - Connected strip of triangles (shares vertices)

### ReadPixels
*Type:* FUNCTION
Read frame buffer pixels in BGRA format

**Parameters**

- `context` (dmGraphics::HContext) - the context
- `x` (int32_t) - x-coordinate of the starting position
- `y` (int32_t) - y-coordinate of the starting position
- `width` (uint32_t) - width of the region
- `height` (uint32_t) - height of the region
- `buffer` (void*) - buffer to read to
- `buffer_size` (uint32_t) - buffer size

### RenderTargetAttachment
*Type:* ENUM
Attachment points for render targets

**Members**

- `ATTACHMENT_COLOR` -     A color buffer attachment (used for rendering visible output)
- `ATTACHMENT_DEPTH` -     A depth buffer attachment (used for depth testing)
- `ATTACHMENT_STENCIL` -   A stencil buffer attachment (used for stencil operations)

### RepackRGBToRGBA
*Type:* FUNCTION

**Parameters**

- `num_pixels` (uint32_t)
- `rgb` (uint8_t*)
- `rgba` (uint8_t*)

### SetBlendFunc
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `source_factor` (gmGraphics::BlendFactor)
- `destination_factor` (dmGraphics::BlendFactor)

### SetColorMask
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `red` (bool)
- `green` (bool)
- `blue` (bool)
- `alpha` (bool)

### SetCullFace
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `face_type` (dmGraphics::FaceType)

### SetDepthFunc
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `func` (dmGraphics::CompareFunc)

### SetDepthMask
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `enable_mask` (bool)

### SetIndexBufferData
*Type:* FUNCTION
Set index buffer data

**Parameters**

- `buffer` (dmGraphics::HIndexBuffer) - the buffer
- `size` (uint32_t) - the size of the buffer (in bytes). May be 0
- `data` (void*) - the data
- `buffer_usage` (dmGraphics::BufferUsage) - the usage

### SetIndexBufferSubData
*Type:* FUNCTION
Set subset of index buffer data

**Parameters**

- `buffer` (dmGraphics::HVertexBuffer) - the buffer
- `offset` (uint32_t) - the offset into the desination buffer (in bytes)
- `size` (uint32_t) - the size of the buffer (in bytes). May be 0
- `data` (void*) - the data

### SetRenderTarget
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `render_target` (dmGraphics::HRenderTarget)
- `transient_buffer_types` (uint32_t)

### SetRenderTargetSize
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `render_target` (dmGraphics::HRenderTarget)
- `width` (uint32_t)
- `height` (uint32_t)

### SetStencilFunc
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `func` (dmGraphics::CompareFunc)
- `ref` (uint32_t)
- `mask` (uint32_t)

### SetStencilFuncSeparate
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `face_type` (dmGraphics::FaceType)
- `func` (dmGraphics::CompareFunc)
- `ref` (uint32_t)
- `mask` (uint32_t)

### SetStencilMask
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `mask` (uint32_t)

### SetStencilOp
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `sfail` (dmGraphics::StencilOp)
- `dpfail` (dmGraphics::StencilOp)
- `dppass` (dmGraphics::StencilOp)

### SetStencilOpSeparate
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `face_type` (dmGraphics::FaceType)
- `sfail` (dmGraphics::StencilOp)
- `dpfail` (dmGraphics::StencilOp)
- `dppass` (dmGraphics::StencilOp)

### SetTexture
*Type:* FUNCTION
Set texture data. For textures of type TEXTURE_TYPE_CUBE_MAP it's assumed that
6 mip-maps are present contiguously in memory with stride m_DataSize

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle
- `params` (const dmGraphics::TextureParams&)

### SetTextureAsync
*Type:* FUNCTION
Set texture data asynchronously. For textures of type TEXTURE_TYPE_CUBE_MAP it's assumed that
6 mip-maps are present contiguously in memory with stride m_DataSize

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle
- `params` (const dmGraphics::TextureParams&) - Texture parameters. Texture will be recreated if parameters differ from creation parameters
- `callback` (dmGraphics::SetTextureAsyncCallback) - Completion callback
- `user_data` (void*) - User data that will be passed to completion callback

### SetTextureAsyncCallback
*Type:* TYPEDEF
Function called when a texture has been set asynchronously

**Parameters**

- `texture` (dmGraphics::HTexture) - Texture handle
- `user_data` (void*) - User data that will be passed to the SetTextureAsyncCallback

### SetTextureParams
*Type:* FUNCTION
Set texture parameters

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle
- `min_filter` (dmGraphics::TextureFilter) - Minification filter type
- `mag_filter` (dmGraphics::TextureFilter) - Magnification filter type
- `uwrap` (dmGraphics::TextureWrap) - Wrapping mode for the U (X) texture coordinate.
- `vwrap` (dmGraphics::TextureWrap) - Wrapping mode for the V (Y) texture coordinate
- `max_anisotropy` (float)

### SetVertexBufferData
*Type:* FUNCTION
Set vertex buffer data

**Parameters**

- `buffer` (dmGraphics::HVertexBuffer) - the buffer
- `size` (uint32_t) - the size of the buffer (in bytes). May be 0
- `data` (void*) - the data
- `buffer_usage` (dmGraphics::BufferUsage) - the usage

### SetVertexBufferSubData
*Type:* FUNCTION
Set subset of vertex buffer data

**Parameters**

- `buffer` (dmGraphics::HVertexBuffer) - the buffer
- `offset` (uint32_t) - the offset into the desination buffer (in bytes)
- `size` (uint32_t) - the size of the buffer (in bytes). May be 0
- `data` (void*) - the data

### StencilOp
*Type:* ENUM
Stencil test actions.
Defines what happens to a stencil buffer value depending on the outcome of the stencil/depth test.

**Members**

- `STENCIL_OP_KEEP` -            Keep the current stencil value
- `STENCIL_OP_ZERO` -            Set stencil value to 0
- `STENCIL_OP_REPLACE` -         Replace stencil value with reference value
- `STENCIL_OP_INCR` -            Increment stencil value (clamps at max)
- `STENCIL_OP_INCR_WRAP` -       Increment stencil value, wrapping around
- `STENCIL_OP_DECR` -            Decrement stencil value (clamps at 0)
- `STENCIL_OP_DECR_WRAP` -       Decrement stencil value, wrapping around
- `STENCIL_OP_INVERT` -          Bitwise invert stencil value

### TextureCreationParams
*Type:* STRUCT
Texture creation parameters.
Defines how a texture is created, initialized, and used.
This structure is typically passed when allocating GPU memory
for a new texture. It controls dimensions, format, layering,
mipmapping, and intended usage.

**Members**

- `m_Type` (dmGraphics::TextureType) - Texture type. Defines the dimensionality and interpretation of the texture (2D, 3D, cube map, array)
- `m_Width` (uint16_t) - Width of the texture in pixels at the base mip level
- `m_Height` (uint16_t) - Height of the texture in pixels at the base mip level
- `m_Depth` (uint16_t) - Depth of the texture. Used for 3D textures or texture arrays. For standard 2D textures, this is typically `1`
- `m_OriginalWidth` (uint16_t) - Width of the original source data before scaling or compression
- `m_OriginalHeight` (uint16_t) - Height of the original source data before scaling or compression
- `m_OriginalDepth` (uint16_t) - Depth of the original source data
- `m_LayerCount` (uint8_t) - Number of layers in the texture. Used for array textures (`TEXTURE_TYPE_2D_ARRAY`). For standard 2D textures, this is `1`
- `m_MipMapCount` (uint8_t) - Number of mipmap levels. A value of `1` means no mipmaps (only the base level is stored). Larger values allow for mipmapped sampling.
- `m_UsageHintBits` (uint8_t) - Bitfield of usage hints. Indicates how the texture will be used (e.g. sampling, render target, storage image). See dmGraphics::TextureUsageFlag

### TextureFilter
*Type:* ENUM
Texture filtering modes.
Controls how texels are sampled when scaling or rotating textures

**Members**

- `TEXTURE_FILTER_DEFAULT` -                   Default texture filtering mode. Depeneds on graphics backend (for example, for OpenGL - TEXTURE_FILTER_LINEAR)
- `TEXTURE_FILTER_NEAREST` -                   Nearest-neighbor sampling (blocky look, fastest)
- `TEXTURE_FILTER_LINEAR` -                    Linear interpolation between texels (smooth look)
- `TEXTURE_FILTER_NEAREST_MIPMAP_NEAREST` -    Nearest mipmap level, nearest texel
- `TEXTURE_FILTER_NEAREST_MIPMAP_LINEAR` -     Linear blend between two mipmap levels, nearest texel
- `TEXTURE_FILTER_LINEAR_MIPMAP_NEAREST` -     Nearest mipmap level, linear texel
- `TEXTURE_FILTER_LINEAR_MIPMAP_LINEAR` -      Linear blend between mipmap levels and texels (trilinear)

### TextureFormat
*Type:* ENUM
Pixel formats supported by textures.
Includes uncompressed, compressed, and floating-point variants

**Members**

- `TEXTURE_FORMAT_LUMINANCE` -            Single-channel grayscale
- `TEXTURE_FORMAT_LUMINANCE_ALPHA` -      Two-channel grayscale + alpha
- `TEXTURE_FORMAT_RGB` -                  Standard 24-bit RGB color
- `TEXTURE_FORMAT_RGBA` -                 Standard 32-bit RGBA color
- `TEXTURE_FORMAT_RGB_16BPP` -            Packed 16-bit RGB (lower precision, saves memory)
- `TEXTURE_FORMAT_RGBA_16BPP` -           Packed 16-bit RGBA
- `TEXTURE_FORMAT_DEPTH` -                Depth buffer texture (used for depth testing)
- `TEXTURE_FORMAT_STENCIL` -              Stencil buffer texture
- `TEXTURE_FORMAT_RGB_PVRTC_2BPPV1` -     PVRTC compressed RGB at 2 bits per pixel
- `TEXTURE_FORMAT_RGB_PVRTC_4BPPV1` -     PVRTC compressed RGB at 4 bits per pixel
- `TEXTURE_FORMAT_RGBA_PVRTC_2BPPV1` -    PVRTC compressed RGBA at 2 bits per pixel
- `TEXTURE_FORMAT_RGBA_PVRTC_4BPPV1` -    PVRTC compressed RGBA at 4 bits per pixel
- `TEXTURE_FORMAT_RGB_ETC1` -             ETC1 compressed RGB (no alpha support)
- `TEXTURE_FORMAT_R_ETC2` -               ETC2 single-channel
- `TEXTURE_FORMAT_RG_ETC2` -              ETC2 two-channel
- `TEXTURE_FORMAT_RGBA_ETC2` -            ETC2 four-channel (with alpha)
- `TEXTURE_FORMAT_RGBA_ASTC_4X4` -        ASTC block-compressed 4×4
- `TEXTURE_FORMAT_RGB_BC1` -              BC1/DXT1 compressed RGB
- `TEXTURE_FORMAT_RGBA_BC3` -             BC3/DXT5 compressed RGBA
- `TEXTURE_FORMAT_R_BC4` -                BC4 single-channel
- `TEXTURE_FORMAT_RG_BC5` -               BC5 two-channel
- `TEXTURE_FORMAT_RGBA_BC7` -             BC7 high-quality compressed RGBA
- `TEXTURE_FORMAT_RGB16F` -               Half-precision float RGB
- `TEXTURE_FORMAT_RGB32F` -               Full 32-bit float RGB
- `TEXTURE_FORMAT_RGBA16F` -              Half-precision float RGBA
- `TEXTURE_FORMAT_RGBA32F` -              Full 32-bit float RGBA
- `TEXTURE_FORMAT_R16F` -                 Half-precision float single channel
- `TEXTURE_FORMAT_RG16F` -                Half-precision float two channels
- `TEXTURE_FORMAT_R32F` -                 Full 32-bit float single channel
- `TEXTURE_FORMAT_RG32F` -                Full 32-bit float two channels
- `TEXTURE_FORMAT_RGBA32UI` -             Internal: 32-bit unsigned integer RGBA (not script-exposed)
- `TEXTURE_FORMAT_BGRA8U` -               Internal: 32-bit BGRA layout
- `TEXTURE_FORMAT_R32UI` -                Internal: 32-bit unsigned integer single channel
- `TEXTURE_FORMAT_RGBA_ASTC_5X4` -        ASTC 5x4 block compression
- `TEXTURE_FORMAT_RGBA_ASTC_5X5` -        ASTC 5x5 block compression
- `TEXTURE_FORMAT_RGBA_ASTC_6X5` -        ASTC 6x5 block compression
- `TEXTURE_FORMAT_RGBA_ASTC_6X6` -        ASTC 6x6 block compression
- `TEXTURE_FORMAT_RGBA_ASTC_8X5` -        ASTC 8x5 block compression
- `TEXTURE_FORMAT_RGBA_ASTC_8X6` -        ASTC 8x6 block compression
- `TEXTURE_FORMAT_RGBA_ASTC_8X8` -        ASTC 8x8 block compression
- `TEXTURE_FORMAT_RGBA_ASTC_10X5` -       ASTC 10x5 block compression
- `TEXTURE_FORMAT_RGBA_ASTC_10X6` -       ASTC 10x6 block compression
- `TEXTURE_FORMAT_RGBA_ASTC_10X8` -       ASTC 10x8 block compression
- `TEXTURE_FORMAT_RGBA_ASTC_10X10` -      ASTC 10x10 block compression
- `TEXTURE_FORMAT_RGBA_ASTC_12X10` -      ASTC 12x10 block compression
- `TEXTURE_FORMAT_RGBA_ASTC_12X12` -      ASTC 12x12 block compression

### TextureParams
*Type:* STRUCT
Texture update parameters.
Defines a block of pixel data to be uploaded to a texture,
along with filtering, wrapping, and sub-region update options.
Typically used when calling texture upload/update functions
after a texture object has been created with TextureCreationParams

**Members**

- `m_Data` (const void*) - Pointer to raw pixel data in CPU memory. The format is defined by `m_Format`
- `m_DataSize` (uint32_t) - Size of the pixel data in bytes. Must match the expected size from width, height, depth, and format
- `m_Format` (dmGraphics::TextureFormat) - Format of the pixel data (e.g. RGBA, RGB, compressed formats). Dictates how the GPU interprets the memory pointed by `m_Data`
- `m_MinFilter` (dmGraphics::TextureFilter) - Minification filter (applied when shrinking). Determines how pixels are sampled when the texture is displayed smaller than its native resolution
- `m_MagFilter` (dmGraphics::TextureFilter) - Magnification filter (applied when enlarging). Determines how pixels are sampled when the texture is displayed larger than its native resolution
- `m_UWrap` (dmGraphics::TextureWrap) - Wrapping mode for U (X) texture coordinate. Controls behavior when texture coordinates exceed [0,1]
- `m_VWrap` (dmGraphics::TextureWrap) - Wrapping mode for V (Y) texture coordinate. Controls behavior when texture coordinates exceed [0,1]
- `m_X` (uint32_t) - X offset in pixels for sub-texture updates. Defines the left edge of the destination region
- `m_Y` (uint32_t) - Y offset in pixels for sub-texture updates. Defines the top edge of the destination region
- `m_Z` (uint32_t) - Z offset (depth layer) for 3D textures. Ignored for standard 2D textures
- `m_Slice` (uint32_t) - Slice index in an array texture where the data should be uploaded
- `m_Width` (uint16_t) - Width of the pixel data block in pixels. Used for both full uploads and sub-updates
- `m_Height` (uint16_t) - Height of the pixel data block in pixels. Used for both full uploads and sub-updates
- `m_Depth` (uint16_t) - Depth of the pixel data block in pixels. Only relevant for 3D textures
- `m_LayerCount` (uint8_t) - Number of layers to update. For array textures, this specifies how many pages are updated
- `m_MipMap` (uint8_t) - Only 7 bit available Mipmap level to update. Level 0 is the base level, higher levels are progressively downscaled versions
- `m_SubUpdate` (uint8_t) - If true, this represents a partial texture update (sub-region), using `m_X`, `m_Y`, `m_Z`, and `m_Slice` offsets. If false, the entire texture/mipmap level is replaced

### TextureStatusFlags
*Type:* ENUM
Texture data upload status flags

**Members**

- `TEXTURE_STATUS_OK` -            Texture updated and ready-to-use
- `TEXTURE_STATUS_DATA_PENDING` -  Data upload to the texture is in progress

### TextureType
*Type:* ENUM
Texture types

**Members**

- `TEXTURE_TYPE_2D`
- `TEXTURE_TYPE_2D_ARRAY`
- `TEXTURE_TYPE_3D`
- `TEXTURE_TYPE_CUBE_MAP`
- `TEXTURE_TYPE_IMAGE_2D`
- `TEXTURE_TYPE_IMAGE_3D`
- `TEXTURE_TYPE_SAMPLER`
- `TEXTURE_TYPE_TEXTURE_2D`
- `TEXTURE_TYPE_TEXTURE_2D_ARRAY`
- `TEXTURE_TYPE_TEXTURE_3D`
- `TEXTURE_TYPE_TEXTURE_CUBE`

### TextureWrap
*Type:* ENUM
Texture addressing/wrapping modes.
Controls behavior when texture coordinates fall outside the [0,1] range

**Members**

- `TEXTURE_WRAP_CLAMP_TO_BORDER` -     Clamp to the color defined as 'border'
- `TEXTURE_WRAP_CLAMP_TO_EDGE` -       Clamp to the edge pixel of the texture
- `TEXTURE_WRAP_MIRRORED_REPEAT` -     Repeat texture, mirroring every other repetition
- `TEXTURE_WRAP_REPEAT` -              Repeat texture in a tiled fashion

### Type
*Type:* ENUM
Data type.
Represents scalar, vector, matrix, image, or sampler types used
for vertex attributes, uniforms, and shader interface definitions

**Members**

- `TYPE_BYTE` -                Signed 8-bit integer. Compact storage, often used for colors, normals, or compressed vertex attributes
- `TYPE_UNSIGNED_BYTE` -       Unsigned 8-bit integer. Common for color channels (0–255) or normalized texture data
- `TYPE_SHORT` -               Signed 16-bit integer. Used for medium-range numeric attributes such as bone weights or coordinates with normalization
- `TYPE_UNSIGNED_SHORT` -      Unsigned 16-bit integer. Often used for indices or normalized attributes when extra precision over bytes is required
- `TYPE_INT` -                 Signed 32-bit integer. Typically used for uniform values, shader constants, or counters
- `TYPE_UNSIGNED_INT` -        Unsigned 32-bit integer. Used for indices, IDs, or GPU counters
- `TYPE_FLOAT` -               32-bit floating point. Standard for most vertex attributes and uniform values (positions, UVs, weights)
- `TYPE_FLOAT_VEC4` -          4-component floating-point vector (`vec4` in GLSL). Typically used for homogeneous coordinates, colors (RGBA), or combined attributes
- `TYPE_FLOAT_MAT4` -          4x4 floating-point matrix (`mat4` in GLSL). Standard for 3D transformations (model, view, projection)
- `TYPE_SAMPLER_2D` -          2D texture sampler. Standard type for most texture lookups
- `TYPE_SAMPLER_CUBE` -        Cube map sampler. Used for environment mapping, reflections, and skyboxes
- `TYPE_SAMPLER_2D_ARRAY` -    Array of 2D texture samplers. Enables efficient texture indexing when using multiple layers (e.g. terrain textures, sprite atlases)
- `TYPE_FLOAT_VEC2` -          2-component floating-point vector (`vec2` in GLSL). Commonly used for texture coordinates or 2D positions
- `TYPE_FLOAT_VEC3` -          3-component floating-point vector (`vec3` in GLSL). Used for positions, normals, and directions in 3D space
- `TYPE_FLOAT_MAT2` -          2x2 floating-point matrix (`mat2` in GLSL). Used in transformations (e.g. 2D rotations, scaling)
- `TYPE_FLOAT_MAT3` -          3x3 floating-point matrix (`mat3` in GLSL). Commonly used for normal matrix calculations in lighting
- `TYPE_IMAGE_2D` -            2D image object. Unlike samplers, images allow read/write access in shaders (e.g. compute shaders or image load/store operations)
- `TYPE_TEXTURE_2D` -          2D texture object handle. Represents an actual GPU texture resource
- `TYPE_SAMPLER` -             Generic sampler handle, used as a placeholder for texture units without specifying the dimension
- `TYPE_TEXTURE_2D_ARRAY` -    2D texture array object handle
- `TYPE_TEXTURE_CUBE` -        Cube map texture object handle
- `TYPE_SAMPLER_3D` -          3D texture sampler. Used for volumetric effects, noise fields, or voxel data
- `TYPE_TEXTURE_3D` -          3D texture object handle
- `TYPE_IMAGE_3D` -            3D image object. Used for compute-based volume processing
- `TYPE_SAMPLER_3D_ARRAY` -    Array of 3D texture samplers
- `TYPE_TEXTURE_3D_ARRAY` -    3D texture array object handle
