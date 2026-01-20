# Camera

**Namespace:** `camera`
**Language:** Lua
**Type:** Defold Lua
**File:** `camera_ddf.proto`
**Source:** `engine/gamesys/proto/gamesys/camera_ddf.proto`

Messages to control camera components and camera focus.

## API

### aspect_ratio
*Type:* PROPERTY
The ratio between the frustum width and height. Used when calculating the
projection of a perspective camera.
The type of the property is number.

**Examples**

```
function init(self)
  local aspect_ratio = go.get("#camera", "aspect_ratio")
  go.set("#camera", "aspect_ratio", 1.2)
end

```

### camera.get_aspect_ratio
*Type:* FUNCTION
Gets the effective aspect ratio of the camera. If auto aspect ratio is enabled,
returns the aspect ratio calculated from the current render target dimensions.
Otherwise returns the manually set aspect ratio.

**Parameters**

- `camera` (url | number | nil) - camera id

**Returns**

- `aspect_ratio` (number) - the effective aspect ratio.

### camera.get_auto_aspect_ratio
*Type:* FUNCTION
Returns whether auto aspect ratio is enabled. When enabled, the camera automatically
calculates aspect ratio from render target dimensions. When disabled, uses the
manually set aspect ratio value.

**Parameters**

- `camera` (url | number | nil) - camera id

**Returns**

- `auto_aspect_ratio` (boolean) - true if auto aspect ratio is enabled

### camera.get_cameras
*Type:* FUNCTION
This function returns a table with all the camera URLs that have been
registered in the render context.

**Returns**

- `cameras` (table) - a table with all camera URLs

**Examples**

```
for k,v in pairs(camera.get_cameras()) do
    render.set_camera(v)
    render.draw(...)
    render.set_camera()
end

```

### camera.get_enabled
*Type:* FUNCTION
get enabled

**Parameters**

- `camera` (url | number | nil) - camera id

**Returns**

- `flag` (boolean) - true if the camera is enabled

### camera.get_far_z
*Type:* FUNCTION
get far z

**Parameters**

- `camera` (url | number | nil) - camera id

**Returns**

- `far_z` (number) - the far z.

### camera.get_fov
*Type:* FUNCTION
get field of view

**Parameters**

- `camera` (url | number | nil) - camera id

**Returns**

- `fov` (number) - the field of view.

### camera.get_near_z
*Type:* FUNCTION
get near z

**Parameters**

- `camera` (url | number | nil) - camera id

**Returns**

- `near_z` (number) - the near z.

### camera.get_orthographic_mode
*Type:* FUNCTION
get orthographic zoom mode

**Parameters**

- `camera` (url | number | nil) - camera id

**Returns**

- `mode` (number) - one of camera.ORTHO_MODE_FIXED, camera.ORTHO_MODE_AUTO_FIT or
camera.ORTHO_MODE_AUTO_COVER

### camera.get_orthographic_zoom
*Type:* FUNCTION
get orthographic zoom

**Parameters**

- `camera` (url | number | nil) - camera id

**Returns**

- `orthographic_zoom` (number) - the zoom level when the camera uses orthographic projection.

### camera.get_projection
*Type:* FUNCTION
get projection matrix

**Parameters**

- `camera` (url | number | nil) - camera id

**Returns**

- `projection` (matrix4) - the projection matrix.

### camera.get_view
*Type:* FUNCTION
get view matrix

**Parameters**

- `camera` (url | number | nil) - camera id

**Returns**

- `view` (matrix4) - the view matrix.

### camera.ORTHO_MODE_AUTO_COVER
*Type:* CONSTANT
Computes zoom so the original display area covers the entire window while preserving aspect ratio.
Equivalent to using max(window_width/width, window_height/height).

### camera.ORTHO_MODE_AUTO_FIT
*Type:* CONSTANT
Computes zoom so the original display area (game.project width/height) fits inside the window
while preserving aspect ratio. Equivalent to using min(window_width/width, window_height/height).

### camera.ORTHO_MODE_FIXED
*Type:* CONSTANT
Uses the manually set orthographic zoom value (camera.set_orthographic_zoom).

### camera.screen_to_world
*Type:* FUNCTION
Converts a screen-space 2D point with view depth to a 3D world point.
z is the view depth in world units measured from the camera plane along the camera forward axis.
If a camera isn't specified, the last enabled camera is used.

**Parameters**

- `pos` (vector3) - Screen-space position (x, y) with z as view depth in world units
- `camera` (url | number | nil) (optional) - optional camera id

**Returns**

- `world_pos` (vector3) - the world coordinate

**Examples**

Place objects at the touch point with a random Z position, keeping them within the visible view zone.
```
 function on_input(self, action_id, action)
     if action_id == hash("touch") then
         if action.pressed then
             local percpective_camera = msg.url("#perspective_camera")
             local random_z = math.random(camera.get_near_z(percpective_camera) + 0.01, camera.get_far_z(percpective_camera) - 0.01)
             local world_position = camera.screen_to_world(vmath.vector3(action.screen_x, action.screen_y, random_z), percpective_camera)
             go.set_position(world_position, "/go1")
         end
     end
 end

```

### camera.screen_xy_to_world
*Type:* FUNCTION
Converts 2D screen coordinates (x,y) to the 3D world-space point on the camera's near plane for that pixel.
If a camera isn't specified, the last enabled camera is used.

**Parameters**

- `x` (number) - X coordinate on screen.
- `y` (number) - Y coordinate on screen.
- `camera` (url | number | nil) (optional) - optional camera id

**Returns**

- `world_pos` (vector3) - the world coordinate on the camera near plane

