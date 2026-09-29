# Image

**Namespace:** `image`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_image.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_image.cpp`

Functions for creating image objects.

## API

### image.astc_header
*Type:* STRUCT
ASTC image header

**Members**

- `width` (integer) - Image width.
- `height` (integer) - Image height.
- `depth` (integer) - Image depth.
- `block_size_x` (integer) - Block size on the x-axis.
- `block_size_y` (integer) - Block size on the y-axis.
- `block_size_z` (integer) - Block size on the z-axis.

### image.get_astc_header
*Type:* FUNCTION
get the header of an .astc buffer

**Parameters**

- `buffer` (string) - .astc file data buffer

**Returns**

- `header` (image.astc_header | nil) - header, or <code>nil</code> if the buffer is not a valid ASTC image

**Examples**

How to get the block size and dimensions from a .astc file
```
local s = sys.load_resource("/assets/cat.astc")
local header = image.get_astc_header(s)
pprint(s)

```

### image.load
*Type:* FUNCTION
Load image (PNG or JPEG) from buffer.

**Parameters**

- `buffer` (string) - image data buffer
- `options` (boolean | image.load_options) (optional) - Optional loading parameters. A boolean is accepted for backwards compatibility and controls <code>premultiply_alpha</code>.

**Returns**

- `image` (image.load_result | nil) - loaded image, or <code>nil</code> if loading fails

**Examples**

How to load an image from an URL and create a GUI texture from it:
```
local imgurl = "http://www.site.com/image.png"
http.request(imgurl, "GET", function(self, id, response)
        local img = image.load(response.response)
        local tx = gui.new_texture("image_node", img.width, img.height, img.type, img.buffer)
    end)

```

### image.load_buffer
*Type:* FUNCTION
Load image (PNG or JPEG) from a string buffer.

**Parameters**

- `buffer` (string) - image data buffer
- `options` (boolean | image.load_options) (optional) - Optional loading parameters. A boolean is accepted for backwards compatibility and controls <code>premultiply_alpha</code>.

**Returns**

- `image` (image.load_buffer_result | nil) - loaded image, or <code>nil</code> if loading fails

**Examples**

Load an image from an URL as a buffer and create a texture resource from it:
```
local imgurl = "http://www.site.com/image.png"
http.request(imgurl, "GET", function(self, id, response)
        local img = image.load_buffer(response.response, { flip_vertically = true })
        local tparams = {
            width  = img.width,
            height = img.height,
            type   = graphics.TEXTURE_TYPE_2D,
            format = graphics.TEXTURE_FORMAT_RGBA }

        local my_texture_id = resource.create_texture("/my_custom_texture.texturec", tparams, img.buffer)
        -- Apply the texture to a model
        go.set("/go1#model", "texture0", my_texture_id)
    end)

```

### image.load_buffer_result
*Type:* STRUCT
Loaded buffer image data

**Members**

- `width` (integer) - Image width.
- `height` (integer) - Image height.
- `type` (image.TYPE) - Image type.
- `buffer` (buffer_data) - Script buffer containing the decompressed image data.

### image.load_options
*Type:* STRUCT
Image loading options

**Members**

- `premultiply_alpha?` (boolean) - Whether to premultiply alpha into the color components. Defaults to <code>false</code>.
- `flip_vertically?` (boolean) - Whether to flip the image contents vertically. Defaults to <code>false</code>.

### image.load_result
*Type:* STRUCT
Loaded string image data

**Members**

- `width` (integer) - Image width.
- `height` (integer) - Image height.
- `type` (image.TYPE) - Image type.
- `buffer` (string) - Raw image data.

### image.TYPE
*Type:* ENUM
Image types

**Parameters**

- `value` (string) - image type

**Members**

- `image.TYPE_RGB` - RGB image type.
- `image.TYPE_RGBA` - RGBA image type.
- `image.TYPE_LUMINANCE` - Luminance image type.
- `image.TYPE_LUMINANCE_ALPHA` - Luminance-alpha image type.
