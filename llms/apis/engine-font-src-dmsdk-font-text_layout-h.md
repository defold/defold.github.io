# TextLayout

**Namespace:** `TextLayout`
**Language:** C++
**Type:** Defold C++
**File:** `text_layout.h`
**Source:** `engine/font/src/dmsdk/font/text_layout.h`
**Include:** `dmsdk/font/text_layout.h`

API for laying out complex text into format ready for display

## API

### HTextLayout
*Type:* TYPEDEF
A handle representing a text layout

### TextDirection
*Type:* ENUM
An enum representing text layout directions

**Members**

- `TEXT_DIRECTION_LTR` -   Left-to-right text direction
- `TEXT_DIRECTION_RTL` -   Right-to-left text direction

### TextGlyph
*Type:* STRUCT
Glyph representing the final position within a layout

**Members**

- `m_Font` (HFont) - The font used for this glyph
- `m_X` (float) - the final x position, relative the top-left corner of the layout
- `m_Y` (float) - the final y position, relative the top-left corner of the layout
- `m_Width` (float) - the width of the glyph
- `m_Height` (float) - the height of the glyph
- `m_Codepoint` (uint32_t) - original copdepoint (if available)
- `m_GlyphIndex` (uint16_t) - the glyph index in the font
- `m_Cluster` (uint16_t) - the index in the original text, that this glyph corresponds to

### TextLayoutCreate
*Type:* FUNCTION
Create a text layout using a font collection
if successful, the caller must call TextLayoutFree() on the layout

**Parameters**

- `collection` (HFontCollection) - the font collection
- `codepoints` (uint32_t*) - an array of codepoints
- `num_codepoints` (uint32_t) - number of codepoints in the array
- `settings` (TextLayoutSettings*) - the settings used for rendering
- `layout` (HTextLayout*) - (out) the output text layout

**Returns**

- `result` (TextResult) - the result. TEXT_RESULT_OK if successful

### TextLayoutFree
*Type:* FUNCTION
Frees a previously created layout

**Parameters**

- `layout` (HTextLayout) - the text layout

### TextLayoutGetBounds
*Type:* FUNCTION
Get the lines in the layout

**Parameters**

- `layout` (HTextLayout) - the text layout

**Returns**

- `width` (float*) - the total width of the layout (out)
- `height` (float*) - the total height of the layout (out)

### TextLayoutGetGlyphCount
*Type:* FUNCTION
Get the glyph count in the layout

**Parameters**

- `layout` (HTextLayout) - the text layout

**Returns**

- `count` (uint32_t) - the number of glyphs in the layout

### TextLayoutGetGlyphs
*Type:* FUNCTION
Get the glyphs in the layout

**Parameters**

- `layout` (HTextLayout) - the text layout

**Returns**

- `glyphs` (TextGlyph*) - the array of glyphs in the layout

### TextLayoutGetLineCount
*Type:* FUNCTION
Get the line count in the layout

**Parameters**

- `layout` (HTextLayout) - the text layout

**Returns**

- `count` (uint32_t) - the number of lines in the layout

### TextLayoutGetLines
*Type:* FUNCTION
Get the lines in the layout

**Parameters**

- `layout` (HTextLayout) - the text layout

**Returns**

- `lines` (TextLine*) - the array of lines in the layout

### TextLayoutSettings
*Type:* STRUCT
Describes how to do a text layout

**Members**

- `m_Size` (float) - The desired size of the font (in pixels)
- `m_Width` (float) - Max layout width. Used only when m_LineBreak is non-zero
- `m_Leading` (float) - The extra space between each line. Set 1.0f as default.
- `m_Tracking` (float) - The extra tracking between glyphs. Set 0 as default.
- `m_Padding` (uint32_t) - Legacy: Padding for monospace, glyphbank fonts
- `m_LineBreak` (uint8_t:1) - Allow line breaks
- `m_Monospace` (uint8_t:1) - Legacy: Is the font a monospace font. Current: should be set on the font in the font collection!

### TextLayoutType
*Type:* ENUM
An enum representing text layout features
Each font supports a layout type
The selected layout type it the minimum value of layout types

**Members**

- `TEXT_LAYOUT_TYPE_LEGACY` - Legacy text shaping api
- `TEXT_LAYOUT_TYPE_FULL` -   Full text shaping api

### TextLine
*Type:* STRUCT
Represents a line of glyphs

**Members**

- `m_Width` (float) - Width of the line
- `m_Index` (uint16_t) - Index into the list of glyphs
- `m_Length` (uint16_t) - Number of glyphs to render

### TextResult
*Type:* ENUM
An enum representing text layout results

**Members**

- `TEXT_RESULT_OK`
- `TEXT_RESULT_ERROR`
