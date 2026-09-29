# Graphics

**Namespace:** `graphics`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_graphics.cpp`
**Source:** `engine/script/src/script_graphics.cpp`

Graphics functions and constants.

## API

### graphics.adapter_info
*Type:* STRUCT
Graphics adapter information

**Members**

- `family` (string) - Adapter family name.
- `version_major` (integer) - Adapter API major version.
- `version_minor` (integer) - Adapter API minor version.
- `limits` (graphics.adapter_limits) - Hardware and driver limits.
- `extensions` (string[]) - Driver-reported extension names.
- `features` (graphics.CONTEXT_FEATURE[]) - Supported optional context features.

### graphics.adapter_limits
*Type:* STRUCT
Graphics context limits

**Members**

- `max_texture_size_2d` (integer) - Maximum 2D texture dimension in texels.
- `max_texture_size_3d` (integer) - Maximum 3D texture dimension in texels.
- `max_texture_size_cube` (integer) - Maximum cube-map face dimension in texels.
- `max_texture_array_layers` (integer) - Maximum number of array texture layers.
- `max_framebuffer_width` (integer) - Maximum framebuffer width in pixels.
- `max_framebuffer_height` (integer) - Maximum framebuffer height in pixels.
- `max_color_attachments` (integer) - Maximum number of simultaneous color attachments.
- `max_samplers_per_stage` (integer) - Maximum number of texture samplers per shader stage.
- `max_textures_per_stage` (integer) - Maximum number of sampled textures per shader stage.
- `max_vertex_attributes` (integer) - Maximum number of vertex attributes.
- `max_vertex_buffers` (integer) - Maximum number of vertex-buffer bindings.
- `max_compute_workgroup_size_x` (integer) - Maximum compute workgroup size on the X axis.
- `max_compute_workgroup_size_y` (integer) - Maximum compute workgroup size on the Y axis.
- `max_compute_workgroup_size_z` (integer) - Maximum compute workgroup size on the Z axis.
- `max_compute_workgroup_invocations` (integer) - Maximum invocations per compute workgroup.
- `max_compute_shared_memory_size` (integer) - Maximum shared memory per compute workgroup in bytes.
- `max_uniform_buffer_range` (integer) - Maximum bindable uniform-buffer range in bytes.
- `max_storage_buffer_range` (integer) - Maximum bindable storage-buffer range in bytes.

### graphics.BLEND_EQUATION
*Type:* ENUM
Blend equations

**Members**

- `graphics.BLEND_EQUATION_ADD`
- `graphics.BLEND_EQUATION_MAX`
- `graphics.BLEND_EQUATION_MIN`
- `graphics.BLEND_EQUATION_REVERSE_SUBTRACT`
- `graphics.BLEND_EQUATION_SUBTRACT`

### graphics.BLEND_FACTOR
*Type:* ENUM
Blend factors

**Members**

- `graphics.BLEND_FACTOR_CONSTANT_ALPHA` - constant blend alpha for every component
- `graphics.BLEND_FACTOR_CONSTANT_COLOR` - constant blend color
- `graphics.BLEND_FACTOR_DST_ALPHA` - destination alpha for every component
- `graphics.BLEND_FACTOR_DST_COLOR` - destination color
- `graphics.BLEND_FACTOR_ONE` - one for every component
- `graphics.BLEND_FACTOR_ONE_MINUS_CONSTANT_ALPHA` - one minus the constant blend alpha for every component
- `graphics.BLEND_FACTOR_ONE_MINUS_CONSTANT_COLOR` - one minus the constant blend color
- `graphics.BLEND_FACTOR_ONE_MINUS_DST_ALPHA` - one minus the destination alpha for every component
- `graphics.BLEND_FACTOR_ONE_MINUS_DST_COLOR` - one minus the destination color
- `graphics.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA` - one minus the source alpha for every component
- `graphics.BLEND_FACTOR_ONE_MINUS_SRC_COLOR` - one minus the source color
- `graphics.BLEND_FACTOR_SRC_ALPHA` - source alpha for every component
- `graphics.BLEND_FACTOR_SRC_ALPHA_SATURATE` - minimum of source alpha and one minus destination alpha for color, and one for alpha
- `graphics.BLEND_FACTOR_SRC_COLOR` - source color
- `graphics.BLEND_FACTOR_ZERO` - zero for every component

### graphics.BUFFER_TYPE
*Type:* ENUM
Buffer types

**Members**

- `graphics.BUFFER_TYPE_COLOR0_BIT` - first color attachment
- `graphics.BUFFER_TYPE_COLOR1_BIT` - second color attachment; may be nil if multiple render targets are unsupported
- `graphics.BUFFER_TYPE_COLOR2_BIT` - third color attachment; may be nil if multiple render targets are unsupported
- `graphics.BUFFER_TYPE_COLOR3_BIT` - fourth color attachment; may be nil if multiple render targets are unsupported
- `graphics.BUFFER_TYPE_DEPTH_BIT` - depth attachment
- `graphics.BUFFER_TYPE_STENCIL_BIT` - stencil attachment

### graphics.COMPARE_FUNC
*Type:* ENUM
Comparison functions

**Members**

- `graphics.COMPARE_FUNC_ALWAYS` - always passes
- `graphics.COMPARE_FUNC_EQUAL` - passes when the values are equal
- `graphics.COMPARE_FUNC_GEQUAL` - passes when the incoming value is greater than or equal to the stored value
- `graphics.COMPARE_FUNC_GREATER` - passes when the incoming value is greater than the stored value
- `graphics.COMPARE_FUNC_LEQUAL` - passes when the incoming value is less than or equal to the stored value
- `graphics.COMPARE_FUNC_LESS` - passes when the incoming value is less than the stored value
- `graphics.COMPARE_FUNC_NEVER` - never passes
- `graphics.COMPARE_FUNC_NOTEQUAL` - passes when the values are not equal

### graphics.COMPRESSION_TYPE
*Type:* ENUM
Texture compression types

**Members**

- `graphics.COMPRESSION_TYPE_BASIS_ETC1S`
- `graphics.COMPRESSION_TYPE_BASIS_UASTC`
- `graphics.COMPRESSION_TYPE_DEFAULT`
- `graphics.COMPRESSION_TYPE_WEBP`
- `graphics.COMPRESSION_TYPE_WEBP_LOSSY`

### graphics.CONTEXT_FEATURE
*Type:* ENUM
Optional graphics-context features

**Members**

- `graphics.CONTEXT_FEATURE_3D_TEXTURES` - Context feature flag indicating support for 3D (volume) textures.
- `graphics.CONTEXT_FEATURE_ASTC_ARRAY_TEXTURES` - Context feature flag indicating support for ASTC compressed 2D array textures. Some WebGL/GLES drivers fail array texture ASTC uploads while 2D ASTC works.
- `graphics.CONTEXT_FEATURE_BC_ARRAY_TEXTURES` - Context feature flag indicating support for BC (S3TC/RGTC/BPTC) compressed 2D array and 3D textures. WebGL2 forbids these compressed families on array/3D targets while allowing them on 2D.
- `graphics.CONTEXT_FEATURE_BLEND_EQUATION_MIN_MAX` - Context feature flag indicating support for min/max blend equations. Requires GLES3+ or EXT_blend_minmax.
- `graphics.CONTEXT_FEATURE_COMPUTE_SHADER` - Context feature flag indicating support for compute shaders.
- `graphics.CONTEXT_FEATURE_INSTANCING` - Context feature flag indicating support for hardware instancing.
- `graphics.CONTEXT_FEATURE_MULTI_TARGET_RENDERING` - Context feature flag indicating support for rendering to multiple color targets simultaneously.
- `graphics.CONTEXT_FEATURE_STORAGE_BUFFER` - Context feature flag indicating support for storage buffers.
- `graphics.CONTEXT_FEATURE_TEXTURE_ARRAY` - Context feature flag indicating support for texture arrays.
- `graphics.CONTEXT_FEATURE_VSYNC` - Context feature flag indicating support for vertical sync (vsync).

### graphics.COORDINATE_SPACE
*Type:* ENUM
Vertex attribute coordinate spaces

**Members**

- `graphics.COORDINATE_SPACE_DEFAULT` - Default vertex attribute coordinate space.
- `graphics.COORDINATE_SPACE_LOCAL` - Local vertex attribute coordinate space.
- `graphics.COORDINATE_SPACE_WORLD` - World vertex attribute coordinate space.

### graphics.DATA_TYPE
*Type:* ENUM
Vertex attribute data types

**Members**

- `graphics.DATA_TYPE_BYTE` - Signed 8-bit vertex attribute data.
- `graphics.DATA_TYPE_FLOAT` - 32-bit floating-point vertex attribute data.
- `graphics.DATA_TYPE_INT` - Signed 32-bit vertex attribute data.
- `graphics.DATA_TYPE_SHORT` - Signed 16-bit vertex attribute data.
- `graphics.DATA_TYPE_UNSIGNED_BYTE` - Unsigned 8-bit vertex attribute data.
- `graphics.DATA_TYPE_UNSIGNED_INT` - Unsigned 32-bit vertex attribute data.
- `graphics.DATA_TYPE_UNSIGNED_SHORT` - Unsigned 16-bit vertex attribute data.

### graphics.FACE_TYPE
*Type:* ENUM
Face types

**Members**

- `graphics.FACE_TYPE_BACK` - back-facing polygons
- `graphics.FACE_TYPE_FRONT` - front-facing polygons
- `graphics.FACE_TYPE_FRONT_AND_BACK` - both front- and back-facing polygons

### graphics.get_adapter_info
*Type:* FUNCTION
Returns a table describing the active graphics context: the adapter family,
its hardware limits, the list of driver-reported extensions, and the set of
optional context features supported by the backend.

**Returns**

- `info` (graphics.adapter_info) - information about the active graphics adapter and context

### graphics.get_engine_adapters
*Type:* FUNCTION
get the list of graphics adapters that have been registered with the engine

**Returns**

- `adapters` (string[]) - array of adapter family name strings (e.g. "opengl", "vulkan", "webgpu")

### graphics.SEMANTIC_TYPE
*Type:* ENUM
Vertex attribute semantic types

**Members**

- `graphics.SEMANTIC_TYPE_BONE_INDICES` - Bone-index vertex attribute.
- `graphics.SEMANTIC_TYPE_BONE_WEIGHTS` - Bone-weight vertex attribute.
- `graphics.SEMANTIC_TYPE_COLOR` - Color vertex attribute.
- `graphics.SEMANTIC_TYPE_MORPH_TARGET_WEIGHTS` - Morph-target-weight vertex attribute.
- `graphics.SEMANTIC_TYPE_NONE` - Vertex attribute without a predefined semantic.
- `graphics.SEMANTIC_TYPE_NORMAL` - Normal vertex attribute.
- `graphics.SEMANTIC_TYPE_NORMAL_MATRIX` - Normal-matrix vertex attribute.
- `graphics.SEMANTIC_TYPE_PAGE_INDEX` - Texture page-index vertex attribute.
- `graphics.SEMANTIC_TYPE_POSITION` - Position vertex attribute.
- `graphics.SEMANTIC_TYPE_TANGENT` - Tangent vertex attribute.
- `graphics.SEMANTIC_TYPE_TEXCOORD` - Texture-coordinate vertex attribute.
- `graphics.SEMANTIC_TYPE_TEXTURE_TRANSFORM_2D` - 2D texture-transform vertex attribute.
- `graphics.SEMANTIC_TYPE_WORLD_MATRIX` - World-matrix vertex attribute.

### graphics.STATE
*Type:* ENUM
Graphics states

**Members**

- `graphics.STATE_ALPHA_TEST`
- `graphics.STATE_ALPHA_TEST_SUPPORTED`
- `graphics.STATE_BLEND`
- `graphics.STATE_CULL_FACE`
- `graphics.STATE_DEPTH_TEST`
- `graphics.STATE_POLYGON_OFFSET_FILL`
- `graphics.STATE_SCISSOR_TEST`
- `graphics.STATE_STENCIL_TEST`

### graphics.STENCIL_OP
*Type:* ENUM
Stencil operations

**Members**

- `graphics.STENCIL_OP_DECR` - decrement and clamp at zero
- `graphics.STENCIL_OP_DECR_WRAP` - decrement and wrap zero to the maximum unsigned value
- `graphics.STENCIL_OP_INCR` - increment and clamp at the maximum unsigned value
- `graphics.STENCIL_OP_INCR_WRAP` - increment and wrap the maximum unsigned value to zero
- `graphics.STENCIL_OP_INVERT` - bitwise invert
- `graphics.STENCIL_OP_KEEP` - keep the current value
- `graphics.STENCIL_OP_REPLACE` - replace with the reference value from <a href="/ref/render#render.set_stencil_func">render.set_stencil_func</a>
- `graphics.STENCIL_OP_ZERO` - set to zero

### graphics.TEXTURE_FILTER
*Type:* ENUM
Texture filters

**Members**

- `graphics.TEXTURE_FILTER_DEFAULT`
- `graphics.TEXTURE_FILTER_LINEAR`
- `graphics.TEXTURE_FILTER_LINEAR_MIPMAP_LINEAR`
- `graphics.TEXTURE_FILTER_LINEAR_MIPMAP_NEAREST`
- `graphics.TEXTURE_FILTER_NEAREST`
- `graphics.TEXTURE_FILTER_NEAREST_MIPMAP_LINEAR`
- `graphics.TEXTURE_FILTER_NEAREST_MIPMAP_NEAREST`

### graphics.TEXTURE_FORMAT
*Type:* ENUM
Texture formats

**Members**

- `graphics.TEXTURE_FORMAT_BGRA8U` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_DEPTH`
- `graphics.TEXTURE_FORMAT_LUMINANCE` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_LUMINANCE_ALPHA` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_R16F` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_R32F` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_R32UI` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RG16F` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RG32F` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGB` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGB16F` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGB32F` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGBA` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGBA16F` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGBA32F` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGBA32UI` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGBA_16BPP` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGBA_ASTC_4X4` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGBA_BC3` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGBA_BC7` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGBA_ETC2` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGBA_PVRTC_2BPPV1` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGBA_PVRTC_4BPPV1` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGB_16BPP` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGB_BC1` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGB_ETC1` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGB_PVRTC_2BPPV1` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RGB_PVRTC_4BPPV1` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RG_BC5` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_RG_ETC2` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_R_BC4` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_R_ETC2` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_FORMAT_STENCIL`

