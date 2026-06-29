# Compute

**Namespace:** `compute`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_compute.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_compute.cpp`

Functions for interacting with compute programs.

## API

### compute.get_constants
*Type:* FUNCTION
Returns a table of all the shader constants in the compute program.

**Parameters**

- `path` (hash | string) - The path to the resource

**Returns**

- `table` (table) - A table of tables, where each entry contains info about the shader constants:
<dl>
<dt><code>name</code></dt>
<dd><span class="type">hash</span> the hashed name of the constant</dd>
<dt><code>type</code></dt>
<dd><span class="type">number</span> the type of the constant. Supported values:</dd>
</dl>
<ul>
<li><code>material.CONSTANT_TYPE_USER</code></li>
<li><code>material.CONSTANT_TYPE_USER_MATRIX4</code></li>
<li><code>material.CONSTANT_TYPE_VIEWPROJ</code></li>
<li><code>material.CONSTANT_TYPE_WORLD</code></li>
<li><code>material.CONSTANT_TYPE_TEXTURE</code></li>
<li><code>material.CONSTANT_TYPE_VIEW</code></li>
<li><code>material.CONSTANT_TYPE_PROJECTION</code></li>
<li><code>material.CONSTANT_TYPE_NORMAL</code></li>
<li><code>material.CONSTANT_TYPE_WORLDVIEW</code></li>
<li><code>material.CONSTANT_TYPE_WORLDVIEWPROJ</code></li>
<li><code>material.CONSTANT_TYPE_TIME</code></li>
<li><code>material.CONSTANT_TYPE_WORLD_INVERSE</code></li>
<li><code>material.CONSTANT_TYPE_VIEW_INVERSE</code></li>
<li><code>material.CONSTANT_TYPE_PROJECTION_INVERSE</code></li>
<li><code>material.CONSTANT_TYPE_VIEWPROJ_INVERSE</code></li>
<li><code>material.CONSTANT_TYPE_WORLDVIEW_INVERSE</code></li>
<li><code>material.CONSTANT_TYPE_WORLDVIEWPROJ_INVERSE</code></li>
</ul>
<dl>
<dt><code>value</code></dt>
<dd><span class="type">vmath.vector4 | vmath.matrix4</span> the value(s) of the constant. If the constant is an array, the value will be a table of vmath.vector4 or vmath.matrix4 if the type is <code>material.CONSTANT_TYPE_USER_MATRIX4</code>.</dd>
</dl>

**Examples**

Get the shader constants from a compute program resource
```
function init(self)
    local constants = compute.get_constants("/my_compute.computec")
end

```

### compute.get_samplers
*Type:* FUNCTION
Returns a table of all the texture samplers in the compute program. This function will return all the texture samplers
that are available, even the ones that have not been specified in the compute resource.

**Parameters**

- `path` (hash | string) - The path to the resource

**Returns**

- `table` (table) - A table of tables, where each entry contains info about the texture samplers:
<dl>
<dt><code>name</code></dt>
<dd><span class="type">hash</span> the hashed name of the texture sampler</dd>
<dt><code>u_wrap</code></dt>
<dd><span class="type">number</span> the u wrap mode of the texture sampler. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_WRAP_CLAMP_TO_BORDER</code></li>
<li><code>graphics.TEXTURE_WRAP_CLAMP_TO_EDGE</code></li>
<li><code>graphics.TEXTURE_WRAP_MIRRORED_REPEAT</code></li>
<li><code>graphics.TEXTURE_WRAP_REPEAT</code></li>
</ul>
<dl>
<dt><code>v_wrap</code></dt>
<dd><span class="type">number</span> the v wrap mode of the texture sampler. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_WRAP_CLAMP_TO_BORDER</code></li>
<li><code>graphics.TEXTURE_WRAP_CLAMP_TO_EDGE</code></li>
<li><code>graphics.TEXTURE_WRAP_MIRRORED_REPEAT</code></li>
<li><code>graphics.TEXTURE_WRAP_REPEAT</code></li>
</ul>
<dl>
<dt><code>min_filter</code></dt>
<dd><span class="type">number</span> the min filter mode of the texture sampler. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_FILTER_DEFAULT</code></li>
<li><code>graphics.TEXTURE_FILTER_NEAREST</code></li>
<li><code>graphics.TEXTURE_FILTER_LINEAR</code></li>
<li><code>graphics.TEXTURE_FILTER_NEAREST_MIPMAP_NEAREST</code></li>
<li><code>graphics.TEXTURE_FILTER_NEAREST_MIPMAP_LINEAR</code></li>
<li><code>graphics.TEXTURE_FILTER_LINEAR_MIPMAP_NEAREST</code></li>
<li><code>graphics.TEXTURE_FILTER_LINEAR_MIPMAP_LINEAR</code></li>
</ul>
<dl>
<dt><code>mag_filter</code></dt>
<dd><span class="type">number</span> the mag filter mode of the texture sampler</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_FILTER_DEFAULT</code></li>
<li><code>graphics.TEXTURE_FILTER_NEAREST</code></li>
<li><code>graphics.TEXTURE_FILTER_LINEAR</code></li>
</ul>
<dl>
<dt><code>max_anisotropy</code></dt>
<dd><span class="type">number</span> the max anisotropy of the texture sampler</dd>
</dl>

**Examples**

Get the texture samplers from a compute program resource
```
function init(self)
    local samplers = compute.get_samplers("/my_compute.computec")
