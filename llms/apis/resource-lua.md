# Resource

**Namespace:** `resource`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_resource.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_resource.cpp`

Functions and constants to access resources.

## API

### resource.atlas
*Type:* FUNCTION
Constructor-like function with two purposes:

Load the specified resource as part of loading the script
Return a hash to the run-time version of the resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `path` (hash) - a path hash to the binary version of the resource

**Examples**

Load an atlas and set it to a sprite:
```
go.property("my_atlas", resource.atlas("/atlas.atlas"))
function init(self)
  go.set("#sprite", "image", self.my_atlas)
end

```

Load an atlas and set it to a gui:
```
go.property("my_atlas", resource.atlas("/atlas.atlas"))
function init(self)
  go.set("#gui", "textures", self.my_atlas, {key = "my_atlas"})
end

```

### resource.buffer
*Type:* FUNCTION
Constructor-like function with two purposes:

Load the specified resource as part of loading the script
Return a hash to the run-time version of the resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `path` (hash) - a path hash to the binary version of the resource

**Examples**

Set a unique buffer it to a sprite:
```
go.property("my_buffer", resource.buffer("/cube.buffer"))
function init(self)
  go.set("#mesh", "vertices", self.my_buffer)
end

```

### resource.create_atlas
*Type:* FUNCTION
This function creates a new atlas resource that can be used in the same way as any atlas created during build time.
The path used for creating the atlas must be unique, trying to create a resource at a path that is already
registered will trigger an error. If the intention is to instead modify an existing atlas, use the resource.set_atlas
function. Also note that the path to the new atlas resource must have a '.texturesetc' extension,
meaning "/path/my_atlas" is not a valid path but "/path/my_atlas.texturesetc" is.
When creating the atlas, at least one geometry and one animation is required, and an error will be
raised if these requirements are not met. A reference to the resource will be held by the collection
that created the resource and will automatically be released when that collection is destroyed.
Note that releasing a resource essentially means decreasing the reference count of that resource,
and not necessarily that it will be deleted.

**Notes**

- The index values are zero based where zero refers to the first entry of the vertex and uv lists

**Parameters**

- `path` (string) - The path to the resource.
- `table` (table) - A table containing info about how to create the atlas. Supported entries:
<ul>
<li>
<dl>
<dt><code>texture</code></dt>
<dd><span class="type">string | hash</span> the path to the texture resource, e.g "/main/my_texture.texturec"</dd>
</dl>
</li>
<li>
<dl>
<dt><code>animations</code></dt>
<dd><span class="type">table</span> a list of the animations in the atlas. Supports the following fields:</dd>
</dl>
</li>
<li>
<dl>
<dt><code>id</code></dt>
<dd><span class="type">string</span> the id of the animation, used in e.g sprite.play_animation</dd>
</dl>
</li>
<li>
<dl>
<dt><code>width</code></dt>
<dd><span class="type">number</span> the width of the animation</dd>
</dl>
</li>
<li>
<dl>
<dt><code>height</code></dt>
<dd><span class="type">number</span> the height of the animation</dd>
</dl>
</li>
<li>
<dl>
<dt><code>frame_start</code></dt>
<dd><span class="type">number</span> index to the first geometry of the animation. Indices are lua based and must be in the range of 1 .. <number-of-geometries> in atlas.</dd>
</dl>
</li>
<li>
<dl>
<dt><code>frame_end</code></dt>
<dd><span class="type">number</span> index to the last geometry of the animation (non-inclusive). Indices are lua based and must be in the range of 1 .. <number-of-geometries> in atlas.</dd>
</dl>
</li>
<li>
<dl>
<dt><code>playback</code></dt>
<dd><span class="type">constant</span> optional playback mode of the animation, the default value is <a href="/ref/go#go.PLAYBACK_ONCE_FORWARD">go.PLAYBACK_ONCE_FORWARD</a></dd>
</dl>
</li>
<li>
<dl>
<dt><code>fps</code></dt>
<dd><span class="type">number</span> optional fps of the animation, the default value is 30</dd>
</dl>
</li>
<li>
<dl>
<dt><code>flip_vertical</code></dt>
<dd><span class="type">boolean</span> optional flip the animation vertically, the default value is false</dd>
</dl>
</li>
<li>
<dl>
<dt><code>flip_horizontal</code></dt>
<dd><span class="type">boolean</span> optional flip the animation horizontally, the default value is false</dd>
</dl>
</li>
<li>
<dl>
<dt><code>geometries</code></dt>
<dd><span class="type">table</span> A list of the geometries that should map to the texture data. Supports the following fields:</dd>
</dl>
</li>
<li>
<dl>
<dt><code>id</code></dt>
<dd><span class="type">string</span> The name of the geometry. Used when matching animations between multiple atlases</dd>
</dl>
</li>
<li>
<dl>
<dt><code>width</code></dt>
<dd><span class="type">number</span> The width of the image the sprite geometry represents</dd>
</dl>
</li>
<li>
<dl>
<dt><code>height</code></dt>
<dd><span class="type">number</span> The height of the image the sprite geometry represents</dd>
</dl>
</li>
<li>
<dl>
<dt><code>pivot_x</code></dt>
<dd><span class="type">number</span> The pivot x value of the image in unit coords. (0,0) is upper left corner, (1,1) is bottom right. Default is 0.5.</dd>
</dl>
</li>
<li>
<dl>
<dt><code>pivot_y</code></dt>
<dd><span class="type">number</span> The pivot y value of the image in unit coords. (0,0) is upper left corner, (1,1) is bottom right. Default is 0.5.</dd>
</dl>
</li>
<li>
<dl>
<dt><code>rotated</code></dt>
<dd><span class="type">boolean</span> Whether the image is rotated 90 degrees counter-clockwise in the atlas. This affects UV coordinate generation for proper rendering. Default is false.</dd>
</dl>
</li>
<li>
<dl>
<dt><code>vertices</code></dt>
<dd><span class="type">table</span> a list of the vertices in image space of the geometry in the form {px0, py0, px1, py1, ..., pxn, pyn}</dd>
</dl>
</li>
<li>
<dl>
<dt><code>uvs</code></dt>
<dd><span class="type">table</span> a list of the uv coordinates in image space of the geometry in the form of {u0, v0, u1, v1, ..., un, vn}.</dd>
</dl>
</li>
<li>
<dl>
<dt><code>indices</code></dt>
<dd><span class="type">table</span> a list of the indices of the geometry in the form {i0, i1, i2, ..., in}. Each tripe in the list represents a triangle.</dd>
</dl>
</li>
</ul>

**Returns**

- `path` (hash) - Returns the atlas resource path

**Examples**

Create a backing texture and an atlas
```
function init(self)
    -- create an empty texture
    local tparams = {
        width          = 128,
        height         = 128,
        type           = graphics.TEXTURE_TYPE_2D,
        format         = graphics.TEXTURE_FORMAT_RGBA,
    }
    local my_texture_id = resource.create_texture("/my_texture.texturec", tparams)

    -- optionally use resource.set_texture to upload data to texture

    -- create an atlas with one animation and one square geometry
    -- note that the function doesn't support hashes for the texture,
    -- you need to use a string for the texture path here aswell
    local aparams = {
        texture = "/my_texture.texturec",
        animations = {
            {
                id          = "my_animation",
                width       = 128,
                height      = 128,
                frame_start = 1,
                frame_end   = 2,
            }
        },
        geometries = {
            {
                id = 'idle0',
                width = 128,
                height = 128,
                pivot_x = 0.5,
                pivot_y = 0.5,
                vertices  = {
                    0,   0,
                    0,   128,
                    128, 128,
                    128, 0
                },
                uvs = {
                    0,   0,
                    0,   128,
                    128, 128,
                    128, 0
                },
                indices = {0,1,2,0,2,3}
            }
        }
    }
    local my_atlas_id = resource.create_atlas("/my_atlas.texturesetc", aparams)

    -- assign the atlas to the 'sprite' component on the same go
    go.set("#sprite", "image", my_atlas_id)
