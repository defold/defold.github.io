# Graphics

**Namespace:** `graphics`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_graphics.cpp`
**Source:** `engine/script/src/script_graphics.cpp`

Graphics functions and constants.

## API

### graphics.BLEND_EQUATION_ADD
*Type:* CONSTANT

### graphics.BLEND_EQUATION_MAX
*Type:* CONSTANT

### graphics.BLEND_EQUATION_MIN
*Type:* CONSTANT

### graphics.BLEND_EQUATION_REVERSE_SUBTRACT
*Type:* CONSTANT

### graphics.BLEND_EQUATION_SUBTRACT
*Type:* CONSTANT

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

### graphics.CONTEXT_FEATURE_3D_TEXTURES
*Type:* CONSTANT
Context feature flag indicating support for 3D (volume) textures.

### graphics.CONTEXT_FEATURE_ASTC_ARRAY_TEXTURES
*Type:* CONSTANT
Context feature flag indicating support for ASTC compressed 2D array textures.
Some WebGL/GLES drivers fail array texture ASTC uploads while 2D ASTC works.

### graphics.CONTEXT_FEATURE_BLEND_EQUATION_MIN_MAX
*Type:* CONSTANT
Context feature flag indicating support for min/max blend equations.
Requires GLES3+ or EXT_blend_minmax.

### graphics.CONTEXT_FEATURE_COMPUTE_SHADER
*Type:* CONSTANT
Context feature flag indicating support for compute shaders.

### graphics.CONTEXT_FEATURE_INSTANCING
*Type:* CONSTANT
Context feature flag indicating support for hardware instancing.

### graphics.CONTEXT_FEATURE_MULTI_TARGET_RENDERING
*Type:* CONSTANT
Context feature flag indicating support for rendering to multiple color targets simultaneously.

### graphics.CONTEXT_FEATURE_STORAGE_BUFFER
*Type:* CONSTANT
Context feature flag indicating support for storage buffers.

### graphics.CONTEXT_FEATURE_TEXTURE_ARRAY
*Type:* CONSTANT
Context feature flag indicating support for texture arrays.

### graphics.CONTEXT_FEATURE_VSYNC
*Type:* CONSTANT
Context feature flag indicating support for vertical sync (vsync).

### graphics.FACE_TYPE_BACK
*Type:* CONSTANT

### graphics.FACE_TYPE_FRONT
*Type:* CONSTANT

### graphics.FACE_TYPE_FRONT_AND_BACK
*Type:* CONSTANT

### graphics.get_adapter_info
*Type:* FUNCTION
Returns a table describing the active graphics context: the adapter family,
its hardware limits, the list of driver-reported extensions, and the set of
optional context features supported by the backend.

**Returns**

- `info` (table) - table with the following fields:
<code>family</code>         <span class="type">string</span>   adapter family name (e.g. "opengl", "vulkan")
  <code>version_major</code>  <span class="type">number</span>   adapter API major version (e.g. 1 for Vulkan 1.4)
  <code>version_minor</code>  <span class="type">number</span>   adapter API minor version (e.g. 4 for Vulkan 1.4)
<code>limits</code>         <span class="type">table</span>    hardware/driver limits:
<div class="codehilite"><pre><span></span><code><span class="n n-Quoted">`max_texture_size_2d`</span><span class="w">              </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">2D</span><span class="w"> </span><span class="n">texture</span><span class="w"> </span><span class="n">dimension</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">texels</span><span class="w"></span>
<span class="n n-Quoted">`max_texture_size_3d`</span><span class="w">              </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">3D</span><span class="w"> </span><span class="p">(</span><span class="n">volume</span><span class="p">)</span><span class="w"> </span><span class="n">texture</span><span class="w"> </span><span class="n">dimension</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">texels</span><span class="w"></span>
<span class="n n-Quoted">`max_texture_size_cube`</span><span class="w">            </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="k">cube</span><span class="w"> </span><span class="n">map</span><span class="w"> </span><span class="n">face</span><span class="w"> </span><span class="n">dimension</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">texels</span><span class="w"></span>
<span class="n n-Quoted">`max_texture_array_layers`</span><span class="w">         </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">layers</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">an</span><span class="w"> </span><span class="k">array</span><span class="w"> </span><span class="n">texture</span><span class="w"></span>
<span class="n n-Quoted">`max_framebuffer_width`</span><span class="w">            </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">framebuffer</span><span class="w"> </span><span class="n">width</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">pixels</span><span class="w"></span>
<span class="n n-Quoted">`max_framebuffer_height`</span><span class="w">           </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">framebuffer</span><span class="w"> </span><span class="n">height</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="n">pixels</span><span class="w"></span>
<span class="n n-Quoted">`max_color_attachments`</span><span class="w">            </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">simultaneous</span><span class="w"> </span><span class="n">color</span><span class="w"> </span><span class="n">attachments</span><span class="w"></span>
<span class="n n-Quoted">`max_samplers_per_stage`</span><span class="w">           </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">texture</span><span class="w"> </span><span class="n">samplers</span><span class="w"> </span><span class="n">per</span><span class="w"> </span><span class="n">shader</span><span class="w"> </span><span class="n">stage</span><span class="w"></span>
<span class="n n-Quoted">`max_textures_per_stage`</span><span class="w">           </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">sampled</span><span class="w"> </span><span class="n">textures</span><span class="w"> </span><span class="n">per</span><span class="w"> </span><span class="n">shader</span><span class="w"> </span><span class="n">stage</span><span class="w"></span>
<span class="n n-Quoted">`max_vertex_attributes`</span><span class="w">            </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">vertex</span><span class="w"> </span><span class="n">attributes</span><span class="w"></span>
<span class="n n-Quoted">`max_vertex_buffers`</span><span class="w">               </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">vertex</span><span class="w"> </span><span class="n">buffer</span><span class="w"> </span><span class="n">bindings</span><span class="w"></span>
<span class="n n-Quoted">`max_compute_workgroup_size_x`</span><span class="w">     </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">compute</span><span class="w"> </span><span class="n">workgroup</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="p">(</span><span class="n">X</span><span class="p">)</span><span class="w"></span>
<span class="n n-Quoted">`max_compute_workgroup_size_y`</span><span class="w">     </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">compute</span><span class="w"> </span><span class="n">workgroup</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="p">(</span><span class="n">Y</span><span class="p">)</span><span class="w"></span>
<span class="n n-Quoted">`max_compute_workgroup_size_z`</span><span class="w">     </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">compute</span><span class="w"> </span><span class="n">workgroup</span><span class="w"> </span><span class="n">size</span><span class="w"> </span><span class="p">(</span><span class="n">Z</span><span class="p">)</span><span class="w"></span>
<span class="n n-Quoted">`max_compute_workgroup_invocations`</span><span class="w"> </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w"> </span><span class="n">max</span><span class="w"> </span><span class="n">invocations</span><span class="w"> </span><span class="n">per</span><span class="w"> </span><span class="n">compute</span><span class="w"> </span><span class="n">workgroup</span><span class="w"></span>
<span class="n n-Quoted">`max_compute_shared_memory_size`</span><span class="w">   </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">shared</span><span class="w"> </span><span class="k">memory</span><span class="w"> </span><span class="n">per</span><span class="w"> </span><span class="n">compute</span><span class="w"> </span><span class="n">workgroup</span><span class="w"> </span><span class="p">(</span><span class="n">bytes</span><span class="p">)</span><span class="w"></span>
<span class="n n-Quoted">`max_uniform_buffer_range`</span><span class="w">         </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">bindable</span><span class="w"> </span><span class="n">uniform</span><span class="w"> </span><span class="n">buffer</span><span class="w"> </span><span class="k">range</span><span class="w"> </span><span class="p">(</span><span class="n">bytes</span><span class="p">)</span><span class="w"></span>
<span class="n n-Quoted">`max_storage_buffer_range`</span><span class="w">         </span><span class="err">[</span><span class="k">type</span><span class="o">:</span><span class="k">number</span><span class="err">]</span><span class="w">  </span><span class="n">max</span><span class="w"> </span><span class="n">bindable</span><span class="w"> </span><span class="k">storage</span><span class="w"> </span><span class="n">buffer</span><span class="w"> </span><span class="k">range</span><span class="w"> </span><span class="p">(</span><span class="n">bytes</span><span class="p">)</span><span class="w"></span>
</code></pre></div>

<code>extensions</code>     <span class="type">table</span>    array of driver-reported extension name strings
<code>features</code>       <span class="type">table</span>    array of supported context feature ids:
<div class="codehilite"><pre><span></span><code><span class="err">`</span><span class="n">graphics</span><span class="p">.</span><span class="n">CONTEXT_FEATURE_MULTI_TARGET_RENDERING</span><span class="err">`</span>  <span class="n">multi</span><span class="o">-</span><span class="n">target</span> <span class="n">rendering</span>
<span class="err">`</span><span class="n">graphics</span><span class="p">.</span><span class="n">CONTEXT_FEATURE_TEXTURE_ARRAY</span><span class="err">`</span>           <span class="n">texture</span> <span class="n">arrays</span>
<span class="err">`</span><span class="n">graphics</span><span class="p">.</span><span class="n">CONTEXT_FEATURE_COMPUTE_SHADER</span><span class="err">`</span>          <span class="n">compute</span> <span class="n">shaders</span>
<span class="err">`</span><span class="n">graphics</span><span class="p">.</span><span class="n">CONTEXT_FEATURE_STORAGE_BUFFER</span><span class="err">`</span>          <span class="n">storage</span> <span class="n">buffers</span>
<span class="err">`</span><span class="n">graphics</span><span class="p">.</span><span class="n">CONTEXT_FEATURE_VSYNC</span><span class="err">`</span>                   <span class="n">vertical</span> <span class="n">sync</span>
<span class="err">`</span><span class="n">graphics</span><span class="p">.</span><span class="n">CONTEXT_FEATURE_INSTANCING</span><span class="err">`</span>              <span class="n">hardware</span> <span class="n">instancing</span>
<span class="err">`</span><span class="n">graphics</span><span class="p">.</span><span class="n">CONTEXT_FEATURE_3D_TEXTURES</span><span class="err">`</span>             <span class="mi">3</span><span class="n">D</span> <span class="p">(</span><span class="n">volume</span><span class="p">)</span> <span class="n">textures</span>
<span class="err">`</span><span class="n">graphics</span><span class="p">.</span><span class="n">CONTEXT_FEATURE_ASTC_ARRAY_TEXTURES</span><span class="err">`</span>     <span class="n">ASTC</span> <span class="n">compressed</span> <span class="mi">2</span><span class="n">D</span> <span class="n">array</span> <span class="n">textures</span>
<span class="err">`</span><span class="n">graphics</span><span class="p">.</span><span class="n">CONTEXT_FEATURE_BLEND_EQUATION_MIN_MAX</span><span class="err">`</span>  <span class="n">min</span><span class="o">/</span><span class="n">max</span> <span class="n">blend</span> <span class="n">equations</span>
</code></pre></div>

### graphics.get_engine_adapters
*Type:* FUNCTION
get the list of graphics adapters that have been registered with the engine

**Returns**

- `adapters` (table) - array of adapter family name strings (e.g. "opengl", "vulkan", "webgpu")

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
