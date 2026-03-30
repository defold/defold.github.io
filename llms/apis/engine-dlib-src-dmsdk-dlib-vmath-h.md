# Vector Math

**Namespace:** `dmVMath`
**Language:** C++
**Type:** Defold C++
**File:** `vmath.h`
**Source:** `engine/dlib/src/dmsdk/dlib/vmath.h`
**Include:** `dmsdk/dlib/vmath.h`

Vector Math functions.

## API

### AppendScale
*Type:* FUNCTION
post multiply scale

**Parameters**

- `m` (Matrix4) - the matrix
- `v` (Vector3) - the scale vector

**Returns**

- `r` (Matrix4) - the scaled vector

### Cross
*Type:* FUNCTION
cross product between two vectors

**Parameters**

- `a` (Vector3) - the operand
- `b` (Vector3) - the dividend

**Returns**

- `v` (Vector3) - the result vector

### DivPerElem
*Type:* FUNCTION
Divide two vectors per element: Vector3(a.x/b.x, a.y/b.y, a.z/b.z)

**Parameters**

- `a` (Vector3) - the operand
- `b` (Vector3) - the dividend

**Returns**

- `v` (Vector3) - the result vector

### DivPerElem
*Type:* FUNCTION
Divide two vectors per element: Vector3(a.x/b.x, a.y/b.y, a.z/b.z, a.w/b.w)

**Parameters**

- `a` (Vector4) - the operand
- `b` (Vector4) - the dividend

**Returns**

- `v` (Vector4) - the result vector

### Dot
*Type:* FUNCTION
dot product between two vectors

**Parameters**

- `a` (Vector3) - the first vector
- `b` (Vector3) - the second vector

**Returns**

- `dot_product` (float) - the dot product

### Dot
*Type:* FUNCTION
dot product between two vectors

**Parameters**

- `a` (Vector4) - the first vector
- `b` (Vector4) - the second vector

**Returns**

- `dot_product` (float) - the dot product

### Inverse
*Type:* FUNCTION
inverse matrix

**Parameters**

- `m` (Matrix3) - the rotation

**Returns**

- `r` (Matrix3) - the transposed matrix

### Inverse
*Type:* FUNCTION
inverse matrix

**Parameters**

- `m` (Matrix4) - the rotation

**Returns**

- `r` (Matrix4) - the transposed matrix

### Length
*Type:* FUNCTION
calculate length of a vector

**Parameters**

- `v` (Vector3) - the vector

**Returns**

- `length` (float) - the length

### Length
*Type:* FUNCTION
calculate length of a vector

**Parameters**

- `v` (Vector3) - the vector

**Returns**

- `length` (float) - the length

### Length
*Type:* FUNCTION
calculate length of a quaternion

**Parameters**

- `v` (Quat) - the quaternion

**Returns**

- `length` (float) - the length

### Length
*Type:* FUNCTION
calculate squared length of a vector

**Parameters**

- `v` (Vector3) - the vector

**Returns**

- `length` (float) - the squared length

### Length
*Type:* FUNCTION
calculate squared length of a vector

**Parameters**

- `v` (Vector4) - the vector

**Returns**

- `length` (float) - the squared length

### Length
*Type:* FUNCTION
calculate squared length of a quaternion

**Parameters**

- `v` (Quat) - the vector

**Returns**

- `length` (float) - the squared length

### Lerp
*Type:* FUNCTION
linear interpolate between two vectors

**Notes**

- Does not clamp t to between 0 and 1

**Parameters**

- `t` (float) - the unit time
- `a` (Vector3) - the start vector (t == 0)
- `b` (Vector3) - the end vector (t == 1)

**Returns**

- `v` (Vector3) - the result vector <code>v = a + (b - a) * t</code>

**Examples**

```
dmVMath::Vector3 v0 = dmVMath::Lerp(0.0f, a, b); // v0 == a
dmVMath::Vector3 v1 = dmVMath::Lerp(1.0f, a, b); // v1 == b
dmVMath::Vector3 v2 = dmVMath::Lerp(2.0f, a, b); // v2 == a + (b-a) * 2.0f

```

### Lerp
*Type:* FUNCTION
linear interpolate between two vectors

**Notes**

- Does not clamp t to between 0 and 1

**Parameters**

- `t` (float) - the unit time
- `a` (Vector4) - the start vector (t == 0)
- `b` (Vector4) - the end vector (t == 1)

**Returns**

- `v` (Vector4) - the result vector <code>v = a + (b - a) * t</code>

**Examples**

```
dmVMath::Vector4 v0 = dmVMath::Lerp(0.0f, a, b); // v0 == a
dmVMath::Vector4 v1 = dmVMath::Lerp(1.0f, a, b); // v1 == b
dmVMath::Vector4 v2 = dmVMath::Lerp(2.0f, a, b); // v2 == a + (b-a) * 2.0f

```

### Matrix3
*Type:* TYPEDEF
A 3x3 matrix

**Notes**

- 16 byte aligned
- Implemented as 3 x Vector3
- Column major
- Currently scalar implementation is used on most platforms

### Matrix4
*Type:* TYPEDEF
A 4x4 matrix

**Notes**

- 16 byte aligned
- Implemented as 4 x Vector4
- Column major
- Currently scalar implementation is used on most platforms

### MulPerElem
*Type:* FUNCTION
Multiply two vectors per element: Vector3(a.x * b.x, a.y * b.y, a.z * b.z)

