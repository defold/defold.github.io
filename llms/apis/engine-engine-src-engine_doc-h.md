# Engine runtime

**Namespace:** `engine`
**Language:** C++
**Type:** Defold C++
**File:** `engine_doc.h`
**Source:** `engine/engine/src/engine_doc.h`
**Include:** `engine/engine/src/engine_doc.h`

Engine runtime documentation

## API

### --config=
*Type:* MACRO
Override game properties with the format --config=section.key=value

**Examples**

```
$ ./dmengine --config=project.mode=TEST --config=project.server=http://testserver.com

```

### --verify-graphics-calls=
*Type:* MACRO
Disables OpenGL error checking.
This is especially beneficial for running debug builds in the Chrome browser,
in which the calls to glGetError() is notoriously slow.
Default value is "true" for debug builds, and "false" for release builds.

**Examples**

```
$ ./dmengine --verify-graphics-calls=false

```

### DM_LOG_PORT
*Type:* MACRO
Enables receiving the log on a designated port (e.g. using telnet)
Valid values are integers between [0, 65535]

### DM_QUIT_ON_ESC
*Type:* MACRO
Enables quitting the app directly by pressing the ESCAPE key.
Set to "1" to enable this feature.

### DM_SAVE_HOME
*Type:* MACRO
Overrides the save directory when using sys.get_save_file()

### DM_SERVICE_PORT
*Type:* MACRO
Overrides the engine service port, when creating the internal http server (e.g web profiler)
Valid values are integers between [0, 65535] and the string "dynamic" (which translates to 0).
Default value is 8001.

### launch_project
*Type:* MACRO
Launch the engine with a specific project file
If no project is specified, it will default to "./game.projectc", "build/default/game.projectc"

**Notes**

- It has to be the first argument

**Examples**

```
$ ./dmengine some/folder/game.projectc

```
