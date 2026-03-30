# Profile

**Namespace:** `dmProfile`
**Language:** C++
**Type:** Defold C++
**File:** `profile.h`
**Source:** `engine/dlib/src/dmsdk/dlib/profile.h`
**Include:** `dmsdk/dlib/profile.h`

Profiling macros

## API

### DM_PROFILE
*Type:* MACRO
Adds a profiling scope. Excluded by default in release builds.

**Parameters**

- `a` (const char*) - A name for the scope

**Examples**

Profile a scope
```
{
    DM_PROFILE("DoWork");
    DoWork1();
    DoWork2();
}

```

### DM_PROFILE_DYN
*Type:* MACRO
Adds a profiling scope. Excluded by default in release builds.
Accepts a name cache value for performance.

**Parameters**

- `a` (const char*) - The scope name
- `a` (uint64_t*) - The scope name hash value pointer. May be 0.

**Examples**

Create a dynamic profiling scope
```
{
    DM_PROFILE_DYN(work->m_Name, &work->m_NameHash);
    work->DoWork();
}

```

### DM_PROFILE_TEXT
*Type:* MACRO
Send text to the profiler

**Notes**

- The max length of the text is DM_PROFILE_TEXT_LENGTH (1024)

**Parameters**

- `a` (const char*) - The format string
- `a` (va_list) - The variable argument list

**Examples**

Send a string to the profiler
```
DM_PROFILE_TEXT("Some value: %d", value);

```

### DM_PROPERTY_ADD_F32
*Type:* MACRO
Add a value to float property

**Parameters**

- `name` (symbol) - The property
- `value` (float) - The value

**Examples**

```
DM_PROPERTY_ADD_F32(rmtp_MyValue, 1.5);

```

### DM_PROPERTY_ADD_F64
*Type:* MACRO
Add a value to double property

**Parameters**

- `name` (symbol) - The property
- `value` (double) - The value

**Examples**

```
DM_PROPERTY_ADD_F64(rmtp_MyValue, 1.5);

```

### DM_PROPERTY_ADD_S32
*Type:* MACRO
Add a value to int32_t property

**Parameters**

- `name` (symbol) - The property
- `value` (int32_t) - The value

**Examples**

```
DM_PROPERTY_ADD_S32(rmtp_MyValue, -1);

```

### DM_PROPERTY_ADD_S64
*Type:* MACRO
Add a value to int64_t property

**Parameters**

- `name` (symbol) - The property
- `value` (int64_t) - The value

**Examples**

```
DM_PROPERTY_ADD_S64(rmtp_MyValue, -1);

```

### DM_PROPERTY_ADD_U32
*Type:* MACRO
Add a value to uint32_t property

**Parameters**

- `name` (symbol) - The property
- `value` (uint32_t) - The value

**Examples**

```
DM_PROPERTY_ADD_U32(rmtp_MyValue, 1);

```

### DM_PROPERTY_ADD_U64
*Type:* MACRO
Add a value to uint64_t property

**Parameters**

- `name` (symbol) - The property
- `value` (uint64_t) - The value

**Examples**

```
DM_PROPERTY_ADD_U64(rmtp_MyValue, 1);

```

### DM_PROPERTY_BOOL
*Type:* MACRO
Declare a property of type bool

**Parameters**

- `name` (symbol) - The property symbol/name
- `default` (bool) - The default value
- `flags` (uint32_t) - The flags. Either <code>PROFILE_PROPERTY_NONE</code> or <code>PROFILE_PROPERTY_FRAME_RESET</code>. <code>PROFILE_PROPERTY_FRAME_RESET</code> makes the value reset each frame.
- `desc` (const char*) - The description
- `group` (ProfileIdx*) - The parent group. May be 0.

**Examples**

```
DM_PROPERTY_BOOL(rmtp_MyBool, 0, PROFILE_PROPERTY_FRAME_RESET, "true or false", &rmtp_MyGroup);

```

### DM_PROPERTY_EXTERN
*Type:* MACRO
Declare an extern property

**Parameters**

- `name` (symbol) - The symbol name

**Examples**

Use a property declared elsewhere in the same library
```
DM_PROPERTY_EXTERN(rmtp_GameObject);
DM_PROPERTY_U32(rmtp_ComponentsAnim, 0, PROFILE_PROPERTY_FRAME_RESET, "#", &rmtp_GameObject);

```

### DM_PROPERTY_F32
*Type:* MACRO
Declare a property of type float

**Parameters**

- `name` (symbol) - The property symbol/name
- `default` (float) - The default value
- `flags` (uint32_t) - The flags. Either <code>PROFILE_PROPERTY_NONE</code> or <code>PROFILE_PROPERTY_FRAME_RESET</code>. <code>PROFILE_PROPERTY_FRAME_RESET</code> makes the value reset each frame.
- `desc` (const char*) - The description
- `group` (ProfileIdx*) - The parent group. May be 0.

