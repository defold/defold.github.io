# macOS development {#manuals:macos}

Developing Defold applications for the macOS platform is a straight forward process with very few considerations to make.

## Project settings

macOS specific application configuration is done from the [macOS section](https://defold.com/llms/manuals/project-settings.md) of the *game.project* settings file.

## Application icon

The application icon used for a macOS game must be in the .`icns` format. You can easily create a `.icns` file from a set of `.png` files collected as a `.iconset`. Follow the [official instructions for creating a `.icns` file](https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/HighResolutionOSX/Optimizing/Optimizing.html). Brief summary of the steps involved are:

* Create a folder for the icons, e.g. `game.iconset`
* Copy icon files to the created folder:

    * `icon_16x16.png`
    * `icon_16x16@2x.png`
    * `icon_32x32.png`
    * `icon_32x32@2x.png`
    * `icon_128x128.png`
    * `icon_128x128@2x.png`
    * `icon_256x256.png`
    * `icon_256x256@2x.png`
    * `icon_512x512.png`
    * `icon_512x512@2x.png`

* Convert the `.iconset` folder to a `.icns` file using the `iconutil` command line tool:
```
iconutil -c icns -o game.icns game.iconset
```

## Publishing your application
You can publish your application to the Mac App Store, using a 3rd party store or portal such as Steam or itch.io or on your own through a website. Before publishing your application you need to prepare it for submission. The following steps are required regardless of how you intend to distribute the application:

* 1) Make sure that anyone is able to run your game by adding the execute permissions (the default is that only the file owner has execute permissions):
```
$ chmod +x Game.app/Contents/MacOS/Game
```

* 2) Create an entitlements file specifying the permissions required by your game. For most games the following permissions are enough:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>com.apple.security.cs.allow-jit</key>
    <true/>
    <key>com.apple.security.cs.allow-unsigned-executable-memory</key>
    <true/>
    <key>com.apple.security.cs.allow-dyld-environment-variables</key>
    <true/>
  </dict>
</plist>
```

  * `com.apple.security.cs.allow-jit` - Indicates whether the app may create writable and executable memory using the MAP_JIT flag
  * `com.apple.security.cs.allow-unsigned-executable-memory` - Indicates whether the app may create writable and executable memory without the restrictions imposed by using the MAP_JIT flag
  * `com.apple.security.cs.allow-dyld-environment-variables` - Indicates whether the app may be affected by dynamic linker environment variables, which you can use to inject code into your app’s process

Some applications may also need additional entitlements. The Steamworks extension needs this extra entitlement:
```
<key>com.apple.security.cs.disable-library-validation</key>
<true/>
```

    * `com.apple.security.cs.disable-library-validation` - Indicates whether the app may load arbitrary plug-ins or frameworks, without requiring code signing.

All of the entitlements that can be granted to an application are listed in the official [Apple developer documentation](https://developer.apple.com/documentation/bundleresources/entitlements).

* 3) Sign your game using `codesign`:
```
$ codesign --force --sign "Developer ID Application: Company Name" --options runtime --deep --timestamp --entitlements entitlement.plist Game.app
```

## Publishing outside the Mac App Store
Apple requires all software distributed outside the Mac App Store to be notarized by Apple in order to run by default on macOS Catalina. Refer to the [official documentation](https://developer.apple.com/documentation/xcode/notarizing_macos_software_before_distribution/customizing_the_notarization_workflow) to learn how to add notarization to a scripted build environment outside of Xcode. Brief summary of the steps involved are:

* 1) Follow the above steps of adding permissions and signing the application.

* 2) Zip and upload your game for notarization using `altool`.
```
$ xcrun altool --notarize-app
               --primary-bundle-id "com.acme.foobar"
               --username "AC_USERNAME"
               --password "@keychain:AC_PASSWORD"
               --asc-provider <ProviderShortname>
               --file Game.zip

altool[16765:378423] No errors uploading 'Game.zip'.
RequestUUID = 2EFE2717-52EF-43A5-96DC-0797E4CA1041
```

* 3) Check the status of your submission using the returned request UUID from the call to `altool --notarize-app`:
```
$ xcrun altool --notarization-info 2EFE2717-52EF-43A5-96DC-0797E4CA1041
               -u "AC_USERNAME"
```

* 4) Wait until the status becomes `success` and staple the notarization ticket to the game:
```
$ xcrun stapler staple "Game.app"
```

* 5) Your game is now ready for distribution.

## Publishing to the Mac App Store
The process when publishing to the Mac App Store is well documented in the [Apple Developer documentation](https://developer.apple.com/macos/submit/). Make sure to add permissions and codesign the application as described above before submitting.

Note: The game does not have to be notarized when publishing to the Mac App Store.

## Apple Privacy Manifest

The privacy manifest is a property list that records the types of data collected by your app or third-party SDK, and the required reasons APIs your app or third-party SDK uses. For each type of data your app or third-party SDK collects and category of required reasons API it uses, the app or third-party SDK needs to record the reasons in its bundled privacy manifest file.

Defold provides a default privacy manifest through the Privacy Manifest field in the *game.project* file. When creating an application bundle the privacy manifest will be merged with any privacy manifests in the project dependencies and included in the application bundle.

Read more about privacy manifests in the [official documentation from Apple](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files?language=objc).