end

```

### resource.create_buffer
*Type:* FUNCTION
This function creates a new buffer resource that can be used in the same way as any buffer created during build time.
The function requires a valid buffer created from either buffer.create or another pre-existing buffer resource.
By default, the new resource will take ownership of the buffer lua reference, meaning the buffer will not automatically be removed
when the lua reference to the buffer is garbage collected. This behaviour can be overruled by specifying 'transfer_ownership = false'
in the argument table. If the new buffer resource is created from a buffer object that is created by another resource,
the buffer object will be copied and the new resource will effectively own a copy of the buffer instead.
Note that the path to the new resource must have the '.bufferc' extension, "/path/my_buffer" is not a valid path but "/path/my_buffer.bufferc" is.
The path must also be unique, attempting to create a buffer with the same name as an existing resource will raise an error.

**Parameters**

- `path` (string) - The path to the resource.
- `table` (table) (optional) - A table containing info about how to create the buffer. Supported entries:
<ul>
<li>
<dl>
<dt><code>buffer</code></dt>
<dd><span class="type">buffer</span> the buffer to bind to this resource</dd>
</dl>
</li>
<li>
<dl>
<dt><code>transfer_ownership</code></dt>
<dd><span class="type">boolean</span> optional flag to determine wether or not the resource should take over ownership of the buffer object (default true)</dd>
</dl>
</li>
</ul>

**Returns**

- `path` (hash) - Returns the buffer resource path

**Examples**

Create a buffer object and bind it to a buffer resource
```
function init(self)
    local size = 1
    local positions = {
        -- triangle 1
         size,  size, 0,
        -size, -size, 0,
         size, -size, 0,
        -- triangle 2
         size, size,  0,
        -size,  size, 0,
        -size, -size, 0,
    }

    local buffer_handle = buffer.create(#positions, {
        {
            name  = hash("position"),
            type  = buffer.VALUE_TYPE_FLOAT32,
            count = 3
        }
    })

    local stream = buffer.get_stream(buffer_handle, hash("position"))

    -- transfer vertex data to buffer
    for k=1,#positions do
        stream[k] = positions[k]
    end

    local my_buffer = resource.create_buffer("/my_buffer.bufferc", { buffer = buffer_handle })
    go.set("/go#mesh", "vertices", my_buffer)
end
```Create a buffer resource from existing resource

```lua
function init(self)
    local res = resource.get_buffer("/my_buffer_path.bufferc")
    -- create a cloned buffer resource from another resource buffer
    local buf = reource.create_buffer("/my_cloned_buffer.bufferc", { buffer = res })
    -- assign cloned buffer to a mesh component
    go.set("/go#mesh", "vertices", buf)
end

```

### resource.create_sound_data
*Type:* FUNCTION
Creates a sound data resource
Supported formats are .oggc, .opusc and .wavc

**Parameters**

- `path` (string) - the path to the resource. Must not already exist.
- `options` (table) (optional) - A table containing parameters for the text. Supported entries:
<dl>
<dt><code>data</code></dt>
<dd><span class="type">string</span> The raw data of the file. May be partial, but must include the header of the file</dd>
<dt><code>filesize</code></dt>
<dd><span class="type">number</span> If the file is partial, it must also specify the full size of the complete file.</dd>
<dt><code>partial</code></dt>
<dd><span class="type">boolean</span> Is the data not representing the full file, but just the initial chunk?</dd>
</dl>

**Returns**

- `path_hash` (hash) - the resulting path hash to the resource

**Examples**

```
function init(self)
    -- create a new sound resource, given the initial chunk of the file
    local relative_path = "/a/unique/resource/name.oggc"
    local hash = resource.create_sound_data(relative_path, { data = data, filesize = filesize, partial = true })
    go.set("#music", "sound", hash) -- override the previous sound resource
    sound.play("#music") -- start the playing
end

