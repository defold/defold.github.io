# Resource

**Namespace:** `resource`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_resource.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_resource.cpp`

Functions and constants to access resources.

## API

### resource.animation
*Type:* STRUCT
Animation data accepted when creating or updating an atlas. Specify either
frames, or both frame_start and frame_end.

**Members**

- `id` (string) - Animation id.
- `width` (integer) - Animation width.
- `height` (integer) - Animation height.
- `frames?` (integer[]) - Geometry indices for the animation frames.
- `frame_start?` (integer) - First geometry index for the legacy contiguous frame range.
- `frame_end?` (integer) - Non-inclusive last geometry index for the legacy contiguous frame range.
- `playback?` (go.PLAYBACK) - Playback mode. The default is <code>go.PLAYBACK_ONCE_FORWARD</code>.
- `fps?` (integer) - Animation frame rate. The default is 30.
- `flip_vertical?` (boolean) - Whether to flip the animation vertically. The default is false.
- `flip_horizontal?` (boolean) - Whether to flip the animation horizontally. The default is false.

### resource.animation_data
*Type:* STRUCT
Animation data returned by resource.get_atlas.

**Members**

- `id` (string) - Animation id.
- `width` (integer) - Animation width.
- `height` (integer) - Animation height.
- `frames` (integer[]) - Geometry indices for the animation frames.
- `playback` (go.PLAYBACK) - Playback mode.
- `fps` (integer) - Animation frame rate.
- `flip_vertical` (boolean) - Whether the animation is flipped vertically.
- `flip_horizontal` (boolean) - Whether the animation is flipped horizontally.

### resource.atlas
*Type:* STRUCT
Data accepted by resource.create_atlas and resource.set_atlas.

**Members**

- `texture` (string|hash) - Path to the texture resource, for example <code>"/main/my_texture.texturec"</code>.
- `animations` (resource.animation[]) - Animations in the atlas.
- `geometries` (resource.geometry[]) - Geometries that map to the texture data.

### resource.atlas
*Type:* FUNCTION
Constructor-like function with two purposes:

Load the specified resource as part of loading the script
Create a resource reference that resolves to the hashed path of the run-time resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `resource` (resource_data) - a reference to the binary version of the resource

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

### resource.atlas_data
*Type:* STRUCT
Data returned by resource.get_atlas.

**Members**

- `texture` (string|hash) - Path to the texture resource.
- `animations` (resource.animation_data[]) - Animations in the atlas.
- `geometries` (resource.geometry_data[]) - Geometries that map to the texture data.

### resource.buffer
*Type:* FUNCTION
Constructor-like function with two purposes:

Load the specified resource as part of loading the script
Create a resource reference that resolves to the hashed path of the run-time resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `resource` (resource_data) - a reference to the binary version of the resource

**Examples**

Set a unique buffer it to a sprite:
```
go.property("my_buffer", resource.buffer("/cube.buffer"))
function init(self)
  go.set("#mesh", "vertices", self.my_buffer)
end

```

### resource.buffer_creation_params
*Type:* STRUCT
Buffer-resource creation parameters

**Members**

- `buffer` (buffer_data) - Buffer to bind to the resource.
- `transfer_ownership?` (boolean) - Whether the resource takes ownership of the buffer. The default is true.

### resource.buffer_update_options
*Type:* STRUCT
Buffer-resource update options

**Members**

- `transfer_ownership?` (boolean) - Whether the resource takes ownership of the buffer. The default is false.

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

**Parameters**

- `path` (string) - The path to the resource.
- `table` (resource.atlas) - atlas creation data

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
                frames      = { 1 }
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
- `table` (resource.buffer_creation_params) - buffer-resource creation parameters

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

```

Create a buffer resource from existing resource
```
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
- `options` (resource.sound_data_options) (optional) - optional sound-data parameters

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
- `table` (resource.texture_creation_params) - texture creation parameters
- `buffer` (buffer_data) (optional) - optional buffer of precreated pixel data

**Returns**

- `path` (hash) - The path to the resource.

**Examples**

Check whether a texture format is supported by the device:
```
if graphics.TEXTURE_FORMAT_RGBA16F ~= nil then
    -- It is safe to use this format.
end

```

 3D textures are currently only supported on OpenGL and Vulkan adapters. Check whether the device supports 3D textures before using them:
```
if graphics.TEXTURE_TYPE_3D ~= nil then
    -- The device and graphics adapter support 3D textures.
end

```

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

```

How to create an 128x128 floating point texture (RGBA32F) resource from a buffer object
```
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

```

