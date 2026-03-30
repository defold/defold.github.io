# Mutex

**Namespace:** `dmMutex`
**Language:** C++
**Type:** Defold C++
**File:** `mutex.h`
**Source:** `engine/dlib/src/dmsdk/dlib/mutex.h`
**Include:** `dmsdk/dlib/mutex.h`

API for platform independent mutex synchronization primitive.

## API

### DM_MUTEX_OPTIONAL_SCOPED_LOCK
*Type:* MACRO
If mutex is not null, Will lock the mutex and automatically unlock it at the end of the scope.
Since using threads is optional, we want to make it easy to switch on/off the mutex behavior

**Parameters**

- `mutex` (dmMutex::HMutex) - Mutex handle to lock, or null.

### DM_MUTEX_SCOPED_LOCK
*Type:* MACRO
Will lock a Mutex and automatically unlock it at the end of the scope.

**Parameters**

- `mutex` (dmMutex::HMutex) - Mutex handle to lock.

### dmMutex::Delete
*Type:* FUNCTION
Deletes a HMutex.

**Parameters**

- `mutex` (dmMutex::HMutex) - Mutex handle to delete.

### dmMutex::HMutex
*Type:* TYPEDEF
```
typedef struct Mutex* HMutex;

```

### dmMutex::Lock
*Type:* FUNCTION
Lock a HMutex, will block until mutex is unlocked if already locked elsewhere.

**Parameters**

- `mutex` (dmMutex::HMutex) - Mutex handle to lock.

### dmMutex::New
*Type:* FUNCTION
Creates a new HMutex.

**Returns**

- `mutex` (dmMutex::HMutex) - A new Mutex handle.

### dmMutex::TryLock
*Type:* FUNCTION
Tries to lock a HMutex, if mutex is already locked it will return false and
continue without locking the mutex.

**Parameters**

- `mutex` (dmMutex::HMutex) - Mutex handle to lock.

**Returns**

- `result` (bool) - True if mutex was successfully locked, false otherwise.

### dmMutex::Unlock
*Type:* FUNCTION
Unlock a HMutex.

**Parameters**

- `mutex` (dmMutex::HMutex) - Mutex handle to unlock.
