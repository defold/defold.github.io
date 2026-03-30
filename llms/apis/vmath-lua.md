# Vector math

**Namespace:** `vmath`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_vmath.cpp`
**Source:** `engine/script/src/script_vmath.cpp`

Functions for mathematical operations on vectors, matrices and quaternions.

- The vector types (`vmath.vector3` and `vmath.vector4`) supports addition and subtraction
  with vectors of the same type. Vectors can be negated and multiplied (scaled) or divided by numbers.
- The quaternion type (`vmath.quat`) supports multiplication with other quaternions.
- The matrix type (`vmath.matrix4`) can be multiplied with numbers, other matrices
  and `vmath.vector4` values.
- All types performs equality comparison by each component value.

The following components are available for the various types:

vector3
: `x`, `y` and `z`. Example: `v.y`

vector4
: `x`, `y`, `z`, and `w`. Example: `v.w`

quaternion
: `x`, `y`, `z`, and `w`. Example: `q.w`

matrix4
: `m00` to `m33` where the first number is the row (starting from 0) and the second
number is the column. Columns can be accessed with `c0` to `c3`, returning a `vector4`.
Example: `m.m21` which is equal to `m.c1.z`

vector
: indexed by number 1 to the vector length. Example: `v[3]`

## API

### vmath.clamp
*Type:* FUNCTION
Clamp input value to be in range of [min, max]. In case if input value has vector3|vector4 type
return new vector3|vector4 with clamped value at every vector's element.
Min/max arguments can be vector3|vector4. In that case clamp excuted per every vector's element

**Parameters**

- `value` (number | vector3 | vector4) - Input value or vector of values
- `min` (number | vector3 | vector4) - Min value(s) border
- `max` (number | vector3 | vector4) - Max value(s) border

**Returns**

- `clamped_value` (number | vector3 | vector4) - Clamped value or vector

**Examples**

```
local value1 = 56
print(vmath.clamp(value1, 89, 134)) -> 89
local v2 = vmath.vector3(190, 190, -10)
print(vmath.clamp(v2, -50, 150)) -> vmath.vector3(150, 150, -10)
local v3 = vmath.vector4(30, -30, 45, 1)
print(vmath.clamp(v3, 0, 20)) -> vmath.vector4(20, 0, 20, 1)

local min_v = vmath.vector4(0, -10, -10, 1)
print(vmath.clamp(v3, min_v, 20)) -> vmath.vector4(20, -10, 20, 1)

```

### vmath.conj
*Type:* FUNCTION
Calculates the conjugate of a quaternion. The result is a
quaternion with the same magnitudes but with the sign of
the imaginary (vector) parts changed:
q* = [w, -v]

**Parameters**

- `q1` (quaternion) - quaternion of which to calculate the conjugate

**Returns**

- `q` (quaternion) - the conjugate

**Examples**

```
local quat = vmath.quat(1, 2, 3, 4)
print(vmath.conj(quat)) --> vmath.quat(-1, -2, -3, 4)

```

### vmath.cross
*Type:* FUNCTION
Given two linearly independent vectors P and Q, the cross product,
P × Q, is a vector that is perpendicular to both P and Q and
therefore normal to the plane containing them.
If the two vectors have the same direction (or have the exact
opposite direction from one another, i.e. are not linearly independent)
or if either one has zero length, then their cross product is zero.

**Parameters**

- `v1` (vector3) - first vector
- `v2` (vector3) - second vector

**Returns**

- `v` (vector3) - a new vector representing the cross product

**Examples**

```
local vec1 = vmath.vector3(1, 0, 0)
local vec2 = vmath.vector3(0, 1, 0)
print(vmath.cross(vec1, vec2)) --> vmath.vector3(0, 0, 1)
local vec3 = vmath.vector3(-1, 0, 0)
print(vmath.cross(vec1, vec3)) --> vmath.vector3(0, -0, 0)

```

### vmath.dot
*Type:* FUNCTION
The returned value is a scalar defined as:
P ⋅ Q = |P| |Q| cos θ
where θ is the angle between the vectors P and Q.

If the dot product is positive then the angle between the vectors is below 90 degrees.
If the dot product is zero the vectors are perpendicular (at right-angles to each other).
If the dot product is negative then the angle between the vectors is more than 90 degrees.

**Parameters**

- `v1` (vector3 | vector4) - first vector
- `v2` (vector3 | vector4) - second vector

**Returns**

- `n` (number) - dot product

**Examples**

```
if vmath.dot(vector1, vector2) == 0 then
    -- The two vectors are perpendicular (at right-angles to each other)
    ...
