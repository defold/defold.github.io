# Gui

**Namespace:** `dmGui`
**Language:** C++
**Type:** Defold C++
**File:** `gui.h`
**Source:** `engine/gui/src/dmsdk/gui/gui.h`
**Include:** `dmsdk/gui/gui.h`

Defold GUI system

## API

### AdjustMode
*Type:* ENUM

**Members**

- `ADJUST_MODE_FIT` - <div class="codehilite"><pre><span></span><code>//!&lt; 0
</code></pre></div>
- `ADJUST_MODE_ZOOM` - //!&lt; 1
- `ADJUST_MODE_STRETCH` - //!&lt; 2

### AdjustReference
*Type:* ENUM

**Members**

- `ADJUST_REFERENCE_PARENT`
- `ADJUST_REFERENCE_DISABLED`

### CustomProperty
*Type:* STRUCT
Custom GUI node property value.
String values returned from GetNodeCustomProperty() are owned by the GUI
scene and must not be freed by the caller. String values passed to
SetNodeCustomProperty() are copied.

**Members**

- `m_Type` (dmGui::CustomPropertyType) - the value type

### CustomPropertyType
*Type:* ENUM

**Members**

- `CUSTOM_PROPERTY_TYPE_NUMBER`
- `CUSTOM_PROPERTY_TYPE_BOOLEAN`
- `CUSTOM_PROPERTY_TYPE_HASH`
- `CUSTOM_PROPERTY_TYPE_STRING`
- `CUSTOM_PROPERTY_TYPE_VECTOR3`
- `CUSTOM_PROPERTY_TYPE_VECTOR4`
- `CUSTOM_PROPERTY_TYPE_QUAT`

### DeleteNode
*Type:* FUNCTION
Defer delete a node

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (dmGui::HNode) - the node to delete

### GetFirstChildNode
*Type:* FUNCTION
Get first child node

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (dmGui::HNode) - Gets the first child node. If 0, gets the first top level node.

**Returns**

- `child` (dmGui::HNode) - The first child node

### GetNextNode
*Type:* FUNCTION
Get next sibling

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (dmGui::HNode) - the current sibling

**Returns**

- `sibling` (dmGui::HNode) - the next sibling, or INVALID_HANDLE if no more siblings

### GetNodeCustomData
*Type:* FUNCTION
get node custom type

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (HNode) - the gui node

**Returns**

- `type` (uint32_t) - the custom type. Or 0 if it is no custom type

### GetNodeCustomData
*Type:* FUNCTION
get node custom data

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (HNode) - the gui node

**Returns**

- `data` (void*) - the custom data created per node by the gui node type extension

### GetNodeCustomProperty
*Type:* FUNCTION
Get a custom property from a GUI node.
String values returned in the output property are owned by the GUI scene
and must not be freed by the caller.

**Parameters**

- `scene` (dmGui::HScene) - scene
- `node` (dmGui::HNode) - node
- `key` (dmhash_t) - property name hash
- `prop` (dmGui::CustomProperty*) - output property

**Returns**

- `result` (dmGui::Result) - RESULT_OK on success

### GetNodeId
*Type:* FUNCTION
Get the id of a node.

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (dmGui::HNode) - the gui node

**Returns**

- `id` (dmhash_t) - the id of the node

### GetNodeIsBone
*Type:* FUNCTION
Query if the node is a bone

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (dmGui::HNode) - the gui node

**Returns**

- `result` (bool) - true if the node is a bone

### GetNodeParent
*Type:* FUNCTION
Get the parent of a gui node

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (dmGui::HNode) - the gui node

**Returns**

- `parent` (dmGui::HNode) - the parent, or INVALID_HANDLE is unsuccessful

### GetNodeProperty
*Type:* FUNCTION
Get property value

**Parameters**

- `scene` (dmGui::HScene) - scene
- `node` (dmGui::HNode) - node
- `property` (dmGui::Property) - property enum

**Returns**

- `value` (dmVMath::Vector4)

### GetNodeTextureId
*Type:* FUNCTION
get node texture

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (HNode) - the gui node

**Returns**

- `texture` (dmhash_t) - the currently assigned texture

### GetResource
*Type:* FUNCTION
Gets a resource by its resource alias.

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `resource_id` (dmhash_t) - the resource alias
- `suffix_with_dot` (dmhash_t) - the hash of the suffix: hash(".spinescenec")

**Returns**

- `resource` (void*) - the resource if successful

### HContext
*Type:* TYPEDEF
A handle to a gui context

### HNode
*Type:* TYPEDEF
A handle to a gui node

### HScene
*Type:* TYPEDEF
A handle to a gui scene

### HScript
*Type:* TYPEDEF
A handle to a gui script

### HTextureSource
*Type:* TYPEDEF
A handle to a texture source, which can be a pointer to a resource,
a dmGraphics::HTexture or a dynamic texture created from a gui script.

### INVALID_HANDLE
*Type:* FUNCTION
Invalid node handle

### LuaPushNode
*Type:* FUNCTION
Pushes a dmGui::HNode to the stack

**Parameters**

- `L` (lua_State*) - the Lua scene
- `scene` (dmGui::HScene) - the gui scene
- `node` (HNode) - the gui node

### NewNode
*Type:* FUNCTION

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `position` (dmVMath::Point3) - the position
- `size` (dmVMath::Vector3) - the size
- `node_type` (dmGui::NodeType) - the node type
- `custom_type` (uint32_t) - If node_type == dmGui::NODE_TYPE_CUSTOM, then this is used to create a custom node data for the registered custom type

