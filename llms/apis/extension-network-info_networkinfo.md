# extension-network-info

**Namespace:** `networkinfo`
**Language:** Lua
**Type:** Extension

Functions to get information about the network configuration of the device.

## API

### networkinfo.get_proxy_info
*Type:* FUNCTION
Get information about proxies for a specific url.

**Parameters**

- `url` (string) - The url to get proxy configurations for

**Returns**

- `table` - A list of proxies to try in order. Each proxy has three values
  type: direct (no proxy), http, socks
  host: proxy url
  port: proxy port number