**Examples**

Place objects at the touch point.
```
 function on_input(self, action_id, action)
     if action_id == hash("touch") then
         if action.pressed then
             local world_position = camera.screen_xy_to_world(action.screen_x, action.screen_y)
             go.set_position(world_position, "/go1")
         end
     end
 end

```

### camera.set_aspect_ratio
*Type:* FUNCTION
Sets the manual aspect ratio for the camera. This value is only used when
auto aspect ratio is disabled. To disable auto aspect ratio and use this
manual value, call camera.set_auto_aspect_ratio(camera, false).

**Parameters**

- `camera` (url | number | nil) - camera id
- `aspect_ratio` (number) - the manual aspect ratio value.

### camera.set_auto_aspect_ratio
*Type:* FUNCTION
Enables or disables automatic aspect ratio calculation. When enabled (true),
the camera automatically calculates aspect ratio from render target dimensions.
When disabled (false), uses the manually set aspect ratio value.

**Parameters**

- `camera` (url | number | nil) - camera id
- `auto_aspect_ratio` (boolean) - true to enable auto aspect ratio

### camera.set_far_z
*Type:* FUNCTION
set far z

**Parameters**

- `camera` (url | number | nil) - camera id
- `far_z` (number) - the far z.

### camera.set_fov
*Type:* FUNCTION
set field of view

**Parameters**

- `camera` (url | number | nil) - camera id
- `fov` (number) - the field of view.

### camera.set_near_z
*Type:* FUNCTION
set near z

**Parameters**

- `camera` (url | number | nil) - camera id
- `near_z` (number) - the near z.

### camera.set_orthographic_mode
*Type:* FUNCTION
set orthographic zoom mode

**Parameters**

- `camera` (url | number | nil) - camera id
- `mode` (number) - camera.ORTHO_MODE_FIXED, camera.ORTHO_MODE_AUTO_FIT or camera.ORTHO_MODE_AUTO_COVER

### camera.set_orthographic_zoom
*Type:* FUNCTION
set orthographic zoom

**Parameters**

- `camera` (url | number | nil) - camera id
- `orthographic_zoom` (number) - the zoom level when the camera uses orthographic projection.

### camera.world_to_screen
*Type:* FUNCTION
Converts a 3D world position to screen-space coordinates with view depth.
Returns a vector3 where x and y are in screen pixels and z is the view depth in world units
measured from the camera plane along the camera forward axis. The returned z can be used with
camera.screen_to_world to reconstruct the world position on the same pixel ray.
If a camera isn't specified, the last enabled camera is used.

**Parameters**

- `world_pos` (vector3) - World-space position
- `camera` (url | number | nil) (optional) - optional camera id

**Returns**

- `screen_pos` (vector3) - Screen position (x,y in pixels, z is view depth)

**Examples**

Convert go position into screen pisition
```
 go.update_world_transform("/go1")
 local world_pos = go.get_world_position("/go1")
 local screen_pos = camera.world_to_screen(world_pos)

```

### far_z
*Type:* PROPERTY
Camera frustum far plane.
The type of the property is float.

**Examples**

```
function init(self)
  local far_z = go.get("#camera", "far_z")
  go.set("#camera", "far_z", 10)
end

```

### fov
*Type:* PROPERTY
Vertical field of view of the camera.
The type of the property is float.

**Examples**

```
function init(self)
  local fov = go.get("#camera", "fov")
  go.set("#camera", "fov", fov + 0.1)
  go.animate("#camera", "fov", go.PLAYBACK_ONCE_PINGPONG, 1.2, go.EASING_LINEAR, 1)
end

```

### near_z
*Type:* PROPERTY
Camera frustum near plane.
The type of the property is float.

**Examples**

```
function init(self)
  local near_z = go.get("#camera", "near_z")
  go.set("#camera", "near_z", 10)
end

```

### orthographic_zoom
*Type:* PROPERTY
Zoom level when using an orthographic projection.
The type of the property is float.

**Examples**

```
function init(self)
  local orthographic_zoom = go.get("#camera", "orthographic_zoom")
  go.set("#camera", "orthographic_zoom", 2.0)
  go.animate("#camera", "orthographic_zoom", go.PLAYBACK_ONCE_PINGPONG, 0.5, go.EASING_INOUTQUAD, 2)
end

```

### projection
*Type:* PROPERTY
READ ONLY The calculated projection matrix of the camera.
The type of the property is matrix4.

**Examples**

```
function init(self)
  local projection = go.get("#camera", "projection")
end

```

### set_camera
*Type:* MESSAGE
Post this message to a camera-component to set its properties at run-time.

**Parameters**

- `aspect_ratio` (number) - aspect ratio of the screen (width divided by height)
- `fov` (number) - field of view of the lens, measured as the angle in radians between the right and left edge
- `near_z` (number) - position of the near clipping plane (distance from camera along relative z)
- `far_z` (number) - position of the far clipping plane (distance from camera along relative z)
- `orthographic_projection` (boolean) - set to use an orthographic projection
- `orthographic_zoom` (number) - zoom level when the camera is using an orthographic projection
- `orthographic_mode` (number) - orthographic zoom behavior when orthographic_projection is enabled

**Examples**

In the examples, it is assumed that the instance of the script has a camera-component with id "camera".
```
msg.post("#camera", "set_camera", {aspect_ratio = 16/9, fov = math.pi * 0.5, near_z = 0.1, far_z = 500})

```

### view
*Type:* PROPERTY
READ ONLY The calculated view matrix of the camera.
The type of the property is matrix4.

**Examples**

```
function init(self)
  local view = go.get("#camera", "view")
end

```
