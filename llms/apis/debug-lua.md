# Debug

**Namespace:** `debug`
**Language:** Lua
**Type:** Defold Lua
**File:** `lua_debug.doc_h`
**Source:** `engine/lua/src/lua_debug.doc_h`

Documentation for the Lua debug standard library.

From [Lua 5.1 Reference Manual](https://www.lua.org/manual/5.1/)
by Roberto Ierusalimschy, Luiz Henrique de Figueiredo, Waldemar Celes.

Copyright © 2006-2012 Lua.org, PUC-Rio.

Freely available under the terms of the [Lua license](https://www.lua.org/license.html).

## API

### debug.debug
*Type:* FUNCTION
Enters an interactive mode with the user,
running each string that the user enters.
Using simple commands and other debug facilities,
the user can inspect global and local variables,
change their values, evaluate expressions, and so on.
A line containing only the word cont finishes this function,
so that the caller continues its execution.
Note that commands for debug.debug are not lexically nested
within any function, and so have no direct access to local variables.

### debug.getfenv
*Type:* FUNCTION
Returns the environment of object o.

**Parameters**

- `o` (any)

### debug.gethook
*Type:* FUNCTION
Returns the current hook settings of the thread, as three values:
the current hook function, the current hook mask,
and the current hook count
(as set by the debug.sethook function).

**Parameters**

- `thread` (thread) (optional)

### debug.getinfo
*Type:* FUNCTION
Returns a table with information about a function.
You can give the function directly,
or you can give a number as the value of function,
which means the function running at level function of the call stack
of the given thread:
level 0 is the current function (getinfo itself);
level 1 is the function that called getinfo;
and so on.
If function is a number larger than the number of active functions,
then getinfo returns  nil.
The returned table can contain all the fields returned by lua_getinfo,
with the string what describing which fields to fill in.
The default for what is to get all information available,
except the table of valid lines.
If present,
the option 'f'
adds a field named func with the function itself.
If present,
the option 'L'
adds a field named activelines with the table of
valid lines.
For instance, the expression debug.getinfo(1,"n").name returns
a table with a name for the current function,
if a reasonable name can be found,
and the expression debug.getinfo(print)
returns a table with all available information
about the print function.

**Parameters**

- `thread` (thread) (optional)
- `function` (function)
- `what` (string) (optional)

### debug.getlocal
*Type:* FUNCTION
This function returns the name and the value of the local variable
with index local of the function at level level of the stack.
(The first parameter or local variable has index 1, and so on,
until the last active local variable.)
The function returns  nil if there is no local
variable with the given index,
and raises an error when called with a level out of range.
(You can call debug.getinfo to check whether the level is valid.)
Variable names starting with '(' (open parentheses)
represent internal variables
(loop control variables, temporaries, and C function locals).

**Parameters**

- `thread` (thread) (optional)
- `level` (number)
- `local` (number)

### debug.getmetatable
*Type:* FUNCTION
Returns the metatable of the given object
or  nil if it does not have a metatable.

**Parameters**

- `object` (any)

### debug.getregistry
*Type:* FUNCTION
Returns the registry table .

### debug.getupvalue
*Type:* FUNCTION
This function returns the name and the value of the upvalue
with index up of the function func.
The function returns  nil if there is no upvalue with the given index.

**Parameters**

- `func` (function)
- `up` (number)

### debug.setfenv
*Type:* FUNCTION
Sets the environment of the given object to the given table.
Returns object.

**Parameters**

- `object` (any)
- `table` (table)

### debug.sethook
*Type:* FUNCTION
Sets the given function as a hook.
The string mask and the number count describe
when the hook will be called.
The string mask may have the following characters,
with the given meaning:

"c"
the hook is called every time Lua calls a function;
"r"
the hook is called every time Lua returns from a function;
"l"
the hook is called every time Lua enters a new line of code.

With a count different from zero,
the hook is called after every count instructions.
When called without arguments,
debug.sethook turns off the hook.
When the hook is called, its first parameter is a string
describing the event that has triggered its call:
"call", "return" (or "tail return",
when simulating a return from a tail call),
"line", and "count".
For line events,
the hook also gets the new line number as its second parameter.
Inside a hook,
you can call getinfo with level 2 to get more information about
the running function
(level 0 is the getinfo function,
and level 1 is the hook function),
unless the event is "tail return".
In this case, Lua is only simulating the return,
and a call to getinfo will return invalid data.

**Parameters**

- `thread` (thread) (optional)
- `hook` (function)
- `mask` (string)
- `count` (number) (optional)

### debug.setlocal
*Type:* FUNCTION
This function assigns the value value to the local variable
with index local of the function at level level of the stack.
The function returns  nil if there is no local
variable with the given index,
and raises an error when called with a level out of range.
(You can call getinfo to check whether the level is valid.)
Otherwise, it returns the name of the local variable.

**Parameters**

- `thread` (thread) (optional)
- `level` (number)
- `local` (number)
- `value` (any)

### debug.setmetatable
*Type:* FUNCTION
Sets the metatable for the given object to the given table
(which can be  nil).

**Parameters**

- `object` (any)
- `table` (table)

### debug.setupvalue
*Type:* FUNCTION
This function assigns the value value to the upvalue
with index up of the function func.
The function returns  nil if there is no upvalue
with the given index.
Otherwise, it returns the name of the upvalue.

**Parameters**

- `func` (function)
- `up` (number)
- `value` (any)

### debug.traceback
*Type:* FUNCTION
Returns a string with a traceback of the call stack.
An optional message string is appended
at the beginning of the traceback.
An optional level number tells at which level
to start the traceback
(default is 1, the function calling traceback).

**Parameters**

- `thread` (thread) (optional)
- `message` (string) (optional)
- `level` (number) (optional)
