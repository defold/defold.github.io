# GUI

**Namespace:** `gui`
**Language:** Lua
**Type:** Defold Lua
**File:** `gui_script.cpp`
**Source:** `engine/gui/src/gui_script.cpp`

GUI core hooks, functions, messages, properties and constants for
creation and manipulation of GUI nodes. The "gui" namespace is
accessible only from gui scripts.

## API

### final
*Type:* FUNCTION
This is a callback-function, which is called by the engine when a gui component is finalized (destroyed). It can
be used to e.g. take some last action, report the finalization to other game object instances
or release user input focus (see release_input_focus). There is no use in starting any animations or similar
from this function since the gui component is about to be destroyed.

**Parameters**

- `self` (userdata) - reference to the script state to be used for storing data

**Examples**

```
function final(self)
    -- report finalization
    msg.post("my_friend_instance", "im_dead", {my_stats = self.some_value})
end

```

### fonts
*Type:* PROPERTY
The fonts used in the gui. The type of the property is hash.
Key must be specified in options table.

**Examples**

How to set font using a script property (see resource.font)
```
go.property("title_latin", resource.font("/open_sans.font"))
go.property("title_cyrillic", resource.font("/open_sans_cyrillic.font"))

function init(self)
  go.set("#gui", "fonts", self.title_cyrillic, {key = "title"})
end

```

### gui.ADJUST_FIT
*Type:* CONSTANT
Adjust mode is used when the screen resolution differs from the project settings.
The fit mode ensures that the entire node is visible in the adjusted gui scene.

### gui.ADJUST_STRETCH
*Type:* CONSTANT
Adjust mode is used when the screen resolution differs from the project settings.
The stretch mode ensures that the node is displayed as is in the adjusted gui scene, which might scale it non-uniformally.

### gui.ADJUST_ZOOM
*Type:* CONSTANT
Adjust mode is used when the screen resolution differs from the project settings.
The zoom mode ensures that the node fills its entire area and might make the node exceed it.

### gui.ANCHOR_BOTTOM
*Type:* CONSTANT
bottom y-anchor

### gui.ANCHOR_LEFT
*Type:* CONSTANT
left x-anchor

### gui.ANCHOR_NONE
*Type:* CONSTANT
no anchor

### gui.ANCHOR_RIGHT
*Type:* CONSTANT
right x-anchor

### gui.ANCHOR_TOP
*Type:* CONSTANT
top y-anchor

### gui.animate
*Type:* FUNCTION
This starts an animation of a node property according to the specified parameters.
If the node property is already being animated, that animation will be canceled and
replaced by the new one. Note however that several different node properties
can be animated simultaneously. Use gui.cancel_animation to stop the animation
before it has completed.
Composite properties of type vector3, vector4 or quaternion
also expose their sub-components (x, y, z and w).
You can address the components individually by suffixing the name with a dot '.'
and the name of the component.
For instance, "position.x" (the position x coordinate) or "color.w"
(the color alpha value).
If a complete_function (Lua function) is specified, that function will be called
when the animation has completed.
By starting a new animation in that function, several animations can be sequenced
together. See the examples below for more information.

**Parameters**

- `node` (node) - node to animate
- `property` (string | constant) - property to animate
<ul>
<li><code>"position"</code></li>
<li><code>"rotation"</code></li>
<li><code>"euler"</code></li>
<li><code>"scale"</code></li>
<li><code>"color"</code></li>
<li><code>"outline"</code></li>
<li><code>"shadow"</code></li>
<li><code>"size"</code></li>
<li><code>"fill_angle"</code> (pie)</li>
<li><code>"inner_radius"</code> (pie)</li>
<li><code>"leading"</code> (text)</li>
<li><code>"tracking"</code> (text)</li>
<li><code>"slice9"</code> (slice9)</li>
</ul>
The following property constants are defined equaling the corresponding property string names.
<ul>
<li><code>gui.PROP_POSITION</code></li>
<li><code>gui.PROP_ROTATION</code></li>
<li><code>gui.PROP_EULER</code></li>
<li><code>gui.PROP_SCALE</code></li>
<li><code>gui.PROP_COLOR</code></li>
<li><code>gui.PROP_OUTLINE</code></li>
<li><code>gui.PROP_SHADOW</code></li>
<li><code>gui.PROP_SIZE</code></li>
<li><code>gui.PROP_FILL_ANGLE</code></li>
<li><code>gui.PROP_INNER_RADIUS</code></li>
<li><code>gui.PROP_LEADING</code></li>
<li><code>gui.PROP_TRACKING</code></li>
<li><code>gui.PROP_SLICE9</code></li>
</ul>
- `to` (number | vector3 | vector4 | quaternion) - target property value
- `easing` (constant | vector) - easing to use during animation.
     Either specify one of the <code>gui.EASING_*</code> constants or provide a
     <span class="type">vector</span> with a custom curve. See the <a href="/manuals/animation#_easing">animation guide</a> for more information.
- `duration` (number) - duration of the animation in seconds.
- `delay` (number) (optional) - delay before the animation starts in seconds.
- `complete_function` (function(self, node)) (optional) - function to call when the
     animation has completed
- `playback` (constant) (optional) - playback mode
<ul>
<li><code>gui.PLAYBACK_ONCE_FORWARD</code></li>
<li><code>gui.PLAYBACK_ONCE_BACKWARD</code></li>
<li><code>gui.PLAYBACK_ONCE_PINGPONG</code></li>
<li><code>gui.PLAYBACK_LOOP_FORWARD</code></li>
<li><code>gui.PLAYBACK_LOOP_BACKWARD</code></li>
<li><code>gui.PLAYBACK_LOOP_PINGPONG</code></li>
</ul>

**Examples**

How to start a simple color animation, where the node fades in to white during 0.5 seconds:
```
gui.set_color(node, vmath.vector4(0, 0, 0, 0)) -- node is fully transparent
gui.animate(node, gui.PROP_COLOR, vmath.vector4(1, 1, 1, 1), gui.EASING_INOUTQUAD, 0.5) -- start animation

```

How to start a sequenced animation where the node fades in to white during 0.5 seconds, stays visible for 2 seconds and then fades out:
```
local function on_animation_done(self, node)
    -- fade out node, but wait 2 seconds before the animation starts
    gui.animate(node, gui.PROP_COLOR, vmath.vector4(0, 0, 0, 0), gui.EASING_OUTQUAD, 0.5, 2.0)
end

function init(self)
    -- fetch the node we want to animate
    local my_node = gui.get_node("my_node")
    -- node is initially set to fully transparent
    gui.set_color(my_node, vmath.vector4(0, 0, 0, 0))
    -- animate the node immediately and call on_animation_done when the animation has completed
    gui.animate(my_node, gui.PROP_COLOR, vmath.vector4(1, 1, 1, 1), gui.EASING_INOUTQUAD, 0.5, 0.0, on_animation_done)
end

```

How to animate a node's y position using a crazy custom easing curve:
```
function init(self)
    local values = { 0, 0, 0, 0, 0, 0, 0, 0,
                     1, 1, 1, 1, 1, 1, 1, 1,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     1, 1, 1, 1, 1, 1, 1, 1,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     1, 1, 1, 1, 1, 1, 1, 1,
                     0, 0, 0, 0, 0, 0, 0, 0,
                     1, 1, 1, 1, 1, 1, 1, 1 }
    local vec = vmath.vector(values)
    local node = gui.get_node("box")
    gui.animate(node, "position.y", 100, vec, 4.0, 0, nil, gui.PLAYBACK_LOOP_PINGPONG)
end

```

### gui.BLEND_ADD
*Type:* CONSTANT
additive blending

### gui.BLEND_ADD_ALPHA
*Type:* CONSTANT
additive alpha blending

### gui.BLEND_ALPHA
*Type:* CONSTANT
alpha blending

### gui.BLEND_MULT
*Type:* CONSTANT
multiply blending

### gui.BLEND_SCREEN
*Type:* CONSTANT
screen blending

### gui.cancel_animations
*Type:* FUNCTION
If one or more animations of the specified node is currently running (started by gui.animate), they will immediately be canceled.

**Parameters**

- `node` (node) - node that should have its animation canceled
- `property` (nil | string | constant) (optional) - optional property for which the animation should be canceled
<ul>
<li><code>"position"</code></li>
<li><code>"rotation"</code></li>
<li><code>"euler"</code></li>
<li><code>"scale"</code></li>
<li><code>"color"</code></li>
<li><code>"outline"</code></li>
<li><code>"shadow"</code></li>
<li><code>"size"</code></li>
<li><code>"fill_angle"</code> (pie)</li>
<li><code>"inner_radius"</code> (pie)</li>
<li><code>"leading"</code> (text)</li>
<li><code>"tracking"</code> (text)</li>
<li><code>"slice9"</code> (slice9)</li>
</ul>

**Examples**

Start an animation of the position property of a node, then cancel parts of
the animation:
```
local node = gui.get_node("my_node")
-- animate to new position
local pos = vmath.vector3(100, 100, 0)
gui.animate(node, "position", pos, go.EASING_LINEAR, 2)
...
-- cancel animation of the x component.
gui.cancel_animations(node, "position.x")

```

