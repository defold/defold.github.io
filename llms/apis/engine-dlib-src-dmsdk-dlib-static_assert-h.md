# Static Assert

**Namespace:** `dmStaticAssert`
**Language:** C++
**Type:** Defold C++
**File:** `static_assert.h`
**Source:** `engine/dlib/src/dmsdk/dlib/static_assert.h`
**Include:** `dmsdk/dlib/static_assert.h`

```cpp
void test() {
    DM_STATIC_ASSERT(sizeof(int) == 4, Invalid_int_size);
}
```

## API

### DM_STATIC_ASSERT
*Type:* MACRO
This is using C++11 static_assert on platforms that support it and use c++11. Otherwise
it's using a c construct to check the condition.
As such, it is currently required to be used whithin a function scope.

**Parameters**

- `x` (bool) - expression
- `xmsg` (string) - expression

**Examples**

Verify the size of a struct is within a limit
```
DM_STATIC_ASSERT(sizeof(MyStruct) <= 32, Invalid_Struct_Size);

```