```

### resource.create_texture
*Type:* FUNCTION
Creates a new texture resource that can be used in the same way as any texture created during build time.
The path used for creating the texture must be unique, trying to create a resource at a path that is already
registered will trigger an error. If the intention is to instead modify an existing texture, use the resource.set_texture
function. Also note that the path to the new texture resource must have a '.texturec' extension,
meaning "/path/my_texture" is not a valid path but "/path/my_texture.texturec" is.
If the texture is created without a buffer, the pixel data will be blank.

**Parameters**

- `path` (string) - The path to the resource.
- `table` (table) - A table containing info about how to create the texture. Supported entries:
<dl>
<dt><code>type</code></dt>
<dd><span class="type">number</span> The texture type. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_TYPE_2D</code></li>
<li><code>graphics.TEXTURE_TYPE_IMAGE_2D</code></li>
<li><code>graphics.TEXTURE_TYPE_3D</code></li>
<li><code>graphics.TEXTURE_TYPE_IMAGE_3D</code></li>
<li><code>graphics.TEXTURE_TYPE_CUBE_MAP</code></li>
</ul>
<dl>
<dt><code>width</code></dt>
<dd><span class="type">number</span> The width of the texture (in pixels). Must be larger than 0.</dd>
<dt><code>height</code></dt>
<dd><span class="type">number</span> The width of the texture (in pixels). Must be larger than 0.</dd>
<dt><code>depth</code></dt>
<dd><span class="type">number</span> The depth of the texture (in pixels). Must be larger than 0. Only used when <code>type</code> is <code>graphics.TEXTURE_TYPE_3D</code> or <code>graphics.TEXTURE_TYPE_IMAGE_3D</code>.</dd>
<dt><code>format</code></dt>
<dd><span class="type">number</span> The texture format, note that some of these formats might not be supported by the running device. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_FORMAT_LUMINANCE</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGB</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA</code></li>
</ul>
These constants might not be available on the device:
<ul>
<li><code>graphics.TEXTURE_FORMAT_RGB_PVRTC_2BPPV1</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGB_PVRTC_4BPPV1</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA_PVRTC_2BPPV1</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA_PVRTC_4BPPV1</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGB_ETC1</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA_ETC2</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA_ASTC_4X4</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGB_BC1</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA_BC3</code></li>
<li><code>graphics.TEXTURE_FORMAT_R_BC4</code></li>
<li><code>graphics.TEXTURE_FORMAT_RG_BC5</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA_BC7</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGB16F</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGB32F</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA16F</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA32F</code></li>
<li><code>graphics.TEXTURE_FORMAT_R16F</code></li>
<li><code>graphics.TEXTURE_FORMAT_RG16F</code></li>
<li><code>graphics.TEXTURE_FORMAT_R32F</code></li>
<li><code>graphics.TEXTURE_FORMAT_RG32F</code></li>
</ul>
You can test if the device supports these values by checking if a specific enum is nil or not:
<div class="codehilite"><pre><span></span><code><span class="kr">if</span> <span class="n">graphics</span><span class="p">.</span><span class="n">TEXTURE_FORMAT_RGBA16F</span> <span class="o">~=</span> <span class="kc">nil</span> <span class="kr">then</span>
    <span class="c1">-- it is safe to use this format</span>
<span class="kr">end</span>
</code></pre></div>

<dl>
<dt><code>flags</code></dt>
<dd><span class="type">number</span> Texture creation flags that can be used to dictate how the texture is created. The default value is <a href="/ref/graphics#graphics.TEXTURE_USAGE_FLAG_SAMPLE">graphics.TEXTURE_USAGE_FLAG_SAMPLE</a>, which means that the texture can be sampled from a shader.
These flags may or may not be supported on the running device and/or the underlying graphics API and is simply used internally as a 'hint' when creating the texture. There is no guarantee that any of these will have any effect. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_USAGE_FLAG_SAMPLE</code> - The texture can be sampled from a shader (default)</li>
<li><code>graphics.TEXTURE_USAGE_FLAG_MEMORYLESS</code> - The texture can be used as a memoryless texture, i.e only transient memory for the texture is used during rendering</li>
<li><code>graphics.TEXTURE_USAGE_FLAG_STORAGE</code> - The texture can be used as a storage texture, which is required for a shader to write to the texture</li>
</ul>
<dl>
<dt><code>max_mipmaps</code></dt>
<dd><span class="type">number</span> optional max number of mipmaps. Defaults to zero, i.e no mipmap support</dd>
<dt><code>compression_type</code></dt>
<dd><span class="type">number</span> optional specify the compression type for the data in the buffer object that holds the texture data. Will only be used when a compressed buffer has been passed into the function.
Creating an empty texture with no buffer data is not supported as a core feature. Defaults to graphics.COMPRESSION_TYPE_DEFAULT, i.e no compression. Supported values:</dd>
</dl>
<ul>
<li><code>COMPRESSION_TYPE_DEFAULT</code></li>
<li><code>COMPRESSION_TYPE_BASIS_UASTC</code></li>
</ul>
- `buffer` (buffer) - optional buffer of precreated pixel data

**Returns**

- `path` (hash) - The path to the resource.
<span class="icon-attention"></span> 3D Textures are currently only supported on OpenGL and Vulkan adapters. To check if your device supports 3D textures, use:
```lua
if graphics.TEXTURE_TYPE_3D ~= nil then
    -- Device and graphics adapter support 3D textures
end

**Examples**

How to create an 128x128 RGBA texture resource and assign it to a model
```
function init(self)
    local tparams = {
       width          = 128,
       height         = 128,
       type           = graphics.TEXTURE_TYPE_2D,
       format         = graphics.TEXTURE_FORMAT_RGBA,
   }
   local my_texture_id = resource.create_texture("/my_custom_texture.texturec", tparams)
   go.set("#model", "texture0", my_texture_id)
end
```How to create an 128x128 floating point texture (RGBA32F) resource from a buffer object

```lua
function init(self)
    -- Create a new buffer with 4 components and FLOAT32 type
    local tbuffer = buffer.create(128 * 128, { {name=hash("rgba"), type=buffer.VALUE_TYPE_FLOAT32, count=4} } )
    local tstream = buffer.get_stream(tbuffer, hash("rgba"))

    -- Fill the buffer stream with some float values
    for y=1,128 do
        for x=1,128 do
            local index = (y-1) * 128 * 4 + (x-1) * 4 + 1
            tstream[index + 0] = 999.0
            tstream[index + 1] = -1.0
            tstream[index + 2] = 0.5
            tstream[index + 3] = 1.0
        end
    end

    -- Create a 2D Texture with a RGBA23F format
    local tparams = {
       width          = 128,
       height         = 128,
       type           = graphics.TEXTURE_TYPE_2D,
       format         = graphics.TEXTURE_FORMAT_RGBA32F,
   }

   -- Note that we pass the buffer as the last argument here!
   local my_texture_id = resource.create_texture("/my_custom_texture.texturec", tparams, tbuffer)

   -- assign the texture to a model
   go.set("#model", "texture0", my_texture_id)
end
```How to create a 32x32x32 floating point 3D texture that can be used to generate volumetric data in a compute shader

```lua
function init(self)
    local t_volume = resource.create_texture("/my_backing_texture.texturec", {
        type   = graphics.TEXTURE_TYPE_IMAGE_3D,
        width  = 32,
        height = 32,
        depth  = 32,
        format = resource.TEXTURE_FORMAT_RGBA32F,
        flags  = resource.TEXTURE_USAGE_FLAG_STORAGE + resource.TEXTURE_USAGE_FLAG_SAMPLE,
    })

    -- pass the backing texture to the render script
    msg.post("@render:", "add_textures", { t_volume })
end
```How to create 512x512 texture array with 5 pages.

```lua
        local new_tex = resource.create_texture("/runtime/example_array.texturec", {
            type = graphics.TEXTURE_TYPE_2D_ARRAY,
            width = 512,
            height = 512,
            page_count = 5,
            format = graphics.TEXTURE_FORMAT_RGB,
        })

```

### resource.create_texture_async
*Type:* FUNCTION
Creates a new texture resource that can be used in the same way as any texture created during build time.
The path used for creating the texture must be unique, trying to create a resource at a path that is already
registered will trigger an error. If the intention is to instead modify an existing texture, use the resource.set_texture
function. Also note that the path to the new texture resource must have a '.texturec' extension,
meaning "/path/my_texture" is not a valid path but "/path/my_texture.texturec" is.
If the texture is created without a buffer, the pixel data will be blank.
The difference between the async version and resource.create_texture is that the texture data will be uploaded
in a graphics worker thread. The function will return a resource immediately that contains a 1x1 blank texture which can be used
immediately after the function call. When the new texture has been uploaded, the initial blank texture will be deleted and replaced with the
new texture. Be careful when using the initial texture handle handle as it will not be valid after the upload has finished.

**Parameters**