Cancels all property animations on a node in a single call:
```
local node = gui.get_node("my_node")
-- animate to new position and scale
gui.animate(node, "position", vmath.vector3(100, 100, 0), go.EASING_LINEAR, 5)
gui.animate(node, "scale", vmath.vector3(0.5), go.EASING_LINEAR, 5)
...
-- cancel positioning and scaling at once
gui.cancel_animations(node)

```

### gui.cancel_flipbook
*Type:* FUNCTION
Cancels any running flipbook animation on the specified node.

**Parameters**

- `node` (node) - node cancel flipbook animation for

**Examples**

```
local node = gui.get_node("anim_node")
gui.cancel_flipbook(node)

```

### gui.CLIPPING_MODE_NONE
*Type:* CONSTANT
clipping mode none

### gui.CLIPPING_MODE_STENCIL
*Type:* CONSTANT
clipping mode stencil

### gui.clone
*Type:* FUNCTION
Make a clone instance of a node. The cloned node will be identical to the
original node, except the id which is generated as the string "node" plus
a sequential unsigned integer value.
This function does not clone the supplied node's children nodes.
Use gui.clone_tree for that purpose.

**Parameters**

- `node` (node) - node to clone

**Returns**

- `clone` (node) - the cloned node

### gui.clone_tree
*Type:* FUNCTION
Make a clone instance of a node and all its children.
Use gui.clone to clone a node excluding its children.

**Parameters**

- `node` (node) - root node to clone

**Returns**

- `clones` (table) - a table mapping node ids to the corresponding cloned nodes

### gui.delete_node
*Type:* FUNCTION
Deletes the specified node. Any child nodes of the specified node will be
recursively deleted.

**Parameters**

- `node` (node) - node to delete

**Examples**

Delete a particular node and any child nodes it might have:
```
local node = gui.get_node("my_node")
gui.delete_node(node)

```

### gui.delete_texture
*Type:* FUNCTION
Delete a dynamically created texture.

**Parameters**

- `texture` (string | hash) - texture id

**Examples**

```
function init(self)
     -- Create a texture.
     if gui.new_texture("temp_tx", 10, 10, "rgb", string.rep('\0', 10 * 10 * 3)) then
         -- Do something with the texture.
         ...

         -- Delete the texture
         gui.delete_texture("temp_tx")
     end
end

```

### gui.EASING_INBACK
*Type:* CONSTANT
in-back

### gui.EASING_INBOUNCE
*Type:* CONSTANT
in-bounce

### gui.EASING_INCIRC
*Type:* CONSTANT
in-circlic

### gui.EASING_INCUBIC
*Type:* CONSTANT
in-cubic

### gui.EASING_INELASTIC
*Type:* CONSTANT
in-elastic

### gui.EASING_INEXPO
*Type:* CONSTANT
in-exponential

### gui.EASING_INOUTBACK
*Type:* CONSTANT
in-out-back

### gui.EASING_INOUTBOUNCE
*Type:* CONSTANT
in-out-bounce

### gui.EASING_INOUTCIRC
*Type:* CONSTANT
in-out-circlic

### gui.EASING_INOUTCUBIC
*Type:* CONSTANT
in-out-cubic

### gui.EASING_INOUTELASTIC
*Type:* CONSTANT
in-out-elastic

### gui.EASING_INOUTEXPO
*Type:* CONSTANT
in-out-exponential

### gui.EASING_INOUTQUAD
*Type:* CONSTANT
in-out-quadratic

### gui.EASING_INOUTQUART
*Type:* CONSTANT
in-out-quartic

### gui.EASING_INOUTQUINT
*Type:* CONSTANT
in-out-quintic

### gui.EASING_INOUTSINE
*Type:* CONSTANT
in-out-sine

### gui.EASING_INQUAD
*Type:* CONSTANT
in-quadratic

### gui.EASING_INQUART
*Type:* CONSTANT
in-quartic

### gui.EASING_INQUINT
*Type:* CONSTANT
in-quintic

### gui.EASING_INSINE
*Type:* CONSTANT
in-sine

### gui.EASING_LINEAR
*Type:* CONSTANT
linear interpolation

### gui.EASING_OUTBACK
*Type:* CONSTANT
out-back

### gui.EASING_OUTBOUNCE
*Type:* CONSTANT
out-bounce

### gui.EASING_OUTCIRC
*Type:* CONSTANT
out-circlic

### gui.EASING_OUTCUBIC
*Type:* CONSTANT
out-cubic

### gui.EASING_OUTELASTIC
*Type:* CONSTANT
out-elastic

### gui.EASING_OUTEXPO
*Type:* CONSTANT
out-exponential

### gui.EASING_OUTINBACK
*Type:* CONSTANT
out-in-back

### gui.EASING_OUTINBOUNCE
*Type:* CONSTANT
out-in-bounce

### gui.EASING_OUTINCIRC
*Type:* CONSTANT
out-in-circlic

### gui.EASING_OUTINCUBIC
*Type:* CONSTANT
out-in-cubic

### gui.EASING_OUTINELASTIC
*Type:* CONSTANT
out-in-elastic

### gui.EASING_OUTINEXPO
*Type:* CONSTANT
out-in-exponential

### gui.EASING_OUTINQUAD
*Type:* CONSTANT
out-in-quadratic

### gui.EASING_OUTINQUART
*Type:* CONSTANT
out-in-quartic

### gui.EASING_OUTINQUINT
*Type:* CONSTANT
out-in-quintic

### gui.EASING_OUTINSINE
*Type:* CONSTANT
out-in-sine

### gui.EASING_OUTQUAD
*Type:* CONSTANT
out-quadratic

### gui.EASING_OUTQUART
*Type:* CONSTANT
out-quartic

### gui.EASING_OUTQUINT
*Type:* CONSTANT
out-quintic

### gui.EASING_OUTSINE
*Type:* CONSTANT
out-sine

### gui.get
*Type:* FUNCTION
Instead of using specific getters such as gui.get_position or gui.get_scale,
you can use gui.get instead and supply the property as a string or a hash.
While this function is similar to go.get, there are a few more restrictions
when operating in the gui namespace. Most notably, only these explicitly named properties are supported:

"position"
"rotation"
"euler"
"scale"
"color"
"outline"
"shadow"
"size"
"fill_angle" (pie)
"inner_radius" (pie)
"leading" (text)
"tracking" (text)
"slice9" (slice9)

The value returned will either be a vmath.vector4 or a single number, i.e getting the "position"
property will return a vec4 while getting the "position.x" property will return a single value.
You can also use this function to get material constants.

**Parameters**

- `node` (node) - node to get the property for
- `property` (string | hash | constant) - the property to retrieve
- `options` (table) (optional) - optional options table (only applicable for material constants)
- <code>index</code> <span class="type">number</span> index into array property (1 based)

**Examples**

Get properties on existing nodes:
```
local node = gui.get_node("my_box_node")
local node_position = gui.get(node, "position")

```

### gui.get_adjust_mode
*Type:* FUNCTION
Returns the adjust mode of a node.
The adjust mode defines how the node will adjust itself to screen
resolutions that differs from the one in the project settings.

**Parameters**

- `node` (node) - node from which to get the adjust mode (node)

**Returns**

- `adjust_mode` (constant) - the current adjust mode
<ul>
<li><code>gui.ADJUST_FIT</code></li>
<li><code>gui.ADJUST_ZOOM</code></li>
<li><code>gui.ADJUST_STRETCH</code></li>
</ul>

### gui.get_alpha
*Type:* FUNCTION
gets the node alpha

**Parameters**

- `node` (node) - node from which to get alpha

**Returns**

- `alpha` (number) - alpha

### gui.get_blend_mode
*Type:* FUNCTION
Returns the blend mode of a node.
Blend mode defines how the node will be blended with the background.

**Parameters**

- `node` (node) - node from which to get the blend mode

**Returns**

- `blend_mode` (constant) - blend mode
<ul>
<li><code>gui.BLEND_ALPHA</code></li>
<li><code>gui.BLEND_ADD</code></li>
<li><code>gui.BLEND_ADD_ALPHA</code></li>
<li><code>gui.BLEND_MULT</code></li>
<li><code>gui.BLEND_SCREEN</code></li>
</ul>

### gui.get_clipping_inverted
*Type:* FUNCTION
If node is set as an inverted clipping node, it will clip anything inside as opposed to outside.

**Parameters**

- `node` (node) - node from which to get the clipping inverted state

**Returns**

- `inverted` (boolean) - <code>true</code> or <code>false</code>

### gui.get_clipping_mode
*Type:* FUNCTION
Clipping mode defines how the node will clip it's children nodes

**Parameters**

- `node` (node) - node from which to get the clipping mode

**Returns**

- `clipping_mode` (constant) - clipping mode
<ul>
  <li><code>gui.CLIPPING_MODE_NONE</code></li>
  <li><code>gui.CLIPPING_MODE_STENCIL</code></li>
