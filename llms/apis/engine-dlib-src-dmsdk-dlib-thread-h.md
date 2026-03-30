# Thread

**Namespace:** `dmThread`
**Language:** C++
**Type:** Defold C++
**File:** `thread.h`
**Source:** `engine/dlib/src/dmsdk/dlib/thread.h`
**Include:** `dmsdk/dlib/thread.h`

Thread functions.

## API

### AllocTls
*Type:* FUNCTION
Allocate thread local storage key

**Returns**

- `key` (dmThread::TlsKey) - Key

### Detach
*Type:* FUNCTION
Detach thread. When a detached thread terminates, its resources are
automatically released back to the system without the need for another
thread to join with the terminated thread.

**Parameters**

- `thread` (dmThread::Thread) - Thread to detach

### FreeTls
*Type:* FUNCTION
Free thread local storage key

**Parameters**

- `key` (dmThread::TlsKey) - Key

### GetCurrentThread
*Type:* FUNCTION
Gets the current thread

**Returns**

- `thread` (dmThread::Thread) - the current thread

### GetTlsValue
*Type:* FUNCTION
Get thread specific data

**Parameters**

- `key` (dmThread::TlsKey) - Key

### Join
*Type:* FUNCTION
Join thread. Waits for the thread specified by thread to terminate.  If
that thread has already terminated, then Join() returns immediately.  The
thread specified by thread must be joinable (see Detach()).

**Parameters**

- `thread` (dmThread::Thread) - Thread to join

### New
*Type:* FUNCTION
Create a new named thread

**Notes**

- thread name currently not supported on win32

**Parameters**

- `thread_start` (ThreadStart) - Thread entry function
- `stack_size` (uint32_t) - Stack size
- `arg` (void*) - Thread argument
- `name` (const char*) - Thread name

**Returns**

- `thread` (dmThread::Thread) - Thread handle

**Examples**

Create a thread
```
#include
#include

struct Context
{
    bool m_DoWork;
    int  m_Work;
};

static void Worker(void* _ctx)
{
    Context* ctx = (Context*)_ctx;
    while (ctx->m_DoWork)
    {
        ctx->m_Work++; // do work
        dmTime::Sleep(10*1000); // yield
    }
}

int StartThread()
{
    Context ctx;
    ctx.m_DoWork = true;
    ctx.m_Work = 0;
    dmThread::Thread thread = dmThread::New(Worker, 0x80000, (void*)&ctx, "my_thread");

    // do other work...
    // ..eventually stop the thread:
    ctx.m_DoWork = false;

    // wait for thread
    dmThread::Join(thread);

    printf("work done: %d\n", ctx.m_Work);
}

```

### SetThreadName
*Type:* FUNCTION
Sets the current thread name

**Notes**

- The thread argument is unused on Darwin (uses current thread)

**Parameters**

- `thread` (dmThread::Thread) - the thread
- `name` (const char*) - the thread name

### SetTlsValue
*Type:* FUNCTION
Set thread specific data

**Parameters**

- `key` (dmThread::TlsKey) - Key
- `value` (void*) - Value

### ThreadStart
*Type:* TYPEDEF
