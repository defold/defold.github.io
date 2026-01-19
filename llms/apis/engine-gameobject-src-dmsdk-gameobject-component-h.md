# Component

**Namespace:** `dmGameObject`
**Language:** C++
**Type:** Defold C++
**File:** `component.h`
**Source:** `engine/gameobject/src/dmsdk/gameobject/component.h`
**Include:** `dmsdk/gameobject/component.h`

Api for manipulating game object components (WIP)

## API

### ComponentAddToUpdate
*Type:* TYPEDEF
Component add to update function. Only components called with this function should be included in the update passes.

**Parameters**

- `params` (const dmGameObject::ComponentAddToUpdateParams&)

**Returns**

- `result` (CreateResult) - CREATE_RESULT_OK on success

### ComponentAddToUpdateParams
*Type:* STRUCT
Parameters to ComponentAddToUpdate callback.

**Members**

- `m_Collection` (HCollection) - Collection handle
- `m_Instance` (HInstance) - Game object instance
- `m_World` (void*) - Component world
- `m_Context` (void*) - User context
- `m_UserData` (uintptr_t*) - User data storage pointer

### ComponentCreate
*Type:* TYPEDEF
Component create function. Should allocate all necessary resources for the component.
The game object instance is guaranteed to have its id, scene hierarchy and transform data updated when this is called.

**Parameters**

- `params` (const dmGameObject::ComponentCreateParams&)

**Returns**

- `result` (CreateResult) - CREATE_RESULT_OK on success

### ComponentCreateParams
*Type:* STRUCT
Parameters to ComponentCreate callback.

**Members**

- `m_Instance` (HInstance) - Game object instance
- `m_Position` (dmVMath::Point3) - Local component position
- `m_Rotation` (dmVMath::Quat) - Local component rotation
- `m_Scale` (dmVMath::Vector3) - Local component scale
- `m_PropertySet` (PropertySet) - Set of properties
- `m_Resource` (void*) - Component resource
- `m_World` (void*) - Component world, as created in the ComponentNewWorld callback
- `m_Context` (void*) - User context
- `m_UserData` (uintptr_t*) - User data storage pointer
- `m_ComponentIndex` (uint16_t) - Index of the component type being created (among all component types)

### ComponentDeleteWorld
*Type:* TYPEDEF
Component world destroy function

**Parameters**

- `params` (const dmGameObject::ComponentDeleteWorldParams&)

**Returns**

- `result` (CreateResult) - CREATE_RESULT_OK on success

### ComponentDeleteWorldParams
*Type:* STRUCT
Parameters to ComponentDeleteWorld callback.

**Members**

- `m_Context` - [type void*] Context for the component type
- `m_World` - [type void*] The pointer to the world to destroy

### ComponentDestroy
*Type:* TYPEDEF
Component destroy function. Should deallocate all necessary resources.

**Parameters**

- `params` (const dmGameObject::ComponentDestroyParams&)

**Returns**

- `result` (CreateResult) - CREATE_RESULT_OK on success

### ComponentDestroyParams
*Type:* STRUCT
Parameters to ComponentDestroy callback.

**Members**

- `m_Collection` (HCollection) - Collection handle
- `m_Instance` (HInstance) - Game object instance
- `m_World` (void*) - Component world
- `m_Context` (void*) - User context
- `m_UserData` (uintptr_t*) - User data storage pointer

### ComponentFinal
*Type:* TYPEDEF
Component finalize function. Should clean up as it is called when the component is disabled.

**Parameters**

- `params` (const dmGameObject::ComponentFinalParams&)

**Returns**

- `result` (CreateResult) - CREATE_RESULT_OK on success

### ComponentFinalParams
*Type:* STRUCT
Parameters to ComponentFinal callback.

**Members**

- `m_Collection` (HCollection) - Collection handle
- `m_Instance` (HInstance) - Game object instance
- `m_World` (void*) - Component world
- `m_Context` (void*) - User context
- `m_UserData` (uintptr_t*) - User data storage pointer

### ComponentGet
*Type:* TYPEDEF
A simple way to get the component instance from the user_data (which was set during creation)

**Parameters**

- `params` (const dmGameObject::ComponentGetParams&) - Update parameters

**Returns**

- `component` (void*) - The internal component pointer

### ComponentGetParams
*Type:* STRUCT
Parameters to ComponentGet callback.

**Members**

- `m_World` (HComponentWorld) - Component world
- `m_UserData` (HComponentInternal) - Component internal representation

### ComponentGetProperty
*Type:* TYPEDEF
Callback for retrieving a property value of the component.

**Parameters**

- `params` (const dmGameObject::ComponentGetPropertyParams&) - the parameters
- `out_value` (dmGameObject::PropertyDesc&) - (out) the property