</ul>

### gui.get_clipping_visible
*Type:* FUNCTION
If node is set as visible clipping node, it will be shown as well as clipping. Otherwise, it will only clip but not show visually.

**Parameters**

- `node` (node) - node from which to get the clipping visibility state

**Returns**

- `visible` (boolean) - <code>true</code> or <code>false</code>

### gui.get_color
*Type:* FUNCTION
Returns the color of the supplied node. The components
of the returned vector4 contains the color channel values:

Component
Color value

x
Red value

y
Green value

z
Blue value

w
Alpha value

**Parameters**

- `node` (node) - node to get the color from

**Returns**

- `color` (vector4) - node color

### gui.get_euler
*Type:* FUNCTION
Returns the rotation of the supplied node.
The rotation is expressed in degree Euler angles.

**Parameters**

- `node` (node) - node to get the rotation from

**Returns**

- `rotation` (vector3) - node rotation

### gui.get_fill_angle
*Type:* FUNCTION
Returns the sector angle of a pie node.

**Parameters**

- `node` (node) - node from which to get the fill angle

**Returns**

- `angle` (number) - sector angle

### gui.get_flipbook
*Type:* FUNCTION
Get node flipbook animation.

**Parameters**

- `node` (node) - node to get flipbook animation from

**Returns**

- `animation` (hash) - animation id

### gui.get_flipbook_cursor
*Type:* FUNCTION
This is only useful nodes with flipbook animations. Gets the normalized cursor of the flipbook animation on a node.

**Parameters**

- `node` (node) - node to get the cursor for (node)

**Returns**

- `cursor` (number) - cursor value

### gui.get_flipbook_playback_rate
*Type:* FUNCTION
This is only useful nodes with flipbook animations. Gets the playback rate of the flipbook animation on a node.

**Parameters**

- `node` (node) - node to set the cursor for

**Returns**

- `rate` (number) - playback rate

### gui.get_font
*Type:* FUNCTION
This is only useful for text nodes. The font must be mapped to the gui scene in the gui editor.

**Parameters**

- `node` (node) - node from which to get the font

**Returns**

- `font` (hash) - font id

### gui.get_font_resource
*Type:* FUNCTION
This is only useful for text nodes. The font must be mapped to the gui scene in the gui editor.

**Parameters**

- `font_name` (hash | string) - font of which to get the path hash

**Returns**

- `hash` (hash) - path hash to resource

**Examples**

Get the text metrics for a text
```
function init(self)
  local node = gui.get_node("name")
  local font_name = gui.get_font(node)
  local font = gui.get_font_resource(font_name)
  local metrics = resource.get_text_metrics(font, "The quick brown fox\n jumps over the lazy dog")
end

```

### gui.get_height
*Type:* FUNCTION
Returns the scene height.

**Returns**

- `height` (number) - scene height

### gui.get_id
*Type:* FUNCTION
Retrieves the id of the specified node.

**Parameters**

- `node` (node) - the node to retrieve the id from

**Returns**

- `id` (hash) - the id of the node

**Examples**

Gets the id of a node:
```
local node = gui.get_node("my_node")

local id = gui.get_id(node)
print(id) --> hash: [my_node]

```

### gui.get_index
*Type:* FUNCTION
Retrieve the index of the specified node among its siblings.
The index defines the order in which a node appear in a GUI scene.
Higher index means the node is drawn on top of lower indexed nodes.

**Parameters**

- `node` (node) - the node to retrieve the id from

**Returns**

- `index` (number) - the index of the node

**Examples**

Compare the index order of two sibling nodes:
```
local node1 = gui.get_node("my_node_1")
local node2 = gui.get_node("my_node_2")

if gui.get_index(node1) < gui.get_index(node2) then
    -- node1 is drawn below node2
else
    -- node2 is drawn below node1
end

```

### gui.get_inherit_alpha
*Type:* FUNCTION
gets the node inherit alpha state

**Parameters**

- `node` (node) - node from which to get the inherit alpha state

**Returns**

- `inherit_alpha` (boolean) - <code>true</code> or <code>false</code>

### gui.get_inner_radius
*Type:* FUNCTION
Returns the inner radius of a pie node.
The radius is defined along the x-axis.

**Parameters**

- `node` (node) - node from where to get the inner radius

**Returns**

- `radius` (number) - inner radius

### gui.get_layer
*Type:* FUNCTION
The layer must be mapped to the gui scene in the gui editor.

**Parameters**

- `node` (node) - node from which to get the layer

**Returns**

- `layer` (hash) - layer id

### gui.get_layout
*Type:* FUNCTION
gets the scene current layout

**Returns**

- `layout` (hash) - layout id

### gui.get_layouts
*Type:* FUNCTION
Returns a table mapping each layout id hash to a vector3(width, height, 0). For the default layout,
the current scene resolution is returned. If a layout name is not present in the Display Profiles (or when
no display profiles are assigned), the width/height pair is 0.

**Returns**

- `return` (table) - layout_id_hash -&gt; vmath.vector3(width, height, 0)

### gui.get_leading
*Type:* FUNCTION
Returns the leading value for a text node.

**Parameters**

- `node` (node) - node from where to get the leading

**Returns**

- `leading` (number) - leading scaling value (default=1)

### gui.get_line_break
*Type:* FUNCTION
Returns whether a text node is in line-break mode or not.
This is only useful for text nodes.

**Parameters**

- `node` (node) - node from which to get the line-break for

**Returns**

- `line_break` (boolean) - <code>true</code> or <code>false</code>

### gui.get_material
*Type:* FUNCTION
Returns the material of a node.
The material must be mapped to the gui scene in the gui editor.

**Parameters**

- `node` (node) - node to get the material for

**Returns**

- `materal` (hash) - material id

**Examples**

Getting the material for a node, and assign it to another node:
```
local node1 = gui.get_node("my_node")
local node2 = gui.get_node("other_node")
local node1_material = gui.get_material(node1)
gui.set_material(node2, node1_material)

```

### gui.get_node
*Type:* FUNCTION
Retrieves the node with the specified id.

**Parameters**

- `id` (string | hash) - id of the node to retrieve

**Returns**

- `instance` (node) - a new node instance

**Examples**

Gets a node by id and change its color:
```
local node = gui.get_node("my_node")
local red = vmath.vector4(1.0, 0.0, 0.0, 1.0)
gui.set_color(node, red)

```

### gui.get_outer_bounds
*Type:* FUNCTION
Returns the outer bounds mode for a pie node.

**Parameters**

- `node` (node) - node from where to get the outer bounds mode

**Returns**

- `bounds_mode` (constant) - the outer bounds mode of the pie node:
<ul>
<li><code>gui.PIEBOUNDS_RECTANGLE</code></li>
<li><code>gui.PIEBOUNDS_ELLIPSE</code></li>
</ul>

### gui.get_outline
*Type:* FUNCTION
Returns the outline color of the supplied node.
See gui.get_color for info how vectors encode color values.

**Parameters**

- `node` (node) - node to get the outline color from

**Returns**

- `color` (vector4) - outline color

### gui.get_parent
*Type:* FUNCTION
Returns the parent node of the specified node.
If the supplied node does not have a parent, nil is returned.

**Parameters**

- `node` (node) - the node from which to retrieve its parent

**Returns**

- `parent` (node | nil) - parent instance or <code>nil</code>

### gui.get_particlefx
*Type:* FUNCTION
Get the paricle fx for a gui node

**Parameters**

- `node` (node) - node to get particle fx for

**Returns**

- `particlefx` (hash) - particle fx id

### gui.get_perimeter_vertices
*Type:* FUNCTION
Returns the number of generated vertices around the perimeter
of a pie node.

**Parameters**

- `node` (node) - pie node

**Returns**

- `vertices` (number) - vertex count

### gui.get_pivot
*Type:* FUNCTION
The pivot specifies how the node is drawn and rotated from its position.

**Parameters**

- `node` (node) - node to get pivot from

**Returns**

- `pivot` (constant) - pivot constant
<ul>
  <li><code>gui.PIVOT_CENTER</code></li>
  <li><code>gui.PIVOT_N</code></li>
  <li><code>gui.PIVOT_NE</code></li>
  <li><code>gui.PIVOT_E</code></li>
  <li><code>gui.PIVOT_SE</code></li>
  <li><code>gui.PIVOT_S</code></li>
  <li><code>gui.PIVOT_SW</code></li>
  <li><code>gui.PIVOT_W</code></li>
  <li><code>gui.PIVOT_NW</code></li>
</ul>

### gui.get_position
*Type:* FUNCTION
Returns the position of the supplied node.

**Parameters**

- `node` (node) - node to get the position from

**Returns**

- `position` (vector3) - node position

### gui.get_rotation
*Type:* FUNCTION
Returns the rotation of the supplied node.
The rotation is expressed as a quaternion

**Parameters**

- `node` (node) - node to get the rotation from

**Returns**

- `rotation` (quaternion) - node rotation

