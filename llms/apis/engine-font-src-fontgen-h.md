# Font Generation

**Namespace:** `FontGeneration`
**Language:** C++
**Type:** Defold C++
**File:** `fontgen.h`
**Source:** `engine/font/src/fontgen.h`
**Include:** `engine/font/src/fontgen.h`

Asynchronously generates glyphs and hands them to a caller-owned cache.
Glyph insertion and completion callbacks run on the job context owner, or on
the caller of FontGenUpdateGlyphs for a batch started with FontGenStartGlyphs.
Cache lookup runs while preparing the batch. The caller context must remain
valid until the completion callback has run or the job has been cancelled.

## API

### FFontGenAddGlyph
*Type:* TYPEDEF
Returning FONT_RESULT_OK transfers ownership of the glyph to the callback.
For every other result, font_gen retains ownership and frees the glyph.

### FFontGenComplete
*Type:* TYPEDEF
Reports completion of a glyph generation batch.

### FFontGenIsGlyphCached
*Type:* TYPEDEF
Looks up a glyph in the caller-owned cache.

### FontGenCreateJobData
*Type:* FUNCTION
Allocates scratch data for one generation batch.

**Parameters**

- `params` (FontGenParams*) - Generation settings and callbacks. The values are copied.
- `num_glyphs` (uint32_t) - Maximum number of glyphs in the batch.

**Returns**

- `job_data` (FontGenJobData*) - Job data, or null when unsupported.

### FontGenDestroyJobData
*Type:* FUNCTION
Batches started with FontGenStartGlyphs cancel and wait for their own jobs.
Other batches must already have finished or been canceled by the caller.

**Parameters**

- `jobdata` (FontGenJobData*) - Batch to release.

### FontGenIsSupported
*Type:* FUNCTION
Tests whether runtime glyph generation is linked into the engine.

**Returns**

- `supported` (bool) - True when the full font_gen library is linked.

### FontGenParams
*Type:* STRUCT
Runtime glyph generation parameters.

**Members**

- `m_UserContext` (void*) - Opaque context passed to all callbacks.
- `m_IsGlyphCached` (FFontGenIsGlyphCached) - Cache lookup callback.
- `m_AddGlyph` (FFontGenAddGlyph) - Glyph insertion callback.
- `m_Complete` (FFontGenComplete) - Batch completion callback.
- `m_Jobs` (HJobContext) - Job system used for asynchronous generation.
- `m_Size` (float) - Glyph generation size in pixels.
- `m_OutlineWidth` (float) - Outline width in pixels.
- `m_ShadowBlur` (float) - Shadow blur spread in pixels.
- `m_IsSdf` (uint8_t) - Non-zero when SDF output is requested.
- `m_IsVector` (uint8_t) - Non-zero when Vector glyph output is requested.
- `m_BitmapEffects` (uint8_t) - Generate RGB vector effect bitmaps on the CPU.
- `m_HasOutline` (uint8_t) - Include the authored outline in the effect bitmaps.
- `m_HasShadow` (uint8_t) - Generate the authored shadow bitmap.

### FontGenStartGlyphs
*Type:* FUNCTION
Worker jobs generate glyphs without invoking callbacks. Call FontGenUpdateGlyphs
on the resource's creation thread to install the results. That update can take
over queued glyphs, including when the caller occupies the last worker. With
no workers it generates all glyphs. The job context must outlive the batch.

**Parameters**

- `jobdata` (FontGenJobData*) - Fresh batch; keep alive until completion or destruction.
- `glyphs` (::TextGlyph*) - Input glyphs, copied during this call.
- `num_glyphs` (uint32_t) - Number of input glyphs.

**Returns**

- `started` (bool) - False when runtime generation is unsupported.

### FontGenUpdateGlyphs
*Type:* FUNCTION
Generates queued glyphs or consumes finished results without dispatching other
jobs or callbacks. Running jobs keep ownership until they finish. The completion
callback may destroy the batch. Calls for one batch must be serialized by its owner.

**Parameters**

- `jobdata` (FontGenJobData*) - Batch to advance.
- `time_limit` (uint64_t) - Soft time limit in microseconds; 0 processes at most one glyph.

**Returns**

- `complete` (bool) - True once all glyphs and the completion callback have been processed.