**Returns**

- `result` (dmGameObject::PropertyResult) - PROPERTY_RESULT_OK if retrieving the property was ok

### ComponentGetPropertyParams
*Type:* STRUCT
Parameters to ComponentGetProperty callback.

**Members**

- `m_Context` (void*) - Context for the component type
- `m_World` (void*) - Component world
- `m_Instance` (HInstance) - Game object instance
- `m_PropertyId` (dmhash_t) - Id of the property
- `m_UserData` (uintptr_t*) - User data storage pointer
- `m_Options` (PropertyOptions) - Options for getting the property

### ComponentInit
*Type:* TYPEDEF
Component init function. Should set the components initial state as it is called when the component is enabled.

**Parameters**

- `params` (const dmGameObject::ComponentInitParams&)

**Returns**

- `result` (CreateResult) - CREATE_RESULT_OK on success

### ComponentInitParams
*Type:* STRUCT
Parameters to ComponentInit callback.

**Members**

- `m_Collection` (HCollection) - Collection handle
- `m_Instance` (HInstance) - Game object instance
- `m_World` (void*) - Component world
- `m_Context` (void*) - User context
- `m_UserData` (uintptr_t*) - User data storage pointer

### ComponentIterProperties
*Type:* TYPEDEF
Callback when iterating over the properties for a component.

**Notes**

- This function is only available/used in debug builds, when traversing the scene graph in order to export
this data for external tools (e.g. external testing libraries like Poco)

**Parameters**

- `pit` (dmGameObject::SceneNodePropertyIterator) - the property iterator
- `node` (dmGameObject::SceneNode*) - the scene node

### ComponentNewWorld
*Type:* TYPEDEF
Component world create function

**Parameters**

- `params` (const dmGameObject::ComponentNewWorldParams&)

**Returns**

- `result` (CreateResult) - CREATE_RESULT_OK on success

### ComponentNewWorldParams
*Type:* STRUCT
Parameters to ComponentNewWorld callback.

**Members**

- `m_Context` (void*) - Context for the component type
- `m_ComponentIndex` (uint8_t) - Component type index that can be used later with GetWorld()
- `m_MaxInstances` (uint32_t) - Max component game object instance count (if applicable)
- `m_World` (void**) - Out-parameter of the pointer in which to store the created world
- `m_MaxComponentInstances` (uint32_t) - Max components count of this type in current collection counted at the build stage.
                                        If component in factory then value is 0xFFFFFFFF

### ComponentOnInput
*Type:* TYPEDEF
Component on-input function. Called when input is sent to this component

**Parameters**

- `params` (const dmGameObject::ComponentOnInputParams&) - Input parameters

**Returns**

- `result` (InputResult) - How the component handled the input

### ComponentOnInputParams
*Type:* STRUCT
Parameters to ComponentOnInput callback.

**Members**

- `m_Instance` (HInstance) - Instance handle
- `m_InputAction` (const InputAction*) - Information about the input that occurred (note that input being released is also treated as input)
- `m_Context` (void*) - User context
- `m_UserData` (uintptr_t*) - User data storage pointer

### ComponentOnMessage
*Type:* TYPEDEF
Component on-message function. Called when message is sent to this component

**Parameters**

- `params` (const dmGameObject::ComponentOnMessageParams&) - Update parameters

**Returns**

- `result` (UpdateResult) - UPDATE_RESULT_OK on success

### ComponentOnMessageParams
*Type:* STRUCT
Parameters to ComponentOnMessage callback.

**Members**

- `m_Instance` (HInstance) - Instance handle
- `m_World` (void*) - World
- `m_Context` (void*) - User context
- `m_UserData` (uintptr_t*) - User data storage pointer
- `m_Message` (dmMessage::Message*) - Message

### ComponentOnReload
*Type:* FUNCTION
Called when the resource the component is based on has been reloaded.

**Parameters**

- `params` (const dmGameObject::ComponentOnReloadParams&) - the parameters

### ComponentOnReloadParams
*Type:* STRUCT
Parameters to ComponentOnReload callback.

**Members**

- `m_Instance` (HInstance) - Instance handle
- `m_Resource` (void*) - Resource that was reloaded
- `m_World` (void*) - Component world
- `m_Context` (void*) - User context
- `m_UserData` (uintptr_t*) - User data storage pointer

### ComponentSetProperties
*Type:* TYPEDEF
Set a property set for the component.

**Parameters**

- `params` (const dmGameObject::ComponentSetPropertiesParams&) - the parameters

**Returns**

- `result` (dmGameObject::PropertyResult) - PROPERTY_RESULT_OK if property was set

