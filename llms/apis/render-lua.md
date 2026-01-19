# Render

**Namespace:** `render`
**Language:** Lua
**Type:** Defold Lua
**File:** `render_ddf.proto`
**Source:** `engine/render/proto/render/render_ddf.proto`

Rendering API documentation

## API

### clear_color
*Type:* MESSAGE
Set render clear color. This is the color that appears on the screen where nothing is rendered, i.e. background.

**Parameters**

- `color` (vector4) - color to use as clear color

**Examples**

```
msg.post("@render:", "clear_color", { color = vmath.vector4(1, 0, 0, 0) } )

```

### constant_buffer
*Type:* TYPEDEF
Constant buffer

**Parameters**

- `value` (userdata)

### draw_debug_text
*Type:* MESSAGE
Draw a text on the screen. This should be used for debugging purposes only.

**Parameters**

- `position` (vector3) - position of the text
- `text` (string) - the text to draw
- `color` (vector4) - color of the text

**Examples**

```
msg.post("@render:", "draw_debug_text", { text = "Hello world!", position = vmath.vector3(200, 200, 0), color = vmath.vector4(1, 0, 0, 1) } )

```

### draw_line
*Type:* MESSAGE
Draw a line on the screen. This should mostly be used for debugging purposes.

**Parameters**

- `start_point` (vector3) - start point of the line
- `end_point` (vector3) - end point of the line
- `color` (vector4) - color of the line

**Examples**

```
-- draw a white line from (200, 200) to (200, 300)
msg.post("@render:", "draw_line", { start_point = vmath.vector3(200, 200, 0), end_point = vmath.vector3(200, 300, 0), color = vmath.vector4(1, 1, 1, 1) } )

```

### render.clear
*Type:* FUNCTION
Clear buffers in the currently enabled render target with specified value. If the render target has been created with multiple
color attachments, all buffers will be cleared with the same value.

**Parameters**

- `buffers` (table) - table with keys specifying which buffers to clear and values set to clear values. Available keys are:
<ul>
<li><code>graphics.BUFFER_TYPE_COLOR0_BIT</code></li>
<li><code>graphics.BUFFER_TYPE_DEPTH_BIT</code></li>
<li><code>graphics.BUFFER_TYPE_STENCIL_BIT</code></li>
</ul>

**Examples**

Clear the color buffer and the depth buffer.
```
render.clear({[graphics.BUFFER_TYPE_COLOR0_BIT] = vmath.vector4(0, 0, 0, 0), [graphics.BUFFER_TYPE_DEPTH_BIT] = 1})

```

### render.constant_buffer
*Type:* FUNCTION
Constant buffers are used to set shader program variables and are optionally passed to the render.draw() function.
The buffer's constant elements can be indexed like an ordinary Lua table, but you can't iterate over them with pairs() or ipairs().

**Returns**

- `buffer` (constant_buffer) - new constant buffer

**Examples**

Set a "tint" constant in a constant buffer in the render script:
```
local constants = render.constant_buffer()
constants.tint = vmath.vector4(1, 1, 1, 1)

```

Then use the constant buffer when drawing a predicate:
```
render.draw(self.my_pred, {constants = constants})

```

The constant buffer also supports array values by specifying constants in a table:
```
local constants = render.constant_buffer()
constants.light_colors    = {}
constants.light_colors[1] = vmath.vector4(1, 0, 0, 1)
constants.light_colors[2] = vmath.vector4(0, 1, 0, 1)
constants.light_colors[3] = vmath.vector4(0, 0, 1, 1)

```

You can also create the table by passing the vectors directly when creating the table:
```
local constants = render.constant_buffer()
constants.light_colors    = {
     vmath.vector4(1, 0, 0, 1)
     vmath.vector4(0, 1, 0, 1)
     vmath.vector4(0, 0, 1, 1)
}

-- Add more constant to the array
constants.light_colors[4] = vmath.vector4(1, 1, 1, 1)

```

### render.delete_render_target
*Type:* FUNCTION
Deletes a render target created by a render script.
You cannot delete a render target resource.

**Parameters**

- `render_target` (render_target) - render target to delete

**Examples**

How to delete a render target:
```
 render.delete_render_target(self.my_render_target)

```

### render.disable_material
*Type:* FUNCTION
If a material is currently enabled, disable it.
The name of the material must be specified in the ".render" resource set
in the "game.project" setting.

**Examples**

Enable material named "glow", then draw my_pred with it.
```
render.enable_material("glow")
render.draw(self.my_pred)
render.disable_material()

```

### render.disable_state
*Type:* FUNCTION
Disables a render state.

**Parameters**

- `state` (constant) - state to disable
<ul>
<li><code>graphics.STATE_DEPTH_TEST</code></li>
<li><code>graphics.STATE_STENCIL_TEST</code></li>
<li><code>graphics.STATE_BLEND</code></li>
<li><code>graphics.STATE_ALPHA_TEST</code> (<span class="icon-ios"></span><span class="icon-android"></span> not available on iOS and Android)</li>
<li><code>graphics.STATE_CULL_FACE</code></li>
<li><code>graphics.STATE_POLYGON_OFFSET_FILL</code></li>
</ul>

**Examples**

Disable face culling when drawing the tile predicate:
```
render.disable_state(graphics.STATE_CULL_FACE)
render.draw(self.tile_pred)

```

### render.disable_texture
*Type:* FUNCTION
Disables a texture that has previourly been enabled.

**Parameters**

- `binding` (texture | string | hash) - texture binding, either by texture unit, string or hash that should be disabled

**Examples**

```
function update(self, dt)
    render.enable_texture(0, self.my_render_target, graphics.BUFFER_TYPE_COLOR0_BIT)
    -- draw a predicate with the render target available as texture 0 in the predicate
    -- material shader.
    render.draw(self.my_pred)
    -- done, disable the texture
    render.disable_texture(0)
end

```