**Examples**

```
DM_PROPERTY_F32(rmtp_MyValue, 0, PROFILE_PROPERTY_FRAME_RESET, "a value", &rmtp_MyGroup);

```

### DM_PROPERTY_F64
*Type:* MACRO
Declare a property of type double

**Parameters**

- `name` (symbol) - The property symbol/name
- `default` (double) - The default value
- `flags` (uint32_t) - The flags. Either <code>PROFILE_PROPERTY_NONE</code> or <code>PROFILE_PROPERTY_FRAME_RESET</code>. <code>PROFILE_PROPERTY_FRAME_RESET</code> makes the value reset each frame.
- `desc` (const char*) - The description
- `group` (ProfileIdx*) - The parent group. May be 0.

**Examples**

```
DM_PROPERTY_F64(rmtp_MyValue, 0, PROFILE_PROPERTY_FRAME_RESET, "a value", &rmtp_MyGroup);

```

### DM_PROPERTY_GROUP
*Type:* MACRO
Declare a property group

**Parameters**

- `name` (symbol) - The group name
- `desc` (const char*) - The description
- `parent` (ProfileIdx*) - pointer to parent property

**Examples**

```
DM_PROPERTY_GROUP(rmtp_GameObject, "My Group", 0);

```

### DM_PROPERTY_RESET
*Type:* MACRO
Reset a property to its default value

**Parameters**

- `name` (symbol) - The property

**Examples**

```
DM_PROPERTY_RESET(rmtp_MyValue);

```

### DM_PROPERTY_S32
*Type:* MACRO
Declare a property of type int32_t

**Parameters**

- `name` (symbol) - The property symbol/name
- `default` (int32_t) - The default value
- `flags` (uint32_t) - The flags. Either <code>PROFILE_PROPERTY_NONE</code> or <code>PROFILE_PROPERTY_FRAME_RESET</code>. <code>PROFILE_PROPERTY_FRAME_RESET</code> makes the value reset each frame.
- `desc` (const char*) - The description
- `group` (ProfileIdx*) - The parent group. May be 0.

**Examples**

```
DM_PROPERTY_S32(rmtp_MyValue, 0, PROFILE_PROPERTY_FRAME_RESET, "a value", &rmtp_MyGroup);

```

### DM_PROPERTY_S64
*Type:* MACRO
Declare a property of type int64_t

**Parameters**

- `name` (symbol) - The property symbol/name
- `default` (int64_t) - The default value
- `flags` (uint32_t) - The flags. Either <code>PROFILE_PROPERTY_NONE</code> or <code>PROFILE_PROPERTY_FRAME_RESET</code>. <code>PROFILE_PROPERTY_FRAME_RESET</code> makes the value reset each frame.
- `desc` (const char*) - The description
- `group` (ProfileIdx*) - The parent group. May be 0.

**Examples**

```
DM_PROPERTY_S64(rmtp_MyValue, 0, PROFILE_PROPERTY_FRAME_RESET, "a value", &rmtp_MyGroup);

```

### DM_PROPERTY_SET_BOOL
*Type:* MACRO
Set the value of a bool property

**Parameters**

- `name` (symbol) - The property
- `value` (bool) - The value

**Examples**

```
DM_PROPERTY_SET_BOOL(rmtp_MyBool, false);

```

### DM_PROPERTY_SET_F32
*Type:* MACRO
Set the value of a float property

**Parameters**

- `name` (symbol) - The property
- `value` (float) - The value

**Examples**

```
DM_PROPERTY_SET_F32(rmtp_MyValue, 1.5);

```

### DM_PROPERTY_SET_F64
*Type:* MACRO
Set the value of a double property

**Parameters**

- `name` (symbol) - The property
- `value` (double) - The value

**Examples**

```
DM_PROPERTY_SET_F64(rmtp_MyValue, 1.5);

```

### DM_PROPERTY_SET_S32
*Type:* MACRO
Set the value of a int32_t property

**Parameters**

- `name` (symbol) - The property
- `value` (int32_t) - The value

**Examples**

```
DM_PROPERTY_SET_S32(rmtp_MyValue, -1);

```

### DM_PROPERTY_SET_S64
*Type:* MACRO
Set the value of a int64_t property

**Parameters**

- `name` (symbol) - The property
- `value` (int64_t) - The value

**Examples**

```
DM_PROPERTY_SET_S64(rmtp_MyValue, -1);

```

### DM_PROPERTY_SET_U32
*Type:* MACRO
Set the value of a uint32_t property

**Parameters**

- `name` (symbol) - The property
- `value` (uint32_t) - The value

**Examples**

```
DM_PROPERTY_SET_U32(rmtp_MyValue, 1);

```

### DM_PROPERTY_SET_U64
*Type:* MACRO
Set the value of a uint64_t property

