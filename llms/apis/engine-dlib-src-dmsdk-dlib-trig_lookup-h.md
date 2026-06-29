# TrigLookup

**Namespace:** `dmTrigLookup`
**Language:** C++
**Type:** Defold C++
**File:** `trig_lookup.h`
**Source:** `engine/dlib/src/dmsdk/dlib/trig_lookup.h`
**Include:** `dmsdk/dlib/trig_lookup.h`

Api for trigonometrics using lookup tables. The precision is guaranteed to
have an error less than 0.001f.

## API

### Cos
*Type:* FUNCTION
Returns the cosine of the given angle from a lookup table.

**Parameters**

- `radians` (float) - Radians of the angle

**Returns**

- `cosine` (float) - The cosine of the angle

### Sin
*Type:* FUNCTION
Returns the sine of the given angle from a lookup table.

**Parameters**

- `radians` (float) - Radians of the angle

**Returns**

- `sine` (float) - The sine of the angle
