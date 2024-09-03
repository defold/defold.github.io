---
layout: post
title:  Defold user survey results
excerpt: The results from the Defold user survey have been compiled and shared in this blog post.
author: Björn Ritzl
tags: ["survey"]
---

Some time ago we shared a survey with our users on Discord and on the Defold forum. The survey tried to find the answers to these questions:

* Which aspects of Defold are the most appreciated?
* Which aspects of Defold are the most disliked?
* Which platforms are the most important?
* Is there an interest in 3D game development?
* What is the community opinion on the state of 3D support in Defold?
* How does our community prefer to learn new things?
* Which third party integrations are missing?

There was also a free-form feedback field at the end of the survey. The survey was open from June 26 until August 26. The results from the survey will help guide long-term strategic decisions and development efforts.

## Which aspects of Defold do you like the most? (pick 5)

![](/images/posts/defold-user-survey-results-2024/like.png)

There were not really any big surprises in these results. We know that a lot of users are very happy with the runtime performance of Defold. We are also happy that many users still value the free support we provide and the friendly community we foster over at the Defold forum and Discord. Thank you to everyone for helping the Defold community remain a friendly place for developers from all over the world!

## Which aspects of Defold do you dislike the most? (pick 5)

![](/images/posts/defold-user-survey-results-2024/dislike.png)

We were not surprised that "Poor 3D support" was chosen by a lot of users. Interest in 3D game development using Defold has grown a lot since we started working on more 3D features. We still have a long way to go and by the time of the next survey we expect the number of developers picking "Poor 3D support" to have decreased by quite a bit.

We are not happy with the fact that many developers chose "Not enough code samples". We will increase our efforts to improve on this in the coming 6 to 12 months.

The "Requires internet connection" option when building nagtive extensions will see some improvements soon. We have been busy improving the build server infrastructure and one of our goals is that it should be much simpler to set up a local build server on a developer machine instead of building nagtive code in the cloud.

## Which platforms are the most important to you? (pick 3)

![](/images/posts/defold-user-survey-results-2024/platforms.png)

The fact that HTML5 is the most popular platform really shows how Defold developers have embraced the web as a valid target platform for their games. We also see many success stories on sites such as Poki, CrazyGames, Cool Math Games and the like.

Windows is both the main development environment for a lot of developers and the main desktop platform to release games on.

Compared to the results from last year's survey Android has dropped from second to third place and iOS remains at the fourth spot. Mobile games are still important, but is their importance declining in favour of the web?

## How do you prefer to learn new things?

![](/images/posts/defold-user-survey-results-2024/ways-of-learning.png)

At least among our community developers prefer to learn from code samples and written manuals over video tutorials. From our point of view this is a good thing because high quality videos are expensive and time consuming to make. We will not focus efforts into video production and instead leave that to experts such as Unfolding Defold and other good game development channels.

## How would you describe your interest in 3D game development?

![](/images/posts/defold-user-survey-results-2024/3d-interest.png)

We were a bit surprised by the fact that more than 50% of developers are interested in 3D game development in Defold. The strong response will help guide future development efforts, but we will have to tread carefully to also maintain very strong 2D support.

![](/images/posts/defold-user-survey-results-2024/3d-support.png)

We knew that we would score low on this question. It also showed in the previous question where many users said that they dislike the lack of good 3D support in Defold. Perhaps a little bit surprising is that so many developers are still interested in 3D game development using Defold despite these shortcomings.

## Which 3D features are you missing the most?

In this free-form feedback field a lot of known but also some new feedback was presented.

__Editor__
* Shader previews in the editor
* 3D scene editing and camera (1)
* Model creation
* Editor performance with large scenes (2)
* Terrain editing

1 = We will actively work on this during Q3 and Q4.
2 = There is bound to be some low hanging optimization fruit here.

__Runtime__
* GPU instancing (1)
* GPU skinning
* Improved camera component
* Point primitives
* Navigation
* Proper 3D math library
* 3D particle effects with mesh support
* 3D GUI

1 = GPU instancing will be released in Defold 1.9.3 or 1.9.4.

__Rendering and materials__
* Lighting (1)
* PBR by default (1)
* Skybox and Fog (1)
* Easy material creation
* Level Of Detail

1 = These features should created and shared in a template or sample project that other developers can use as a base for their own games. In the future, some things might be built in to Defold, such as a basic light component.

__Physics__
* Better physics (Jolt) (1)
* Cloth simulation
* Better collision shapes (2)
* Shape casting (3)
* Ragdoll

1 = We are planning how to turn the physics engines into native extensions so that it is easier to replace Bullet with Jolt for instance.
2 = This is identified as a critical missing component which we have to provide to make 3D physics game development easier.
3 = This is planned for both 2D and 3D

__Animation__
* Inverse kinematics
* Skeletal animations
* Animation blending

__Formats__
* Blender integration (1)
* Better glTF import (2)