How to create a 32x32x32 floating point 3D texture that can be used to generate volumetric data in a compute shader
```
function init(self)
    local t_volume = resource.create_texture("/my_backing_texture.texturec", {
        type   = graphics.TEXTURE_TYPE_IMAGE_3D,
        width  = 32,
        height = 32,
        depth  = 32,
        format = graphics.TEXTURE_FORMAT_RGBA32F,
        flags  = graphics.TEXTURE_USAGE_FLAG_STORAGE + graphics.TEXTURE_USAGE_FLAG_SAMPLE,
    })

    -- pass the backing texture to the render script
    msg.post("@render:", "add_textures", { t_volume })
end

```

How to create 512x512 texture array with 5 pages.
```
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

- `path` (string) - The path to the resource.
- `table` (resource.texture_creation_params) - texture creation parameters
- `buffer` (buffer_data) (optional) - optional buffer of precreated pixel data
- `callback` (fun(self:script_instance, request_id:integer, result:resource.texture_creation_result)) (optional) - callback function invoked when the texture is created

**Returns**

- `path` (hash) - The path to the texture resource.
- `request_id` (integer) - The request id for the async request.

**Examples**

Check whether a texture format is supported by the device:
```
if graphics.TEXTURE_FORMAT_RGBA16F ~= nil then
    -- It is safe to use this format.
end

```

 3D textures are currently only supported on OpenGL and Vulkan adapters. Check whether the device supports 3D textures before using them:
```
if graphics.TEXTURE_TYPE_3D ~= nil then
    -- The device and graphics adapter support 3D textures.
end

```

Create a texture resource asyncronously with a buffer and a callback
```
function callback(self, request_id, result)
    -- The resource has been updated with a new texture,
    -- so we can update other systems with the new handle,
    -- or update components to use the resource if we want
    local tinfo = resource.get_texture_info(result.path)
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

```

Create a texture resource asyncronously without a callback
```
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
Create a resource reference that resolves to the hashed path of the run-time resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `resource` (resource_data) - a reference to the binary version of the resource

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

### resource.geometry
*Type:* STRUCT
Geometry data accepted when creating or updating an atlas. Vertex, UV, and
index values are zero-based.

**Members**

- `id?` (string) - Geometry name, used when matching animations between atlases.
- `width?` (number) - Width of the image represented by the geometry. If omitted, it is calculated from the vertices.
- `height?` (number) - Height of the image represented by the geometry. If omitted, it is calculated from the vertices.
- `pivot_x?` (number) - Horizontal pivot in unit coordinates. The default is 0.5.
- `pivot_y?` (number) - Vertical pivot in unit coordinates. The default is 0.5.
- `rotated?` (boolean) - Whether the image is rotated 90 degrees counter-clockwise in the atlas.
- `vertices` (number[]) - Vertex coordinates in image space as <code>{px0, py0, px1, py1, ...}</code>.
- `uvs` (number[]) - UV coordinates in image space as <code>{u0, v0, u1, v1, ...}</code>.
- `indices` (integer[]) - Geometry indices where each group of three entries represents a triangle.

### resource.geometry_data
*Type:* STRUCT
Geometry data returned by resource.get_atlas.

**Members**

- `width` (number) - Width of the image represented by the geometry.
- `height` (number) - Height of the image represented by the geometry.
- `pivot_x` (number) - Horizontal pivot in unit coordinates.
- `pivot_y` (number) - Vertical pivot in unit coordinates.
- `rotated` (boolean) - Whether the image is rotated 90 degrees counter-clockwise in the atlas.
- `vertices` (number[]) - Vertex coordinates in image space as <code>{px0, py0, px1, py1, ...}</code>.
- `uvs` (number[]) - UV coordinates in image space as <code>{u0, v0, u1, v1, ...}</code>.
- `indices` (integer[]) - Geometry indices where each group of three entries represents a triangle.

### resource.get_atlas
*Type:* FUNCTION
Returns the atlas data for an atlas

**Parameters**

- `path` (hash | string) - The path to the atlas resource

**Returns**

- `data` (resource.atlas_data) - atlas data

### resource.get_buffer
*Type:* FUNCTION
gets the buffer from a resource

**Parameters**

- `path` (hash | string) - The path to the resource

**Returns**

- `buffer` (buffer_data) - The resource buffer

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

- `path` (hash | string | render_target) - The path to the resource or a render target handle

**Returns**

- `table` (resource.render_target_info) - render-target information

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

```

Get a texture attachment from a render target and set it on a model component
```
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
Gets the text metrics from a font. Rich text markup is measured using its
visible text and font sizes. If markup cannot be parsed, the text is measured literally.
Inline sprites reserve their specified dimensions, or one em by default.

**Parameters**

- `url` (hash) - the font to get the (unscaled) metrics from
- `text` (string) - text to measure
- `options` (resource.text_metrics_options) (optional) - optional text-metric options

