---
layout: post
title:  A first look at the Defold 2021 roadmap
excerpt: In this post we'll go through the Defold roadmap for 2021.
author: Björn Ritzl
tags: ["roadmap", "news"]
---

This roadmap outlines our plans for Defold in 2021. The contents of the roadmap is based on input from several stakeholders:

* **Platforms providers** - What are the upcoming requirements from Google, Apple and other platforms?
* **Corporate partners** - What are the needs of our corporate partners?
* **Community requests** - What are the most important requests from our community of developers?
* **Defold vision** - What is the Defold Foundation's vision and goals for Defold?

Keep in mind that the list contains our **current** plans for Defold and while we do our best to plan for and work towards long-term goals the priorities may change over time and what we end up with at the end of the year may not be exactly what we had planned at the beginning of the year. The [roadmap is available on GitHub](https://github.com/defold/defold/projects/46) and will be kept updated throughout the year. Also note that we will work on additional smaller tasks as well as bug fixes and maintenance throughout the year. The 2021 roadmap can be divided into four main areas:

* **Platforms**
* **Extensions**
* **Stability and performance**
* **New features**


## Platforms
Developing a cross platform game engine usually means working with several constantly evolving platforms, each with its own requirements and restrictions. This is especially true on mobile, but also to some extent on the web and desktop. Consoles on the other hand are thankfully almost entirely static and unchanging. Each year we must pay attention to the new iOS and Android platform releases and make sure Defold works well and is kept up to date with latest requirements. This year is no different.

### Android
On Android we will make sure to be compliant with the latest Android version (12, planned for release sometime in Q2) and also make sure we target at least Android API level 30 which will be a requirement in August of 2021. On Android we'll also upgrade our build tools and migrate from dx to d8. Finally we also aim to deliver support for Play Asset Delivery as a new way to distribute Defold Live Update content to an installed Defold game.

### iOS
On iOS we will upgrade to iOS 15 when it is released (usually announced at WWDC in June and released a few months later). We will also look into recent problems running Defold applications on the iOS Simulator in Xcode.

### Mobile controller support
For both iOS and Android we'd also like to look into controller/gamepad support, but that is more of a stretch goal for the year than a hard promise.

### PlayStation 4
Our first foray into the world of consoles was with the release of Nintendo Switch support in June of 2020. The investment we did on Nintendo Switch was rather significant but the return was great as Defold has become even more attractive as a cross platform engine. We also saw the release of a first batch of games made with Defold on Nintendo Switch. This year we plan to expand our console support to also include support for PlayStation 4.

Yes, we know what you think "PS4! Why not PS5?". We will start with PS4 for two reasons: 1) The PS4 will be around for a few more years. 2) Access to PS5 is currently restricted to select middleware and tools providers. Once we have PS4 support in Defold it is easier to become an approved tools provider for PS5.

### Xbox
We would like to also add support for Xbox in 2021, but if that happens it will likely not be until late this year. If you have a game you want to publish on Xbox you can increase the priority of this task by reaching out to your Xbox representative and request Defold support.

---

## Extensions
The ability to extend the game engine with new features using native extensions has been an amazing enabler for developers around the world. Developers can use native code in their games to get access to platform integrations and third-party SDKs. Extensions can easily be shared with others as they require no additional setup of build tools or SDKs. Most extensions can be found in the Defold [Asset Portal](/assets). Adding support for Google Play Game Services, Steamworks or FMOD to your project is as easy as adding the URL to a packaged version of the extension (usually hosted on GitHub) to the *game.project* file and then rebuilding your project. No additional setup is required and the functionality becomes immediately available through a Lua API.

This year we plan to continue building on the success of the extension system and add more features and new officially supported extensions.

### Extension updates
We plan to add, update or improve the following extensions:

* Facebook - update to Facebook SDK 9.0
* Firebase Analytics - update to Firebase 7.0.1
* Firebase Crashlytics - NEW
* AdMob - NEW

### Spine and Physics as extensions
Spine is currently tightly integrated with the engine and editor and is in its current state hard to update in order to support newer versions of the Spine animation format. The same tight integration and limitations apply to the Box2D/Bullet based physics systems in Defold.

In order to move Spine and Box2D/Bullet to extension and enable faster updates and community contributions we will make a number of significant improvements to the extension system:

* **Component resource API** - Extension will be able to register new resource types and hook into our resource pipeline. Example: the Spine scene resource tying together a Spine JSON file with a Defold atlas.
* **Component type API** - Extension will be able to register component types and associate them with resource types. Example: The Spine model component which uses the Spine scene resource.
* **Game Object API** - Extension will be able to create and manipulate game objects (the basic building block of any Defold game). Example: The Spine bones of a model are represented as game objects to which you can attach other objects.
* **Graphics API** - Extension will be able to create vertex/index buffers and register renderable objects to our renderer. Example: The Spine model component generates the required data to draw a frame of a Spine model animation.

Once we have these extension APIs in place we'll be able to move Spine and Box2D/Bullet to extensions. Not only will this allow the community to contribute updates and improvements but it will open the field for other tightly integrated yet flexible and easily modifiable extension.

---

## Stability and performance
Two of the guiding design principles of Defold are stability and performance. We want an engine that rarely (never?) crashes and performs well not only when it comes to rendering large amounts of objects at a constant high frame rate but also in terms of memory, disk and battery usage. We will work on several tasks this year to further improve Defold when it comes to stability and performance.

### Improved texture compression
We are currently in the process of migrating our entire texture compression pipeline to Basis Universal. This has the potential to improve the performance of the engine, reduce build times and add support for several new texture compression formats. The feature is already [available to test in an alpha](https://forum.defold.com/t/texture-compression-update-alpha-testing/67470). As a positive side-effect of this change we will also upgrade to OpenGLES 3.0 and WebGL 2 where applicable ([help us test this](https://forum.defold.com/t/opengles-3-alpha-testing/67495)).

### Culling
The engine currently does no culling of offscreen objects at all and leaves that job completely to the developer to deal with using Lua. This is inefficient and something we would like to address this year.

### Variable and high refresh rate screens
One source of recurring problems and instability is the way Defold currently handles monitors with variable refresh rate or screens with a high refresh rate. The problem can manifest itself as incorrect delta time being reported to scripts or games running faster than they should. We will give this issue priority this year and it is our goal to provide a predictable and stable engine update loop regardless of screen refresh rate.

### Mesh and font component performance
The Mesh component and font rendered will both receive a significant performance increase this year by avoiding uploads of new vertex buffers unless they have changed.

### Reduced draw calls for sprites
We plan to explore a way to batch draw calls for sprites with different tints by writing additional data per vertex. This becomes a trade-off between draw calls and the amount of vertex data required per sprite but should in most cases result in a performance increase.

---

## New features
Another very important design principle of Defold is to avoid breaking changes at all costs. We do not want our developers to worry about breaking changes every time they update to a new version of Defold (we release a new version every four weeks). As a developer you can rest assured that the project you worked on a year ago will still work with no (or very small) changes using the latest version of Defold.

This design principle of no breaking changes combined with our focus on low memory usage and small engine size results in an engine core with a feature set that is evolving at a much more moderate rate compared to other engines which seem to add new features without any regard to engine size or the stability of the APIs. We believe it is better to provide stable and efficient low level building blocks and let the end user build their game specific solutions using these low level blocks.

With that said we still plan to add a number of new features to Defold this year:

* Multi texturing
* 9-slice support for sprites
* Run-time modification of collision object groups and masks
* Use Mesh data as shapes for physics collisions

---

## Summary
That's it for now. We hope you agree with the direction we are taking with Defold. If not then please let us know!
