# Sys

**Namespace:** `dmSys`
**Language:** C++
**Type:** Defold C++
**File:** `sys.h`
**Source:** `engine/dlib/src/dmsdk/dlib/sys.h`
**Include:** `dmsdk/dlib/sys.h`

Sys allocation functions

## API

### Exists
*Type:* FUNCTION
Checks if a path exists

**Parameters**

- `path` (const char*) - path to directory to create

**Returns**

- `result` (bool) - true on success

### Rename
*Type:* FUNCTION
Move a file or directory

**Notes**

- This operation is atomic

**Parameters**

- `dst_path` (const char*) - the destination path. The file which contents is to be overwritten.
- `src_path` (const char*) - the source path. The contents will be written to the destination path and the file unlinked if successful.

**Returns**

- `RESULT_OK` - on success

### Result
*Type:* ENUM
Result code. Similar to standard posix result codes

**Members**

- `dmSys::RESULT_OK` -      0
- `dmSys::RESULT_PERM` -   -1
- `dmSys::RESULT_NOENT` -  -2
- `dmSys::RESULT_SRCH` -   -3
- `dmSys::RESULT_INTR` -   -4
- `dmSys::RESULT_IO` -     -5
- `dmSys::RESULT_NXIO` -   -6
- `dmSys::RESULT_2BIG` -   -7
- `dmSys::RESULT_NOEXEC` - -8
- `dmSys::RESULT_BADF` -   -9
- `dmSys::RESULT_CHILD` -  -10
- `dmSys::RESULT_DEADLK` - -11
- `dmSys::RESULT_NOMEM` -  -12
- `dmSys::RESULT_ACCES` -  -13
- `dmSys::RESULT_FAULT` -  -14
- `dmSys::RESULT_BUSY` -   -15
- `dmSys::RESULT_EXIST` -  -16
- `dmSys::RESULT_XDEV` -   -17
- `dmSys::RESULT_NODEV` -  -18
- `dmSys::RESULT_NOTDIR` - -19
- `dmSys::RESULT_ISDIR` -  -20
- `dmSys::RESULT_INVAL` -  -21
- `dmSys::RESULT_NFILE` -  -22
- `dmSys::RESULT_MFILE` -  -23
- `dmSys::RESULT_NOTTY` -  -24
- `dmSys::RESULT_TXTBSY` - -25
- `dmSys::RESULT_FBIG` -   -26
- `dmSys::RESULT_NOSPC` -  -27
- `dmSys::RESULT_SPIPE` -  -28
- `dmSys::RESULT_ROFS` -   -29
- `dmSys::RESULT_MLINK` -  -30
- `dmSys::RESULT_PIPE` -   -31
- `dmSys::RESULT_NOTEMPTY` - -32
- `dmSys::RESULT_UNKNOWN` - -1000

### StatInfo
*Type:* STRUCT
Status info for a file or directory

**Members**

- `m_Size` (uint32_t) - the file size (if it's a file)
- `m_Mode` (uint32_t) - the flags of the path
- `m_AccessTime` (uint32_t) - the last access time
- `m_ModifiedTime` (uint32_t) - the last modified time

### Unlink
*Type:* FUNCTION
Remove file

**Parameters**

- `path` (const char*) - path to file to remove

**Returns**

- `result` (dmSys::Result) - RESULT_OK on success
