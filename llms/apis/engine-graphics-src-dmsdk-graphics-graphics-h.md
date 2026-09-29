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

- `ADAPTER_FAMILY_NONE` - <div class="codehilite"><pre><span></span><code> No adapter detected. Used as an error state or uninitialized value
</code></pre></div>
- `ADAPTER_FAMILY_NULL` - <div class="codehilite"><pre><span></span><code> <span class="nv">Null</span> <span class="ss">(</span><span class="nv">dummy</span><span class="ss">)</span> <span class="nv">backend</span>. <span class="nv">Used</span> <span class="k">for</span> <span class="nv">headless</span> <span class="nv">operation</span>, <span class="nv">testing</span>, <span class="nv">or</span> <span class="nv">environments</span> <span class="nv">where</span> <span class="nv">rendering</span> <span class="nv">output</span> <span class="nv">is</span> <span class="nv">not</span> <span class="nv">required</span>
</code></pre></div>
- `ADAPTER_FAMILY_OPENGL` - OpenGL desktop backend. Common on Windows, macOS and Linux systems
- `ADAPTER_FAMILY_OPENGLES` - OpenGL ES backend. Primarily used on mobile devices (Android, iOS), as well as WebGL (browser)
- `ADAPTER_FAMILY_VULKAN` - Vulkan backend. Cross-platform modern graphics API with explicit control over GPU resources and multithreading
- `ADAPTER_FAMILY_VENDOR` - Vendor-specific backend. A placeholder for proprietary or experimental APIs tied to a particular GPU vendor.
- `ADAPTER_FAMILY_WEBGPU` - WebGPU backend. Modern web graphics API designed as the successor to WebGL
- `ADAPTER_FAMILY_DIRECTX` - DirectX backend. Microsoft’s graphics API used on Windows and Xbox
- `ADAPTER_FAMILY_METAL` - <div class="codehilite"><pre><span></span><code>Metal backend. Apples graphics API used on OSX and iOS
</code></pre></div>

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
- `ATTACHMENT_OP_LOAD` - <div class="codehilite"><pre><span></span><code> Preserve the existing contents of the attachment
</code></pre></div>
- `ATTACHMENT_OP_STORE` - <div class="codehilite"><pre><span></span><code>Store the attachment’s results after the pass finishes
</code></pre></div>
- `ATTACHMENT_OP_CLEAR` - <div class="codehilite"><pre><span></span><code>Clear the attachment to a predefined value at the beginning of the pass
</code></pre></div>

### BeginFrame
*Type:* FUNCTION
Begins frame rendering.
Prepares the graphics context for rendering a new frame.
This should be called at the start of each frame.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context

### BlendEquation
*Type:* ENUM
Blend equation operations.
Determines how source and destination colors are combined during blending

**Members**

- `BLEND_EQUATION_ADD` - <div class="codehilite"><pre><span></span><code>            Source + Destination
</code></pre></div>
- `BLEND_EQUATION_SUBTRACT` - <div class="codehilite"><pre><span></span><code>       Source - Destination
</code></pre></div>
- `BLEND_EQUATION_REVERSE_SUBTRACT` - Destination - Source
- `BLEND_EQUATION_MIN` - <div class="codehilite"><pre><span></span><code>            Min(Source, Destination)
</code></pre></div>
- `BLEND_EQUATION_MAX` - <div class="codehilite"><pre><span></span><code>            Max(Source, Destination)
</code></pre></div>

### BlendFactor
*Type:* ENUM
Blend factors for color blending.
Defines how source and destination colors are combined

**Members**

- `BLEND_FACTOR_ZERO` - <div class="codehilite"><pre><span></span><code>                   Always use 0.0
</code></pre></div>
- `BLEND_FACTOR_ONE` - <div class="codehilite"><pre><span></span><code>                    Always use 1.0
</code></pre></div>
- `BLEND_FACTOR_SRC_COLOR` - <div class="codehilite"><pre><span></span><code>              Use source color
</code></pre></div>
- `BLEND_FACTOR_ONE_MINUS_SRC_COLOR` - <div class="codehilite"><pre><span></span><code>    Use (1 - source color)
</code></pre></div>
- `BLEND_FACTOR_DST_COLOR` - <div class="codehilite"><pre><span></span><code>              Use destination color
</code></pre></div>
- `BLEND_FACTOR_ONE_MINUS_DST_COLOR` - <div class="codehilite"><pre><span></span><code>    Use (1 - destination color)
</code></pre></div>
- `BLEND_FACTOR_SRC_ALPHA` - <div class="codehilite"><pre><span></span><code>              Use source alpha
</code></pre></div>
- `BLEND_FACTOR_ONE_MINUS_SRC_ALPHA` - <div class="codehilite"><pre><span></span><code>    Use (1 - source alpha)
</code></pre></div>
- `BLEND_FACTOR_DST_ALPHA` - <div class="codehilite"><pre><span></span><code>              Use destination alpha
</code></pre></div>
- `BLEND_FACTOR_ONE_MINUS_DST_ALPHA` - <div class="codehilite"><pre><span></span><code>    Use (1 - destination alpha)
</code></pre></div>
- `BLEND_FACTOR_SRC_ALPHA_SATURATE` - <div class="codehilite"><pre><span></span><code>     Use min(srcAlpha, 1 - dstAlpha)
</code></pre></div>
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

- `BUFFER_USAGE_STREAM_DRAW` - <div class="codehilite"><pre><span></span><code>Updated every frame, used once (e.g. dynamic geometry)
</code></pre></div>
- `BUFFER_USAGE_DYNAMIC_DRAW` - Updated occasionally, used many times
- `BUFFER_USAGE_STATIC_DRAW` - <div class="codehilite"><pre><span></span><code><span class="nv">Set</span> <span class="nv">once</span>, <span class="nv">used</span> <span class="nv">many</span> <span class="nv">times</span> <span class="ss">(</span><span class="nv">e</span>.<span class="nv">g</span>. <span class="nv">meshes</span>, <span class="nv">textures</span><span class="ss">)</span>. <span class="nv">Preferred</span> <span class="k">for</span> <span class="nv">buffers</span> <span class="nv">that</span> <span class="nv">never</span> <span class="nv">change</span>
</code></pre></div>

### Clear
*Type:* FUNCTION
Clears the render target buffers.
Fills the specified buffers with predefined values. Commonly used at the
beginning of a frame to clear the screen to a specific color and depth.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `flags` (uint32_t) - Bitmask specifying which buffers to clear (BUFFER_TYPE_*)
- `red` (uint8_t) - Red component value (0-255)
- `green` (uint8_t) - Green component value (0-255)
- `blue` (uint8_t) - Blue component value (0-255)
- `alpha` (uint8_t) - Alpha component value (0-255)
- `depth` (float) - Depth value to clear depth buffer to
- `stencil` (uint32_t) - Stencil value to clear stencil buffer to