### gui.get_scale
*Type:* FUNCTION
Returns the scale of the supplied node.

**Parameters**

- `node` (node) - node to get the scale from

**Returns**

- `scale` (vector3) - node scale

### gui.get_screen_position
*Type:* FUNCTION
Returns the screen position of the supplied node. This function returns the
calculated transformed position of the node, taking into account any parent node
transforms.

**Parameters**

- `node` (node) - node to get the screen position from

**Returns**

- `position` (vector3) - node screen position

### gui.get_shadow
*Type:* FUNCTION
Returns the shadow color of the supplied node.
See gui.get_color for info how vectors encode color values.

**Parameters**

- `node` (node) - node to get the shadow color from

**Returns**

- `color` (vector4) - node shadow color

### gui.get_size
*Type:* FUNCTION
Returns the size of the supplied node.

**Parameters**

- `node` (node) - node to get the size from

**Returns**

- `size` (vector3) - node size

### gui.get_size_mode
*Type:* FUNCTION
Returns the size of a node.
The size mode defines how the node will adjust itself in size. Automatic
size mode alters the node size based on the node's content. Automatic size
mode works for Box nodes and Pie nodes which will both adjust their size
to match the assigned image. Particle fx and Text nodes will ignore
any size mode setting.

**Parameters**

- `node` (node) - node from which to get the size mode (node)

**Returns**

- `size_mode` (constant) - the current size mode
<ul>
<li><code>gui.SIZE_MODE_MANUAL</code></li>
<li><code>gui.SIZE_MODE_AUTO</code></li>
</ul>

### gui.get_slice9
*Type:* FUNCTION
Returns the slice9 configuration values for the node.

**Parameters**

- `node` (node) - node to manipulate

**Returns**

- `values` (vector4) - configuration values

### gui.get_text
*Type:* FUNCTION
Returns the text value of a text node. This is only useful for text nodes.

**Parameters**

- `node` (node) - node from which to get the text

**Returns**

- `text` (string) - text value

### gui.get_texture
*Type:* FUNCTION
Returns the texture of a node.
This is currently only useful for box or pie nodes.
The texture must be mapped to the gui scene in the gui editor.

**Parameters**

- `node` (node) - node to get texture from

**Returns**

- `texture` (hash) - texture id

### gui.get_tracking
*Type:* FUNCTION
Returns the tracking value of a text node.

**Parameters**

- `node` (node) - node from where to get the tracking

**Returns**

- `tracking` (number) - tracking scaling number (default=0)

### gui.get_tree
*Type:* FUNCTION
Get a node and all its children as a Lua table.

**Parameters**

- `node` (node) - root node to get node tree from

**Returns**

- `clones` (table) - a table mapping node ids to the corresponding nodes

### gui.get_type
*Type:* FUNCTION
gets the node type

**Parameters**

- `node` (node) - node from which to get the type

**Returns**

- `type` (constant) - type
<ul>
<li><code>gui.TYPE_BOX</code></li>
<li><code>gui.TYPE_TEXT</code></li>
<li><code>gui.TYPE_PIE</code></li>
<li><code>gui.TYPE_PARTICLEFX</code></li>
<li><code>gui.TYPE_CUSTOM</code></li>
</ul>
- `subtype` (number | nil) - id of the custom type

### gui.get_visible
*Type:* FUNCTION
Returns true if a node is visible and false if it's not.
Invisible nodes are not rendered.

**Parameters**

- `node` (node) - node to query

**Returns**

- `visible` (boolean) - whether the node is visible or not

### gui.get_width
*Type:* FUNCTION
Returns the scene width.

**Returns**

- `width` (number) - scene width

### gui.get_xanchor
*Type:* FUNCTION
The x-anchor specifies how the node is moved when the game is run in a different resolution.

**Parameters**

- `node` (node) - node to get x-anchor from

**Returns**

- `anchor` (constant) - anchor constant
<ul>
<li><code>gui.ANCHOR_NONE</code></li>
<li><code>gui.ANCHOR_LEFT</code></li>
<li><code>gui.ANCHOR_RIGHT</code></li>
</ul>

### gui.get_yanchor
*Type:* FUNCTION
The y-anchor specifies how the node is moved when the game is run in a different resolution.

**Parameters**

- `node` (node) - node to get y-anchor from

**Returns**

- `anchor` (constant) - anchor constant
<ul>
<li><code>gui.ANCHOR_NONE</code></li>
<li><code>gui.ANCHOR_TOP</code></li>
<li><code>gui.ANCHOR_BOTTOM</code></li>
</ul>

### gui.hide_keyboard
*Type:* FUNCTION
Hides the on-display touch keyboard on the device.

### gui.is_enabled
*Type:* FUNCTION
Returns true if a node is enabled and false if it's not.
Disabled nodes are not rendered and animations acting on them are not evaluated.

**Parameters**

- `node` (node) - node to query
- `recursive` (boolean) (optional) - check hierarchy recursively

**Returns**

- `enabled` (boolean) - whether the node is enabled or not

### gui.KEYBOARD_TYPE_DEFAULT
*Type:* CONSTANT
default keyboard

### gui.KEYBOARD_TYPE_EMAIL
*Type:* CONSTANT
email keyboard

### gui.KEYBOARD_TYPE_NUMBER_PAD
*Type:* CONSTANT
number input keyboard

### gui.KEYBOARD_TYPE_PASSWORD
*Type:* CONSTANT
password keyboard

### gui.move_above
*Type:* FUNCTION
Alters the ordering of the two supplied nodes by moving the first node
above the second.
If the second argument is nil the first node is moved to the top.

**Parameters**

- `node` (node) - to move
- `reference` (node | nil) - reference node above which the first node should be moved

### gui.move_below
*Type:* FUNCTION
Alters the ordering of the two supplied nodes by moving the first node
below the second.
If the second argument is nil the first node is moved to the bottom.

**Parameters**

- `node` (node) - to move
- `reference` (node | nil) - reference node below which the first node should be moved

### gui.new_box_node
*Type:* FUNCTION
Dynamically create a new box node.

**Parameters**

- `pos` (vector3 | vector4) - node position
- `size` (vector3) - node size

**Returns**

- `node` (node) - new box node

### gui.new_particlefx_node
*Type:* FUNCTION
Dynamically create a particle fx node.

**Parameters**

- `pos` (vector3 | vector4) - node position
- `particlefx` (hash | string) - particle fx resource name

**Returns**

- `node` (node) - new particle fx node

### gui.new_pie_node
*Type:* FUNCTION
Dynamically create a new pie node.

**Parameters**

- `pos` (vector3 | vector4) - node position
- `size` (vector3) - node size

**Returns**

- `node` (node) - new pie node

### gui.new_text_node
*Type:* FUNCTION
Dynamically create a new text node.

**Parameters**

- `pos` (vector3 | vector4) - node position
- `text` (string) - node text

**Returns**

- `node` (node) - new text node

### gui.new_texture
*Type:* FUNCTION
Dynamically create a new texture.

**Parameters**

- `texture_id` (string | hash) - texture id
- `width` (number) - texture width
- `height` (number) - texture height
- `type` (string | constant) - texture type
<ul>
<li><code>"rgb"</code> - RGB</li></li>
<li><code>"rgba"</code> - RGBA</li></li>
<li><code>"l"</code> - LUMINANCE</li></li>
<li><code>"astc"</code> - ASTC compressed format</li></li>
</ul>
- `buffer` (string) - texture data
- `flip` (boolean) - flip texture vertically

**Returns**

- `success` (boolean) - texture creation was successful
- `code` (number) - one of the gui.RESULT_* codes if unsuccessful

**Examples**

How to create a texture and apply it to a new box node:
```
function init(self)
     local w = 200
     local h = 300

     -- A nice orange. String with the RGB values.
     local orange = string.char(0xff) .. string.char(0x80) .. string.char(0x10)

     -- Create the texture. Repeat the color string for each pixel.
     local ok, reason = gui.new_texture("orange_tx", w, h, "rgb", string.rep(orange, w * h))
     if ok then
         -- Create a box node and apply the texture to it.
         local n = gui.new_box_node(vmath.vector3(200, 200, 0), vmath.vector3(w, h, 0))
         gui.set_texture(n, "orange_tx")
     else
         -- Could not create texture for some reason...
         if reason == gui.RESULT_TEXTURE_ALREADY_EXISTS then
             ...
         else
             ...
         end
     end
end
```How to create a texture using .astc format

```lua
local path = "/assets/images/logo_4x4.astc"
local buffer = sys.load_resource(path)
local n = gui.new_box_node(pos, vmath.vector3(size, size, 0))
-- size is read from the .astc buffer
-- flip is not supported
gui.new_texture(path, 0, 0, "astc", buffer, false)
gui.set_texture(n, path)

```

### gui.pick_node
*Type:* FUNCTION
Tests whether a coordinate is within the bounding box of a
node.

**Parameters**

- `node` (node) - node to be tested for picking
- `x` (number) - x-coordinate (see <a href="#on_input">on_input</a> )
- `y` (number) - y-coordinate (see <a href="#on_input">on_input</a> )

