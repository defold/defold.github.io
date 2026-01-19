# Collection factory

**Namespace:** `dmGameSystem`
**Language:** C++
**Type:** Defold C++
**File:** `comp_collection_factory.h`
**Source:** `engine/gamesys/src/dmsdk/gamesys/components/comp_collection_factory.h`
**Include:** `dmsdk/gamesys/components/comp_collection_factory.h`

API for spawning collections from a collection factory component.

## API

### CompCollectionFactorySpawn
*Type:* FUNCTION
Spawns a collection of gameobjects in a collection using a collection factory component.

**Parameters**

- `world` (HCollectionFactoryWorld) - Collection factory world
- `component` (HCollectionFactoryComponent) - Collection factory component
- `collection` (HCollection) - Gameobject collection to spawn into
- `id_prefix` (const char*) - Prefix for the spawned instance identifiers. Must start with a forward slash (/). Must be unique within the collection. Pass nullptr to automatically generate a unique identifier prefix (e.g. /collection1, /collection2 etc.).
- `position` (dmVMath::Point3) - Position of the spawned objects
- `rotation` (dmVMath::Quat) - Rotation of the spawned objects
- `scale` (dmVMath::Vector3) - Scale of the spawned objects
- `properties` (dmGameObject::InstancePropertyContainers) - Property containers with override properties
- `out_instances` (dmGameObject::InstanceIdMap) - A map with the spawned instance id's

**Returns**

- `result` (dmGameObject::Result) - Result of the operation