### CloseWindow
*Type:* FUNCTION
Closes the window associated with the graphics context.
If a window is open, this will close it and clean up associated resources.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context

### CompareFunc
*Type:* ENUM
Depth and alpha test comparison functions.
Defines how incoming values are compared against stored ones

**Members**

- `COMPARE_FUNC_NEVER` - <div class="codehilite"><pre><span></span><code>   Never passes.
</code></pre></div>
- `COMPARE_FUNC_LESS` - <div class="codehilite"><pre><span></span><code>    <span class="nv">Passes</span> <span class="k">if</span> <span class="nv">incoming</span> <span class="o">&lt;</span> <span class="nv">stored</span>
</code></pre></div>
- `COMPARE_FUNC_LEQUAL` - <div class="codehilite"><pre><span></span><code>  <span class="nv">Passes</span> <span class="k">if</span> <span class="nv">incoming</span> <span class="o">&lt;=</span> <span class="nv">stored</span>
</code></pre></div>
- `COMPARE_FUNC_GREATER` - <div class="codehilite"><pre><span></span><code> <span class="nv">Passes</span> <span class="k">if</span> <span class="nv">incoming</span> <span class="o">&gt;</span> <span class="nv">stored</span>
</code></pre></div>
- `COMPARE_FUNC_GEQUAL` - <div class="codehilite"><pre><span></span><code>  <span class="nv">Passes</span> <span class="k">if</span> <span class="nv">incoming</span> <span class="o">&gt;=</span> <span class="nv">stored</span>
</code></pre></div>
- `COMPARE_FUNC_EQUAL` - <div class="codehilite"><pre><span></span><code>   <span class="nv">Passes</span> <span class="k">if</span> <span class="nv">incoming</span> <span class="o">==</span> <span class="nv">stored</span>
</code></pre></div>
- `COMPARE_FUNC_NOTEQUAL` - <div class="codehilite"><pre><span></span><code><span class="nv">Passes</span> <span class="k">if</span> <span class="nv">incoming</span> <span class="o">!=</span> <span class="nv">stored</span>
</code></pre></div>
- `COMPARE_FUNC_ALWAYS` - <div class="codehilite"><pre><span></span><code>  Always passes (ignores stored values)
</code></pre></div>

### ContextParams
*Type:* STRUCT
Graphics context creation parameters.
Defines the configuration for creating a new graphics context.
This structure is used when initializing the graphics system and
specifies window association, job system context, texture filtering defaults,
resolution, memory limits, and various debugging/validation options.

**Members**

- `m_Window` (dmPlatform::HWindow) - Platform window handle to associate with the graphics context
- `m_JobContext` (dmJobSystem::HJobContext) - Job system context for asynchronous operations
- `m_DefaultTextureMinFilter` (dmGraphics::TextureFilter) - Default minification filter for textures
- `m_DefaultTextureMagFilter` (dmGraphics::TextureFilter) - Default magnification filter for textures
- `m_Width` (uint32_t) - Initial width of the rendering surface
- `m_Height` (uint32_t) - Initial height of the rendering surface
- `m_GraphicsMemorySize` (uint32_t) - Maximum allowed graphics memory in bytes (0 for default/unlimited) (Switch)
- `m_SwapInterval` (uint32_t) - Vertical synchronization interval (1 for 60Hz, 2 for 30Hz, etc.) (Default = 1)
- `m_GraphicsApiVersionMajorHint` (uint16_t) - Requested graphics API major version hint. A value of 0 lets the platform use its default.
- `m_GraphicsApiVersionMinorHint` (uint16_t) - Requested graphics API minor version hint.
- `m_VerifyGraphicsCalls` (bool) - Enable API call verification for debugging
- `m_PrintDeviceInfo` (bool) - Print graphics device information at startup
- `m_UseValidationLayers` (bool) - Enable validation layers for debugging (Vulkan/DirectX 12 only)

### DeleteContext
*Type:* FUNCTION
Destroys a graphics context.
Cleans up all resources associated with the graphics context.
The context becomes invalid after this call.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context to destroy

### DeleteIndexBuffer
*Type:* FUNCTION
Delete the index buffer

**Parameters**

- `buffer` (dmGraphics::HIndexBuffer) - the index buffer

### DeleteProgram
*Type:* FUNCTION
Destroys a shader program and frees associated resources.
Cleans up GPU memory and resources associated with the program handle.
The handle becomes invalid after this call.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `program` (dmGraphics::HProgram) - Program handle to destroy

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

### DisableProgram
*Type:* FUNCTION
Deactivates the currently bound shader program.
Unbinds any active program from the graphics pipeline, returning to the default state
where no custom shader program is active.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context

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

### DisableVertexBuffer
*Type:* FUNCTION
Unbinds a vertex buffer from the graphics pipeline.
Removes the association between a vertex buffer and its binding index,
freeing up the binding slot for other buffers.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `vertex_buffer` (dmGraphics::HVertexBuffer) - Vertex buffer handle to unbind

### DisableVertexDeclaration
*Type:* FUNCTION
Unbinds a vertex declaration from the graphics pipeline.
Removes the association between a vertex declaration and its binding index,
freeing up the binding slot for other declarations.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `vertex_declaration` (dmGraphics::HVertexDeclaration) - Vertex declaration handle to unbind

### Draw
*Type:* FUNCTION
Draws non-indexed primitives.
Renders geometry using vertex data directly from the bound vertex buffers
without index buffer indirection. The vertices are processed sequentially
from the specified starting point.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `prim_type` (dmGraphics::PrimitiveType) - Type of primitives to draw
- `first` (uint32_t) - Index of the first vertex to draw
- `count` (uint32_t) - Number of vertices to draw
- `instance_count` (uint32_t) - Number of instances to draw (for instanced rendering)

### DrawElements
*Type:* FUNCTION
Draws indexed primitives.
Renders geometry using indices from the supplied index buffer. The first
argument is a byte offset into the index buffer.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `prim_type` (dmGraphics::PrimitiveType) - Type of primitives to draw
- `first` (uint32_t) - Byte offset of the first index to draw
- `count` (uint32_t) - Number of indices to draw
- `type` (dmGraphics::Type) - Index element type
- `index_buffer` (dmGraphics::HIndexBuffer) - Index buffer handle
- `instance_count` (uint32_t) - Number of instances to draw (for instanced rendering)

### EnableProgram
*Type:* FUNCTION
Activates a shader program for rendering.
Binds the specified program to the graphics pipeline, making it the active program
for all subsequent rendering operations until another program is activated or disabled.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `program` (dmGraphics::HProgram) - Program handle to activate

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

