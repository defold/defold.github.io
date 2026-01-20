# extension-fontgen

**Namespace:** `fontgen`
**Language:** Lua
**Type:** Extension

Functions to generate glyphs for fonts at runtime.

## API

### fontgen.load_font
*Type:* FUNCTION
Creates a mapping between a .fontc file and a .ttf file. Increases the ref count for both resources.

**Parameters**

- `fontc_path` (string) - Path to a .fontc file in the project
- `ttf_path` (string) - Path to a .ttf file in the project
- `options` (table) - Options for generating the glyphs
  - `sdf_padding` (number) - The number of padding pixels [0-255]
  - `sdf_edge` (number) - Where the edge is decided to be [0-255]
- `complete_function` (function) - function to call when the animation has completed
  - `self` (object) - The context of the calling script
  - `fontc_hash` (hash) - The path hash of the .fontc resource

### fontgen.unload_font
*Type:* FUNCTION
Removes the generator mapping between the .fontc and .ttf file. Decreases the ref count for both resources. Does not remove the previously generated glyphs!

**Parameters**

- `fontc_path_hash` (hash) - Path hash of the .fontc file in the project

### fontgen.add_glyphs
*Type:* FUNCTION
Asynchronoously sdds glyphs to the .fontc resource.

**Parameters**

- `fontc_path_hash` (hash) - Path hash of the .fontc file in the project
- `text` (string) - Utf-8 string containing glyphs to add to the .fontc *Note* No checks for duplicate glyphs is done.
- `callback` (function) - Function to be called after the last glyph was processed. May be nil.
  - `self` (object) - The script instance that called `add_glyphs`
  - `request` (int) - The request id returned by `add_glyphs`
  - `result` (bool) - True if all glyphs were added successfully
  - `errmsg` (string) - Error string if a glyph wasn't generated or added successfully

**Returns**

- `integer` - Returns a request id, used in the callback

### fontgen.remove_glyphs
*Type:* FUNCTION
Removes glyphs from the .fontc resource

**Parameters**

- `fontc_path_hash` (hash) - Path hash of the .fontc file in the project
- `text` (string) - Utf-8 string containing glyphs to remove from the .fontc