### graphics.TEXTURE_TYPE
*Type:* ENUM
Texture types

**Members**

- `graphics.TEXTURE_TYPE_2D`
- `graphics.TEXTURE_TYPE_2D_ARRAY`
- `graphics.TEXTURE_TYPE_3D` - May be nil if the graphics driver doesn't support it
- `graphics.TEXTURE_TYPE_CUBE_MAP`
- `graphics.TEXTURE_TYPE_IMAGE_2D`
- `graphics.TEXTURE_TYPE_IMAGE_3D` - May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_USAGE_FLAG
*Type:* ENUM
Texture usage flags

**Members**

- `graphics.TEXTURE_USAGE_FLAG_COLOR`
- `graphics.TEXTURE_USAGE_FLAG_INPUT`
- `graphics.TEXTURE_USAGE_FLAG_MEMORYLESS`
- `graphics.TEXTURE_USAGE_FLAG_SAMPLE`
- `graphics.TEXTURE_USAGE_FLAG_STORAGE`

### graphics.TEXTURE_WRAP
*Type:* ENUM
Texture wrapping modes

**Members**

- `graphics.TEXTURE_WRAP_CLAMP_TO_BORDER`
- `graphics.TEXTURE_WRAP_CLAMP_TO_EDGE`
- `graphics.TEXTURE_WRAP_MIRRORED_REPEAT`
- `graphics.TEXTURE_WRAP_REPEAT`
