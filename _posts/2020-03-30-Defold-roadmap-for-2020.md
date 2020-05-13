---
layout: text
title:  Defold roadmap for 2020
excerpt: This roadmap outlines our long-term plans for Defold.
author: Björn Ritzl
---

This roadmap outlines our long-term plans for Defold. Keep in mind that ehe list contains our **current** plans for Defold and while we do our best to plan for and work towards long-term goals the priorities may change over time and what we end up with at the end of the year may not be exactly what we had planned at the beginning of the year.

# iOS

We will continue to keep the iOS platform support up to date with the latest iOS versions and requirements. Specific iOS tasks in no particular order:

### Metal

Apple has announced that OpenGL will be deprecated on iOS and macOS, but no date has been announced. We have worked during 2019 to add a new Vulkan based graphics backend. This work is nearing completion and it will allow us to use MoltenVK on iOS and macOS. MoltenVK is a Vulkan Portability implementation. It layers a subset of the high-performance, industry-standard Vulkan graphics and compute API over Apple's Metal graphics framework, enabling Vulkan applications to run on iOS and macOS. We have worked together with members of the Khronos Group to benchmark our implementation and have received only a few points of improvement.

### Sign in with Apple

Apple will require that apps that authenticate or set up user accounts must support Sign in with Apple (SIWA). The deadline is June 30, 2020. We will release SIWA support through a native extension in Q2 of 2020. The extension has been developed at King and has already been tested in production.

### Storyboard launch screens

Apple will require that apps use Xcode storyboards as the app&rsquo;s launch screen. The deadline is June 30, 2020. We will automatically create a launch screen storyboard from the launch images set in game.project.

# Android

We will continue to keep the Android platform support up to date with the latest Android requirements. We are collaborating with the Android and Google Play partnership teams to identify important tasks. The top four tasks in order of priority are:

### Billing

Google Play Billing is a service that lets you sell digital content on Android. We will add support for the new Billing API via the existing [IAP extension](https://www.github.com/defold/extension-iap).

### Google Play Game Services

We will continue to improve on the existing [Google Play Game Services extension](https://www.github.com/defold/extension-gpgs) to ensure that it supports all of the latest features of Google Play Game Services.

### Android App Bundles

Android App Bundle is a publishing format that includes all your app&rsquo;s compiled code and resources, and defers APK generation and signing to Google Play. Google Play uses your app bundle to generate and serve optimized APKs for each device configuration, so only the code and resources that are needed for a specific device are downloaded to run your app. We will initially add support for basic bundling of applications using Android App Bundles and then expand upon the feature as needed.

### Google Play Instant

Google Play Instant enables native games to launch on devices running Android 5.0 (API level 21) or higher without being installed. By allowing users to run an instant game, known as providing an instant experience, you improve your game's discovery, which helps drive more active users or installations.

# HTML5

We will focus on increased performance and reduced application size on HTML5. We will when possible update to newer versions of Emscripten and WebAssembly to achieve this.

# Desktop

On desktop our only identified focus area is to add the ability to run the engine loop while the window is in the background.

# Editor

We will mainly focus on performance and stability improvements in the editor. In terms of new features we have identified the following (in no particular order):

### Improved 3D support

In 2019 we added support for perspective cameras and made some improvements to how collision shapes were visualised. These changes made it easier to work with and place 3D models in a collection, but there are still many improvements to be made to scene navigation when working in a 3D.

### Auto-tiling

While we did some minor improvements to the tilemap system in 2019 (better tile palette and interleaved layers) we have so far left out auto-tiling. Auto-tiling can really speed up tilemap editing and it is the next big feature to add for the tilemap editor.

### Editor extensions

We plan to expand the existing system for editor scripts to allow for more complex operations and we will look at how to customize the UI and/or add new UI widgets using editor scripts.

### GUI layouts and templates

The system with GUI layouts and templates where one or both involve value overrides is fairly complex and hard to work with from a code maintenance perspective. We plan to review the system and possibly simplify it.

# Engine

In 2019 we made several changes to improve editor stability. Two examples of this were reduced ANRs on Android and a standardized application loop on iOS. In 2020 we will continue to identify and fix stability issues in the engine. Besides stability improvements we will also work on the following features (in no particular order):

### Sound threading

Sound playback is currently done on the main thread together with the rest of the game loop. This can become a problem if loading large resources while playing sound, resulting in playback stutter. The solution is to do sound playback on a separate thread to avoid stutter when loading content.

### Physics decoupling

Physics is currently running at the same rate as the rest of the game loop. We will try to decouple the physics simulation from the game loop by running the simulation on a separate thread and optionally with a different number of updates per second.

### Spine as an extension

We will look into the possibility of using the official Spine runtime as an extension and a replacement for the existing custom made native Spine support. This will allow the use of newer versions of Spine, something that currently is not possible with the existing and custom Spine runtime.

### Physics as an extension

We will look into the possibility of moving the Box2D and Bullet3D physics engines to a native extension. This will allow the community to update or replace the physics simulation with an update version or completely different implementation.

### Live update

We're very happy to see that the live update functionality is used in several different scenarios (from Android Expansion Files to Steam DLCs). We have with the help of the community identified several improvements and we plan to deliver the most critical improvements in 2020.

### Mesh component

The custom mesh component will be released in Q2 of 2020.

### Vulkan

We will release support for Vulkan on all systems where it is supported. On Android it will be used by default on newer devices. On iOS it will be used under the hood to be able to use MoltenVK (see iOS above).

# Build server

The Defold build server for native extensions will be open sourced in Q2 of 2020 to allow developers to build locally or set up their own build servers to cut the dependency to the Defold provided build service.