- `path` (string | hash) - The path to the resource.
- `table` (table) - <dl>
<dt>A table containing info about how to create the texture. Supported entries:</dt>
<dt><code>type</code></dt>
<dd><span class="type">number</span> The texture type. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_TYPE_2D</code></li>
<li><code>graphics.TEXTURE_TYPE_IMAGE_2D</code></li>
<li><code>graphics.TEXTURE_TYPE_3D</code></li>
<li><code>graphics.TEXTURE_TYPE_IMAGE_3D</code></li>
<li><code>graphics.TEXTURE_TYPE_CUBE_MAP</code></li>
</ul>
<dl>
<dt><code>width</code></dt>
<dd><span class="type">number</span> The width of the texture (in pixels). Must be larger than 0.</dd>
<dt><code>height</code></dt>
<dd><span class="type">number</span> The width of the texture (in pixels). Must be larger than 0.</dd>
<dt><code>depth</code></dt>
<dd><span class="type">number</span> The depth of the texture (in pixels). Must be larger than 0. Only used when <code>type</code> is <code>graphics.TEXTURE_TYPE_3D</code> or <code>graphics.TEXTURE_TYPE_IMAGE_3D</code>.</dd>
<dt><code>format</code></dt>
<dd><span class="type">number</span> The texture format, note that some of these formats might not be supported by the running device. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_FORMAT_LUMINANCE</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGB</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA</code></li>
</ul>
These constants might not be available on the device:
<ul>
<li><code>graphics.TEXTURE_FORMAT_RGB_PVRTC_2BPPV1</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGB_PVRTC_4BPPV1</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA_PVRTC_2BPPV1</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA_PVRTC_4BPPV1</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGB_ETC1</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA_ETC2</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA_ASTC_4X4</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGB_BC1</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA_BC3</code></li>
<li><code>graphics.TEXTURE_FORMAT_R_BC4</code></li>
<li><code>graphics.TEXTURE_FORMAT_RG_BC5</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA_BC7</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGB16F</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGB32F</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA16F</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA32F</code></li>
<li><code>graphics.TEXTURE_FORMAT_R16F</code></li>
<li><code>graphics.TEXTURE_FORMAT_RG16F</code></li>
<li><code>graphics.TEXTURE_FORMAT_R32F</code></li>
<li><code>graphics.TEXTURE_FORMAT_RG32F</code></li>
</ul>
You can test if the device supports these values by checking if a specific enum is nil or not:
<div class="codehilite"><pre><span></span><code><span class="kr">if</span> <span class="n">graphics</span><span class="p">.</span><span class="n">TEXTURE_FORMAT_RGBA16F</span> <span class="o">~=</span> <span class="kc">nil</span> <span class="kr">then</span>
    <span class="c1">-- it is safe to use this format</span>
<span class="kr">end</span>
</code></pre></div>

<dl>
<dt><code>flags</code></dt>
<dd><span class="type">number</span> Texture creation flags that can be used to dictate how the texture is created. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_USAGE_FLAG_SAMPLE</code> - The texture can be sampled from a shader (default)</li>
<li><code>graphics.TEXTURE_USAGE_FLAG_MEMORYLESS</code> - The texture can be used as a memoryless texture, i.e only transient memory for the texture is used during rendering</li>
<li><code>graphics.TEXTURE_USAGE_FLAG_STORAGE</code> - The texture can be used as a storage texture, which is required for a shader to write to the texture</li>
</ul>
<dl>
<dt><code>max_mipmaps</code></dt>
<dd><span class="type">number</span> optional max number of mipmaps. Defaults to zero, i.e no mipmap support</dd>
<dt><code>compression_type</code></dt>
<dd><span class="type">number</span> optional specify the compression type for the data in the buffer object that holds the texture data. Will only be used when a compressed buffer has been passed into the function.
Creating an empty texture with no buffer data is not supported as a core feature. Defaults to graphics.COMPRESSION_TYPE_DEFAULT, i.e no compression. Supported values:</dd>
</dl>
<ul>
<li><code>COMPRESSION_TYPE_DEFAULT</code></li>
<li><code>COMPRESSION_TYPE_BASIS_UASTC</code></li>
</ul>
- `buffer` (buffer) - optional buffer of precreated pixel data
- `callback` (function) - callback function when texture is created (self, request_id, resource)

**Returns**

- `path` (hash) - The path to the texture resource.
- `request_id` (number) - The request id for the async request.
<span class="icon-attention"></span> 3D Textures are currently only supported on OpenGL and Vulkan adapters. To check if your device supports 3D textures, use:
```lua
if graphics.TEXTURE_TYPE_3D ~= nil then
    -- Device and graphics adapter support 3D textures
end

**Examples**

Create a texture resource asyncronously with a buffer and a callback
```
function callback(self, request_id, resource)
    -- The resource has been updated with a new texture,
    -- so we can update other systems with the new handle,
    -- or update components to use the resource if we want
    local tinfo = resource.get_texture_info(resource)
    msg.post("@render:", "set_backing_texture", tinfo.handle)
end
function init(self)
    -- Create a texture resource async
    local tparams = {
        width          = 128,
        height         = 128,
        type           = graphics.TEXTURE_TYPE_2D,
        format         = graphics.TEXTURE_FORMAT_RGBA,
    }

    -- Create a new buffer with 4 components
    local tbuffer = buffer.create(tparams.width * tparams.height, { {name=hash("rgba"), type=buffer.VALUE_TYPE_UINT8, count=4} } )
    local tstream = buffer.get_stream(tbuffer, hash("rgba"))

    -- Fill the buffer stream with some float values
    for y=1,tparams.width do
        for x=1,tparams.height do
            local index = (y-1) * 128 * 4 + (x-1) * 4 + 1
            tstream[index + 0] = 255
            tstream[index + 1] = 0
            tstream[index + 2] = 255
            tstream[index + 3] = 255
        end
    end
    -- create the texture
    local tpath, request_id = resource.create_texture_async("/my_texture.texturec", tparams, tbuffer, callback)
    -- at this point you can use the resource as-is, but note that the texture will be a blank 1x1 texture
    -- that will be removed once the new texture has been updated
    go.set("#model", "texture0", tpath)
end
```Create a texture resource asyncronously without a callback

```lua
function init(self)
    -- Create a texture resource async
    local tparams = {
        width          = 128,
        height         = 128,
        type           = graphics.TEXTURE_TYPE_2D,
        format         = graphics.TEXTURE_FORMAT_RGBA,
    }

    -- Create a new buffer with 4 components
    local tbuffer = buffer.create(tparams.width * tparams.height, { {name=hash("rgba"), type=buffer.VALUE_TYPE_UINT8, count=4} } )
    local tstream = buffer.get_stream(tbuffer, hash("rgba"))

    -- Fill the buffer stream with some float values
    for y=1,tparams.width do
        for x=1,tparams.height do
            local index = (y-1) * 128 * 4 + (x-1) * 4 + 1
            tstream[index + 0] = 255
            tstream[index + 1] = 0
            tstream[index + 2] = 255
            tstream[index + 3] = 255
        end
    end
    -- create the texture
    local tpath, request_id = resource.create_texture_async("/my_texture.texturec", tparams, tbuffer)
    -- at this point you can use the resource as-is, but note that the texture will be a blank 1x1 texture
    -- that will be removed once the new texture has been updated
    go.set("#model", "texture0", tpath)
end

