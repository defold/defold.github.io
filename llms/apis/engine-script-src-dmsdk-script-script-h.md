# Script

**Namespace:** `dmScript`
**Language:** C++
**Type:** Defold C++
**File:** `script.h`
**Source:** `engine/script/src/dmsdk/script/script.h`
**Include:** `dmsdk/script/script.h`

Built-in scripting functions.

## API

### CheckHash
*Type:* FUNCTION
Check if the value in the supplied index on the lua stack is a hash.

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `value` (hash) - The hash value

### CheckHashOrString
*Type:* FUNCTION
Check if the value in the supplied index on the lua stack is a hash or string.
If it is a string, it gets hashed on the fly

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `value` (hash) - The hash value

### CheckMatrix4
*Type:* FUNCTION
Check if the value in the supplied index on the lua stack is a dmVMath::Matrix4.

**Notes**

- throws a luaL_error if it's not the correct type

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `matrix` (dmVMath::Matrix4*) - The pointer to the value

### CheckQuat
*Type:* FUNCTION
Check if the value in the supplied index on the lua stack is a dmVMath::Quat.

**Notes**

- throws a luaL_error if it's not the correct type

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `quat` (dmVMath::Quat*) - The pointer to the value

### CheckTable
*Type:* FUNCTION
Serialize a table to a buffer
Supported types: LUA_TBOOLEAN, LUA_TNUMBER, LUA_TSTRING, Point3, Vector3, Vector4 and Quat
Keys must be strings

**Parameters**

- `L` (lua_State*) - Lua state
- `buffer` (char*) - Buffer that will be written to (must be DM_ALIGNED(16))
- `buffer_size` (uint32_t) - Buffer size
- `index` (int) - Index of the table

**Returns**

- `result` (uint32_t) - Number of bytes used in buffer

### CheckURL
*Type:* FUNCTION
Check if the value in the supplied index on the lua stack is a dmMessage::URL and returns it if so.

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `url` (dmMessage::URL*) - The pointer to the value

### CheckURL
*Type:* FUNCTION
Get the current game object URL

**Parameters**

- `L` (lua_State*) - Lua state
- `out_url` (dmMessage::URL*) - where to store the result

**Returns**

- `result` (bool) - true if successful

### CheckVector3
*Type:* FUNCTION
Check if the value in the supplied index on the lua stack is a dmVMath::Vector3.

**Notes**

- throws a luaL_error if it's not the correct type

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `vector3` (dmVMath::Vector3*) - The pointer to the value

### CheckVector4
*Type:* FUNCTION
Check if the value in the supplied index on the lua stack is a dmVMath::Vector3.

**Notes**

- throws a luaL_error if it's not the correct type

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `vector4` (dmVMath::Vector4*) - The pointer to the value

### CreateCallback
*Type:* FUNCTION
Stores the current Lua state plus references to the script instance (self) and the callback.
Expects SetInstance() to have been called prior to using this method.
The allocated data is created on the Lua stack and references are made against the
instances own context table.
If the callback is not explicitly deleted with DestroyCallback() the references and
data will stay around until the script instance is deleted.

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Lua stack index of the function

**Returns**

- `callback` (LuaCallbackInfo*) - Lua callback struct if successful, 0 otherwise

**Examples**

```
static int SomeFunction(lua_State* L) // called from Lua
{
    LuaCallbackInfo* cbk = dmScript::CreateCallback(L, 1);
    ... store the callback for later
}

static void InvokeCallback(LuaCallbackInfo* cbk)
{
    lua_State* L = dmScript::GetCallbackLuaContext(cbk);
    DM_LUA_STACK_CHECK(L, 0);

    if (!dmScript::SetupCallback(callback))
    {
        return;
    }

    lua_pushstring(L, "hello");

    dmScript::PCall(L, 2, 0); // self + # user arguments

    dmScript::TeardownCallback(callback);
    dmScript::DestroyCallback(cbk); // only do this if you're not using the callback again
}

```

### DestroyCallback
*Type:* FUNCTION
Deletes the Lua callback

**Parameters**

- `cbk` (LuaCallbackInfo*) - Lua callback struct

### DM_LUA_ERROR
*Type:* MACRO
This macro will verify that the Lua stack size hasn't been changed before
throwing a Lua error, which will long-jump out of the current function.
This macro can only be used together with DM_LUA_STACK_CHECK and should
be prefered over manual checking of the stack.

**Parameters**

