# Component Render Constants

**Namespace:** `dmGameSystem`
**Language:** C++
**Type:** Defold C++
**File:** `render_constants.h`
**Source:** `engine/gamesys/src/dmsdk/gamesys/render_constants.h`
**Include:** `dmsdk/gamesys/render_constants.h`

Api for setting and updating component render constants

## API

### AreRenderConstantsUpdated
*Type:* FUNCTION
check if the constants have changed

**Parameters**

- `constants` (dmGameSystem::HComponentRenderConstants) - the constants

**Returns**

- `result` (int) - non zero if the constants were changed

### ClearRenderConstant
*Type:* FUNCTION
Removes a render constant from the container

**Parameters**

- `constants` (dmGameSystem::HComponentRenderConstants) - the constants
- `name_hash` (dmhash_t) - the hashed name of the constant

**Returns**

- `result` (int) - non zero if the constant was removed

### CompGetConstantCallback
*Type:* TYPEDEF
Used in GetMaterialConstant to resolve a render constant's value

### CompSetConstantCallback
*Type:* TYPEDEF
Used in SetMaterialConstant to set a render constant's value

### CreateRenderConstants
*Type:* FUNCTION
Create a new HComponentRenderConstants container

**Returns**

- `constants` (dmGameSystem::HComponentRenderConstants)

### DestroyRenderConstants
*Type:* FUNCTION
Destroys a render constants container

**Parameters**

- `constants` (dmGameSystem::HComponentRenderConstants) - (must not be 0)

### EnableRenderObjectConstants
*Type:* FUNCTION
set the constants of a render object

**Parameters**

- `ro` (dmRender::RenderObject*) - the render object
- `constants` (dmGameSystem::HComponentRenderConstants) - the constants

### GetRenderConstant
*Type:* FUNCTION
Destroys a render constants container

**Parameters**

- `constants` (dmGameSystem::HComponentRenderConstants) - the constants
- `name_hash` (dmhash_t) - the hashed name of the property
- `out_constant` (dmRender::Constant**) - the pointer where to store the constant

**Returns**

- `result` (bool) - returns true if the constant exists

### GetRenderConstant
*Type:* FUNCTION
Get a render constant by index

**Parameters**

- `constants` (dmGameSystem::HComponentRenderConstants) - the constants
- `index` (uint32_t) - the index

**Returns**

- `constant` (dmRender::HConstant) - the pointer where to store the constant

### GetRenderConstantCount
*Type:* FUNCTION
Get the number of render constants

**Parameters**

- `constants` (dmGameSystem::HComponentRenderConstants) - the constants

**Returns**

- `size` (uint32_t) - returns the number of set constants

### HashRenderConstants
*Type:* FUNCTION
Hashes the constants

**Notes**

- Also updates the internal state of the constants container. After a call to this function, the `AreRenderConstantsUpdated` will always return false.

**Parameters**

- `constants` (dmGameSystem::HComponentRenderConstants) - the constants
- `state` (HashState32*) - the hash state to update

### HashState32
*Type:* TYPEDEF
Found in hash.h

### HComponentRenderConstants
*Type:* TYPEDEF
Render constants handle

### SetRenderConstant
*Type:* FUNCTION
Set a render constant by name. The constant must exist in the material

**Parameters**

- `constants` (dmGameSystem::HComponentRenderConstants) - the render constants buffer
- `material` (dmRender::HMaterial) - the material to get default values from if constant didn't already exist in the render constants buffer
- `name_hash` (dmhash_t) - the hashed name of the constant
- `value_index` (uint32_t) - index of the constant value to set, if the constant is an array
- `element_index` (uint32_t*) - pointer to the index of the element (in range [0,3]). May be 0
- `var` (const dmGameObject::PropertyVar&) - the constant value

### SetRenderConstant
*Type:* FUNCTION
Set a render constant by name. The constant must exist in the material

**Parameters**

- `constants` (dmGameSystem::HComponentRenderConstants) - the constants
- `name_hash` (dmhash_t) - the hashed name of the constant
- `values` (dmVMath::Vector4*) - the values
- `num_values` (uint32_t) - number of values in the array