```

### resource.font
*Type:* FUNCTION
Constructor-like function with two purposes:

Load the specified resource as part of loading the script
Return a hash to the run-time version of the resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `path` (hash) - a path hash to the binary version of the resource

**Examples**

Load a font and set it to a label:
```
go.property("my_font", resource.font("/font.font"))
function init(self)
  go.set("#label", "font", self.my_font)
end

```

Load a font and set it to a gui:
```
go.property("my_font", resource.font("/font.font"))
function init(self)
  go.set("#gui", "fonts", self.my_font, {key = "my_font"})
end

```

### resource.get_atlas
*Type:* FUNCTION
Returns the atlas data for an atlas

**Parameters**

- `path` (hash | string) - The path to the atlas resource

**Returns**

- `data` (table) - A table with the following entries:
<ul>
<li>texture</li>
<li>geometries</li>
<li>animations</li>
</ul>
See <a href="/ref/resource#resource.set_atlas">resource.set_atlas</a> for a detailed description of each field

### resource.get_buffer
*Type:* FUNCTION
gets the buffer from a resource

**Parameters**

- `path` (hash | string) - The path to the resource

**Returns**

- `buffer` (buffer) - The resource buffer

**Examples**

How to get the data from a buffer
```
function init(self)

    local res_path = go.get("#mesh", "vertices")
    local buf = resource.get_buffer(res_path)
    local stream_positions = buffer.get_stream(buf, "position")

    for i=1,#stream_positions do
        print(i, stream_positions[i])
    end
end

```

### resource.get_render_target_info
*Type:* FUNCTION
Gets render target info from a render target resource path or a render target handle

**Parameters**

- `path` (hash | string | number) - The path to the resource or a render target handle

**Returns**

- `table` (table) - A table containing info about the render target:
<dl>
<dt><code>handle</code></dt>
<dd><span class="type">number</span> the opaque handle to the texture resource</dd>
<dt>'attachments'</dt>
<dd><span class="type">table</span> a table of attachments, where each attachment contains the following entries:</dd>
<dt><code>width</code></dt>
<dd><span class="type">number</span> width of the texture</dd>
<dt><code>height</code></dt>
<dd><span class="type">number</span> height of the texture</dd>
<dt><code>depth</code></dt>
<dd><span class="type">number</span> depth of the texture (i.e 1 for a 2D texture and 6 for a cube map)</dd>
<dt><code>mipmaps</code></dt>
<dd><span class="type">number</span> number of mipmaps of the texture</dd>
<dt><code>type</code></dt>
<dd><span class="type">number</span> The texture type. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_TYPE_2D</code></li>
<li><code>graphics.TEXTURE_TYPE_CUBE_MAP</code></li>
<li><code>graphics.TEXTURE_TYPE_2D_ARRAY</code></li>
</ul>
<dl>
<dt><code>buffer_type</code></dt>
<dd><span class="type">number</span> The attachment buffer type. Supported values:</dd>
</dl>
<ul>
<li><code>resource.BUFFER_TYPE_COLOR0</code></li>
<li><code>resource.BUFFER_TYPE_COLOR1</code></li>
<li><code>resource.BUFFER_TYPE_COLOR2</code></li>
<li><code>resource.BUFFER_TYPE_COLOR3</code></li>
<li><code>resource.BUFFER_TYPE_DEPTH</code></li>
<li>
<code>resource.BUFFER_TYPE_STENCIL</code>
</li>
<li>
<dl>
<dt><code>texture</code></dt>
<dd><span class="type">hash</span> The hashed path to the attachment texture resource. This field is only available if the render target passed in is a resource.</dd>
</dl>
</li>
</ul>

**Examples**

Get the metadata from a render target resource
```
function init(self)
    local info = resource.get_render_target_info("/my_render_target.render_targetc")
    -- the info table contains meta data about all the render target attachments
    -- so it's not necessary to use resource.get_texture here, but we do it here
    -- just to show that it's possible:
    local info_attachment_1 = resource.get_texture_info(info.attachments[1].handle)
end
```Get a texture attachment from a render target and set it on a model component

```lua
function init(self)
    local info = resource.get_render_target_info("/my_render_target.render_targetc")
    local attachment = info.attachments[1].texture
    -- you can also get texture info from the 'texture' field, since it's a resource hash
    local texture_info = resource.get_texture_info(attachment)
    go.set("#model", "texture0", attachment)
end

```

### resource.get_text_metrics
*Type:* FUNCTION
Gets the text metrics from a font

**Parameters**

- `url` (hash) - the font to get the (unscaled) metrics from
- `text` (string) - text to measure
- `options` (table) (optional) - A table containing parameters for the text. Supported entries:
<dl>
<dt><code>width</code></dt>
<dd><span class="type">number</span> The width of the text field. Not used if <code>line_break</code> is false.</dd>
<dt><code>leading</code></dt>
<dd><span class="type">number</span> The leading (default 1.0)</dd>
<dt><code>tracking</code></dt>
<dd><span class="type">number</span> The tracking (default 0.0)</dd>
<dt><code>line_break</code></dt>
<dd><span class="type">boolean</span> If the calculation should consider line breaks (default false)</dd>
</dl>

**Returns**

- `metrics` (table) - a table with the following fields:
<ul>
<li>width</li>
<li>height</li>
<li>max_ascent</li>
<li>max_descent</li>
</ul>

**Examples**

```
function init(self)
    local font = go.get("#label", "font")
    local metrics = resource.get_text_metrics(font, "The quick brown fox\n jumps over the lazy dog")
    pprint(metrics)
end

```

### resource.get_texture_info
*Type:* FUNCTION
Gets texture info from a texture resource path or a texture handle

**Parameters**

- `path` (hash | string | number) - The path to the resource or a texture handle

**Returns**

- `table` (table) - A table containing info about the texture:
<dl>
<dt><code>handle</code></dt>
<dd><span class="type">number</span> the opaque handle to the texture resource</dd>
<dt><code>width</code></dt>
<dd><span class="type">number</span> width of the texture</dd>
<dt><code>height</code></dt>
<dd><span class="type">number</span> height of the texture</dd>
<dt><code>depth</code></dt>
<dd><span class="type">number</span> depth of the texture (i.e 1 for a 2D texture, 6 for a cube map, the actual depth of a 3D texture)</dd>
<dt><code>page_count</code></dt>
<dd><span class="type">number</span> number of pages of the texture array. For 2D texture value is 1. For cube map - 6</dd>
<dt><code>mipmaps</code></dt>
<dd><span class="type">number</span> number of mipmaps of the texture</dd>
<dt><code>flags</code></dt>
<dd><span class="type">number</span> usage hints of the texture.</dd>
<dt><code>type</code></dt>
<dd><span class="type">number</span> The texture type. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_TYPE_2D</code></li>
<li><code>graphics.TEXTURE_TYPE_2D_ARRAY</code></li>
<li><code>graphics.TEXTURE_TYPE_IMAGE_2D</code></li>
<li><code>graphics.TEXTURE_TYPE_3D</code></li>
<li><code>graphics.TEXTURE_TYPE_IMAGE_3D</code></li>
<li><code>graphics.TEXTURE_TYPE_CUBE_MAP</code></li>
</ul>

**Examples**

Create a new texture and get the metadata from it
```
function init(self)
    -- create an empty texture
    local tparams = {
        width          = 128,
        height         = 128,
        type           = graphics.TEXTURE_TYPE_2D,
        format         = graphics.TEXTURE_FORMAT_RGBA,
    }

    local my_texture_path = resource.create_texture("/my_texture.texturec", tparams)
    local my_texture_info = resource.get_texture_info(my_texture_path)

    -- my_texture_info now contains
    -- {
    --      handle = ,
    --      width = 128,
    --      height = 128,
    --      depth = 1
    --      mipmaps = 1,
    --      page_count = 1,
    --      type = graphics.TEXTURE_TYPE_2D,
    --      flags = graphics.TEXTURE_USAGE_FLAG_SAMPLE
    -- }