**Parameters**

- `a` (Vector3) - the first vector
- `b` (Vector3) - the second vector

**Returns**

- `v` (Vector3) - the result vector

### MulPerElem
*Type:* FUNCTION
Multiply two vectors per element: Vector3(a.x * b.x, a.y * b.y, a.z * b.z, a.w * b.w)

**Parameters**

- `a` (Vector4) - the first vector
- `b` (Vector4) - the second vector

**Returns**

- `v` (Vector4) - the result vector

### MulPerElem
*Type:* FUNCTION
Return absolute value per element: Vector3(abs(v.x), abs(v.y), abs(v.z))

**Parameters**

- `v` (Vector3) - the vector

**Returns**

- `r` (Vector3) - the result vector

### MulPerElem
*Type:* FUNCTION
Returns the conjugate of the quaternion: conj = -q

**Parameters**

- `q` (Quat) - the quaternions

**Returns**

- `r` (Quat) - the result

### Normalize
*Type:* FUNCTION
normalize a vector to length 1

**Parameters**

- `v` (Vector3) - the vector

**Returns**

- `n` (Vector3) - the normalized vector

### Normalize
*Type:* FUNCTION
normalize a vector to length 1

**Parameters**

- `v` (Vector4) - the vector

**Returns**

- `n` (Vector4) - the normalized vector

### Normalize
*Type:* FUNCTION
normalize a quaternion to length 1

**Parameters**

- `v` (Quat) - the quaternion

**Returns**

- `n` (Quat) - the normalized quaternion

### OrthoInverse
*Type:* FUNCTION
Compute the inverse of a 4x4 matrix, which is expected to be an affine matrix with an orthogonal upper-left 3x3 submatrix

**Parameters**

- `m` (Matrix4) - the rotation

**Returns**

- `r` (Matrix4) - the transposed matrix

### Point3
*Type:* TYPEDEF
A 3-tuple (with 4-th element always set to 1)

**Notes**

- 16 byte aligned
- Always size of 4 float32
- Currently scalar implementation is used on most platforms

**Examples**

```
dmVMath::Point3 p = dmVMath::Point3(x, y, z); // Create new point
float length_squared = p.getX() * p.getX() + p.getY() * p.getY() + p.getZ() * p.getZ();

```

### Quat
*Type:* TYPEDEF
A 4-tuple representing a rotation rotation. The xyz represents the axis, and the w represents the angle.

**Notes**

- 16 byte aligned
- Always size of 4 float32
- Currently scalar implementation is used on most platforms

**Examples**

```
dmVMath::Quat p = dmVMath::Quat(x, y, z, w); // Create new rotation. W is the angle

```

### Rotate
*Type:* FUNCTION
rotate vector using quaternion

**Parameters**

- `q` (Quat) - the rotation
- `v` (Vector3) - the vector

**Returns**

- `r` (Vector3) - the rotated vector

### Slerp
*Type:* FUNCTION
spherical linear interpolate between two vectors

**Notes**

- Does not clamp t to between 0 and 1
- Unpredicatable results if a and b point in opposite direction

**Parameters**

- `t` (float) - the unit time
- `a` (Vector3) - the start vector (t == 0)
- `b` (Vector3) - the end vector (t == 1)

**Returns**

- `v` (Vector3) - the result vector

### Slerp
*Type:* FUNCTION
spherical linear interpolate between two vectors

**Notes**

- Does not clamp t to between 0 and 1
- Unpredicatable results if a and b point in opposite direction

**Parameters**

- `t` (float) - the unit time
- `a` (Vector4) - the start vector (t == 0)
- `b` (Vector4) - the end vector (t == 1)

**Returns**

- `v` (Vector4) - the result vector

### Slerp
*Type:* FUNCTION
Interpolates along the shortest path between two quaternions

**Notes**

- Does not clamp t to between 0 and 1

**Parameters**

- `t` (float) - the unit time
- `a` (Quat) - the start vector (t == 0)
- `b` (Quat) - the end vector (t == 1)

**Returns**

- `v` (Quat) - the result vector

### Transpose
*Type:* FUNCTION
transpose matrix

**Parameters**

- `m` (Matrix3) - the rotation

**Returns**

- `r` (Matrix3) - the transposed matrix

### Transpose
*Type:* FUNCTION
transpose matrix

**Parameters**

- `m` (Matrix4) - the rotation

**Returns**

- `r` (Matrix4) - the transposed matrix

### Vector3
*Type:* TYPEDEF
A 3-tuple (with 4-th element always set to 0)

**Notes**

- 16 byte aligned
- Always size of 4 float32
- Currently scalar implementation is used on most platforms

**Examples**

```
dmVMath::Vector3 p = dmVMath::Vector3(x, y, z); // Create new vector
float length_squared = p.getX() * p.getX() + p.getY() * p.getY() + p.getZ() * p.getZ();

```

### Vector4
*Type:* TYPEDEF
A 4-tuple

**Notes**

- 16 byte aligned
- Always size of 4 float32
- Currently scalar implementation is used on most platforms

**Examples**

```
dmVMath::Vector4 p = dmVMath::Vector4(x, y, z, w); // Create new vector
float length_squared = p.getX() * p.getX() + p.getY() * p.getY() + p.getZ() * p.getZ() + p.getW() * p.getW();

```
