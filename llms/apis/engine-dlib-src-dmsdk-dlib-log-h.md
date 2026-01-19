# Log

**Namespace:** `Log`
**Language:** C++
**Type:** Defold C++
**File:** `log.h`
**Source:** `engine/dlib/src/dmsdk/dlib/log.h`
**Include:** `dmsdk/dlib/log.h`

Logging functions.

## Notes

- Log functions will be omitted (NOP) for release builds
- Prefer these functions over `printf` since these can print to the platform specific logs

## API

### DLIB_LOG_DOMAIN
*Type:* MACRO
If DLIB_LOG_DOMAIN is defined the value of the defined is printed after severity.
Otherwise DEFAULT will be printed.

**Notes**

- Extensions do not need to set this since they get their own logging domain automatically

**Examples**

```
#define DLIB_LOG_DOMAIN "MyOwnDomain"
#include

```

### dmLogDebug
*Type:* FUNCTION
Debug messages are temporary log instances used when debugging a certain behavior
Use dmLogOnceDebug for one-shot logging

**Parameters**

- `format` (const char*) - Format string
- `args` (...) - Format string args (variable arg list)

**Returns**

- `return` (void)

### dmLogError
*Type:* FUNCTION
Error messages are used in cases where an recoverable error has occurred.
Use dmLogOnceError for one-shot logging

**Parameters**

- `format` (const char*) - Format string
- `args` (...) - Format string args (variable arg list)

**Returns**

- `return` (void)

### dmLogFatal
*Type:* FUNCTION
Fatal messages are used in cases where an unrecoverable error has occurred.
Use dmLogOnceFatal for one-shot logging

**Parameters**

- `format` (const char*) - Format string
- `args` (...) - Format string args (variable arg list)

**Returns**

- `return` (void)

### dmLogGetLevel
*Type:* FUNCTION
Get log system severity level.

**Returns**

- `severity` (LogSeverity) - Current log system severity level

### dmLogInfo
*Type:* FUNCTION
Info messages are used to inform the developers of relevant information
Use dmLogOnceInfo for one-shot logging

**Parameters**

- `format` (const char*) - Format string
- `args` (...) - Format string args (variable arg list)

**Returns**

- `return` (void)

### dmLogRegisterListener
*Type:* FUNCTION
Registers a log listener.
This listener receive logs even in release bundle.

**Notes**

- Any calls to dmLogInfo et al from within the calllback will be ignored

**Parameters**

- `listener` (FLogListener)

### dmLogSetLevel
*Type:* FUNCTION
Set log system severity level.

**Parameters**

- `severity` (LogSeverity) - Log system severity level to set

### dmLogUnregisterListener
*Type:* FUNCTION
Unregisters a log listener.

**Parameters**

- `listener` (FLogListener)

### dmLogUserDebug
*Type:* FUNCTION
Debug messages are temporary log instances used when debugging a certain behavior
Use dmLogOnceUserDebug for one-shot logging

**Parameters**

- `format` (const char*) - Format string
- `args` (...) - Format string args (variable arg list)

**Returns**

- `return` (void)

### dmLogWarning
*Type:* FUNCTION
Warning messages are used to inform the developers about potential problems which can cause errors.
Use dmLogOnceWarning for one-shot logging

**Parameters**

- `format` (const char*) - Format string
- `args` (...) - Format string args (variable arg list)

**Returns**

- `return` (void)

### FLogListener
*Type:* TYPEDEF
dmLog listener function type. Provides all logs from dmLog* functions and print/pprint Lua functions.
Used with dmLogRegisterListener() and dmLogUnregisterListener()

**Parameters**

- `severity` (LogSeverity)
- `domain` (const char*)
- `formatted_string` (const char*) - null terminated string

### LogSeverity
*Type:* ENUM
Log severity

**Members**

- `LOG_SEVERITY_DEBUG`
- `LOG_SEVERITY_USER_DEBUG`
- `LOG_SEVERITY_INFO`
- `LOG_SEVERITY_WARNING`
- `LOG_SEVERITY_ERROR`
- `LOG_SEVERITY_FATAL`
