---
layout: post
title:  Defold in 2023 - A Retrospective
excerpt: Another year has gone by. Let's take a moment to reflect on some of the events and highlights of 2023!
author: Björn Ritzl
tags: ["news"]
---

Another year has gone by. Let's take a moment to reflect on some of the events and highlights of 2023! Let's start by noting that we kept our monthly release cadence in 2023, with some minor deviation. In 2023 we did 11 releases (the twelth release was left as a public beta over the holidays).


## Release cycle

From a team perspective a four week development cycle and a two week beta period works pretty well. Four weeks is sufficient time to fill each release with enough features, changes and fixes to warrant going through the release process. We're also happy with how the two week beta period works. We get enough public testing to catch most issues before release. We would like to thank our community of developers for taking the time to test their game content on the betas! It is truly helpful.


## Breaking changes

One thing to note about the 11 releases we did this year is that two releases contained breaking changes. This might not seem like much but for Defold and the team it is a pretty huge deal as we try to avoid introducing breaking changes no matter how big or small. The breaking changes were in this case unavoidable but fortunately minor and only affecting a small portion of users.


## Release highlights

The releases made in 2023 included around 70 new features and 160 bug fixes. Let's look at some of the highlights!


### Runtime creation of textures and atlases

We've started loosening up our "everything needs to be defined up-front" engine design to allow more dynamic content creation at runtime. End of 2022 we added runtime creation of textures ([#7154](https://github.com/defold/defold/pull/7154)) and during 2023 we also added support for full atlas creation at runtime ([#7196](https://github.com/defold/defold/pull/7196)).

We also added support for paged texture atlases to more efficiently pack and draw images ([#6845](https://github.com/defold/defold/pull/6845)).


### Android and iOS updates

No end-of-year-review is complete without some Android and iOS updates! During 2023 we added support for Android 13 ([#7266](https://github.com/defold/defold/pull/7266)), macOS 13.1 and iOS 16.2 ([#7480](https://github.com/defold/defold/pull/7480)). These updates are necessary and somewhat time consuming, but we've done quite a few over the years now and most of the time the update process goes smoothly.


### Shader and graphics API updates

2023 was the year when we really started to put all of the critical pieces in place to enable great 3D game development using Defold. We are slowly but surely moving towards a more GPU driven rendering architecture. In 2023 we started seeing more 3D games made with Defold and we are looking forward to what our community will create in 2024! Some of the key features of 2023 were:

* Shader include support ([#6902](https://github.com/defold/defold/pull/6902))
* Create depth / stencil buffers as textures for render targets ([#7681](https://github.com/defold/defold/pull/7681))
* Frustum culling of meshes ([#7093](https://github.com/defold/defold/pull/7093)) and models ([[#7378](https://github.com/defold/defold/pull/7378))
* Texture handles ([#7559](https://github.com/defold/defold/pull/7559) and [#7583](https://github.com/defold/defold/pull/7583))
* Floating point texture formats ([#8225](https://github.com/defold/defold/pull/8225) and [#7238](https://github.com/defold/defold/pull/7238))
* Cubemap fixes ([#7625](https://github.com/defold/defold/pull/7625))
* Custom vertex formats (sprite [#7508](https://github.com/defold/defold/pull/7508) and pfx [#7866](https://github.com/defold/defold/pull/7866))
* Material constant array support ([#7803](https://github.com/defold/defold/pull/7803)).
* Improved model importer (glTF format)


### Apple Silicon support

We finally added Apple Silicon support to our command line tools, the Defold editor and the game engine runtime. The difference in performance is absolutely amazing!


## Editor improvements

The editor received a lot of great updates too. We now have [support for the Language Server Protocol through an extension](https://forum.defold.com/t/linting-and-code-navigation-in-the-code-editor/72465) and the editor will show workspace diagnostics, code completions, annotations, documentation and much more. You can expect these extension features to become a part of the standard editor installation in 2024.

The editor also received the ability to directly install iOS and Android bundles if the command line tools are present on the system.


## Extensions

Defold is built around an eco system of engine extensions. This adds a lot of flexibility to the engine and it allows developers to [easily pick and chose](//defold.com/assets/) which features they want to include in their games to not bloat the engine with unused functionality. We actively develop and maintain a large amount of official extensions (and the community provides even more!), and each year we usually add a number of new extensions:

* IronSource - Ad mediation ([GitHub](https://github.com/defold/extension-ironsource))
* Steam - SteamWorks SDK integration ([GitHub](https://github.com/defold/extension-steam))
* lmprof - Lua Memory Profiler ([GitHub](https://github.com/defold/extension-lmprof))
* Permissions - Query and request app permissions ([GitHub](https://github.com/defold/extension-permissions))
* Profile Counters - Provide profile counters also in release mode ([GitHub](https://github.com/defold/extension-profile-counters))
* Poki SDK - Poki SDK integration ([GitHub](https://github.com/defold/extension-poki-sdk))


It is also worth specifically mentioning the [Rive](https://rive.app/) integration ([GitHub](https://github.com/defold/extension-rive)) which has been updated with the new high performance vector renderer for graphics and text. The new renderer is currently only supported by a subset of platforms but we expect to be able to support the entire range of platforms in 2024.


## Console support

This year we finally also added PlayStation®4 console support to Defold. Defold is designed with mostly clean platform separations but it is usually the case that each new platform introduces some new concept or technical requirement that we need to design and refactor for. PS4™ was no exception. The good thing is that PS5 support should come relatively soon!


## Console source code access

In December we decided to remove the source code access fee of $200/month for our console platforms. Approved developers will now also get access to the Defold source code forks with console specific low-level integrations for things such as rendering, sound, controller input and file IO. Note that source code access is not required to build for consoles. We provide this access primarily to give developers an ability to solve issues on their own, should the need ever arise.


## Great games

We're constantly amazed by the games released by our community of developers. This year some truly great games were released. Keep your eye out for a showreel video later this month.


## Corporate partners

We would also like to take this opportunity to thank our corporate partners, without whom we'd never be able to develop Defold at the pace we did in 2023. Thank you!

* [Melsoft Games](https://melsoft-games.com/)
* [Rive Inc.](https://www.rive.app/)
* [Poki](https://www.poki.com/)
* [Heroic Labs](https://www.heroiclabs.com/)


## What's in store for 2024?

This year will be the year when 3D games in Defold will really take off. We've now reached a point where Defold has the required building blocks to build visually impressive 3D games. We still miss a few things (for instance compute shaders, instancing and GPU skinning) but these will be added in 2024 together with new 3D examples to help developers get started.

We will continue to focus on the web as one of our primary platforms. We will continue to improve stability and performance and most likely also look into WebGPU as a new graphics backend.

We also hope to see Xbox in the list of supported consoles by the end of 2024.