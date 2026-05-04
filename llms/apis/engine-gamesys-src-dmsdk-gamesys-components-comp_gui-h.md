# GameSystem GUI Component

**Namespace:** `dmGameSystem`
**Language:** C++
**Type:** Defold C++
**File:** `comp_gui.h`
**Source:** `engine/gamesys/src/dmsdk/gamesys/components/comp_gui.h`
**Include:** `dmsdk/gamesys/components/comp_gui.h`

Per-property registration functions for GUI component extensions.

## API

### CompGuiPropertyGetterFn
*Type:* TYPEDEF
GUI component property getter function

**Parameters**

- `scene` (dmGui::HScene) - The GUI scene
- `params` (dmGameObject::ComponentGetPropertyParams) - Property parameters
- `out_value` (dmGameObject::PropertyDesc&) - Output value

**Returns**

- `return` (dmGameObject::PropertyResult) - PROPERTY_RESULT_OK on success

### CompGuiPropertySetterFn
*Type:* TYPEDEF
GUI component property setter function

**Parameters**

- `scene` (dmGui::HScene) - The GUI scene
- `params` (dmGameObject::ComponentSetPropertyParams) - Property parameters

**Returns**

- `return` (dmGameObject::PropertyResult) - PROPERTY_RESULT_OK on success