**Returns**

- `pickable` (boolean) - pick result

### gui.PIEBOUNDS_ELLIPSE
*Type:* CONSTANT
elliptical pie node bounds

### gui.PIEBOUNDS_RECTANGLE
*Type:* CONSTANT
rectangular pie node bounds

### gui.PIVOT_CENTER
*Type:* CONSTANT
center pivot

### gui.PIVOT_E
*Type:* CONSTANT
east pivot

### gui.PIVOT_N
*Type:* CONSTANT
north pivot

### gui.PIVOT_NE
*Type:* CONSTANT
north-east pivot

### gui.PIVOT_NW
*Type:* CONSTANT
north-west pivot

### gui.PIVOT_S
*Type:* CONSTANT
south pivot

### gui.PIVOT_SE
*Type:* CONSTANT
south-east pivot

### gui.PIVOT_SW
*Type:* CONSTANT
south-west pivot

### gui.PIVOT_W
*Type:* CONSTANT
west pivot

### gui.play_flipbook
*Type:* FUNCTION
Play flipbook animation on a box or pie node.
The current node texture must contain the animation.
Use this function to set one-frame still images on the node.

**Parameters**

- `node` (node) - node to set animation for
- `animation` (string | hash) - animation id
- `complete_function` (function(self, node)) (optional) - optional function to call when the animation has completed
<dl>
<dt><code>self</code></dt>
<dd>
<span class="type">object</span> The current object.
</dd>
<dt><code>node</code></dt>
<dd>
<span class="type">node</span> The node that is animated.
</dd>
</dl>
- `play_properties` (table) (optional) - optional table with properties
<dl>
<dt><code>offset</code></dt>
<dd><span class="type">number</span> The normalized initial value of the animation cursor when the animation starts playing</dd>
<dt><code>playback_rate</code></dt>
<dd><span class="type">number</span> The rate with which the animation will be played. Must be positive</dd>
</dl>

**Examples**

Set the texture of a node to a flipbook animation from an atlas:
```
local function anim_callback(self, node)
    -- Take action after animation has played.
end

function init(self)
    -- Create a new node and set the texture to a flipbook animation
    local node = gui.get_node("button_node")
    gui.set_texture(node, "gui_sprites")
    gui.play_flipbook(node, "animated_button")
end

```

Set the texture of a node to an image from an atlas:
```
-- Create a new node and set the texture to a "button.png" from atlas
local node = gui.get_node("button_node")
gui.set_texture(node, "gui_sprites")
gui.play_flipbook(node, "button")

```

### gui.play_particlefx
*Type:* FUNCTION
Plays the paricle fx for a gui node

**Parameters**

- `node` (node) - node to play particle fx for
- `emitter_state_function` (function(self, node, emitter, state)) (optional) - optional callback function that will be called when an emitter attached to this particlefx changes state.
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The current object</dd>
<dt><code>node</code></dt>
<dd><span class="type">hash</span> The particle fx node, or <code>nil</code> if the node was deleted</dd>
<dt><code>emitter</code></dt>
<dd><span class="type">hash</span> The id of the emitter</dd>
<dt><code>state</code></dt>
<dd><span class="type">constant</span> the new state of the emitter:</dd>
</dl>
<ul>
<li><code>particlefx.EMITTER_STATE_SLEEPING</code></li>
<li><code>particlefx.EMITTER_STATE_PRESPAWN</code></li>
<li><code>particlefx.EMITTER_STATE_SPAWNING</code></li>
<li><code>particlefx.EMITTER_STATE_POSTSPAWN</code></li>
</ul>

**Examples**

How to play a particle fx when a gui node is created.
The callback receives the gui node, the hash of the id
of the emitter, and the new state of the emitter as particlefx.EMITTER_STATE_.
```
local function emitter_state_change(self, node, emitter, state)
  if emitter == hash("exhaust") and state == particlefx.EMITTER_STATE_POSTSPAWN then
    -- exhaust is done spawning particles...
  end
end

function init(self)
    gui.play_particlefx(gui.get_node("particlefx"), emitter_state_change)
end

```

### gui.PLAYBACK_LOOP_BACKWARD
*Type:* CONSTANT
loop backward

### gui.PLAYBACK_LOOP_FORWARD
*Type:* CONSTANT
loop forward

### gui.PLAYBACK_LOOP_PINGPONG
*Type:* CONSTANT
ping pong loop

### gui.PLAYBACK_ONCE_BACKWARD
*Type:* CONSTANT
once backward

### gui.PLAYBACK_ONCE_FORWARD
*Type:* CONSTANT
once forward

### gui.PLAYBACK_ONCE_PINGPONG
*Type:* CONSTANT
once forward and then backward

### gui.PROP_COLOR
*Type:* CONSTANT
color property

### gui.PROP_EULER
*Type:* CONSTANT
euler property

### gui.PROP_FILL_ANGLE
*Type:* CONSTANT
fill_angle property

### gui.PROP_INNER_RADIUS
*Type:* CONSTANT
inner_radius property

### gui.PROP_LEADING
*Type:* CONSTANT
leading property

### gui.PROP_OUTLINE
*Type:* CONSTANT
outline color property

### gui.PROP_POSITION
*Type:* CONSTANT
position property

### gui.PROP_ROTATION
*Type:* CONSTANT
rotation property

### gui.PROP_SCALE
*Type:* CONSTANT
scale property

### gui.PROP_SHADOW
*Type:* CONSTANT
shadow color property

### gui.PROP_SIZE
*Type:* CONSTANT
size property

### gui.PROP_SLICE9
*Type:* CONSTANT
slice9 property

### gui.PROP_TRACKING
*Type:* CONSTANT
tracking property

### gui.reset_keyboard
*Type:* FUNCTION
Resets the input context of keyboard. This will clear marked text.

### gui.reset_material
*Type:* FUNCTION
Resets the node material to the material assigned in the gui scene.

**Parameters**

- `node` (node) - node to reset the material for

**Examples**

Resetting the material for a node:
```
local node = gui.get_node("my_node")
gui.reset_material(node)

```

### gui.reset_nodes
*Type:* FUNCTION
Resets all nodes in the current GUI scene to their initial state.
The reset only applies to static node loaded from the scene.
Nodes that are created dynamically from script are not affected.

### gui.RESULT_DATA_ERROR
*Type:* CONSTANT
The provided data is not in the expected format or is in some other way
incorrect, for instance the image data provided to gui.new_texture().

### gui.RESULT_OUT_OF_RESOURCES
*Type:* CONSTANT
The system is out of resources, for instance when trying to create a new
texture using gui.new_texture().

### gui.RESULT_TEXTURE_ALREADY_EXISTS
*Type:* CONSTANT
The texture id already exists when trying to use gui.new_texture().

### gui.screen_to_local
*Type:* FUNCTION
Convert the screen position to the local position of supplied node

**Parameters**

- `node` (node) - node used for getting local transformation matrix
- `screen_position` (vector3) - screen position

**Returns**

- `local_position` (vector3) - local position

### gui.set
*Type:* FUNCTION
Instead of using specific setteres such as gui.set_position or gui.set_scale,
you can use gui.set instead and supply the property as a string or a hash.
While this function is similar to go.get and go.set, there are a few more restrictions
when operating in the gui namespace. Most notably, only these named properties identifiers are supported:

"position"
"rotation"
"euler"
"scale"
"color"
"outline"
"shadow"
"size"
"fill_angle" (pie)
"inner_radius" (pie)
"leading" (text)
"tracking" (text)
"slice9" (slice9)

The value to set must either be a vmath.vector4, vmath.vector3, vmath.quat or a single number and depends on the property name you want to set.
I.e when setting the "position" property, you need to use a vmath.vector4 and when setting a single component of the property,
such as "position.x", you need to use a single value.
Note: When setting the rotation using the "rotation" property, you need to pass in a vmath.quat. This behaviour is different than from the gui.set_rotation function,
the intention is to move new functionality closer to go namespace so that migrating between gui and go is easier. To set the rotation using degrees instead,
use the "euler" property instead. The rotation and euler properties are linked, changing one of them will change the backing data of the other.
Similar to go.set, you can also use gui.set for setting material constant values on a node. E.g if a material has specified a constant called tint in
the .material file, you can use gui.set to set the value of that constant by calling gui.set(node, "tint", vmath.vec4(1,0,0,1)), or gui.set(node, "matrix", vmath.matrix4())
if the constant is a matrix. Arrays are also supported by gui.set - to set an array constant, you need to pass in an options table with the 'index' key set.
If the material has a constant array called 'tint_array' specified in the material, you can use gui.set(node, "tint_array", vmath.vec4(1,0,0,1), { index = 4}) to set the fourth array element to a different value.

**Parameters**

- `node` (node | url) - node to set the property for, or msg.url() to the gui itself
- `property` (string | hash | constant) - the property to set
- `value` (number | vector4 | vector3 | quaternion) - the property to set
- `options` (table) (optional) - optional options table (only applicable for material constants)
- <code>index</code> <span class="type">number</span> index into array property (1 based)
- <code>key</code> <span class="type">hash</span> name of internal property

