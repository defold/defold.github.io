# script-script_engine.cpp_doc.json

**Namespace:** `script-script_engine.cpp_doc.json`
**Language:** Lua
**Type:** Defold Lua

## API

### sys.set_engine_throttle
*Type:* FUNCTION
Enables engine throttling.

**Notes**

- It will automatically wake up on input events
- It will automatically throttle again after the cooldown period
- It skips entire update+render loop on the main thread. E.g loading of assets, callbacks from threads (http)
- On threaded systems, Sound will continue to play any started non-streaming sounds. (e.g. looping background music)

**Parameters**

- `enable` (boolean) - true if throttling should be enabled
- `cooldown` (number) - the time period to do update + render for (seconds)

**Examples**

Disable throttling
```
sys.set_engine_throttle(false)

```

Enable throttling
```
sys.set_engine_throttle(true, 1.5)

```

### sys.set_render_enable
*Type:* FUNCTION
Disables rendering

**Notes**

- It will will leave the back buffer as-is

**Parameters**

- `enable` (boolean) - true if throttling should be enabled

**Examples**

Disable rendering
```
sys.set_render_enable(false)

```
