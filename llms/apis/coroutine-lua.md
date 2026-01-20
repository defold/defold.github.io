# Coroutine

**Namespace:** `coroutine`
**Language:** Lua
**Type:** Defold Lua
**File:** `lua_coroutine.doc_h`
**Source:** `engine/lua/src/lua_coroutine.doc_h`

Documentation for the Lua coroutine standard library.

From [Lua 5.1 Reference Manual](https://www.lua.org/manual/5.1/)
by Roberto Ierusalimschy, Luiz Henrique de Figueiredo, Waldemar Celes.

Copyright © 2006-2012 Lua.org, PUC-Rio.

Freely available under the terms of the [Lua license](https://www.lua.org/license.html).

## API

### coroutine.create
*Type:* FUNCTION
Creates a new coroutine, with body f.
f must be a Lua function.
Returns this new coroutine,
an object with type "thread".

**Parameters**

- `f` (function)

### coroutine.resume
*Type:* FUNCTION
Starts or continues the execution of coroutine co.
The first time you resume a coroutine,
it starts running its body.
The values val1, ... are passed
as the arguments to the body function.
If the coroutine has yielded,
resume restarts it;
the values val1, ... are passed
as the results from the yield.
If the coroutine runs without any errors,
resume returns  true plus any values passed to yield
(if the coroutine yields) or any values returned by the body function
(if the coroutine terminates).
If there is any error,
resume returns  false plus the error message.

**Parameters**

- `co` (thread)
- `val1` (any) (optional)
- `...` (optional)

### coroutine.running
*Type:* FUNCTION
Returns the running coroutine,
or  nil when called by the main thread.

### coroutine.status
*Type:* FUNCTION
Returns the status of coroutine co, as a string:
"running",
if the coroutine is running (that is, it called status);
"suspended", if the coroutine is suspended in a call to yield,
or if it has not started running yet;
"normal" if the coroutine is active but not running
(that is, it has resumed another coroutine);
and "dead" if the coroutine has finished its body function,
or if it has stopped with an error.

**Parameters**

- `co` (thread)

### coroutine.wrap
*Type:* FUNCTION
Creates a new coroutine, with body f.
f must be a Lua function.
Returns a function that resumes the coroutine each time it is called.
Any arguments passed to the function behave as the
extra arguments to resume.
Returns the same values returned by resume,
except the first boolean.
In case of error, propagates the error.

**Parameters**

- `f` (function)

### coroutine.yield
*Type:* FUNCTION
Suspends the execution of the calling coroutine.
The coroutine cannot be running a C function,
a metamethod, or an iterator.
Any arguments to yield are passed as extra results to resume.

**Parameters**

- `...`