### EnableVertexBuffer
*Type:* FUNCTION
Binds a vertex buffer for rendering.
Associates a vertex buffer with a specific binding index in the graphics pipeline.
The buffer provides the actual vertex data that will be processed according to
the active vertex declaration for that binding index.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `vertex_buffer` (dmGraphics::HVertexBuffer) - Vertex buffer handle
- `binding_index` (uint32_t) - Binding index to associate with this buffer

### EnableVertexDeclaration
*Type:* FUNCTION
Binds a vertex declaration for rendering.
Associates a vertex declaration with a specific binding index in the graphics pipeline.
The declaration defines how vertex data is interpreted and laid out in memory.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `vertex_declaration` (dmGraphics::HVertexDeclaration) - Vertex declaration handle
- `binding_index` (uint32_t) - Binding index to associate with this declaration
- `base_offset` (uint32_t) - Byte offset to add to all vertex attribute pointers
- `program` (dmGraphics::HProgram) - Shader program to use with this declaration

### FaceWinding
*Type:* ENUM

**Members**

- `FACE_WINDING_CCW`
- `FACE_WINDING_CW`

### Finalize
*Type:* FUNCTION
Finalizes the graphics system.
Cleans up global graphics resources and shuts down the graphics system.
This should be called when the application is exiting.

### FindUniformLocation
*Type:* FUNCTION
Finds the location of a uniform variable in a shader program by name hash.
Returns the uniform location that can be used with other uniform-setting functions.
This is the preferred method when the uniform name is known at compile time
as it avoids runtime string hashing.

**Parameters**

- `program` (dmGraphics::HProgram) - Shader program handle
- `name_hash` (dmhash_t) - Hash of the uniform variable name

**Returns**

- `location` (dmGraphics::HUniformLocation) - Uniform location handle, or INVALID_UNIFORM_LOCATION if not found

### FindUniformLocation
*Type:* FUNCTION
Finds the location of a uniform variable in a shader program by name string.
Returns the uniform location that can be used with other uniform-setting functions.
This method is useful when the uniform name is only known at runtime.

**Parameters**

- `program` (dmGraphics::HProgram) - Shader program handle
- `name` (const char*) - Name of the uniform variable

**Returns**

- `location` (dmGraphics::HUniformLocation) - Uniform location handle, or INVALID_UNIFORM_LOCATION if not found

### Flip
*Type:* FUNCTION
Flips screen buffers.
Presents the rendered frame to the display.
This should be called at the end of each frame after all rendering is complete.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context

### GetAdapterFamily
*Type:* FUNCTION
Gets the adapter family from a string name.
Converts a string identifier to the corresponding AdapterFamily enum value.

**Parameters**

- `adapter_name` (const char*) - String name of the adapter (e.g., "opengl", "vulkan")

**Returns**

- `family` (dmGraphics::AdapterFamily) - Corresponding adapter family enum value

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

### GetRenderTargetSampleCount
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `render_target` (dmGraphics::HRenderTarget)

**Returns**

- `sample_count` (uint32_t) - the effective, adapter-conformed sample count

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

### GRAPHICS_CONTEXT_NAME
*Type:* CONSTANT
Name used when registering the graphics context with the engine context registry.

### HandleResult
*Type:* ENUM
Function's call result code

**Members**

- `HANDLE_RESULT_OK` - <div class="codehilite"><pre><span></span><code>        The function&#39;s call succeeded and returned a valid result
</code></pre></div>
- `HANDLE_RESULT_NOT_AVAILABLE` - The function is not supported by the current graphics backend
- `HANDLE_RESULT_ERROR` - <div class="codehilite"><pre><span></span><code>     <span class="nv">An</span> <span class="nv">error</span> <span class="nv">occurred</span> <span class="k">while</span> <span class="nv">function</span> <span class="nv">call</span>
</code></pre></div>

### HContext
*Type:* TYPEDEF
Context handle

### HIndexBuffer
*Type:* TYPEDEF
Index buffer handle

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

- `INDEXBUFFER_FORMAT_16` - 16-bit unsigned integers (max 65535 vertices)
- `INDEXBUFFER_FORMAT_32` - 32-bit unsigned integers (supports larger meshes)

### InstallAdapter
*Type:* FUNCTION
Installs a graphics adapter.
Initializes the specified graphics backend (OpenGL, Vulkan, etc.).
This must be called before creating any graphics context.

**Parameters**

- `family` (dmGraphics::AdapterFamily) - Graphics adapter family to install

**Returns**

- `success` (bool) - True if the adapter was successfully installed, false otherwise

### INVALID_PROGRAM_HANDLE
*Type:* CONSTANT
Invalid program handle constant.
Used to represent an uninitialized or invalid program handle.
Can be used to check if program creation or loading failed.

### INVALID_STREAM_OFFSET
*Type:* CONSTANT
Invalid stream offset

### INVALID_UNIFORM_LOCATION
*Type:* CONSTANT
Invalid uniform location constant.
Used to represent an uninitialized or invalid uniform location.
Can be used to check if uniform location lookup failed.

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

### NewContext
*Type:* FUNCTION
Creates a new graphics context.
Initializes the graphics system with the specified parameters.
Only one graphics context can be active at a time.

**Parameters**

- `params` (const dmGraphics::ContextParams&) - Context creation parameters

**Returns**

- `context` (dmGraphics::HContext) - New graphics context handle, or null on failure

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

### NewProgram
*Type:* FUNCTION
Creates a new shader program from a shader description.
Compiles and links shader sources defined in the ShaderDesc into a GPU program.
Returns a program handle that can be used for rendering.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `ddf` (dmGraphics::ShaderDesc*) - Shader description containing source code and parameters
- `error_buffer` (char*) - Buffer to receive error messages (can be null)
- `error_buffer_size` (uint32_t) - Size of the error buffer

**Returns**

- `program` (dmGraphics::HProgram) - New program handle, or INVALID_PROGRAM_HANDLE on failure

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

- `PRIMITIVE_LINES` - <div class="codehilite"><pre><span></span><code>     Each pair of vertices forms a line
</code></pre></div>
- `PRIMITIVE_TRIANGLES` - <div class="codehilite"><pre><span></span><code> Each group of 3 vertices forms a triangle
</code></pre></div>
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

- `ATTACHMENT_COLOR` - <div class="codehilite"><pre><span></span><code><span class="nv">A</span> <span class="nv">color</span> <span class="nv">buffer</span> <span class="nv">attachment</span> <span class="ss">(</span><span class="nv">used</span> <span class="k">for</span> <span class="nv">rendering</span> <span class="nv">visible</span> <span class="nv">output</span><span class="ss">)</span>
</code></pre></div>
- `ATTACHMENT_DEPTH` - <div class="codehilite"><pre><span></span><code><span class="nv">A</span> <span class="nv">depth</span> <span class="nv">buffer</span> <span class="nv">attachment</span> <span class="ss">(</span><span class="nv">used</span> <span class="k">for</span> <span class="nv">depth</span> <span class="nv">testing</span><span class="ss">)</span>
</code></pre></div>
- `ATTACHMENT_STENCIL` - A stencil buffer attachment (used for stencil operations)

