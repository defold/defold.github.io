# Graphics

**Namespace:** `dmGraphics`
**Language:** C++
**Type:** Defold C++
**File:** `graphics_native.h`
**Source:** `engine/graphics/src/dmsdk/graphics/graphics_native.h`
**Include:** `dmsdk/graphics/graphics_native.h`

Platform specific native graphics functions.

## API

### dmGraphics::GetNativeAndroidActivity
*Type:* FUNCTION
Get Android native jobject. Any other platform return zero.

**Returns**

- `jobject` (jobject) - native handle

### dmGraphics::GetNativeAndroidApp
*Type:* FUNCTION
Get Android app object. Any other platform return zero.

**Returns**

- `app` (struct android_app*) - native handle

### dmGraphics::GetNativeAndroidEGLContext
*Type:* FUNCTION
Get Android EGLContext native handle (EGLContext). Any other platform return zero.

**Returns**

- `EGLContext` (EGLContext) - native handle

### dmGraphics::GetNativeAndroidEGLSurface
*Type:* FUNCTION
Get Android EGLSurface native handle (EGLSurface). Any other platform return zero.

**Returns**

- `EGLSurface` (EGLSurface) - native handle

### dmGraphics::GetNativeAndroidJavaVM
*Type:* FUNCTION
Get Android JavaVM ptr. Any other platform return zero.

**Returns**

- `JavaVM*` (JavaVM*) - native handle

### dmGraphics::GetNativeiOSEAGLContext
*Type:* FUNCTION
Get iOS EAGLContext native handle (id). Any other platform return zero.

**Returns**

- `id` (id) - native handle

### dmGraphics::GetNativeiOSUIView
*Type:* FUNCTION
Get iOS UIView native handle (id). Any other platform return zero.

**Returns**

- `id` (id) - native handle

### dmGraphics::GetNativeiOSUIWindow
*Type:* FUNCTION
Get iOS UIWindow native handle (id). Any other platform return zero.

**Returns**

- `id` (id) - native handle

### dmGraphics::GetNativeOSXNSOpenGLContext
*Type:* FUNCTION
Get OSX NSOpenGLContext native handle (id). Any other platform return zero.

**Returns**

- `id` (id) - native handle

### dmGraphics::GetNativeOSXNSView
*Type:* FUNCTION
Get OSX NSView native handle (id). Any other platform return zero.

**Returns**

- `id` (id) - native handle

### dmGraphics::GetNativeOSXNSWindow
*Type:* FUNCTION
Get OSX NSWindow native handle (id). Any other platform return zero.

**Returns**

- `id` (id) - native handle

### dmGraphics::GetNativeWindowsHGLRC
*Type:* FUNCTION
Get Win32 gl rendercontext native handle (HGLRC). Any other platform return zero.

**Returns**

- `HGLRC` (HGLRC) - native handle

### dmGraphics::GetNativeWindowsHWND
*Type:* FUNCTION
Get Win32 windows native handle (HWND). Any other platform return zero.

**Returns**

- `HWND` (HWND) - native handle

### dmGraphics::GetNativeX11GLXContext
*Type:* FUNCTION
Get Linux X11GLXContext native handle (GLXContext). Any other platform return zero.

**Returns**

- `GLXContext` (GLXContext) - native handle

### dmGraphics::GetNativeX11Window
*Type:* FUNCTION
Get Linux X11Window windows native handle (Window). Any other platform return zero.

**Returns**

- `Window` (Window) - native handle
