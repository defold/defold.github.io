# ConfigFile

**Namespace:** `dmConfigFile`
**Language:** C++
**Type:** Defold C++
**File:** `configfile_gen.hpp`
**Source:** `engine/dlib/src/dmsdk/dlib/configfile_gen.hpp`
**Include:** `dmsdk/dlib/configfile_gen.hpp`

Configuration file access functions.
The configuration file is compiled version of the [file:game.project] file.

## API

### ConfigFileExtensionDescBufferSize
*Type:* FUNCTION
It defines the minimum size of the description blob being registered.

### ConfigFileGetFloat
*Type:* FUNCTION
Get config value as float, returns default if the key isn't found

**Parameters**

- `config` (HConfigFile) - Config file handle
- `key` (const char*) - Key in format section.key (.key for no section)
- `default_value` (int32_t) - Default value to return if key isn't found

**Returns**

- `value` (int32_t) - found value or default value

**Examples**

```
static ExtensionResult AppInitialize(ExtensionAppParams* params)
{
    float gravity = ConfigFileGetFloat(params->m_ConfigFile, "physics.gravity_y", -9.8f);
}
``````cpp
static dmExtension::Result AppInitialize(dmExtension::AppParams* params)
{
    float gravity = dmConfigFile::GetFloat(params->m_ConfigFile, "physics.gravity_y", -9.8f);
}

```

### ConfigFileGetInt
*Type:* FUNCTION
Get config value as integer, returns default if the key isn't found

**Parameters**

- `config` (HConfigFile) - Config file handle
- `key` (const char*) - Key in format section.key (.key for no section)
- `default_value` (int32_t) - Default value to return if key isn't found

**Returns**

- `value` (int32_t) - found value or default value

**Examples**

```
static ExtensionResult AppInitialize(ExtensionAppParams* params)
{
    int32_t displayWidth = ConfigFileGetInt(params->m_ConfigFile, "display.width", 640);
}
``````cpp
static dmExtension::Result AppInitialize(dmExtension::AppParams* params)
{
    int32_t displayWidth = dmConfigFile::GetInt(params->m_ConfigFile, "display.width", 640);
}

```

### ConfigFileGetString
*Type:* FUNCTION
Get config value as string, returns default if the key isn't found

**Parameters**

- `config` (HConfigFile) - Config file handle
- `key` (const char*) - Key in format section.key (.key for no section)
- `default_value` (const char*) - Default value to return if key isn't found

**Returns**

- `value` (const char*) - found value or default value

**Examples**

```
static ExtensionResult AppInitialize(ExtensionAppParams* params)
{
    const char* projectTitle = ConfigFileGetString(params->m_ConfigFile, "project.title", "Untitled");
}
``````cpp
static dmExtension::Result AppInitialize(dmExtension::AppParams* params)
{
    const char* projectTitle = dmConfigFile::GetString(params->m_ConfigFile, "project.title", "Untitled");
}

```

### DM_DECLARE_CONFIGFILE_EXTENSION
*Type:* MACRO
Declare and register new config file extension to the engine.
Each get function should return true if it sets a proper value. Otherwise return false.

**Examples**

Register a new config file extension:
```
DM_DECLARE_CONFIGFILE_EXTENSION(MyConfigfileExtension, "MyConfigfileExtension", create, destroy, get_string, get_int, get_float);

```

### FConfigFileCreate
*Type:* TYPEDEF
Called when config file extension is created

**Parameters**

- `config` (HConfigFile) - Config file handle

### FConfigFileDestroy
*Type:* TYPEDEF
Called when config file extension is destroyed

**Parameters**

- `config` (HConfigFile) - Config file handle

### FConfigFileGetFloat
*Type:* TYPEDEF
Called when a float is requested from the config file extension

**Parameters**

- `config` (HConfigFile) - Config file handle
- `key` (const char*) - Key in format section.key (.key for no section)
- `default_value` (float) - Default value to return if key isn't found
- `out` (float*) - Out argument where result is stored if found.

**Returns**

- `result` (bool) - True if property was found