**Examples**

Updates the position property on an existing node:
```
local node = gui.get_node("my_box_node")
local node_position = gui.get(node, "position")
gui.set(node, "position.x", node_position.x + 128)

```

Updates the rotation property on an existing node:
```
local node = gui.get_node("my_box_node")
gui.set(node, "rotation", vmath.quat_rotation_z(math.rad(45)))
-- this is equivalent to:
gui.set(node, "euler.z", 45)
-- or using the entire vector:
gui.set(node, "euler", vmath.vector3(0,0,45))
-- or using the set_rotation
gui.set_rotation(node, vmath.vector3(0,0,45))

```

Sets various material constants for a node:
```
local node = gui.get_node("my_box_node")
gui.set(node, "tint", vmath.vector4(1,0,0,1))
-- matrix4 is also supported
gui.set(node, "light_matrix", vmath.matrix4())
-- update a constant in an array at position 4. the array is specified in the shader as:
-- uniform vec4 tint_array[4]; // lua is 1 based, shader is 0 based
gui.set(node, "tint_array", vmath.vector4(1,0,0,1), { index = 4 })
-- update a matrix constant in an array at position 4. the array is specified in the shader as:
-- uniform mat4 light_matrix_array[4];
gui.set(node, "light_matrix_array", vmath.matrix4(), { index = 4 })
-- update a sub-element in a constant
gui.set(node, "tint.x", 1)
-- update a sub-element in an array constant at position 4
gui.set(node, "tint_array.x", 1, {index = 4})

```

Set a named property
```
function on_message(self, message_id, message, sender)
   if message_id == hash("set_font") then
       gui.set(msg.url(), "fonts", message.font, {key = "my_font_name"})
       gui.set_font(gui.get_node("text"), "my_font_name")
   elseif message_id == hash("set_texture") then
       gui.set(msg.url(), "textures", message.texture, {key = "my_texture"})
       gui.set_texture(gui.get_node("box"), "my_texture")
       gui.play_flipbook(gui.get_node("box"), "logo_256")
   end
end

```

### gui.set_adjust_mode
*Type:* FUNCTION
Sets the adjust mode on a node.
The adjust mode defines how the node will adjust itself to screen
resolutions that differs from the one in the project settings.

**Parameters**

- `node` (node) - node to set adjust mode for
- `adjust_mode` (constant) - adjust mode to set
<ul>
<li><code>gui.ADJUST_FIT</code></li>
<li><code>gui.ADJUST_ZOOM</code></li>
<li><code>gui.ADJUST_STRETCH</code></li>
</ul>

### gui.set_alpha
*Type:* FUNCTION
sets the node alpha

**Parameters**

- `node` (node) - node for which to set alpha
- `alpha` (number) - 0..1 alpha color

### gui.set_blend_mode
*Type:* FUNCTION
Set the blend mode of a node.
Blend mode defines how the node will be blended with the background.

**Parameters**

- `node` (node) - node to set blend mode for
- `blend_mode` (constant) - blend mode to set
<ul>
<li><code>gui.BLEND_ALPHA</code></li>
<li><code>gui.BLEND_ADD</code></li>
<li><code>gui.BLEND_ADD_ALPHA</code></li>
<li><code>gui.BLEND_MULT</code></li>
<li><code>gui.BLEND_SCREEN</code></li>
</ul>

### gui.set_clipping_inverted
*Type:* FUNCTION
If node is set as an inverted clipping node, it will clip anything inside as opposed to outside.

**Parameters**

- `node` (node) - node to set clipping inverted state for
- `inverted` (boolean) - <code>true</code> or <code>false</code>

### gui.set_clipping_mode
*Type:* FUNCTION
Clipping mode defines how the node will clip it's children nodes

**Parameters**

- `node` (node) - node to set clipping mode for
- `clipping_mode` (constant) - clipping mode to set
<ul>
  <li><code>gui.CLIPPING_MODE_NONE</code></li>
  <li><code>gui.CLIPPING_MODE_STENCIL</code></li>
</ul>

### gui.set_clipping_visible
*Type:* FUNCTION
If node is set as an visible clipping node, it will be shown as well as clipping. Otherwise, it will only clip but not show visually.

**Parameters**

- `node` (node) - node to set clipping visibility for
- `visible` (boolean) - <code>true</code> or <code>false</code>

### gui.set_color
*Type:* FUNCTION
Sets the color of the supplied node. The components
of the supplied vector3 or vector4 should contain the color channel values:

Component
Color value

x
Red value

y
Green value

z
Blue value

w vector4
Alpha value

**Parameters**

- `node` (node) - node to set the color for
- `color` (vector3 | vector4) - new color

### gui.set_enabled
*Type:* FUNCTION
Sets a node to the disabled or enabled state.
Disabled nodes are not rendered and animations acting on them are not evaluated.

**Parameters**

- `node` (node) - node to be enabled/disabled
- `enabled` (boolean) - whether the node should be enabled or not

### gui.set_euler
*Type:* FUNCTION
Sets the rotation of the supplied node.
The rotation is expressed in degree Euler angles.

**Parameters**

- `node` (node) - node to set the rotation for
- `rotation` (vector3 | vector4) - new rotation

### gui.set_fill_angle
*Type:* FUNCTION
Set the sector angle of a pie node.

**Parameters**

- `node` (node) - node to set the fill angle for
- `angle` (number) - sector angle

### gui.set_flipbook_cursor
*Type:* FUNCTION
This is only useful nodes with flipbook animations. The cursor is normalized.

**Parameters**

- `node` (node) - node to set the cursor for
- `cursor` (number) - cursor value

### gui.set_flipbook_playback_rate
*Type:* FUNCTION
This is only useful nodes with flipbook animations. Sets the playback rate of the flipbook animation on a node. Must be positive.

**Parameters**

- `node` (node) - node to set the cursor for
- `playback_rate` (number) - playback rate

### gui.set_font
*Type:* FUNCTION
This is only useful for text nodes.
The font must be mapped to the gui scene in the gui editor.

**Parameters**

- `node` (node) - node for which to set the font
- `font` (string | hash) - font id

### gui.set_id
*Type:* FUNCTION
Set the id of the specicied node to a new value.
Nodes created with the gui.new_*_node() functions get
an empty id. This function allows you to give dynamically
created nodes an id.
 No checking is done on the uniqueness of supplied ids.
It is up to you to make sure you use unique ids.

**Parameters**

- `node` (node) - node to set the id for
- `id` (string | hash) - id to set

**Examples**

Create a new node and set its id:
```
local pos = vmath.vector3(100, 100, 0)
local size = vmath.vector3(100, 100, 0)
local node = gui.new_box_node(pos, size)
gui.set_id(node, "my_new_node")

```

### gui.set_inherit_alpha
*Type:* FUNCTION
sets the node inherit alpha state

**Parameters**

- `node` (node) - node from which to set the inherit alpha state
- `inherit_alpha` (boolean) - <code>true</code> or <code>false</code>

### gui.set_inner_radius
*Type:* FUNCTION
Sets the inner radius of a pie node.
The radius is defined along the x-axis.

**Parameters**

- `node` (node) - node to set the inner radius for
- `radius` (number) - inner radius

### gui.set_layer
*Type:* FUNCTION
The layer must be mapped to the gui scene in the gui editor.

**Parameters**

- `node` (node) - node for which to set the layer
- `layer` (string | hash) - layer id

### gui.set_layout
*Type:* FUNCTION
Applies a named layout on the GUI scene. This re-applies per-layout node descriptors
and, if a matching Display Profile exists, updates the scene resolution. Emits
the "layout_changed" message to the scene script when the layout actually changes.

**Parameters**

- `layout` (string | hash) - the layout id to apply

**Returns**

- `return` (boolean) - true if the layout exists in the scene and was applied, false otherwise

### gui.set_leading
*Type:* FUNCTION
Sets the leading value for a text node. This value is used to
scale the line spacing of text.

**Parameters**

- `node` (node) - node for which to set the leading
- `leading` (number) - a scaling value for the line spacing (default=1)

### gui.set_line_break
*Type:* FUNCTION
Sets the line-break mode on a text node.
This is only useful for text nodes.

**Parameters**

- `node` (node) - node to set line-break for
- `line_break` (boolean) - <code>true</code> or <code>false</code>

### gui.set_material
*Type:* FUNCTION
Set the material on a node. The material must be mapped to the gui scene in the gui editor,
and assigning a material is supported for all node types. To set the default material that
is assigned to the gui scene node, use gui.reset_material(node_id) instead.

**Parameters**

- `node` (node) - node to set material for
- `material` (string | hash) - material id

**Examples**

Assign an existing material to a node:
```
local node = gui.get_node("my_node")
gui.set_material(node, "my_material")

```

### gui.set_outer_bounds
*Type:* FUNCTION
Sets the outer bounds mode for a pie node.

**Parameters**

