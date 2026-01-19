# Hash

**Namespace:** `Hash`
**Language:** C++
**Type:** Defold C++
**File:** `hash.h`
**Source:** `engine/dlib/src/dmsdk/dlib/hash.h`
**Include:** `dmsdk/dlib/hash.h`

Hash functions.

## API

### DM_HASH_REVERSE_MEM
*Type:* FUNCTION
Allocate stack memory context for safely reversing hash values into strings

**Parameters**

- `name` (symbol) - The name of the dmAllocator struct
- `size` (size_t) - The max size of the stack allocated context

### dmhash_t
*Type:* TYPEDEF
```
typedef uint64_t dmhash_t

```

### dmHashBuffer32
*Type:* FUNCTION
Calculate 32-bit hash value from buffer

**Parameters**

- `buffer` (const void*) - Buffer
- `buffer_len` (uint32_t) - Length of buffer

**Returns**

- `hash` (uint32_t) - hash value

### dmHashBuffer64
*Type:* FUNCTION
calculate 64-bit hash value from buffer

**Parameters**

- `buffer` (const void*) - Buffer
- `buffer_len` (uint32_t) - Length of buffer

**Returns**

- `hash` (uint64_t) - hash value

### dmHashClone32
*Type:* FUNCTION
Clone 32-bit incremental hash state

**Parameters**

- `hash_state` (HashState32*) - Hash state
- `source_hash_state` (HashState32*) - Source hash state
- `reverse_hash` (bool) - true to enable reverse hashing of buffers up to ::DMHASH_MAX_REVERSE_LENGTH. Ignored if source state reverse hashing is disabled.

### dmHashClone64
*Type:* FUNCTION
Clone 64-bit incremental hash state

**Parameters**

- `hash_state` (HashState64*) - Hash state
- `source_hash_state` (HashState64*) - Source hash state
- `reverse_hash` (bool) - true to enable reverse hashing of buffers up to ::DMHASH_MAX_REVERSE_LENGTH. Ignored if source state reverse hashing is disabled.

### dmHashFinal32
*Type:* FUNCTION
Finalize incremental hashing and release associated resources

**Parameters**

- `hash_state` (HashState32*) - Hash state

**Returns**

- `hash` (uint32_t) - the hash value

### dmHashFinal64
*Type:* FUNCTION
Finalize incremental hashing and release associated resources

**Parameters**

- `hash_state` (HashState64*) - Hash state

**Returns**

- `hash` (uint64_t) - The hash value

### dmHashInit32
*Type:* FUNCTION
Initialize hash-state for 32-bit incremental hashing

**Parameters**

- `hash_state` (HashState32*) - Hash state
- `reverse_hash` (bool) - true to enable reverse hashing of buffers up to ::DMHASH_MAX_REVERSE_LENGTH

### dmHashInit64
*Type:* FUNCTION
Initialize hash-state for 64-bit incremental hashing

**Parameters**

- `hash_state` (HashState64*) - Hash state
- `reverse_hash` (bool) - true to enable reverse hashing of buffers up to ::DMHASH_MAX_REVERSE_LENGTH

### dmHashRelease32
*Type:* FUNCTION
Release incremental hashing resources
Used to release assocciated resources for intermediate incremental hash states.

**Parameters**

- `hash_state` (HashState32*) - Hash state

### dmHashRelease64
*Type:* FUNCTION
Release incremental hashing resources
Used to release assocciated resources for intermediate incremental hash states.

**Parameters**

- `hash_state` (HashState64*) - Hash state

### dmHashReverseSafe32
*Type:* FUNCTION
Returns the original string used to produce a hash.
Always returns a null terminated string. Returns "" if the original string wasn't found.

**Notes**

- Do not store this pointer

**Parameters**

- `hash` (uint32_t) - hash value

**Returns**

- `return` (const char*) - Original string value or "<unknown>" if it wasn't found.

