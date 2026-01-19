# extension-adinfo

**Namespace:** `adinfo`
**Language:** Lua
**Type:** Extension

Provides functionality to get the advertising id and tracking status. Supported on iOS and Android. [icon:ios] [icon:android]

## API

### adinfo.get
*Type:* FUNCTION
Get a table with advertising information. [icon:attention] function returns nil if values do not ready

**Examples**

```
function init(self)
    adinfo.get(function(self, info)
      print(info.ad_ident, info.ad_tracking_enabled)
    end)
end

```