end

```

### vmath.euler_to_quat
*Type:* FUNCTION
Converts euler angles (x, y, z) in degrees into a quaternion
The error is guaranteed to be less than 0.001.
If the first argument is vector3, its values are used as x, y, z angles.

**Parameters**

- `x` (number | vector3) - rotation around x-axis in degrees or vector3 with euler angles in degrees
- `y` (number) - rotation around y-axis in degrees
- `z` (number) - rotation around z-axis in degrees

**Returns**

- `q` (quaternion) - quaternion describing an equivalent rotation (231 (YZX) rotation sequence)

**Examples**

```
local q = vmath.euler_to_quat(0, 45, 90)
print(q) --> vmath.quat(0.27059805393219, 0.27059805393219, 0.65328145027161, 0.65328145027161)

local v = vmath.vector3(0, 0, 90)
print(vmath.euler_to_quat(v)) --> vmath.quat(0, 0, 0.70710676908493, 0.70710676908493)

```

### vmath.inv
*Type:* FUNCTION
The resulting matrix is the inverse of the supplied matrix.
 For ortho-normal matrices, e.g. regular object transformation,
use vmath.ortho_inv() instead.
The specialized inverse for ortho-normalized matrices is much faster
than the general inverse.

**Parameters**

- `m1` (matrix4) - matrix to invert

**Returns**

- `m` (matrix4) - inverse of the supplied matrix

**Examples**

```
local mat1 = vmath.matrix4_rotation_z(3.141592653)
local mat2 = vmath.inv(mat1)
-- M * inv(M) = identity matrix
print(mat1 * mat2) --> vmath.matrix4(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)

```

### vmath.length
*Type:* FUNCTION
Returns the length of the supplied vector or quaternion.
If you are comparing the lengths of vectors or quaternions, you should compare
the length squared instead as it is slightly more efficient to calculate
(it eliminates a square root calculation).

**Parameters**

- `v` (vector3 | vector4 | quaternion) - value of which to calculate the length

**Returns**

- `n` (number) - length

**Examples**

```
if vmath.length(self.velocity) < max_velocity then
    -- The speed (velocity vector) is below max.

    -- TODO: max_velocity can be expressed as squared
    -- so we can compare with length_sqr() instead.
    ...
end

```

### vmath.length_sqr
*Type:* FUNCTION
Returns the squared length of the supplied vector or quaternion.

**Parameters**

- `v` (vector3 | vector4 | quaternion) - value of which to calculate the squared length

**Returns**

- `n` (number) - squared length

**Examples**

```
if vmath.length_sqr(vector1) < vmath.length_sqr(vector2) then
    -- Vector 1 has less magnitude than vector 2
    ...
end

```

### vmath.lerp
*Type:* FUNCTION
Linearly interpolate between two vectors. The function
treats the vectors as positions and interpolates between
the positions in a straight line. Lerp is useful to describe
transitions from one place to another over time.
 The function does not clamp t between 0 and 1.

**Parameters**

- `t` (number) - interpolation parameter, 0-1
- `v1` (vector3 | vector4) - vector to lerp from
- `v2` (vector3 | vector4) - vector to lerp to

**Returns**

- `v` (vector3 | vector4) - the lerped vector

**Examples**

```
function init(self)
    self.t = 0
end

function update(self, dt)
    self.t = self.t + dt
    if self.t <= 1 then
        local startpos = vmath.vector3(0, 600, 0)
        local endpos = vmath.vector3(600, 0, 0)
        local pos = vmath.lerp(self.t, startpos, endpos)
        go.set_position(pos, "go")
    end
end

```

### vmath.lerp
*Type:* FUNCTION
Linearly interpolate between two quaternions. Linear
interpolation of rotations are only useful for small
rotations. For interpolations of arbitrary rotations,
vmath.slerp yields much better results.
 The function does not clamp t between 0 and 1.

**Parameters**

- `t` (number) - interpolation parameter, 0-1
- `q1` (quaternion) - quaternion to lerp from
- `q2` (quaternion) - quaternion to lerp to

**Returns**

- `q` (quaternion) - the lerped quaternion

**Examples**

```
function init(self)
    self.t = 0
end

function update(self, dt)
    self.t = self.t + dt
    if self.t <= 1 then
        local startrot = vmath.quat_rotation_z(0)
        local endrot = vmath.quat_rotation_z(3.141592653)
        local rot = vmath.lerp(self.t, startrot, endrot)
        go.set_rotation(rot, "go")
    end
end