### RepackRGBToRGBA
*Type:* FUNCTION

**Parameters**

- `num_pixels` (uint32_t)
- `rgb` (uint8_t*)
- `rgba` (uint8_t*)

### SetBlendEquationSeparate
*Type:* FUNCTION
Set separate blend equations for color and alpha channels.

**Parameters**

- `context` (dmGraphics::HContext)
- `equation_color` (dmGraphics::BlendEquation)
- `equation_alpha` (dmGraphics::BlendEquation)

### SetBlendFunc
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `source_factor` (gmGraphics::BlendFactor)
- `destination_factor` (dmGraphics::BlendFactor)

### SetBlendFuncSeparate
*Type:* FUNCTION
Set separate blend factors for color and alpha channels.

**Parameters**

- `context` (dmGraphics::HContext)
- `src_factor_color` (dmGraphics::BlendFactor)
- `dst_factor_color` (dmGraphics::BlendFactor)
- `src_factor_alpha` (dmGraphics::BlendFactor)
- `dst_factor_alpha` (dmGraphics::BlendFactor)

### SetColorMask
*Type:* FUNCTION

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `red` (bool)
- `green` (bool)
- `blue` (bool)
- `alpha` (bool)

### SetConstantM4
*Type:* FUNCTION
Sets one or more mat4 uniform values.
Updates a shader uniform or uniform-buffer member starting at the supplied
uniform location.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `data` (const dmVMath::Matrix4*) - Matrix data to upload
- `count` (int) - Number of mat4 values to upload
- `base_location` (dmGraphics::HUniformLocation) - Uniform location

### SetConstantV4
*Type:* FUNCTION
Sets one or more vec4 uniform values.
Updates a shader uniform or uniform-buffer member starting at the supplied
uniform location.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `data` (const dmVMath::Vector4*) - Vector data to upload
- `count` (int) - Number of vec4 values to upload
- `base_location` (dmGraphics::HUniformLocation) - Uniform location

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

### SetSampler
*Type:* FUNCTION
Binds a texture sampler to a texture unit.
Associates a texture with a specific sampler uniform in the shader,
allowing the shader to access the texture data during rendering.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `location` (dmGraphics::HUniformLocation) - Uniform location of the sampler
- `unit` (int32_t) - Texture unit index to bind to

### SetScissor
*Type:* FUNCTION
Sets the scissor rectangle for rendering.
Defines the rectangular pixel region that rendering is clipped to when
STATE_SCISSOR_TEST is enabled.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `x` (int32_t) - X coordinate of the scissor rectangle's origin (in pixels)
- `y` (int32_t) - Y coordinate of the scissor rectangle's origin (in pixels)
- `width` (int32_t) - Width of the scissor rectangle (in pixels)
- `height` (int32_t) - Height of the scissor rectangle (in pixels)

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
Set texture parameters, including the W wrapping mode used by 3D textures.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle
- `min_filter` (dmGraphics::TextureFilter) - Minification filter type
- `mag_filter` (dmGraphics::TextureFilter) - Magnification filter type
- `uwrap` (dmGraphics::TextureWrap) - Wrapping mode for the U (X) texture coordinate.
- `vwrap` (dmGraphics::TextureWrap) - Wrapping mode for the V (Y) texture coordinate
- `wwrap` (dmGraphics::TextureWrap) - Wrapping mode for the W (Z) texture coordinate
- `max_anisotropy` (float)

### SetTextureParams
*Type:* FUNCTION
Set texture parameters using the legacy U/V wrapping interface.
The U wrapping mode is also applied to the W texture coordinate.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `texture` (dmGraphics::HTexture) - Texture handle
- `min_filter` (dmGraphics::TextureFilter) - Minification filter type
- `mag_filter` (dmGraphics::TextureFilter) - Magnification filter type
- `uwrap` (dmGraphics::TextureWrap) - Wrapping mode for the U (X) and W (Z) texture coordinates
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

### SetViewport
*Type:* FUNCTION
Sets the viewport for rendering.
Defines the affine transformation from normalized device coordinates to window coordinates.
This affects all subsequent rendering operations.

**Parameters**

- `context` (dmGraphics::HContext) - Graphics context
- `x` (int32_t) - X coordinate of the viewport's origin (in pixels)
- `y` (int32_t) - Y coordinate of the viewport's origin (in pixels)
- `width` (int32_t) - Width of the viewport (in pixels)
- `height` (int32_t) - Height of the viewport (in pixels)

### ShaderDesc
*Type:* STRUCT
Shader program description (from graphics_ddf.h)

### StencilOp
*Type:* ENUM
Stencil test actions.
Defines what happens to a stencil buffer value depending on the outcome of the stencil/depth test.

**Members**

- `STENCIL_OP_KEEP` - <div class="codehilite"><pre><span></span><code>       Keep the current stencil value
</code></pre></div>
- `STENCIL_OP_ZERO` - <div class="codehilite"><pre><span></span><code>       Set stencil value to 0
</code></pre></div>
- `STENCIL_OP_REPLACE` - <div class="codehilite"><pre><span></span><code>    Replace stencil value with reference value
</code></pre></div>
- `STENCIL_OP_INCR` - <div class="codehilite"><pre><span></span><code>       Increment stencil value (clamps at max)
</code></pre></div>
- `STENCIL_OP_INCR_WRAP` - <div class="codehilite"><pre><span></span><code>  Increment stencil value, wrapping around
</code></pre></div>
- `STENCIL_OP_DECR` - <div class="codehilite"><pre><span></span><code>       Decrement stencil value (clamps at 0)
</code></pre></div>
- `STENCIL_OP_DECR_WRAP` - <div class="codehilite"><pre><span></span><code>  Decrement stencil value, wrapping around
</code></pre></div>
- `STENCIL_OP_INVERT` - <div class="codehilite"><pre><span></span><code>     Bitwise invert stencil value
</code></pre></div>

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
- `m_Depth` (uint16_t) - Depth of the texture. Used for 3D textures or texture arrays. For standard 2D textures, this is typically <code>1</code>
- `m_OriginalWidth` (uint16_t) - Width of the original source data before scaling or compression
- `m_OriginalHeight` (uint16_t) - Height of the original source data before scaling or compression
- `m_OriginalDepth` (uint16_t) - Depth of the original source data
- `m_LayerCount` (uint8_t) - Number of layers in the texture. Used for array textures (<code>TEXTURE_TYPE_2D_ARRAY</code>). For standard 2D textures, this is <code>1</code>
- `m_MipMapCount` (uint8_t) - Number of mipmap levels. A value of <code>1</code> means no mipmaps (only the base level is stored). Larger values allow for mipmapped sampling.
- `m_UsageHintBits` (uint8_t) - Bitfield of usage hints. Indicates how the texture will be used (e.g. sampling, render target, storage image). See dmGraphics::TextureUsageFlag

