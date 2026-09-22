# Project settings {#manuals:project-settings}

The file *game.project* contains all project wide settings. It must stay in the root folder of the project and must be named *game.project*. The first thing the engine does when starting up and launching your game is look for this file.

Every setting in the file belongs to a category. When you open the file Defold presents all settings grouped by category.

## File format

The settings in *game.project* are usually changed from within Defold, but the file can also be edited in any standard text editor. The file follows the INI file format standard and looks like this:
```ini
[category1]
setting1 = value
setting2 = value
[category2]
...
```

A real example is:
```ini
[bootstrap]
main_collection = /main/main.collectionc
```

which means that the setting *main_collection* belongs to the *bootstrap* category. Whenever a file reference is used, like the example above, the path needs to be appended with a 'c' character, which means you're referencing the compiled version of the file. Also note that the folder containing *game.project* will be the project root, which is why there is an initial '/' in the setting path.

## Runtime access

It is possible to read values from *game.project* at runtime using [`sys.get_config_string(key)`](https://defold.com/ref/sys/#sys.get_config_string), [`sys.get_config_number(key)`](https://defold.com/ref/sys/#sys.get_config_number), [`sys.get_config_int(key)`](https://defold.com/ref/sys/#sys.get_config_int), and [`sys.get_config_boolean(key)`](https://defold.com/ref/sys/#sys.get_config_boolean). Examples:
```lua
local title = sys.get_config_string("project.title")
local gravity_y = sys.get_config_number("physics.gravity_y")
local fullscreen = sys.get_config_boolean("display.fullscreen", false)
```

The key is a combination of the category and setting name, separated by a dot, and written in lowercase letters with any space characters replaced by underscores. Examples: The field "Title" from the "Project" category becomes `project.title` and the "Gravity Y" field from the "Physics" category becomes `physics.gravity_y`.

## Sections and settings

Below are all the available settings, arranged by category.

### Project

#### Title
The title of the application.

#### Version
The version of the application.

#### Publisher
Publisher name.

#### Developer
Developer name.

#### Write Log File
Controls when the engine writes a log file. Options:

- "Never": Do not write a log file.
- "Debug": Write a log file only for Debug builds.
- "Always": Write a log file for both Debug and Release builds.

If running more than one instance from the editor the file will be named *instance_2_log.txt* with `2` being the instance index. If running a single instance or from a bundle the file will be named *log.txt*. The location of the log file will be one of the following paths (tried in order):

1. The path specified in *project.log_dir* (hidden setting)
2. The system log path:
  * macOS/iOS: `NSDocumentDirectory`
  * Android: `Context.getExternalFilesDir()`
  * Others: Application root
3. The application support path
  * macOS/iOS: `NSApplicationSupportDirectory`
  * Windows: `CSIDL_APPDATA` (e.g. `C:\Users\\AppData\Roaming`)
  * Android: `Context.getFilesDir()`
  * Linux: `HOME` environment variable

#### Minimum Log Level
Specify the minimum log level for the logging system. Only logs at or above this level will be shown.

#### Compress Archive
Enables compression of archives when bundling. Note that this currently applies to all platforms except Android where the apk already contains all data compressed.

#### Dependencies
A list of URLs to the project *Library URL*s. Refer to the [Libraries manual](https://defold.com/llms/manuals/libraries.md) for more information.

#### Dependencies Metadata
`project.dependencies_metadata` includes metadata about library dependencies in the runtime bundle. Disabled by default. The metadata can be read at runtime using `sys.load_resource("/.internal/dependencies.json")`.

#### Custom Resources
`custom_resources`
Custom resources are bundled in the main game archive using the [*Custom Resources* field](https://defold.com/llms/manuals/project-settings.md) in *game.project*.

The *Custom Resources* field should contain a comma separated list of resources that will be included in the main game archive. If directories are specified, all files and directories in that directory are recursively included. You can read the files using [`sys.load_resource()`](https://defold.com/ref/sys/#sys.load_resource).

Loading custom resources is covered in more detail in the [File Access manual](https://defold.com/llms/manuals/file-access.md).

Paths contributed by extensions through `custom_resources.default` in `ext.properties` are combined with this setting. See [extension custom resources](https://defold.com/llms/manuals/extensions.md) for an example.

#### Bundle Resources
`bundle_resources`
Bundle resources are additional files and folders located as a part of your application bundle using the [*Bundle Resources* field](https://defold.com/llms/manuals/project-settings.md) in *game.project*.

The *Bundle Resources* field should contain a comma separated list of directories containing resource files and folders that should be copied as-is into the resulting package when bundling. The directories must be specified with an absolute path from the project root, for example `/res`. The resource directory must contain subfolders named by `platform`, or `architecture-platform`.

Supported platforms are `ios`, `android`, `osx`, `win32`, `linux`, `web`, `switch` A subfolder named `common` is also allowed, containing resource files common for all platforms. Example:
```
res
├── win32
│   └── mywin32file.txt
├── common
│   └── mycommonfile.txt
└── android
    ├── myandroidfile.txt
    └── res
        └── xml
            └── filepaths.xml
```

You can use [`sys.get_application_path()`](https://defold.com/ref/sys/#sys.get_application_path:) to get the path to where the application is stored. Use this application base path to create the final absolute path to the files you need access to. Once you have the absolute path of these files you can use the `io.*` and `os.*` functions to access the files.

Loading bundle resources is covered in more detail in the [File Access manual](https://defold.com/llms/manuals/file-access.md).

#### Bundle Exclude Resources
`bundle_exclude_resources`
A comma separated list of resources that should not be included in the bundle. That is, they're removed from the result of the collection of the `bundle_resources` step.

### Library

#### Include Dirs
A space separated list of directories that should be shared from your project via library sharing. Refer to the [Libraries manual](https://defold.com/llms/manuals/libraries.md) for more information.

#### Defold Min Version
`library.defold_min_version` specifies the minimum Defold/Bob version required to use this project as a library, for example `1.11.2`. Leave empty to specify no minimum version.

### Display

#### Width
The width in pixels of the application window.

#### Height
The height in pixels of the application window.

#### High Dpi
Creates a high dpi back buffer on displays that support it. Typically the game will render in double the resolution than what is set in the *Width* and *Height* settings, which will still be the logical resolution used in scripts and properties.

#### Samples
How many samples to use for super sampling anti-aliasing. It sets the `GLFW_FSAA_SAMPLES` window hint. A value of `0` means that anti-aliasing is turned off.

This setting controls the window. Offscreen [multisampled render targets](https://defold.com/llms/manuals/render.md) have their own sample count.

#### Fullscreen
Check if the application should start full screen. If unchecked, the application runs windowed.

#### Update Frequency
The desired frame rate in Hertz. Set to 0 for variable frame rate. A value larger than 0 will result in a fixed frame rate capped at runtime towards the actual frame rate (which means that you cannot update the game loop twice in an engine frame). Use [`sys.set_update_frequency(hz)`](https://defold.com/ref/sys/?q=set_update_frequency#sys.set_update_frequency:frequency) to change this value at runtime. This setting also works in headless builds.

#### Swap interval
This integer value controls how the application deals with vsync. 0 disables vsync, and the default value is 1. When using an OpenGL adapter, this value sets the number of frames the window should [update between buffer swaps](https://www.khronos.org/opengl/wiki/Swap_Interval). For Vulkan, there is no built-in concept of swap interval, the value instead controls if vsync should be enabled or not.

#### Vsync
Legacy compatibility setting. This setting is deprecated; use **Swap Interval** for new projects. If disabled, it forces the effective swap interval to `0`. If enabled, **Swap Interval** determines the effective value.

#### Display Profiles
Specifies which display profiles file to use, `/builtins/render/default.display_profilesc` by default. Learn more in the [GUI Layouts manual](https://defold.com/llms/manuals/gui-layouts.md).

#### Dynamic Orientation
Check if the app should dynamically switch between portrait and landscape on device rotation. Note that the development app does not currently respect this setting.

#### Display Device Info
Output GPU info to console at startup.

### Font

#### Runtime Generation
Use runtime font generation.

### Graphics

#### Default Texture Min Filter
Specifies which filtering to use for minification filtering.

#### Default Texture Mag Filter
Specifies which filtering to use for magnification filtering.

#### Max Draw Calls
The max number of render calls.

#### Max Characters:
The number of characters preallocated in the text rendering buffer, i.e. the number of characters that can be displayed each frame.

#### Max Font Batches
The maximum number of text batches that can be displayed each frame.

#### Max Debug Vertices
The maximum number of debug vertices. Used for physics shape rendering among other things.

#### Texture Profiles
The texture profiles file to use for this project, `/builtins/graphics/default.texture_profiles` by default.

#### Verify Graphics Calls
Verify the return value after each graphics call and report any errors in the log.

#### WebGL Version Hint
`graphics.webgl_version_hint` selects the WebGL context version to request for HTML5. Valid values are `1` (WebGL 1) and `2` (WebGL 2, the default). Set it to `1` to target or test WebGL 1 even on a browser that supports WebGL 2. Keep [Exclude GLES 2.0](#exclude-gles-20) disabled when targeting WebGL 1 so the required shaders are included.

#### OpenGL Version Hint
OpenGL context version hint. If a specific version is selected, this will be used as the minimum version required (does not apply to OpenGL ES).

#### OpenGL Core Profile Hint
Set the 'core' OpenGL profile hint when creating the context. The core profile removes all deprecated features from OpenGL, such as immediate mode rendering. Does not apply to OpenGL ES.

#### Vulkan Version Major
`graphics.vulkan_version_major` is the Vulkan context/API major version hint. This applies only when the Vulkan graphics backend is selected. The default is `1`.

#### Vulkan Version Minor
`graphics.vulkan_version_minor` is the Vulkan context/API minor version hint. This applies only when the Vulkan graphics backend is selected. The default is `0`.

### Input

#### Repeat Delay
Seconds to wait before a held down input should start repeating itself.

#### Repeat Interval
Seconds to wait between each repetition of a held down input.

#### Gamepads
File reference of the gamepads config file, which maps gamepad signals to OS, `/builtins/input/default.gamepads` by default.

#### Gamepad Database
`input.gamepad_database` selects an SDL-format gamepad mapping database (`.txt`). The default is `/builtins/input/gamecontrollerdb.txt`. Its mappings are combined with the *Gamepads* file when building the project.

#### Gamepad Deadzone
`input.gamepad_deadzone` sets the runtime dead zone applied to mappings from the SDL gamepad database. The default is `0.2`.

#### Game Binding
File reference of the input config file, which maps hardware inputs to actions, `/input/game.input_binding` by default.

#### Use Accelerometer
Check to make the engine receive accelerator input events each frame. Disabling accelerometer input may give some performance benefit.

### Network

#### Http Timeout
The HTTP timeout in seconds. Set to `0` to disable timeout.

#### Http Thread Count
The number of worker threads for the HTTP service.

#### Http Cache Enabled
Check to enable the HTTP cache for network requests (using `http.request()`. The HTTP cache will store the response associated with a request and reuse the stored response for subsequent requests. The HTTP cache supports the `ETag` and `Cache-Control: max-age` HTTP response headers.

#### SSL Certificates
File containing SSL root certificates to use when verifying the certificate chain during SSL handshakes.

### Sound

#### Gain
Global gain (volume), `0`--`1`.

#### Use Linear Gain
If enabled, gain is linear. If disabled, uses an exponential curve.

#### Max Sound Data
Max number of sound resources, i.e the number of unique sound files at runtime.

#### Max Sound Buffers
(Currently not used) Max number of concurrent sound buffers.

#### Max Sound Sources
(Currently not used) Max number of concurrently playing sounds.

#### Max Sound Instances
Max number of concurrent sound instances, i.e. actual sounds played at the same time.

#### Max Component Count
Max number of sound components per collection.

#### Sample Frame Count
Number of samples used for each audio update. 0 means automatic (1024 for 48 kHz, 768 for 44.1 kHz).

#### Use Thread
If checked, the sound system will use threads for sound playback to reduce risk of stutter when the main thread is under heavy load.

#### Stream Enabled
If checked, the sound system will use streaming to load source files.

#### Stream Cache Size
The max size of the sound chunk cache containing _all_ chunks. `2097152` bytes by default.
This number should be larger than the number of loaded sound files times the stream chunk size.
Otherwise, you risk evicting new chunks each frame.

#### Stream Chunk Size
The size in bytes of each streamed chunk.

#### Stream Preload Size
Determines the size in bytes of the initial chunk for sound files read from the archive.

### Tilemap

#### Max Count
Max number of tile maps per collection. [(See information about component max count optimizations)](#component-max-count-optimizations).

#### Max Tile Count
Max number of concurrent visible tiles per collection.

### Mesh

#### Max Count
Max number of mesh components per collection. [(See information about component max count optimizations)](#component-max-count-optimizations).

### Light

#### Max Count {#light-max-count}
`light.max_count` sets the maximum number of light components, `64` by default. [(See information about component max count optimizations)](#component-max-count-optimizations).

### Label

#### Max Count
Max number of labels. [(See information about component max count optimizations)](#component-max-count-optimizations).

#### Subpixels
Check to allow labels to appear unaligned with respect to pixels.

### Box2D

#### Velocity Iterations
Number of velocity iterations for the Box2D 2.2 physics solver.

#### Position Iterations
Number of position iterations for the Box2D 2.2 physics solver.

#### Sub Step Count
Number of sub-steps for the Box2D 3.x physics solver.

### Collection factory

#### Max Count
Max number of collection factories. [(See information about component max count optimizations)](#component-max-count-optimizations).

### iOS

#### App Icon 57x57--180x180
Image file (.png) to use as application icon at given width and height dimensions `W` &times; `H`.

#### Launch Screen
Storyboard file (.storyboard). Learn more about how to create one in the [iOS manual](https://defold.com/llms/manuals/ios.md).

#### Icons Asset
The icons asset file (.car) containing app icons.

#### Prerendered Icons
(iOS 6 and earlier) Check if your icons are prerendered. If this is unchecked the icons will get a glossy highlight added automatically.

#### Bundle Identifier
The bundle identifier lets iOS recognize any updates to your app. Your bundle ID must be registered with Apple and be unique to your app. You cannot use the same identifier for both iOS and macOS apps. Must consist of two or more segments separated by a dot. Each segment must start with a letter. Each segment must only consist of alphanumeric letters, the underscore or hyphen (-) character (see [`CFBundleIdentifier`](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-130430))

#### Bundle Name
The bundle short name (15 characters) (see [`CFBundleName`](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-130430)).

#### Bundle Version
The bundle version, either a number or x.y.z. (see [`CFBundleVersion`](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-130430))

#### Info.plist
If specified, use this *`Info.plist`* file instead of the built-in iOS base manifest when bundling your app. The built-in manifest contains the local-network and Bonjour entries needed for Editor target discovery in non-release builds. If you supply a custom manifest and need target discovery, profiling, hot reload, or log streaming on a device, preserve those entries as described in the [iOS manual](https://defold.com/llms/manuals/ios.md).

#### Privacy Manifest
The Apple Privacy Manifest for the application. The field will default to `/builtins/manifests/ios/PrivacyInfo.xcprivacy`.

#### Custom Entitlements
If specified, the entitlements in the supplied provisioning profile (`.entitlements`, `.xcent`, `.plist`) will be merged with the entitlements from the provisioning profile supplied when bundling the application.

#### Default Language
The language used if the application doesn't have user's preferred language in `Localizations` list (see [`CFBundleDevelopmentRegion`](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-130430)). Use the two-letter ISO 639-1 standard if preferred language is available there or the three-letter ISO 639-2.

#### Localizations
This field contains comma-separated strings identifying the language name or ISO language designator of the supported localizations (see [`CFBundleLocalizations`](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-109552)).

### macOS

#### App Icon
Bundle icon file (.icns) to use as application icon on macOS.

#### Info.plist
If set, use the specified info.plist file when bundling.

#### Privacy Manifest
The Apple Privacy Manifest for the application. The field will default to `/builtins/manifests/osx/PrivacyInfo.xcprivacy`.

#### Bundle Identifier
The bundle identifier lets macOS recognize updates to your app. Your bundle ID must be registered with Apple and be unique to your app. You cannot use the same identifier for both iOS and macOS apps. Must consist of two or more segments separated by a dot. Each segment must start with a letter. Each segment must only consist of alphanumeric letters, the underscore or hyphen (-) character.

#### Bundle Name {#osx-bundle-name}
`osx.bundle_name` specifies the short bundle name (`CFBundleName`), limited to 15 characters.

#### Bundle Version {#osx-bundle-version}
`osx.bundle_version` specifies the build number (`CFBundleVersion`), either a number or `x.y.z`. The default is `1`.

#### Default Language
The language used if the application doesn't have user's preferred language in `Localizations` list (see [`CFBundleDevelopmentRegion`](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-130430)). Use the two-letter ISO 639-1 standard if preferred language is available there or the three-letter ISO 639-2.

#### Localizations
This field contains comma-separated strings identifying the language name or ISO language designator of the supported localizations (see [`CFBundleLocalizations`](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-109552)).

### HTML5

Refer to the [HTML5 platform manual](https://defold.com/llms/manuals/html5.md) for more information about many of these options.

#### Heap Size
Heap size in megabytes for Emscripten to use.

#### .html Shell
Use the specified template HTML file when bundling. By default `/builtins/manifests/web/engine_template.html`.

#### Custom .css
Use the specified theme CSS file when bundling. By default `/builtins/manifests/web/light_theme.css`.

#### Splash Image
If set, use the specified splash image on startup when bundling instead of Defold logo.

#### Archive Location Prefix
When bundling for HTML5 game data is split up into one or more archive data files. When the engine starts the game, these archive files are read into memory. Use this setting to specify the location of the data.

#### Archive Location Suffix
Suffix to be appended to the archive files. Useful to, for instance, force non-cached content from a CDN (`?version2` for example).

#### Engine Arguments
List of arguments that will be passed to the engine.

#### Wasm Streaming
Enable streaming of the wasm file (faster and uses less memory, but requires the `application/wasm` MIME type).

#### Show Fullscreen Button
Enables Fullscreen Button in `index.html` file.

#### Show Made With Defold
Enables Made With Defold link in `index.html` file.

#### Show Console Banner
When enabled this option will print information about the engine and engine version in the browser console (using `console.log()`) when the engine starts.

#### Scale Mode
Specifies which method to use to scale the game canvas.

#### Retry Count
The number of retries after a failed download during startup, including network errors, failed HTTP statuses and size mismatches in the engine's JavaScript or WebAssembly file. The initial request is separate. Archive-file verification has its own retry limit; see [download verification](https://defold.com/llms/manuals/html5.md) and `Retry Time`.

#### Retry Time
The number of seconds to wait between attempts to download a file when the download failed (see `Retry Count`).

#### Verify Downloaded File Size
`html5.verify_downloaded_file_size` checks downloaded engine and archive files against their expected sizes. Enabled by default (`true`). Set it to `false` only if a server, proxy or CDN intentionally rewrites files and changes their sizes. Failed verification causes download retries before startup fails. The retry limits differ for engine downloads and archive-file verification; see [download verification](https://defold.com/llms/manuals/html5.md).

#### Transparent Graphics Context
Check if you want the graphics context to have a transparent backdrop.

### Live update

#### Enabled {#liveupdate-enabled}
`liveupdate.enabled` enables the Live update system at runtime. Enabled by default. See the [Live update manual](https://defold.com/llms/manuals/live-update.md) for how to exclude, download, and mount resources.

#### Settings
Liveupdate settings resource file to use during bundling.

### Profiler

The App Manifest **Profiler** setting controls whether profiler code is linked into debug and release builds. The settings below control the runtime behavior of profiler code that is present in the selected build. See the [Profiling manual](https://defold.com/llms/manuals/profiling.md) for details.

#### Enabled
Enable the in-game profiler.

#### Track Cpu
CPU usage sampling is enabled by default in debug builds. Enable this setting when CPU sampling is also needed in a release build that includes profiler support through the App Manifest.

#### Track Detailed Memory
`profiler.track_detailed_memory` enables detailed memory sampling in the profiler. Disabled by default. This can be expensive on HTML5.

#### Sleep Between Server Updates
Number of milliseconds to sleep between server updates.

#### Performance Timeline Enabled
Enable in-browser performance timeline (HTML5 only).

#### Max Sample Count
`profiler.max_sample_count` is the maximum number of profiler samples recorded per thread per frame. The default is `4096` and the minimum is `128`. Increase this only when a legitimate profile exceeds the limit; first check native-extension profiling code for mismatched scope begin/end calls.

---

## Setting config values on engine startup

When the engine starts, it is possible to provide config values from the command line that override the *game.project* settings:
```bash
# Specify a bootstrap collection
$ dmengine --config=bootstrap.main_collection=/my.collectionc

# Set two custom config values
$ dmengine --config=test.my_value=4711 --config=test2.my_value2=foobar
```

Custom values can---just like any other config value---be read with the matching function described under [Runtime access](#runtime-access):
```lua
local my_value = sys.get_config_number("test.my_value")
local my_value2 = sys.get_config_string("test.my_value2")
local my_flag = sys.get_config_boolean("test.my_flag", false)
```

## Component max count optimizations
The *game.project* settings file contains many values specifying the maximum number of a certain resource that can exist at the same time, often counted per loaded collection (also called world). The Defold engine will use these max values to preallocate memory for this amount of memory to avoid dynamic allocations and memory fragmentation while the game is running.

The Defold data structures used to represent components and other resources are optimized to use as little memory as possible but care should still be taken when setting the values to avoid allocating more memory than is actually necessary.

To further optimize memory usage the Defold build process will analyse the content of the game and override the max counts if it is possible to know for certain the exact amount:

* If a collection doesn't contain any factory components the exact amount of each component and Game Object will be allocated and the max count values will be ignored.
* If a collection contains a factory component the spawned objects will be analysed and the max count will be used for components that can be spawned from the factories and for Game Objects.
* If a collection contains a factory or a collection factory with activated "Dynamic Prototype" option, this collection will use the max counters.

## Custom project settings

It is possible to define custom settings for the main project or for a [native extension](https://defold.com/llms/manuals/extensions.md). Custom settings for the main project must be defined in a `game.properties` file in the project root. Files named `ext.properties` are discovered anywhere in the project and fetched library dependencies; they do not require a neighboring `ext.manifest`. All discovered extension metadata is merged, after which the root `game.properties` file is applied and can override it.

The settings file uses the same INI format as *game.project* and property attributes are defined using a dot notation with a suffix:
```
[my_category]
my_property.private = 1
...
```

The default meta file that is always applied is available [here](https://github.com/defold/defold/blob/dev/com.dynamo.cr/com.dynamo.cr.bob/src/com/dynamo/bob/meta.properties)

The following attributes are currently available:
```
[my_extension]
// `type` - used for the value string parsing
my_property.type = string // one of the following values: bool, string, number, integer, string_array, resource

// `help` - displayed as a help tooltip in the editor
my_property.help = string

// `default` - value used as default if user didn't set value manually
my_property.default = string

// `private` - private value used during the bundle process but will be removed from the bundle itself
my_property.private = 1 // boolean value 1 or 0

// `label` - editor input label
my_property.label = My Awesome Property

// `minimum` and/or `maximum` - valid range for numeric properties, validated in the editor UI
my_property.minimum = 0
my_property.maximum = 255

// `options` - drop-down choices for the editor UI, comma-separated value[:label] pairs
my_property.options = android: Android, ios: iOS

// `resource` type only:
my_property.filter = jpg,png // allowed file extensions for resource selector dialog
my_property.preserve-extension = 1 // use original resource extension instead of a built one

// deprecation
my_property.deprecated = 1 // mark property as deprecated
my_property.severity-default = warning // if deprecated property is specified, but set to a default value
my_property.severity-override = error  // if deprecated property is specified and set to a non-default value

```
Additionally, you can set the following attributes on a setting category:
```
[my_extension]
// `group` - game.project category group, e.g. Main, Platforms, Components, Runtime, Distribution
group = Runtime
// `title` - displayed category title
title = My Awesome Extension
// `help` - displayed category help
help = Settings for My Awesome Extension
```

Both Bob and the Editor parse these metadata files. The Editor uses them to create the corresponding fields, choices, validation, and help tooltips in the *game.project* viewer.