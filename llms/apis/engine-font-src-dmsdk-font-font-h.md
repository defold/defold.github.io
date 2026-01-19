# Font

**Namespace:** `Font`
**Language:** C++
**Type:** Defold C++
**File:** `font.h`
**Source:** `engine/font/src/dmsdk/font/font.h`
**Include:** `dmsdk/font/font.h`

Font API for loading a font (truetype), getting glyph metrics and bitmap/sdf data

## API

### FontDestroy
*Type:* FUNCTION
Destroys a loaded font

**Parameters**

- `font` (HFont) - The font to deallocate

### FontFreeGlyph
*Type:* FUNCTION
Free the bitmap of the glyph

**Parameters**

- `font` (HFont) - The font
- `glyph` (dmFont::Glyph*) - The glyph

**Returns**

- `result` (dmFont::FontResult) - The result

### FontGetAscent
*Type:* FUNCTION
Get the max ascent of the font

**Parameters**

- `font` (HFont) - The font
- `scale` (float) - The scale factor

**Returns**

- `ascent` (float) - The max ascent

### FontGetDescent
*Type:* FUNCTION
Get the max descent of the font

**Parameters**

- `font` (HFont) - The font
- `scale` (float) - The scale factor

**Returns**

- `descent` (float) - The max descent

### FontGetGlyph
*Type:* FUNCTION
Get the metrics of a glyph

**Parameters**

- `font` (HFont) - The font
- `codepoint` (uint32_t) - The unicode code point
- `options` - (in) <span class="type"> FontGlyphOptions*</span> The glyph options
- `glyph` - (out) <span class="type"> FontGlyph*</span> The glyph

**Returns**

- `result` (FontFontResult) - If successful, user must call FreeGlyph() on the result to clear any image data.

### FontGetGlyphByIndex
*Type:* FUNCTION
Get the metrics of a glyph

**Parameters**

- `font` (HFont) - The font
- `glyph_index` (uint32_t) - The unicode code point
- `options` - (in) <span class="type"> FontGlyphOptions*</span> The glyph options
- `glyph` - (out) <span class="type"> FontGlyph*</span> The glyph

**Returns**

- `result` (FontFontResult) - If successful, user must call FreeGlyph() on the result to clear any image data.

### FontGetGlyphIndex
*Type:* FUNCTION
Get glyph index of a codepoint

**Parameters**

- `font` (HFont) - The font
- `codepoint` (uint32_t) - The unicode code point

**Returns**

- `glyph_index` (uint32_t) - 0 if no index was found

### FontGetLineGap
*Type:* FUNCTION
Get the line gap of the font

**Parameters**

- `font` (HFont) - The font
- `scale` (float) - The scale factor

**Returns**

- `line_gap` (float) - The line gap

### FontGetPath
*Type:* FUNCTION
Gets the path of the loaded font

**Parameters**

- `font` (HFont) - The font

**Returns**

- `path` (const char*) - The path

### FontGetPathHash
*Type:* FUNCTION
Gets the path hash of the loaded font

**Notes**

- We use a 32bit hash to make it easier to pair with a glyph index into a 64-bit key

**Parameters**

- `font` (HFont) - The font

**Returns**

- `path` (uint32_t) - The path

### FontGetResourceSize
*Type:* FUNCTION
Get the bytes used by this resource

**Parameters**

- `font` (HFont) - The font

**Returns**

- `size` (uint32_t) - The resource size

### FontGetScaleFromSize
*Type:* FUNCTION
Get the scale factor from a given pixel size.
Used to convert from points to pixel size

**Parameters**

- `font` (HFont) - The font
- `size` (float) - The font size (in pixel height)

**Returns**

- `scale` (float) - The scale factor

### FontGetType
*Type:* FUNCTION
Gets the specific implementation of the loaded font

**Parameters**

- `font` (HFont) - The font

**Returns**

- `type` (dmFont::FontType) - The type

### FontGlyph
*Type:* STRUCT
Represents a glyph.
If there's an associated image, it is of size width * height * channels.

**Notes**

- The baseline of a glyph bitmap is calculated: `base = glyph.bitmap.height - glyph.ascent`

**Members**

- `m_Bitmap` (FontGlyphBitmap) - The bitmap data of the glyph.
- `m_Codepoint` (uint32_t) - The unicode code point
- `m_Width` (float) - The glyph bounding width
- `m_Height` (float) - The glyph bounding height
- `m_Advance` (float) - The advance step of the glyph (in pixels)
- `m_LeftBearing` (float) - The left bearing of the glyph (in pixels)
- `m_Ascent` (float) - The ascent of the glyph. (in pixels)
- `m_Descent` (float) - The descent of the glyph. Positive! (in pixels)

### FontGlyphBitmap
*Type:* STRUCT
Holds the bitmap data of a glyph.
If there's an associated image, it is of size width * height * channels.

**Members**

- `m_Width` (uint16_t) - The glyph image width
- `m_Height` (uint16_t) - The glyph image height
- `m_Channels` (uint8_t) - The number of color channels
- `m_Flags` (uint8_t) - Flags describing the data. See #FontGlyphBitmapFlags.
- `m_Data` (uint8_t*) - The bitmap data, or null if no data available.
- `m_DataSize` (uint32_t) - The bitmap data size (e.g. if the data is compressed)

### FontGlyphBitmapFlags
*Type:* ENUM
FontGlyphBitmapFlags

**Members**

- `GLYPH_BM_FLAG_COMPRESSION_NONE` - = 0
- `GLYPH_BM_FLAG_COMPRESSION_DEFLATE` - = 1

### FontGlyphOptions
*Type:* STRUCT
Holds the bitmap data of a glyph.
If there's an associated image, it is of size width * height * channels.

**Members**

- `m_Scale` (float) - The font scale
- `m_GenerateImage` (bool) - If true, generates an SDF image, and fills out the glyph.m_Bitmap structure.
- `m_StbttSDFPadding` (int) - The sdk padding value (valid for FONT_TYPE_STBTTF fonts)
- `m_StbttSDFOnEdgeValue` (int) - Where the edge value is located (valid for FONT_TYPE_STBTTF fonts)

### FontLoadFromMemory
*Type:* FUNCTION
Loads a font from memory

**Parameters**

- `name` (const char*) - The name of the resource. For easier debugging
- `data` (void*) - The raw data
- `data_size` (uint32_t) - The length of the data (in bytes)
- `allocate` (bool) - If true, the font may allocate a copy of the data (if needed)

**Returns**

- `font` (HFont) - The loaded font, or null if it failed to load.

### FontLoadFromPath
*Type:* FUNCTION
Loads a font using a path

**Parameters**

- `path` (const char*) - The path to the resource

**Returns**

- `font` (HFont) - The loaded font, or null if it failed to load.

### FontResult
*Type:* ENUM
FontResult

**Members**

- `FONT_RESULT_OK`
- `FONT_RESULT_NOT_SUPPORTED`
- `FONT_RESULT_ERROR`

### FontType
*Type:* ENUM
FontType

**Members**

- `FONT_TYPE_STBTTF`
- `FONT_TYPE_STBOTF`
- `FONT_TYPE_UNKNOWN` - = 0xFFFFFFFF
