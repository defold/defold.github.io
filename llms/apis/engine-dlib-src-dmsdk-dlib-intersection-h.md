# Intersection structs and functions

**Namespace:** `dmIntersection`
**Language:** C++
**Type:** Defold C++
**File:** `intersection.h`
**Source:** `engine/dlib/src/dmsdk/dlib/intersection.h`
**Include:** `dmsdk/dlib/intersection.h`

Intersection math structs and functions

## API

### CreateFrustumFromMatrix
*Type:* FUNCTION
Constructs a dmIntersection::Frustum from a View*Projection matrix

**Parameters**

- `m` (dmVMath::Matrix4&) - The matrix. Usually a "ViewProj" matrix
- `normalize` (bool) - true if the normals should be normalized

**Returns**

- `frustum` (dmIntersection::Frustum&) - the frustum output

### DistanceToPlane
*Type:* FUNCTION
Returns the closest distance between a plane and a position

**Parameters**

- `plane` (dmIntersection::Plane) - plane equation
- `pos` (dmVMath::Point3) - position

**Returns**

- `distance` (float) - closest distance between plane and position

### Frustum
*Type:* STRUCT
Frustum

**Notes**

- The plane normals point inwards

**Members**

- `m_Planes` (dmIntersection::Plane[6) - ] plane equations: // left, right, bottom, top, near, far

### Plane
*Type:* TYPEDEF
Plane struct (currently an alias for dmVMath::Vector4)

### TestFrustumOBB
*Type:* FUNCTION
Tests intersection between a frustum and an oriented bounding box (OBB)

**Parameters**

- `frustum` (dmIntersection::Frustum&) - the frustum
- `world` (dmVMath::Matrix4&) - The world transform of the OBB
- `aabb_min` (dmVMath::Vector3&) - the minimum corner of the object. In local space.
- `aabb_max` (dmVMath::Vector3&) - the maximum corner of the object. In local space.
- `skip_near_far` (bool) - if true, the near+far planes of the frustum are ignored

**Returns**

- `intersects` (bool) - Returns true if the objects intersect

### TestFrustumPoint
*Type:* FUNCTION
Tests intersection between a frustum and a point

**Parameters**

- `frustum` (dmIntersection::Frustum&) - the frustum
- `pos` (dmVMath::Point3&) - the position
- `skip_near_far` (bool) - if true, the near+far planes of the frustum are ignored

**Returns**

- `intersects` (bool) - Returns true if the objects intersect

### TestFrustumSphere
*Type:* FUNCTION
Tests intersection between a frustum and a sphere

**Parameters**

- `frustum` (dmIntersection::Frustum&) - the frustum
- `pos` (dmVMath::Point3&) - the center position of the sphere
- `radius` (float) - the radius of the sphere
- `skip_near_far` (bool) - if true, the near+far planes of the frustum are ignored

**Returns**

- `intersects` (bool) - Returns true if the objects intersect

### TestFrustumSphere
*Type:* FUNCTION
Tests intersection between a frustum and a sphere

**Parameters**

- `frustum` (dmIntersection::Frustum&) - the frustum
- `pos` (dmVMath::Vector4&) - the center position of the sphere. The w component must be 1.
- `radius` (float) - the radius of the sphere
- `skip_near_far` (bool) - if true, the near+far planes of the frustum are ignored

**Returns**

- `intersects` (bool) - Returns true if the objects intersect

### TestFrustumSphereSq
*Type:* FUNCTION
Tests intersection between a frustum and a sphere

**Parameters**

- `frustum` (dmIntersection::Frustum&) - the frustum
- `pos` (dmVMath::Point3&) - the center position of the sphere
- `radius_sq` (float) - the squared radius of the sphere
- `skip_near_far` (bool) - if true, the near+far planes of the frustum are ignored

**Returns**

- `intersects` (bool) - Returns true if the objects intersect

### TestFrustumSphereSq
*Type:* FUNCTION
Tests intersection between a frustum and a sphere

**Parameters**

- `frustum` (dmIntersection::Frustum&) - the frustum
- `pos` (dmVMath::Vector4&) - the center position of the sphere. The w component must be 1.
- `radius_sq` (float) - the squared radius of the sphere
- `skip_near_far` (bool) - if true, the near+far planes of the frustum are ignored

**Returns**

- `intersects` (bool) - Returns true if the objects intersect
