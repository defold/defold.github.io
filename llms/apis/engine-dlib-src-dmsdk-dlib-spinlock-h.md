# Spinlock

**Namespace:** `dmSpinlock`
**Language:** C++
**Type:** Defold C++
**File:** `spinlock.h`
**Source:** `engine/dlib/src/dmsdk/dlib/spinlock.h`
**Include:** `dmsdk/dlib/spinlock.h`

API for platform independent spinlock synchronization primitive.

## API

### DM_SPINLOCK_SCOPED_LOCK
*Type:* MACRO
Will lock a Spinlock and automatically unlock it at the end of the scope.

**Parameters**

- `mutex` (dmSpinlock::Spinlock) - Spinlock reference to lock.

### dmSpinlock::Create
*Type:* FUNCTION
Initialize a Spinlock

**Parameters**

- `spinlock` (dmSpinlock::Spinlock*) - spinlock to initialize.

### dmSpinlock::Destroy
*Type:* FUNCTION
Destroy a Spinlock

**Parameters**

- `spinlock` (dmSpinlock::Spinlock*) - spinlock to destroy.

### dmSpinlock::Lock
*Type:* FUNCTION
Lock a Spinlock

**Parameters**

- `spinlock` (dmSpinlock::Spinlock*) - spinlock to lock.

### dmSpinlock::Spinlock
*Type:* STRUCT
```
struct Spinlock;

```

### dmSpinlock::Unlock
*Type:* FUNCTION
Unlock a Spinlock

**Parameters**

- `spinlock` (dmSpinlock::Spinlock*) - spinlock to unlock.
