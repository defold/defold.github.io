# Hashtable

**Namespace:** `Hashtable`
**Language:** C++
**Type:** Defold C++
**File:** `hashtable.h`
**Source:** `engine/dlib/src/dmsdk/dlib/hashtable.h`
**Include:** `dmsdk/dlib/hashtable.h`

Hash table

## API

### Capacity
*Type:* FUNCTION
Hashtable capacity. Maximum number of entries possible to store in table

**Returns**

- `return` (uint32_t) - the capacity of the table

### Clear
*Type:* FUNCTION
Removes all the entries from the table.

### dmHashTable
*Type:* CLASS
Hashtable with chaining for collision resolution, memcpy-copy semantics (POD types) and 32-bit indicies instead of pointers. (NUMA-friendly)

**Notes**

- The key type needs to support == and % operators

**Template Parameters**

- `KEY`
- `T`

### dmHashTable
*Type:* FUNCTION
Constructor. Create an empty hashtable with zero capacity and zero hashtable (buckets)

### dmHashTable
*Type:* FUNCTION
Creates a hashtable array with user allocated memory.

**Notes**

- User allocated arrays can not change capacity.

**Parameters**

- `user_allocated` (void*) - Pointer to user allocated continous data-block ((table_size<em>sizeof(uint32_t)) + (capacity</em>sizeof(dmHashTable::Entry))
- `table_size` (uint32_t) - Hashtable size, ie number of buckets. table_size &lt; 0xffffffff
- `capacity` (uint32_t) - Capacity. capacity &lt; 0xffffffff

### dmHashTable16
*Type:* CLASS
Specialized hash table with uint16_t as keys

### dmHashTable32
*Type:* CLASS
Specialized hash table with uint32_t as keys

### dmHashTable64
*Type:* CLASS
Specialized hash table with uint64_t as keys

### Empty
*Type:* FUNCTION
Check if the table is empty

**Returns**

- `true` - if the table is empty

### Erase
*Type:* FUNCTION
Remove key/value pair.

**Notes**

- Only valid if key exists in table

**Parameters**

- `key` (KEY) - Key to remove

### Full
*Type:* FUNCTION
Check if the table is full

**Returns**

- `true` - if the table is full

### Get
*Type:* FUNCTION
Get pointer to value from key

**Parameters**

- `key` (KEY) - Key

**Returns**

- `value` (T*) - Pointer to value. NULL if the key/value pair doesn't exist.

### GetIterator
*Type:* FUNCTION
Get an iterator for the key/value pairs

**Returns**

- `iterator` (dmHashTable<T>::Iterator) - the iterator

**Examples**

```
dmHashTable::Iterator iter = ht.GetIterator();
while(iter.Next())
{
    printf("%s: %d\n", dmHashReverseSafe64(iter.GetKey()), iter.GetValue());
}

```

### Iterate
*Type:* FUNCTION
Iterate over all entries in table

**Template Parameters**

- `CONTEXT`

**Parameters**

- `call_back` (void*) - Call-back called for every entry
- `context` (CONTEXT*) - Context

### Iterator
*Type:* STRUCT
Iterator to the key/value pairs of a hash table

**Members**

- `GetKey()`
- `GetValue()`

### OffsetCapacity
*Type:* FUNCTION
Relative change of capacity
Equivalent to SetCapacity(Capacity() + offset).
Only allowed for auto-allocated hash tables and will result in a new dynamic allocation

**Parameters**

- `offset` (uint32_t) - relative amount of elements to change the capacity

### Put
*Type:* FUNCTION
Put key/value pair in hash table. NOTE: The method will "assert" if the hashtable is full.

**Parameters**

- `key` (KEY) - Key
- `value` (const T&) - Value

### SetCapacity
*Type:* FUNCTION
Set hashtable capacity. New capacity must be greater or equal to current capacity

**Parameters**

- `table_size` (uint32_t) - Hashtable size, ie number of buckets. table_size &lt; 0xffffffff
- `capacity` (uint32_t) - Capacity. capacity &lt; 0xffffffff

### Size
*Type:* FUNCTION
Number of entries stored in table. (not the actual hashtable size)

**Returns**

- `Number` - of entries.

### Swap
*Type:* FUNCTION
Swaps the contents of two hash tables

**Parameters**

- `other` (dmHashTable<KEY, T>&) - the other table
