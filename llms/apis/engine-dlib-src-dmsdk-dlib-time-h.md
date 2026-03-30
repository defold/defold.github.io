# Time

**Namespace:** `dmTime`
**Language:** C++
**Type:** Defold C++
**File:** `time.h`
**Source:** `engine/dlib/src/dmsdk/dlib/time.h`
**Include:** `dmsdk/dlib/time.h`

Time functions.

## API

### dmTime::GetMonotonicTime
*Type:* FUNCTION
Get monotonic time in microseconds since some unspecified starting point.

**Returns**

- `result` (uint64_t) - Monotonic time in microseconds

### dmTime::GetTime
*Type:* FUNCTION
Get current time in microseconds since Jan. 1, 1970.

**Returns**

- `result` (uint64_t) - Current time in microseconds

### dmTime::Sleep
*Type:* FUNCTION
Sleep thread with low precision (~10 milliseconds).

**Parameters**

- `useconds` (uint32_t) - Time to sleep in microseconds
