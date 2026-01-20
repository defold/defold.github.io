# FontCollection

**Namespace:** `FontCollection`
**Language:** C++
**Type:** Defold C++
**File:** `fontcollection.h`
**Source:** `engine/font/src/dmsdk/font/fontcollection.h`
**Include:** `dmsdk/font/fontcollection.h`

Font API for grouping multiple fonts into a collection

## API

### FontCollectionAddFont
*Type:* FUNCTION
add a font to the font collection

**Notes**

- No ownership transfer occurrs. HFont must be alive during the lifetime of the font collection

**Parameters**

- `coll` (HFontCollection) - the font collection
- `font` (HFont) - the font

**Returns**

- `result` (FontResult) - the result. FONT_RESULT_OK if successful

### FontCollectionCreate
*Type:* FUNCTION
Create a font collection

**Returns**

- `coll` (HFontCollection) - the font collection

### FontCollectionDestroy
*Type:* FUNCTION
destroy a font collection

**Parameters**

- `coll` (HFontCollection) - the font collection

### FontCollectionGetFont
*Type:* FUNCTION
return the font associated with the given index

**Parameters**

- `coll` (HFontCollection) - the font collection

**Returns**

- `font` (HFont) - the font at the given index

### FontCollectionGetFontCount
*Type:* FUNCTION
return number of fonts in the collection

**Parameters**

- `coll` (HFontCollection) - the font collection

**Returns**

- `count` (uint32_t) - the number of fonts

### FontCollectionRemoveFont
*Type:* FUNCTION
remove a font from the font collection

**Parameters**

- `coll` (HFontCollection) - the font collection
- `font` (HFont) - the font

**Returns**

- `result` (FontResult) - the result. FONT_RESULT_OK if successful

### HFontCollection
*Type:* TYPEDEF
Handle that holds a collection of fonts to use during text shaping