end
```Get the meta data from an atlas resource

```lua
function init(self)
    local my_atlas_info   = resource.get_atlas("/my_atlas.a.texturesetc")
    local my_texture_info = resource.get_texture_info(my_atlas_info.texture)

    -- my_texture_info now contains the information about the texture that is backing the atlas
end

```

### resource.load
*Type:* FUNCTION
Loads the resource data for a specific resource.

**Parameters**

- `path` (string) - The path to the resource

**Returns**

- `buffer` (buffer) - Returns the buffer stored on disc

**Examples**

```
-- read custom resource data into buffer
local buffer = resource.load("/resources/datafile")

```

In order for the engine to include custom resources in the build process, you need
to specify them in the "game.project" settings file:
```
[project]
title = My project
version = 0.1
custom_resources = resources/,assets/level_data.json

```

### resource.material
*Type:* FUNCTION
Constructor-like function with two purposes:

Load the specified resource as part of loading the script
Return a hash to the run-time version of the resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `path` (hash) - a path hash to the binary version of the resource

**Examples**

Load a material and set it to a sprite:
```
go.property("my_material", resource.material("/material.material"))
function init(self)
  go.set("#sprite", "material", self.my_material)
end

```

Load a material resource and update a named material with the resource:
```
go.property("my_material", resource.material("/material.material"))
function init(self)
  go.set("#gui", "materials", self.my_material, {key = "my_material"})
end

```

### resource.release
*Type:* FUNCTION
Release a resource.
 This is a potentially dangerous operation, releasing resources currently being used can cause unexpected behaviour.

**Parameters**

- `path` (hash | string) - The path to the resource.

### resource.render_target
*Type:* FUNCTION
Constructor-like function with two purposes:

Load the specified resource as part of loading the script
Return a hash to the run-time version of the resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `path` (hash) - a path hash to the binary version of the resource

**Examples**

Set a render target color attachment as a model texture:
```
go.property("my_render_target", resource.render_target("/rt.render_target"))
function init(self)
  local rt_info = resource.get_render_target_info(self.my_render_target)
  go.set("#model", "texture0", rt_info.attachments[1].texture)
end

```

### resource.set
*Type:* FUNCTION
Sets the resource data for a specific resource

**Parameters**

- `path` (string | hash) - The path to the resource
- `buffer` (buffer) - The buffer of precreated data, suitable for the intended resource type

**Examples**

Assuming the folder "/res" is added to the project custom resources:
```
-- load a texture resource and set it on a sprite
local buffer = resource.load("/res/new.texturec")
resource.set(go.get("#sprite", "texture0"), buffer)

```

### resource.set_atlas
*Type:* FUNCTION
Sets the data for a specific atlas resource. Setting new atlas data is specified by passing in
a texture path for the backing texture of the atlas, a list of geometries and a list of animations
that map to the entries in the geometry list. The geometry entries are represented by three lists:
vertices, uvs and indices that together represent triangles that are used in other parts of the
engine to produce render objects from.
Vertex and uv coordinates for the geometries are expected to be
in pixel coordinates where 0,0 is the top left corner of the texture.
There is no automatic padding or margin support when setting custom data,
which could potentially cause filtering artifacts if used with a material sampler that has linear filtering.
If that is an issue, you need to calculate padding and margins manually before passing in the geometry data to
this function.

**Notes**

- Custom atlas data is not compatible with slice-9 for sprites
- The index values are zero based where zero refers to the first entry of the vertex and uv lists

**Parameters**

- `path` (hash | string) - The path to the atlas resource
- `table` (table) - A table containing info about the atlas. Supported entries:
<ul>
<li>
<dl>
<dt><code>texture</code></dt>
<dd><span class="type">string | hash</span> the path to the texture resource, e.g "/main/my_texture.texturec"</dd>
</dl>
</li>
<li>
<dl>
<dt><code>animations</code></dt>
<dd><span class="type">table</span> a list of the animations in the atlas. Supports the following fields:</dd>
</dl>
</li>
<li>
<dl>
<dt><code>id</code></dt>
<dd><span class="type">string</span> the id of the animation, used in e.g sprite.play_animation</dd>
</dl>
</li>
<li>
<dl>
<dt><code>width</code></dt>
<dd><span class="type">number</span> the width of the animation</dd>
</dl>
</li>
<li>
<dl>
<dt><code>height</code></dt>
<dd><span class="type">number</span> the height of the animation</dd>
</dl>
</li>
<li>
<dl>
<dt><code>frame_start</code></dt>
<dd><span class="type">number</span> index to the first geometry of the animation. Indices are lua based and must be in the range of 1 .. <number-of-geometries> in atlas.</dd>
</dl>
</li>
<li>
<dl>
<dt><code>frame_end</code></dt>
<dd><span class="type">number</span> index to the last geometry of the animation (non-inclusive). Indices are lua based and must be in the range of 1 .. <number-of-geometries> in atlas.</dd>
</dl>
</li>
<li>
<dl>
<dt><code>playback</code></dt>
<dd><span class="type">constant</span> optional playback mode of the animation, the default value is <a href="/ref/go#go.PLAYBACK_ONCE_FORWARD">go.PLAYBACK_ONCE_FORWARD</a></dd>
</dl>
</li>
<li>
<dl>
<dt><code>fps</code></dt>
<dd><span class="type">number</span> optional fps of the animation, the default value is 30</dd>
</dl>
</li>
<li>
<dl>
<dt><code>flip_vertical</code></dt>
<dd><span class="type">boolean</span> optional flip the animation vertically, the default value is false</dd>
</dl>
</li>
<li>
<dl>
<dt><code>flip_horizontal</code></dt>
<dd><span class="type">boolean</span> optional flip the animation horizontally, the default value is false</dd>
</dl>
</li>
<li>
<dl>
<dt><code>geometries</code></dt>
<dd><span class="type">table</span> A list of the geometries that should map to the texture data. Supports the following fields:</dd>
</dl>
</li>
<li>
<dl>
<dt><code>vertices</code></dt>
<dd><span class="type">table</span> a list of the vertices in texture space of the geometry in the form {px0, py0, px1, py1, ..., pxn, pyn}</dd>
</dl>
</li>
<li>
<dl>
<dt><code>uvs</code></dt>
<dd><span class="type">table</span> a list of the uv coordinates in texture space of the geometry in the form of {u0, v0, u1, v1, ..., un, vn}</dd>
</dl>
</li>
<li>
<dl>
<dt><code>indices</code></dt>
<dd><span class="type">table</span> a list of the indices of the geometry in the form {i0, i1, i2, ..., in}. Each tripe in the list represents a triangle.</dd>
</dl>
</li>
</ul>

**Examples**

Add a new animation to an existing atlas
```
function init(self)
    local data = resource.get_atlas("/main/my_atlas.a.texturesetc")
    local my_animation = {
        id          = "my_new_animation",
        width       = 128,
        height      = 128,
        frame_start = 1,
        frame_end   = 6,
        playback    = go.PLAYBACK_LOOP_PINGPONG,
        fps         = 8
    }
    table.insert(data.animations, my_animation)
    resource.set_atlas("/main/my_atlas.a.texturesetc", data)
