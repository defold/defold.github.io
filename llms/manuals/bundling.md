# Bundling an application {#manuals:bundling}

While developing your application you should make a habit of testing the game on the target platforms as often as possible. You should do this to detect performance issues early on in the development process where these things are much easier to fix. It is also recommended to test on all target platforms to find discrepancies in things such as shaders. When developing on mobile you have the option to use the [mobile development app](dev-app.md) to push content to the app, instead of having to do a full bundle and uninstall/install cycle.

You can create an application bundle for all platforms that Defold supports from within the Defold editor itself, with no external tools needed. You can also bundle from the command line using our command line tools. Application bundling requires a network connection if your project contains one or more [native extensions](extensions.md).

## Bundling from within the editor

You create an application bundle from the Project menu and Bundle option:

Selecting any of the menu options will bring up the Bundle dialog for that specific platform.

### Build reports

When bundling your game there is an option to create a build report. This is very useful to get a grip on the size of all the assets that are part of your game bundle. Simply check the *Generate build report* checkbox when bundling the game.

To learn more about build reports please refer to the [Profiling manual](profiling.md).

### Android

Creating an Android application bundle (.apk file) is documented in the [Android manual](android.md).

### iOS

Creating an iOS application bundle (.ipa file) is documented in the [iOS manual](ios.md).

### macOS

Creating a macOS application bundle (.app file) is documented in the [macOS manual](macos.md).

### Linux

Creating a Linux application bundle requires no specific setup and no optional platform specific configuration in the *game.project* [project settings file](project-settings.md).

### Windows

Creating a Windows application bundle (.exe file) is documented in the [Windows manual](windows.md).

### HTML5

Creating an HTML5 application bundle as well as optional setup is documented in the [HTML5 manual](html5.md).

#### Facebook Instant Games

It is possible to create a special version of an HTML5 application bundle specifically for Facebook Instant Games. This process is documented in the [Facebook Instant Games manual](instant-games.md).

## Bundling from the command line

The editor uses our command line tool [Bob](bob.md) to bundle the application.

While doing day to day development of your application it is likely that you build and bundle from within the Defold editor. In other circumstances you may wish to automatically generate application bundles, for instance batch building for all targets when releasing a new version or when creating nightly builds of the latest version of the game, perhaps in a CI environment. Building and bundling of an application can be done outside the normal editor workflow using the [Bob command line tool](bob.md).

## The bundle layout

The logical bundle layout is structured like this:

A bundle is output into a folder. Depending on platform, that folder may also be zip archived into an `.apk` or `.ipa`.
The contents of the folder depends on the platform.

Apart from the executable files, our bundling process also collects the required assets for the platform (e.g. the .xml resource files for Android).

Using the [bundle_resources](project-settings.md) setting, you can configure assets that should be placed within the bundle as-is.
You can control this per platform.

The game assets are located in the `game.arcd` file, and they are individually compressed using LZ4 compression.
Using the [custom_resources](project-settings.md) setting, you can configure assets that should be placed (with compression) within the `game.arcd`.
These assets can be accessed via the [`sys.load_resource()`](https://defold.com/ref/sys/#sys.load_resource) function.

## Release vs Debug

When creating an application bundle you have an option of creating a debug or release bundle. The differences between the two bundles are small but important to keep in mind:

* Release builds do not include the [profiler](profiling.md)
* Release builds do not include the [screen recorder](https://defold.com/ref/stable/sys/#start_record)
* Release builds do not show the output of any calls to `print()` or the output from any native extensions
* Release builds have the `is_debug` value in `sys.get_engine_info()` set to`false`
* Release builds will not do reverse lookups of `hash` values when calling `tostring()`. What this means in practice is that a `tostring()` for a value of type `url` or `hash` will return its numeric representation and not the original string (`'hash: [/camera_001]'` vs `'hash: [11844936738040519888 (unknown)]'`)
* Release builds do not support targeting from the editor for [hot-reload](hot-reload.md) and similar functionality