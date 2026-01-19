# Atomic

**Namespace:** `Atomic`
**Language:** C++
**Type:** Defold C++
**File:** `atomic.h`
**Source:** `engine/dlib/src/dmsdk/dlib/atomic.h`
**Include:** `dmsdk/dlib/atomic.h`

Atomic functions

## API

### dmAtomicAdd32
*Type:* FUNCTION
Atomic addition of an int32_atomic_t.

**Parameters**

- `ptr` (int32_atomic_t*) - Pointer to an int32_atomic_t to add to.
- `value` (int32_t) - Value to add.

**Returns**

- `prev` (int32_t) - Previous value

### dmAtomicCompareStore32
*Type:* FUNCTION
Atomic set (or exchange) of an int32_atomic_t if comparand is equal to the value of ptr.

**Parameters**

- `ptr` (int32_atomic_t*) - Pointer to an int32_atomic_t to store into.
- `value` (int32_t) - Value to set.
- `comparand` (int32_t) - Value to compare to.

**Returns**

- `prev` (int32_t) - Previous value

### dmAtomicDecrement32
*Type:* FUNCTION
Atomic decrement of an int32_atomic_t.

**Parameters**

- `ptr` (int32_atomic_t*) - Pointer to an int32_atomic_t to decrement.

**Returns**

- `prev` (int32_t) - Previous value

### dmAtomicGet32
*Type:* FUNCTION
Atomic get of an int32_atomic_t

**Notes**

- Retrieves the current value by adding 0

**Parameters**

- `ptr` (int32_atomic_t*) - Pointer to an int32_atomic_t to get from.

**Returns**

- `value` (int32_t) - Current value

### dmAtomicIncrement32
*Type:* FUNCTION
Atomic increment of an int32_atomic_t.

**Parameters**

- `ptr` (int32_atomic_t*) - Pointer to an int32_atomic_t to increment.

**Returns**

- `prev` (int32_t) - Previous value

### dmAtomicStore32
*Type:* FUNCTION
Atomic set (or exchange) of an int32_atomic_t.

**Parameters**

- `ptr` (int32_atomic_t*) - Pointer to an int32_atomic_t to store into.
- `value` (int32_t) - Value to set.

**Returns**

- `prev` (int32_t) - Previous value

### dmAtomicSub32
*Type:* FUNCTION
Atomic subtraction of an int32_atomic_t.

**Parameters**

- `ptr` (int32_atomic_t*) - Pointer to an int32_atomic_t to subtract from.
- `value` (int32_t) - Value to subtract.

**Returns**

- `prev` (int32_t) - Previous value

### int32_atomic_t
*Type:* TYPEDEF
32 bit signed integer atomic