end

```

### compute.get_textures
*Type:* FUNCTION
Returns a table of all the textures from the compute program.

**Parameters**

- `path` (hash | string) - The path to the resource

**Returns**

- `table` (table) - A table of tables, where each entry contains info about the compute textures:
<dl>
<dt><code>path</code></dt>
<dd><span class="type">hash</span> the resource path of the texture. Only available if the texture is a resource.</dd>
<dt><code>handle</code></dt>
<dd><span class="type">hash</span> the runtime handle of the texture.</dd>
<dt><code>width</code></dt>
<dd><span class="type">number</span> the width of the texture</dd>
<dt><code>height</code></dt>
<dd><span class="type">number</span> the height of the texture</dd>
<dt><code>depth</code></dt>
<dd><span class="type">number</span> the depth of the texture. Corresponds to the number of layers in an array texture.</dd>
<dt><code>mipmaps</code></dt>
<dd><span class="type">number</span> the number of mipmaps in the texture</dd>
<dt><code>type</code></dt>
<dd><span class="type">number</span> the type of the texture. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_TYPE_2D</code></li>
<li><code>graphics.TEXTURE_TYPE_2D_ARRAY</code></li>
<li><code>graphics.TEXTURE_TYPE_CUBE_MAP</code></li>
<li><code>graphics.TEXTURE_TYPE_IMAGE_2D</code></li>
<li><code>graphics.TEXTURE_TYPE_3D</code></li>
<li><code>graphics.TEXTURE_TYPE_IMAGE_3D</code></li>
</ul>
<dl>
<dt><code>flags</code></dt>
<dd><span class="type">number</span> the flags of the texture. This field is a bit mask of these supported flags:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_USAGE_FLAG_SAMPLE</code></li>
<li><code>graphics.TEXTURE_USAGE_FLAG_MEMORYLESS</code></li>
<li><code>graphics.TEXTURE_USAGE_FLAG_STORAGE</code></li>
<li><code>graphics.TEXTURE_USAGE_FLAG_INPUT</code></li>
<li><code>graphics.TEXTURE_USAGE_FLAG_COLOR</code></li>
</ul>

**Examples**

Get the textures from a compute program resource
```
function init(self)
    local textures = compute.get_textures("/my_compute.computec")
end

```

### compute.set_constants
*Type:* FUNCTION
Sets shader constants in a compute program, if the constants exist.

**Parameters**

- `path` (hash | string) - The path to the resource
- `constants` (table) - A table keyed by constant name with args tables as values. Constants can be partially updated. Supported entries:
<dl>
<dt><code>type</code></dt>
<dd><span class="type">number</span> the type of the constant. Supported values:</dd>
</dl>
<ul>
<li><code>material.CONSTANT_TYPE_USER</code></li>
<li><code>material.CONSTANT_TYPE_USER_MATRIX4</code></li>
<li><code>material.CONSTANT_TYPE_VIEWPROJ</code></li>
<li><code>material.CONSTANT_TYPE_WORLD</code></li>
<li><code>material.CONSTANT_TYPE_TEXTURE</code></li>
<li><code>material.CONSTANT_TYPE_VIEW</code></li>
<li><code>material.CONSTANT_TYPE_PROJECTION</code></li>
<li><code>material.CONSTANT_TYPE_NORMAL</code></li>
<li><code>material.CONSTANT_TYPE_WORLDVIEW</code></li>
<li><code>material.CONSTANT_TYPE_WORLDVIEWPROJ</code></li>
<li><code>material.CONSTANT_TYPE_TIME</code></li>
<li><code>material.CONSTANT_TYPE_WORLD_INVERSE</code></li>
<li><code>material.CONSTANT_TYPE_VIEW_INVERSE</code></li>
<li><code>material.CONSTANT_TYPE_PROJECTION_INVERSE</code></li>
<li><code>material.CONSTANT_TYPE_VIEWPROJ_INVERSE</code></li>
<li><code>material.CONSTANT_TYPE_WORLDVIEW_INVERSE</code></li>
<li><code>material.CONSTANT_TYPE_WORLDVIEWPROJ_INVERSE</code></li>
</ul>
<dl>
<dt><code>value</code></dt>
<dd><span class="type">vmath.vector4 | vmath.vector3 | vmath.matrix4 | number | table</span> the value(s) of the constant. If the shader constant is an array, the amount of values to update depends on how many values that are passed in the 'value' field.</dd>
</dl>

**Examples**

Set a shader constant in a compute program
```
function update(self)
    -- update the 'tint' constant
    compute.set_constants("/my_compute.computec", {
        tint = { value = vmath.vector4(1, 0, 0, 1) }
    })
    -- change the type of the 'view_proj' constant to CONSTANT_TYPE_USER_MATRIX4 so the renderer can set our custom data
    compute.set_constants("/my_compute.computec", {
        view_proj = { value = self.my_view_proj, type = material.CONSTANT_TYPE_USER_MATRIX4 }
    })