### render.dispatch_compute
*Type:* FUNCTION
Dispatches the currently enabled compute program. The dispatch call takes three arguments x,y,z which constitutes
the 'global working group' of the compute dispatch. Together with the 'local working group' specified in the compute shader
as a layout qualifier, these two sets of parameters forms the number of invocations the compute shader will execute.
An optional constant buffer can be provided to override the default constants. If no constants buffer is provided, a default
system constants buffer is used containing constants as defined in the compute program.

**Parameters**

- `x` (number) - global work group size X
- `y` (number) - global work group size Y
- `z` (number) - global work group size Z
- `options` (table) (optional) - optional table with properties:
<dl>
<dt><code>constants</code></dt>
<dd><span class="type">constant_buffer</span> optional constants to use while rendering</dd>
</dl>

**Examples**

```
function init(self)
    local color_params = { format = graphics.TEXTURE_FORMAT_RGBA,
                           width = render.get_window_width(),
                           height = render.get_window_height()}
    self.scene_rt = render.render_target({[graphics.BUFFER_TYPE_COLOR0_BIT] = color_params})
end

function update(self, dt)
    render.set_compute("bloom")
    render.enable_texture(0, self.backing_texture)
    render.enable_texture(1, self.scene_rt)
    render.dispatch_compute(128, 128, 1)
    render.set_compute()
end

```

Dispatch a compute program with a constant buffer:
```
local constants = render.constant_buffer()
constants.tint = vmath.vector4(1, 1, 1, 1)
render.dispatch_compute(32, 32, 32, {constants = constants})

```

### render.draw
*Type:* FUNCTION
Draws all objects that match a specified predicate. An optional constant buffer can be
provided to override the default constants. If no constants buffer is provided, a default
system constants buffer is used containing constants as defined in materials and set through
go.set (or particlefx.set_constant) on visual components.

**Parameters**

- `predicate` (number) - predicate to draw for
- `options` (table) (optional) - optional table with properties:
<dl>
<dt><code>frustum</code></dt>
<dd><span class="type">matrix4</span> A frustum matrix used to cull renderable items. (E.g. <code>local frustum = proj * view</code>). default=nil</dd>
<dt><code>frustum_planes</code></dt>
<dd><span class="type">int</span> Determines which sides of the frustum will be used. Default is render.FRUSTUM_PLANES_SIDES.</dd>
</dl>
<ul>
<li>render.FRUSTUM_PLANES_SIDES : The left, right, top and bottom sides of the frustum.</li>
<li>render.FRUSTUM_PLANES_ALL : All 6 sides of the frustum.</li>
</ul>
<dl>
<dt><code>constants</code></dt>
<dd><span class="type">constant_buffer</span> optional constants to use while rendering</dd>
<dt><code>sort_order</code></dt>
<dd><span class="type">int</span> How to sort draw order for world-ordered entries. Default uses the renderer's preferred world sorting (back-to-front).</dd>
</dl>

**Examples**

```
function init(self)
    -- define a predicate matching anything with material tag "my_tag"
    self.my_pred = render.predicate({hash("my_tag")})
end

function update(self, dt)
    -- draw everything in the my_pred predicate
    render.draw(self.my_pred)
end

```

Draw predicate with constants:
```
local constants = render.constant_buffer()
constants.tint = vmath.vector4(1, 1, 1, 1)
render.draw(self.my_pred, {constants = constants})

```

Draw with predicate and frustum culling (without near+far planes):
```
local frustum = self.proj * self.view
render.draw(self.my_pred, {frustum = frustum})

```

Draw with predicate and frustum culling (with near+far planes):
```
local frustum = self.proj * self.view
render.draw(self.my_pred, {frustum = frustum, frustum_planes = render.FRUSTUM_PLANES_ALL})

```

### render.draw_debug3d
*Type:* FUNCTION
Draws all 3d debug graphics such as lines drawn with "draw_line" messages and physics visualization.

**Parameters**

- `options` (table) (optional) - optional table with properties:
<dl>
<dt><code>frustum</code></dt>
<dd><span class="type">matrix4</span> A frustum matrix used to cull renderable items. (E.g. <code>local frustum = proj * view</code>). May be nil.</dd>
<dt><code>frustum_planes</code></dt>
<dd><span class="type">int</span> Determines which sides of the frustum will be used. Default is render.FRUSTUM_PLANES_SIDES.</dd>
</dl>
<ul>
<li>render.FRUSTUM_PLANES_SIDES : The left, right, top and bottom sides of the frustum.</li>
<li>render.FRUSTUM_PLANES_ALL : All sides of the frustum.</li>
</ul>

**Replaces:** render.draw_debug2d

**Examples**

```
function update(self, dt)
    -- draw debug visualization
    render.draw_debug3d()
end

```

### render.enable_material
*Type:* FUNCTION
If another material was already enabled, it will be automatically disabled
and the specified material is used instead.
The name of the material must be specified in the ".render" resource set
in the "game.project" setting.

**Parameters**

- `material_id` (string | hash) - material id to enable

**Examples**

Enable material named "glow", then draw my_pred with it.
```
render.enable_material("glow")
render.draw(self.my_pred)
render.disable_material()

```

### render.enable_state
*Type:* FUNCTION
Enables a particular render state. The state will be enabled until disabled.

**Parameters**

- `state` (constant) - state to enable
<ul>
<li><code>graphics.STATE_DEPTH_TEST</code></li>
<li><code>graphics.STATE_STENCIL_TEST</code></li>
<li><code>graphics.STATE_BLEND</code></li>
<li><code>graphics.STATE_ALPHA_TEST</code> (<span class="icon-ios"></span><span class="icon-android"></span> not available on iOS and Android)</li>
<li><code>graphics.STATE_CULL_FACE</code></li>
<li><code>graphics.STATE_POLYGON_OFFSET_FILL</code></li>
</ul>

**Examples**

Enable stencil test when drawing the gui predicate, then disable it:
```
render.enable_state(graphics.STATE_STENCIL_TEST)
render.draw(self.gui_pred)
render.disable_state(graphics.STATE_STENCIL_TEST)

```

