# Font

**Namespace:** `font`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_font.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_font.cpp`

Functions, messages and properties used to manipulate font resources.

## API

### font.add_font
*Type:* FUNCTION
associates a ttf resource to a .fontc file.

**Notes**

- The ttf font is loaded via the resource system. There are a few ways it can be accessed:
    - It was already loaded in the resource system
    - It is bundled via our game data
    - It is accessible via a live update mount
- The reference count will increase for the .ttf font

**Parameters**

- `fontc` (string | hash) - The path to the .fontc resource
- `ttf` (string | hash) - The path to the .ttf resource

**Examples**

```
local font_hash = hash("/assets/fonts/roboto.fontc")
local ttf_hash = hash("/assets/fonts/Roboto/Roboto-Bold.ttf")
font.add_font(font_hash, ttf_hash)

```

### font.get_info
*Type:* FUNCTION
Gets information about a font, such as the associated font files

**Parameters**

- `fontc` (string | hash) - The path to the .fontc resource

**Returns**

- `info` (table) - the information table contains these fields:
<dl>
<dt><code>path</code></dt>
<dd><span class="type">hash</span> The path hash of the current file.</dd>
<dt><code>fonts</code></dt>
<dd>
<span class="type">table</span> An array of associated font (e.g. .ttf) files. Each item is a table that contains:
<dl>
<dt><code>path</code></dt>
<dd><span class="type">string</span> The path of the font file</dd>
<dt><code>path_hash</code></dt>
<dd><span class="type">hash</span> The path of the font file</dd>
</dl>
</dd>
</dl>

### font.prewarm_text
*Type:* FUNCTION
prepopulates the font glyph cache with rasterised glyphs

**Parameters**

- `fontc` (string | hash) - The path to the .fontc resource
- `text` (string) - The text to layout
- `callback` (function(self, request_id, result, errstring)) (optional) - (optional) A callback function that is called after the request is finished
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The current object.</dd>
<dt><code>request_id</code></dt>
<dd><span class="type">number</span> The request id</dd>
<dt><code>result</code></dt>
<dd><span class="type">boolean</span> True if request was succesful</dd>
<dt><code>errstring</code></dt>
<dd><span class="type">string</span> <code>nil</code> if the request was successful</dd>
</dl>

**Returns**

- `request_id` (number) - Returns the asynchronous request id

**Examples**

```
local font_hash = hash("/assets/fonts/roboto.fontc")
font.prewarm_text(font_hash, "Some text", function (self, request_id, result, errstring)
        -- cache is warm, show the text!
    end)

```

### font.remove_font
*Type:* FUNCTION
associates a ttf resource to a .fontc file

**Notes**

- The reference count will decrease for the .ttf font

**Parameters**

- `fontc` (string | hash) - The path to the .fontc resource
- `ttf` (string | hash) - The path to the .ttf resource

**Examples**

```
local font_hash = hash("/assets/fonts/roboto.fontc")
local ttf_hash = hash("/assets/fonts/Roboto/Roboto-Bold.ttf")
font.remove_font(font_hash, ttf_hash)

```