### ComponentSetPropertiesParams
*Type:* STRUCT
Parameters to ComponentSetProperties callback.

**Members**

- `m_Instance` (HInstance) - Instance handle
- `m_PropertySet` (PropertySet) - Property set to use
- `m_UserData` (uintptr_t*) - User data storage pointer

### ComponentSetProperty
*Type:* TYPEDEF
Callback for setting a property value of the component.

**Parameters**

- `params` (const dmGameObject::ComponentSetPropertyParams&) - the parameters

**Returns**

- `result` (dmGameObject::PropertyResult) - PROPERTY_RESULT_OK if property was set

### ComponentSetPropertyParams
*Type:* STRUCT
Parameters to ComponentSetProperty callback.

**Members**

- `m_Context` (void*) - Context for the component type
- `m_World` (void*) - Component world
- `m_Instance` (HInstance) - Game object instance
- `m_PropertyId` (dmhash_t) - Id of the property
- `m_UserData` (uintptr_t*) - User data storage pointer
- `m_Value` (PropertyVar) - New value of the property
- `m_Options` (PropertyOptions) - Options for setting the property

### ComponentsPostUpdate
*Type:* TYPEDEF
Component post update function. The component state should never be modified in this function.

**Parameters**

- `params` (const dmGameObject::ComponentsPostUpdateParams&) - Update parameters

**Returns**

- `result` (UpdateResult) - UPDATE_RESULT_OK on success

### ComponentsPostUpdateParams
*Type:* STRUCT
Parameters for ComponentsPostUpdate callback.

**Members**

- `m_Collection` (HCollection) - Collection handle
- `m_World` (void*) - Component world
- `m_Context` (void*) - User context

### ComponentsRender
*Type:* TYPEDEF
Component render function.

**Parameters**

- `params` (const dmGameObject::ComponentsRenderParams&) - Update parameters

**Returns**

- `result` (UpdateResult) - UPDATE_RESULT_OK on success

### ComponentsRenderParams
*Type:* STRUCT
Parameters to ComponentsRender callback.

**Members**

- `m_Collection` (HCollection) - Collection handle
- `m_World` (void*) - Component world
- `m_Context` (void*) - User context

### ComponentsUpdate
*Type:* TYPEDEF
Component update function. Updates all component of this type for all game objects

**Parameters**

- `params` (const dmGameObject::ComponentsUpdateParams&) - Update parameters
- `params` (dmGameObject::ComponentsUpdateResult&) - (out) Update result

**Returns**

- `result` (UpdateResult) - UPDATE_RESULT_OK on success

### ComponentsUpdateParams
*Type:* STRUCT
Parameters to ComponentsUpdate callback.

**Members**

- `m_Collection` (HCollection) - Collection handle
- `m_UpdateContext` (const UpdateContext*) - Update context
- `m_World` (void*) - Component world
- `m_Context` (void*) - User context

### ComponentsUpdateResult
*Type:* STRUCT
Parameters to ComponentsUpdate callback.

**Members**

- `m_TransformsUpdated` (bool) - True if a component type updated any game object transforms

### ComponentTypeCreateCtx
*Type:* STRUCT
Context used when registering a new component type

**Members**

- `m_Config` (dmConfigFile::HConfig) - The config file
- `m_Factory` (dmResource::HFactory) - The resource factory
- `m_Register` (dmGameObject::HRegister) - The game object registry
- `m_Script` (dmScript::HContext) - The shared script context
- `m_Contexts` (dmHashTable64<void*>) - Mappings between names and contextx

### ComponentTypeGetContext
*Type:* FUNCTION
get the component type global context

**Parameters**

- `type` (HComponentType) - the type

**Returns**

- `context` (void*) - component type global context

### ComponentTypeGetTypeIndex
*Type:* FUNCTION
Get the component type index. Used for with e.g. dmGameObject::GetWorld()/GetContext()

**Parameters**

- `type` (HComponentType) - the type

**Returns**

- `type_index` (uint32_t) - The type index.

### ComponentTypeSetAddToUpdateFn
*Type:* FUNCTION
Set the component add-to-update callback. Called for each component instal, when the game object is spawned.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentAddToUpdate) - callback

### ComponentTypeSetChildIteratorFn
*Type:* FUNCTION
set the component child iterator function. Called during inspection

**Parameters**

- `type` (HComponentType) - the type
- `fn` (dmGameObject::FIteratorChildren) - child iterator function

### ComponentTypeSetContext
*Type:* FUNCTION
Set the component type global context. Usually set when registering the component type.

**Parameters**

- `type` (HComponentType) - the type
- `context` (void*) - component type global context

### ComponentTypeSetCreateFn
*Type:* FUNCTION
Set the component create callback. Called when a component instance is created.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentCreate) - callback