- `fmt` (const char*) - Format string that contains error information.
- `args` (...) - Format string args (variable arg list)

**Examples**

```
static int ModuleFunc(lua_State* L)
{
    DM_LUA_STACK_CHECK(L, 1);
    if (some_error_check(L))
    {
        return DM_LUA_ERROR("some error message");
    }
    lua_pushnumber(L, 42);
    return 1;
}

```

### DM_LUA_STACK_CHECK
*Type:* MACRO
Diff is the expected difference of the stack size.
If luaL_error, or another function that executes a long-jump, is part of the executed code,
the stack guard cannot be guaranteed to execute at the end of the function.
In that case you should manually check the stack using lua_gettop.
In the case of luaL_error, see DM_LUA_ERROR.

**Parameters**

- `L` (lua_State*) - lua state
- `diff` (int) - Number of expected items to be on the Lua stack once this struct goes out of scope

**Examples**

```
DM_LUA_STACK_CHECK(L, 1);
lua_pushnumber(L, 42);

```

### GetCallbackLuaContext
*Type:* FUNCTION
Gets the Lua context from a callback struct

**Parameters**

- `cbk` (LuaCallbackInfo*) - Lua callback struct

**Returns**

- `L` (lua_State*) - Lua state

### GetInstance
*Type:* FUNCTION
Retrieve current script instance from the global table and place it on the top of the stack, only valid when set.
(see dmScript::GetMainThread)

**Parameters**

- `L` (lua_State*) - lua state

### GetLuaState
*Type:* FUNCTION
Retrieve Lua state from the context

**Parameters**

- `context` (HContext) - the script context

**Returns**

- `state` (lua_State*) - the lua state

### GetMainThread
*Type:* FUNCTION
Retrieve the main thread lua state from any lua state (main thread or coroutine).

**Parameters**

- `L` (lua_State*) - lua state

**Returns**

- `lua_State` (lua_State*) - the main thread lua state

**Examples**

How to create a Lua callback
```
dmScript::LuaCallbackInfo* g_MyCallbackInfo = 0;

static void InvokeCallback(dmScript::LuaCallbackInfo* cbk)
{
    if (!dmScript::IsCallbackValid(cbk))
        return;

    lua_State* L = dmScript::GetCallbackLuaContext(cbk);
    DM_LUA_STACK_CHECK(L, 0)

    if (!dmScript::SetupCallback(cbk))
    {
        dmLogError("Failed to setup callback");
        return;
    }

    lua_pushstring(L, "Hello from extension!");
    lua_pushnumber(L, 76);

    dmScript::PCall(L, 3, 0); // instance + 2

    dmScript::TeardownCallback(cbk);
}

static int Start(lua_State* L)
{
    DM_LUA_STACK_CHECK(L, 0);

    g_MyCallbackInfo = dmScript::CreateCallback(L, 1);

    return 0;
}

static int Update(lua_State* L)
{
    DM_LUA_STACK_CHECK(L, 0);

    static int count = 0;
    if( count++ == 5 )
    {
        InvokeCallback(g_MyCallbackInfo);
        if (g_MyCallbackInfo)
            dmScript::DestroyCallback(g_MyCallbackInfo);
        g_MyCallbackInfo = 0;
    }
    return 0;
}

```

### GetStringFromHashOrString
*Type:* FUNCTION
Gets as good as possible printable string from a hash or string

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value
- `buffer` (char*) - buffer receiving the value
- `buffer_length` (uint32_t) - the buffer length

**Returns**

- `string` (const char*) - Returns buffer. If buffer is non null, it will always contain a null terminated string. "<unknown>" if the hash could not be looked up.

### HContext
*Type:* TYPEDEF
The script context

### IsCallbackValid
*Type:* FUNCTION
Check if Lua callback is valid.

**Parameters**

- `cbk` (LuaCallbackInfo*) - Lua callback struct

### IsHash
*Type:* FUNCTION
Check if the value at #index is a hash

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `result` (bool) - true if the value at #index is a hash

### IsInstanceValid
*Type:* FUNCTION
Check if the script instance in the lua state is valid. The instance is assumed to have been previously set by dmScript::SetInstance.

**Parameters**

- `L` (lua_State*) - lua state

**Returns**

- `boolean` (bool) - Returns true if the instance is valid

### IsMatrix4
*Type:* FUNCTION
Check if the value at #index is a dmVMath::Matrix4*

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `true` (bool) - if value at #index is a dmVMath::Matrix4*

