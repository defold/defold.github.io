# Memory

**Namespace:** `dmMemory`
**Language:** C++
**Type:** Defold C++
**File:** `memory.h`
**Source:** `engine/dlib/src/dmsdk/dlib/memory.h`
**Include:** `dmsdk/dlib/memory.h`

Memory allocation functions

## API

### AlignedFree
*Type:* FUNCTION
Frees a block of memory that was allocated with dmMemory::AlignedMalloc

**Parameters**

- `memptr` (void*) - A pointer to the memory block that was returned by dmMemory::AlignedMalloc

### AlignedMalloc
*Type:* FUNCTION
Allocate size bytes of uninitialized storage whose alignment is specified by alignment.

**Parameters**

- `memptr` (void**) - Pointer to a void* where the allocated pointer address should be stored.
- `alignment` (uint32_t) - The alignment value, which must be an integer power of 2.
- `size` (uint32_t) - Size of the requested memory allocation.

**Returns**

- `result` (Result) - Returns RESULT_OK on success, RESULT_INVAL if alignment is not a power of 2 and RESULT_NOMEM if out of memory.

### Result
*Type:* ENUM
Aligned memory allocation result

**Members**

- `dmMemory::RESULT_OK` - 0
- `dmMemory::RESULT_INVAL` - -1
- `dmMemory::RESULT_NOMEM` - -2
