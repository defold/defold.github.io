# Light Resource

**Namespace:** `dmGameSystem`
**Language:** C++
**Type:** Defold C++
**File:** `res_light.h`
**Source:** `engine/gamesys/src/dmsdk/gamesys/resources/res_light.h`
**Include:** `dmsdk/gamesys/resources/res_light.h`

Helper types and accessors for the light resource type (`.lightc`).

## API

### GetLightPrototype
*Type:* FUNCTION
Returns the dmRender::HLightPrototype handle created from the .lightc data.
The pointer remains valid until the resource is released.

**Parameters**

- `res` (LightResource*) - Light resource

**Returns**

- `prototype` (dmRender::HLightPrototype*) - Prototype pointer

### LightResource
*Type:* STRUCT
This struct is an opaque handle managed by the engine.
