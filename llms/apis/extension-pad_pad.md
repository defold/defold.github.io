# extension-pad

**Namespace:** `pad`
**Language:** Lua
**Type:** Extension

Functionality to work with Play Asset Delivery and the AssetPackManager

## API

### pad.cancel
*Type:* FUNCTION
Requests to cancel the download of the specified asset packs.

**Parameters**

- `pack_name` (string)

### pad.fetch
*Type:* FUNCTION
Requests to download the specified asset pack.

**Parameters**

- `pack_name` (string)

### pad.remove_pack
*Type:* FUNCTION
Deletes the specified asset pack from the internal storage of the app.

**Parameters**

- `pack_name` (string)

### pad.get_pack_state
*Type:* FUNCTION
Requests download state and details for the specified asset pack. This is an asynchronous function and will send a `PACK_STATE_UPDATED` event once the new state is available.

**Parameters**

- `pack_name` (string)

### pad.get_pack_location
*Type:* FUNCTION
Returns the location of the specified asset pack on the device or an empty string if this pack is not downloaded.

**Parameters**

- `pack_name` (string)

**Returns**

- `strin`

### pad.get_pack_bytes_downloaded
*Type:* FUNCTION
Returns the total number of bytes already downloaded for the pack. Note that you must have called the `get_pack_state()` function first and wait for a `PACK_STATE_UPDATED` event before calling this function.

**Parameters**

- `pack_name` (string)

**Returns**

- `bytes_downloade`

### pad.get_pack_error_code
*Type:* FUNCTION
Returns the error code for the pack, if Play has failed to download the pack. Note that you must have called the `get_pack_state()` function first and wait for a `PACK_STATE_UPDATED` event before calling this function.

**Parameters**

- `pack_name` (string)

**Returns**

- `error_cod`

### pad.get_pack_status
*Type:* FUNCTION
Returns the download status of the pack. Note that you must have called the `get_pack_state()` function first and wait for a `PACK_STATE_UPDATED` event before calling this function.

**Parameters**

- `pack_name` (string)

**Returns**

- `statu`

### pad.get_pack_total_bytes_to_download
*Type:* FUNCTION
Returns the total size of the pack in bytes. Note that you must have called the `get_pack_state()` function first and wait for a `PACK_STATE_UPDATED` event before calling this function.

**Parameters**

- `pack_name` (string)

**Returns**

- `bytes_to_downloa`

### pad.get_pack_transfer_progress_percentage
*Type:* FUNCTION
Returns the percentage of the asset pack already transferred to the app. Note that you must have called the `get_pack_state()` function first and wait for a `PACK_STATE_UPDATED` event before calling this function.

**Parameters**

- `pack_name` (string)

**Returns**

- `numbe`

### pad.show_confirmation_dialog
*Type:* FUNCTION
Shows a dialog that asks the user for consent to download packs Shows a dialog that asks the user for consent to download packs that are currently in either the AssetPackStatus.REQUIRES_USER_CONFIRMATION state or the AssetPackStatus.WAITING_FOR_WIFI state. Will return result in event listener.

**Parameters**

- `pack_name` (string)

### pad.set_listener
*Type:* FUNCTION
Set listener to receive events

**Parameters**

- `listener` (function) - The function to call (self, event)

### EVENT_PACK_STATE_UPDATED
*Type:* VARIABLE

### EVENT_PACK_STATE_ERROR
*Type:* VARIABLE

### EVENT_REMOVE_PACK_COMPLETED
*Type:* VARIABLE

### EVENT_REMOVE_PACK_CANCELED
*Type:* VARIABLE

### EVENT_REMOVE_PACK_ERROR
*Type:* VARIABLE

### EVENT_DIALOG_CONFIRMED
*Type:* VARIABLE

### EVENT_DIALOG_DECLINED
*Type:* VARIABLE

### EVENT_DIALOG_CANCELED
*Type:* VARIABLE

### EVENT_DIALOG_ERROR
*Type:* VARIABLE

### STATUS_UNKNOWN
*Type:* VARIABLE

### STATUS_PENDING
*Type:* VARIABLE

### STATUS_DOWNLOADING
*Type:* VARIABLE

### STATUS_TRANSFERRING
*Type:* VARIABLE

### STATUS_COMPLETED
*Type:* VARIABLE

### STATUS_FAILED
*Type:* VARIABLE

### STATUS_CANCELED
*Type:* VARIABLE

### STATUS_WAITING_FOR_WIFI
*Type:* VARIABLE

### STATUS_NOT_INSTALLED
*Type:* VARIABLE

### STATUS_REQUIRES_USER_CONFIRMATION
*Type:* VARIABLE

### ERRORCODE_ACCESS_DENIED
*Type:* VARIABLE
Download not permitted under the current device circumstances

### ERRORCODE_API_NOT_AVAILABLE
*Type:* VARIABLE
The Asset Delivery API isn't available.

### ERRORCODE_APP_NOT_OWNED
*Type:* VARIABLE
The app isn't owned by any user on this device.

### ERRORCODE_APP_UNAVAILABLE
*Type:* VARIABLE
The requesting app is unavailable.

### ERRORCODE_CONFIRMATION_NOT_REQUIRED
*Type:* VARIABLE
Returned if AssetPackManager.showConfirmationDialog(Activity) is called but no asset packs require user confirmation.

### ERRORCODE_DOWNLOAD_NOT_FOUND
*Type:* VARIABLE
The requested download isn't found.

### ERRORCODE_INSUFFICIENT_STORAGE
*Type:* VARIABLE
Asset pack download failed due to insufficient storage.

### ERRORCODE_INTERNAL_ERROR
*Type:* VARIABLE
Unknown error downloading an asset pack.

### ERRORCODE_INVALID_REQUEST
*Type:* VARIABLE
The request is invalid.

### ERRORCODE_NETWORK_ERROR
*Type:* VARIABLE
Network error.

### ERRORCODE_NETWORK_UNRESTRICTED
*Type:* VARIABLE
Returned if AssetPackManager.showCellularDataConfirmation(Activity) is called but no asset packs are waiting for Wi-Fi.

### ERRORCODE_NO_ERROR
*Type:* VARIABLE

### ERRORCODE_PACK_UNAVAILABLE
*Type:* VARIABLE
The requested asset pack isn't available.

### ERRORCODE_PLAY_STORE_NOT_FOUND
*Type:* VARIABLE
The Play Store app is either not installed or not the official version.

### ERRORCODE_UNRECOGNIZED_INSTALLATION
*Type:* VARIABLE
The installed app version is not recognized by Play.