end
```Sets atlas data for a 256x256 texture with a single animation being rendered as a quad

```lua
function init(self)
    local params = {
        texture = "/main/my_256x256_texture.texturec",
        animations = {
            {
                id          = "my_animation",
                width       = 256,
                height      = 256,
                frame_start = 1,
                frame_end   = 2,
            }
        },
        geometries = {
            {
                vertices = {
                    0,   0,
                    0,   256,
                    256, 256,
                    256, 0
                },
                uvs = {
                    0, 0,
                    0, 256,
                    256, 256,
                    256, 0
                },
                indices = { 0,1,2,0,2,3 }
            }
        }
    }
    resource.set_atlas("/main/test.a.texturesetc", params)
end

```

### resource.set_buffer
*Type:* FUNCTION
Sets the buffer of a resource. By default, setting the resource buffer will either copy the data from the incoming buffer object
to the buffer stored in the destination resource, or make a new buffer object if the sizes between the source buffer and the destination buffer
stored in the resource differs. In some cases, e.g performance reasons, it might be beneficial to just set the buffer object on the resource without copying or cloning.
To achieve this, set the transfer_ownership flag to true in the argument table. Transferring ownership from a lua buffer to a resource with this function
works exactly the same as resource.create_buffer: the destination resource will take ownership of the buffer held by the lua reference, i.e the buffer will not automatically be removed
when the lua reference to the buffer is garbage collected.
Note: When setting a buffer with transfer_ownership = true, the currently bound buffer in the resource will be destroyed.

**Parameters**

- `path` (hash | string) - The path to the resource
- `buffer` (buffer) - The resource buffer
- `table` (table) (optional) - A table containing info about how to set the buffer. Supported entries:
<ul>
<li>
<dl>
<dt><code>transfer_ownership</code></dt>
<dd><span class="type">boolean</span> optional flag to determine wether or not the resource should take over ownership of the buffer object (default false)</dd>
</dl>
</li>
</ul>

**Examples**

How to set the data from a buffer
```
local function fill_stream(stream, verts)
    for key, value in ipairs(verts) do
        stream[key] = verts[key]
    end
end

function init(self)

    local res_path = go.get("#mesh", "vertices")

    local positions = {
         1, -1, 0,
         1,  1, 0,
         -1, -1, 0
    }

    local num_verts = #positions / 3

    -- create a new buffer
    local buf = buffer.create(num_verts, {
        { name = hash("position"), type=buffer.VALUE_TYPE_FLOAT32, count = 3 }
    })

    local buf = resource.get_buffer(res_path)
    local stream_positions = buffer.get_stream(buf, "position")

    fill_stream(stream_positions, positions)

    resource.set_buffer(res_path, buf)
end

```

### resource.set_sound
*Type:* FUNCTION
Update internal sound resource (wavc/oggc/opusc) with new data

**Parameters**

- `path` (hash | string) - The path to the resource
- `buffer` (string) - A lua string containing the binary sound data

### resource.set_texture
*Type:* FUNCTION
Sets the pixel data for a specific texture.

**Parameters**

- `path` (hash | string) - The path to the resource
- `table` (table) - A table containing info about the texture. Supported entries:
<dl>
<dt><code>type</code></dt>
<dd><span class="type">number</span> The texture type. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_TYPE_2D</code></li>
<li><code>graphics.TEXTURE_TYPE_IMAGE_2D</code></li>
<li><code>graphics.TEXTURE_TYPE_3D</code></li>
<li><code>graphics.TEXTURE_TYPE_IMAGE_3D</code></li>
<li><code>graphics.TEXTURE_TYPE_CUBE_MAP</code></li>
</ul>
<dl>
<dt><code>width</code></dt>
<dd><span class="type">number</span> The width of the texture (in pixels)</dd>
<dt><code>height</code></dt>
<dd><span class="type">number</span> The width of the texture (in pixels)</dd>
<dt><code>format</code></dt>
<dd><span class="type">number</span> The texture format, note that some of these formats are platform specific. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_FORMAT_LUMINANCE</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGB</code></li>
<li><code>graphics.TEXTURE_FORMAT_RGBA</code></li>
</ul>
These constants might not be available on the device:
- <code>graphics.TEXTURE_FORMAT_RGB_PVRTC_2BPPV1</code>
- <code>graphics.TEXTURE_FORMAT_RGB_PVRTC_4BPPV1</code>
- <code>graphics.TEXTURE_FORMAT_RGBA_PVRTC_2BPPV1</code>
- <code>graphics.TEXTURE_FORMAT_RGBA_PVRTC_4BPPV1</code>
- <code>graphics.TEXTURE_FORMAT_RGB_ETC1</code>
- <code>graphics.TEXTURE_FORMAT_RGBA_ETC2</code>
- <code>graphics.TEXTURE_FORMAT_RGBA_ASTC_4X4</code>
- <code>graphics.TEXTURE_FORMAT_RGB_BC1</code>
- <code>graphics.TEXTURE_FORMAT_RGBA_BC3</code>
- <code>graphics.TEXTURE_FORMAT_R_BC4</code>
- <code>graphics.TEXTURE_FORMAT_RG_BC5</code>
- <code>graphics.TEXTURE_FORMAT_RGBA_BC7</code>
- <code>graphics.TEXTURE_FORMAT_RGB16F</code>
- <code>graphics.TEXTURE_FORMAT_RGB32F</code>
- <code>graphics.TEXTURE_FORMAT_RGBA16F</code>
- <code>graphics.TEXTURE_FORMAT_RGBA32F</code>
- <code>graphics.TEXTURE_FORMAT_R16F</code>
- <code>graphics.TEXTURE_FORMAT_RG16F</code>
- <code>graphics.TEXTURE_FORMAT_R32F</code>
- <code>graphics.TEXTURE_FORMAT_RG32F</code>
You can test if the device supports these values by checking if a specific enum is nil or not:
<div class="codehilite"><pre><span></span><code><span class="kr">if</span> <span class="n">graphics</span><span class="p">.</span><span class="n">TEXTURE_FORMAT_RGBA16F</span> <span class="o">~=</span> <span class="kc">nil</span> <span class="kr">then</span>
    <span class="c1">-- it is safe to use this format</span>
<span class="kr">end</span>
</code></pre></div>

<dl>
<dt><code>x</code></dt>
<dd><span class="type">number</span> optional x offset of the texture (in pixels)</dd>
<dt><code>y</code></dt>
<dd><span class="type">number</span> optional y offset of the texture (in pixels)</dd>
<dt><code>z</code></dt>
<dd><span class="type">number</span> optional z offset of the texture (in pixels). Only applies to 3D textures</dd>
<dt><code>page</code></dt>
<dd><span class="type">number</span> optional slice of the array texture. Only applies to 2D texture arrays. Zero-based</dd>
<dt><code>mipmap</code></dt>
<dd><span class="type">number</span> optional mipmap to upload the data to</dd>
<dt><code>compression_type</code></dt>
<dd><span class="type">number</span> optional specify the compression type for the data in the buffer object that holds the texture data. Defaults to graphics.COMPRESSION_TYPE_DEFAULT, i.e no compression. Supported values:</dd>
</dl>
<ul>
<li><code>COMPRESSION_TYPE_DEFAULT</code></li>
<li><code>COMPRESSION_TYPE_BASIS_UASTC</code></li>
</ul>
- `buffer` (buffer) - The buffer of precreated pixel data
<span class="icon-attention"></span> To update a cube map texture you need to pass in six times the amount of data via the buffer, since a cube map has six sides!
<span class="icon-attention"></span> 3D Textures are currently only supported on OpenGL and Vulkan adapters. To check if your device supports 3D textures, use:
```lua
if graphics.TEXTURE_TYPE_3D ~= nil then
    -- Device and graphics adapter support 3D textures
