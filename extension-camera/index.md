---
layout: manual
language: en
github: https://github.com/defold/extension-camera
title: Defold camera extension API documentation
brief: This manual covers how to use the camera on macOS, iOS and Android in Defold.
---

# Defold camera extension API documentation

This extension provides a unified, simple to use interface to capture images using the camera on macOS, iOS and Android.


## Installation
To use this library in your Defold project, add the following URL to your `game.project` dependencies:

https://github.com/defold/extension-camera/archive/master.zip

We recommend using a link to a zip file of a [specific release](https://github.com/defold/extension-camera/releases).


## Configuration
The extension can be configured by adding the following fields to game.project:

```
[adinfo]
tracking_usage_description = We would like to show you relevant ads.
register_for_attribution = 1
```

### tracking_usage_description

Before requesting advertising info and status on iOS 14 the application must request user authorization to access app-related data for tracking the user or the device. This is done automatically when `adinfo.get()` is called. The string set in `adinfo.tracking_usage_description` will be shown to the user.

Apple documentation: https://developer.apple.com/documentation/apptrackingtransparency?language=objc

### register_for_attribution

The extension can automatically register the application for ad network attribution using `SkAdNetwork` and the `registerAppForAdNetworkAttribution()` function. Enable this functionality by setting `adinfo.register_for_attribution` to 1 in game.project.

Apple documentation: https://developer.apple.com/documentation/storekit/skadnetwork


## Example

```lua
function init(self)
    adinfo.get(function(self, info)
      print(info.ad_ident, info.ad_tracking_enabled)
    end)
end
```

## FAQ

### How do I reset macOS camera permission?

To test macOS camera permission popup multiple times you can reset the permission from the terminal:

```bash
tccutil reset Camera
```


## Source code

The source code is available on [GitHub](https://github.com/defold/extension-adinfo)


## API reference
[API Reference](/extension-camera/api)