### render.enable_texture
*Type:* FUNCTION
Sets the specified texture handle for a render target attachment or a regular texture
that should be used for rendering. The texture can be bound to either a texture unit
or to a sampler name by a hash or a string.
A texture can be bound to multiple units and sampler names at the same time,
the actual binding will be applied to the shaders when a shader program is bound.
When mixing binding using both units and sampler names, you might end up in situations
where two different textures will be applied to the same bind location in the shader.
In this case, the texture set to the named sampler will take precedence over the unit.
Note that you can bind multiple sampler names to the same texture, in case you want to reuse
the same texture for differnt use-cases. It is however recommended that you use the same name
everywhere for the textures that should be shared across different materials.

**Parameters**

- `binding` (number | string | hash) - texture binding, either by texture unit, string or hash for the sampler name that the texture should be bound to
- `handle_or_name` (texture | string | hash) - render target or texture handle that should be bound, or a named resource in the "Render Resource" table in the currently assigned .render file
- `buffer_type` (type:graphics.BUFFER_TYPE_COLOR0_BIT | graphics.BUFFER_TYPE_COLOR1_BIT | graphics.BUFFER_TYPE_COLOR2_BIT | graphics.BUFFER_TYPE_COLOR3_BIT | graphics.BUFFER_TYPE_DEPTH_BIT | graphics.BUFFER_TYPE_STENCIL_BIT) (optional) - optional buffer type from which to enable the texture. Note that this argument only applies to render targets. Defaults to <code>graphics.BUFFER_TYPE_COLOR0_BIT</code>. These values are supported:
<ul>
<li><code>graphics.BUFFER_TYPE_COLOR0_BIT</code></li>
</ul>
If The render target has been created as depth and/or stencil textures, these buffer types can be used:
<ul>
<li><code>graphics.BUFFER_TYPE_DEPTH_BIT</code></li>
<li><code>graphics.BUFFER_TYPE_STENCIL_BIT</code></li>
</ul>
If the render target has been created with multiple color attachments, these buffer types can be used
to enable those textures as well. Currently 4 color attachments are supported:
<ul>
<li><code>graphics.BUFFER_TYPE_COLOR0_BIT</code></li>
<li><code>graphics.BUFFER_TYPE_COLOR1_BIT</code></li>
<li><code>graphics.BUFFER_TYPE_COLOR2_BIT</code></li>
<li><code>graphics.BUFFER_TYPE_COLOR3_BIT</code></li>
</ul>

**Examples**

```
function update(self, dt)
    -- enable target so all drawing is done to it
    render.set_render_target(self.my_render_target)

    -- draw a predicate to the render target
    render.draw(self.my_pred)

    -- disable target
    render.set_render_target(render.RENDER_TARGET_DEFAULT)

    render.enable_texture(0, self.my_render_target, graphics.BUFFER_TYPE_COLOR0_BIT)
    -- draw a predicate with the render target available as texture 0 in the predicate
    -- material shader.
    render.draw(self.my_pred)
end

```

```
function update(self, dt)
    -- enable render target by resource id
    render.set_render_target('my_rt_resource')
    render.draw(self.my_pred)
    render.set_render_target(render.RENDER_TARGET_DEFAULT)

    render.enable_texture(0, 'my_rt_resource', graphics.BUFFER_TYPE_COLOR0_BIT)
    -- draw a predicate with the render target available as texture 0 in the predicate
    -- material shader.
    render.draw(self.my_pred)
end

```

```
function update(self, dt)
    -- bind a texture to the texture unit 0
    render.enable_texture(0, self.my_texture_handle)
    -- bind the same texture to a named sampler
    render.enable_texture("my_texture_sampler", self.my_texture_handle)
end

```

### render.FRUSTUM_PLANES_ALL
*Type:* CONSTANT

### render.FRUSTUM_PLANES_SIDES
*Type:* CONSTANT

### render.get_height
*Type:* FUNCTION
Returns the logical window height that is set in the "game.project" settings.
Note that the actual window pixel size can change, either by device constraints
or user input.

**Returns**

- `height` (number) - specified window height

**Examples**

Get the height of the window
```
local h = render.get_height()

```

### render.get_render_target_height
*Type:* FUNCTION
Returns the specified buffer height from a render target.

**Parameters**

- `render_target` (render_target) - render target from which to retrieve the buffer height
- `buffer_type` (graphics.BUFFER_TYPE_COLOR0_BIT | graphics.BUFFER_TYPE_COLOR1_BIT | graphics.BUFFER_TYPE_COLOR2_BIT | graphics.BUFFER_TYPE_COLOR3_BIT | graphics.BUFFER_TYPE_DEPTH_BIT | graphics.BUFFER_TYPE_STENCIL_BIT) - which type of buffer to retrieve the height from
<ul>
<li><code>graphics.BUFFER_TYPE_COLOR0_BIT</code></li>
<li><code>graphics.BUFFER_TYPE_DEPTH_BIT</code></li>
<li><code>graphics.BUFFER_TYPE_STENCIL_BIT</code></li>
</ul>

**Returns**

- `height` (number) - the height of the render target buffer texture

**Examples**

```
-- get the height of the render target color buffer
local h = render.get_render_target_height(self.target_right, graphics.BUFFER_TYPE_COLOR0_BIT)
-- get the height of a render target resource
local w = render.get_render_target_height('my_rt_resource', graphics.BUFFER_TYPE_COLOR0_BIT)

```

### render.get_render_target_width
*Type:* FUNCTION
Returns the specified buffer width from a render target.

**Parameters**