**Returns**

- `metrics` (resource.text_metrics) - measured text metrics

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

- `path` (hash | string | texture) - The path to the resource or a texture handle

**Returns**

- `table` (resource.texture_info) - texture information

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

```

Get the meta data from an atlas resource
```
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

- `buffer` (buffer_data) - Returns the buffer stored on disc

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
Create a resource reference that resolves to the hashed path of the run-time resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `resource` (resource_data) - a reference to the binary version of the resource

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
Create a resource reference that resolves to the hashed path of the run-time resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `resource` (resource_data) - a reference to the binary version of the resource

**Examples**

Set a render target color attachment as a model texture:
```
go.property("my_render_target", resource.render_target("/rt.render_target"))
function init(self)
  local rt_info = resource.get_render_target_info(self.my_render_target)
  go.set("#model", "texture0", rt_info.attachments[1].texture)
end

```

### resource.render_target_attachment_info
*Type:* STRUCT
Render target attachment information

**Members**

- `handle` (texture) - Opaque texture handle.
- `width` (integer) - Texture width.
- `height` (integer) - Texture height.
- `depth` (integer) - Texture depth or layer count.
- `page_count` (integer) - Texture page count.
- `mipmaps` (integer) - Number of mipmaps.
- `flags` (graphics.TEXTURE_USAGE_FLAG) - Texture usage flags.
- `type` (graphics.TEXTURE_TYPE) - Texture type.
- `buffer_type` (graphics.BUFFER_TYPE) - Render-target buffer type.
- `texture?` (hash) - Backing texture resource, when present.

### resource.render_target_info
*Type:* STRUCT
Render target information

**Members**

- `handle` (render_target) - Opaque render-target handle.
- `sample_count` (integer) - Effective sample count shared by all render-target attachments.
- `attachments` (resource.render_target_attachment_info[]) - Render-target attachments.

### resource.set
*Type:* FUNCTION
Sets the resource data for a specific resource

**Parameters**

- `path` (string | hash) - The path to the resource
- `buffer` (buffer_data) - The buffer of precreated data, suitable for the intended resource type

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

**Parameters**

- `path` (hash | string) - The path to the atlas resource
- `table` (resource.atlas) - atlas data

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

