# ObjectPool

**Namespace:** `ObjectPool`
**Language:** C++
**Type:** Defold C++
**File:** `object_pool.h`
**Source:** `engine/dlib/src/dmsdk/dlib/object_pool.h`
**Include:** `dmsdk/dlib/object_pool.h`

SDK Object Pool API documentation

## API

### Alloc
*Type:* FUNCTION
Allocate a new object

**Returns**

- `index` (uint32_t) - logical index

### Capacity
*Type:* FUNCTION

**Returns**

- `capacity` (uint32_t) - maximum number of objects

### dmObjectPool
*Type:* STRUCT
Object pool data-structure with the following properties
- Mapping from logical index to physical index
- Logical index does not changes
- Allocated objects are contiguously laid out in memory
  Loop of m_Objects [0..Size()-1] times to iterate all objects
- Internal physical order is not preserved and a direct consequence of the
  contiguous property

**Template Parameters**

- `T`

### dmObjectPool
*Type:* FUNCTION
Constructor

### Free
*Type:* FUNCTION
Returns object index to the object pool

**Parameters**

- `index` (uint32_t) - index of object
- `clear` (bool) - If set, memset's the object memory

### Full
*Type:* FUNCTION
Checks if the pool is full

**Returns**

- `result` (bool) - returns true if the pool is full

### Get
*Type:* FUNCTION
Get object from logical index

**Parameters**

- `index` (uint32_t) - index of the object

**Returns**

- `object` (T&) - a reference to the object

### GetPtr
*Type:* FUNCTION
Get object pointer from logical index

**Parameters**

- `index` (uint32_t) - index of the object

**Returns**

- `object` (T*) - a pointer to the object. Null if the logical index wasn't valid

### GetRawObjects
*Type:* FUNCTION
Get the array of currently active objects

**Notes**

- The order of objects in this array may change if Alloc() or Free() has been called

**Returns**

- `object` (dmArray<T>&) - a reference to the array of objects

### OffsetCapacity
*Type:* FUNCTION
Grow by an amount.

**Parameters**

- `grow` (uint32_t) - number of items to grow

### Set
*Type:* FUNCTION
Set object from logical index

**Parameters**

- `index` (uint32_t) - index of object
- `object` (T&) - reference ot object. THe object stored is copied by value.

### SetCapacity
*Type:* FUNCTION
Set capacity. New capacity must be >= old_capacity

**Parameters**

- `capacity` (uint32_t) - max number of objects to store

### Size
*Type:* FUNCTION
Get number of objects currently stored

**Returns**

- `size` (uint32_t) - returns the number of objects currently stored