### dmHashReverseSafe32
*Type:* FUNCTION
Reverse hash lookup. Maps hash to original data. It is guaranteed that the returned
buffer is null-terminated. If the buffer contains a valid c-string
it can safely be used in printf and friends.

**Notes**

- Do not store this pointer

**Parameters**

- `hash` (uint32_t) - hash to lookup
- `length` (uint32_t*) - original data length. Optional argument and NULL-pointer is accepted.

**Returns**

- `return` (const char*) - pointer to buffer. 0 if no reverse exists or if reverse lookup is disabled

### dmHashReverseSafe32Alloc
*Type:* FUNCTION
Returns the original string used to produce a hash.

**Notes**

- This function is thread safe
- The pointer is valid during the scope of the allocator

**Parameters**

- `allocator` (dmAllocator*) - The reverse hash allocator
- `hash` (uint32_t) - hash value

**Returns**

- `return` (const char*) - Original string value or "<unknown:value>" if it wasn't found,
                           or "<unknown>" if the allocator failed to allocate more memory.
                           Always returns a null terminated string.

**Examples**

Get the string representaiton of a hash value
```
DM_HASH_REVERSE_MEM(hash_ctx, 128);
const char* reverse = (const char*) dmHashReverseSafe32Alloc(&hash_ctx, hash);

```

### dmHashReverseSafe64
*Type:* FUNCTION
Returns the original string used to produce a hash.
Always returns a null terminated string. Returns "" if the original string wasn't found.

**Notes**

- Do not store this pointer

**Parameters**

- `hash` (uint64_t) - hash value

**Returns**

- `return` (const char*) - Original string value or "<unknown>" if it wasn't found.

### dmHashReverseSafe64
*Type:* FUNCTION
Reverse hash lookup. Maps hash to original data. It is guaranteed that the returned
buffer is null-terminated. If the buffer contains a valid c-string
it can safely be used in printf and friends.

**Notes**

- Do not store this pointer

**Parameters**

- `hash` (uint64_t) - hash to lookup
- `length` (uint32_t*) - original data length. Optional argument and NULL-pointer is accepted.

**Returns**

- `return` (const char*) - pointer to buffer. 0 if no reverse exists or if reverse lookup is disabled

### dmHashReverseSafe64Alloc
*Type:* FUNCTION
Returns the original string used to produce a hash.

**Notes**

- This function is thread safe
- The pointer is valid during the scope of the allocator

**Parameters**

- `allocator` (dmAllocator*) - The reverse hash allocator
- `hash` (uint64_t) - hash value

**Returns**

- `return` (const char*) - Original string value or "<unknown:value>" if it wasn't found,
                           or "<unknown>" if the allocator failed to allocate more memory.
                           Always returns a null terminated string.

**Examples**

Get the string representaiton of a hash value
```
DM_HASH_REVERSE_MEM(hash_ctx, 128);
const char* reverse = dmHashReverseSafe64Alloc(&hash_ctx, hash);

```

### dmHashString32
*Type:* FUNCTION
Calculate 32-bit hash value from string

**Parameters**

- `string` (const char*) - Null terminated string

**Returns**

- `hash` (uint32_t) - hash value

### dmHashString64
*Type:* FUNCTION
calculate 64-bit hash value from string

**Parameters**

- `string` (const char*) - Null terminated string

**Returns**

- `hash` (uint64_t) - hash value

### dmHashUpdateBuffer32
*Type:* FUNCTION
Incremental hashing

**Parameters**

- `hash_state` (HashState32*) - Hash state
- `buffer` (const void*) - Buffer
- `buffer_len` (uint32_t) - Length of buffer

### dmHashUpdateBuffer64
*Type:* FUNCTION
Incremental hashing

**Parameters**

- `hash_state` (HashState64*) - Hash state
- `buffer` (const void*) - Buffer
- `buffer_len` (uint32_t) - Length of buffer

### HashState32
*Type:* STRUCT
Hash state used for 32-bit incremental hashing

### HashState64
*Type:* STRUCT
Hash state used for 64-bit incremental hashing