### TextureFilter
*Type:* ENUM
Texture filtering modes.
Controls how texels are sampled when scaling or rotating textures

**Members**

- `TEXTURE_FILTER_DEFAULT` - <div class="codehilite"><pre><span></span><code>              <span class="nv">Default</span> <span class="nv">texture</span> <span class="nv">filtering</span> <span class="nv">mode</span>. <span class="nv">Depeneds</span> <span class="nv">on</span> <span class="nv">graphics</span> <span class="nv">backend</span> <span class="ss">(</span><span class="k">for</span> <span class="nv">example</span>, <span class="k">for</span> <span class="nv">OpenGL</span> <span class="o">-</span> <span class="nv">TEXTURE_FILTER_LINEAR</span><span class="ss">)</span>
</code></pre></div>
- `TEXTURE_FILTER_NEAREST` - <div class="codehilite"><pre><span></span><code>              Nearest-neighbor sampling (blocky look, fastest)
</code></pre></div>
- `TEXTURE_FILTER_LINEAR` - <div class="codehilite"><pre><span></span><code>               Linear interpolation between texels (smooth look)
</code></pre></div>
- `TEXTURE_FILTER_NEAREST_MIPMAP_NEAREST` - Nearest mipmap level, nearest texel
- `TEXTURE_FILTER_NEAREST_MIPMAP_LINEAR` - <div class="codehilite"><pre><span></span><code>Linear blend between two mipmap levels, nearest texel
</code></pre></div>
- `TEXTURE_FILTER_LINEAR_MIPMAP_NEAREST` - <div class="codehilite"><pre><span></span><code>Nearest mipmap level, linear texel
</code></pre></div>
- `TEXTURE_FILTER_LINEAR_MIPMAP_LINEAR` - <div class="codehilite"><pre><span></span><code> Linear blend between mipmap levels and texels (trilinear)
</code></pre></div>

### TextureFormat
*Type:* ENUM
Pixel formats supported by textures.
Includes uncompressed, compressed, and floating-point variants

**Members**

- `TEXTURE_FORMAT_LUMINANCE` - <div class="codehilite"><pre><span></span><code>       Single-channel grayscale
</code></pre></div>
- `TEXTURE_FORMAT_LUMINANCE_ALPHA` - <div class="codehilite"><pre><span></span><code> Two-channel grayscale + alpha
</code></pre></div>
- `TEXTURE_FORMAT_RGB` - <div class="codehilite"><pre><span></span><code>             Standard 24-bit RGB color
</code></pre></div>
- `TEXTURE_FORMAT_RGBA` - <div class="codehilite"><pre><span></span><code>            Standard 32-bit RGBA color
</code></pre></div>
- `TEXTURE_FORMAT_RGB_16BPP` - <div class="codehilite"><pre><span></span><code>       Packed 16-bit RGB (lower precision, saves memory)
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_16BPP` - <div class="codehilite"><pre><span></span><code>      Packed 16-bit RGBA
</code></pre></div>
- `TEXTURE_FORMAT_DEPTH` - <div class="codehilite"><pre><span></span><code>           <span class="nv">Depth</span> <span class="nv">buffer</span> <span class="nv">texture</span> <span class="ss">(</span><span class="nv">used</span> <span class="k">for</span> <span class="nv">depth</span> <span class="nv">testing</span><span class="ss">)</span>
</code></pre></div>
- `TEXTURE_FORMAT_STENCIL` - <div class="codehilite"><pre><span></span><code>         Stencil buffer texture
</code></pre></div>
- `TEXTURE_FORMAT_RGB_PVRTC_2BPPV1` - <div class="codehilite"><pre><span></span><code>PVRTC compressed RGB at 2 bits per pixel
</code></pre></div>
- `TEXTURE_FORMAT_RGB_PVRTC_4BPPV1` - <div class="codehilite"><pre><span></span><code>PVRTC compressed RGB at 4 bits per pixel
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_PVRTC_2BPPV1` - PVRTC compressed RGBA at 2 bits per pixel
- `TEXTURE_FORMAT_RGBA_PVRTC_4BPPV1` - PVRTC compressed RGBA at 4 bits per pixel
- `TEXTURE_FORMAT_RGB_ETC1` - <div class="codehilite"><pre><span></span><code>        ETC1 compressed RGB (no alpha support)
</code></pre></div>
- `TEXTURE_FORMAT_R_ETC2` - <div class="codehilite"><pre><span></span><code>          ETC2 single-channel
</code></pre></div>
- `TEXTURE_FORMAT_RG_ETC2` - <div class="codehilite"><pre><span></span><code>         ETC2 two-channel
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ETC2` - <div class="codehilite"><pre><span></span><code>       ETC2 four-channel (with alpha)
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_4X4` - <div class="codehilite"><pre><span></span><code>   ASTC block-compressed 4×4
</code></pre></div>
- `TEXTURE_FORMAT_RGB_BC1` - <div class="codehilite"><pre><span></span><code>         BC1/DXT1 compressed RGB
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_BC3` - <div class="codehilite"><pre><span></span><code>        BC3/DXT5 compressed RGBA
</code></pre></div>
- `TEXTURE_FORMAT_R_BC4` - <div class="codehilite"><pre><span></span><code>           BC4 single-channel
</code></pre></div>
- `TEXTURE_FORMAT_RG_BC5` - <div class="codehilite"><pre><span></span><code>          BC5 two-channel
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_BC7` - <div class="codehilite"><pre><span></span><code>        BC7 high-quality compressed RGBA
</code></pre></div>
- `TEXTURE_FORMAT_RGB16F` - <div class="codehilite"><pre><span></span><code>          Half-precision float RGB
</code></pre></div>
- `TEXTURE_FORMAT_RGB32F` - <div class="codehilite"><pre><span></span><code>          Full 32-bit float RGB
</code></pre></div>
- `TEXTURE_FORMAT_RGBA16F` - <div class="codehilite"><pre><span></span><code>         Half-precision float RGBA
</code></pre></div>
- `TEXTURE_FORMAT_RGBA32F` - <div class="codehilite"><pre><span></span><code>         Full 32-bit float RGBA
</code></pre></div>
- `TEXTURE_FORMAT_R16F` - <div class="codehilite"><pre><span></span><code>            Half-precision float single channel
</code></pre></div>
- `TEXTURE_FORMAT_RG16F` - <div class="codehilite"><pre><span></span><code>           Half-precision float two channels
</code></pre></div>
- `TEXTURE_FORMAT_R32F` - <div class="codehilite"><pre><span></span><code>            Full 32-bit float single channel
</code></pre></div>
- `TEXTURE_FORMAT_RG32F` - <div class="codehilite"><pre><span></span><code>           Full 32-bit float two channels
</code></pre></div>
- `TEXTURE_FORMAT_RGBA32UI` - <div class="codehilite"><pre><span></span><code>        Internal: 32-bit unsigned integer RGBA (not script-exposed)
</code></pre></div>
- `TEXTURE_FORMAT_BGRA8U` - <div class="codehilite"><pre><span></span><code>          Internal: 32-bit BGRA layout
</code></pre></div>
- `TEXTURE_FORMAT_R32UI` - <div class="codehilite"><pre><span></span><code>           Internal: 32-bit unsigned integer single channel
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_5X4` - <div class="codehilite"><pre><span></span><code>   ASTC 5x4 block compression
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_5X5` - <div class="codehilite"><pre><span></span><code>   ASTC 5x5 block compression
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_6X5` - <div class="codehilite"><pre><span></span><code>   ASTC 6x5 block compression
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_6X6` - <div class="codehilite"><pre><span></span><code>   ASTC 6x6 block compression
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_8X5` - <div class="codehilite"><pre><span></span><code>   ASTC 8x5 block compression
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_8X6` - <div class="codehilite"><pre><span></span><code>   ASTC 8x6 block compression
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_8X8` - <div class="codehilite"><pre><span></span><code>   ASTC 8x8 block compression
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_10X5` - <div class="codehilite"><pre><span></span><code>  ASTC 10x5 block compression
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_10X6` - <div class="codehilite"><pre><span></span><code>  ASTC 10x6 block compression
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_10X8` - <div class="codehilite"><pre><span></span><code>  ASTC 10x8 block compression
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_10X10` - <div class="codehilite"><pre><span></span><code> ASTC 10x10 block compression
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_12X10` - <div class="codehilite"><pre><span></span><code> ASTC 12x10 block compression
</code></pre></div>
- `TEXTURE_FORMAT_RGBA_ASTC_12X12` - <div class="codehilite"><pre><span></span><code> ASTC 12x12 block compression
</code></pre></div>

