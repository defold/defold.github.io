# Shared Library

**Namespace:** `SharedLibrary`
**Language:** C++
**Type:** Defold C++
**File:** `shared_library.h`
**Source:** `engine/dlib/src/dmsdk/dlib/shared_library.h`
**Include:** `dmsdk/dlib/shared_library.h`

Utility functions for shared library export/import

## API

### DM_DLLEXPORT
*Type:* MACRO
Export and import functions, data, and objects to or from a DLL

**Examples**

```
DM_DLLEXPORT uint64_t dmHashBuffer64(const void* buffer, uint32_t buffer_len);

```