**Parameters**

- `name` (symbol) - The property
- `value` (uint64_t) - The value

**Examples**

```
DM_PROPERTY_SET_U64(rmtp_MyValue, 1);

```

### DM_PROPERTY_U32
*Type:* MACRO
Declare a property of type uint32_t

**Parameters**

- `name` (symbol) - The property symbol/name
- `default` (uint32_t) - The default value
- `flags` (uint32_t) - The flags. Either <code>PROFILE_PROPERTY_NONE</code> or <code>PROFILE_PROPERTY_FRAME_RESET</code>. <code>PROFILE_PROPERTY_FRAME_RESET</code> makes the value reset each frame.
- `desc` (const char*) - The description
- `group` (ProfileIdx*) - The parent group. May be 0.

**Examples**

```
DM_PROPERTY_U32(rmtp_MyValue, 0, PROFILE_PROPERTY_FRAME_RESET, "a value", &rmtp_MyGroup);

```

### DM_PROPERTY_U64
*Type:* MACRO
Declare a property of type uint64_t

**Parameters**

- `name` (symbol) - The property symbol/name
- `default` (uint64_t) - The default value
- `flags` (uint32_t) - The flags. Either <code>PROFILE_PROPERTY_NONE</code> or <code>PROFILE_PROPERTY_FRAME_RESET</code>. <code>PROFILE_PROPERTY_FRAME_RESET</code> makes the value reset each frame.
- `desc` (const char*) - The description
- `group` (ProfileIdx*) - The parent group. May be 0.

**Examples**

```
DM_PROPERTY_U64(rmtp_MyValue, 0, PROFILE_PROPERTY_FRAME_RESET, "a value", &rmtp_MyGroup);

```

### HProfile
*Type:* TYPEDEF
Handle to a an active profile frame

### PROFILE_PROPERTY_INVALID_IDX
*Type:* ENUM
Index constant to mark a a property as invalid

### ProfileFinalize
*Type:* FUNCTION
Finalize the profiling system

### ProfileFrameBegin
*Type:* FUNCTION
Begin profiling, eg start of frame

**Notes**

- NULL is returned if profiling is disabled

**Returns**

- `context` (HProfile) - The current profiling context. Must be released by #EndFrame

### ProfileFrameEnd
*Type:* FUNCTION
Release profile returned by #ProfileFrameBegin

**Parameters**

- `profile` (HProfile) - Profile to release

### ProfileIdx
*Type:* TYPEDEF
Index type to hold internal references of samplers and properties

### ProfileInitialize
*Type:* FUNCTION
Initialize the profiling system

### ProfileIsInitialized
*Type:* FUNCTION
Finalize the profiling system

**Returns**

- `initialized` (bool) - Returns non zero if the profiler is initialized

### ProfileListener
*Type:* STRUCT
Structure for registering a profile listener

### ProfileLogText
*Type:* FUNCTION
Log text via the registered profilers

**Parameters**

- `name` (const char*) - Name of the scope
- `...` - Arguments for internal logging function

### ProfilePropertyFlags
*Type:* ENUM
Set of bit flags to be used when declaring propertis

**Members**

- `PROFILE_PROPERTY_NONE`
- `PROFILE_PROPERTY_FRAME_RESET`

### ProfilePropertyType
*Type:* ENUM
Enum to describe type of a property

**Members**

- `PROFILE_PROPERTY_TYPE_GROUP`
- `PROFILE_PROPERTY_TYPE_BOOL`
- `PROFILE_PROPERTY_TYPE_S32`
- `PROFILE_PROPERTY_TYPE_U32`
- `PROFILE_PROPERTY_TYPE_F32`
- `PROFILE_PROPERTY_TYPE_S64`
- `PROFILE_PROPERTY_TYPE_U64`
- `PROFILE_PROPERTY_TYPE_F64`

### ProfilePropertyValue
*Type:* FUNCTION
Union to hold a property value

### ProfileRegisterProfiler
*Type:* FUNCTION
Register a new profiler. Can be done after the profiling has started.

**Parameters**

- `name` (const char*) - Name of the profiler

### ProfileScopeBegin
*Type:* FUNCTION
Start a new profile scope

**Parameters**

- `name` (const char*) - Name of the scope
- `name_hash` (uint64_t) - Hashed name of the scope

### ProfileScopeEnd
*Type:* FUNCTION
End the last added scope

**Parameters**

- `name` (const char*) - Name of the scope
- `name_hash` (uint64_t) - Hashed name of the scope

### ProfileSetThreadName
*Type:* FUNCTION
Set the current thread name to each registered profiler

**Parameters**

- `name` (const char*) - Name of the thread

### ProfileUnregisterProfiler
*Type:* FUNCTION
Unregister a profiler

**Parameters**

- `name` (const char*) - Name of the profiler
