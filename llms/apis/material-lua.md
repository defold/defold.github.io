# Material

**Namespace:** `material`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_material.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_material.cpp`

Functions for interacting with materials.

## API

### material.constant_info
*Type:* STRUCT
Shader constant information

**Members**

- `name` (hash) - Constant name.
- `type` (material.CONSTANT_TYPE) - Constant type.
- `value?` (material.constant_info_value) - Constant value or values. Present for user constants.

### material.constant_info_value
*Type:* TYPEDEF
The value of a user constant returned in a material.constant_info
entry by material.get_constants. A scalar constant is returned as a
vector4 or matrix4; a shader constant array is returned as an
array of those values. Non-user constants do not include a value field.

**Parameters**

- `value` (vector4 | matrix4 | vector4[] | matrix4[])

**Examples**

```
for _, constant in ipairs(material.get_constants(self.material)) do
    if constant.value then
        pprint(constant.name, constant.value)
    end
end

```

### material.constant_options
*Type:* STRUCT
Shader constant update

**Members**

- `type?` (material.CONSTANT_TYPE) - Constant type.
- `value?` (material.constant_value) - Constant value or values.

### material.CONSTANT_TYPE
*Type:* ENUM
Material constant types

**Members**

- `material.CONSTANT_TYPE_USER` - User vector constant.
- `material.CONSTANT_TYPE_USER_COLOR` - User color constant.
- `material.CONSTANT_TYPE_USER_MATRIX4` - User matrix constant.
- `material.CONSTANT_TYPE_VIEWPROJ` - View-projection matrix constant.
- `material.CONSTANT_TYPE_WORLD` - World matrix constant.
- `material.CONSTANT_TYPE_TEXTURE` - Texture matrix constant.
- `material.CONSTANT_TYPE_VIEW` - View matrix constant.
- `material.CONSTANT_TYPE_PROJECTION` - Projection matrix constant.
- `material.CONSTANT_TYPE_NORMAL` - Normal matrix constant.
- `material.CONSTANT_TYPE_WORLDVIEW` - World-view matrix constant.
- `material.CONSTANT_TYPE_WORLDVIEWPROJ` - World-view-projection matrix constant.
- `material.CONSTANT_TYPE_TIME` - Time constant.
- `material.CONSTANT_TYPE_WORLD_INVERSE` - Inverse world matrix constant.
- `material.CONSTANT_TYPE_VIEW_INVERSE` - Inverse view matrix constant.
- `material.CONSTANT_TYPE_PROJECTION_INVERSE` - Inverse projection matrix constant.
- `material.CONSTANT_TYPE_VIEWPROJ_INVERSE` - Inverse view-projection matrix constant.
- `material.CONSTANT_TYPE_WORLDVIEW_INVERSE` - Inverse world-view matrix constant.
- `material.CONSTANT_TYPE_WORLDVIEWPROJ_INVERSE` - Inverse world-view-projection matrix constant.

### material.constant_value
*Type:* TYPEDEF
A value accepted by material.set_constants when updating a shader
constant. Use a number or vector for user vector constants, a matrix4
for matrix constants, and an array to update a shader constant array.

**Parameters**

- `value` (number | vector3 | vector4 | matrix4 | (number|vector3|vector4|matrix4)[])

**Examples**

```
material.set_constants(self.material, {
    tint = { value = vmath.vector4(1, 0.5, 0.5, 1) },
    weights = { value = { 0.25, 0.5, 0.75, 1 } }
})

```

### material.get_constants
*Type:* FUNCTION
Returns a table of all the shader constants in the material. This function will return all the shader constants
that are used in both the vertex and the fragment shaders.

**Parameters**

- `path` (hash | string) - The path to the resource

**Returns**

- `constants` (material.constant_info[]) - Shader constant information.

**Examples**

Get the shader constants from a material specified as a resource property
```
go.property("my_material", resource.material())

function init(self)
    local constants = material.get_constants(self.my_material)
end

```

### material.get_samplers
*Type:* FUNCTION
Returns a table of all the texture samplers in the material. This function will return all the texture samplers
that are used in both the vertex and the fragment shaders.

**Parameters**

- `path` (hash | string) - The path to the resource

**Returns**

- `samplers` (material.sampler_info[]) - texture sampler information

**Examples**

Get the texture samplers from a material specified as a resource property
```
go.property("my_material", resource.material())