- `node` (node) - node for which to set the outer bounds mode
- `bounds_mode` (constant) - the outer bounds mode of the pie node:
<ul>
<li><code>gui.PIEBOUNDS_RECTANGLE</code></li>
<li><code>gui.PIEBOUNDS_ELLIPSE</code></li>
</ul>

### gui.set_outline
*Type:* FUNCTION
Sets the outline color of the supplied node.
See gui.set_color for info how vectors encode color values.

**Parameters**

- `node` (node) - node to set the outline color for
- `color` (vector3 | vector4) - new outline color

### gui.set_parent
*Type:* FUNCTION
Sets the parent node of the specified node.

**Parameters**

- `node` (node) - node for which to set its parent
- `parent` (node) (optional) - parent node to set, pass <code>nil</code> to remove parent
- `keep_scene_transform` (boolean) (optional) - optional flag to make the scene position being perserved

### gui.set_particlefx
*Type:* FUNCTION
Set the paricle fx for a gui node

**Parameters**

- `node` (node) - node to set particle fx for
- `particlefx` (hash | string) - particle fx id

### gui.set_perimeter_vertices
*Type:* FUNCTION
Sets the number of generated vertices around the perimeter of a pie node.

**Parameters**

- `node` (node) - pie node
- `vertices` (number) - vertex count

### gui.set_pivot
*Type:* FUNCTION
The pivot specifies how the node is drawn and rotated from its position.

**Parameters**

- `node` (node) - node to set pivot for
- `pivot` (constant) - pivot constant
<ul>
  <li><code>gui.PIVOT_CENTER</code></li>
  <li><code>gui.PIVOT_N</code></li>
  <li><code>gui.PIVOT_NE</code></li>
  <li><code>gui.PIVOT_E</code></li>
  <li><code>gui.PIVOT_SE</code></li>
  <li><code>gui.PIVOT_S</code></li>
  <li><code>gui.PIVOT_SW</code></li>
  <li><code>gui.PIVOT_W</code></li>
  <li><code>gui.PIVOT_NW</code></li>
</ul>

### gui.set_position
*Type:* FUNCTION
Sets the position of the supplied node.

**Parameters**

- `node` (node) - node to set the position for
- `position` (vector3 | vector4) - new position

### gui.set_render_order
*Type:* FUNCTION
Set the order number for the current GUI scene.
The number dictates the sorting of the "gui" render predicate,
in other words in which order the scene will be rendered in relation
to other currently rendered GUI scenes.
The number must be in the range 0 to 15.

**Parameters**

- `order` (number) - rendering order (0-15)

### gui.set_rotation
*Type:* FUNCTION
Sets the rotation of the supplied node.
The rotation is expressed as a quaternion

**Parameters**

- `node` (node) - node to set the rotation for
- `rotation` (quaternion | vector4) - new rotation

### gui.set_scale
*Type:* FUNCTION
Sets the scaling of the supplied node.

**Parameters**

- `node` (node) - node to set the scale for
- `scale` (vector3 | vector4) - new scale

### gui.set_screen_position
*Type:* FUNCTION
Set the screen position to the supplied node

**Parameters**

- `node` (node) - node to set the screen position to
- `screen_position` (vector3) - screen position

### gui.set_shadow
*Type:* FUNCTION
Sets the shadow color of the supplied node.
See gui.set_color for info how vectors encode color values.

**Parameters**

- `node` (node) - node to set the shadow color for
- `color` (vector3 | vector4) - new shadow color

### gui.set_size
*Type:* FUNCTION
Sets the size of the supplied node.
 You can only set size on nodes with size mode set to SIZE_MODE_MANUAL

**Parameters**

- `node` (node) - node to set the size for
- `size` (vector3 | vector4) - new size

### gui.set_size_mode
*Type:* FUNCTION
Sets the size mode of a node.
The size mode defines how the node will adjust itself in size. Automatic
size mode alters the node size based on the node's content. Automatic size
mode works for Box nodes and Pie nodes which will both adjust their size
to match the assigned image. Particle fx and Text nodes will ignore
any size mode setting.

**Parameters**

- `node` (node) - node to set size mode for
- `size_mode` (constant) - size mode to set
<ul>
<li><code>gui.SIZE_MODE_MANUAL</code></li>
<li><code>gui.SIZE_MODE_AUTO</code></li>
</ul>

### gui.set_slice9
*Type:* FUNCTION
Set the slice9 configuration values for the node.

**Parameters**

- `node` (node) - node to manipulate
- `values` (vector4) - new values

### gui.set_text
*Type:* FUNCTION
Set the text value of a text node. This is only useful for text nodes.

**Parameters**

- `node` (node) - node to set text for
- `text` (string | number) - text to set

### gui.set_texture
*Type:* FUNCTION
Set the texture on a box or pie node. The texture must be mapped to
the gui scene in the gui editor. The function points out which texture
the node should render from. If the texture is an atlas, further
information is needed to select which image/animation in the atlas
to render. In such cases, use gui.play_flipbook() in
addition to this function.

**Parameters**

- `node` (node) - node to set texture for
- `texture` (string | hash) - texture id

**Examples**

To set a texture (or animation) from an atlas:
```
local node = gui.get_node("box_node")
gui.set_texture(node, "my_atlas")
gui.play_flipbook(node, "image")

```

Set a dynamically created texture to a node. Note that there is only
one texture image in this case so gui.set_texture() is
sufficient.
```
local w = 200
local h = 300
-- A nice orange. String with the RGB values.
local orange = string.char(0xff) .. string.char(0x80) .. string.char(0x10)
-- Create the texture. Repeat the color string for each pixel.
if gui.new_texture("orange_tx", w, h, "rgb", string.rep(orange, w * h)) then
    local node = gui.get_node("box_node")
    gui.set_texture(node, "orange_tx")
end

```

### gui.set_texture_data
*Type:* FUNCTION
Set the texture buffer data for a dynamically created texture.

**Parameters**

- `texture` (string | hash) - texture id
- `width` (number) - texture width
- `height` (number) - texture height
- `type` (string | constant) - texture type
<ul>
  <li><code>"rgb"</code> - RGB</li>
  <li><code>"rgba"</code> - RGBA</li>
  <li><code>"l"</code> - LUMINANCE</li>
  <li><code>"astc"</code> - ASTC compressed format</li>
</ul>
- `buffer` (string) - texture data
- `flip` (boolean) - flip texture vertically

**Returns**

- `success` (boolean) - setting the data was successful

**Examples**

```
function init(self)
     local w = 200
     local h = 300

     -- Create a dynamic texture, all white.
     if gui.new_texture("dynamic_tx", w, h, "rgb", string.rep(string.char(0xff), w * h * 3)) then
         -- Create a box node and apply the texture to it.
         local n = gui.new_box_node(vmath.vector3(200, 200, 0), vmath.vector3(w, h, 0))
         gui.set_texture(n, "dynamic_tx")

         ...

         -- Change the data in the texture to a nice orange.
         local orange = string.char(0xff) .. string.char(0x80) .. string.char(0x10)
         if gui.set_texture_data("dynamic_tx", w, h, "rgb", string.rep(orange, w * h)) then
             -- Go on and to more stuff
             ...
         end
     else
         -- Something went wrong
         ...
     end
end

```

### gui.set_tracking
*Type:* FUNCTION
Sets the tracking value of a text node. This value is used to
adjust the vertical spacing of characters in the text.

**Parameters**

- `node` (node) - node for which to set the tracking
- `tracking` (number) - a scaling number for the letter spacing (default=0)

### gui.set_visible
*Type:* FUNCTION
Set if a node should be visible or not. Only visible nodes are rendered.

**Parameters**

- `node` (node) - node to be visible or not
- `visible` (boolean) - whether the node should be visible or not

### gui.set_xanchor
*Type:* FUNCTION
The x-anchor specifies how the node is moved when the game is run in a different resolution.

**Parameters**

- `node` (node) - node to set x-anchor for
- `anchor` (constant) - anchor constant
<ul>
<li><code>gui.ANCHOR_NONE</code></li>
<li><code>gui.ANCHOR_LEFT</code></li>
<li><code>gui.ANCHOR_RIGHT</code></li>
</ul>

### gui.set_yanchor
*Type:* FUNCTION
The y-anchor specifies how the node is moved when the game is run in a different resolution.

**Parameters**

- `node` (node) - node to set y-anchor for
- `anchor` (constant) - anchor constant
<ul>
<li><code>gui.ANCHOR_NONE</code></li>
<li><code>gui.ANCHOR_TOP</code></li>
<li><code>gui.ANCHOR_BOTTOM</code></li>
</ul>

### gui.show_keyboard
*Type:* FUNCTION
Shows the on-display touch keyboard.
The specified type of keyboard is displayed if it is available on
the device.
This function is only available on iOS and Android.  .

**Parameters**

- `type` (constant) - keyboard type
<ul>
<li><code>gui.KEYBOARD_TYPE_DEFAULT</code></li>
<li><code>gui.KEYBOARD_TYPE_EMAIL</code></li>
<li><code>gui.KEYBOARD_TYPE_NUMBER_PAD</code></li>
<li><code>gui.KEYBOARD_TYPE_PASSWORD</code></li>
</ul>
- `autoclose` (boolean) - if the keyboard should automatically close when clicking outside

