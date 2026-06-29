# Endian

**Namespace:** `dmEndian`
**Language:** C++
**Type:** Defold C++
**File:** `endian.hpp`
**Source:** `engine/dlib/src/dmsdk/dlib/endian.hpp`
**Include:** `dmsdk/dlib/endian.hpp`

C++ overloads for endian conversion functions.

## API

### dmEndian::ByteSwap
*Type:* FUNCTION
swap bytes in a 16-bit value

**Parameters**

- `x` (uint16_t) - Value to byte swap

**Returns**

- `value` (uint16_t) - Byte-swapped value

### dmEndian::ByteSwap
*Type:* FUNCTION
swap bytes in a 32-bit value

**Parameters**

- `x` (uint32_t) - Value to byte swap

**Returns**

- `value` (uint32_t) - Byte-swapped value

### dmEndian::ByteSwap
*Type:* FUNCTION
swap bytes in a 64-bit value

**Parameters**

- `x` (uint64_t) - Value to byte swap

**Returns**

- `value` (uint64_t) - Byte-swapped value

### dmEndian::ToHost
*Type:* FUNCTION
Network byte order is big-endian.

**Parameters**

- `x` (uint16_t) - Network-order (big-endian) value

**Returns**

- `value` (uint16_t) - Host-order value

### dmEndian::ToHost
*Type:* FUNCTION
Network byte order is big-endian.

**Parameters**

- `x` (uint32_t) - Network-order (big-endian) value

**Returns**

- `value` (uint32_t) - Host-order value

### dmEndian::ToHost
*Type:* FUNCTION
Network byte order is big-endian.

**Parameters**

- `x` (uint64_t) - Network-order (big-endian) value

**Returns**

- `value` (uint64_t) - Host-order value

### dmEndian::ToNetwork
*Type:* FUNCTION
Network byte order is big-endian.

**Parameters**

- `x` (uint16_t) - Host-order value

**Returns**

- `value` (uint16_t) - Network-order (big-endian) value

### dmEndian::ToNetwork
*Type:* FUNCTION
Network byte order is big-endian.

**Parameters**

- `x` (uint32_t) - Host-order value

**Returns**

- `value` (uint32_t) - Network-order (big-endian) value

### dmEndian::ToNetwork
*Type:* FUNCTION
Network byte order is big-endian.

**Parameters**

- `x` (uint64_t) - Host-order value

**Returns**

- `value` (uint64_t) - Network-order (big-endian) value
