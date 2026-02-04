# Gameobject

**Namespace:** `dmGameObject`
**Language:** C++
**Type:** Defold C++
**File:** `gameobject.h`
**Source:** `engine/gameobject/src/dmsdk/gameobject/gameobject.h`
**Include:** `dmsdk/gameobject/gameobject.h`

API for manipulating game objects

## API

### AcquireInstanceIndex
*Type:* FUNCTION
Retrieve an instance index from the index pool for the collection.

**Parameters**

- `collection` (dmGameObject::HColleciton) - Collection from which to retrieve the instance index.

**Returns**

- `instance` (uint32_t) - index from the index pool of collection.

### AddDynamicResourceHash
*Type:* FUNCTION
Adds a reference to a dynamically created resource into the collection.
If the resource is not released before the collection is being destroyed,
the collection will automatically free the resource.

**Parameters**

- `collection` (HCollection) - Collection handle
- `path_hash` (dmhash_t) - resource path hash

### AssignInstanceIndex
*Type:* FUNCTION
Assign an index to the instance, only if the instance is not null.

**Parameters**

- `index` (uint32_t) - The index to assign.
- `instance` (dmGameObject::HInstance) - The instance that should be assigned the index.

### CreateInstanceId
*Type:* FUNCTION
Creates a new unique instance ID and returns its hash.

**Returns**

- `id` (dmhash_t) - hash of the new unique instance id

### CreateResult
*Type:* ENUM
Create result enum.

**Members**

- `dmGameObject::CREATE_RESULT_OK`
- `dmGameObject::CREATE_RESULT_UNKNOWN_ERROR`

### Delete
*Type:* FUNCTION
Delete gameobject instance

**Parameters**

- `collection` (dmGameObject::HCollection) - Gameobject collection
- `instance` (dmGameObject::HInstance) - Gameobject instance
- `recursive` (bool) - If true, delete child hierarchy recursively in child to parent order (leaf first)

### DeleteBones
*Type:* FUNCTION
Recursively delete all instances flagged as bones under the given parent instance.
The order of deletion is depth-first, so that the children are deleted before the parents.

**Parameters**

- `parent` (HInstance) - Parent instance of the hierarchy

### GetAbsoluteIdentifier
*Type:* FUNCTION
Get absolute identifier relative to instance. The returned identifier is the
representation of the qualified name, i.e. the path from root-collection to
the sub-collection which the instance belongs to.
Example: if the instance is part of a sub-collection in the root-collection
named "sub" and id == "a" the returned identifier represents the path "sub.a"

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance to get absolute identifier to
- `identifier` (const char*) - Identifier relative to instance

**Returns**

- `return` (dmhash_t) - Absolute identifier.

### GetCollection
*Type:* FUNCTION
Retrieve a collection from the specified instance

**Parameters**

- `instance` (dmGameObject::HInstance) - Game object instance

**Returns**

- `collection` (dmGameObject::HInstance) - The collection the specified instance belongs to

### GetCollectionByHash
*Type:* FUNCTION
Retrieve a collection by socket name hash
Note: in native extensions, the register can be retrieved during init using dmEngine::GetGameObjectRegister(dmExtension::AppParams *params)

**Parameters**

- `regist` (dmGameObject::HRegister) - Register
- `socket_name` (dmhash_t) - The socket name

**Returns**

- `collection` (dmGameObject::HCollection) - The collection if successful. 0 otherwise.

### GetComponent
*Type:* FUNCTION
Get the component, component type and its world

**Parameters**

- `instance` (dmGameObject::HInstance) - Instance
- `component_id` (dmhash_t) - Component id
- `component_type` (uint32_t*) - (out) Component type. Used for validation.
- `component` (HComponent*) - (out) The component.
- `world` (HComponentWorld*) - (out) The component world. May be 0.

**Returns**

- `result` (dmGameObject::Result) - RESULT_OK if the component was found

