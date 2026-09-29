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
associates a TTF or OTF resource to a .fontc file.

**Notes**

- The font is loaded via the resource system. There are a few ways it can be accessed:
    - It was already loaded in the resource system
    - It is bundled via our game data
    - It is accessible via a live update mount
- The reference count will increase for the .ttf or .otf font

**Parameters**

- `fontc` (string | hash) - The path to the .fontc resource
- `font` (string | hash) - The path to the .ttf or .otf resource

**Examples**

```
local font_hash = hash("/assets/fonts/roboto.fontc")
local ttf_hash = hash("/assets/fonts/Roboto/Roboto-Bold.ttf")
font.add_font(font_hash, ttf_hash)

```

### font.file_info
*Type:* STRUCT
Associated font file information

**Members**

- `path` (string) - path to the <code>.ttf</code> or <code>.otf</code> font file
- `path_hash` (hash) - hashed font-file path

### font.get_info
*Type:* FUNCTION
Gets information about a font, such as the associated font files

**Parameters**

- `fontc` (string | hash) - The path to the .fontc resource

**Returns**

- `info` (font.info) - font resource information

### font.info
*Type:* STRUCT
Font resource information

**Members**

- `path` (hash) - path hash of the <code>.fontc</code> resource
- `fonts` (font.file_info[]) - associated font files

### font.prewarm_text
*Type:* FUNCTION
prepopulates the font glyph cache with rasterised glyphs

**Parameters**

- `fontc` (string | hash) - The path to the .fontc resource
- `text` (string) - The text to layout
- `callback` (fun(self:script_instance, request_id:integer, result:boolean, errstring?:string)) (optional) - (optional) A callback function that is called after the request is finished
<dl>
<dt class="api-lua-v2-type-definition"><code>self:<a href="../builtins-lua/#script_instance">script_instance</a></code></dt>
<dd>The current script instance.</dd>
<dt class="api-lua-v2-type-definition"><code>request_id:<a href="../../../manuals/lua/#variables-and-data-types">integer</a></code></dt>
<dd>The request id</dd>
<dt class="api-lua-v2-type-definition"><code>result:<a href="../../../manuals/lua/#variables-and-data-types">boolean</a></code></dt>
<dd>True if request was succesful</dd>
<dt class="api-lua-v2-type-definition"><code>errstring:<a href="../../../manuals/lua/#variables-and-data-types">string</a></code></dt>
<dd><code>nil</code> if the request was successful</dd>
</dl>

**Returns**

- `request_id` (integer) - Returns the asynchronous request id

**Examples**

```
local font_hash = hash("/assets/fonts/roboto.fontc")
font.prewarm_text(font_hash, "Some text", function (self, request_id, result, errstring)
        -- cache is warm, show the text!
    end)

```

### font.remove_font
*Type:* FUNCTION
associates a TTF or OTF resource to a .fontc file

**Notes**

- The reference count will decrease for the .ttf or .otf font

**Parameters**

- `fontc` (string | hash) - The path to the .fontc resource
- `font` (string | hash) - The path to the .ttf or .otf resource

**Examples**

```
local font_hash = hash("/assets/fonts/roboto.fontc")
local ttf_hash = hash("/assets/fonts/Roboto/Roboto-Bold.ttf")
font.remove_font(font_hash, ttf_hash)

```

### font.set_style
*Type:* FUNCTION
Named object styles are resolved by text layouts without reshaping text.
A link tag uses link by default. Callers may select another named style,
such as link:hover or link:active, in response to input.
Font collections initially define these named styles. Each default contains
a normalized RGBA face-color multiplier and no effects. The default link
style also uses a solid underline, which remains when hover or active colors
are applied:

link: (0.10, 0.45, 0.90, 1.0), solid underline
link:hover: (0.30, 0.65, 1.00, 1.0)
link:active: (0.05, 0.30, 0.70, 1.0)

The definition is an opening-only sequence of rich-text tags. Tags are
implicitly closed in reverse order. Calling this function replaces the
named render properties and effects. Resource-defined decorations, such as
the default link underline, remain unchanged.

**Parameters**

- `fontc` (string | hash) - The path to the <code>.fontc</code> resource.
- `name` (string) - Style name, for example <code>link:hover</code>.
- `style` (string) - Opening-only render-style markup.

**Examples**

```
font.set_style("/fonts/ui.fontc", "link:hover",
    "")

```
