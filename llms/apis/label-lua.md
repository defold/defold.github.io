# Label

**Namespace:** `label`
**Language:** Lua
**Type:** Defold Lua
**File:** `label_ddf.proto`
**Source:** `engine/gamesys/proto/gamesys/label_ddf.proto`

Label API documentation

## API

### color
*Type:* PROPERTY
The color of the label. The type of the property is vector4.

**Examples**

```
function init(self)
   -- Get the current color's y component
   local red_component = go.get("#label", "color.y")
   -- Animate the color
   go.animate("#label", "color", go.PLAYBACK_LOOP_PINGPONG, vmath.vector4(0,1,0,1), go.EASING_INOUTSINE, 1)
end

```

### font
*Type:* PROPERTY
The font used when rendering the label. The type of the property is hash.

**Examples**

How to set font using a script property (see resource.font)
```
go.property("my_font", resource.font("/font.font"))

function init(self)
  go.set("#label", "font", self.my_font)
end

```

### label.get_layout_objects
*Type:* FUNCTION
Returns the sprites and links found in the label's current layout.
Each entry contains type, id, the zero-based UTF-32 text_offset,
text_length, resolved x, y, width
and height, and an attributes table. The position is the lower-left
object corner relative to the label's upper-left layout origin.
Inline resource rendering is not part of this MVP; sprites use their explicit
dimensions or a one-em square fallback.

**Parameters**

- `url` (string | hash | url) - the label to inspect

**Returns**

- `objects` (label.layout_object[]) - layout objects in source order

**Examples**

```
local objects = label.get_layout_objects("#label")
for _, object in ipairs(objects) do
    if object.type == "link" then
        print(object.attributes.src, object.text_offset, object.text_length)
    elseif object.type == "sprite" then
        print(object.attributes.src, object.x, object.y, object.width, object.height)
    end
end

```

### label.get_text
*Type:* FUNCTION
Gets the text from a label component
 This function is deprecated. Use go.get("#label", "text") instead.

**Parameters**

- `url` (string | hash | url) - the label to get the text from

**Returns**

- `text` (string) - the label text

**Examples**

```
function init(self)
    local text = go.get("#label", "text")
    print(text)
end

```

### label.layout_object
*Type:* STRUCT
Rich-text layout object

**Members**

- `type` (string) - object type, currently <code>link</code> or <code>sprite</code>
- `id` (hash) - the object's <code>id</code> attribute, or its generated layout object id
- `text_offset` (integer) - zero-based UTF-32 offset in the visible text
- `text_length` (integer) - visible UTF-32 text length covered by the object
- `x` (number) - lower-left x-coordinate relative to the label's upper-left layout origin
- `y` (number) - lower-left y-coordinate relative to the label's upper-left layout origin
- `width` (number) - resolved object width
- `height` (number) - resolved object height
- `attributes` (table<string, string>) - markup attributes keyed by name

### label.set_text
*Type:* FUNCTION
Sets the text of a label component
 This function is deprecated. Use go.set("#label", "text", value) instead.
 This method uses the message passing that means the value will be set after dispatch messages step.
More information is available in the Application Lifecycle manual.

**Parameters**

- `url` (string | hash | url) - the label that should have a constant set
- `text` (string | number) - the text

**Examples**

```
function init(self)
    go.set("#label", "text", "Hello World!")
end

```

### leading
*Type:* PROPERTY
The leading of the label. This value is used to scale the line spacing of text.
The type of the property is number.

**Examples**

How to query a label's leading:
```
function init(self)
 -- get leading from component "label"
 local leading = go.get("#label", "leading")
 -- do something useful
 leading = leading * 1.2
 go.set("#label", "leading", leading)
end

```

### line_break
*Type:* PROPERTY
The line break of the label.
This value is used to adjust the vertical spacing of characters in the text.
The type of the property is boolean.

**Examples**