### TextureParams
*Type:* STRUCT
Texture update parameters.
Defines a block of pixel data to be uploaded to a texture,
along with filtering, wrapping, and sub-region update options.
Typically used when calling texture upload/update functions
after a texture object has been created with TextureCreationParams

**Members**

- `m_Data` (const void*) - Pointer to raw pixel data in CPU memory. The format is defined by <code>m_Format</code>
- `m_DataSize` (uint32_t) - Size of the pixel data in bytes. Must match the expected size from width, height, depth, and format
- `m_Format` (dmGraphics::TextureFormat) - Format of the pixel data (e.g. RGBA, RGB, compressed formats). Dictates how the GPU interprets the memory pointed by <code>m_Data</code>
- `m_MinFilter` (dmGraphics::TextureFilter) - Minification filter (applied when shrinking). Determines how pixels are sampled when the texture is displayed smaller than its native resolution
- `m_MagFilter` (dmGraphics::TextureFilter) - Magnification filter (applied when enlarging). Determines how pixels are sampled when the texture is displayed larger than its native resolution
- `m_UWrap` (dmGraphics::TextureWrap) - Wrapping mode for U (X) texture coordinate. Controls behavior when texture coordinates exceed [0,1]
- `m_VWrap` (dmGraphics::TextureWrap) - Wrapping mode for V (Y) texture coordinate. Controls behavior when texture coordinates exceed [0,1]
- `m_WWrap` (dmGraphics::TextureWrap) - Wrapping mode for W (Z) texture coordinate. Controls behavior when texture coordinates exceed [0,1]
- `m_X` (uint32_t) - X offset in pixels for sub-texture updates. Defines the left edge of the destination region
- `m_Y` (uint32_t) - Y offset in pixels for sub-texture updates. Defines the top edge of the destination region
- `m_Z` (uint32_t) - Z offset (depth layer) for 3D textures. Ignored for standard 2D textures
- `m_Slice` (uint32_t) - Slice index in an array texture where the data should be uploaded
- `m_Width` (uint16_t) - Width of the pixel data block in pixels. Used for both full uploads and sub-updates
- `m_Height` (uint16_t) - Height of the pixel data block in pixels. Used for both full uploads and sub-updates
- `m_Depth` (uint16_t) - Depth of the pixel data block in pixels. Only relevant for 3D textures
- `m_LayerCount` (uint8_t) - Number of layers to update. For array textures, this specifies how many pages are updated
- `m_MipMap` (uint8_t) - Only 7 bit available Mipmap level to update. Level 0 is the base level, higher levels are progressively downscaled versions
- `m_SubUpdate` (uint8_t) - If true, this represents a partial texture update (sub-region), using <code>m_X</code>, <code>m_Y</code>, <code>m_Z</code>, and <code>m_Slice</code> offsets. If false, the entire texture/mipmap level is replaced

### TextureStatusFlags
*Type:* ENUM
Texture data upload status flags

**Members**

- `TEXTURE_STATUS_OK` - <div class="codehilite"><pre><span></span><code>       Texture updated and ready-to-use
</code></pre></div>
- `TEXTURE_STATUS_DATA_PENDING` - Data upload to the texture is in progress

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

- `TEXTURE_WRAP_CLAMP_TO_BORDER` - <div class="codehilite"><pre><span></span><code>Clamp to the color defined as &#39;border&#39;
</code></pre></div>
- `TEXTURE_WRAP_CLAMP_TO_EDGE` - <div class="codehilite"><pre><span></span><code>  Clamp to the edge pixel of the texture
</code></pre></div>
- `TEXTURE_WRAP_MIRRORED_REPEAT` - <div class="codehilite"><pre><span></span><code>Repeat texture, mirroring every other repetition
</code></pre></div>
- `TEXTURE_WRAP_REPEAT` - <div class="codehilite"><pre><span></span><code>         Repeat texture in a tiled fashion
</code></pre></div>

### Type
*Type:* ENUM
Data type.
Represents scalar, vector, matrix, image, or sampler types used
for vertex attributes, uniforms, and shader interface definitions

**Members**

