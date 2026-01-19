# Crypt

**Namespace:** `dmCrypt`
**Language:** C++
**Type:** Defold C++
**File:** `crypt.h`
**Source:** `engine/dlib/src/dmsdk/dlib/crypt.h`
**Include:** `dmsdk/dlib/crypt.h`

Various hash and encode/decode functions.

## API

### Algorithm
*Type:* ENUM
encryption algorithm enumeration

**Members**

- `dmCrypt::ALGORITHM_XTEA`

### dmCrypt::Base64Decode
*Type:* FUNCTION
Base64 decode a buffer

**Notes**

- Call this function with *dst_len = 0 to obtain the required buffer size in *dst_len

**Parameters**

- `src` (const uint8_t*) - The source data to encode
- `src_len` (uint32_t) - key The length of source data in bytes
- `dst` (uint8_t*) - The destination buffer
- `dst_len[in,out]` (uint32_t*) - In: The length of the destination in bytes. Out: The length of the decoded string.

**Returns**

- `success` (bool) - true if the decoding went ok

### dmCrypt::Base64Encode
*Type:* FUNCTION
Base64 encode a buffer

**Notes**

- Call this function with *dst_len = 0 to obtain the required buffer size in *dst_len

**Parameters**

- `src` (const uint8_t*) - The source data to encode
- `src_len` (uint32_t) - key The length of source data in bytes
- `dst` (uint8_t*) - The destination buffer
- `dst_len[in,out]` (uint32_t*) - In: The length of the destination in bytes. Out: The length of the encoded string.

**Returns**

- `success` (bool) - true if the encoding went ok

### dmCrypt::Decrypt
*Type:* FUNCTION
Decrypt data in place

**Parameters**

- `algo` (dmCrypt::Algorithm) - algorithm
- `data` (const uint8_t*) - data
- `datalen` (uint32_t) - data length in bytes
- `key` (const uint8_t*) - key
- `keylen` (uint32_t) - key length

**Returns**

- `result` (dmCrypt::Result) - the decryption result

### dmCrypt::Encrypt
*Type:* FUNCTION
Encrypt data in place

**Parameters**

- `algo` (dmCrypt::Algorithm) - algorithm
- `data` (const uint8_t*) - data
- `datalen` (uint32_t) - data length in bytes
- `key` (const uint8_t*) - key
- `keylen` (uint32_t) - key length

**Returns**

- `result` (dmCrypt::Result) - the encryption result

### dmCrypt::HashMd5
*Type:* FUNCTION
Hash buffer using MD5

**Parameters**

- `buf` (const uint8_t*) - The source data to hash
- `buflen` (uint32_t) - key The length of source data in bytes
- `digest` (const uint8_t*) - The destination buffer (16 bytes)

### dmCrypt::HashSha1
*Type:* FUNCTION
Hash buffer using SHA1

**Parameters**

- `buf` (const uint8_t*) - The source data to hash
- `buflen` (uint32_t) - The length of source data in bytes
- `digest` (uint8_t*) - The destination buffer (20 bytes)

### dmCrypt::HashSha256
*Type:* FUNCTION
Hash buffer using SHA256

**Parameters**

- `buf` (const uint8_t*) - The source data to hash
- `buflen` (uint32_t) - key The length of source data in bytes
- `digest` (uint8_t*) - The destination buffer (32 bytes)

### dmCrypt::HashSha512
*Type:* FUNCTION
Hash buffer using SHA512

**Parameters**

- `buf` (const uint8_t*) - The source data to hash
- `buflen` (uint32_t) - key The length of source data in bytes
- `digest` (uint8_t*) - The destination buffer (64 bytes)

### Result
*Type:* ENUM
result enumeration

**Members**

- `dmCrypt::RESULT_OK` - = 0
- `dmCrypt::RESULT_ERROR` - = 1
