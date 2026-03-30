# Property

**Namespace:** `dmGameSystem`
**Language:** C++
**Type:** Defold C++
**File:** `property.h`
**Source:** `engine/gamesys/src/dmsdk/gamesys/property.h`
**Include:** `dmsdk/gamesys/property.h`

Property functions.

## API

### GetResourceProperty
*Type:* FUNCTION
Gets the resource path hash

**Parameters**

- `property` (const PropVector4&) - the property
- `resource` (void*) - the resource to get the
- `out_value` (dmGameObject::PropertyDesc&) - the out property

**Returns**

- `result` (dmGameObject::PropertyResult) - RESULT_OK if successful

### IsReferencingProperty
*Type:* FUNCTION
Checks if the name matches any field in the property

**Parameters**

- `property` (const PropVector3&) - the property
- `query` (dmhash_t) - the name to look for (e.g. hash("pos.x"))

**Returns**

- `result` (bool) - true if the property contains the name

### IsReferencingProperty
*Type:* FUNCTION
Checks if the name matches any field in the property

**Parameters**

- `property` (const PropVector4&) - the property
- `query` (dmhash_t) - the name to look for (e.g. hash("pos.x"))

**Returns**

- `result` (bool) - true if the property contains the name

### PropVector3
*Type:* STRUCT

### PropVector4
*Type:* STRUCT

### SetResourceProperty
*Type:* FUNCTION
Updates the reference count of the resources, and returns the new resource.

**Parameters**

- `factory` (dmGameObject::HFactory) - the factory
- `value` (const dmGameObject::PropertyVar&) - the property containing the hash of the resources to get
- `ext` (dmhash_t) - the hash of the resource file suffix (without the "."). E.g. hash("spritec")
- `out_resource` (void**) - pointer to the current resource. Will also get the pointer to the new resource.

**Returns**

- `result` (dmGameObject::PropertyResult) - RESULT_OK if successful