- `TYPE_BYTE` - <div class="codehilite"><pre><span></span><code>           <span class="nv">Signed</span> <span class="mi">8</span><span class="o">-</span><span class="nv">bit</span> <span class="nv">integer</span>. <span class="nv">Compact</span> <span class="nv">storage</span>, <span class="nv">often</span> <span class="nv">used</span> <span class="k">for</span> <span class="nv">colors</span>, <span class="nv">normals</span>, <span class="nv">or</span> <span class="nv">compressed</span> <span class="nv">vertex</span> <span class="nv">attributes</span>
</code></pre></div>
- `TYPE_UNSIGNED_BYTE` - <div class="codehilite"><pre><span></span><code>  <span class="nv">Unsigned</span> <span class="mi">8</span><span class="o">-</span><span class="nv">bit</span> <span class="nv">integer</span>. <span class="nv">Common</span> <span class="k">for</span> <span class="nv">color</span> <span class="nv">channels</span> <span class="ss">(</span><span class="mi">0</span>–<span class="mi">255</span><span class="ss">)</span> <span class="nv">or</span> <span class="nv">normalized</span> <span class="nv">texture</span> <span class="nv">data</span>
</code></pre></div>
- `TYPE_SHORT` - <div class="codehilite"><pre><span></span><code>          <span class="nv">Signed</span> <span class="mi">16</span><span class="o">-</span><span class="nv">bit</span> <span class="nv">integer</span>. <span class="nv">Used</span> <span class="k">for</span> <span class="nv">medium</span><span class="o">-</span><span class="nv">range</span> <span class="nv">numeric</span> <span class="nv">attributes</span> <span class="nv">such</span> <span class="nv">as</span> <span class="nv">bone</span> <span class="nv">weights</span> <span class="nv">or</span> <span class="nv">coordinates</span> <span class="nv">with</span> <span class="nv">normalization</span>
</code></pre></div>
- `TYPE_UNSIGNED_SHORT` - <div class="codehilite"><pre><span></span><code> <span class="nv">Unsigned</span> <span class="mi">16</span><span class="o">-</span><span class="nv">bit</span> <span class="nv">integer</span>. <span class="nv">Often</span> <span class="nv">used</span> <span class="k">for</span> <span class="nv">indices</span> <span class="nv">or</span> <span class="nv">normalized</span> <span class="nv">attributes</span> <span class="nv">when</span> <span class="nv">extra</span> <span class="nv">precision</span> <span class="nv">over</span> <span class="nv">bytes</span> <span class="nv">is</span> <span class="nv">required</span>
</code></pre></div>
- `TYPE_INT` - <div class="codehilite"><pre><span></span><code><span class="w">            </span><span class="n">Signed</span><span class="w"> </span><span class="mi">32</span><span class="o">-</span><span class="n">bit</span><span class="w"> </span><span class="n">integer</span><span class="o">.</span><span class="w"> </span><span class="n">Typically</span><span class="w"> </span><span class="n">used</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">uniform</span><span class="w"> </span><span class="n">values</span><span class="p">,</span><span class="w"> </span><span class="n">shader</span><span class="w"> </span><span class="n">constants</span><span class="p">,</span><span class="w"> </span><span class="ow">or</span><span class="w"> </span><span class="n">counters</span><span class="w"></span>
</code></pre></div>
- `TYPE_UNSIGNED_INT` - <div class="codehilite"><pre><span></span><code>   <span class="nv">Unsigned</span> <span class="mi">32</span><span class="o">-</span><span class="nv">bit</span> <span class="nv">integer</span>. <span class="nv">Used</span> <span class="k">for</span> <span class="nv">indices</span>, <span class="nv">IDs</span>, <span class="nv">or</span> <span class="nv">GPU</span> <span class="nv">counters</span>
</code></pre></div>
- `TYPE_FLOAT` - <div class="codehilite"><pre><span></span><code>          <span class="mi">32</span><span class="o">-</span><span class="nv">bit</span> <span class="nv">floating</span> <span class="nv">point</span>. <span class="nv">Standard</span> <span class="k">for</span> <span class="nv">most</span> <span class="nv">vertex</span> <span class="nv">attributes</span> <span class="nv">and</span> <span class="nv">uniform</span> <span class="nv">values</span> <span class="ss">(</span><span class="nv">positions</span>, <span class="nv">UVs</span>, <span class="nv">weights</span><span class="ss">)</span>
</code></pre></div>
- `TYPE_FLOAT_VEC4` - <div class="codehilite"><pre><span></span><code><span class="w">     </span><span class="mi">4</span><span class="o">-</span><span class="k">component</span><span class="w"> </span><span class="n">floating</span><span class="o">-</span><span class="kt">point</span><span class="w"> </span><span class="n">vector</span><span class="w"> </span><span class="p">(</span><span class="n n-Quoted">`vec4`</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">GLSL</span><span class="p">).</span><span class="w"> </span><span class="n">Typically</span><span class="w"> </span><span class="n">used</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">homogeneous</span><span class="w"> </span><span class="n">coordinates</span><span class="p">,</span><span class="w"> </span><span class="n">colors</span><span class="w"> </span><span class="p">(</span><span class="n">RGBA</span><span class="p">),</span><span class="w"> </span><span class="k">or</span><span class="w"> </span><span class="n">combined</span><span class="w"> </span><span class="n">attributes</span><span class="w"></span>
</code></pre></div>
- `TYPE_FLOAT_MAT4` - <div class="codehilite"><pre><span></span><code><span class="w">     </span><span class="n">4x4</span><span class="w"> </span><span class="n">floating</span><span class="o">-</span><span class="kt">point</span><span class="w"> </span><span class="n">matrix</span><span class="w"> </span><span class="p">(</span><span class="n n-Quoted">`mat4`</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">GLSL</span><span class="p">).</span><span class="w"> </span><span class="n">Standard</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">3D</span><span class="w"> </span><span class="n">transformations</span><span class="w"> </span><span class="p">(</span><span class="n">model</span><span class="p">,</span><span class="w"> </span><span class="k">view</span><span class="p">,</span><span class="w"> </span><span class="n">projection</span><span class="p">)</span><span class="w"></span>
</code></pre></div>
- `TYPE_SAMPLER_2D` - <div class="codehilite"><pre><span></span><code>     <span class="mi">2</span><span class="nv">D</span> <span class="nv">texture</span> <span class="nv">sampler</span>. <span class="nv">Standard</span> <span class="nv">type</span> <span class="k">for</span> <span class="nv">most</span> <span class="nv">texture</span> <span class="nv">lookups</span>
</code></pre></div>
- `TYPE_SAMPLER_CUBE` - <div class="codehilite"><pre><span></span><code>   <span class="nv">Cube</span> <span class="nv">map</span> <span class="nv">sampler</span>. <span class="nv">Used</span> <span class="k">for</span> <span class="nv">environment</span> <span class="nv">mapping</span>, <span class="nv">reflections</span>, <span class="nv">and</span> <span class="nv">skyboxes</span>
</code></pre></div>
- `TYPE_SAMPLER_2D_ARRAY` - Array of 2D texture samplers. Enables efficient texture indexing when using multiple layers (e.g. terrain textures, sprite atlases)
- `TYPE_FLOAT_VEC2` - <div class="codehilite"><pre><span></span><code><span class="w">     </span><span class="mi">2</span><span class="o">-</span><span class="k">component</span><span class="w"> </span><span class="n">floating</span><span class="o">-</span><span class="kt">point</span><span class="w"> </span><span class="n">vector</span><span class="w"> </span><span class="p">(</span><span class="n n-Quoted">`vec2`</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">GLSL</span><span class="p">).</span><span class="w"> </span><span class="n">Commonly</span><span class="w"> </span><span class="n">used</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">texture</span><span class="w"> </span><span class="n">coordinates</span><span class="w"> </span><span class="k">or</span><span class="w"> </span><span class="n">2D</span><span class="w"> </span><span class="n">positions</span><span class="w"></span>
</code></pre></div>
- `TYPE_FLOAT_VEC3` - <div class="codehilite"><pre><span></span><code><span class="w">     </span><span class="mi">3</span><span class="o">-</span><span class="k">component</span><span class="w"> </span><span class="n">floating</span><span class="o">-</span><span class="kt">point</span><span class="w"> </span><span class="n">vector</span><span class="w"> </span><span class="p">(</span><span class="n n-Quoted">`vec3`</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">GLSL</span><span class="p">).</span><span class="w"> </span><span class="n">Used</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">positions</span><span class="p">,</span><span class="w"> </span><span class="n">normals</span><span class="p">,</span><span class="w"> </span><span class="k">and</span><span class="w"> </span><span class="n">directions</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">3D</span><span class="w"> </span><span class="n">space</span><span class="w"></span>
</code></pre></div>
- `TYPE_FLOAT_MAT2` - <div class="codehilite"><pre><span></span><code><span class="w">     </span><span class="n">2x2</span><span class="w"> </span><span class="n">floating</span><span class="o">-</span><span class="kt">point</span><span class="w"> </span><span class="n">matrix</span><span class="w"> </span><span class="p">(</span><span class="n n-Quoted">`mat2`</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">GLSL</span><span class="p">).</span><span class="w"> </span><span class="n">Used</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">transformations</span><span class="w"> </span><span class="p">(</span><span class="n">e</span><span class="p">.</span><span class="n">g</span><span class="p">.</span><span class="w"> </span><span class="n">2D</span><span class="w"> </span><span class="n">rotations</span><span class="p">,</span><span class="w"> </span><span class="n">scaling</span><span class="p">)</span><span class="w"></span>
</code></pre></div>
- `TYPE_FLOAT_MAT3` - <div class="codehilite"><pre><span></span><code><span class="w">     </span><span class="n">3x3</span><span class="w"> </span><span class="n">floating</span><span class="o">-</span><span class="kt">point</span><span class="w"> </span><span class="n">matrix</span><span class="w"> </span><span class="p">(</span><span class="n n-Quoted">`mat3`</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">GLSL</span><span class="p">).</span><span class="w"> </span><span class="n">Commonly</span><span class="w"> </span><span class="n">used</span><span class="w"> </span><span class="k">for</span><span class="w"> </span><span class="n">normal</span><span class="w"> </span><span class="n">matrix</span><span class="w"> </span><span class="n">calculations</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">lighting</span><span class="w"></span>
</code></pre></div>
- `TYPE_IMAGE_2D` - <div class="codehilite"><pre><span></span><code><span class="w">       </span><span class="mi">2</span><span class="n">D</span><span class="w"> </span><span class="n">image</span><span class="w"> </span><span class="n">object</span><span class="o">.</span><span class="w"> </span><span class="n">Unlike</span><span class="w"> </span><span class="n">samplers</span><span class="p">,</span><span class="w"> </span><span class="n">images</span><span class="w"> </span><span class="n">allow</span><span class="w"> </span><span class="n">read</span><span class="o">/</span><span class="n">write</span><span class="w"> </span><span class="n">access</span><span class="w"> </span><span class="ow">in</span><span class="w"> </span><span class="n">shaders</span><span class="w"> </span><span class="p">(</span><span class="n">e</span><span class="o">.</span><span class="n">g</span><span class="o">.</span><span class="w"> </span><span class="n">compute</span><span class="w"> </span><span class="n">shaders</span><span class="w"> </span><span class="ow">or</span><span class="w"> </span><span class="n">image</span><span class="w"> </span><span class="nb">load</span><span class="o">/</span><span class="n">store</span><span class="w"> </span><span class="n">operations</span><span class="p">)</span><span class="w"></span>
</code></pre></div>
- `TYPE_TEXTURE_2D` - <div class="codehilite"><pre><span></span><code>     2D texture object handle. Represents an actual GPU texture resource
</code></pre></div>
- `TYPE_SAMPLER` - <div class="codehilite"><pre><span></span><code>        <span class="nv">Generic</span> <span class="nv">sampler</span> <span class="nv">handle</span>, <span class="nv">used</span> <span class="nv">as</span> <span class="nv">a</span> <span class="nv">placeholder</span> <span class="k">for</span> <span class="nv">texture</span> <span class="nv">units</span> <span class="nv">without</span> <span class="nv">specifying</span> <span class="nv">the</span> <span class="nv">dimension</span>
</code></pre></div>
- `TYPE_TEXTURE_2D_ARRAY` - 2D texture array object handle
- `TYPE_TEXTURE_CUBE` - <div class="codehilite"><pre><span></span><code>   Cube map texture object handle
</code></pre></div>
- `TYPE_SAMPLER_3D` - <div class="codehilite"><pre><span></span><code>     <span class="mi">3</span><span class="nv">D</span> <span class="nv">texture</span> <span class="nv">sampler</span>. <span class="nv">Used</span> <span class="k">for</span> <span class="nv">volumetric</span> <span class="nv">effects</span>, <span class="nv">noise</span> <span class="nv">fields</span>, <span class="nv">or</span> <span class="nv">voxel</span> <span class="nv">data</span>
</code></pre></div>
- `TYPE_TEXTURE_3D` - <div class="codehilite"><pre><span></span><code>     3D texture object handle
</code></pre></div>
- `TYPE_IMAGE_3D` - <div class="codehilite"><pre><span></span><code>       <span class="mi">3</span><span class="nv">D</span> <span class="nv">image</span> <span class="nv">object</span>. <span class="nv">Used</span> <span class="k">for</span> <span class="nv">compute</span><span class="o">-</span><span class="nv">based</span> <span class="nv">volume</span> <span class="nv">processing</span>
</code></pre></div>
- `TYPE_SAMPLER_3D_ARRAY` - Array of 3D texture samplers
- `TYPE_TEXTURE_3D_ARRAY` - 3D texture array object handle