- `render_target` (render_target) - render target from which to retrieve the buffer width
- `buffer_type` (graphics.BUFFER_TYPE_COLOR0_BIT | graphics.BUFFER_TYPE_COLOR1_BIT | graphics.BUFFER_TYPE_COLOR2_BIT | graphics.BUFFER_TYPE_COLOR3_BIT | graphics.BUFFER_TYPE_DEPTH_BIT | graphics.BUFFER_TYPE_STENCIL_BIT) - which type of buffer to retrieve the width from
<ul>
<li><code>graphics.BUFFER_TYPE_COLOR0_BIT</code></li>
<li><code>graphics.BUFFER_TYPE_COLOR[x]_BIT</code> (x: [0..3], if supported!)</li>
<li><code>graphics.BUFFER_TYPE_DEPTH_BIT</code></li>
<li><code>graphics.BUFFER_TYPE_STENCIL_BIT</code></li>
</ul>

**Returns**

- `width` (number) - the width of the render target buffer texture

**Examples**

```
-- get the width of the render target color buffer
local w = render.get_render_target_width(self.target_right, graphics.BUFFER_TYPE_COLOR0_BIT)
-- get the width of a render target resource
local w = render.get_render_target_width('my_rt_resource', graphics.BUFFER_TYPE_COLOR0_BIT)

```

### render.get_width
*Type:* FUNCTION
Returns the logical window width that is set in the "game.project" settings.
Note that the actual window pixel size can change, either by device constraints
or user input.

**Returns**

- `width` (number) - specified window width (number)

**Examples**

Get the width of the window.
```
local w = render.get_width()

```

### render.get_window_height
*Type:* FUNCTION
Returns the actual physical window height.
Note that this value might differ from the logical height that is set in the
"game.project" settings.

**Returns**

- `height` (number) - actual window height

**Examples**

Get the actual height of the window
```
local h = render.get_window_height()

```

### render.get_window_width
*Type:* FUNCTION
Returns the actual physical window width.
Note that this value might differ from the logical width that is set in the
"game.project" settings.

**Returns**

- `width` (number) - actual window width

**Examples**

Get the actual width of the window
```
local w = render.get_window_width()

```

### render.predicate
*Type:* FUNCTION
This function returns a new render predicate for objects with materials matching
the provided material tags. The provided tags are combined into a bit mask
for the predicate. If multiple tags are provided, the predicate matches materials
with all tags ANDed together.
The current limit to the number of tags that can be defined is 64.

**Parameters**

- `tags` (table) - table of tags that the predicate should match. The tags can be of either hash or string type

**Returns**

- `predicate` (number) - new predicate

**Examples**

Create a new render predicate containing all visual objects that
have a material with material tags "opaque" AND "smoke".
```
local p = render.predicate({hash("opaque"), hash("smoke")})

```

### render.render_target
*Type:* FUNCTION
Creates a new render target according to the supplied
specification table.
The table should contain keys specifying which buffers should be created
with what parameters. Each buffer key should have a table value consisting
of parameters. The following parameter keys are available:

Key
Values

format
graphics.TEXTURE_FORMAT_LUMINANCEgraphics.TEXTURE_FORMAT_RGBgraphics.TEXTURE_FORMAT_RGBAgraphics.TEXTURE_FORMAT_DEPTHgraphics.TEXTURE_FORMAT_STENCILgraphics.TEXTURE_FORMAT_RGBA32Fgraphics.TEXTURE_FORMAT_RGBA16F

width
number

height
number

min_filter (optional)
graphics.TEXTURE_FILTER_LINEARgraphics.TEXTURE_FILTER_NEAREST

mag_filter (optional)
graphics.TEXTURE_FILTER_LINEARgraphics.TEXTURE_FILTER_NEAREST

u_wrap     (optional)
graphics.TEXTURE_WRAP_CLAMP_TO_BORDERgraphics.TEXTURE_WRAP_CLAMP_TO_EDGEgraphics.TEXTURE_WRAP_MIRRORED_REPEATgraphics.TEXTURE_WRAP_REPEAT

v_wrap     (optional)
graphics.TEXTURE_WRAP_CLAMP_TO_BORDERgraphics.TEXTURE_WRAP_CLAMP_TO_EDGEgraphics.TEXTURE_WRAP_MIRRORED_REPEATgraphics.TEXTURE_WRAP_REPEAT

flags      (optional)
render.TEXTURE_BIT (only applicable to depth and stencil buffers)

The render target can be created to support multiple color attachments. Each attachment can have different format settings and texture filters,
but attachments must be added in sequence, meaning you cannot create a render target at slot 0 and 3.
Instead it has to be created with all four buffer types ranging from [0..3] (as denoted by graphics.BUFFER_TYPE_COLORX_BIT where 'X' is the attachment you want to create).
It is not guaranteed that the device running the script can support creating render targets with multiple color attachments. To check if the device can support multiple attachments,
you can check if the render table contains any of the BUFFER_TYPE_COLOR1_BIT, BUFFER_TYPE_COLOR2_BIT or BUFFER_TYPE_COLOR3_BIT constants:
```
function init(self)
    if graphics.BUFFER_TYPE_COLOR1_BIT == nil then
        -- this devices does not support multiple color attachments
    end
end

```

**Parameters**

- `name` (string) - render target name
- `parameters` (table) - table of buffer parameters, see the description for available keys and values

**Returns**

- `render_target` (render_target) - new render target

**Examples**

How to create a new render target and draw to it:
```
function init(self)
    -- render target buffer parameters
    local color_params = { format = graphics.TEXTURE_FORMAT_RGBA,
                           width = render.get_window_width(),
                           height = render.get_window_height(),
                           min_filter = graphics.TEXTURE_FILTER_LINEAR,
                           mag_filter = graphics.TEXTURE_FILTER_LINEAR,
                           u_wrap = graphics.TEXTURE_WRAP_CLAMP_TO_EDGE,
                           v_wrap = graphics.TEXTURE_WRAP_CLAMP_TO_EDGE }
    local depth_params = { format = graphics.TEXTURE_FORMAT_DEPTH,
                           width = render.get_window_width(),
                           height = render.get_window_height(),
                           u_wrap = graphics.TEXTURE_WRAP_CLAMP_TO_EDGE,
                           v_wrap = graphics.TEXTURE_WRAP_CLAMP_TO_EDGE }
    self.my_render_target = render.render_target({[graphics.BUFFER_TYPE_COLOR0_BIT] = color_params, [graphics.BUFFER_TYPE_DEPTH_BIT] = depth_params })
end

function update(self, dt)
    -- enable target so all drawing is done to it
    render.set_render_target(self.my_render_target)

    -- draw a predicate to the render target
    render.draw(self.my_pred)
end

```

