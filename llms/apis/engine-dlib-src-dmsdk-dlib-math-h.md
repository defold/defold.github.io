# Math

**Namespace:** `dmMath`
**Language:** C++
**Type:** Defold C++
**File:** `math.h`
**Source:** `engine/dlib/src/dmsdk/dlib/math.h`
**Include:** `dmsdk/dlib/math.h`

Math functions.

## API

### Abs
*Type:* FUNCTION
Abs function

**Template Parameters**

- `T`

**Parameters**

- `x` (T)

**Returns**

- `v` (T) - Absolute value of x

### Clamp
*Type:* FUNCTION
Clamp function

**Template Parameters**

- `T`

**Parameters**

- `v` (T) - Value to clamp
- `min` (T) - Lower bound
- `max` (T) - Upper bound

**Returns**

- `v` (T) - Value closest to v inside the range [min, max]

### Max
*Type:* FUNCTION
Max function

**Template Parameters**

- `T`

**Parameters**

- `a` (T) - Value a
- `b` (T) - Value b

**Returns**

- `v` (T) - Max of a and b

### Min
*Type:* FUNCTION
Min function

**Template Parameters**

- `T`

**Parameters**

- `a` (T) - Value a
- `b` (T) - Value b

**Returns**

- `v` (T) - Min of a and b

### Select
*Type:* FUNCTION
Select one of two values depending on the sign of another.

**Template Parameters**

- `T`

**Parameters**

- `x` (T) - Value to test for positiveness
- `a` (T) - Result if test succeeded
- `b` (T) - Result if test failed

**Returns**

- `v` (T) - a when x &gt;= 0, b otherwise
