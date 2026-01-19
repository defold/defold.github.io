# Android development {#manuals:android}

Android devices allows you to freely run your own apps on them. It is very easy to build a version of your game and copy it onto an Android device. This manual explains the steps involved in bundling your game for Android. During development, running your game through the [development app](dev-app.md) is often preferred since it allows you to hot reload content and code directly to your device.

## Android and Google Play signing process

Android requires that all APKs be digitally signed with a certificate before they are installed on a device or updated. If you use Android App Bundles, you need to sign only your app bundle before you upload it to the Play Console, and [Play App Signing](https://developer.android.com/studio/publish/app-signing#app-signing-google-play) takes care of the rest. However, you can also manually sign your app for upload to Google Play, other app stores and for distribution outside of any store.

When you create an Android application bundle from the Defold editor or the [command line tool](bob.md) you can provide a keystore (containing your certificate and key) and keystore password which will be used when signing your application. If you don't, Defold generates a debug keystore and uses it when signing the application bundle.

You should **never** upload your application to Google Play if it was signed using a debug keystore. Always use a dedicated keystore which you have created yourself.

## Creating a keystore

The Android signing process in Defold changed in version 1.2.173 from using a stand-alone key and certificate to a keystore. [More information in this forum post](https://forum.defold.com/t/upcoming-change-to-the-android-build-pipeline/66084).

You can create a keystore [using Android Studio](https://developer.android.com/studio/publish/app-signing#generate-key) or from a terminal/command prompt:
```bash
keytool -genkey -v -noprompt -dname "CN=John Smith, OU=Area 51, O=US Air Force, L=Unknown, ST=Nevada, C=US" -keystore mykeystore.keystore -storepass 5Up3r_53cR3t -alias myAlias -keyalg RSA -validity 9125
```

This will create a keystore file named `mykeystore.keystore` containing a key and certificate. Access to key and certificate will be protected by the password `5Up3r_53cR3t`. The key and certificate will be valid for 25 years (9125 days). The generated key and certificate will be identified by the alias `myAlias`.

Make sure to store the keystore and associated password somewhere safe. If you sign and upload your applications to Google Play yourself and the keystore or keystore password is lost there is no way for you to update the application on Google Play. You can avoid this by using Google Play App Signing and let Google sign your applications for you.

## Creating an Android application bundle

The editor lets you easily create a stand alone application bundle for your game. Before bundling you can specify what icon(s) to use for the app, set version code etc in the *game.project* [project settings file](project-settings.md).

To bundle select `Project ▸ Bundle... ▸ Android Application...` from the menu.

If you want the editor to automatically create random debug certificates, leave the *Keystore* and *Keystore password* fields empty:

If you want to sign your bundle with a particular keystore, specify the *Keystore* and *Keystore password*. The *Keystore* is expected to have the `.keystore` file extension while the password is expected to be stored in a text file with the `.txt` extension. It is also possible to specify a *Key password* if the key in the keystore uses a different password than the keystore itself:

Defold supports the creation of both APK and AAB files. Select APK or AAB from the Bundle Format drop down.

Press `Create Bundle` when you have configured the application bundle settings. You will then be prompted to specify where on your computer the bundle will be created.

## Build variants

When you bundle a game, you need to choose what type of engine you wish to use. You have three basic options:

  * Debug
  * Release
  * Headless

These different versions are also referred to as `Build variants`

When you choose `Project ▸ Build` you'll always get the debug version.

### Debug

This type of executable is typically used during development of a game as it has several useful debugging features included:

* Profiler - Used for gathering performance and usage counters. Learn how to use the profiler in the [Profiling manual](profiling.md).
* Logging - The engine will log system information, warnings and errors when logging is enabled. The engine will also output logs from the Lua `print()` function and from native extensions logging using `dmLogInfo()`, `dmLogError()` and so on. Learn how to read these logs in the [Game and System Logs manual](debugging-game-and-system-logs.md).
* Hot reload - Hot-reload is a powerful feature which lets a developer reload resource while the game is running. Learn how to use this in the [Hot-Reload manual](hot-reload.md).
* Engine services - It is possible to connect to and interact with a debug version of a game through a number of different open TCP ports and services. The services include the hot-reload feature, remote log access and the profiler mentioned above, but also other services to remotely interact with the engine. Learn more about the engine services [in the developer documentation](https://github.com/defold/defold/blob/dev/engine/docs/DEBUG_PORTS_AND_SERVICES.md).

### Release

This variant has the debugging features disabled. This options should be chosen when the game is ready to be released to the app store or in other ways shared with players. It is not recommended to release a game with the debugging features enabled for a number of reasons:

* The debugging features take up a little bit of size in the binary, and [it is a best practice to try to keep the binary size of a released game as small as possible](optimization.md).
* The debugging features takes a little bit of CPU time as well. This can impact the performance of the game if a user has a low-end hardware. On mobile phones the increased CPU usage will also contribute to heating and battery drain.
* The debugging features may expose information about the game that is not intended for the eyes of the players, either from a security, cheating or fraud perspective.

### Headless

This executable runs without any graphics and sound. It means that you can run the game unit/smoke tests on a CI server, or even have it as a game server in the cloud.

### Installing an Android application bundle

#### Installing an APK

An *`.apk`* file can be copied to your device with the `adb` tool, or to Google Play via the [Google Play developer console](https://play.google.com/apps/publish/).

The `adb` command line tool is an easy to use and versatile program that is used to interact with Android devices. You can download and install `adb` as part of the Android SDK Platform-Tools, for Mac, Linux or Windows.

Download the Android SDK Platform-Tools from: https://developer.android.com/studio/releases/platform-tools. You find the *adb* tool in */platform-tools/*. Alternatively, platform specific packages can be installed through respective package managers.

On Ubuntu Linux:
```
$ sudo apt-get install android-tools-adb
```

On Fedora 18/19:
```
$ sudo yum install android-tools
```

On macOS (Homebrew)
```
$ brew cask install android-platform-tools
```

You can verify that `adb` works by connecting your Android device to your computer via USB and issue the following command:
```
$ adb devices
List of devices attached
31002535c90ef000    device
```

If your device does not show up, verify that you have enabled *USB debugging* on the Android device. Open the device *Settings* and look for *Developer options* (or *Development*).

```
$ adb install Defold\ examples.apk
4826 KB/s (18774344 bytes in 3.798s)
  pkg: /data/local/tmp/my_app.apk
Success
```

#### Installing an APK using editor

You can install and launch an *`.apk`* file using the editor's "Install on connected device" and "Launch installed app" check-boxes in the Bundle dialog:

For this feature to work, you will need ADB installed and *USB debugging* enabled on the connected device. If the editor can't detect the install location of the ADB command line tool, you will need to specify it in [Preferences](editor-preferences.md).

#### Installing an AAB

An *.aab* file can be uploaded to Google Play via the [Google Play developer console](https://play.google.com/apps/publish/). It is also possible to generate an *`.apk`* file from an *.aab* file to install it locally using the [Android bundletool](https://developer.android.com/studio/command-line/bundletool).

## Permissions

The Defold engine requires a number of different permissions for all engine features to work. The permissions are defined in the `AndroidManifest.xml`, specified in the *game.project* [project settings file](project-settings.md). You can read more about Android permissions in [the official docs](https://developer.android.com/guide/topics/permissions/overview). The following permissions are requested in the default manifest:

### android.permission.INTERNET and android.permission.ACCESS_NETWORK_STATE (Protection level: normal)
Allows applications to open network sockets and access information about networks. These permission are needed for internet access. ([Android official docs](https://developer.android.com/reference/android/Manifest.permission#INTERNET)) and ([Android official docs](https://developer.android.com/reference/android/Manifest.permission#ACCESS_NETWORK_STATE)).

### android.permission.WAKE_LOCK (Protection level: normal)
Allows using PowerManager WakeLocks to keep processor from sleeping or screen from dimming. This permission is needed to temporarily prevent the device from sleeping while receiving a push notification. ([Android official docs](https://developer.android.com/reference/android/Manifest.permission#WAKE_LOCK))

## Using AndroidX
AndroidX is a major improvement to the original Android Support Library, which is no longer maintained. AndroidX packages fully replace the Support Library by providing feature parity and new libraries. Most of the Android extensions in the [Asset Portal](https://defold.com/assets) support AndroidX. If you do not wish to use AndroidX you can explicitly disable it in favour of the old Android Support Library by checking the `Use Android Support Lib` in the [application manifest](app-manifest.md).

## FAQ
#### Q: Is it possible to hide the navigation and status bars on Android?
A: Yes, set the *immersive_mode* setting in the *Android* section of your *game.project* file. This lets your app take over the whole screen and capture all touch events on the screen.

#### Q: Why am I'm getting "Failure [INSTALL_PARSE_FAILED_INCONSISTENT_CERTIFICATES]" when installing a Defold game on device?
A: Android detects that you try to install the app with a new certificate. When bundling debug builds, each build will be signed with a temporary certificate. Uninstall the old app before installing the new version:
```
$ adb uninstall com.defold.examples
Success
$ adb install Defold\\ examples.apk
4826 KB/s (18774344 bytes in 3.798s)
      pkg: /data/local/tmp/Defold examples.apk
Success
```

#### Q: Why am I getting errors about conflicting properties in AndroidManifest.xml when building with certain extensions?
A: This can happen when two or more extensions provide an Android Manifest stub containing the same property tag but with different values. This has for instance happened with Firebase and AdMob. The build error looks similar to this:
```
SEVERE: /tmp/job4531953598647135356/upload/AndroidManifest.xml:32:13-58
Error: Attribute property#android.adservices.AD_SERVICES_CONFIG@resource
value=(@xml/ga_ad_services_config) from AndroidManifest.xml:32:13-58 is also
present at AndroidManifest.xml:92:13-59 value=(@xml/gma_ad_services_config).
Suggestion: add 'tools:replace="android:resource"' to <property> element at
AndroidManifest.xml to override.
```

You can read more about the issue and the workaround in reported Defold issue [#9453](https://github.com/defold/defold/issues/9453#issuecomment-2367367269) and Google issue [#327696048](https://issuetracker.google.com/issues/327696048?pli=1).