### IsQuat
*Type:* FUNCTION
Check if the value at #index is a dmVMath::Quat*

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `true` (bool) - if value at #index is a dmVMath::Quat*

### IsURL
*Type:* FUNCTION
Check if the value at #index is a URL

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `result` (bool) - true if the value at #index is a URL

### IsVector3
*Type:* FUNCTION
Check if the value at #index is a dmVMath::Vector3*

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `true` (bool) - if value at #index is a dmVMath::Vector3*

### IsVector4
*Type:* FUNCTION
Check if the value at #index is a dmVMath::Vector4*

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `true` (bool) - if value at #index is a dmVMath::Vector4*

### JsonToLua
*Type:* FUNCTION
Convert a Json string to Lua table.

**Notes**

- Throws Lua error if it fails to parser the json

**Parameters**

- `L` (lua_State*) - lua state
- `json` (const char*) - json string
- `json_len` (size_t) - length of json string

**Returns**

- `int` (int) - 1 if it succeeds. Throws a Lua error if it fails

### LuaCallbackInfo
*Type:* STRUCT
callback info struct that will hold the relevant info needed to make a callback into Lua

### LuaToJson
*Type:* FUNCTION
Convert a Lua table to a Json string

**Parameters**

- `L` (lua_State*) - lua state
- `json` (char**) - [out] Pointer to char*, which will receive a newly allocated string. Use free().
- `json_len` (size_t*) - length of json string

**Returns**

- `int` (int) - &lt;0 if it fails. &gt;=0 if it succeeds.

### PCall
*Type:* FUNCTION
This function wraps lua_pcall with the addition of specifying an error handler which produces a backtrace.
In the case of an error, the error is logged and popped from the stack.

**Parameters**

- `L` (lua_State*) - lua state
- `nargs` (int) - number of arguments
- `nresult` (int) - number of results

**Returns**

- `error` (int) - error code from pcall

### PushDDF
*Type:* FUNCTION
Push DDF message to Lua stack

**Parameters**

- `L` (lua_State*) - the Lua state
- `descriptor` (const dmDDF::Descriptor*) - field descriptor
- `data` (const char*) - the message data (i.e. the message struct)
- `pointers_are_offsets` (bool) - True if pointers are offsets

### PushHash
*Type:* FUNCTION
Push a hash value onto the supplied lua state, will increase the stack by 1.

**Parameters**

- `L` (lua_State*) - Lua state
- `hash` (dmhash_t) - Hash value to push

### PushMatrix4
*Type:* FUNCTION
Push a matrix4 value onto the Lua stack. Will increase the stack by 1.

**Parameters**

- `L` (lua_State*) - Lua state
- `matrix` (dmVMath::Matrix4) - dmVMath::Matrix4 value to push

### PushQuat
*Type:* FUNCTION
Push a quaternion value onto Lua stack. Will increase the stack by 1.

**Parameters**

- `L` (lua_State*) - Lua state
- `quat` (dmVMath::Quat) - dmVMath::Quat value to push

### PushURL
*Type:* FUNCTION
Push a URL value onto the supplied lua state, will increase the stack by 1.

**Parameters**

- `L` (lua_State*) - Lua state
- `url` (dmMessage::URL&) - URL reference to push

### PushVector3
*Type:* FUNCTION
Push a dmVMath::Vector3 value onto the supplied lua state, will increase the stack by 1.

**Parameters**

- `L` (lua_State*) - Lua state
- `v` (dmVMath::Vector3) - Vector3 value to push

### PushVector4
*Type:* FUNCTION
Push a dmVMath::Vector4 value onto the supplied lua state, will increase the stack by 1.

**Parameters**

- `L` (lua_State*) - Lua state
- `v` (dmVMath::Vector4) - dmVMath::Vector4 value to push

### Ref
*Type:* FUNCTION
Creates and returns a reference, in the table at index t, for the object at the
top of the stack (and pops the object).
It also tracks number of global references kept.

**Parameters**

- `L` (lua_State*) - lua state
- `table` (int) - table the lua table that stores the references. E.g LUA_REGISTRYINDEX

**Returns**

- `reference` (int) - the new reference

### RefInInstance
*Type:* FUNCTION
Creates a reference to the value at top of stack, the ref is done in the
current instances context table.
Expects SetInstance() to have been set with an value that has a meta table
with META_GET_INSTANCE_CONTEXT_TABLE_REF method.

**Parameters**

