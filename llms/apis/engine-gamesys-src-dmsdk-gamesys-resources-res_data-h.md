# Data Resource

**Namespace:** `dmGameSystem`
**Language:** C++
**Type:** Defold C++
**File:** `res_data.h`
**Source:** `engine/gamesys/src/dmsdk/gamesys/resources/res_data.h`
**Include:** `dmsdk/gamesys/resources/res_data.h`

Helper types and accessors for the data resource type (`.datac`).

## API

### DataResource
*Type:* STRUCT
This struct is an opaque handle managed by the engine. Use
GetDDFData() to access the underlying protobuf message for read-only
inspection.

### GetDDFData
*Type:* FUNCTION
Returns a pointer to the decoded dmGameSystemDDF::Data protobuf
message contained in the given data resource.
The lifetime of the returned pointer is tied to the lifetime of the
resource. It must not be freed by the caller.

**Parameters**

- `res` (DataResource*) - Data resource handle

**Returns**

- `data` (const dmGameSystemDDF::Data*) - Pointer to the DDF
        data message, or <code>0</code> if the resource is invalid.
