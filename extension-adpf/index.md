---
layout: manual
language: en
github: https://github.com/defold/extension-adpf
title: Android Device Performance Framework extension for Defold
brief: This manual covers how to use the Android Device Performance Framework in Defold
---

# Android Device Performance Framework extension for Defold

Android Dynamic Performance Framework (ADPF) is a set of APIs that allow games and to interact more directly with power and thermal systems of Android devices. It is possible to monitor the dynamic behavior on Android systems and optimize game performance at a sustainable level that doesn't overheat devices.

This extension currently support the following ADPF features:

* [Performance Hint API](https://developer.android.com/games/optimize/adpf/performance-hint-api)
* [Thermal API](https://developer.android.com/games/optimize/adpf/thermal)


## Installation
To use ADPF in your Defold project, add a version of the ADPF extension to your `game.project` dependencies from the list of available [Releases](https://github.com/defold/extension-adpf/releases). Find the version you want, copy the URL to ZIP archive of the release and add it to the project dependencies.

![](add-dependency.png)

Select `Project->Fetch Libraries` once you have added the version to `game.project` to download the version and make it available in your project.


## Usage

### Performance Hint API

With CPU performance hints, a game can influence dynamic CPU performance behavior to better match its needs. On most devices, Android dynamically adjusts the CPU clock speed and core type for a workload based on the previous demands. If a workload uses more CPU resources, the clock speed is increased and the workload is eventually moved to a larger core. If the workload uses less resources, then Android lowers resource allocation. With ADPF, the application or game can send an additional signal about its performance and deadlines. This helps the system ramp up more aggressively (improving performance) and lower the clocks quickly when the workload is complete (saving power usage).

The extension will create a `PerformanceHintManager` instance and a `PerformanceHintManager.Session` instance for the main thread only. The Defold extension system currently doesn't allow extensions to list and measure threads which the engine creates, for instance the audio and network threads.

```lua

-- initialize performance hint manager with a target FPS in nanosecond (60 fps)
local available = adpf.hint.init((1 / 60) * 1000 * 1000)

-- update target FPS for the performance hint manager (30 fps)
adpf.hint.update_target_fps((1 / 30) * 1000 * 1000)

-- the extension will automatically report actual work duration each frame
```


### Thermal API

The potential performance of your app is limited by the thermal state of the device, which can vary based on characteristics such as weather, recent usage, and the device's thermal design. Devices can only maintain a high level of performance for a limited amount of time before being thermally throttled. A key goal of your implementation should be to achieve performance goals without exceeding thermal limitations. Thermal API makes it possible without the need for device specific optimizations. Furthermore, when debugging performance issues, knowing if the thermal state of your device is limiting performance is important.

You can monitor the thermal state of the device by polling the `adpf.thermal.get_headroom()` function. This function predicts how long the device can maintain the current performance level without overheating. If the time is less than the amount needed to run the workload, then your game should decrease the workload to a sustainable level. For example, the game can reduce the frame rate using `adpf.hint.update_target_fps()`, or lower graphics fidelity.


```lua
-- initialize the extension to use the Thermal API
local available = adp.thermal.init()
if not available then
    print("Thermal API is not available")
    return
end

-- get thermal status
local status = adpf.thermal.get_status()

-- get thermal headroom forecast for 3 seconds ahead
local headroom = adpf.thermal.get_headroom(3)
```



## Example

[Refer to the example project](https://github.com/defold/extension-adpf/blob/master/example/example.script) to see a complete example of how the intergation works.


## Source code

The source code is available on [GitHub](https://github.com/defold/extension-adpf)


## API reference
[API Reference - adpf](/extension-adpf/adpf_api)