1 = There is a [community created Blender to Defold exporter](https://forum.defold.com/t/building-a-sync-tool-for-blender-to-defold/69920).
2 = We will improve glTF model imports and treat the glTF format more as a container format than something only used on a specific model.

__Docs__
* Lack of instructions on a decent 3D setup
* Samples and guides

The lack of good samples and guides was also identified as a problem previously in the survey and you can expect to see improvements in this regard going forward.



## Third party SDK support

![](/images/posts/defold-user-survey-results-2024/third-party-sdks.png)

We are pretty happy with this result. The Defold Foundation maintains almost 70 open source extensions and the Defold Asset Portal as a while contains almost 250 assets that can be used in Defold. With that said, it will be very hard to support and maintain integrations with every conceivable service and SDK out there. Fortunately the native extension system can be used by individual developers to create integrations with the services they need.


## Which third party SDKs, services and tools are you missing the most?

While it is impossible to support and maintain all integrations there might still be some that are considered critical to the success of our community, in which case we need to consider creating official integrations.

__Audio tools and frameworks__
* FMOD (1)
* Wwise

1 = A [community created version exists](https://github.com/dapetcu21/defold-fmod).

__Map tools__
* LDtk
* Improved Tiled support (1)

1 = We should perhaps consider to add support for the TMX tilemap format as an extension.

__Art and animation tool support and integrations__
* Sketchfab
* Blender
* Aseprite (1)
* Live 2D
* Rive (all platforms) (2)

1 = A member of the community recently shared an [Aseprite to Defold exporter](https://forum.defold.com/t/if-you-use-aseprite-try-this-one-click-exporter/77892).
2 = We will attempt an update of the Rive runtime during Q3 and use a more standardized Rive runtime integration. With this update we should in theory be able to support all platforms.

__Store SDKs__
* Steam SDK (Networking) (1)
* GOG Galaxy SDK
* Epic Online Services SDK

1 = The Steam SDK does support a fairly large portion of the most popular APIs. If an API is missing the recommendation is always to submit a feature request.

__Networking and multiplayer__
* Photon
* Playfab
* Lootlocker

Multiplayer/online game development is hard. There are a number of good services with Defold support, for instance [Nakama](https://heroiclabs.com/nakama/index.html) and [Colyseus](https://docs.colyseus.io/getting-started/defold-client/).

__HTML5__
* CrazyGames (1)
* Kongregate
* Newgrounds
* Discord Embedded SDK

1 = A community created integration with [CrazyGames exists on GitHub](https://github.com/d954mas/defold-crazygames-sdk).

__Mobile SDKs__
* Appsflyer
* Applovin (1)
* Bright SDK
* Admob (2)
* Apple Game Center (3)
* Apple Authentication (4)
* Firebase Crashlytics
* Mixpanel
* Samsung IAP
* Play Asset Delivery


1 = Applovin MAX SDK integration [exists in the Asset Portal](https://defold.com/assets/applovin-max/)
2 = [AdMob too](https://defold.com/assets/admob-defold/)
3 = Apple Game Center [can also be found in the Asset Portal](https://defold.com/assets/gamekit/)
4 = Sign in with Apple is [also in the Asset Portal](https://defold.com/assets/siwa/)

__Platforms__
* Meta XR SDK
* LG Web OS
* Tizen OS

It is very unlikely that we will add support for any of these.

__Miscellaneous__
* Text To Speech
* Jetbrains IDE support
* Force feedback


## Free-form feedback

The final field of the survey contained a field where free-form feedback could be submitted. The feedback covered many different areas. Here is a summary:

__Editor__
* UI tools
* Bezier Curve Tools
* Better 3D tools
* Live Update tools
* Improved code editor
* Editor extensions
* Shader editor
* Animation editor
* Better Asset Portal integration
* Configurable keybindings
* Configurable editor panels
* Grid tools

Runtime
* Improved camera and camera to world conversion
* Improved dynamic asset loading

__Text support__
* Right-to-left support
* Improved font handling

__Concepts__
* Merge gui and go
* Nest game objects in a .go file

__Features__
* Ready-made shaders and special effects
* Native solution for 2d skeletal meshes
* Video playback
* Pathfinding
* Parallax 2D
* Hex tilemaps
* Isometric tilemaps
* Advanced GUI system
* Better box2d joints support

__Languages__
* Improved Teal support
* Add TypeScript support

__Documentation__
* More code snippets
* In-depth Android development docs
* Tutorials on rendering

__Roadmap and vision__
* Focus on 2D, not 3D!
* Better feedback on submitted issues on GitHub

__Extensions__
* Remove assets that have not been updated in a long time

Many of the things suggested are also on our radar and we will, if time permits, work on some of them over the next 12 months. Other things are out of scope of what we are trying to achieve with Defold and are best implemented as extensions or not at all.


## Final words

We would like to thank everyone who took the time to answer the survey. Your answers are really useful to us as they will help guide our decisions going forward.