How to query a label's line break:
```
function init(self)
 -- get line_break from component "label"
 local line_break = go.get("#label", "line_break")
 -- do something useful
 go.set("#label", "line_break", false)
end

```

### material
*Type:* PROPERTY
The material used when rendering the label. The type of the property is hash.

**Examples**

How to set material using a script property (see resource.material)
```
go.property("my_material", resource.material("/material.material"))

function init(self)
  go.set("#label", "material", self.my_material)
end

```

### outline
*Type:* PROPERTY
The outline color of the label. The type of the property is vector4.

**Examples**

```
function init(self)
   -- Get the current outline color
   local outline = go.get("#label", "outline")
   -- Animate the property
   go.animate("#label", "outline", go.PLAYBACK_LOOP_PINGPONG, vmath.vector4(0,1,0,1), go.EASING_INOUTSINE, 1)
end

```

### scale
*Type:* PROPERTY
The scale of the label. The type of the property is number (uniform)
or vector3 (non uniform).

**Examples**

How to scale a label independently along the X and Y axis:
```
function init(self)
   -- Double the y-axis scaling on component "label"
   local yscale = go.get("#label", "scale.y")
   go.set("#label", "scale.y", yscale * 2)
   -- Set the new scale altogether
   go.set("#label", "scale", vmath.vector3(2,2,2))
   -- Animate the scale
   go.animate("#label", "scale", go.PLAYBACK_LOOP_PINGPONG, vmath.vector3(2,2,2), go.EASING_INOUTSINE, 1)
end

```

### shadow
*Type:* PROPERTY
The shadow color of the label. The type of the property is vector4.

**Examples**

```
function init(self)
 -- Get the current shadow color
 local shadow = go.get("#label", "shadow")
 -- Animate the property
 go.animate("#label", "shadow", go.PLAYBACK_LOOP_PINGPONG, vmath.vector4(0,1,0,1), go.EASING_INOUTSINE, 1)
end

```

### size
*Type:* PROPERTY
Returns the size of the label. The size will constrain the text if line break is enabled.
The type of the property is vector3.

**Examples**

How to query a label's size, either as a vector or selecting a specific dimension:
```
function init(self)
 -- get size from component "label"
 local size = go.get("#label", "size")
 local sizex = go.get("#label", "size.x")
 -- do something useful
 assert(size.x == sizex)
end

```

### text
*Type:* PROPERTY
The text of the label.

**Examples**

```
function init(self)
    go.set("#label", "text", "Hello World!")
    local text = go.get("#label", "text")
end

```

### text_object_clicked
*Type:* MESSAGE
Sent to the owning game object when an interactive rich-text object is clicked.

**Parameters**

- `id` (hash) - the object's <code>id</code> attribute, or its generated layout object id
- `type` (hash) - the layout object type, currently <code>link</code>
- `src` (string) - the application-defined target from the object's <code>src</code> attribute

### text_object_hovered
*Type:* MESSAGE
Sent to the owning game object when the pointer enters an interactive rich-text object.

**Parameters**

- `id` (hash) - the object's <code>id</code> attribute, or its generated layout object id
- `type` (hash) - the layout object type, currently <code>link</code>
- `src` (string) - the application-defined target from the object's <code>src</code> attribute

### text_object_unhovered
*Type:* MESSAGE
Sent to the owning game object when the pointer leaves an interactive rich-text object.

**Parameters**

- `id` (hash) - the object's <code>id</code> attribute, or its generated layout object id
- `type` (hash) - the layout object type, currently <code>link</code>
- `src` (string) - the application-defined target from the object's <code>src</code> attribute

### tracking
*Type:* PROPERTY
The tracking of the label.
This value is used to adjust the vertical spacing of characters in the text.
The type of the property is number.

**Examples**

How to query a label's tracking:
```
function init(self)
 -- get tracking from component "label"
 local tracking = go.get("#label", "tracking")
 -- do something useful
 tracking = tracking * 1.2
 go.set("#label", "tracking", tracking)
end

```
