---
layout: post
title:  Defold user feedback survey follow-up
excerpt: In this blog post we follow-up on the results of the 2023 user survey.
author: Björn Ritzl
tags: ["survey"]
---

Almost exactly one year ago we sent out a Defold user feedback survey where we asked our users three questions:

* What aspects of Defold do you like the most?
* What aspects of Defold do you dislike the most?
* What platforms are the most important for you?

We summarized the results in [this blog post](/2023/06/13/Defold-user-survey-results/). Let's take a look at the things our users disliked the most and cross-check those against the release notes and other news to see if things have improved.


## Lack of advanced 3D features

A little over a year ago we started a journey to improve 3D support in Defold. Since then quite a few things have happened:

* Physically based rendering is now available through the [PBR extension](https://github.com/defold/defold-pbr).
* Floating point texture formats are now supported.
* It is possible to use custom vertex formats.
* Material constant arrays can now read and write arrays of data to shaders using go.get() and go.set().
* We've added support for compute shaders.
* It is now possible to use a render targets as a regular textures.
* The glTF model importer has received several improvements. We still have more improvements planned but the importer is now miles better than it was twelve months ago.
* Improvements to the mesh component to simplify runtime mesh creation
* The support for cubemaps have been improved.
* It is now possible to create textures (and atlases) at runtime.


## Not enough code samples and tutorials

We've continued to improve our documentation based on user feedback and we have added a couple of [more examples](https://defold.com/examples/) to help explain some new concepts that have been introduced this year.

[Unfolding Gamedev](https://www.youtube.com/@unfolding_gamedev) has continued to produce high quality video content. And very recently [Zenva released their first course material on Defold](https://academy.zenva.com/search/?s=defold).


## Lack of third party integrations and plugins

The "Lack of third party integrations and plugins" received quite a few votes last year. During the last twelve months we've added a couple of frequently requested integrations. Some of this development work has been sponsored by developers in our community. Thank you! In the end we added the following new official integrations:

* [IronSource](https://github.com/defold/extension-ironsource) - This integration was released just around the time of the last survey.
* [Texture Packer](https://github.com/defold/extension-texturepacker) - Support for the widely used TexturePacker tool. Texture Packer now also integrate the Defold exporter in the standard installation.
* [Steam](https://github.com/defold/extension-steam) - This was a long-awaited sequel to the original Steamworks extension by britzl. The new one features a hand-crafted and easy to use API.
* [Zendesk](https://github.com/defold/extension-zendesk) - Zendesk SDK for in-game customer service and support functionality.
* [Teal](https://github.com/defold/extension-teal) - Teal language support.


## Requires an internet connection to build a game with native extensions

This is still true one year later, but we have begun a process to simplify how developers can set up a local build environment using Docker. We are moving away from a single monolithic container to individual containers per platform. These can be hosted in a public container repository and require very little effort to get up and running on a local developer machine.


## Lua scripting

A lot has happened this year when it comes to improving the Lua scripting experience in Defold. The biggest change is probably the integration of a [Lua Language Server](https://github.com/LuaLS/lua-language-server) in the Defold Editor. This means that you will now see syntax checking and linting in real time in the editor while writing Lua code. Static code analysis results from Luacheck has also been integrated.

The community created [VSCode extension](https://marketplace.visualstudio.com/items?itemName=astronachos.defold) has also seen several new releases, making it a very powerful choice for anyone using VSCode with Defold.

If static code analysis is not enough, we also recently released Lua transpiler support which will allow developers to use languages which can be transpiled to Lua. An officially supported transpiled language is [Teal](https://github.com/defold/extension-teal), a Lua dialect with types.

We are also expanding our public C++ API (aka dmSDK) with more functionality. The goal is to let developer write all of their game logic using C++ if they wish. As part of this work we also create a public C API which will be used to generate the C++ AND other languages. As a proof-of-concept we will also provide C# as an optional extension language with the same set of APIs as the dmSDK.


## Community is too small or not helpful enough

As we noted in the survey result summary the community is growing, albeit at a slow pace. There is one big exception to this and that was in mid September last year when [Unity announced a runtime fee](https://www.polygon.com/23870247/unity-engine-pricing-model-install-fee). Game developers across the globe scrambled to find alternatives and for a period of time we saw a 240% increase in traffic and 150% more users than average launching the Defold editor (we gather [anonymous usage statistics](https://github.com/defold/defold/blob/dev/editor/src/clj/editor/analytics.clj) while the editor is running). As expected, many moved on to try other engines, but a significant number of developers stayed. Now 9 months later we still have about twice as many users of the Defold editor every day!


## Quality of manuals

Last year, the survey results and free text option revealed that some users thought that the manuals weren't updated when new features were released. Since then we've tried our best to keep the manuals updated when we add new features. We will specifically ask about this in the next survey.


## Editor features or performance (Free text choice)

Last year many users mentioned lack of good support for editing input bindings, drag and drop, scene navigation and tilemap editing. Most of these things are unfortunately still not in a state where we'd like them to be. The last twelve months we've spent a significant amount of time on improving the code editor with the previously mentioned Lua Language Server and Teal transpiler support. We've also fixed many issues and made a whole bunch of smaller improvements. We have unfortunately yet to tackle some of the larger more complex things. Our plan is to start working on improved scene navigation (both for 3D and 2D content) in a month or so. And we have recently started working on an improved editor scripting API.


## Cross platform support is not good enough

This came as a surprise last year, and when we asked for more information we didn't really receive any feedback. 


## Too frequent releases

We've come to realise that we can't please everyone and we have decided to keep our current release cadence of one new version per month. Since the last survey we've tried to improve the release notes that we share on the forum to help users better understand what each change or new feature means. We still haven't gotten around to sharing release notes in the editor though. This is something we would like to address soon.


# What's next?

Based on what we've accomplished in the last twelve months we feel confident that we are moving Defold in the right direction. We will continue to iteratively improve Defold and try to listen to feedback from our community. The next step will be to send out a new survey in a week or two to gather new feedback.