function init(self)
    local samplers = material.get_samplers(self.my_material)
end

```

### material.get_textures
*Type:* FUNCTION
Returns a table of all the textures from the material.

**Parameters**

- `path` (hash | string) - The path to the resource

**Returns**

- `textures` (material.texture_info[]) - material texture information

**Examples**

Get the textures from a material specified as a resource property
```
go.property("my_material", resource.material())

function init(self)
    local textures = material.get_textures(self.my_material)
end

```

### material.get_vertex_attributes
*Type:* FUNCTION
Returns a table of all the vertex attributes in the material. This function will return all the vertex attributes
that are used in the vertex shader of the material.

**Parameters**

- `path` (hash | string) - The path to the resource

**Returns**

- `attributes` (material.vertex_attribute_info[]) - vertex attribute information

**Examples**

Get the vertex attributes from a material specified as a resource property
```
go.property("my_material", resource.material())

function init(self)
    local vertex_attributes = material.get_vertex_attributes(self.my_material)
end

```

### material.named_vertex_attribute_options
*Type:* STRUCT
Named material vertex attribute update

**Members**

- `name` (string|hash) - Attribute name.
- `value?` (material.vertex_attribute_value) - Attribute value.
- `normalize?` (boolean) - Whether integer data is normalized.
- `data_type?` (graphics.DATA_TYPE) - Attribute data type.
- `coordinate_space?` (graphics.COORDINATE_SPACE) - Attribute coordinate space.
- `semantic_type?` (graphics.SEMANTIC_TYPE) - Attribute semantic.

### material.sampler_info
*Type:* STRUCT
Texture sampler information

**Members**

- `name` (hash) - Sampler name.
- `type` (graphics.TEXTURE_TYPE) - Sampler texture type.
- `u_wrap` (graphics.TEXTURE_WRAP) - Horizontal wrap mode.
- `v_wrap` (graphics.TEXTURE_WRAP) - Vertical wrap mode.
- `w_wrap` (graphics.TEXTURE_WRAP) - Depth wrap mode.
- `min_filter` (graphics.TEXTURE_FILTER) - Minification filter.
- `mag_filter` (graphics.TEXTURE_FILTER) - Magnification filter.
- `max_anisotropy` (number) - Maximum anisotropy.

### material.sampler_options
*Type:* STRUCT
Texture sampler update

**Members**

- `u_wrap?` (graphics.TEXTURE_WRAP) - Horizontal wrap mode.
- `v_wrap?` (graphics.TEXTURE_WRAP) - Vertical wrap mode.
- `w_wrap?` (graphics.TEXTURE_WRAP) - Depth wrap mode.
- `min_filter?` (graphics.TEXTURE_FILTER) - Minification filter.
- `mag_filter?` (graphics.TEXTURE_FILTER) - Magnification filter.
- `max_anisotropy?` (number) - Maximum anisotropy.

### material.set_constants
*Type:* FUNCTION
Sets shader constants in a material, if the constants exist.

**Parameters**

- `path` (hash | string) - The path to the resource
- `constants` (table<string|hash, material.constant_options>) - Shader constant updates keyed by constant name. Partial updates are supported.

**Examples**

Set a shader constant in a material specified as a resource property
```
go.property("my_material", resource.material())

function update(self)
    -- update the 'tint' constant
    material.set_constants(self.my_material, {
        tint = { value = vmath.vector4(1, 0, 0, 1) }
    })
    -- change the type of the 'view_proj' constant to CONSTANT_TYPE_USER_MATRIX4 so the renderer can set our custom data
    material.set_constants(self.my_material, {
        view_proj = { value = self.my_view_proj, type = material.CONSTANT_TYPE_USER_MATRIX4 }
    })
end

