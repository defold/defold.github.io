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

It is possible to read any value from *game.project* at runtime using [`sys.get_config_string(key)`](https://defold.com/ref/sys/#sys.get_config_string), [`sys.get_config_number(key)`](https://defold.com/ref/sys/#sys.get_config_number) and [`sys.get_config_int(key)`](https://defold.com/ref/sys/#sys.get_config_int). Examples:
```lua
local title = sys.get_config_string("project.title")
local gravity_y = sys.get_config_number("physics.gravity_y")
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

#### Custom Resources
`custom_resources`
Custom resources are bundled in the main game archive using the [*Custom Resources* field](https://defold.com/llms/manuals/project-settings.md) in *game.project*.

The *Custom Resources* field should contain a comma separated list of resources that will be included in the main game archive. If directories are specified, all files and directories in that directory are recursively included. You can read the files using [`sys.load_resource()`](https://defold.com/ref/sys/#sys.load_resource).

Loading custom resources is covered in more detail in the [File Access manual](https://defold.com/llms/manuals/file-access.md).

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

You can use [`sys.get_application_path()`](https://defold.com/ref/stable/sys/#sys.get_application_path:) to get the path to where the application is stored. Use this application base path to create the final absolute path to the files you need access to. Once you have the absolute path of these files you can use the `io.*` and `os.*` functions to access the files.

Loading bundle resources is covered in more detail in the [File Access manual](https://defold.com/llms/manuals/file-access.md).

#### Bundle Exclude Resources
`bundle_exclude_resources`
A comma separated list of resources that should not be included in the bundle. That is, they're removed from the result of the collection of the `bundle_resources` step.

### Library

#### Include Dirs
A space separated list of directories that should be shared from your project via library sharing. Refer to the [Libraries manual](https://defold.com/llms/manuals/libraries.md) for more information.

### Engine

#### Run While Iconified
Allow the engine to continue running while the application window is iconified (desktop platforms only).

#### Fixed Update Frequency
The update frequency of the `fixed_update(self, dt)` lifecycle function. In Hertz.

#### Max Time Step
If the time step becomes too large during a single frame, it will be capped to this max value. Seconds.

### Render

#### Clear Color Red
Clear color red channel, used by the render script and when the window is created.

#### Clear Color Green
Clear color green channel, used by the render script and when the window is created.

#### Clear Color Blue
Clear color blue channel, used by the render script and when the window is created.

#### Clear Color Alpha
Clear color alpha channel, used by the render script and when the window is created.

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
Don't compile shaders for devices running OpenGLES 2.0 / WebGL 1.0.

### Resource

#### Http Cache
If checked, a HTTP cache is enabled for faster loading of resources over the network to the running engine on device.

#### Uri
Where to find the project build data, in URI format.

#### Max Resources
The max number of resources that can be loaded at the same time.

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
If specified, use this *`info.plist`* file when bundling your app.

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
The number of attempts to download a file when the engine starts (see `Retry Time`).

#### Retry Time
The number of seconds to wait between attempts to download a file when the download failed (see `Retry Count`).

#### Transparent Graphics Context
Check if you want the graphics context to have a transparent backdrop.

### Live update

#### Settings
Liveupdate settings resource file to use during bundling.

#### Mount On Start
Enables auto-mount of previously mounted resources when the application starts.

### Profiler

#### Enabled
Enable the in-game profiler.

#### Track Cpu
If checked, enable CPU profiling in release versions of the builds. Normally, you can only access profiling information in debug builds.

#### Sleep Between Server Updates
Number of milliseconds to sleep between server updates.

#### Performance Timeline Enabled
Enable in-browser performance timeline (HTML5 only).

---

## Setting config values on engine startup

When the engine starts, it is possible to provide config values from the command line that override the *game.project* settings:
```bash
# Specify a bootstrap collection
$ dmengine --config=bootstrap.main_collection=/my.collectionc

# Set two custom config values
$ dmengine --config=test.my_value=4711 --config=test2.my_value2=foobar
```

Custom values can---just like any other config value---be read with [`sys.get_config_string()`](https://defold.com/ref/sys/#sys.get_config_string) or [`sys.get_config_number()`](https://defold.com/ref/sys/#sys.get_config_number):
```lua
local my_value = sys.get_config_number("test.my_value")
local my_value2 = sys.get_config_string("test.my_value2")
```

## Component max count optimizations
The *game.project* settings file contains many values specifying the maximum number of a certain resource that can exist at the same time, often counted per loaded collection (also called world). The Defold engine will use these max values to preallocate memory for this amount of memory to avoid dynamic allocations and memory fragmentation while the game is running.

The Defold data structures used to represent components and other resources are optimized to use as little memory as possible but care should still be taken when setting the values to avoid allocating more memory than is actually necessary.

To further optimize memory usage the Defold build process will analyse the content of the game and override the max counts if it is possible to know for certain the exact amount:

* If a collection doesn't contain any factory components the exact amount of each component and Game Object will be allocated and the max count values will be ignored.
* If a collection contains a factory component the spawned objects will be analysed and the max count will be used for components that can be spawned from the factories and for Game Objects.
* If a collection contains a factory or a collection factory with activated "Dynamic Prototype" option, this collection will use the max counters.

## Custom project settings

It is possible to define custom settings for the main project or for a [native extension](https://defold.com/llms/manuals/extensions.md). Custom settings for the main project must be defined in a `game.properties` file in the root of the project. For a native extension they should be defined in an `ext.properties` file next to the `ext.manifest` file.

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

// `help` - used as help tip in the editor (not used for now)
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

At the moment meta properties are used only in `bob.jar` when bundling application, but later will be parsed by the editor and represented in the *game.project* viewer.