How to create a render target with multiple outputs:
```
function init(self)
    -- render target buffer parameters
    local color_params_rgba = { format = graphics.TEXTURE_FORMAT_RGBA,
                                width = render.get_window_width(),
                                height = render.get_window_height(),
                                min_filter = graphics.TEXTURE_FILTER_LINEAR,
                                mag_filter = graphics.TEXTURE_FILTER_LINEAR,
                                u_wrap = graphics.TEXTURE_WRAP_CLAMP_TO_EDGE,
                                v_wrap = graphics.TEXTURE_WRAP_CLAMP_TO_EDGE }
    local color_params_float = { format = graphics.TEXTURE_FORMAT_RG32F,
                           width = render.get_window_width(),
                           height = render.get_window_height(),
                           min_filter = graphics.TEXTURE_FILTER_LINEAR,
                           mag_filter = graphics.TEXTURE_FILTER_LINEAR,
                           u_wrap = graphics.TEXTURE_WRAP_CLAMP_TO_EDGE,
                           v_wrap = graphics.TEXTURE_WRAP_CLAMP_TO_EDGE }

    -- Create a render target with three color attachments
    -- Note: No depth buffer is attached here
    self.my_render_target = render.render_target({
           [graphics.BUFFER_TYPE_COLOR0_BIT] = color_params_rgba,
           [graphics.BUFFER_TYPE_COLOR1_BIT] = color_params_rgba,
           [graphics.BUFFER_TYPE_COLOR2_BIT] = color_params_float, })
end

function update(self, dt)
    -- enable target so all drawing is done to it
    render.enable_render_target(self.my_render_target)

    -- draw a predicate to the render target
    render.draw(self.my_pred)
end

```

### render.RENDER_TARGET_DEFAULT
*Type:* CONSTANT

### render.set_blend_func
*Type:* FUNCTION
Specifies the arithmetic used when computing pixel values that are written to the frame
buffer. In RGBA mode, pixels can be drawn using a function that blends the source RGBA
pixel values with the destination pixel values already in the frame buffer.
Blending is initially disabled.
source_factor specifies which method is used to scale the source color components.
destination_factor specifies which method is used to scale the destination color
components.
Source color components are referred to as (Rs,Gs,Bs,As).
Destination color components are referred to as (Rd,Gd,Bd,Ad).
The color specified by setting the blendcolor is referred to as (Rc,Gc,Bc,Ac).
The source scale factor is referred to as (sR,sG,sB,sA).
The destination scale factor is referred to as (dR,dG,dB,dA).
The color values have integer values between 0 and (kR,kG,kB,kA), where kc = 2mc - 1 and mc is the number of bitplanes for that color. I.e for 8 bit color depth, color values are between 0 and 255.
Available factor constants and corresponding scale factors:

Factor constant
Scale factor (fR,fG,fB,fA)

graphics.BLEND_FACTOR_ZERO
(0,0,0,0)

graphics.BLEND_FACTOR_ONE
(1,1,1,1)

graphics.BLEND_FACTOR_SRC_COLOR
(Rs/kR,Gs/kG,Bs/kB,As/kA)

graphics.BLEND_FACTOR_ONE_MINUS_SRC_COLOR
(1,1,1,1) - (Rs/kR,Gs/kG,Bs/kB,As/kA)

graphics.BLEND_FACTOR_DST_COLOR
(Rd/kR,Gd/kG,Bd/kB,Ad/kA)

graphics.BLEND_FACTOR_ONE_MINUS_DST_COLOR
(1,1,1,1) - (Rd/kR,Gd/kG,Bd/kB,Ad/kA)

graphics.BLEND_FACTOR_SRC_ALPHA
(As/kA,As/kA,As/kA,As/kA)

graphics.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA
(1,1,1,1) - (As/kA,As/kA,As/kA,As/kA)

graphics.BLEND_FACTOR_DST_ALPHA
(Ad/kA,Ad/kA,Ad/kA,Ad/kA)

graphics.BLEND_FACTOR_ONE_MINUS_DST_ALPHA
(1,1,1,1) - (Ad/kA,Ad/kA,Ad/kA,Ad/kA)

graphics.BLEND_FACTOR_CONSTANT_COLOR
(Rc,Gc,Bc,Ac)

graphics.BLEND_FACTOR_ONE_MINUS_CONSTANT_COLOR
(1,1,1,1) - (Rc,Gc,Bc,Ac)

graphics.BLEND_FACTOR_CONSTANT_ALPHA
(Ac,Ac,Ac,Ac)

graphics.BLEND_FACTOR_ONE_MINUS_CONSTANT_ALPHA
(1,1,1,1) - (Ac,Ac,Ac,Ac)

graphics.BLEND_FACTOR_SRC_ALPHA_SATURATE
(i,i,i,1) where i = min(As, kA - Ad) /kA

The blended RGBA values of a pixel comes from the following equations:

Rd = min(kR, Rs * sR + Rd * dR)
Gd = min(kG, Gs * sG + Gd * dG)
Bd = min(kB, Bs * sB + Bd * dB)
Ad = min(kA, As * sA + Ad * dA)

Blend function (graphics.BLEND_FACTOR_SRC_ALPHA, graphics.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA) is useful for
drawing with transparency when the drawn objects are sorted from farthest to nearest.
It is also useful for drawing antialiased points and lines in arbitrary order.

**Parameters**

- `source_factor` (number) - source factor
- `destination_factor` (number) - destination factor

**Examples**

