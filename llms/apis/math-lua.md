# Math

**Namespace:** `math`
**Language:** Lua
**Type:** Defold Lua
**File:** `lua_math.doc_h`
**Source:** `engine/lua/src/lua_math.doc_h`

Documentation for the Lua math standard library.

From [Lua 5.1 Reference Manual](https://www.lua.org/manual/5.1/)
by Roberto Ierusalimschy, Luiz Henrique de Figueiredo, Waldemar Celes.

Copyright © 2006-2012 Lua.org, PUC-Rio.

Freely available under the terms of the [Lua license](https://www.lua.org/license.html).

## API

### math.abs
*Type:* FUNCTION
Returns the absolute value of x.

**Parameters**

- `x` (number)

### math.acos
*Type:* FUNCTION
Returns the arc cosine of x (in radians).

**Parameters**

- `x` (number)

### math.asin
*Type:* FUNCTION
Returns the arc sine of x (in radians).

**Parameters**

- `x` (number)

### math.atan
*Type:* FUNCTION
Returns the arc tangent of x (in radians).

**Parameters**

- `x` (number)

### math.atan2
*Type:* FUNCTION
Returns the arc tangent of y/x (in radians),
but uses the signs of both parameters to find the
quadrant of the result.
(It also handles correctly the case of x being zero.)

**Parameters**

- `y` (number)
- `x` (number)

### math.ceil
*Type:* FUNCTION
Returns the smallest integer larger than or equal to x.

**Parameters**

- `x` (number)

### math.cos
*Type:* FUNCTION
Returns the cosine of x (assumed to be in radians).

**Parameters**

- `x` (number)

### math.cosh
*Type:* FUNCTION
Returns the hyperbolic cosine of x.

**Parameters**

- `x` (number)

### math.deg
*Type:* FUNCTION
Returns the angle x (given in radians) in degrees.

**Parameters**

- `x` (number)

### math.exp
*Type:* FUNCTION
Returns the value ex.

**Parameters**

- `x` (number)

### math.floor
*Type:* FUNCTION
Returns the largest integer smaller than or equal to x.

**Parameters**

- `x` (number)

### math.fmod
*Type:* FUNCTION
Returns the remainder of the division of x by y
that rounds the quotient towards zero.

**Parameters**

- `x` (number)
- `y` (number)

### math.frexp
*Type:* FUNCTION
Returns m and e such that x = m2e,
e is an integer and the absolute value of m is
in the range [0.5, 1)
(or zero when x is zero).

**Parameters**

- `x` (number)

### math.huge
*Type:* VARIABLE
The value HUGE_VAL,
a value larger than or equal to any other numerical value.

### math.ldexp
*Type:* FUNCTION
Returns m2e (e should be an integer).

**Parameters**

- `m` (number)
- `e` (number)

### math.log
*Type:* FUNCTION
Returns the natural logarithm of x.

**Parameters**

- `x` (number)

### math.log10
*Type:* FUNCTION
Returns the base-10 logarithm of x.

**Parameters**

- `x` (number)

### math.max
*Type:* FUNCTION
Returns the maximum value among its arguments.

**Parameters**

- `x` (number)
- `...`

### math.min
*Type:* FUNCTION
Returns the minimum value among its arguments.

**Parameters**

- `x` (number)
- `...`

### math.modf
*Type:* FUNCTION
Returns two numbers,
the integral part of x and the fractional part of x.

**Parameters**

- `x` (number)

### math.pi
*Type:* VARIABLE
The value of PI.

### math.pow
*Type:* FUNCTION
Returns xy.
(You can also use the expression x^y to compute this value.)

**Parameters**

- `x` (number)
- `y` (number)

### math.rad
*Type:* FUNCTION
Returns the angle x (given in degrees) in radians.

**Parameters**

- `x` (number)

### math.random
*Type:* FUNCTION
This function is an interface to the simple
pseudo-random generator function rand provided by ANSI C.
(No guarantees can be given for its statistical properties.)
When called without arguments,
returns a uniform pseudo-random real number
in the range [0,1).
When called with an integer number m,
math.random returns
a uniform pseudo-random integer in the range [1, m].
When called with two integer numbers m and n,
math.random returns a uniform pseudo-random
integer in the range [m, n].

**Parameters**

- `m` (number) (optional)
- `n` (number) (optional)

### math.randomseed
*Type:* FUNCTION
Sets x as the "seed"
for the pseudo-random generator:
equal seeds produce equal sequences of numbers.

**Parameters**

- `x` (number)

### math.sin
*Type:* FUNCTION
Returns the sine of x (assumed to be in radians).

**Parameters**

- `x` (number)

### math.sinh
*Type:* FUNCTION
Returns the hyperbolic sine of x.

**Parameters**

- `x` (number)

### math.sqrt
*Type:* FUNCTION
Returns the square root of x.
(You can also use the expression x^0.5 to compute this value.)

**Parameters**

- `x` (number)

### math.tan
*Type:* FUNCTION
Returns the tangent of x (assumed to be in radians).

**Parameters**

- `x` (number)

### math.tanh
*Type:* FUNCTION
Returns the hyperbolic tangent of x.

**Parameters**

- `x` (number)
