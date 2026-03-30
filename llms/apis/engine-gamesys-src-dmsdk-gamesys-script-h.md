# Script

**Namespace:** `dmScript`
**Language:** C++
**Type:** Defold C++
**File:** `script.h`
**Source:** `engine/gamesys/src/dmsdk/gamesys/script.h`
**Include:** `dmsdk/gamesys/script.h`

Built-in scripting functions.

## API

### CheckCollection
*Type:* FUNCTION
Get current gameobject's collection handle

**Notes**

- Works from both a .script/.gui_script

**Parameters**

- `L` (lua_State*) - lua state
- `index` (int) - lua-arg

**Returns**

- `instance` (lua_State*) - gameobject instance

### CheckGOInstance
*Type:* FUNCTION
Get current game object instance
Works in both gameobjects and gui scripts

**Parameters**

- `L` (lua_State*) - lua state

**Returns**

- `instance` (dmGameObject::HInstance)

### CheckGOInstance
*Type:* FUNCTION
Get gameobject instance
The instance reference (url) at stack index "index" will be resolved to an instance.

**Notes**

- The function only accepts instances in "this" collection. Otherwise a lua-error will be raised.

**Parameters**

- `L` (lua_State*) - lua state
- `index` (int) - lua-arg

**Returns**

- `instance` (dmGameObject::HInstance) - gameobject instance

**Examples**

How to get the position of a gameobject in a script extension
```
static int get_position(lua_State* L)
{
    DM_LUA_STACK_CHECK(L, 3);
    dmGameObject::HInstance instance = dmScript::CheckGOInstance(L, 1);
    dmVMath::Point3 position = dmGameObject::GetPosition(instance);
    lua_pushnumber(L, position.getX());
    lua_pushnumber(L, position.getY());
    lua_pushnumber(L, position.getZ());
    return 3;
}

```

### dmScript::CheckBuffer
*Type:* FUNCTION
Retrieve a LuaHBuffer from the supplied lua state.
Check if the value in the supplied index on the lua stack is a LuaHBuffer and returns it.

**Notes**

- The dmBuffer::IsBufferValid is already called on the returned buffer

**Parameters**

- `L` (lua_State*) - lua state
- `index` (int) - Index of the value

**Returns**

- `buffer` (LuaHBuffer*) - pointer to dmScript::LuaHBuffer

### dmScript::CheckBufferNoError
*Type:* FUNCTION
Retrieve a LuaHBuffer from the supplied lua state.
Check if the value in the supplied index on the lua stack is a LuaHBuffer and returns it.

**Notes**

- Returns 0 on error. Does not invoke lua_error.
- deprecated. Prefer ToBuffer() instead.
- The dmBuffer::IsBufferValid is already called on the returned buffer

**Parameters**

- `L` (lua_State*) - lua state
- `index` (int) - Index of the value

**Returns**

- `buffer` (LuaHBuffer*) - pointer to dmScript::LuaHBuffer or 0 if not valid

### dmScript::CheckBufferUnpack
*Type:* FUNCTION
Retrieve a HBuffer from the supplied lua state
Check if the value in the supplied index on the lua stack is a LuaHBuffer and it's valid, returns the HBuffer.

**Notes**

- The dmBuffer::IsBufferValid is already called on the returned buffer

**Parameters**

- `L` (lua_State*) - lua state
- `index` (int) - Index of the value

**Returns**

- `buffer` (dmBuffer::HBuffer) - buffer if valid, 0 otherwise

### dmScript::CheckBufferUnpackNoError
*Type:* FUNCTION
Retrieve a HBuffer from the supplied lua state
Check if the value in the supplied index on the lua stack is a LuaHBuffer and it's valid, returns the HBuffer.

**Notes**

- The dmBuffer::IsBufferValid is already called on the returned buffer

**Parameters**

- `L` (lua_State*) - lua state
- `index` (int) - Index of the value

**Returns**

- `buffer` (dmBuffer::HBuffer) - buffer if valid, 0 otherwise

### dmScript::IsBuffer
*Type:* FUNCTION
Check if the value is a dmScript::LuaHBuffer

**Parameters**

- `L` (lua_State*) - lua state
- `index` (int) - Index of the value

**Returns**

- `boolean` (boolean) - True if value at index is a LuaHBuffer

### dmScript::LuaHBuffer
*Type:* STRUCT
Holds info about the buffer and who owns it.

**Members**

- `Union` - of
    - m_BufferRes [type:void*]                       A buffer resource
    - m_Buffer    [type:dmBuffer::HBuffer]           A buffer
- `m_Buffer` (dmBuffer::HBuffer) - The buffer (or resource)
- `m_Owner` (dmScript::LuaBufferOwnership) - What ownership the pointer has

**Examples**

See examples for dmScript::PushBuffer()

### dmScript::PushBuffer
*Type:* FUNCTION
Will increase the stack by 1.

**Parameters**

- `L` (lua_State*) - lua state
- `buffer` (dmScript::LuaHBuffer) - buffer to push

**Examples**

How to push a buffer and give Lua ownership of the buffer (GC)
```
dmScript::LuaHBuffer luabuf(buffer, dmScript::OWNER_LUA);
PushBuffer(L, luabuf);

```

How to push a buffer and keep ownership in C++
```
dmScript::LuaHBuffer luabuf(buffer, dmScript::OWNER_C);
PushBuffer(L, luabuf);

```

### dmScript::ToBuffer
*Type:* FUNCTION
Retrieve a LuaHBuffer from the supplied lua state.
Check if the value in the supplied index on the lua stack is a LuaHBuffer and returns it.

**Notes**

- Returns 0 on error. Does not invoke lua_error.
- The dmBuffer::IsBufferValid is already called on the returned buffer

**Parameters**

- `L` (lua_State*) - lua state
- `index` (int) - Index of the value

**Returns**

- `buffer` (LuaHBuffer*) - pointer to dmScript::LuaHBuffer or 0 if not valid

### GetComponentFromLua
*Type:* FUNCTION
Get component user data from a url.

**Notes**

- The object referenced by the url must be in the same collection as the caller.

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - index to argument (a url)
- `component_type` (const char*) - E.g. "factoryc". The call will fail if the found component does not have the specified extension
- `world` (dmGameObject::HComponentWorld*) - The world associated owning the component. May be 0
- `component` (dmGameObject::HComponent*) - The component data associated with the url. May be 0
- `url` (dmMessage::URL*) - The resolved url. May be 0

### LuaBufferOwnership
*Type:* ENUM
Buffer ownership.
 - OWNER_C   - m_Buffer is owned by C side, should not be destroyed when GCed
 - OWNER_LUA - m_Buffer is owned by Lua side, will be destroyed when GCed
 - OWNER_RES - m_Buffer not used, has a reference to a buffer resource instead. m_BufferRes is owned by C side, will be released when GCed

**Members**

- `dmScript::OWNER_C`
- `dmScript::OWNER_LUA`
- `dmScript::OWNER_RES`
