---
brief: This manual covers how to use the camera on macOS, iOS and Android in Defold.
github: https://github.com/defold/extension-camera
language: en
layout: manual
title: Defold camera extension API documentation
toc:
- Defold camera extension API documentation
- Installation
- Example
- FAQ
- How do I reset macOS camera permission?
- Source code
---

# Defold camera extension API documentation

This extension provides a unified, simple to use interface to capture images using the camera on macOS, iOS and Android.


## Installation
To use this library in your Defold project, add the following URL to your `game.project` dependencies:

https://github.com/defold/extension-camera/archive/master.zip

We recommend using a link to a zip file of a [specific release](https://github.com/defold/extension-camera/releases).


## Example

Refer to the [example project](https://github.com/defold/extension-camera/blob/master/main/main.script).


## FAQ

### How do I reset macOS camera permission?

To test macOS camera permission popup multiple times you can reset the permission from the terminal:

```bash
tccutil reset Camera
```


## Source code

The source code is available on [GitHub](https://github.com/defold/extension-camera)
## API reference
[API Reference - camera](/extension-camera/camera_api)
