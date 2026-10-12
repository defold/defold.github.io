# Collection Resource

**Namespace:** `dmGameObject`
**Language:** C++
**Type:** Defold C++
**File:** `res_collection.h`
**Source:** `engine/gameobject/src/dmsdk/gameobject/res_collection.h`
**Include:** `dmsdk/gameobject/res_collection.h`

API for accessing loaded game object collection resources.

## API

### CollectionResource
*Type:* STRUCT
Opaque pointer returned by dmResource::Get for a compiled collection
resource. The pointer remains valid while the caller holds a resource
reference, including across resource reloads.
Do not load a collection resource directly into an HCollection. An
HCollection is a numeric collection handle and is not resource storage.

### ResCollectionGetCollection
*Type:* FUNCTION
Converts a live collection resource returned by dmResource::Get into the
numeric collection handle used by the game-object API. The caller retains
ownership of the resource reference and must release the original resource
pointer with dmResource::Release. The returned handle may change when the
resource is reloaded; call this function again after a reload.

**Parameters**

- `resource` (dmGameObject::CollectionResource*) - Live collection resource returned by dmResource::Get.

**Returns**

- `collection` (dmGameObject::HCollection) - Collection handle, or 0 if resource is null.

**Examples**

```
dmGameObject::CollectionResource* resource = 0;
dmResource::Result result = dmResource::Get(factory, "/main.collectionc", (void**)&resource);
if (result == dmResource::RESULT_OK)
{
    dmGameObject::HCollection collection = dmGameObject::ResCollectionGetCollection(resource);
    // Use collection with the game-object API.
    dmResource::Release(factory, resource);
}

```
