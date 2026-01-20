# DStrings

**Namespace:** `DStrings`
**Language:** C++
**Type:** Defold C++
**File:** `dstrings.h`
**Source:** `engine/dlib/src/dmsdk/dlib/dstrings.h`
**Include:** `dmsdk/dlib/dstrings.h`

SDK Defold String Utils API documentation

## API

### dmSnPrintf
*Type:* FUNCTION
Size-bounded string formating. Resulting string is guaranteed to be 0-terminated. Unlike snprintf, which
always returns the untruncated string length, this function returns -1 if the string was truncated.

**Parameters**

- `buffer` (char*) - Buffer to write to
- `count` (size_t) - Size of the buffer
- `format` (const char*) - String format

**Returns**

- `Size` - of the resulting string (excl terminating 0) if it fits, -1 otherwise

**Examples**

```
char path[64];
dmSnPrintf(path, 64, PATH_FORMAT, filename);

```

### dmStrCaseCmp
*Type:* FUNCTION
Case-insensitive string comparison

**Parameters**

- `s1` (const char*) - First string to compare
- `s2` (const char*) - Second string to compare

**Returns**

- `an` - integer greater than, equal to, or less than 0 after lexicographically comparison of s1 and s2

**Examples**

```
dmStrCaseCmp("a", "b"); // 0
dmStrCaseCmp("a", "a"); // 0

```

### dmStrError
*Type:* FUNCTION
Error code to string representation. Wrapper for thread-safe strerror_s/r variants.
If the size of the buffer is too small, the message will be truncated to fit the buffer.
If the buffer is null, or if size is zero, nothing will happen.

**Parameters**

- `dst` (char*) - Destination string that carries the error message
- `size` (size_t) - Max size of destination string in bytes

**Returns**

- `a` - null-terminated error message

**Examples**

```
char buf[128];
dmStrError(buf, sizeof(buf), ENOENT); // buf => "No such file or directory"

```

### dmStrlCat
*Type:* FUNCTION
Size-bounded string concatenation. Same as OpenBSD 2.4 strlcat.
Appends src to string dst of size siz (unlike strncat, siz is the full size of dst, not space left).
At most siz-1 characters will be copied.  Always NUL terminates (unless siz == 0).
Returns strlen(dst) + strlen(src); if retval >= siz, truncation occurred.

**Parameters**

- `dst` (char*) - Destination string
- `src` (char*) - Source string
- `size` (size_t) - Max size

**Returns**

- `Total` - length of the created string

**Examples**

```
const char* src = "foo";
char dst[3] = { 0 };
dmStrlCat(dst, src, sizeof(dst)); // dst = "fo"

```

### dmStrlCpy
*Type:* FUNCTION
Size-bounded string copying. Same as OpenBSD 2.4 strlcpy.
Copy src to string dst of size siz.  At most siz-1 characters will be copied.
Always NUL terminates (unless siz == 0).Returns strlen(src); if retval >= siz, truncation occurred.

**Parameters**

- `dst` (char*) - Destination string
- `src` (const char*) - Source string
- `size` (size_t) - Max size

**Returns**

- `Total` - length of the created string

**Examples**

```
const char* src = "foo";
char dst[3];
dmStrlCpy(dst, src, sizeof(dst)); // dst = "fo"

```

### dmStrTok
*Type:* FUNCTION
Tokenize strings. Equivalent to BSD strsep_r. Thread-save version of strtok.

**Parameters**

- `string` (char*) - Pointer to string. For the first call string is the string to tokenize. Subsequent should pass NULL.
- `delim` (const char*) - Delimiter string
- `lasts` (char**) - Internal state pointer

**Returns**

- `Each` - call to dmStrTok() returns a pointer to a null-terminated string containing the next token. This string does not include the delimiting byte. If no more tokens are found, dmStrTok() returns NULL

**Examples**

```
char* string = strdup("a b c");
char* s, *last;
s = dmStrTok(string, " ", &last); // a
s = dmStrTok(0, " ", &last); // b
s = dmStrTok(0, " ", &last); // c

```