### GetComponentId
*Type:* FUNCTION
Get component id from component index.

**Parameters**

- `instance` (dmGameObject::HInstance) - Instance
- `component_index` (uint16_t) - Component index
- `component_id` (dmhash_t*) - Component id as out-argument

**Returns**

- `result` (dmGameObject::Result) - RESULT_OK if the component was found

### GetComponentTypeIndex
*Type:* FUNCTION
Get the component type index

**Parameters**

- `collection` (HCollection) - Collection handle
- `type_hash` (dmhash_t) - The hashed name of the registered component type (e.g. dmHashString("guic"))

**Returns**

- `type_index` (uint32_t) - The component type index. 0xFFFFFFFF if not found

### GetContext
*Type:* FUNCTION
Retrieve the context for a component type

**Parameters**

- `collection` (HCollection) - Collection handle
- `component_type_index` (uint32_t) - index of the component type

**Returns**

- `context` (void*) - The pointer to the context, 0x0 if not found

### GetIdentifier
*Type:* FUNCTION
Get instance identifier

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance

**Returns**

- `return` (dmhash_t) - Identifier. dmGameObject::UNNAMED_IDENTIFIER if not set.

### GetInstanceFromIdentifier
*Type:* FUNCTION
Get instance from identifier

**Parameters**

- `collection` (dmGameObject::HCollection) - Collection
- `identifier` (dmhash_t) - Identifier

**Returns**

- `instance` (dmGameObject::HInstance) - Instance. NULL if instance isn't found.

### GetMessageSocket
*Type:* FUNCTION
Retrieve the message socket for the specified collection.

**Parameters**

- `collection` (dmGameObject::HCollection) - Collection handle

**Returns**

- `socket` (dmMessage::HSocket) - The message socket of the specified collection

### GetPosition
*Type:* FUNCTION
Get gameobject instance position

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance

**Returns**

- `return` (dmVMath::Point3) - Position

### GetRotation
*Type:* FUNCTION
Get gameobject instance rotation

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance

**Returns**

- `return` (dmGameObject::Quat) - rotation

### GetScale
*Type:* FUNCTION
Get gameobject instance scale

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance

**Returns**

- `return` (dmGameObject::Vector3) - Non-uniform scale

### GetUniformScale
*Type:* FUNCTION
Get gameobject instance uniform scale

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance

**Returns**

- `return` (float) - Uniform scale

### GetWorld
*Type:* FUNCTION
Retrieve the world in the collection connected to the supplied component

**Parameters**

- `collection` (HCollection) - Collection handle
- `component_type_index` (uint32_t) - index of the component type

**Returns**

- `world` (void*) - The pointer to the world, 0x0 if not found

### GetWorldMatrix
*Type:* FUNCTION
Get game object instance world transform as Matrix4.

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance

**Returns**

- `return` (dmGameObject::Matrix4) - World transform matrix.

### GetWorldPosition
*Type:* FUNCTION
Get gameobject instance world position

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance

**Returns**

- `return` (dmGameObject::Point3) - World position

### GetWorldRotation
*Type:* FUNCTION
Get gameobject instance world rotation

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance

**Returns**

- `return` (dmGameObject::Quat) - World rotation

### GetWorldScale
*Type:* FUNCTION
Get game object instance world transform

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance

**Returns**

- `return` (dmGameObject::Vector3) - World scale

### GetWorldTransform
*Type:* FUNCTION
Get game object instance world transform

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance

**Returns**

- `return` (dmTransform::Transform) - World transform

### GetWorldUniformScale
*Type:* FUNCTION
Get game object instance uniform scale

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance

**Returns**

- `return` (float) - World uniform scale

### HCollection
*Type:* TYPEDEF
Gameobject collection handle

### HComponent
*Type:* TYPEDEF
Opaque handle to component instance

### HComponentInternal
*Type:* TYPEDEF
Opaque handle to internal representation of a component instance

