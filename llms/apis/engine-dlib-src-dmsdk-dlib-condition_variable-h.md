# Condition Variable

**Namespace:** `dmConditionVariable`
**Language:** C++
**Type:** Defold C++
**File:** `condition_variable.h`
**Source:** `engine/dlib/src/dmsdk/dlib/condition_variable.h`
**Include:** `dmsdk/dlib/condition_variable.h`

API for platform independent mutex synchronization primitive.

## API

### dmConditionVariable::Broadcast
*Type:* FUNCTION
Broadcast condition variable, effectively unblocks all of the waiting threads blocked
by the condition variable.

**Parameters**

- `condition` (dmConditionVariable::HConditionVariable) - ConditionVariable handle.

### dmConditionVariable::Delete
*Type:* FUNCTION
Deletes a HConditionVariable.

**Parameters**

- `mutex` (dmConditionVariable::HConditionVariable) - ConditionVariable handle to delete.

### dmConditionVariable::HConditionVariable
*Type:* TYPEDEF
```
typedef struct ConditionVariable* HConditionVariable;

```

### dmConditionVariable::New
*Type:* FUNCTION
Create a new HConditionVariable

**Returns**

- `condition_variable` (dmConditionVariable::HConditionVariable) - A new ConditionVariable handle.

### dmConditionVariable::Signal
*Type:* FUNCTION
Signal condition variable, effectively unblocks at least one of the waiting threads blocked
by the condition variable.

**Parameters**

- `condition` (dmConditionVariable::HConditionVariable) - ConditionVariable handle.

### dmConditionVariable::Wait
*Type:* FUNCTION
Wait for condition variable. This is a blocking function, and should be called with
the mutex being locked.

**Parameters**

- `condition` (dmConditionVariable::HConditionVariable) - ConditionVariable handle.
- `mutex` (dmMutex::HMutex) - Mutex handle.