```

Sets atlas data for a 256x256 texture with a single animation being rendered as a quad
```
function init(self)
    local params = {
        texture = "/main/my_256x256_texture.texturec",
        animations = {
            {
                id          = "my_animation",
                width       = 256,
                height      = 256,
                frames      = { 1 }
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
- `buffer` (buffer_data) - The resource buffer
- `table` (resource.buffer_update_options) (optional) - optional buffer-resource update options

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
- `table` (resource.texture_update_params) - texture update parameters
- `buffer` (buffer_data) - The buffer of precreated pixel data
<span class="icon-attention"></span> To update a cube map texture you need to pass in six times the amount of data via the buffer, since a cube map has six sides!
<span class="icon-attention"></span> 3D textures are currently only supported on OpenGL and Vulkan adapters.

**Examples**

Check whether a texture format is supported by the device:
```
if graphics.TEXTURE_FORMAT_RGBA16F ~= nil then
    -- It is safe to use this format.
end

```

Check whether the device supports 3D textures before using them:
```
if graphics.TEXTURE_TYPE_3D ~= nil then
    -- The device and graphics adapter support 3D textures.
end

```

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

```

How to update a specific region of an atlas by using the x,y values. Assumes the already set atlas is a 128x128 texture.
```
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

```

Update a texture from a buffer resource
```
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

```

Update an existing 3D texture from a lua buffer
```
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
        format = graphics.TEXTURE_FORMAT_RGBA32F
    }

    -- This expects that the texture resource "/my_3d_texture.texturec" already exists
    -- and is a 3D texture resource. To create a dynamic 3D texture resource
    -- use the "resource.create_texture" function.
    resource.set_texture("/my_3d_texture.texturec", t_args, tbuffer)
end

```

Update texture 2nd array page with loaded texture from png
```
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

### resource.sound_data_options
*Type:* STRUCT
Sound-data creation options

**Members**

- `data?` (string) - Raw sound file data, including the file header.
- `filesize?` (number) - Complete file size when <code>data</code> is partial.
- `partial?` (boolean) - Whether <code>data</code> contains only the initial file chunk.

### resource.text_metrics
*Type:* STRUCT
Text metrics

**Members**

- `width` (number) - Text width.
- `height` (number) - Text height.
- `max_ascent` (number) - Maximum ascent.
- `max_descent` (number) - Maximum descent.

### resource.text_metrics_options
*Type:* STRUCT
Text metric options

**Members**

- `width?` (number) - Text-field width; unused when <code>line_break</code> is false.
- `leading?` (number) - Line leading. The default is 1.
- `tracking?` (number) - Character tracking. The default is 0.
- `line_break?` (boolean) - Whether to account for line breaks. The default is false.

### resource.texture
*Type:* FUNCTION
Constructor-like function with two purposes:

Load the specified resource as part of loading the script
Create a resource reference that resolves to the hashed path of the run-time resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `resource` (resource_data) - a reference to the binary version of the resource

**Examples**

Load a texture and set it to a model:
```
go.property("my_texture", resource.texture("/texture.png"))
function init(self)
  go.set("#model", "texture0", self.my_texture)
end

```

### resource.texture_creation_params
*Type:* STRUCT
Texture creation parameters

**Members**

- `type` (graphics.TEXTURE_TYPE) - Texture type.
- `width` (integer) - Texture width in pixels; must be greater than zero.
- `height` (integer) - Texture height in pixels; must be greater than zero.
- `depth?` (integer) - Texture depth; used by 3D texture types and must be greater than zero.
- `page_count?` (integer) - Number of pages for a 2D array texture.
- `format` (graphics.TEXTURE_FORMAT) - Texture format. Device-specific unsupported constants evaluate to <code>nil</code>.
- `flags?` (graphics.TEXTURE_USAGE_FLAG) - Creation-usage hints. The default is <a href="/ref/graphics#graphics.TEXTURE_USAGE_FLAG_SAMPLE">graphics.TEXTURE_USAGE_FLAG_SAMPLE</a>.
- `max_mipmaps?` (integer) - Maximum mipmap count. The default is zero.
- `compression_type?` (graphics.COMPRESSION_TYPE) - Compression used by the supplied buffer. The default is <a href="/ref/graphics#graphics.COMPRESSION_TYPE_DEFAULT">graphics.COMPRESSION_TYPE_DEFAULT</a>.

### resource.texture_creation_result
*Type:* STRUCT
Asynchronous texture creation result

**Members**

- `path` (hash) - Created texture resource path.

### resource.texture_info
*Type:* STRUCT
Texture information

**Members**

- `handle` (texture) - Opaque texture handle.
- `width` (integer) - Texture width.
- `height` (integer) - Texture height.
- `depth` (integer) - Texture depth or layer count.
- `page_count` (integer) - Texture page count.
- `mipmaps` (integer) - Number of mipmaps.
- `flags` (graphics.TEXTURE_USAGE_FLAG) - Texture usage flags.
- `type` (graphics.TEXTURE_TYPE) - Texture type.

### resource.texture_update_params
*Type:* STRUCT
Texture update parameters

**Members**

- `type` (graphics.TEXTURE_TYPE) - Texture type.
- `width` (integer) - Update width in pixels.
- `height` (integer) - Update height in pixels.
- `depth?` (integer) - Update depth for a 3D texture.
- `format` (graphics.TEXTURE_FORMAT) - Texture format. Device-specific unsupported constants evaluate to <code>nil</code>.
- `x?` (integer) - X offset in pixels.
- `y?` (integer) - Y offset in pixels.
- `z?` (integer) - Z offset for a 3D texture.
- `page?` (integer) - Zero-based page of a 2D array texture.
- `mipmap?` (integer) - Mipmap level to update.
- `compression_type?` (graphics.COMPRESSION_TYPE) - Compression used by the supplied buffer. The default is <a href="/ref/graphics#graphics.COMPRESSION_TYPE_DEFAULT">graphics.COMPRESSION_TYPE_DEFAULT</a>.

### resource.tile_source
*Type:* FUNCTION
Constructor-like function with two purposes:

Load the specified resource as part of loading the script
Create a resource reference that resolves to the hashed path of the run-time resource

 This function can only be called within go.property function calls.

**Parameters**

- `path` (string) (optional) - optional resource path string to the resource

**Returns**

- `resource` (resource_data) - a reference to the binary version of the resource

**Examples**

Load tile source and set it to a tile map:
```
go.property("my_tile_source", resource.tile_source("/tilesource.tilesource"))
function init(self)
  go.set("#tilemap", "tile_source", self.my_tile_source)
end

```

### resource_data
*Type:* TYPEDEF
An opaque declaration-time reference to a Defold resource. Resource references
are created by functions such as resource.atlas, resource.font, and
resource.material. They can only be used as default values passed to
go.property.
The referenced resource is loaded together with the script. At runtime, the
property contains the hashed path of the compiled resource.

**Parameters**

- `value` (userdata) - script property resource reference

**Examples**

```
go.property("player_atlas", resource.atlas("/main/player.atlas"))

function init(self)
    go.set("#sprite", "image", self.player_atlas)
end

```