### HComponentWorld
*Type:* TYPEDEF
Opaque handle to a component world

### HInstance
*Type:* TYPEDEF
Gameobject instance handle

### HProperties
*Type:* TYPEDEF
Gameobject properties handle

### HPropertyContainer
*Type:* TYPEDEF
Handle to a list of properties (gameobject_props.h)

### HPrototype
*Type:* TYPEDEF
Gameobject prototype handle

### HRegister
*Type:* TYPEDEF
Collection register.

### HScript
*Type:* TYPEDEF
Script handle

### HScriptInstance
*Type:* TYPEDEF
Script instance handle

### InputAction
*Type:* STRUCT
Container of input related information.

### InputResult
*Type:* ENUM
Input result enum

**Members**

- `INPUT_RESULT_IGNORED` - = 0
- `INPUT_RESULT_CONSUMED` - = 1
- `INPUT_RESULT_UNKNOWN_ERROR` - = -1000

### InstanceIdMap
*Type:* TYPEDEF
Used for mapping instance ids from a collection definition to newly spawned instances

### InstancePropertyContainers
*Type:* TYPEDEF
Contains property containers for game objects to be spawned

### INVALID_INSTANCE_POOL_INDEX
*Type:* CONSTANT
Value for an invalid instance index, this must be the same as defined in gamesys_ddf.proto for Create#index.

### IsBone
*Type:* FUNCTION
Check whether the instance is flagged as a bone.

**Parameters**

- `instance` (HInstance) - Instance

**Returns**

- `result` (bool) - True if flagged as a bone

### New
*Type:* FUNCTION
Create a new gameobject instance

**Notes**

- Calling this function during update is not permitted. Use #Spawn instead for deferred creation

**Parameters**

- `collection` (dmGameObject::HCollection) - Gameobject collection
- `prototype_name` (const char*) - Prototype file name. May be 0.

**Returns**

- `instance` (dmGameObject::HInstance) - New gameobject instance. NULL if any error occured

### Playback
*Type:* ENUM
Playback type enum

### PropertyDesc
*Type:* STRUCT
Description of a property.
If the property is externally mutable, m_ValuePtr points to the value and its length is m_ElementCount.
m_Variant always reflects the value.

**Members**

- `m_ElementIds` (dmhash_t) - For composite properties (float arrays), these ids name each element
- `m_Variant` (PropertyVar) - Variant holding the value
- `m_ValuePtr` (float*) - Pointer to the value, only set for mutable values. The actual data type is described by the variant.
- `m_ReadOnly` (uint16_t) - Determines whether we are permitted to write to this property.
- `m_ValueType` (uint16_t) - Indicates type of the property (of type PropertyValueType).
- `m_ArrayLength` (uint16_t) - Number of array entries, if the property is an array and zero otherwise. Max supported length is 2^14 (16384 elements)

### PropertyOptions
*Type:* STRUCT
Parameters variant that holds key or index for a propertys data structure.

**Members**