end

**Examples**

How to set all pixels of an atlas
```
function init(self)
  self.height = 128
  self.width = 128
  self.buffer = buffer.create(self.width * self.height, { {name=hash("rgb"), type=buffer.VALUE_TYPE_UINT8, count=3} } )
  self.stream = buffer.get_stream(self.buffer, hash("rgb"))

  for y=1,self.height do
      for x=1,self.width do
          local index = (y-1) * self.width * 3 + (x-1) * 3 + 1
          self.stream[index + 0] = 0xff
          self.stream[index + 1] = 0x80
          self.stream[index + 2] = 0x10
      end
  end

  local resource_path = go.get("#model", "texture0")
  local args = { width=self.width, height=self.height, type=graphics.TEXTURE_TYPE_2D, format=graphics.TEXTURE_FORMAT_RGB, num_mip_maps=1 }
  resource.set_texture( resource_path, args, self.buffer )
end
```How to update a specific region of an atlas by using the x,y values. Assumes the already set atlas is a 128x128 texture.

```lua
function init(self)
  self.x = 16
  self.y = 16
  self.height = 128 - self.x * 2
  self.width = 128 - self.y * 2
  self.buffer = buffer.create(self.width * self.height, { {name=hash("rgb"), type=buffer.VALUE_TYPE_UINT8, count=3} } )
  self.stream = buffer.get_stream(self.buffer, hash("rgb"))

  for y=1,self.height do
      for x=1,self.width do
          local index = (y-1) * self.width * 3 + (x-1) * 3 + 1
          self.stream[index + 0] = 0xff
          self.stream[index + 1] = 0x80
          self.stream[index + 2] = 0x10
      end
  end

  local resource_path = go.get("#model", "texture0")
  local args = { width=self.width, height=self.height, x=self.x, y=self.y, type=graphics.TEXTURE_TYPE_2D, format=graphics.TEXTURE_FORMAT_RGB, num_mip_maps=1 }
  resource.set_texture(resource_path, args, self.buffer )
end
```Update a texture from a buffer resource
```lua
go.property("my_buffer", resource.buffer("/my_default_buffer.buffer"))

function init(self)
    local resource_path = go.get("#model", "texture0")
    -- the "my_buffer" resource is expected to hold 128 * 128 * 3 bytes!
    local args = {
         width  = 128,
         height = 128,
         type   = graphics.TEXTURE_TYPE_2D,
         format = graphics.TEXTURE_FORMAT_RGB
     }
    -- Note that the extra resource.get_buffer call is a requirement here
    -- since the "self.my_buffer" is just pointing to a buffer resource path
    -- and not an actual buffer object or buffer resource.
    resource.set_texture(resource_path, args, resource.get_buffer(self.my_buffer))
end
```Update an existing 3D texture from a lua buffer

```lua

function init(self)
    -- create a buffer that can hold the data of a 8x8x8 texture
    local tbuffer = buffer.create(8 * 8 * 8, { {name=hash("rgba"), type=buffer.VALUE_TYPE_FLOAT32, count=4} } )
    local tstream = buffer.get_stream(tbuffer, hash("rgba"))

    -- populate the buffer with some data
    local index = 1
    for z=1,8 do
        for y=1,8 do
            for x=1,8 do
                tstream[index + 0] = x
                tstream[index + 1] = y
                tstream[index + 2] = z
                tstream[index + 3] = 1.0
                index = index + 4
            end
        end
    end

    local t_args = {
        type   = graphics.TEXTURE_TYPE_IMAGE_3D,
        width  = 8,
        height = 8,
        depth  = 8,
        format = resource.TEXTURE_FORMAT_RGBA32F
    }

    -- This expects that the texture resource "/my_3d_texture.texturec" already exists
    -- and is a 3D texture resource. To create a dynamic 3D texture resource
    -- use the "resource.create_texture" function.
    resource.set_texture("/my_3d_texture.texturec", t_args, tbuffer)
endUpdate texture 2nd array page with loaded texture from png

```lua
    -- new_tex is resource handle of texture which was created via resource.create_resource
    local tex_path = "/bundle_resources/page_02.png"
    local data = sys.load_resource(tex_path)
    local buf = image.load_buffer(data)
    resource.set_texture(new_tex, {
        type = graphics.TEXTURE_TYPE_2D_ARRAY,
        width = buf.width,
        height = buf.height,
        page = 1,
        format = graphics.TEXTURE_FORMAT_RGB
    }, buf.buffer)
    go.set("#mesh", "texture0", new_tex)

```

### resource.texture
*Type:* FUNCTION
Constructor-like function with two purposes:

Load the specified resource as part of loading the script
Return a hash to the run-time version of the resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `path` (hash) - a path hash to the binary version of the resource

**Examples**

Load a texture and set it to a model:
```
go.property("my_texture", resource.texture("/texture.png"))
function init(self)
  go.set("#model", "texture0", self.my_texture)
end

```

### resource.tile_source
*Type:* FUNCTION
Constructor-like function with two purposes:

Load the specified resource as part of loading the script
Return a hash to the run-time version of the resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `path` (hash) - a path hash to the binary version of the resource

**Examples**

Load tile source and set it to a tile map:
```
go.property("my_tile_source", resource.tile_source("/tilesource.tilesource"))
function init(self)
  go.set("#tilemap", "tile_source", self.my_tile_source)
end

```
