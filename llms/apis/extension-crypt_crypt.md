# extension-crypt

**Namespace:** `crypt`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with various hash and encode/decode algorithms

## API

### crypt.hash_sha1
*Type:* FUNCTION

**Parameters**

- `buffer` (string)

**Returns**

- `string`

### crypt.hash_sha256
*Type:* FUNCTION

**Parameters**

- `buffer` (string)

**Returns**

- `string`

### crypt.hash_sha512
*Type:* FUNCTION

**Parameters**

- `buffer` (string)

**Returns**

- `string`

### crypt.hash_md5
*Type:* FUNCTION

**Parameters**

- `buffer` (string)

**Returns**

- `string`

### crypt.encode_base64
*Type:* FUNCTION

**Parameters**

- `input` (string)

**Returns**

- `string`

### crypt.decode_base64
*Type:* FUNCTION

**Parameters**

- `input` (string)

**Returns**

- `string`

### crypt.encrypt_xtea
*Type:* FUNCTION

**Parameters**

- `source` (string)
- `key` (string) - key should be <=16

**Returns**

- `string`

### crypt.decrypt_xtea
*Type:* FUNCTION

**Parameters**

- `source` (string)
- `key` (string) - key should be <=16

**Returns**

- `string`
