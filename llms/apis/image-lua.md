# Image

**Namespace:** `image`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_image.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_image.cpp`

Functions for creating image objects.

## API

### image.get_astc_header
*Type:* FUNCTION
get the header of an .astc buffer

**Parameters**

- `buffer` (string) - .astc file data buffer

**Returns**

- `table` (table | nil) - header or <code>nil</code> if buffer is not a valid .astc. The header has these fields:
<ul>
<li><span class="type">number</span> <code>width</code>: image width</li>
<li><span class="type">number</span> <code>height</code>: image height</li>
<li><span class="type">number</span> <code>depth</code>: image depth</li>
<li><span class="type">number</span> <code>block_size_x</code>: block size x</li>
<li><span class="type">number</span> <code>block_size_y</code>: block size y</li>
<li><span class="type">number</span> <code>block_size_z</code>: block size z</li>
</ul>

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
- `options` (table) (optional) - An optional table containing parameters for loading the image. Supported entries:
<dl>
<dt><code>premultiply_alpha</code></dt>
<dd><span class="type">boolean</span> True if alpha should be premultiplied into the color components. Defaults to <code>false</code>.</dd>
<dt><code>flip_vertically</code></dt>
<dd><span class="type">boolean</span> True if the image contents should be flipped vertically. Defaults to <code>false</code>.</dd>
</dl>

**Returns**

- `image` (table | nil) - object or <code>nil</code> if loading fails. The object is a table with the following fields:
<ul>
<li><span class="type">number</span> <code>width</code>: image width</li>
<li><span class="type">number</span> <code>height</code>: image height</li>
<li><span class="type">constant</span> <code>type</code>: image type<ul>
<li><code>image.TYPE_RGB</code></li>
<li><code>image.TYPE_RGBA</code></li>
<li><code>image.TYPE_LUMINANCE</code></li>
<li><code>image.TYPE_LUMINANCE_ALPHA</code></li>
</ul>
</li>
<li><span class="type">string</span> <code>buffer</code>: the raw image data</li>
</ul>

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
- `options` (table) (optional) - An optional table containing parameters for loading the image. Supported entries:
<dl>
<dt><code>premultiply_alpha</code></dt>
<dd><span class="type">boolean</span> True if alpha should be premultiplied into the color components. Defaults to <code>false</code>.</dd>
<dt><code>flip_vertically</code></dt>
<dd><span class="type">boolean</span> True if the image contents should be flipped vertically. Defaults to <code>false</code>.</dd>
</dl>

**Returns**

- `image` (table | nil) - object or <code>nil</code> if loading fails. The object is a table with the following fields:
<ul>
<li><span class="type">number</span> <code>width</code>: image width</li>
<li><span class="type">number</span> <code>height</code>: image height</li>
<li><span class="type">constant</span> <code>type</code>: image type<ul>
<li><code>image.TYPE_RGB</code></li>
<li><code>image.TYPE_RGBA</code></li>
<li><code>image.TYPE_LUMINANCE</code></li>
<li><code>image.TYPE_LUMINANCE_ALPHA</code></li>
</ul>
</li>
<li><span class="type">buffer</span> <code>buffer</code>: the script buffer that holds the decompressed image data. See <a href="/ref/buffer#buffer.create">buffer.create</a> how to use the buffer.</li>
</ul>

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

### image.TYPE_LUMINANCE
*Type:* CONSTANT
luminance image type

### image.TYPE_LUMINANCE_ALPHA
*Type:* CONSTANT
luminance image type

### image.TYPE_RGB
*Type:* CONSTANT
RGB image type

### image.TYPE_RGBA
*Type:* CONSTANT
RGBA image type