- `L` (lua_State*) - Lua state

**Returns**

- `lua` (int) - ref to value or LUA_NOREF
Lua stack on entry
 [-1] value
Lua stack on exit

### RefInInstance
*Type:* FUNCTION
Resolves a url in string format into a dmMessage::URL struct.
Special handling for:
- "." returns the default socket + path
- "#" returns default socket + path + fragment

**Parameters**

- `L` (lua_State*) - Lua state
- `url` (const char*) - url
- `out_url` (dmMessage::URL*) - where to store the result
- `default_url` (dmMessage::URL*) - default url

**Returns**

- `result` (dmMessage::Result) - dmMessage::RESULT_OK if the conversion succeeded

### ResolveURL
*Type:* FUNCTION
Resolves the value in the supplied index on the lua stack to a URL. It long jumps (calls luaL_error) on failure.
It also gets the current (caller) url if the a pointer is passed to out_default_url

**Parameters**

- `L` (lua_State*) - Lua state
- `out_url` (dmMessage::URL*) - where to store the result
- `out_default_url` (dmMessage::URL*) - default URL used in the resolve, can be 0x0 (not used)

**Returns**

- `result` (int) - 0 if successful. Throws Lua error on failure

### SetInstance
*Type:* FUNCTION
Sets the current script instance
Set the value on the top of the stack as the instance into the global table and pops it from the stack.
(see dmScript::GetMainThread)

**Parameters**

- `L` (lua_State*) - lua state

### SetupCallback
*Type:* FUNCTION
The Lua stack after a successful call:
```
   [-4] old instance
   [-3] context table
   [-2] callback
   [-1] self

```

In the event of an unsuccessful call, the Lua stack is unchanged

**Parameters**

- `cbk` (LuaCallbackInfo*) - Lua callback struct

**Returns**

- `true` (bool) - if the setup was successful

### TeardownCallback
*Type:* FUNCTION
Sets the previous instance
Expects Lua stack:
```
   [-2] old instance
   [-1] context table

```

Both values are removed from the stack

**Parameters**

- `cbk` (LuaCallbackInfo*) - Lua callback struct

### ToHash
*Type:* FUNCTION
Check if the value at #index is a hash

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `hash` (dmhash_t*) - pointer to hash or 0 if it's not a hash

### ToMatrix4
*Type:* FUNCTION
Get the value at index as a dmVMath::Matrix4*

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `quat` (dmVMath::Matrix4*) - The pointer to the value, or 0 if not correct type

### ToQuat
*Type:* FUNCTION
Get the value at index as a dmVMath::Quat*

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `quat` (dmVMath::Quat*) - The pointer to the value, or 0 if not correct type

### ToURL
*Type:* FUNCTION
get the value at index as a dmMessage::URL*

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `hash` (dmhash_t*) - pointer to URL or 0 if it's not a URL

### ToVector3
*Type:* FUNCTION
Get the value at index as a dmVMath::Vector3*

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `v` (dmVMath::Vector3*) - The pointer to the value, or 0 if not correct type

### ToVector4
*Type:* FUNCTION
Get the value at index as a dmVMath::Vector4*

**Parameters**

- `L` (lua_State*) - Lua state
- `index` (int) - Index of the value

**Returns**

- `v` (dmVMath::Vector4*) - The pointer to the value, or 0 if not correct type

### Unref
*Type:* FUNCTION
Releases reference ref from the table at index t (see luaL_ref).
The entry is removed from the table, so that the referred object can be collected.
It also decreases the number of global references kept

**Parameters**

- `L` (lua_State*) - lua state
- `table` (int) - table the lua table that stores the references. E.g LUA_REGISTRYINDEX
- `reference` (int) - the reference to the object

### UnrefInInstance
*Type:* FUNCTION
Deletes the instance local lua reference
Expects SetInstance() to have been set with an value that has a meta table
with META_GET_INSTANCE_CONTEXT_TABLE_REF method.

**Parameters**

- `L` (lua_State*) - Lua state
- `ref` (int) - ref to value or LUA_NOREF
Lua stack on entry
Lua stack on exit

### UrlToString
*Type:* FUNCTION
Converts a URL into a readable string. Useful for e.g. error messages

**Parameters**

- `url` (dmMessage::URL*) - url
- `buffer` (char*) - the output buffer
- `buffer_size` (uint32_t) - the output buffer size

**Returns**

- `buffer` (const char*) - returns the passed in buffer
