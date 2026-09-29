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

- `table` (material.constant_info[]) - Information about the shader constants.

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

- `table` (material.sampler_info[]) - Information about the texture samplers.

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

- `table` (material.texture_info[]) - Information about the compute textures.

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
- `constants` (table<string|hash, material.constant_options>) - Constant options keyed by constant name. Partial updates are supported.

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
- `samplers` (table<string|hash, material.sampler_options>) - Sampler options keyed by sampler name. Partial updates are supported.

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
- `textures` (table<string|hash, string|hash>) - A table keyed by sampler name with texture resources as values.

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
