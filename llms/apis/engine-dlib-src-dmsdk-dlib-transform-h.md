# Transform

**Namespace:** `dmTransform`
**Language:** C++
**Type:** Defold C++
**File:** `transform.h`
**Source:** `engine/dlib/src/dmsdk/dlib/transform.h`
**Include:** `dmsdk/dlib/transform.h`

Api for transforms with rotation, scale and translation

## API

### Apply
*Type:* FUNCTION
Apply the transform on a point (includes the transform translation).

**Parameters**

- `t` (dmTransform::Transform&) - Transform
- `p` (dmVMath::Point3&) - Point

**Returns**

- `point` (dmVMath::Point3) - Transformed point

### Apply
*Type:* FUNCTION
Apply the transform on a vector (excludes the transform translation).

**Parameters**

- `t` (dmTransform::Transform&) - Transform
- `v` (dmVMath::Vector3&) - Vector

**Returns**

- `point` (dmVMath::Vector3) - Transformed vector

### ExtractScale
*Type:* FUNCTION
Extract the absolute values of the scale component from a matrix.

**Parameters**

- `mtx` (dmVMath::Matrix4) - Source matrix

**Returns**

- `Vector3` - with scale values for x,y,z

### GetRotation
*Type:* FUNCTION
get rotatiom

**Returns**

- `rotation` (dmVMath::Quat)

### GetScale
*Type:* FUNCTION
get scale

**Returns**

- `scale` (dmVMath::Vector3)

### GetTranslation
*Type:* FUNCTION
get translation

**Returns**

- `translation` (dmVMath::Vector3)

### GetUniformScale
*Type:* FUNCTION
Compute a 'uniform' scale for this transform. In the event that the
scale applied to this transform is not uniform then the value is arbitrary:
we make a selection that will not introduce any floating point rounding errors.

**Returns**

- `scale` (float) - the uniform scale associated with this transform.

### Inv
*Type:* FUNCTION
Invert a transform

**Parameters**

- `t` (const dmTransform::Transform&)

**Returns**

- `result` (dmTransform::Transform) - inverted transform

### Mul
*Type:* FUNCTION
Transforms the right-hand transform by the left-hand transform

**Parameters**

- `lhs` (const dmTransform::Transform&)
- `rhs` (const dmTransform::Transform&)

**Returns**

- `result` (dmTransform::Transform) - Transformed transform

### NormalizeZScale
*Type:* FUNCTION
Eliminate the z scaling components in a matrix

**Parameters**

- `mtx` (dmVMath::Matrix4) - Matrix to operate on

### NormalizeZScale
*Type:* FUNCTION
Eliminate the z scaling components in a matrix

**Parameters**

- `source` (const dmVMath::Matrix&) - Source matrix
- `target` (dmVMath::Matrix*) - Target matrix

### ResetScale
*Type:* FUNCTION
Eliminate the scaling components in a matrix

**Parameters**

- `mtx` (dmVMath::Matrix4) - Matrix to operate on

**Returns**

- `Vector` - containing the scaling by component

### SetIdentity
*Type:* FUNCTION
initialize to identity transform

### SetRotation
*Type:* FUNCTION
set rotatiom

**Parameters**

- `rotation` (dmVMath::Quat)

### SetScale
*Type:* FUNCTION
set scale

**Returns**

- `scale` (dmVMath::Vector3)

### SetScaleXY
*Type:* FUNCTION
set scale for x and y

**Parameters**

- `scale_x` (float)
- `scale_y` (float)

### SetTranslation
*Type:* FUNCTION
set translation

**Parameters**

- `translation` (dmVMath::Vector3)

### SetUniformScale
*Type:* FUNCTION
set uniform scale

**Parameters**

- `scale` (float)

### ToMatrix4
*Type:* FUNCTION
Convert a transform into a 4-dim matrix

**Parameters**

- `t` (Transform) - Transform to convert

**Returns**

- `Matrix` - representing the same transform

### ToTransform
*Type:* FUNCTION
Convert a matrix into a transform

**Parameters**

- `mtx` (dmVMath::Matrix4) - Matrix4 to convert

**Returns**

- `Transform` - representing the same transform

### Transform
*Type:* STRUCT
Transform with non-uniform (3-component) scale.
Transform applied as:
T(p) = translate(rotate(scale(p))) = p'
The scale is non-rotated to avoid shearing in the transform.
Two transforms are applied as:
T1(T2(p)) = t1(r1(t2(r2(s1(s2(p)))))) = p'
This means that the transform is not associative:
T1(T2(p)) != (T1*T2)(P)

### Transform
*Type:* FUNCTION
Constructor. Leaves the struct in an uninitialized state

### Transform
*Type:* FUNCTION
constructor

**Parameters**

- `translation` (dmVMath::Vector3)
- `rotation` (dmVMath::Quat)
- `scale` (dmVMath::Vector3)

### Transform
*Type:* FUNCTION
constructor

**Parameters**

- `translation` (dmVMath::Vector3)
- `rotation` (dmVMath::Quat)
- `scale` (dmVMath::Vector3)
