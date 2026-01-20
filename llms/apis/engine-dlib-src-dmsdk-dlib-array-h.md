# Array

**Namespace:** `Array`
**Language:** C++
**Type:** Defold C++
**File:** `array.h`
**Source:** `engine/dlib/src/dmsdk/dlib/array.h`
**Include:** `dmsdk/dlib/array.h`

Templatized array with bounds checking.

The backing storage is either auto-allocated (dynamically allocated) or user-allocated (supplied by user).
With exception of changing the size and capacity, all operations are guaranteed to be O(1).

```cpp
dmArray a;
a.SetCapacity(1);
a.Push(1);
int b = a[0];
```

## API

### Back
*Type:* FUNCTION
Last element of the array

**Returns**

- `reference` (T&) - reference to the last element

### Back
*Type:* FUNCTION
Last element of the array (const)

**Returns**

- `reference` (const T&) - const-reference to the last element

### Begin
*Type:* FUNCTION
Pointer to the start of the backing storage

**Returns**

- `pointer` (T*) - pointer to start of memory

### Begin
*Type:* FUNCTION
Pointer to the start of the backing storage

**Returns**

- `pointer` (const T*) - pointer to start of memory

### Capacity
*Type:* FUNCTION
Capacity is currently allocated storage.

**Returns**

- `number` (uint32_t) - array capacity

### DM_ARRAY_SIZE
*Type:* MACRO
get number of elements in C array

**Parameters**

- `A` (T) - C array to count

**Returns**

- `Number` - of elements

### dmArray
*Type:* CLASS
The backing storage is either auto-allocated (dynamically allocated) or user-allocated (supplied by user).
With exception of changing the size and capacity, all operations are guaranteed to be O(1).

**Template Parameters**

- `T` - Contained type, must obey memcpy semantics

### dmArray
*Type:* FUNCTION
constructor. empty auto-allocated memory

**Examples**

```
dmArray a;
a.Push(1);

```

### dmArray
*Type:* FUNCTION
user-allocated array with initial size and capacity

**Parameters**

- `user_array` (T*) - User-allocated array to be used as storage.
- `size` (uint32_t) - Initial size
- `capacity` (uint32_t) - Initial capacity

### dmArray
*Type:* FUNCTION
user-allocated array with initial size and capacity

**Parameters**

- `user_array` (T*) - User-allocated array to be used as storage.
- `size` (uint32_t) - Initial size
- `capacity` (uint32_t) - Initial capacity
- `user_allocated` (bool) - If false, the ownership is transferred to the dmArray

### Empty
*Type:* FUNCTION
Check if the array is empty.
The array is empty when the size is zero.

**Returns**

- `boolean` (bool) - true if the array is empty

### End
*Type:* FUNCTION
Pointer to the end of the backing storage
The end is essentially outside of the used storage.

**Returns**

- `pointer` (T*) - pointer to end of memory

### End
*Type:* FUNCTION
Pointer to the end of the backing storage
The end is essentially outside of the used storage.

**Returns**

- `pointer` (const T*) - pointer to end of memory

### EraseSwap
*Type:* FUNCTION
Remove the element at the specified index.
The removed element is replaced by the element at the end (if any), thus potentially altering the order.
While operation changes the array size, it is guaranteed to be O(1).

**Parameters**

- `index` (uint32_t) - index of the element to remove

**Returns**

- `reference` (T&) - reference to the new element at index

### EraseSwapRef
*Type:* FUNCTION
Remove the element by reference
The removed element is replaced by the element at the end (if any), thus potentially altering the order.
While operation changes the array size, it is guaranteed to be O(1).

**Parameters**

- `element` (T&) - reference to the element to remove.

**Returns**

- `reference` (T&) - reference to the new referenced element

### Front
*Type:* FUNCTION
First element of the array

**Returns**

- `reference` (T&) - reference to the first element

### Front
*Type:* FUNCTION
First element of the array (const)

**Returns**

- `reference` (const T&) - const-reference to the first element

### Full
*Type:* FUNCTION
Check if the array is full.
The array is full when the size is equal to the capacity.

**Returns**

- `boolean` (bool) - true if the array is full

### Map
*Type:* FUNCTION
map a function on all values

**Parameters**

- `fn` (void*) - function that will be called for each element
- `ctx` (void*) - user defined context that will be passed in with each callback

### OffsetCapacity
*Type:* FUNCTION
Relative change of capacity
Equivalent to SetCapacity(Capacity() + offset).
Only allowed for auto-allocated arrays and will result in a new dynamic allocation followed by memcpy of the elements.

**Parameters**

- `offset` (uint32_t) - relative amount of elements to change the capacity

### operator[]
*Type:* FUNCTION
Retrieve an element by index

**Parameters**

- `index` (uint32_t) - array index

**Returns**

- `reference` (T&) - reference to the element at the specified index

### operator[]
*Type:* FUNCTION
Retrieve an element by index (const)

**Parameters**

- `index` (uint32_t) - array index

**Returns**

- `reference` (const T&) - const-reference to the element at the specified index

### Pop
*Type:* FUNCTION
Remove the last element of the array
Only allowed when the size is larger than zero.

### Push
*Type:* FUNCTION
Add an element to the end of the array
Only allowed when the capacity is larger than size.

**Parameters**

- `element` (const T&) - element element to add

### PushArray
*Type:* FUNCTION
Add an array of elements to the end of the array
Only allowed when the capacity is larger than size + count

**Parameters**

- `array` (const T*) - array of elements to add
- `count` (uint32_t) - amount of elements in the array

### Remaining
*Type:* FUNCTION
Amount of additional elements that can be stored

**Returns**

- `number` (uint32_t) - amount of additional elements that can be stored

### SetCapacity
*Type:* FUNCTION
Set the capacity of the array.
If the size is less than the capacity, the array is truncated.
If it is larger, the array is extended.
Only allowed for auto-allocated arrays and will result in a new dynamic allocation followed by memcpy of the elements.

**Parameters**

- `capacity` (uint32_t) - capacity of the array

### SetSize
*Type:* FUNCTION
Set size of the array

**Parameters**

- `size` (uint32_t) - size of the array, must be less or equal to the capacity

### Size
*Type:* FUNCTION
Size of the array in elements

**Returns**

- `number` (uint32_t) - array size

### Swap
*Type:* FUNCTION
Swap the content of two arrays

**Parameters**

- `rhs` (dmArray<T>&) - reference to array to swap content with

### ~dmArray
*Type:* FUNCTION
Only frees memory when auto-allocated.
