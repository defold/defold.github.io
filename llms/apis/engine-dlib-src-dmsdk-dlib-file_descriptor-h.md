# FileDescriptor

**Namespace:** `dmFileDescriptor`
**Language:** C++
**Type:** Defold C++
**File:** `file_descriptor.h`
**Source:** `engine/dlib/src/dmsdk/dlib/file_descriptor.h`
**Include:** `dmsdk/dlib/file_descriptor.h`

File Descriptor functions.

## API

### Poller
*Type:* STRUCT
Poller

### PollerClearEvent
*Type:* FUNCTION
Clear event from poller.

**Parameters**

- `poller` (dmFileDescriptor::Poller*) - Poller
- `event` (dmFileDescriptor::PollEvent) - Event to clear
- `fd` (int) - File descriptor to clear

**Returns**

- `return` (void)

### PollerHasEvent
*Type:* FUNCTION
Check if event exists for file descriptor

**Parameters**

- `poller` (dmFileDescriptor::Poller*) - Poller
- `event` (dmFileDescriptor::PollEvent) - Event to check
- `fd` (int) - File descriptor to clear

**Returns**

- `return` (bool) - True if event exists.

### PollerReset
*Type:* FUNCTION
Reset poller.

**Parameters**

- `spoller` (dmFileDescriptor::Poller*) - Poller

**Returns**

- `return` (void)

### PollerSetEvent
*Type:* FUNCTION
Set file descriptor event to poll for

**Parameters**

- `poller` (dmFileDescriptor::Poller*) - Poller
- `event` (dmFileDescriptor::PollEvent) - Event to set
- `fd` (int) - File descriptor to clear

**Returns**

- `return` (void)

### PollEvent
*Type:* ENUM
Poll events

**Members**

- `EVENT_READ`
- `EVENT_WRITE`
- `EVENT_ERROR`

### Wait
*Type:* FUNCTION
Wait for event

**Parameters**

- `poller` (dmFileDescriptor::Poller*) - Poller
- `timeout` (int) - Timeout. For blocking pass -1. (milliseconds)

**Returns**

- `return` (int) - Non-negative value on success, 0 on timeout and
-1 on error with errno set to indicate the error
