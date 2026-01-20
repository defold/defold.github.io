# Graphics Vulkan

**Namespace:** `dmGraphics`
**Language:** C++
**Type:** Defold C++
**File:** `graphics_vulkan.h`
**Source:** `engine/graphics/src/dmsdk/graphics/graphics_vulkan.h`
**Include:** `dmsdk/graphics/graphics_vulkan.h`

Graphics Vulkan API

## API

### VkDescriptorPool
*Type:* TYPEDEF

### VkDevice
*Type:* TYPEDEF

### VulkanCreateDescriptorPool
*Type:* FUNCTION
Create Vulkan descriptor pool. No need to deallocate descripto pool manualy
because it will be deallocated automatically when context will be destroyed.
Only available when using Mac/iOS.

**Parameters**

- `vk_device` (VkDevice) - the Vulkan device handle
- `max_descriptors` (uint16_t) - maximum size of allocated pool
- `vk_descriptor_pool_out` (VkDescriptorPool*) - result Vulkan descriptor pool

**Returns**

- `result` (bool) - true if creation was successful. Otherwise returns false

### VulkanGetActiveSwapChainTexture
*Type:* FUNCTION
Get the current swap chain texture

**Parameters**

- `context` (dmGraphics::HContext) - the Vulkan context

**Returns**

- `swapchain` (dmGraphics::HTexture) - the swap chain texture for the current frame

### VulkanGetCurrentFrameCommandBuffer
*Type:* FUNCTION
Get Vulkan command buffer which used at the current frame. Only available when using Mac/iOS.

**Parameters**

- `context` (dmGraphics::HContext) - the Vulkan context

**Returns**

- `command_buffer` (VkCommandBuffer) - the Vulkan command buffer

### VulkanGetDevice
*Type:* FUNCTION
Get Vulkan device handle. Only available when using Mac/iOS.

**Parameters**

- `context` (dmGraphics::HContext) - the Vulkan context

**Returns**

- `device` (VkDevice) - the Vulkan device handle

### VulkanGetGraphicsQueue
*Type:* FUNCTION
Get Vulkan graphics queue handle. Only available when using Mac/iOS.

**Parameters**

- `context` (dmGraphics::HContext) - the Vulkan context

**Returns**

- `queue` (VkQueue) - the Vulkan graphics queue

### VulkanGetGraphicsQueueFamily
*Type:* FUNCTION
Get Vulkan queue family. Only available when using Mac/iOS.

**Parameters**

- `context` (dmGraphics::HContext) - the Vulkan context
return family <span class="type"> uint16_t</span> graphics queue family

### VulkanGetInstance
*Type:* FUNCTION
Get Vulkan instance handle. Only available when using Mac/iOS.

**Parameters**

- `context` (dmGraphics::HContext) - the Vulkan context

**Returns**

- `instance` (VkInstance) - the Vulkan instance handle

### VulkanGetPhysicalDevice
*Type:* FUNCTION
Get Vulkan physical device handle. Only available when using Mac/iOS.

**Parameters**

- `context` (dmGraphics::HContext) - the Vulkan context

**Returns**

- `physical_device` (VkPhysicalDevice) - the Vulkan physical device handle

### VulkanGetRenderPass
*Type:* FUNCTION
Get Vulkan render pass handle. Only available when using Mac/iOS.

**Parameters**

- `context` (dmGraphics::HContext) - the Vulkan context

**Returns**

- `render_pass` (VkRenderPass) - the Vulkan render pass handle

### VulkanGraphicsCommandQueueToMetal
*Type:* FUNCTION
Get the native MTLCommandQueue from the Vulkan context. Only available when using Mac/iOS.

**Parameters**

- `context` (dmGraphics::HContext) - the Vulkan context

**Returns**

- `mtl_queue` (id<MTLCommandQueue>) - the Metal graphics queue wrapped with a (__bridge void*)

### VulkanTextureToMetal
*Type:* FUNCTION
Get a native MTLTexture from a Vulkan HTexture. Only available when using Mac/iOS.

**Parameters**

- `context` (dmGraphics::HContext) - the Vulkan context
- `texture` (dmGraphics::HTexture) - the texture

**Returns**

- `mtl_texture` (id<MTLTexture>) - the Metal texture wrapped with a (__bridge void*)