Set the blend func to the most common one:
```
render.set_blend_func(graphics.BLEND_FACTOR_SRC_ALPHA, graphics.BLEND_FACTOR_ONE_MINUS_SRC_ALPHA)

```

### render.set_camera
*Type:* FUNCTION
Sets the current render camera to be used for rendering. If a render camera
has been set by the render script, the renderer will be using its projection and view matrix
during rendering. If a projection and/or view matrix has been set by the render script,
they will not be used until the current render camera has been reset by calling render.set_camera().
If the 'use_frustum' flag in the options table has been set to true, the renderer will automatically use the
camera frustum for frustum culling regardless of what frustum is being passed into the render.draw() function.
Note that the frustum plane option in render.draw can still be used together with the camera.

**Parameters**

- `camera` (url | number | nil) - camera id to use, or nil to reset
- `options` (table) (optional) - optional table with properties:
<dl>
<dt><code>use_frustum</code></dt>
<dd><span class="type">boolean</span> If true, the renderer will use the cameras view-projection matrix for frustum culling (default: false)</dd>
</dl>

**Examples**

Set the current camera to be used for rendering
```
render.set_camera("main:/my_go#camera")
render.draw(self.my_pred)
render.set_camera(nil)

```

Use the camera frustum for frustum culling together with a specific frustum plane option for the draw command
```
-- The camera frustum will take precedence over the frustum plane option in render.draw
render.set_camera("main:/my_go#camera", { use_frustum = true })
-- However, we can still customize the frustum planes regardless of the camera option!
render.draw(self.my_pred, { frustum_planes = render.FRUSTUM_PLANES_ALL })
render.set_camera()

```

### render.set_color_mask
*Type:* FUNCTION
Specifies whether the individual color components in the frame buffer is enabled for writing (true) or disabled (false). For example, if blue is false, nothing is written to the blue component of any pixel in any of the color buffers, regardless of the drawing operation attempted. Note that writing are either enabled or disabled for entire color components, not the individual bits of a component.
The component masks are all initially true.

**Parameters**

- `red` (boolean) - red mask
- `green` (boolean) - green mask
- `blue` (boolean) - blue mask
- `alpha` (boolean) - alpha mask

**Examples**

```
-- alpha cannot be written to frame buffer
render.set_color_mask(true, true, true, false)

```

### render.set_compute
*Type:* FUNCTION
The name of the compute program must be specified in the ".render" resource set
in the "game.project" setting. If nil (or no arguments) are passed to this function,
the current compute program will instead be disabled.

**Parameters**

- `compute` (string | hash | nil) - compute id to use, or nil to disable

**Examples**

Enable compute program named "fractals", then dispatch it.
```
render.set_compute("fractals")
render.enable_texture(0, self.backing_texture)
render.dispatch_compute(128, 128, 1)
render.set_compute()

```

### render.set_cull_face
*Type:* FUNCTION
Specifies whether front- or back-facing polygons can be culled
when polygon culling is enabled. Polygon culling is initially disabled.
If mode is graphics.FACE_TYPE_FRONT_AND_BACK, no polygons are drawn, but other
primitives such as points and lines are drawn. The initial value for
face_type is graphics.FACE_TYPE_BACK.

**Parameters**

- `face_type` (number) - face type
<ul>
<li><code>graphics.FACE_TYPE_FRONT</code></li>
<li><code>graphics.FACE_TYPE_BACK</code></li>
<li><code>graphics.FACE_TYPE_FRONT_AND_BACK</code></li>
</ul>

**Examples**

How to enable polygon culling and set front face culling:
```
render.enable_state(graphics.STATE_CULL_FACE)
render.set_cull_face(graphics.FACE_TYPE_FRONT)

```

### render.set_depth_func
*Type:* FUNCTION
Specifies the function that should be used to compare each incoming pixel
depth value with the value present in the depth buffer.
The comparison is performed only if depth testing is enabled and specifies
the conditions under which a pixel will be drawn.
Function constants:

graphics.COMPARE_FUNC_NEVER (never passes)
graphics.COMPARE_FUNC_LESS (passes if the incoming depth value is less than the stored value)
graphics.COMPARE_FUNC_LEQUAL (passes if the incoming depth value is less than or equal to the stored value)
graphics.COMPARE_FUNC_GREATER (passes if the incoming depth value is greater than the stored value)
graphics.COMPARE_FUNC_GEQUAL (passes if the incoming depth value is greater than or equal to the stored value)
graphics.COMPARE_FUNC_EQUAL (passes if the incoming depth value is equal to the stored value)
graphics.COMPARE_FUNC_NOTEQUAL (passes if the incoming depth value is not equal to the stored value)
graphics.COMPARE_FUNC_ALWAYS (always passes)

The depth function is initially set to graphics.COMPARE_FUNC_LESS.

**Parameters**

- `func` (number) - depth test function, see the description for available values

**Examples**

Enable depth test and set the depth test function to "not equal".
```
render.enable_state(graphics.STATE_DEPTH_TEST)
render.set_depth_func(graphics.COMPARE_FUNC_NOTEQUAL)

```

### render.set_depth_mask
*Type:* FUNCTION
Specifies whether the depth buffer is enabled for writing. The supplied mask governs
if depth buffer writing is enabled (true) or disabled (false).
The mask is initially true.

**Parameters**

- `depth` (boolean) - depth mask

**Examples**

How to turn off writing to the depth buffer:
```
render.set_depth_mask(false)

```

### render.set_listener
*Type:* FUNCTION
Set or remove listener. Currenly only only two type of events can arrived:
render.CONTEXT_EVENT_CONTEXT_LOST - when rendering context lost. Rending paused and all graphics resources become invalid.
render.CONTEXT_EVENT_CONTEXT_RESTORED - when rendering context was restored. Rendering still paused and graphics resources still
invalid but can be reloaded.

**Parameters**

