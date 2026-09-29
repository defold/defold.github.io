# Crash

**Namespace:** `crash`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_crash.cpp`
**Source:** `engine/crash/src/script_crash.cpp`

Native crash logging functions and constants.

## API

### crash.get_backtrace
*Type:* FUNCTION
A table is returned containing the addresses of the call stack.

**Parameters**

- `handle` (number) - crash dump handle

**Returns**

- `backtrace` (string[]) - table containing the backtrace

### crash.get_extra_data
*Type:* FUNCTION
The format of read text blob is platform specific
and not guaranteed
but can be useful for manual inspection.

**Parameters**

- `handle` (number) - crash dump handle

**Returns**

- `blob` (string) - string with the platform specific data

### crash.get_modules
*Type:* FUNCTION
get all loaded modules from when the crash occured

**Parameters**

- `handle` (number) - crash dump handle

**Returns**

- `modules` (crash.module_info[]) - loaded modules

### crash.get_signum
*Type:* FUNCTION
read signal number from a crash report

**Parameters**

- `handle` (number) - crash dump handle

**Returns**

- `signal` (number) - signal number

### crash.get_sys_field
*Type:* FUNCTION
reads a system field from a loaded crash dump

**Parameters**

- `handle` (number) - crash dump handle
- `index` (crash.SYSFIELD) - system field enum. Must be less than <a href="/ref/crash#crash.SYSFIELD_MAX">crash.SYSFIELD_MAX</a>

**Returns**

- `value` (string | nil) - value recorded in the crash dump, or <code>nil</code> if it didn't exist

### crash.get_user_field
*Type:* FUNCTION
reads user field from a loaded crash dump

**Parameters**

- `handle` (number) - crash dump handle
- `index` (crash.USERFIELD) - user data slot index

**Returns**

- `value` (string) - user data value recorded in the crash dump

### crash.load_previous
*Type:* FUNCTION
The crash dump will be removed from disk upon a successful
load, so loading is one-shot.

**Returns**

- `handle` (number | nil) - handle to the loaded dump, or <code>nil</code> if no dump was found

### crash.module_info
*Type:* STRUCT
Loaded crash module

**Members**

- `name` (string) - module name
- `address` (string) - module load address

### crash.release
*Type:* FUNCTION
releases a previously loaded crash dump

**Parameters**

- `handle` (number) - handle to loaded crash dump

### crash.set_file_path
*Type:* FUNCTION
Crashes occuring before the path is set will be stored to a default engine location.

**Parameters**

- `path` (string) - file path to use

### crash.set_user_field
*Type:* FUNCTION
Store a user value that will get written to a crash dump when
a crash occurs. This can be user id:s, breadcrumb data etc.
There are 32 slots indexed from 0. Each slot stores at most 255 characters.

**Parameters**

- `index` (crash.USERFIELD) - slot index. 0-indexed
- `value` (string) - string value to store

### crash.SYSFIELD
*Type:* ENUM
System crash fields

**Members**

- `crash.SYSFIELD_ENGINE_VERSION` - engine version as release number
- `crash.SYSFIELD_ENGINE_HASH` - engine version as hash
- `crash.SYSFIELD_DEVICE_MODEL` - device model as reported by sys.get_sys_info
- `crash.SYSFIELD_MANUFACTURER` - device manufacturer as reported by sys.get_sys_info
- `crash.SYSFIELD_SYSTEM_NAME` - system name as reported by sys.get_sys_info
- `crash.SYSFIELD_SYSTEM_VERSION` - system version as reported by sys.get_sys_info
- `crash.SYSFIELD_LANGUAGE` - system language as reported by sys.get_sys_info
- `crash.SYSFIELD_DEVICE_LANGUAGE` - system device language as reported by sys.get_sys_info
- `crash.SYSFIELD_TERRITORY` - system territory as reported by sys.get_sys_info
- `crash.SYSFIELD_ANDROID_BUILD_FINGERPRINT` - android build fingerprint

### crash.SYSFIELD_MAX
*Type:* CONSTANT
The max number of sysfields.

**Parameters**

- `value` (integer)

### crash.USERFIELD
*Type:* TYPEDEF
An integer index identifying one of the 32 user-defined fields stored in a
crash dump. Valid indices are 0 through 31. Each field stores a string of at
most crash.USERFIELD_SIZE bytes; longer strings are truncated.

**Parameters**

- `value` (integer) - zero-based user-field index

**Examples**

```
crash.set_user_field(0, "level=forest")
crash.set_user_field(1, "checkpoint=3")

```

### crash.USERFIELD_MAX
*Type:* CONSTANT
The max number of user fields.

**Parameters**

- `value` (integer)

### crash.USERFIELD_SIZE
*Type:* CONSTANT
The max size of a single user field.

**Parameters**

- `value` (integer)

### crash.write_dump
*Type:* FUNCTION
Performs the same steps as if a crash had just occured but
allows the program to continue.
The generated dump can be read by crash.load_previous