end

```

### compute.set_samplers
*Type:* FUNCTION
Sets texture samplers in a compute program, if the samplers exist. Use this function to change the settings of texture samplers.
To set actual textures that should be bound to the samplers, use the compute.set_textures function instead.

**Parameters**

- `path` (hash | string) - The path to the resource
- `samplers` (table) - A table keyed by sampler name with args tables as values. Partial updates are supported. Supported entries:
<dl>
<dt><code>u_wrap</code></dt>
<dd><span class="type">number</span> the u wrap mode of the texture sampler. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_WRAP_CLAMP_TO_BORDER</code></li>
<li><code>graphics.TEXTURE_WRAP_CLAMP_TO_EDGE</code></li>
<li><code>graphics.TEXTURE_WRAP_MIRRORED_REPEAT</code></li>
<li><code>graphics.TEXTURE_WRAP_REPEAT</code></li>
</ul>
<dl>
<dt><code>v_wrap</code></dt>
<dd><span class="type">number</span> the v wrap mode of the texture sampler. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_WRAP_CLAMP_TO_BORDER</code></li>
<li><code>graphics.TEXTURE_WRAP_CLAMP_TO_EDGE</code></li>
<li><code>graphics.TEXTURE_WRAP_MIRRORED_REPEAT</code></li>
<li><code>graphics.TEXTURE_WRAP_REPEAT</code></li>
</ul>
<dl>
<dt><code>min_filter</code></dt>
<dd><span class="type">number</span> the min filter mode of the texture sampler. Supported values:</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_FILTER_DEFAULT</code></li>
<li><code>graphics.TEXTURE_FILTER_NEAREST</code></li>
<li><code>graphics.TEXTURE_FILTER_LINEAR</code></li>
<li><code>graphics.TEXTURE_FILTER_NEAREST_MIPMAP_NEAREST</code></li>
<li><code>graphics.TEXTURE_FILTER_NEAREST_MIPMAP_LINEAR</code></li>
<li><code>graphics.TEXTURE_FILTER_LINEAR_MIPMAP_NEAREST</code></li>
<li><code>graphics.TEXTURE_FILTER_LINEAR_MIPMAP_LINEAR</code></li>
</ul>
<dl>
<dt><code>mag_filter</code></dt>
<dd><span class="type">number</span> the mag filter mode of the texture sampler</dd>
</dl>
<ul>
<li><code>graphics.TEXTURE_FILTER_DEFAULT</code></li>
<li><code>graphics.TEXTURE_FILTER_NEAREST</code></li>
<li><code>graphics.TEXTURE_FILTER_LINEAR</code></li>
</ul>
<dl>
<dt><code>max_anisotropy</code></dt>
<dd><span class="type">number</span> the max anisotropy of the texture sampler</dd>
</dl>

**Examples**

Configures a sampler in a compute program
```
function init(self)
    compute.set_samplers("/my_compute.computec", {
        texture_sampler = { u_wrap = graphics.TEXTURE_WRAP_REPEAT, v_wrap = graphics.TEXTURE_WRAP_MIRRORED_REPEAT }
    })
end

```

### compute.set_textures
*Type:* FUNCTION
Sets textures in a compute program, if the samplers exist.

**Parameters**

- `path` (hash | string) - The path to the resource
- `textures` (table) - A table keyed by sampler name with texture resources as values.

**Examples**

Set a texture in a compute program from a resource
```
go.property("my_texture", resource.texture())

function init(self)
    compute.set_textures("/my_compute.computec", {
        my_texture = self.my_texture
    })
end

```
