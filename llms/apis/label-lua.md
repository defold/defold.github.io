# Label

**Namespace:** `label`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_label.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_label.cpp`

Functions to manipulate a label component.

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

### label.get_text
*Type:* FUNCTION
Gets the text from a label component

**Parameters**

- `url` (string | hash | url) - the label to get the text from

**Returns**

- `metrics` (string) - the label text

**Examples**

```
function init(self)
    local text = label.get_text("#label")
    print(text)
end

```

### label.set_text
*Type:* FUNCTION
Sets the text of a label component
 This method uses the message passing that means the value will be set after dispatch messages step.
More information is available in the Application Lifecycle manual.

**Parameters**

- `url` (string | hash | url) - the label that should have a constant set
- `text` (string | number) - the text

**Examples**

```
function init(self)
    label.set_text("#label", "Hello World!")
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