### ComponentTypeSetDeleteWorldFn
*Type:* FUNCTION
Set the world destroy callback. Called when a collection (i.e. a "world") is destroyed.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentDeleteWorld) - callback

### ComponentTypeSetDestroyFn
*Type:* FUNCTION
Set the component destroy callback. Called when a component instance is destroyed.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentDestroy) - callback

### ComponentTypeSetFinalFn
*Type:* FUNCTION
Set the component finalize callback. Called on each gameobject's components, during a gameobject's finalization.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentFinal) - callback

### ComponentTypeSetFixedUpdateFn
*Type:* FUNCTION
Set the component update callback. Called when it's time to update all component instances.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentsUpdate) - callback

### ComponentTypeSetGetFn
*Type:* FUNCTION
Set the component get callback. Called when the scripts want to retrieve the individual component user data given an url.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentGet) - callback

### ComponentTypeSetGetPropertyFn
*Type:* FUNCTION
Set the component get property callback. Called when accessing a property via go.get()

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentGetProperty) - callback

### ComponentTypeSetHasUserData
*Type:* FUNCTION
Set the component type need for a per component instance user data. Defaults to true.

**Parameters**

- `type` (HComponentType) - the type
- `has_user_data` (bool) - does each component instance need user data

### ComponentTypeSetInitFn
*Type:* FUNCTION
Set the component init callback. Called on each gameobject's components, during a gameobject's initialization.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentInit) - callback

### ComponentTypeSetLateUpdateFn
*Type:* FUNCTION
Set the component late update callback. Called after regular update of all component instances but before render and before post update.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentsUpdate) - callback

### ComponentTypeSetNewWorldFn
*Type:* FUNCTION
Set the new world callback. Called when a collection (i.e. a "world") is created.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentNewWorld) - callback

### ComponentTypeSetOnInputFn
*Type:* FUNCTION
Set the component on-input callback. Called once per frame, before the Update function.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentOnInput) - callback

### ComponentTypeSetOnMessageFn
*Type:* FUNCTION
Set the component on-message callback. Called multiple times per frame, to flush messages.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentOnMessage) - callback

### ComponentTypeSetOnReloadFn
*Type:* FUNCTION
Set the component on-reload callback. Called when the resource of a component instance is reloaded.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentOnReload) - callback

### ComponentTypeSetPostUpdateFn
*Type:* FUNCTION
Set the component post update callback. Called for each collection after the update, before the render.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentsPostUpdate) - callback

### ComponentTypeSetPrio
*Type:* FUNCTION
Set the component type prio order. Defines the update order of the component types.

**Parameters**

- `type` (HComponentType) - the type
- `prio` (uint16_t) - prio order

### ComponentTypeSetPropertyIteratorFn
*Type:* FUNCTION
set the component property iterator function. Called during inspection

**Parameters**

- `type` (HComponentType) - the type
- `fn` (dmGameObject::FIteratorProperties) - property iterator function

### ComponentTypeSetReadsTransforms
*Type:* FUNCTION
Set the component type transform dependency flag.
If this flag is set, it might trigger an dmGameObject::UpdateTransforms() (if there are dirty transforms)

**Parameters**

- `type` (HComponentType) - the type
- `reads_transforms` (bool) - transform dependency flag

### ComponentTypeSetRenderFn
*Type:* FUNCTION
Set the component render callback. Called when it's time to render all component instances.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentsRender) - callback

### ComponentTypeSetSetPropertiesFn
*Type:* FUNCTION
Set the component set properties callback. Called when the component instance is being spwned.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentSetProperties) - callback

### ComponentTypeSetSetPropertyFn
*Type:* FUNCTION
Set the component set property callback. Called when accessing a property via go.set()

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentSetProperty) - callback

### ComponentTypeSetUpdateFn
*Type:* FUNCTION
Set the component update callback. Called when it's time to update all component instances.

**Parameters**

- `type` (HComponentType) - the type
- `fn` (ComponentsUpdate) - callback

### DM_DECLARE_COMPONENT_TYPE
*Type:* MACRO
Register a new component type

**Parameters**

- `symbol` (symbol) - The unique C++ symbol name
- `name` (const char*) - name of the component type (i.e. the resource suffix)
- `create_fn` (dmGameObject::Result (*fn)(const ComponentTypeCreateCtx* ctx, HComponentType type)) - The type configuration function. May not be 0.
- `destroy_fn` (dmGameObject::Result (*fn)(const ComponentTypeCreateCtx* ctx, HComponentType type)) - The type destruction function. May be 0.

### HComponentType
*Type:* TYPEDEF
Component type handle. It holds the life time functions for a type.
