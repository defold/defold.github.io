# extension-adpf

**Namespace:** `adpf`
**Language:** Lua
**Type:** Extension

Functions and constants for interacting with the Android Device Performance Framework

## API

### adpf.hint.initialize
*Type:* FUNCTION
Initialise performance hints

**Parameters**

- `target_fps_nanos` (number)

**Returns**

- `boolean` - Return true if the PerformanceHintManager API is available on the device

### adpf.hint.update_target_fps
*Type:* FUNCTION
Update the target fps

**Parameters**

- `target_fps_nanos` (number)

###
*Type:* TABLE
Functions and constants for interacting with the PerformanceHintManager

### adpf.thermal.initialize
*Type:* FUNCTION
Initialise thermal

**Parameters**

- `available` (boolean) - Return true if the Thermal API is available on the device

### adpf.thermal.get_headroom
*Type:* FUNCTION
Provides an estimate of how much thermal headroom the device currently has before hitting severe throttling.

**Parameters**

- `forecast_seconds` (number) - how many seconds in the future to forecast

**Returns**

- `number` - a value greater than or equal to 0.0 where 1.0 indicates the SEVERE throttling threshold

### adpf.thermal.get_status
*Type:* FUNCTION
Get the current thermal status of the device

**Returns**

- `number` - The current thermal status of the device. One of THERMAL_STATUS_XYZ.

### THERMAL_STATUS_CRITICAL
*Type:* VARIABLE
Platform has done everything to reduce power.

### THERMAL_STATUS_EMERGENCY
*Type:* VARIABLE
Key components in platform are shutting down due to thermal condition.

### THERMAL_STATUS_LIGHT
*Type:* VARIABLE
Light throttling where UX is not impacted.

### THERMAL_STATUS_MODERATE
*Type:* VARIABLE
Moderate throttling where UX is not largely impacted.

### THERMAL_STATUS_NONE
*Type:* VARIABLE
Not under throttling.

### THERMAL_STATUS_SEVERE
*Type:* VARIABLE
Severe throttling where UX is largely impacted.

### THERMAL_STATUS_SHUTDOWN
*Type:* VARIABLE
Need shutdown immediately

###
*Type:* TABLE
Functions and constants for interacting with the PowerManager ThermalAPI
