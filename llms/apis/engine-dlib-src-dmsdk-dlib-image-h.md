# Image

**Namespace:** `dmImage`
**Language:** C++
**Type:** Defold C++
**File:** `image.h`
**Source:** `engine/dlib/src/dmsdk/dlib/image.h`
**Include:** `dmsdk/dlib/image.h`

Image API functions.

## API

### GetAstcBlockSize
*Type:* FUNCTION
Get the block size

**Parameters**

- `mem` (void*) - the .astc memory (including the header)
- `memsize` (uint32_t) - the length of the memory blob
- `width` (uint32_t*) - (out) the block width
- `height` (uint32_t*) - (out) the block height
- `depth` (uint32_t*) - (out) the block depth

**Returns**

- `result` (bool) - true if it's an astc file

### GetAstcDimensions
*Type:* FUNCTION
Get the astc image size

**Parameters**

- `mem` (void*) - the .astc memory (including the header)
- `memsize` (uint32_t) - the length of the memory blob
- `width` (uint32_t*) - (out) the block width
- `height` (uint32_t*) - (out) the block height
- `depth` (uint32_t*) - (out) the block depth

**Returns**

- `result` (bool) - true if it's an astc file

### Result
*Type:* ENUM
result enumeration

**Members**

- `dmImage::RESULT_OK` - = 0
- `dmImage::RESULT_UNSUPPORTED_FORMAT` - = -1
- `dmImage::RESULT_IMAGE_ERROR` - = -2

### Type
*Type:* ENUM
type enumeration

**Members**

- `dmImage::TYPE_RGB` - = 0
- `dmImage::TYPE_RGBA` - = 1
- `dmImage::TYPE_LUMINANCE` - = 2
- `dmImage::TYPE_LUMINANCE_ALPHA` - = 3
