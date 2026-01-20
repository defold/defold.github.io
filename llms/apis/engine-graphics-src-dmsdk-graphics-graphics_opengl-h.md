# Graphics OpenGL

**Namespace:** `dmGraphics`
**Language:** C++
**Type:** Defold C++
**File:** `graphics_opengl.h`
**Source:** `engine/graphics/src/dmsdk/graphics/graphics_opengl.h`
**Include:** `dmsdk/graphics/graphics_opengl.h`

Graphics OpenGL API

## API

### OpenGLGetDefaultFramebufferId
*Type:* FUNCTION
Get the default framebuffer ID

**Parameters**

- `context` (dmGraphics::HContext) - the OpenGL context

**Returns**

- `framebuffer` (uint32_t) - the framebuffer id

### OpenGLGetRenderTargetId
*Type:* FUNCTION
Get the OpenGL render target id from a render target

**Parameters**

- `context` (dmGraphics::HContext) - the OpenGL context
- `render_target` (dmGraphics::HRenderTarget) - the render target to get the ID from

**Returns**

- `id` (uint32_t) - the OpenGL render target id
