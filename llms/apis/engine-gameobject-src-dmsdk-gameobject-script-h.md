# Script

**Namespace:** `dmGameObject`
**Language:** C++
**Type:** Defold C++
**File:** `script.h`
**Source:** `engine/gameobject/src/dmsdk/gameobject/script.h`
**Include:** `dmsdk/gameobject/script.h`

SDK GameObject script API documentation

## API

### PostDDF
*Type:* FUNCTION
Sends a script message. Wraps the message in a dmGameSystemDDF::ScriptMessage struct.

**Template Parameters**

- `T`

**Parameters**

- `message` (T*) - The ddf message to send
- `sender` (dmMessage::Message*) - The sender
- `receiver` (dmMessage::Message*) - The receiver
- `function_ref` (int) - The function ref. 0 wil cause the "on_message" to be called
- `unref_function_after_call` (bool) - call dmScript::UnrefInInstance on the function_ref after the dmScript::PCall is made

**Returns**

- `success` (bool) - true if successful

### PostScriptUnrefMessage
*Type:* FUNCTION
Sends a script message to unreference a script object

**Parameters**

- `sender` (dmMessage::Message*) - The sender
- `receiver` (dmMessage::Message*) - The receiver
- `reference` (int) - The reference to remove

**Returns**

- `success` (Result) - RESULT_OK if successful

### PropertyContainerCreateFromLua
*Type:* FUNCTION
Creates a property container from a lua table

**Parameters**

- `L` (lua_State*) - The lua state
- `index` (int) - The lua stack index of the lua table

**Returns**

- `container` (HPropertyContainer) - The property container
