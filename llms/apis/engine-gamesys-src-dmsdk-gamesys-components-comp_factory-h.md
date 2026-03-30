# Factory

**Namespace:** `dmGameSystem`
**Language:** C++
**Type:** Defold C++
**File:** `comp_factory.h`
**Source:** `engine/gamesys/src/dmsdk/gamesys/components/comp_factory.h`
**Include:** `dmsdk/gamesys/components/comp_factory.h`

API for spawning gameobject instances from a factory component.

## API

### CompFactorySpawn
*Type:* FUNCTION
Spawns a new gameobject instance in a collection using a factory component.

**Parameters**

- `world` (HFactoryWorld) - Factory world
- `component` (HFactoryComponent) - Factory component
- `collection` (HCollection) - Gameobject collection to spawn into
- `id` (dmhash_t) - Identifier for the new instance. Must be unique within the collection. Pass 0 to automatically generate a unique identifier (e.g. /instance1, /instance2 etc.).
- `position` (dmVMath::Point3) - Position of the spawned object
- `rotation` (dmVMath::Quat) - Rotation of the spawned object
- `scale` (dmVMath::Vector3) - Scale of the spawned object
- `properties` (dmGameObject::HPropertyContainer) - Property container with override properties
- `out_instance` (dmGameObject::HInstance) - Output parameter for the new instance

**Returns**

- `result` (dmGameObject::Result) - Result of the operation