```

### material.set_samplers
*Type:* FUNCTION
Sets texture samplers in a material, if the samplers exist. Use this function to change the settings of texture samplers.
To set actual textures that should be bound to the samplers, use the material.set_textures function instead.

**Parameters**

- `path` (hash | string) - The path to the resource
- `samplers` (table<string|hash, material.sampler_options>) - Sampler updates keyed by sampler name. Partial updates are supported.

**Examples**

Configures a sampler in a material specified as a resource property
```
go.property("my_material", resource.material())

function init(self)
    material.set_samplers(self.my_material, {
        texture_sampler = { u_wrap = graphics.TEXTURE_WRAP_REPEAT, v_wrap = graphics.TEXTURE_WRAP_MIRRORED_REPEAT }
    })
end

```

### material.set_textures
*Type:* FUNCTION
Sets textures in a material, if the samplers exist.

**Parameters**

- `path` (hash | string) - The path to the resource
- `textures` (table<string|hash, string|hash>) - A table keyed by sampler name with texture resources as values.

**Examples**

Set a texture in a material from a resource
```
go.property("my_material", resource.material())
go.property("my_texture", resource.texture())

function init(self)
    material.set_textures(self.my_material, {
        my_texture = self.my_texture
    })
end

```

### material.set_vertex_attributes
*Type:* FUNCTION
Sets vertex attributes in a material, if the vertex attributes exist.

**Parameters**

- `path` (hash | string) - The path to the resource
- `attributes` (table<string|hash, material.vertex_attribute_options> | material.named_vertex_attribute_options[]) - Vertex attributes keyed by name, or an array with explicit <code>name</code> fields. Partial updates are supported.

**Examples**

Configures a vertex attribute in a material specified as a resource property
```
go.property("my_material", resource.material())

function init(self)
    material.set_vertex_attributes(self.my_material, {
        tint_attribute = { value = vmath.vec4(1, 0, 0, 1), semantic_type = graphics.SEMANTIC_TYPE_COLOR },
        weights        = { value = vmath.vec4(0, 1, 0, 0), semantic_type = graphics.SEMANTIC_TYPE_NONE }
    })
end

```

### material.texture_info
*Type:* STRUCT
Texture information

**Members**

- `path?` (hash) - Texture resource path, if backed by a resource.
- `handle` (texture) - Runtime texture handle.
- `width` (integer) - Texture width.
- `height` (integer) - Texture height.
- `depth` (integer) - Texture depth or layer count.
- `page_count` (integer) - Texture page count.
- `mipmaps` (integer) - Mipmap count.
- `type` (graphics.TEXTURE_TYPE) - Texture type.
- `flags` (graphics.TEXTURE_USAGE_FLAG) - Texture usage flags.

### material.vertex_attribute_info
*Type:* STRUCT
Material vertex attribute information

**Members**

- `name` (hash) - Attribute name.
- `value` (material.vertex_attribute_value) - Attribute value.
- `normalize` (boolean) - Whether integer data is normalized.
- `data_type` (graphics.DATA_TYPE) - Attribute data type.
- `coordinate_space` (graphics.COORDINATE_SPACE) - Attribute coordinate space.
- `semantic_type` (graphics.SEMANTIC_TYPE) - Attribute semantic.

### material.vertex_attribute_options
*Type:* STRUCT
Material vertex attribute update

**Members**

- `value?` (material.vertex_attribute_value) - Attribute value.
- `normalize?` (boolean) - Whether integer data is normalized.
- `data_type?` (graphics.DATA_TYPE) - Attribute data type.
- `coordinate_space?` (graphics.COORDINATE_SPACE) - Attribute coordinate space.
- `semantic_type?` (graphics.SEMANTIC_TYPE) - Attribute semantic.

### material.vertex_attribute_value
*Type:* TYPEDEF
A vertex attribute value accepted by material.set_vertex_attributes
and returned by material.get_vertex_attributes. Use a number or vector
for scalar and vector attributes, matrix4 for a 4x4 matrix, and a flat
array of numbers for matrix shapes that do not map to matrix4.

**Parameters**

- `value` (number | vector3 | vector4 | matrix4 | number[])

**Examples**

```
material.set_vertex_attributes(self.material, {
    tint = { value = vmath.vector4(1, 0, 0, 1) },
    transform_2d = { value = { 1, 0, 0, 0, 1, 0, 0, 0, 1 } }
})

```
