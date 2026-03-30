# Font Resource

**Namespace:** `dmGameSystem`
**Language:** C++
**Type:** Defold C++
**File:** `res_font.h`
**Source:** `engine/gamesys/src/dmsdk/gamesys/resources/res_font.h`
**Include:** `dmsdk/gamesys/resources/res_font.h`

Font resource functions.

## API

### FontInfo
*Type:* STRUCT
Used to retrieve the information of a font.

**Members**

- `m_Size` (uint32_t) - The size of the font (in points)
- `m_ShadowX` (float) - The shadow distance in X-axis (in pixels)
- `m_ShadowY` (float) - The shadow distance in Y-axis (in pixels)
- `m_ShadowBlur` (uint32_t) - The shadow blur spread [0.255] (in pixels)
- `m_ShadowAlpha` (float) - The shadow alpha value [0..255]
- `m_Alpha` (float) - The alpha value [0..255]
- `m_OutlineAlpha` (float) - The outline alpha value [0..255]
- `m_OutlineWidth` (float) - The outline size (in pixels)
- `m_OutputFormat` (dmRenderDDF::FontTextureFormat) - The type of font (bitmap or distance field)
- `m_RenderMode` (dmRenderDDF::FontRenderMode) - Single or multi channel

### FontResource
*Type:* STRUCT
Handle to font resource

### FPrewarmTextCallback
*Type:* TYPEDEF

**Parameters**

- `ctx` (void*) - The callback context
- `result` (int) - The result of the prewarming. Non zero if successful
- `errmsg` (const char*) - An error message if not successful.

### PrewarmText
*Type:* FUNCTION
Make sure each glyph in the text gets rasterized and put into the glyph cache

**Parameters**

- `font` (FontResource*) - The font resource
- `text` (const char*) - The text (utf8)
- `cbk` (FPrewarmTextCallback) - The callback is called when the last item is done
- `cbk_ctx` (void*) - The callback context

**Returns**

- `result` (dmResource::Result) - RESULT_OK if successful

### ResFontAddFontByPath
*Type:* FUNCTION
add a ttf font to a font collection

**Notes**

- Loads the resource if not already loaded

**Parameters**

- `factory` (dmResource::HFactory) - The factory
- `font` (FontResource*) - The font collection (.fontc)
- `ttf_path` (const char*) - The .ttf path

**Returns**

- `result` (dmResource::Result) - RESULT_OK if successful

### ResFontAddFontByPathHash
*Type:* FUNCTION
add a ttf font to a font collection

**Notes**

- the ttf resource must already be loaded

**Parameters**

- `factory` (dmResource::HFactory) - The factory
- `font` (FontResource*) - The font collection (.fontc)
- `ttf_hash` (dmhash_t) - The ttf path hash (.ttf)

**Returns**

- `result` (dmResource::Result) - RESULT_OK if successful

### ResFontAddGlyph
*Type:* FUNCTION

**Parameters**

- `font` (FontResource*) - The font resource
- `hfont` (HFont) - The font the glyph was created from
- `glyph_index` (uint32_t) - The glyph index

**Returns**

- `result` (bool) - true if the glyph already has rasterized bitmap data

### ResFontAddGlyph
*Type:* FUNCTION

**Parameters**

- `font` (FontResource*) - The font resource
- `hfont` (HFont) - The font the glyph was created from
- `glyph` (FontGlyph*) - The glyph

**Returns**

- `result` (dmResource::Result) - RESULT_OK if successful

### ResFontGetFontCollection
*Type:* FUNCTION

**Parameters**

- `resource` (FontResource*) - The font resource

**Returns**

- `font_collection` (HFontCollection*) - The font collection if successful. 0 otherwise.

### ResFontGetHandle
*Type:* FUNCTION

**Parameters**

- `font` (FontResource*) - The font resource

**Returns**

- `result` (dmRender::HFontMap) - Handle to a font if successful. 0 otherwise.

### ResFontGetInfo
*Type:* FUNCTION

**Parameters**

- `font` (FontResource*) - The font resource to query
- `info` (FontInfo*) - The output info (out)

**Returns**

- `result` (dmResource::Result) - RESULT_OK if successful

### ResFontGetPathHashFromFont
*Type:* FUNCTION

**Parameters**

- `resource` (FontResource*) - The font resource
- `font` (HFont) - The font

**Returns**

- `path_hash` (dmhash_t) - The path hash to the associated TTFresource*

### ResFontGetTTFResourceFromFont
*Type:* FUNCTION

**Parameters**

- `resource` (FontResource*) - The font resource
- `font` (HFont) - The font

**Returns**

- `ttfresource` (TTFResource*) - The ttfresource if successful. 0 otherwise.

### ResFontRemoveFont
*Type:* FUNCTION
remove a ttf font from a font collection

**Parameters**

- `factory` (dmResource::HFactory) - The factory
- `font` (FontResource*) - The font collection (.fontc)
- `ttf_hash` (dmhash_t) - The ttf path hash (.ttf)

**Returns**

- `result` (dmResource::Result) - RESULT_OK if successful

### SDF_EDGE_VALUE
*Type:* CONSTANT
The edge value of an sdf glyph bitmap
