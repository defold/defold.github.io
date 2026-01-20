# extension-camera

**Namespace:** `camera`
**Language:** Lua
**Type:** Extension

Provides functionality to capture images using the camera. Supported on macOS, iOS and Android. [icon:ios] [icon:android]

## API

### camera.start_capture
*Type:* FUNCTION
Start camera capture using the specified camera (front/back) and capture quality. This may trigger a camera usage permission popup. When the popup has been dismissed the callback will be invoked with camera start status.

**Examples**

```
camera.start_capture(camera.CAMERA_TYPE_BACK, camera.CAPTURE_QUALITY_HIGH, function(self, message)
    if message == camera.CAMERA_STARTED then
        -- do stuff
    end
end)

```

### camera.stop_capture
*Type:* FUNCTION
Stops a previously started capture session.

**Examples**

```
camera.stop_capture()

```

### camera.get_info
*Type:* FUNCTION
Gets the info from the current capture session.

**Examples**

```
local info = camera.get_info()
print("width", info.width)
print("height", info.height)

```

### camera.get_frame
*Type:* FUNCTION
Get captured frame.

**Examples**

```
self.cameraframe = camera.get_frame()

```

### CAMERA_TYPE_FRONT
*Type:* STRING
Constant for the front camera.

### CAMERA_TYPE_BACK
*Type:* STRING
Constant for the back camera.

### CAPTURE_QUALITY_HIGH
*Type:* STRING
High quality capture session.

### CAPTURE_QUALITY_MEDIUM
*Type:* STRING
Medium quality capture session.

### CAPTURE_QUALITY_LOW
*Type:* STRING
Low quality capture session.

### CAMERA_STARTED
*Type:* STRING
The capture session has started.

### CAMERA_STOPPED
*Type:* STRING
The capture session has stopped.

### CAMERA_NOT_PERMITTED
*Type:* STRING
The user did not give permission to start the capture session.

### CAMERA_ERROR
*Type:* STRING
Something went wrong when starting the capture session.
