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

- `backtrace` (table) - table containing the backtrace

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
The function returns a table containing entries with sub-tables that
have fields 'name' and 'address' set for all loaded modules.

**Parameters**

- `handle` (number) - crash dump handle

**Returns**

- `modules` (table) - module table

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
- `index` (number) - system field enum. Must be less than <a href="/ref/crash#crash.SYSFIELD_MAX">crash.SYSFIELD_MAX</a>

**Returns**

- `value` (string | nil) - value recorded in the crash dump, or <code>nil</code> if it didn't exist

### crash.get_user_field
*Type:* FUNCTION
reads user field from a loaded crash dump

**Parameters**

- `handle` (number) - crash dump handle
- `index` (number) - user data slot index

**Returns**

- `value` (string) - user data value recorded in the crash dump

### crash.load_previous
*Type:* FUNCTION
The crash dump will be removed from disk upon a successful
load, so loading is one-shot.

**Returns**

- `handle` (number | nil) - handle to the loaded dump, or <code>nil</code> if no dump was found

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

- `index` (number) - slot index. 0-indexed
- `value` (string) - string value to store

### crash.SYSFIELD_ANDROID_BUILD_FINGERPRINT
*Type:* CONSTANT
android build fingerprint

### crash.SYSFIELD_DEVICE_LANGUAGE
*Type:* CONSTANT
system device language as reported by sys.get_sys_info

### crash.SYSFIELD_DEVICE_MODEL
*Type:* CONSTANT
device model as reported by sys.get_sys_info

### crash.SYSFIELD_ENGINE_HASH
*Type:* CONSTANT
engine version as hash

### crash.SYSFIELD_ENGINE_VERSION
*Type:* CONSTANT
engine version as release number

### crash.SYSFIELD_LANGUAGE
*Type:* CONSTANT
system language as reported by sys.get_sys_info

### crash.SYSFIELD_MANUFACTURER
*Type:* CONSTANT
device manufacturer as reported by sys.get_sys_info

### crash.SYSFIELD_MAX
*Type:* CONSTANT
The max number of sysfields.

### crash.SYSFIELD_SYSTEM_NAME
*Type:* CONSTANT
system name as reported by sys.get_sys_info

### crash.SYSFIELD_SYSTEM_VERSION
*Type:* CONSTANT
system version as reported by sys.get_sys_info

### crash.SYSFIELD_TERRITORY
*Type:* CONSTANT
system territory as reported by sys.get_sys_info

### crash.USERFIELD_MAX
*Type:* CONSTANT
The max number of user fields.

### crash.USERFIELD_SIZE
*Type:* CONSTANT
The max size of a single user field.

### crash.write_dump
*Type:* FUNCTION
Performs the same steps as if a crash had just occured but
allows the program to continue.
The generated dump can be read by crash.load_previous