### gui.SIZE_MODE_AUTO
*Type:* CONSTANT
The size of the node is determined by the currently assigned texture.

### gui.SIZE_MODE_MANUAL
*Type:* CONSTANT
The size of the node is determined by the size set in the editor, the constructor or by gui.set_size()

### gui.stop_particlefx
*Type:* FUNCTION
Stops the particle fx for a gui node

**Parameters**

- `node` (node) - node to stop particle fx for
- `options` (table) (optional) - options when stopping the particle fx. Supported options:
<ul>
<li><span class="type">boolean</span> <code>clear</code>: instantly clear spawned particles</li>
</ul>

### gui.TYPE_BOX
*Type:* CONSTANT
box type

### gui.TYPE_CUSTOM
*Type:* CONSTANT
custom type

### gui.TYPE_PARTICLEFX
*Type:* CONSTANT
particlefx type

### gui.TYPE_PIE
*Type:* CONSTANT
pie type

### gui.TYPE_TEXT
*Type:* CONSTANT
text type

### init
*Type:* FUNCTION
This is a callback-function, which is called by the engine when a gui component is initialized. It can be used
to set the initial state of the script and gui scene.

**Parameters**

- `self` (userdata) - reference to the script state to be used for storing data

**Examples**

```
function init(self)
    -- set up useful data
    self.my_value = 1
end

```

### layout_changed
*Type:* MESSAGE
This message is broadcast to every GUI component when a layout change has been initiated
on device.

**Parameters**

- `id` (hash) - the id of the layout the engine is changing to
- `previous_id` (hash) - the id of the layout the engine is changing from

**Examples**

```
function on_message(self, message_id, message, sender)
   if message_id == hash("layout_changed") and message.id == hash("Landscape") then
       -- switching layout to "Landscape"...
       ...
   end
end

```

### material
*Type:* PROPERTY
The main material (the default material assigned to a GUI) used when rendering the gui. The type of the property is hash.

**Examples**

How to set material using a script property (see resource.material)
```
go.property("desaturate_material", resource.material("/desaturate.material"))

function init(self)
  go.set("#gui", "material", self.desaturate_material)
end

```

### materials
*Type:* PROPERTY
The materials used when rendering the gui. The type of the property is hash.
Key must be specified in options table.

**Examples**

How to change a named material resource using a script property from a script
```
go.property("my_material", resource.material("/my_material.material"))

function init(self)
  -- this will update the "my_gui_material" entry in the GUI to use the material
  -- specified in the "my_material" script property.
  go.set("#gui", "materials", self.my_material, { key = "my_gui_material" })
end

```

### on_input
*Type:* FUNCTION
This is a callback-function, which is called by the engine when user input is sent to the instance of the gui component.
It can be used to take action on the input, e.g. modify the gui according to the input.
For an instance to obtain user input, it must first acquire input
focus through the message acquire_input_focus.
Any instance that has obtained input will be put on top of an
input stack. Input is sent to all listeners on the stack until the
end of stack is reached, or a listener returns true
to signal that it wants input to be consumed.
See the documentation of acquire_input_focus for more
information.
The action parameter is a table containing data about the input mapped to the
action_id.
For mapped actions it specifies the value of the input and if it was just pressed or released.
Actions are mapped to input in an input_binding-file.
Mouse movement is specifically handled and uses nil as its action_id.
The action only contains positional parameters in this case, such as x and y of the pointer.
Here is a brief description of the available table fields:

Field
Description

value
The amount of input given by the user. This is usually 1 for buttons and 0-1 for analogue inputs. This is not present for mouse movement and text input.

pressed
If the input was pressed this frame. This is not present for mouse movement and text input.

released
If the input was released this frame. This is not present for mouse movement and text input.

repeated
If the input was repeated this frame. This is similar to how a key on a keyboard is repeated when you hold it down. This is not present for mouse movement and text input.

x
The x value of a pointer device, if present. This is not present for gamepad, key and text input.

y
The y value of a pointer device, if present. This is not present for gamepad, key and text input.

screen_x
The screen space x value of a pointer device, if present. This is not present for gamepad, key and text input.

screen_y
The screen space y value of a pointer device, if present. This is not present for gamepad, key and text input.

dx
The change in x value of a pointer device, if present. This is not present for gamepad, key and text input.

dy
The change in y value of a pointer device, if present. This is not present for gamepad, key and text input.

screen_dx
The change in screen space x value of a pointer device, if present. This is not present for gamepad, key and text input.

screen_dy
The change in screen space y value of a pointer device, if present. This is not present for gamepad, key and text input.

gamepad
The index of the gamepad device that provided the input. See table below about gamepad input.

touch
List of touch input, one element per finger, if present. See table below about touch input

text
Text input from a (virtual) keyboard or similar.

marked_text
Sequence of entered symbols while entering a symbol combination, for example Japanese Kana.

Gamepad specific fields:

Field
Description

gamepad
The index of the gamepad device that provided the input.

userid
Id of the user associated with the controller. Usually only relevant on consoles.

gamepad_unknown
True if the inout originated from an unknown/unmapped gamepad.

gamepad_name
Name of the gamepad

gamepad_axis
List of gamepad axis values. For raw gamepad input only.

gamepadhats
List of gamepad hat values. For raw gamepad input only.

gamepad_buttons
List of gamepad button values. For raw gamepad input only.

Touch input table:

Field
Description

id
A number identifying the touch input during its duration.

pressed
True if the finger was pressed this frame.

released
True if the finger was released this frame.

tap_count
Number of taps, one for single, two for double-tap, etc

x
The x touch location.

y
The y touch location.

dx
The change in x value.

dy
The change in y value.

acc_x
Accelerometer x value (if present).

acc_y
Accelerometer y value (if present).

acc_z
Accelerometer z value (if present).

**Parameters**

- `self` (userdata) - reference to the script state to be used for storing data
- `action_id` (hash) - id of the received input action, as mapped in the input_binding-file
- `action` (table) - a table containing the input data, see above for a description

**Returns**

- `consume` (boolean | nil) - optional boolean to signal if the input should be consumed (not passed on to others) or not, default is false

**Examples**

```
function on_input(self, action_id, action)
    -- check for input
    if action_id == hash("my_action") then
        -- take appropritate action
        self.my_value = action.value
    end
    -- consume input
    return true
end

```

### on_message
*Type:* FUNCTION
This is a callback-function, which is called by the engine whenever a message has been sent to the gui component.
It can be used to take action on the message, e.g. update the gui or send a response back to the sender of the message.
The message parameter is a table containing the message data. If the message is sent from the engine, the
documentation of the message specifies which data is supplied.
See the update function for examples on how to use this callback-function.

**Parameters**

- `self` (userdata) - reference to the script state to be used for storing data
- `message_id` (hash) - id of the received message
- `message` (table) - a table containing the message data

### on_reload
*Type:* FUNCTION
This is a callback-function, which is called by the engine when the gui script is reloaded, e.g. from the editor.
It can be used for live development, e.g. to tweak constants or set up the state properly for the script.

**Parameters**

- `self` (userdata) - reference to the script state to be used for storing data

**Examples**

```
function on_reload(self)
    -- restore some color (or similar)
    gui.set_color(gui.get_node("my_node"), self.my_original_color)
end

```

### textures
*Type:* PROPERTY
The textures used in the gui. The type of the property is hash.
Key must be specified in options table.

**Examples**

How to set texture using a script property (see resource.atlas)
```
go.property("cards_red", resource.atlas("/cards_red.atlas"))
go.property("cards_blue", resource.atlas("/cards_blue.atlas"))

function init(self)
  go.set("#gui", "textures", self.cards_red, {key = "cards"})
end

```

### update
*Type:* FUNCTION
This is a callback-function, which is called by the engine every frame to update the state of a gui component.
It can be used to perform any kind of gui related tasks, e.g. animating nodes.

**Parameters**

- `self` (userdata) - reference to the script state to be used for storing data
- `dt` (number) - the time-step of the frame update

**Examples**

This example demonstrates how to update a text node that displays game score in a counting fashion.
It is assumed that the gui component receives messages from the game when a new score is to be shown.
```
function init(self)
    -- fetch the score text node for later use (assumes it is called "score")
    self.score_node = gui.get_node("score")
    -- keep track of the current score counted up so far
    self.current_score = 0
    -- keep track of the target score we should count up to
    self.target_score = 0
    -- how fast we will update the score, in score/second
    self.score_update_speed = 1
end

function update(self, dt)
    -- check if target score is more than current score
    if self.current_score  self.target_score then
            self.current_score = self.target_score
        end
        -- update the score text node
        gui.set_text(self.score_node, "" .. math.floor(self.current_score))
    end
end

function on_message(self, message_id, message, sender)
    -- check the message
    if message_id == hash("set_score") then
        self.target_score = message.score
    end
end

```
