# Graphics

**Namespace:** `graphics`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_graphics.cpp`
**Source:** `engine/script/src/script_graphics.cpp`

Graphics functions and constants.

## API

### graphics.BLEND_FACTOR_CONSTANT_ALPHA
*Type:* CONSTANT

### graphics.BLEND_FACTOR_CONSTANT_COLOR
*Type:* CONSTANT

### graphics.BLEND_FACTOR_DST_ALPHA
*Type:* CONSTANT

### graphics.BLEND_FACTOR_DST_COLOR
*Type:* CONSTANT

### graphics.BLEND_FACTOR_ONE
*Type:* CONSTANT

### graphics.BLEND_FACTOR_ONE_MINUS_CONSTANT_ALPHA
*Type:* CONSTANT

### graphics.BLEND_FACTOR_ONE_MINUS_CONSTANT_COLOR
*Type:* CONSTANT

### graphics.BLEND_FACTOR_ONE_MINUS_DST_ALPHA
*Type:* CONSTANT

### graphics.BLEND_FACTOR_ONE_MINUS_DST_COLOR
*Type:* CONSTANT

### graphics.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
*Type:* CONSTANT

### graphics.BLEND_FACTOR_ONE_MINUS_SRC_COLOR
*Type:* CONSTANT

### graphics.BLEND_FACTOR_SRC_ALPHA
*Type:* CONSTANT

### graphics.BLEND_FACTOR_SRC_ALPHA_SATURATE
*Type:* CONSTANT

### graphics.BLEND_FACTOR_SRC_COLOR
*Type:* CONSTANT

### graphics.BLEND_FACTOR_ZERO
*Type:* CONSTANT

### graphics.BUFFER_TYPE_COLOR0_BIT
*Type:* CONSTANT

### graphics.BUFFER_TYPE_COLOR1_BIT
*Type:* CONSTANT
May be nil if multitarget rendering isn't supported

### graphics.BUFFER_TYPE_COLOR2_BIT
*Type:* CONSTANT
May be nil if multitarget rendering isn't supported

### graphics.BUFFER_TYPE_COLOR3_BIT
*Type:* CONSTANT
May be nil if multitarget rendering isn't supported

### graphics.BUFFER_TYPE_DEPTH_BIT
*Type:* CONSTANT

### graphics.BUFFER_TYPE_STENCIL_BIT
*Type:* CONSTANT

### graphics.COMPARE_FUNC_ALWAYS
*Type:* CONSTANT

### graphics.COMPARE_FUNC_EQUAL
*Type:* CONSTANT

### graphics.COMPARE_FUNC_GEQUAL
*Type:* CONSTANT

### graphics.COMPARE_FUNC_GREATER
*Type:* CONSTANT

### graphics.COMPARE_FUNC_LEQUAL
*Type:* CONSTANT

### graphics.COMPARE_FUNC_LESS
*Type:* CONSTANT

### graphics.COMPARE_FUNC_NEVER
*Type:* CONSTANT

### graphics.COMPARE_FUNC_NOTEQUAL
*Type:* CONSTANT

### graphics.COMPRESSION_TYPE_BASIS_ETC1S
*Type:* CONSTANT

### graphics.COMPRESSION_TYPE_BASIS_UASTC
*Type:* CONSTANT

### graphics.COMPRESSION_TYPE_DEFAULT
*Type:* CONSTANT

### graphics.COMPRESSION_TYPE_WEBP
*Type:* CONSTANT

### graphics.COMPRESSION_TYPE_WEBP_LOSSY
*Type:* CONSTANT

### graphics.FACE_TYPE_BACK
*Type:* CONSTANT

### graphics.FACE_TYPE_FRONT
*Type:* CONSTANT

### graphics.FACE_TYPE_FRONT_AND_BACK
*Type:* CONSTANT

### graphics.STATE_ALPHA_TEST
*Type:* CONSTANT

### graphics.STATE_ALPHA_TEST_SUPPORTED
*Type:* CONSTANT

### graphics.STATE_BLEND
*Type:* CONSTANT

### graphics.STATE_CULL_FACE
*Type:* CONSTANT

### graphics.STATE_DEPTH_TEST
*Type:* CONSTANT

### graphics.STATE_POLYGON_OFFSET_FILL
*Type:* CONSTANT

### graphics.STATE_SCISSOR_TEST
*Type:* CONSTANT

### graphics.STATE_STENCIL_TEST
*Type:* CONSTANT

### graphics.STENCIL_OP_DECR
*Type:* CONSTANT

### graphics.STENCIL_OP_DECR_WRAP
*Type:* CONSTANT

### graphics.STENCIL_OP_INCR
*Type:* CONSTANT

### graphics.STENCIL_OP_INCR_WRAP
*Type:* CONSTANT

### graphics.STENCIL_OP_INVERT
*Type:* CONSTANT

### graphics.STENCIL_OP_KEEP
*Type:* CONSTANT

### graphics.STENCIL_OP_REPLACE
*Type:* CONSTANT

### graphics.STENCIL_OP_ZERO
*Type:* CONSTANT

### graphics.TEXTURE_FILTER_DEFAULT
*Type:* CONSTANT

### graphics.TEXTURE_FILTER_LINEAR
*Type:* CONSTANT

### graphics.TEXTURE_FILTER_LINEAR_MIPMAP_LINEAR
*Type:* CONSTANT

### graphics.TEXTURE_FILTER_LINEAR_MIPMAP_NEAREST
*Type:* CONSTANT

### graphics.TEXTURE_FILTER_NEAREST
*Type:* CONSTANT

### graphics.TEXTURE_FILTER_NEAREST_MIPMAP_LINEAR
*Type:* CONSTANT

### graphics.TEXTURE_FILTER_NEAREST_MIPMAP_NEAREST
*Type:* CONSTANT

### graphics.TEXTURE_FORMAT_BGRA8U
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_DEPTH
*Type:* CONSTANT

### graphics.TEXTURE_FORMAT_LUMINANCE
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_LUMINANCE_ALPHA
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_R16F
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_R32F
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_R32UI
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_R_BC4
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_R_ETC2
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RG16F
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RG32F
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RG_BC5
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RG_ETC2
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGB
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGB16F
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGB32F
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGB_16BPP
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGB_BC1
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGB_ETC1
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGB_PVRTC_2BPPV1
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGB_PVRTC_4BPPV1
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGBA
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGBA16F
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGBA32F
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGBA32UI
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGBA_16BPP
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGBA_ASTC_4X4
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGBA_BC3
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGBA_BC7
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGBA_ETC2
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGBA_PVRTC_2BPPV1
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_RGBA_PVRTC_4BPPV1
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_FORMAT_STENCIL
*Type:* CONSTANT

### graphics.TEXTURE_TYPE_2D
*Type:* CONSTANT

### graphics.TEXTURE_TYPE_2D_ARRAY
*Type:* CONSTANT

### graphics.TEXTURE_TYPE_3D
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_TYPE_CUBE_MAP
*Type:* CONSTANT

### graphics.TEXTURE_TYPE_IMAGE_2D
*Type:* CONSTANT

### graphics.TEXTURE_TYPE_IMAGE_3D
*Type:* CONSTANT
May be nil if the graphics driver doesn't support it

### graphics.TEXTURE_USAGE_FLAG_COLOR
*Type:* CONSTANT

### graphics.TEXTURE_USAGE_FLAG_INPUT
*Type:* CONSTANT

### graphics.TEXTURE_USAGE_FLAG_MEMORYLESS
*Type:* CONSTANT

### graphics.TEXTURE_USAGE_FLAG_SAMPLE
*Type:* CONSTANT

### graphics.TEXTURE_USAGE_FLAG_STORAGE
*Type:* CONSTANT

### graphics.TEXTURE_WRAP_CLAMP_TO_BORDER
*Type:* CONSTANT

### graphics.TEXTURE_WRAP_CLAMP_TO_EDGE
*Type:* CONSTANT

### graphics.TEXTURE_WRAP_MIRRORED_REPEAT
*Type:* CONSTANT

### graphics.TEXTURE_WRAP_REPEAT
*Type:* CONSTANT