**Returns**

- `node` (dmGui::HNode) - the created node

### NodeTextureType
*Type:* ENUM
This enum denotes what kind of texture type the m_Texture pointer is referencing.

**Members**

- `NODE_TEXTURE_TYPE_NONE`
- `NODE_TEXTURE_TYPE_TEXTURE`
- `NODE_TEXTURE_TYPE_TEXTURE_SET`

### Playback
*Type:* ENUM

**Members**

- `PLAYBACK_ONCE_FORWARD`
- `PLAYBACK_ONCE_BACKWARD`
- `PLAYBACK_ONCE_PINGPONG`
- `PLAYBACK_LOOP_FORWARD`
- `PLAYBACK_LOOP_BACKWARD`
- `PLAYBACK_LOOP_PINGPONG`
- `PLAYBACK_NONE`

### Property
*Type:* ENUM

**Members**

- `PROPERTY_POSITION` - //!&lt; 0
- `PROPERTY_ROTATION` - //!&lt; 1
- `PROPERTY_SCALE` - <div class="codehilite"><pre><span></span><code>  //!&lt; 2
</code></pre></div>
- `PROPERTY_COLOR` - <div class="codehilite"><pre><span></span><code>  //!&lt; 3
</code></pre></div>
- `PROPERTY_SIZE` - <div class="codehilite"><pre><span></span><code>   //!&lt; 4
</code></pre></div>
- `PROPERTY_OUTLINE` - <div class="codehilite"><pre><span></span><code>//!&lt; 5
</code></pre></div>
- `PROPERTY_SHADOW` - <div class="codehilite"><pre><span></span><code> //!&lt; 6
</code></pre></div>
- `PROPERTY_SLICE9` - <div class="codehilite"><pre><span></span><code> //!&lt; 7
</code></pre></div>
- `PROPERTY_PIE_PARAMS` - //!&lt; 8
- `PROPERTY_TEXT_PARAMS` - //!&lt; 9
- `PROPERTY_COUNT` - <div class="codehilite"><pre><span></span><code>  //!&lt; 10
</code></pre></div>

### Result
*Type:* ENUM

**Members**

- `NODE_TYPE_BOX` - //!&lt; 0,
- `NODE_TYPE_TEXT` - //!&lt; 1,
- `NODE_TYPE_PIE` - //!&lt; 2,
- `NODE_TYPE_TEMPLATE` - //!&lt; 3,
- `NODE_TYPE_PARTICLEFX` - //!&lt; 5,
- `NODE_TYPE_CUSTOM` - //!&lt; 6,
- `NODE_TYPE_COUNT` - //!&lt; 7,

### Result
*Type:* ENUM

**Members**

- `RESULT_OK` - //!&lt; 0
- `RESULT_SYNTAX_ERROR` - //!&lt; -1
- `RESULT_SCRIPT_ERROR` - //!&lt; -2
- `RESULT_OUT_OF_RESOURCES` - //!&lt; -4
- `RESULT_RESOURCE_NOT_FOUND` - //!&lt; -5
- `RESULT_TEXTURE_ALREADY_EXISTS` - //!&lt; -6
- `RESULT_INVAL_ERROR` - //!&lt; -7
- `RESULT_INF_RECURSION` - //!&lt; -8
- `RESULT_DATA_ERROR` - //!&lt; -9
- `RESULT_WRONG_TYPE` - //!&lt; -10

### SetNodeAdjustMode
*Type:* FUNCTION
Set adjust mode

**Parameters**

- `scene` (dmGui::HScene) - scene
- `node` (dmGui::HNode) - node
- `adjust_mode` (AdjustMode) - the adjust mode

### SetNodeCustomProperty
*Type:* FUNCTION
Set a custom property on a GUI node.
String values are copied, and the caller retains ownership of the input
string.

**Parameters**

- `scene` (dmGui::HScene) - scene
- `node` (dmGui::HNode) - node
- `key` (dmhash_t) - property name hash
- `prop` (const dmGui::CustomProperty*) - property value

**Returns**

- `result` (dmGui::Result) - RESULT_OK on success

### SetNodeId
*Type:* FUNCTION
Set the id of a node.

**Notes**

- The id must be unique

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (dmGui::HNode) - the gui node
- `id` (dmhash_t) - the id

### SetNodeIsBone
*Type:* FUNCTION
Set the bone state of the node

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (dmGui::HNode) - the gui node
- `is_bone` (bool) - true if the node is ot be used as a bone

### SetNodeParent
*Type:* FUNCTION
Set the parent of a gui node

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (dmGui::HNode) - the gui node
- `parent` (dmGui::HNode) - the new parent. May be null
- `keep_scene_transform` (bool) - true to keep the world position

**Returns**

- `result` (dmGui::Result) - dmGui::RESULT_OK is successful

### SetNodeProperty
*Type:* FUNCTION
Set property value

**Parameters**

- `scene` (dmGui::HScene) - scene
- `node` (dmGui::HNode) - node
- `property` (dmGui::Property) - property enum
- `value` (dmVMath::Vector4)

### SetNodeTexture
*Type:* FUNCTION
set node texture

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (HNode) - the gui node
- `texture_id` (dmhash_t) - the texture id

### SetNodeTexture
*Type:* FUNCTION
set node texture

**Parameters**

- `scene` (dmGui::HScene) - the gui scene
- `node` (HNode) - the gui node
- `type` (NodeTextureType) - the type of texture
- `texture` (void*) - A pointer to a e.g. dmGameSystem::TextureSetResource*