- `callback` (function(self, event_type) | nil) - A callback that receives all render related events.
Pass <code>nil</code> if want to remove listener.
<dl>
<dt><code>self</code></dt>
<dd><span class="type">object</span> The render script</dd>
<dt><code>event_type</code></dt>
<dd><span class="type">string</span> Rendering event. Possible values: <code>render.CONTEXT_EVENT_CONTEXT_LOST</code>, <code>render.CONTEXT_EVENT_CONTEXT_RESTORED</code></dd>
</dl>

**Examples**

Set listener and handle render context events.
```
--- custom.render_script
function init(self)
   render.set_listener(function(self, event_type)
       if event_type == render.CONTEXT_EVENT_CONTEXT_LOST then
           --- Some stuff when rendering context is lost
       elseif event_type == render.CONTEXT_EVENT_CONTEXT_RESTORED then
           --- Start reload resources, reload game, etc.
       end
   end)
end

```

### render.set_polygon_offset
*Type:* FUNCTION
Sets the scale and units used to calculate depth values.
If graphics.STATE_POLYGON_OFFSET_FILL is enabled, each fragment's depth value
is offset from its interpolated value (depending on the depth value of the
appropriate vertices). Polygon offset can be used when drawing decals, rendering
hidden-line images etc.
factor specifies a scale factor that is used to create a variable depth
offset for each polygon. The initial value is 0.
units is multiplied by an implementation-specific value to create a
constant depth offset. The initial value is 0.
The value of the offset is computed as factor × DZ + r × units
DZ is a measurement of the depth slope of the polygon which is the change in z (depth)
values divided by the change in either x or y coordinates, as you traverse a polygon.
The depth values are in window coordinates, clamped to the range [0, 1].
r is the smallest value that is guaranteed to produce a resolvable difference.
It's value is an implementation-specific constant.
The offset is added before the depth test is performed and before the
value is written into the depth buffer.

**Parameters**

- `factor` (number) - polygon offset factor
- `units` (number) - polygon offset units

**Examples**

```
render.enable_state(graphics.STATE_POLYGON_OFFSET_FILL)
render.set_polygon_offset(1.0, 1.0)

```

### render.set_projection
*Type:* FUNCTION
Sets the projection matrix to use when rendering.

**Parameters**

- `matrix` (matrix4) - projection matrix

**Examples**

How to set the projection to orthographic with world origo at lower left,
width and height as set in project settings and depth (z) between -1 and 1:
```
render.set_projection(vmath.matrix4_orthographic(0, render.get_width(), 0, render.get_height(), -1, 1))

```

### render.set_render_target
*Type:* FUNCTION
Sets a render target. Subsequent draw operations will be to the
render target until it is replaced by a subsequent call to set_render_target.
This function supports render targets created by a render script, or a render target resource.

**Parameters**

- `render_target` (render_target) - render target to set. render.RENDER_TARGET_DEFAULT to set the default render target
- `options` (table) (optional) - optional table with behaviour parameters
<dl>
<dt><code>transient</code></dt>
<dd><span class="type">table</span> Transient frame buffer types are only valid while the render target is active, i.e becomes undefined when a new target is set by a subsequent call to set_render_target.
 Default is all non-transient. Be aware that some hardware uses a combined depth stencil buffer and when this is the case both are considered non-transient if exclusively selected!
 A buffer type defined that doesn't exist in the render target is silently ignored.</dd>
</dl>
<ul>
<li><code>graphics.BUFFER_TYPE_COLOR0_BIT</code></li>
<li><code>graphics.BUFFER_TYPE_DEPTH_BIT</code></li>
<li><code>graphics.BUFFER_TYPE_STENCIL_BIT</code></li>
</ul>

**Examples**

How to set a render target and draw to it and then switch back to the default render target
The render target defines the depth/stencil buffers as transient, when set_render_target is called the next time the buffers may be invalidated and allow for optimisations depending on driver support
```
function update(self, dt)
    -- set render target so all drawing is done to it
    render.set_render_target(self.my_render_target, { transient = { graphics.BUFFER_TYPE_DEPTH_BIT, graphics.BUFFER_TYPE_STENCIL_BIT } } )

    -- draw a predicate to the render target
    render.draw(self.my_pred)

    -- set default render target. This also invalidates the depth and stencil buffers of the current target (self.my_render_target)
    --  which can be an optimisation on some hardware
    render.set_render_target(render.RENDER_TARGET_DEFAULT)

end

```

```
function update(self, dt)
    -- set render target by a render target resource identifier
    render.set_render_target('my_rt_resource')

    -- draw a predicate to the render target
    render.draw(self.my_pred)

    -- reset the render target to the default backbuffer
    render.set_render_target(render.RENDER_TARGET_DEFAULT)

end

```

### render.set_render_target_size
*Type:* FUNCTION
Sets the render target size for a render target created from
either a render script, or from a render target resource.

**Parameters**

- `render_target` (render_target) - render target to set size for
- `width` (number) - new render target width
- `height` (number) - new render target height

**Examples**

Resize render targets to the current window size:
```
render.set_render_target_size(self.my_render_target, render.get_window_width(), render.get_window_height())
render.set_render_target_size('my_rt_resource', render.get_window_width(), render.get_window_height())

```

### render.set_stencil_func
*Type:* FUNCTION
Stenciling is similar to depth-buffering as it enables and disables drawing on a
per-pixel basis. First, GL drawing primitives are drawn into the stencil planes.
Second, geometry and images are rendered but using the stencil planes to mask out
where to draw.
The stencil test discards a pixel based on the outcome of a comparison between the
reference value ref and the corresponding value in the stencil buffer.
func specifies the comparison function. See the table below for values.
The initial value is graphics.COMPARE_FUNC_ALWAYS.
ref specifies the reference value for the stencil test. The value is clamped to
the range [0, 2n-1], where n is the number of bitplanes in the stencil buffer.
The initial value is 0.
mask is ANDed with both the reference value and the stored stencil value when the test
is done. The initial value is all 1's.
Function constant:

graphics.COMPARE_FUNC_NEVER (never passes)
graphics.COMPARE_FUNC_LESS (passes if (ref & mask)
graphics.COMPARE_FUNC_LEQUAL (passes if (ref & mask)
graphics.COMPARE_FUNC_GREATER (passes if (ref & mask) > (stencil & mask))
graphics.COMPARE_FUNC_GEQUAL (passes if (ref & mask) >= (stencil & mask))
graphics.COMPARE_FUNC_EQUAL (passes if (ref & mask) = (stencil & mask))
graphics.COMPARE_FUNC_NOTEQUAL (passes if (ref & mask) != (stencil & mask))
graphics.COMPARE_FUNC_ALWAYS (always passes)

**Parameters**

- `func` (number) - stencil test function, see the description for available values
- `ref` (number) - reference value for the stencil test
- `mask` (number) - mask that is ANDed with both the reference value and the stored stencil value when the test is done

**Examples**

```
-- let only 0's pass the stencil test
render.set_stencil_func(graphics.COMPARE_FUNC_EQUAL, 0, 1)

```

### render.set_stencil_mask
*Type:* FUNCTION
The stencil mask controls the writing of individual bits in the stencil buffer.
The least significant n bits of the parameter mask, where n is the number of
bits in the stencil buffer, specify the mask.
Where a 1 bit appears in the mask, the corresponding
bit in the stencil buffer can be written. Where a 0 bit appears in the mask,
the corresponding bit in the stencil buffer is never written.
The mask is initially all 1's.

**Parameters**

- `mask` (number) - stencil mask

**Examples**

```
-- set the stencil mask to all 1:s
render.set_stencil_mask(0xff)

```

### render.set_stencil_op
*Type:* FUNCTION
The stencil test discards a pixel based on the outcome of a comparison between the
reference value ref and the corresponding value in the stencil buffer.
To control the test, call render.set_stencil_func.
This function takes three arguments that control what happens to the stored stencil
value while stenciling is enabled. If the stencil test fails, no change is made to the
pixel's color or depth buffers, and sfail specifies what happens to the stencil buffer
contents.
Operator constants:

graphics.STENCIL_OP_KEEP (keeps the current value)
graphics.STENCIL_OP_ZERO (sets the stencil buffer value to 0)
graphics.STENCIL_OP_REPLACE (sets the stencil buffer value to ref, as specified by render.set_stencil_func)
graphics.STENCIL_OP_INCR (increments the stencil buffer value and clamp to the maximum representable unsigned value)
graphics.STENCIL_OP_INCR_WRAP (increments the stencil buffer value and wrap to zero when incrementing the maximum representable unsigned value)
graphics.STENCIL_OP_DECR (decrements the current stencil buffer value and clamp to 0)
graphics.STENCIL_OP_DECR_WRAP (decrements the current stencil buffer value and wrap to the maximum representable unsigned value when decrementing zero)
graphics.STENCIL_OP_INVERT (bitwise inverts the current stencil buffer value)

dppass and dpfail specify the stencil buffer actions depending on whether subsequent
depth buffer tests succeed (dppass) or fail (dpfail).
The initial value for all operators is graphics.STENCIL_OP_KEEP.

**Parameters**

- `sfail` (number) - action to take when the stencil test fails
- `dpfail` (number) - the stencil action when the stencil test passes
- `dppass` (number) - the stencil action when both the stencil test and the depth test pass, or when the stencil test passes and either there is no depth buffer or depth testing is not enabled

**Examples**

Set the stencil function to never pass and operator to always draw 1's
on test fail.
```
render.set_stencil_func(graphics.COMPARE_FUNC_NEVER, 1, 0xFF)
-- always draw 1's on test fail
render.set_stencil_op(graphics.STENCIL_OP_REPLACE, graphics.STENCIL_OP_KEEP, graphics.STENCIL_OP_KEEP)

```

### render.set_view
*Type:* FUNCTION
Sets the view matrix to use when rendering.

**Parameters**

- `matrix` (matrix4) - view matrix to set

**Examples**

How to set the view and projection matrices according to
the values supplied by a camera.
```
function init(self)
  self.view = vmath.matrix4()
  self.projection = vmath.matrix4()
end

function update(self, dt)
  -- set the view to the stored view value
  render.set_view(self.view)
  -- now we can draw with this view
end

function on_message(self, message_id, message)
  if message_id == hash("set_view_projection") then
     -- camera view and projection arrives here.
     self.view = message.view
     self.projection = message.projection
  end
end

```

### render.set_viewport
*Type:* FUNCTION
Set the render viewport to the specified rectangle.

**Parameters**

- `x` (number) - left corner
- `y` (number) - bottom corner
- `width` (number) - viewport width
- `height` (number) - viewport height

**Examples**

```
-- Set the viewport to the window dimensions.
render.set_viewport(0, 0, render.get_window_width(), render.get_window_height())

```

### render.SORT_BACK_TO_FRONT
*Type:* CONSTANT
Depth sort far-to-near (default; good for transparent passes).

### render.SORT_FRONT_TO_BACK
*Type:* CONSTANT
Depth sort near-to-far (good for opaque passes to reduce overdraw).

### render.SORT_NONE
*Type:* CONSTANT
No per-call sorting; draw entries in insertion order.

### render_target
*Type:* TYPEDEF
Render target

**Parameters**

- `value` (number)

### resize
*Type:* MESSAGE
Set the size of the game window. Only works on desktop platforms.

**Parameters**

- `height` (number) - the new window height
- `width` (number) - the new window width

**Examples**

```
msg.post("@render:", "resize", { width = 1024, height = 768 } )

```

### texture
*Type:* TYPEDEF
Texture handle

**Parameters**

- `value` (number)

### window_resized
*Type:* MESSAGE
Reports a change in window size. This is initiated on window resize on desktop or by orientation changes
on mobile devices.

**Parameters**

- `height` (number) - the new window height
- `width` (number) - the new window width

**Examples**

```
function on_message(self, message_id, message)
    -- check for the message
    if message_id == hash("window_resized") then
        -- the window was resized.
    end
end

```
