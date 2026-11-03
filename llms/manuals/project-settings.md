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

On desktop platforms, engine windows opened from the editor can restore a size saved during an earlier run. Choose `Debug ▸ Reset Simulated Resolution` to clear remembered sizes and return to the configured size while keeping saved window positions. See [engine window placement and reset](https://defold.com/llms/manuals/editor.md) for details.

#### Width
The width in pixels of the application window.

#### Height
The height in pixels of the application window.

#### High Dpi
Creates a high dpi back buffer on displays that support it. Typically the game will render in double the resolution than what is set in the *Width* and *Height* settings, which will still be the logical resolution used in scripts and properties.

On HTML5, use [Min Pixel Ratio](#min-pixel-ratio) and [Max Pixel Ratio](#max-pixel-ratio) to bound the rendering scale when this setting is enabled.

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

### Physics

#### Max Collision Object Count
Max number of collision objects.

#### Type
Which type of physics to use, `2D` or `3D`.

#### Gravity X
World gravity along x-axis. In meters per second.

#### Gravity Y
World gravity along y-axis. In meters per second.

#### Gravity Z
World gravity along z-axis. In meters per second.

#### Debug
Check if physics should be visualized for debugging.

#### Debug Alpha
Alpha component value for visualized physics, `0`--`1`.

#### World Count
Max number of concurrent physics worlds, `4` by default. If you load more than 4 worlds simultaneously through collection proxies you need to increase this value. Be aware that each physics world allocates a fair amount of memory.

#### Scale
Tells the physics engine how to scale the physics worlds in relation to the game world for numerical precision, `0.01`--`1.0`. If the value is set to `0.02`, it means that the physics engine will view 50 units as 1 meter ($1 / 0.02$).

#### Allow Dynamic Transforms
Check if the physics engine should apply the transform of a game object to any attached collision object components. This can be used to move, scale and rotate collision shapes, even those that are dynamic.

#### Use Fixed Timestep
Check if the physics engine should use fixed and framerate independent updates. Use this setting in combination with the `fixed_update(self, dt)` lifecycle function and the `engine.fixed_update_frequency` project setting to interact with the physics engine at regular intervals. For new projects the recommended setting is `true`.

#### Debug Scale
How big to draw unit objects in physics, like triads and normals.

#### Max Collisions
How many collisions that will be reported back to the scripts.

#### Max Contacts
How many contact points that will be reported back to the scripts.

#### Contact Impulse Limit
Ignore contact impulses with values less than this setting.

#### Ray Cast Limit 2d
The max number of 2d ray cast requests per frame.

#### Ray Cast Limit 3d
The max number of 3d ray cast requests per frame.

#### Trigger Overlap Capacity
The maximum number of overlapping physics triggers.

#### Velocity Threshold
Minimum velocity that will result in elastic collisions.

#### Max Fixed Timesteps
Max number of steps in the simulation when using fixed timestep (3D only).

### Shader

#### Exclude GLES 2.0
`shader.exclude_gles_sm100` excludes shaders for OpenGLES 2.0 and WebGL 1.0. Enabled by default (`1`).

To target these graphics APIs or allow fallback to them, uncheck **Shader ▸ Exclude GLES 2.0** in *game.project*, or set:
```ini
[shader]
exclude_gles_sm100 = 0
```

Projects that do not explicitly set this option use the default. Set it to `0` explicitly if the project needs OpenGLES 2.0 or WebGL 1.0 support.

#### GLSL ES Default Precision Float
`shader.glsl_es_default_precision_float` sets the default global precision qualifier for floating-point values in cross-compiled GLSL ES shaders. Valid values are `mediump` and `highp`; the default is `mediump`.

#### GLSL ES Default Precision Int
`shader.glsl_es_default_precision_int` sets the default global precision qualifier for integer values in cross-compiled GLSL ES shaders. Valid values are `mediump` and `highp`; the default is `highp`.

### Resource

#### Http Cache
If checked, a HTTP cache is enabled for faster loading of resources over the network to the running engine on device.

#### Uri
Where to find the project build data, in URI format.

#### Max Resources
The max number of resources that can be loaded at the same time.

#### Profile
`resource.profile` enables resource loading timings and INFO-level logs for each completed or failed load. Disabled by default (`0`). Enable it (`1`) before launching the game to measure startup loads. The resource profiler shows retained initial-load measurements for currently loaded resources; click **Capture**, then **Show load times** to inspect them. See [Resource loading times](https://defold.com/llms/manuals/profiling.md) for the timing columns and how to interpret them.

### Collection

#### Max Instances
Max number of game object instances in a collection, `1024` by default. [(See information about component max count optimizations)](#component-max-count-optimizations).

#### Max Input Stack Entries
Max number of game objects in the input stack.

### Sprite

#### Max Count
Max number of sprites per collection. [(See information about component max count optimizations)](#component-max-count-optimizations).

#### Subpixels
Check to allow sprites to appear unaligned with respect to pixels.

### Spine

#### Max Count
Max number of spine model components. [(See information about component max count optimizations)](#component-max-count-optimizations).

### Model

#### Max Count
Max number of model components per collection. [(See information about component max count optimizations)](#component-max-count-optimizations).

#### Split Meshes
Split meshes with more than 65536 vertices into new meshes.

#### Max Bone Matrix Texture Width
Maximum width of the bone matrix texture. Only the size needed for animations is used, rounded up to nearest power-of-two.

#### Max Bone Matrix Texture Height
Maximum height of the bone matrix texture. Only the size needed for animations is used, rounded up to nearest power-of-two.

#### Max Morph Target Texture Width
`model.max_morph_target_texture_width` sets the maximum width in pixels of the texture generated per mesh for morph target position, normal, and tangent deltas. The default is `1024`.

#### Max Morph Target Texture Height
`model.max_morph_target_texture_height` sets the maximum height in pixels of the texture generated per mesh for morph target position, normal, and tangent deltas. The default is `1024`.

### GUI

#### Max Count
Max number of GUI components. [(See information about component max count optimizations)](#component-max-count-optimizations).

#### Max Particle Count
The max number of concurrent particles in GUI.

#### Max Particlefx Count
`gui.max_particlefx_count` sets the maximum number of particle FX nodes per collection. The default is `64`.

#### Max Animation Count
The max number of active animations in gui.

#### Safe Area Mode
`gui.safe_area_mode` selects which safe-area insets affect GUI adjustment:

- `none` (default): Ignore the insets.
- `long`: Apply left/right insets in landscape and top/bottom insets in portrait.
- `short`: Apply top/bottom insets in landscape and left/right insets in portrait.
- `both`: Apply all four insets.

A GUI script can override the mode for its scene with [`gui.set_safe_area_mode()`](https://defold.com/ref/gui/#gui.set_safe_area_mode). See the [safe area guidance](https://defold.com/llms/manuals/porting-guidelines.md) for platform support and custom layouts.

### Particle FX

#### Max Count
`particle_fx.max_count` sets the maximum number of particle FX components, `64` by default. [(See information about component max count optimizations)](#component-max-count-optimizations).

#### Max Emitter Count
`particle_fx.max_emitter_count` sets the maximum number of concurrent particle FX emitters. The default is `64`.

#### Max Particle Count
The max number of concurrent particles. This limits the GPU vertex buffer size, `1024` particles by default.

#### Max Particle Buffer Count
`particle_fx.max_particle_buffer_count` sets the maximum number of particles per upload to the GPU. This limits the CPU buffer used to generate particle vertices. The default is `1024`.

### Collection proxy

#### Max Count
Max number of collection proxies. [(See information about component max count optimizations)](#component-max-count-optimizations).

### Factory

#### Max Count
Max number of game object factories. [(See information about component max count optimizations)](#component-max-count-optimizations).

### Android

#### App Icon 36x36--192x192
Image file (.png) to use as application icon at given width and height dimensions `W` &times; `H`.

#### Push Icon Small--LargeXxxhdpi
Image files (.png) to be used as custom push notification icon on Android. The icons will automatically be used for both local or remote push notifications. If not set the application icon will be used by default.

#### Push Field Title
Specifies which payload JSON field should be used as notification title. Leaving this setting empty makes the pushes default to the application name as title.

#### Push Field Text
Specifies which payload JSON field should be used as notification text. If left empty, the text in the field `alert` is used, just as on iOS.

#### Version Code
An integer value indicating the version of the app. Increase the value for each subsequent update.

#### Minimum SDK Version
The minimum API Level required for the application to run (`android:minSdkVersion`).

#### Target SDK Version
The API Level that the application targets (`android:targetSdkVersion`).

#### Package
Package identifier. Must consist of two or more segments separated by a dot. Each segment must start with a letter. Each segment must only consist of alphanumeric letters or the underscore character.

#### GCM Sender Id
Google Cloud Messaging Sender Id. Set this to the string assigned by Google to enable push notifications.

#### FCM Application Id
Firebase Cloud Messaging Application Id.

#### Manifest
If set, use the specified Android manifest XML file when bundling. A custom manifest replaces Defold's built-in base manifest. Native-extension manifest fragments are still merged into it, but later changes to the built-in base manifest are not inherited automatically, so compare custom manifests with the current built-in manifest when upgrading. For games, set `android:appCategory="game"` on the `` element. For non-game applications, set `android:appCategory` only if one of Android's defined [application categories](https://developer.android.com/guide/topics/manifest/application-element#appCategory) accurately describes the app.

#### Iap Provider
Specifies which store to use. Valid options are `Amazon` and `GooglePlay`. Refer to [extension-iap](/extension-iap/) for more information.

#### Input Method
Specifies which method to use to get keyboard input on Android devices. Valid options are `KeyEvent` (old method) and `HiddenInputField` (new).

#### Immersive Mode
If set, hides the navigation and status bars and lets your app capture all touch events on the screen.

#### Display Cutout
Extend to display cutout.

#### Debuggable
Whether or not the application can be debugged using tools such as [GAPID](https://github.com/google/gapid) or [Android Studio](https://developer.android.com/studio/profile/android-profiler). This will set the `android:debuggable` flag in the Android manifest ([official documentation](https://developer.android.com/guide/topics/manifest/application-element#debug)).

#### R8 Keep Rules
`android.r8_keep_rules` selects a `.keep` file to enable R8 shrinking, optimization and obfuscation of Java code in Android builds. Leave the setting empty to use D8 without shrinking.

With a compatible Extender build server, this also removes unused Android resources. Resources loaded dynamically may need separate [XML keep rules](https://defold.com/llms/manuals/android.md).

Select `/builtins/manifests/android/dmengine.keep` to use Defold's default rules directly. Extensions supply their own [keep rules](https://defold.com/llms/manuals/extensions.md), which are combined with this file.

Only copy the built-in file into your project if you need to add project-specific rules. Preserve the built-in rules in the copy: selecting a custom file replaces the complete project rule set.

See the [Android manual](https://defold.com/llms/manuals/android.md) for enabling R8 and retaining its obfuscation mapping with a release bundle.

#### Extract Native Libraries
Specifies whether the package installer extracts native libraries from the APK to the file system. If set to `false`, your native libraries are stored uncompressed in the APK. Although your APK might be larger, your application loads faster because the libraries load directly from the APK at runtime. This will set the `android:extractNativeLibs` flag in the Android Manifest ([official documentation](https://developer.android.com/guide/topics/manifest/application-element#extractNativeLibs)).

### Windows

#### App Icon
Image file (.ico) to use as application icon on Windows. Read more about how to create a .ico file in the [Windows manual](https://defold.com/llms/manuals/windows.md).

### IAP

#### Auto Finish Transactions
Check to automatically finish IAP transactions. If unchecked, you need to explicitly call `iap.finish()` after a successful transaction.

### Native extension

#### _App Manifest_
If set, use the app manifest to customize the engine build. This allows you to remove unused parts from the engine to decrease the final binary size. Learn how to exclude unused feature [in the application manifest manual](https://defold.com/llms/manuals/app-manifest.md).

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