```

### vmath.lerp
*Type:* FUNCTION
Linearly interpolate between two values. Lerp is useful
to describe transitions from one value to another over time.
 The function does not clamp t between 0 and 1.

**Parameters**

- `t` (number) - interpolation parameter, 0-1
- `n1` (number) - number to lerp from
- `n2` (number) - number to lerp to

**Returns**

- `n` (number) - the lerped number

**Examples**

```
function init(self)
    self.t = 0
end

function update(self, dt)
    self.t = self.t + dt
    if self.t <= 1 then
        local startx = 0
        local endx = 600
        local x = vmath.lerp(self.t, startx, endx)
        go.set_position(vmath.vector3(x, 100, 0), "go")
    end
end

```

### vmath.matrix4
*Type:* FUNCTION
The resulting identity matrix describes a transform with
no translation or rotation.

**Returns**

- `m` (matrix4) - identity matrix

**Examples**

```
local mat = vmath.matrix4()
print(mat) --> vmath.matrix4(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
-- get column 0:
print(mat.c0) --> vmath.vector4(1, 0, 0, 0)
-- get the value in row 3 and column 2:
print(mat.m32) --> 0

```

### vmath.matrix4
*Type:* FUNCTION
Creates a new matrix with all components set to the
corresponding values from the supplied matrix. I.e.
the function creates a copy of the given matrix.

**Parameters**

- `m1` (matrix4) - existing matrix

**Returns**

- `m` (matrix4) - matrix which is a copy of the specified matrix

**Examples**

```
local mat1 = vmath.matrix4_rotation_x(3.141592653)
local mat2 = vmath.matrix4(mat1)
if mat1 == mat2 then
    -- yes, they are equal
    print(mat2) --> vmath.matrix4(1, 0, 0, 0, 0, -1, 8.7422776573476e-08, 0, 0, -8.7422776573476e-08, -1, 0, 0, 0, 0, 1)
end

```

### vmath.matrix4_axis_angle
*Type:* FUNCTION
The resulting matrix describes a rotation around the axis by the specified angle.

**Parameters**

- `v` (vector3) - axis
- `angle` (number) - angle in radians

**Returns**

- `m` (matrix4) - matrix represented by axis and angle

**Examples**

```
local vec = vmath.vector4(1, 1, 0, 0)
local axis = vmath.vector3(0, 0, 1) -- z-axis
local mat = vmath.matrix4_axis_angle(axis, 3.141592653)
print(mat * vec) --> vmath.vector4(-0.99999994039536, -1.0000001192093, 0, 0)

```

### vmath.matrix4_compose
*Type:* FUNCTION
Creates a new matrix constructed from separate
translation vector, roation quaternion and scale vector

**Parameters**

- `translation` (vector3 | vector4) - translation
- `rotation` (quaternion) - rotation
- `scale` (vector3) - scale

**Returns**

- `matrix` (matrix4) - new matrix4

**Examples**

```
local translation = vmath.vector3(103, -95, 14)
local quat = vmath.quat(1, 2, 3, 4)
local scale = vmath.vector3(1, 0.5, 0.5)
local result = vmath.matrix4_compose(translation, quat, scale)
print(result) --> vmath.matrix4(-25, -10, 11, 103, 28, -9.5, 2, -95, -10, 10, -4.5, 14, 0, 0, 0, 1)

```

### vmath.matrix4_frustum
*Type:* FUNCTION
Constructs a frustum matrix from the given values. The left, right,
top and bottom coordinates of the view cone are expressed as distances
from the center of the near clipping plane. The near and far coordinates
are expressed as distances from the tip of the view frustum cone.

**Parameters**

- `left` (number) - coordinate for left clipping plane
- `right` (number) - coordinate for right clipping plane
- `bottom` (number) - coordinate for bottom clipping plane
- `top` (number) - coordinate for top clipping plane
- `near` (number) - coordinate for near clipping plane
- `far` (number) - coordinate for far clipping plane

**Returns**

- `m` (matrix4) - matrix representing the frustum

**Examples**

```
-- Construct a projection frustum with a vertical and horizontal
-- FOV of 45 degrees. Useful for rendering a square view.
local proj = vmath.matrix4_frustum(-1, 1, -1, 1, 1, 1000)
render.set_projection(proj)

```

### vmath.matrix4_look_at
*Type:* FUNCTION
The resulting matrix is created from the supplied look-at parameters.
This is useful for constructing a view matrix for a camera or
rendering in general.

**Parameters**

- `eye` (vector3) - eye position
- `look_at` (vector3) - look-at position
- `up` (vector3) - up vector

**Returns**

- `m` (matrix4) - look-at matrix

**Examples**

```
-- Set up a perspective camera at z 100 with 45 degrees (pi/2) FOV
-- Aspect ratio 4:3
local eye = vmath.vector3(0, 0, 100)
local look_at = vmath.vector3(0, 0, 0)
local up = vmath.vector3(0, 1, 0)
local view = vmath.matrix4_look_at(eye, look_at, up)
render.set_view(view)
local proj = vmath.matrix4_perspective(3.141592/2, 4/3, 1, 1000)
render.set_projection(proj)

```

### vmath.matrix4_orthographic
*Type:* FUNCTION
Creates an orthographic projection matrix.
This is useful to construct a projection matrix for a camera or rendering in general.

**Parameters**

- `left` (number) - coordinate for left clipping plane
- `right` (number) - coordinate for right clipping plane
- `bottom` (number) - coordinate for bottom clipping plane
- `top` (number) - coordinate for top clipping plane
- `near` (number) - coordinate for near clipping plane
- `far` (number) - coordinate for far clipping plane

**Returns**

- `m` (matrix4) - orthographic projection matrix

**Examples**

```
-- Set up an orthographic projection based on the width and height
-- of the game window.
local w = render.get_width()
local h = render.get_height()
local proj = vmath.matrix4_orthographic(- w / 2, w / 2, -h / 2, h / 2, -1000, 1000)
render.set_projection(proj)

```

### vmath.matrix4_perspective
*Type:* FUNCTION
Creates a perspective projection matrix.
This is useful to construct a projection matrix for a camera or rendering in general.

**Parameters**

- `fov` (number) - angle of the full vertical field of view in radians
- `aspect` (number) - aspect ratio
- `near` (number) - coordinate for near clipping plane
- `far` (number) - coordinate for far clipping plane

**Returns**

- `m` (matrix4) - perspective projection matrix

**Examples**

```
-- Set up a perspective camera at z 100 with 45 degrees (pi/2) FOV
-- Aspect ratio 4:3
local eye = vmath.vector3(0, 0, 100)
local look_at = vmath.vector3(0, 0, 0)
local up = vmath.vector3(0, 1, 0)
local view = vmath.matrix4_look_at(eye, look_at, up)
render.set_view(view)
local proj = vmath.matrix4_perspective(3.141592/2, 4/3, 1, 1000)
render.set_projection(proj)

```

### vmath.matrix4_quat
*Type:* FUNCTION
The resulting matrix describes the same rotation as the quaternion, but does not have any translation (also like the quaternion).

**Parameters**

- `q` (quaternion) - quaternion to create matrix from

**Returns**

- `m` (matrix4) - matrix represented by quaternion

**Examples**

```
local vec = vmath.vector4(1, 1, 0, 0)
local quat = vmath.quat_rotation_z(3.141592653)
local mat = vmath.matrix4_quat(quat)
print(mat * vec) --> vmath.matrix4_frustum(-1, 1, -1, 1, 1, 1000)

```

### vmath.matrix4_rotation_x
*Type:* FUNCTION
The resulting matrix describes a rotation around the x-axis
by the specified angle.

**Parameters**

- `angle` (number) - angle in radians around x-axis

**Returns**

- `m` (matrix4) - matrix from rotation around x-axis

**Examples**

```
local vec = vmath.vector4(1, 1, 0, 0)
local mat = vmath.matrix4_rotation_x(3.141592653)
print(mat * vec) --> vmath.vector4(1, -1, -8.7422776573476e-08, 0)

```

### vmath.matrix4_rotation_y
*Type:* FUNCTION
The resulting matrix describes a rotation around the y-axis
by the specified angle.

**Parameters**

- `angle` (number) - angle in radians around y-axis

**Returns**

- `m` (matrix4) - matrix from rotation around y-axis

**Examples**

```
local vec = vmath.vector4(1, 1, 0, 0)
local mat = vmath.matrix4_rotation_y(3.141592653)
print(mat * vec) --> vmath.vector4(-1, 1, 8.7422776573476e-08, 0)

```

### vmath.matrix4_rotation_z
*Type:* FUNCTION
The resulting matrix describes a rotation around the z-axis
by the specified angle.

**Parameters**

- `angle` (number) - angle in radians around z-axis

**Returns**

- `m` (matrix4) - matrix from rotation around z-axis

**Examples**

```
local vec = vmath.vector4(1, 1, 0, 0)
local mat = vmath.matrix4_rotation_z(3.141592653)
print(mat * vec) --> vmath.vector4(-0.99999994039536, -1.0000001192093, 0, 0)

```

### vmath.matrix4_scale
*Type:* FUNCTION
Creates a new matrix constructed from scale vector

**Parameters**

- `scale` (vector3) - scale

**Returns**

- `matrix` (matrix4) - new matrix4

**Examples**

```
local scale = vmath.vector3(1, 0.5, 0.5)
local result = vmath.matrix4_scale(scale)
print(result) --> vmath.matrix4(1, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 1)

```

### vmath.matrix4_scale
*Type:* FUNCTION
creates a new matrix4 from uniform scale

**Parameters**

- `scale` (number) - scale

**Returns**

- `matrix` (matrix4) - new matrix4

**Examples**

```
local result = vmath.matrix4_scale(0.5)
print(result) --> vmath.matrix4(0.5, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 1)

```

### vmath.matrix4_scale
*Type:* FUNCTION
Creates a new matrix4 from three scale components

**Parameters**

- `scale_x` (number) - scale along X axis
- `scale_y` (number) - sclae along Y axis
- `scale_z` (number) - scale along Z asis

**Returns**

- `matrix` (matrix4) - new matrix4

**Examples**

```
local result = vmath.matrix4_scale(1, 0.5, 0.5)
print(result) --> vmath.matrix4(1, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 1)

```

### vmath.matrix4_translation
*Type:* FUNCTION
The resulting matrix describes a translation of a point
in euclidean space.

**Parameters**

- `position` (vector3 | vector4) - position vector to create matrix from

**Returns**

- `m` (matrix4) - matrix from the supplied position vector

**Examples**

```
-- Set camera view from custom view and translation matrices
local mat_trans = vmath.matrix4_translation(vmath.vector3(0, 10, 100))
local mat_view  = vmath.matrix4_rotation_y(-3.141592/4)
render.set_view(mat_view * mat_trans)

```

### vmath.mul_per_elem
*Type:* FUNCTION
Performs an element wise multiplication between two vectors of the same type
The returned value is a vector defined as (e.g. for a vector3):
v = vmath.mul_per_elem(a, b) = vmath.vector3(a.x * b.x, a.y * b.y, a.z * b.z)

**Parameters**

- `v1` (vector3 | vector4) - first vector
- `v2` (vector3 | vector4) - second vector

**Returns**

- `v` (vector3 | vector4) - multiplied vector

**Examples**

```
local blend_color = vmath.mul_per_elem(color1, color2)

```

### vmath.normalize
*Type:* FUNCTION
Normalizes a vector, i.e. returns a new vector with the same
direction as the input vector, but with length 1.
 The length of the vector must be above 0, otherwise a
division-by-zero will occur.

**Parameters**

- `v1` (vector3 | vector4 | quaternion) - vector to normalize

**Returns**

- `v` (vector3 | vector4 | quaternion) - new normalized vector

**Examples**

```
local vec = vmath.vector3(1, 2, 3)
local norm_vec = vmath.normalize(vec)
print(norm_vec) --> vmath.vector3(0.26726123690605, 0.5345224738121, 0.80178368091583)
print(vmath.length(norm_vec)) --> 0.99999994039536

```

### vmath.ortho_inv
*Type:* FUNCTION
The resulting matrix is the inverse of the supplied matrix.
The supplied matrix has to be an ortho-normal matrix, e.g.
describe a regular object transformation.
 For matrices that are not ortho-normal
use the general inverse vmath.inv() instead.

**Parameters**

- `m1` (matrix4) - ortho-normalized matrix to invert

**Returns**

- `m` (matrix4) - inverse of the supplied matrix

**Examples**

```
local mat1 = vmath.matrix4_rotation_z(3.141592653)
local mat2 = vmath.ortho_inv(mat1)
-- M * inv(M) = identity matrix
print(mat1 * mat2) --> vmath.matrix4(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)

```

### vmath.project
*Type:* FUNCTION
Calculates the extent the projection of the first vector onto the second.
The returned value is a scalar p defined as:
p = |P| cos θ / |Q|
where θ is the angle between the vectors P and Q.

**Parameters**

- `v1` (vector3) - vector to be projected on the second
- `v2` (vector3) - vector onto which the first will be projected, must not have zero length

**Returns**

- `n` (number) - the projected extent of the first vector onto the second

**Examples**

```
local v1 = vmath.vector3(1, 1, 0)
local v2 = vmath.vector3(2, 0, 0)
print(vmath.project(v1, v2)) --> 0.5

```

### vmath.quat
*Type:* FUNCTION
Creates a new identity quaternion. The identity
quaternion is equal to:
vmath.quat(0, 0, 0, 1)

**Returns**

- `q` (quaternion) - new identity quaternion

**Examples**

```
local quat = vmath.quat()
print(quat) --> vmath.quat(0, 0, 0, 1)
print(quat.w) --> 1

```

### vmath.quat
*Type:* FUNCTION
Creates a new quaternion with all components set to the
corresponding values from the supplied quaternion. I.e.
This function creates a copy of the given quaternion.

**Parameters**

- `q1` (quaternion) - existing quaternion

**Returns**

- `q` (quaternion) - new quaternion

**Examples**

```
local quat1 = vmath.quat(1, 2, 3, 4)
local quat2 = vmath.quat(quat1)
if quat1 == quat2 then
    -- yes, they are equal
    print(quat2) --> vmath.quat(1, 2, 3, 4)
end

```

### vmath.quat
*Type:* FUNCTION
Creates a new quaternion with the components set
according to the supplied parameter values.

**Parameters**

- `x` (number) - x coordinate
- `y` (number) - y coordinate
- `z` (number) - z coordinate
- `w` (number) - w coordinate

**Returns**

- `q` (quaternion) - new quaternion

**Examples**

```
local quat = vmath.quat(1, 2, 3, 4)
print(quat) --> vmath.quat(1, 2, 3, 4)

```

### vmath.quat_axis_angle
*Type:* FUNCTION
The resulting quaternion describes a rotation of angle
radians around the axis described by the unit vector v.

**Parameters**

- `v` (vector3) - axis
- `angle` (number) - angle

**Returns**

- `q` (quaternion) - quaternion representing the axis-angle rotation

**Examples**

```
local axis = vmath.vector3(1, 0, 0)
local rot = vmath.quat_axis_angle(axis, 3.141592653)
local vec = vmath.vector3(1, 1, 0)
print(vmath.rotate(rot, vec)) --> vmath.vector3(1, -1, -8.7422776573476e-08)

```

### vmath.quat_basis
*Type:* FUNCTION
The resulting quaternion describes the rotation from the
identity quaternion (no rotation) to the coordinate system
as described by the given x, y and z base unit vectors.

**Parameters**

- `x` (vector3) - x base vector
- `y` (vector3) - y base vector
- `z` (vector3) - z base vector

**Returns**

- `q` (quaternion) - quaternion representing the rotation of the specified base vectors

**Examples**

```
-- Axis rotated 90 degrees around z.
local rot_x = vmath.vector3(0, -1, 0)
local rot_y = vmath.vector3(1, 0, 0)
local z = vmath.vector3(0, 0, 1)
local rot1 = vmath.quat_basis(rot_x, rot_y, z)
local rot2 = vmath.quat_from_to(vmath.vector3(0, 1, 0), vmath.vector3(1, 0, 0))
if rot1 == rot2 then
    -- These quaternions are equal!
    print(rot2) --> vmath.quat(0, 0, -0.70710676908493, 0.70710676908493)
end

```

### vmath.quat_from_to
*Type:* FUNCTION
The resulting quaternion describes the rotation that,
if applied to the first vector, would rotate the first
vector to the second. The two vectors must be unit
vectors (of length 1).
 The result is undefined if the two vectors point in opposite directions

**Parameters**

- `v1` (vector3) - first unit vector, before rotation
- `v2` (vector3) - second unit vector, after rotation

**Returns**

- `q` (quaternion) - quaternion representing the rotation from first to second vector

**Examples**

```
local v1 = vmath.vector3(1, 0, 0)
local v2 = vmath.vector3(0, 1, 0)
local rot = vmath.quat_from_to(v1, v2)
print(vmath.rotate(rot, v1)) --> vmath.vector3(0, 0.99999994039536, 0)

```

### vmath.quat_matrix4
*Type:* FUNCTION
Creates a new quaternion with the components set
according to the supplied parameter values.

**Parameters**

- `matrix` (matrix4) - source matrix4

**Returns**

- `q` (quaternion) - new quaternion

### vmath.quat_rotation_x
*Type:* FUNCTION
The resulting quaternion describes a rotation of angle
radians around the x-axis.

**Parameters**

- `angle` (number) - angle in radians around x-axis

**Returns**

- `q` (quaternion) - quaternion representing the rotation around the x-axis

**Examples**

```
local rot = vmath.quat_rotation_x(3.141592653)
local vec = vmath.vector3(1, 1, 0)
print(vmath.rotate(rot, vec)) --> vmath.vector3(1, -1, -8.7422776573476e-08)

```

### vmath.quat_rotation_y
*Type:* FUNCTION
The resulting quaternion describes a rotation of angle
radians around the y-axis.

**Parameters**

- `angle` (number) - angle in radians around y-axis

**Returns**

- `q` (quaternion) - quaternion representing the rotation around the y-axis

**Examples**

```
local rot = vmath.quat_rotation_y(3.141592653)
local vec = vmath.vector3(1, 1, 0)
print(vmath.rotate(rot, vec)) --> vmath.vector3(-1, 1, 8.7422776573476e-08)

```

### vmath.quat_rotation_z
*Type:* FUNCTION
The resulting quaternion describes a rotation of angle
radians around the z-axis.

**Parameters**

- `angle` (number) - angle in radians around z-axis

**Returns**

- `q` (quaternion) - quaternion representing the rotation around the z-axis

**Examples**

```
local rot = vmath.quat_rotation_z(3.141592653)
local vec = vmath.vector3(1, 1, 0)
print(vmath.rotate(rot, vec)) --> vmath.vector3(-0.99999988079071, -1, 0)

```

### vmath.quat_to_euler
*Type:* FUNCTION
Converts a quaternion into euler angles (r0, r1, r2), based on YZX rotation order.
To handle gimbal lock (singularity at r1 ~ +/- 90 degrees), the cut off is at r0 = +/- 88.85 degrees, which snaps to +/- 90.
The provided quaternion is expected to be normalized.
The error is guaranteed to be less than +/- 0.02 degrees

**Parameters**

- `q` (quaternion) - source quaternion

**Returns**

- `x` (number) - euler angle x in degrees
- `y` (number) - euler angle y in degrees
- `z` (number) - euler angle z in degrees

**Examples**

```
local q = vmath.quat_rotation_z(math.rad(90))
print(vmath.quat_to_euler(q)) --> 0 0 90

local q2 = vmath.quat_rotation_y(math.rad(45)) * vmath.quat_rotation_z(math.rad(90))
local v = vmath.vector3(vmath.quat_to_euler(q2))
print(v) --> vmath.vector3(0, 45, 90)

```

### vmath.rotate
*Type:* FUNCTION
Returns a new vector from the supplied vector that is
rotated by the rotation described by the supplied
quaternion.

**Parameters**

- `q` (quaternion) - quaternion
- `v1` (vector3) - vector to rotate

**Returns**

- `v` (vector3) - the rotated vector

**Examples**

```
local vec = vmath.vector3(1, 1, 0)
local rot = vmath.quat_rotation_z(3.141592563)
print(vmath.rotate(rot, vec)) --> vmath.vector3(-1.0000002384186, -0.99999988079071, 0)

```

### vmath.slerp
*Type:* FUNCTION
Spherically interpolates between two vectors. The difference to
lerp is that slerp treats the vectors as directions instead of
positions in space.
The direction of the returned vector is interpolated by the angle
and the magnitude is interpolated between the magnitudes of the
from and to vectors.
 Slerp is computationally more expensive than lerp.
The function does not clamp t between 0 and 1.

**Parameters**

- `t` (number) - interpolation parameter, 0-1
- `v1` (vector3 | vector4) - vector to slerp from
- `v2` (vector3 | vector4) - vector to slerp to

**Returns**

- `v` (vector3 | vector4) - the slerped vector

**Examples**

```
function init(self)
    self.t = 0
end

function update(self, dt)
    self.t = self.t + dt
    if self.t <= 1 then
        local startpos = vmath.vector3(0, 600, 0)
        local endpos = vmath.vector3(600, 0, 0)
        local pos = vmath.slerp(self.t, startpos, endpos)
        go.set_position(pos, "go")
    end
end

```

### vmath.slerp
*Type:* FUNCTION
Slerp travels the torque-minimal path maintaining constant
velocity, which means it travels along the straightest path along
the rounded surface of a sphere. Slerp is useful for interpolation
of rotations.
Slerp travels the torque-minimal path, which means it travels
along the straightest path the rounded surface of a sphere.
 The function does not clamp t between 0 and 1.

**Parameters**

- `t` (number) - interpolation parameter, 0-1
- `q1` (quaternion) - quaternion to slerp from
- `q2` (quaternion) - quaternion to slerp to

**Returns**

- `q` (quaternion) - the slerped quaternion

**Examples**

```
function init(self)
    self.t = 0
end

function update(self, dt)
    self.t = self.t + dt
    if self.t <= 1 then
        local startrot = vmath.quat_rotation_z(0)
        local endrot = vmath.quat_rotation_z(3.141592653)
        local rot = vmath.slerp(self.t, startrot, endrot)
        go.set_rotation(rot, "go")
    end
end

```

### vmath.vector
*Type:* FUNCTION
Creates a vector of arbitrary size. The vector is initialized
with numeric values from a table.
 The table values are converted to floating point
values. If a value cannot be converted, a 0 is stored in that
value position in the vector.

**Parameters**

- `t` (table) - table of numbers

**Returns**

- `v` (vector) - new vector

**Examples**

How to create a vector with custom data to be used for animation easing:
```
local values = { 0, 0.5, 0 }
local vec = vmath.vector(values)
print(vec) --> vmath.vector (size: 3)
print(vec[2]) --> 0.5

```

### vmath.vector3
*Type:* FUNCTION
Creates a new zero vector with all components set to 0.

**Returns**

- `v` (vector3) - new zero vector

**Examples**

```
local vec = vmath.vector3()
pprint(vec) --> vmath.vector3(0, 0, 0)
print(vec.x) --> 0

```

### vmath.vector3
*Type:* FUNCTION
Creates a new vector with all components set to the
supplied scalar value.

**Parameters**

- `n` (number) - scalar value to splat

**Returns**

- `v` (vector3) - new vector

**Examples**

```
local vec = vmath.vector3(1.0)
print(vec) --> vmath.vector3(1, 1, 1)
print(vec.x) --> 1

```

### vmath.vector3
*Type:* FUNCTION
Creates a new vector with all components set to the
corresponding values from the supplied vector. I.e.
This function creates a copy of the given vector.

**Parameters**

- `v1` (vector3) - existing vector

**Returns**

- `v` (vector3) - new vector

**Examples**

```
local vec1 = vmath.vector3(1.0)
local vec2 = vmath.vector3(vec1)
if vec1 == vec2 then
    -- yes, they are equal
    print(vec2) --> vmath.vector3(1, 1, 1)
end

```

### vmath.vector3
*Type:* FUNCTION
Creates a new vector with the components set to the
supplied values.

**Parameters**

- `x` (number) - x coordinate
- `y` (number) - y coordinate
- `z` (number) - z coordinate

**Returns**

- `v` (vector3) - new vector

**Examples**

```
local vec = vmath.vector3(1.0, 2.0, 3.0)
print(vec) --> vmath.vector3(1, 2, 3)
print(-vec) --> vmath.vector3(-1, -2, -3)
print(vec * 2) --> vmath.vector3(2, 4, 6)
print(vec + vmath.vector3(2.0)) --> vmath.vector3(3, 4, 5)
print(vec - vmath.vector3(2.0)) --> vmath.vector3(-1, 0, 1)

```

### vmath.vector4
*Type:* FUNCTION
Creates a new zero vector with all components set to 0.

**Returns**

- `v` (vector4) - new zero vector

**Examples**

```
local vec = vmath.vector4()
print(vec) --> vmath.vector4(0, 0, 0, 0)
print(vec.w) --> 0

```

### vmath.vector4
*Type:* FUNCTION
Creates a new vector with all components set to the
supplied scalar value.

**Parameters**

- `n` (number) - scalar value to splat

**Returns**

- `v` (vector4) - new vector

**Examples**

```
local vec = vmath.vector4(1.0)
print(vec) --> vmath.vector4(1, 1, 1, 1)
print(vec.w) --> 1

```

### vmath.vector4
*Type:* FUNCTION
Creates a new vector with all components set to the
corresponding values from the supplied vector. I.e.
This function creates a copy of the given vector.

**Parameters**

- `v1` (vector4) - existing vector

**Returns**

- `v` (vector4) - new vector

**Examples**

```
local vect1 = vmath.vector4(1.0)
local vect2 = vmath.vector4(vec1)
if vec1 == vec2 then
    -- yes, they are equal
    print(vec2) --> vmath.vector4(1, 1, 1, 1)
end

```

### vmath.vector4
*Type:* FUNCTION
Creates a new vector with the components set to the
supplied values.

**Parameters**

- `x` (number) - x coordinate
- `y` (number) - y coordinate
- `z` (number) - z coordinate
- `w` (number) - w coordinate

**Returns**

- `v` (vector4) - new vector

**Examples**

```
local vec = vmath.vector4(1.0, 2.0, 3.0, 4.0)
print(vec) --> vmath.vector4(1, 2, 3, 4)
print(-vec) --> vmath.vector4(-1, -2, -3, -4)
print(vec * 2) --> vmath.vector4(2, 4, 6, 8)
print(vec + vmath.vector4(2.0)) --> vmath.vector4(3, 4, 5, 6)
print(vec - vmath.vector4(2.0)) --> vmath.vector4(-1, 0, 1, 2)

```