### FConfigFileGetFloat
*Type:* TYPEDEF
Called when a float is requested from the config file extension

**Parameters**

- `config` (HConfigFile) - Config file handle
- `key` (const char*) - Key in format section.key (.key for no section)
- `default_value` (float) - Default value to return if key isn't found
- `out` (float*) - Out argument where result is stored if found.

**Returns**

- `result` (bool) - True if property was found

### FConfigFileGetInt
*Type:* TYPEDEF
Called when an integer is requested from the config file extension

**Parameters**

- `config` (HConfigFile) - Config file handle
- `key` (const char*) - Key in format section.key (.key for no section)
- `default_value` (int32_t) - Default value to return if key isn't found
- `out` (int32_t*) - Out argument where result is stored if found.

**Returns**

- `result` (bool) - True if property was found

### FConfigFileGetString
*Type:* TYPEDEF
Called when a string is requested from the config file extension

**Parameters**

- `config` (HConfigFile) - Config file handle
- `key` (const char*) - Key in format section.key (.key for no section)
- `default_value` (const char*) - Default value to return if key isn't found
- `out` (const char**) - Out argument where result is stored if found. Caller must free() this memory.

**Returns**

- `result` (bool) - True if property was found

### GetFloat
*Type:* FUNCTION
Get config value as float, returns default if the key isn't found

**Parameters**

- `config` (HConfigFile) - Config file handle
- `key` (const char*) - Key in format section.key (.key for no section)
- `default_value` (int32_t) - Default value to return if key isn't found

**Returns**

- `value` (int32_t) - found value or default value

**Examples**

```
static ExtensionResult AppInitialize(ExtensionAppParams* params)
{
    float gravity = ConfigFileGetFloat(params->m_ConfigFile, "physics.gravity_y", -9.8f);
}
``````cpp
static dmExtension::Result AppInitialize(dmExtension::AppParams* params)
{
    float gravity = dmConfigFile::GetFloat(params->m_ConfigFile, "physics.gravity_y", -9.8f);
}

```

### GetInt
*Type:* FUNCTION
Get config value as integer, returns default if the key isn't found

**Parameters**

- `config` (HConfigFile) - Config file handle
- `key` (const char*) - Key in format section.key (.key for no section)
- `default_value` (int32_t) - Default value to return if key isn't found

**Returns**

- `value` (int32_t) - found value or default value

**Examples**

```
static ExtensionResult AppInitialize(ExtensionAppParams* params)
{
    int32_t displayWidth = ConfigFileGetInt(params->m_ConfigFile, "display.width", 640);
}
``````cpp
static dmExtension::Result AppInitialize(dmExtension::AppParams* params)
{
    int32_t displayWidth = dmConfigFile::GetInt(params->m_ConfigFile, "display.width", 640);
}

```

### GetString
*Type:* FUNCTION
Get config value as string, returns default if the key isn't found

**Parameters**

- `config` (HConfigFile) - Config file handle
- `key` (const char*) - Key in format section.key (.key for no section)
- `default_value` (const char*) - Default value to return if key isn't found

**Returns**

- `value` (const char*) - found value or default value

**Examples**

```
static ExtensionResult AppInitialize(ExtensionAppParams* params)
{
    const char* projectTitle = ConfigFileGetString(params->m_ConfigFile, "project.title", "Untitled");
}
``````cpp
static dmExtension::Result AppInitialize(dmExtension::AppParams* params)
{
    const char* projectTitle = dmConfigFile::GetString(params->m_ConfigFile, "project.title", "Untitled");
}

```

### HConfig
*Type:* TYPEDEF
Each game session has a single config file that holds all parameters from game.project and any overridden values.

**Notes**

- Properties can be overridden on command line or via the config file extension system. (See [ref:DM_DECLARE_CONFIGFILE_EXTENSION])

### HConfigFile
*Type:* TYPEDEF
Each game session has a single config file that holds all parameters from game.project and any overridden values.

**Notes**

- Properties can be overridden on command line or via the config file extension system. (See [ref:DM_DECLARE_CONFIGFILE_EXTENSION])
