# Align

**Namespace:** `Align`
**Language:** C++
**Type:** Defold C++
**File:** `align.h`
**Source:** `engine/dlib/src/dmsdk/dlib/align.h`
**Include:** `dmsdk/dlib/align.h`

Alignment macros. Use for compiler compatibility

## API

### DM_ALIGN
*Type:* MACRO
Align a value to a boundary

**Parameters**

- `x` (int) - value to align
- `a` (int) - alignment boundary

**Examples**

Align 24 to 16 alignment boundary. results is 32:
```
int result = DM_ALIGN(24, 16);

```

### DM_ALIGNED
*Type:* MACRO
Data structure alignment

**Parameters**

- `a` (int) - number of bytes to align to

**Examples**

Align m_Data to 16 bytes alignment boundary:
```
int DM_ALIGNED(16) m_Data;

```