- `m_Index` (int32_t) - The index of the property to set, only applicable if property is array.
- `m_Key` (dmhash_t) - The key of the property to set, only applicable if property is hashtable.
- `m_HasKey` (uint8_t) - A flag if structure contain m_Key value (it can't contain both)

### PropertyResult
*Type:* ENUM
Property result.

**Members**

- `dmGameObject::PROPERTY_RESULT_OK`
- `dmGameObject::PROPERTY_RESULT_NOT_FOUND`
- `dmGameObject::PROPERTY_RESULT_INVALID_FORMAT`
- `dmGameObject::PROPERTY_RESULT_UNSUPPORTED_TYPE`
- `dmGameObject::PROPERTY_RESULT_TYPE_MISMATCH`
- `dmGameObject::PROPERTY_RESULT_COMP_NOT_FOUND`
- `dmGameObject::PROPERTY_RESULT_INVALID_INSTANCE`
- `dmGameObject::PROPERTY_RESULT_BUFFER_OVERFLOW`
- `dmGameObject::PROPERTY_RESULT_UNSUPPORTED_VALUE`
- `dmGameObject::PROPERTY_RESULT_UNSUPPORTED_OPERATION`
- `dmGameObject::PROPERTY_RESULT_RESOURCE_NOT_FOUND`
- `dmGameObject::PROPERTY_RESULT_INVALID_INDEX`
- `dmGameObject::PROPERTY_RESULT_INVALID_KEY`
- `dmGameObject::PROPERTY_RESULT_READ_ONLY`

### PropertyType
*Type:* ENUM
Property types.

**Members**

- `dmGameObject::PROPERTY_TYPE_NUMBER`
- `dmGameObject::PROPERTY_TYPE_HASH`
- `dmGameObject::PROPERTY_TYPE_URL`
- `dmGameObject::PROPERTY_TYPE_VECTOR3`
- `dmGameObject::PROPERTY_TYPE_VECTOR4`
- `dmGameObject::PROPERTY_TYPE_QUAT`
- `dmGameObject::PROPERTY_TYPE_BOOLEAN`
- `dmGameObject::PROPERTY_TYPE_COUNT`

### PropertyValueType
*Type:* ENUM
Type of property value

**Members**

- `dmGameObject::PROP_VALUE_ARRAY`
- `dmGameObject::PROP_VALUE_HASHTABLE`

### PropertyVar
*Type:* STRUCT
Property variant that holds the data for a variable

**Members**

- `m_Type` (dmGameObject::PropertyType) - property type
- `m_Number` (double) - A floating point value (union)
- `m_Hash` (dmhash_t) - A hash value (union)
- `m_Url` (const uin8_t*) - An URL value (union)
- `m_V4` (float) - A vector4 value (union)
- `m_Bool` (bool) - A boolean value (union)

### Result
*Type:* ENUM
Result enumeration.

**Members**

- `dmGameObject::RESULT_OK`
- `dmGameObject::RESULT_OUT_OF_RESOURCES`
- `dmGameObject::RESULT_ALREADY_REGISTERED`
- `dmGameObject::RESULT_IDENTIFIER_IN_USE`
- `dmGameObject::RESULT_IDENTIFIER_ALREADY_SET`
- `dmGameObject::RESULT_COMPONENT_NOT_FOUND`
- `dmGameObject::RESULT_MAXIMUM_HIEARCHICAL_DEPTH`
- `dmGameObject::RESULT_INVALID_OPERATION`
- `dmGameObject::RESULT_RESOURCE_TYPE_NOT_FOUND`
- `dmGameObject::RESULT_BUFFER_OVERFLOW`
- `dmGameObject::RESULT_IDENTIFIER_INVALID`
- `dmGameObject::RESULT_RESOURCE_ERROR`
- `dmGameObject::RESULT_CHILD_NOT_FOUND`
- `dmGameObject::RESULT_INVALID_PROPERTIES`
- `dmGameObject::RESULT_UNABLE_TO_CREATE_COMPONENTS`
- `dmGameObject::RESULT_UNABLE_TO_INIT_INSTANCE`
- `dmGameObject::RESULT_UNKNOWN_ERROR`

### SceneNode
*Type:* STRUCT
Opaque struct that holds info about the current node

**Notes**

- The concept of a `scene node` only exists here, for the purposes of inspecting the scene graph for inspection and testing purposes only.

### SceneNodeIterator
*Type:* STRUCT
Opaque struct that holds info about the current position when traversing the scene

### SceneNodeProperty
*Type:* STRUCT
Struct that holds info about the current position when traversing the scene

**Members**

- `m_NameHash` (dmhash_t) - name
- `m_Type` (dmGameObject::SceneNodePropertyType) - type
- `m_Value` (union) - value

`m_Number`
: [type:double] floating point number

`m_Hash`
: [type:dmhash_t] The hashed value.

`m_URL`
: [type:char[1024]] The text representation of the url (if reverse hashes are enabled)

`m_V4`
: [type:float[4]] Used for Vector3, Vector4 and Quat

`m_Bool`
: [type:bool] A boolean value

`m_Text`
: [type:const char*] Text from a text property

### SceneNodePropertyIterator
*Type:* STRUCT
Holds the property

**Members**

- `m_Property` (dmGameObject::SceneNodeProperty) - property

### SceneNodePropertyType
*Type:* ENUM
scene node property types

**Notes**

- Since we don't support text properties, we'll keep a separate enum here for now

**Members**

- `dmGameObject::SCENE_NODE_PROPERTY_TYPE_NUMBER`
- `dmGameObject::SCENE_NODE_PROPERTY_TYPE_HASH`
- `dmGameObject::SCENE_NODE_PROPERTY_TYPE_URL`
- `dmGameObject::SCENE_NODE_PROPERTY_TYPE_VECTOR3`
- `dmGameObject::SCENE_NODE_PROPERTY_TYPE_VECTOR4`
- `dmGameObject::SCENE_NODE_PROPERTY_TYPE_QUAT`
- `dmGameObject::SCENE_NODE_PROPERTY_TYPE_BOOLEAN`
- `dmGameObject::SCENE_NODE_PROPERTY_TYPE_TEXT`
- `dmGameObject::SCENE_NODE_PROPERTY_TYPE_COUNT`

### SetBone
*Type:* FUNCTION
Set whether the instance should be flagged as a bone.
Instances flagged as bones can have their transforms updated in a batch through SetBoneTransforms.
Used for animated skeletons.

**Parameters**

- `instance` (HInstance) - Instance
- `bone` (bool) - true if the instance is a bone

### SetBoneTransforms
*Type:* FUNCTION
Set the local transforms recursively of all instances flagged as bones, starting with component with id.
The order of the transforms is depth-first.

**Parameters**

- `instance` (HInstance) - First Instance of the hierarchy to set
- `component_transform` (dmTransform::Transform) - the transform for component root
- `transforms` (dmTransform::Transform*) - Array of transforms to set depth-first for the bone instances
- `transform_count` (uint32_t) - Size of the transforms array

**Returns**

- `Number` - of instances found

### SetIdentifier
*Type:* FUNCTION
Set instance identifier. Must be unique within the collection.

**Parameters**

- `collection` (dmGameObject::HCollection) - Collection
- `instance` (dmGameObject::HInstance) - Instance
- `identifier` (dmhash_t) - Identifier

**Returns**

- `result` (dmGameObject::Result) - RESULT_OK on success

### SetPosition
*Type:* FUNCTION
Set gameobject instance position

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance
- `position` (dmVMath::Point3) - New Position

### SetRotation
*Type:* FUNCTION
Set gameobject instance rotation

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance
- `rotation` (dmVmath::Quat) - New rotation

### SetScale
*Type:* FUNCTION
Set gameobject instance uniform scale

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance
- `scale` (float) - New uniform scale

### SetScale
*Type:* FUNCTION
Set gameobject instance non-uniform scale

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance
- `scale` (dmVmath::Vector3) - New non-uniform scale

### SetScaleXY
*Type:* FUNCTION
Set gameobject instance x and y scale

**Parameters**

- `instance` (dmGameObject::HInstance) - Gameobject instance
- `scale_x` - New x scale
- `scale_y` - New y scale

### Spawn
*Type:* FUNCTION
Spawns a new gameobject instance. The actual creation is performed after the update is completed.

**Parameters**

- `collection` (HCollection) - Gameobject collection
- `prototype` (HPrototype) - Prototype
- `prototype_name` (const char*) - Prototype file name (.goc)
- `id` (dmhash_t) - Id of the spawned instance
- `properties` (HPropertyContainer) - Container with override properties
- `position` (dmVMath::Vector3) - Position of the spawed object
- `rotation` (dmVMath::Quat) - Rotation of the spawned object
- `scale` (dmVMath::Vector3) - Scale of the spawned object
return instance <span class="type"> HInstance</span> the spawned instance, 0 at failure

### TraverseGetRoot
*Type:* FUNCTION
Gets the top node of the whole game (the main collection)

**Notes**

- The dmGameObject::HRegister is obtained from the `dmEngine::GetGameObjectRegister(dmExtension::AppParams)`
- Traversing the scene like this is not efficient. These functions are here for inspection and testing purposes only.

**Parameters**

- `regist` (dmGameObject::HRegister) - the full gameobject register
- `node` (dmGameObject::HRegister) - the node to inspect

**Returns**

- `result` (bool) - True if successful

**Examples**

The following examples show how to iterate over currently loaded scene graph
```
void OutputNode(dmGameObject::SceneNode* node) {
    dmGameObject::SceneNodeIterator it = dmGameObject::TraverseIterateChildren(node);
    while(dmGameObject::TraverseIterateNext(&it))
    {
        OutputProperties(&it.m_Node); // see dmGameObject::TraverseIterateProperties()
        OutputNode(&it.m_Node);
    }
}

bool OutputScene(HRegister regist) {
    dmGameObject::SceneNode root;
    if (!dmGameObject::TraverseGetRoot(regist, &root))
        return false;
    OutputNode(&node);
}

```

### TraverseIterateChildren
*Type:* FUNCTION
Get a scene node iterator for the nodes' children

**Parameters**

- `node` (dmGameObject::SceneNode*) - the parent node

**Returns**

- `iterator` (dmGameObject::SceneNodeIterator) - the iterator

### TraverseIterateNext
*Type:* FUNCTION
Step a scene node iterator to the next sibling

**Parameters**

- `it` (dmGameObject::SceneNodeIterator*) - the iterator

**Returns**

- `result` (bool) - true if successful. false if the iterator is finished

### TraverseIterateProperties
*Type:* FUNCTION
Create a scene node traversal property iterator

**Notes**

- Getting the properties like this is not efficient. These functions are here for inspection and testing purposes only.
- Reverse hashes via `dmHashReverseSafe64()` isn't available in release builds.

**Parameters**

- `node` (dmGameObject::SceneNode*) - the node to inspect

**Returns**

- `iterator` (dmGameObject::SceneNodePropertyIterator) - the property iterator

**Examples**

The following examples show how to iterate over the properties of a node
```
dmGameObject::SceneNodePropertyIterator pit = TraverseIterateProperties(node);
while(dmGameObject::TraverseIteratePropertiesNext(&pit))
{
    const char* name = dmHashReverseSafe64(pit.m_Property.m_NameHash);
    switch(pit.m_Property.m_Type)
    {
    case dmGameObject::SCENE_NODE_PROPERTY_TYPE_NUMBER: ...
    ...
    }
}

```

### TraverseIteratePropertiesNext
*Type:* FUNCTION
Steps the scene node traversal property iterator to the next property

**Parameters**

- `it` (dmGameObject::SceneNodePropertyIterator*) - the iterator

**Returns**

- `finished` (bool) - True if the iterator it valid, false if the iterator is finished.

### UpdateContext
*Type:* STRUCT
Update context

**Members**

- `m_TimeScale` (float) - the scaling factor what was applied on the dt (i.e. the collection update time scale)
- `m_DT` (float) - the delta time elapsed since last frame (seconds)
- `m_FixedUpdateFrequency` (uint32_t) - Number of of calls per second to the FixedUpdate of each component

### UpdateResult
*Type:* ENUM
Update result enum.

**Members**

- `dmGameObject::UPDATE_RESULT_OK`
- `dmGameObject::UPDATE_RESULT_UNKNOWN_ERROR`
