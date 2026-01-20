# Engine

**Namespace:** `dmEngine`
**Language:** C++
**Type:** Defold C++
**File:** `extension.hpp`
**Source:** `engine/engine/src/dmsdk/engine/extension.hpp`
**Include:** `dmsdk/engine/extension.hpp`

SDK Engine extension API documentation

## API

### DM_DEBUG
*Type:* MACRO
define for debug builds

**Examples**

Only enable code in debug builds
```
#if defined(DM_DEBUG)
    // ...
#endif

```

### DM_HEADLESS
*Type:* MACRO
define for headless builds

**Examples**

Only enable code in headless builds
```
#if defined(DM_HEADLESS)
    // ...
#endif

```

### DM_RELEASE
*Type:* MACRO
define for release builds

**Examples**

Only enable code in release builds
```
#if defined(DM_RELEASE)
    // ...
#endif

```

### GetConfigFile
*Type:* FUNCTION
get the config file

**Parameters**

- `app_params` (dmExtension::AppParams*) - The app params sent to the extension dmExtension::AppInitialize / dmExtension::AppInitialize

**Returns**

- `config` (dmConfigFile::HConfig) - The game project config file

### GetGameObjectRegister
*Type:* FUNCTION
get the game object register

**Parameters**

- `app_params` (dmExtension::AppParams*) - The app params sent to the extension dmExtension::AppInitialize / dmExtension::AppInitialize

**Returns**

- `register` (dmGameObject::HRegister) - The game object register

### GetHIDContext
*Type:* FUNCTION
get the hid context

**Parameters**

- `app_params` (dmExtension::AppParams*) - The app params sent to the extension dmExtension::AppInitialize / dmExtension::AppInitialize

**Returns**

- `context` (dmHID::HContext) - The hid context

### GetWebServer
*Type:* FUNCTION
get the web server handle

**Notes**

- Only valid in debug builds

**Parameters**

- `app_params` (dmExtension::AppParams*) - The app params sent to the extension dmExtension::AppInitialize / dmExtension::AppInitialize

**Returns**

- `server` (dmWebServer::HServer) - The web server handle
