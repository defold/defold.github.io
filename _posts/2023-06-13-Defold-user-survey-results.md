---
layout: post
title:  Defold user feedback survey results
excerpt: The results from the Defold user survey have been compiled and shared in this blog post.
author: Björn Ritzl
tags: ["survey"]
---

# Defold user feedback survey results

Some time ago we shared a survey with our users on Discord and on the Defold forum. The survey focused on three questions:

* What aspects of Defold do you like the most?
* What aspects of Defold do you dislike the most?
* What platforms are the most important for you?

The results from the survey will help guide long-term strategic decisions and development efforts. We will for instance try to focus more on promoting features of Defold that users like when we talk about Defold and when we market Defold online. We will also analyse and try to improve on the things users do not like in Defold. Finally, we will put extra effort and focus on the stability, performance and features of the platforms our users care about the most.


## What aspects of Defold do you like the most?

From a list of 16 different choices and one free text choice the top ten choices were:

* Small bundle size
* Truly cross-platform (write code once and it works on all the platforms)
* Good runtime performance
* Completely free of charge
* Friendly and helpful community
* Lua scripting
* Support from the Defold team
* Turn-key solution (you only need to download the editor to build for any platform)
* Focus on 2D games
* Informative and up-to-date manuals

The fact that **"Small bundle size"**, **"Truly cross-platform"** and **"Good runtime performance"** took the top three positions came as no surprise. These aspects of Defold have always been extremely important to us and we believe all three of them make Defold stand out from the competition. It takes a tremendous amount of effort to maintain a product that delivers on these points, but it is well worth it!

We are also very proud of our **"Friendly and helpful community"** and we are glad to see how much it is appreciated by our users. We also pride ourselves by trying to stay in touch with our community every day of the year, on the Defold forum, on Discord, on Twitter and in many unofficial channels such as Telegram and Reddit.

Some users raised concerns in the comment section of the survey that recent focus on 3D functionality might negatively impact the **"Focus on 2D games"**. We can assure everyone that we will never compromise on the 2D functionality and performance of the engine and tools.


## What aspects of Defold do you dislike the most?

From a list of 17 different choices and one free text choice the top ten choices were:

* Lack of advanced 3D features
* Not enough code samples and tutorials
* Lack of third party integrations and plugins
* Requires an internet connection to build a game with native extensions
* Lua scripting
* Community is too small or not helpful enough
* Quality of manuals
* Editor features or performance (Free text choice)
* Cross platform support is not good enough
* Too frequent releases


### Lack of advanced 3D features

We are actively working on new 3D features in Defold. In the last few months several features have been shipped that will make advanced 3D rendering in Defold possible. The next step is to package these features into an easy to use rendering package for use in games. Some of this work can be seen in the [PBR Progress thread](https://forum.defold.com/t/defold-pbr-progress/73175) on the forum.


### Not enough code samples and tutorials

Creating good educational material is both a time consuming and hard to learn artform, and we do recognise that we have work left to do here. In addition, the free form feedback text mentioned that the onboarding for new users must be improved and that new users feel like they are pushed into the deep end of the pool and presented with too much and too advanced content from the start. We will evaluate the documenation in the [Learn section](https://defold.com/learn) of the Defold webpage and try to create a better onboarding experience for new users.

In the meantime, we are truly grateful for the community efforts to create more tutorials, especically video tutorials. Two great sources of content are the [Unfolding Defold](https://www.youtube.com/channel/UCum1KBydwOdAHOIbtHwmy1g) and [Tactx Studios](https://www.youtube.com/@DefoldTutorials) videos.


### Lack of third party integrations and plugins

At the time of writing, the [Asset Portal](https://defold.com/assets/) contains 199 unique assets covering a wide range of features, from service integrations for analytics, monetization and social networks to game specific functionality such as achievements, quests and pathfinding. Many of the assets are officially supported and maintained by the Defold Foundation, while others are community created. Despite the relatively large choice of integrations we do acknowledge the fact that the Asset Portal doesn't cover all popular service integrations and features. If you have specific requests for new assets, then please let us know on the Defold forum or on Discord!


### Requires an internet connection to build a game with native extensions

It is true that if you add an extension containing native code, for instance to handle in-app purchases on iOS and Android, this code has to somehow be integrated into the engine and in the final application before it can be used. This will require some form of compilation of code and assets, and in order to compile the code and create a custom Defold game engine, additional SDKs and tools need to be installed and configured for each platform that the native code should run on. Installing and configuring SDKs and command line tools is non-trivial fopr a beginner and it goes against [our goal that Defold should have a zero-setup policy](https://defold.com/why/) meaning that a developer should not have to install any additional tools to create an application bundle for any platform.

Our solution to this problem is to [perform the build process on a cloud server](https://github.com/defold/extender) where we have taken care of the setup of all the required SDKs and tools. The drawback is that the first time a project containing native code is built, a network connection is required. Keep in mind that subsequent builds where the native code has not changed will not require a network connection. It is possible to set up a build server of your own, even on your local machine, and we do provide the instructions on how to do so, but it is not something we recommend beginners to attempt.


### Lua scripting

The fact that Defold uses Lua for scripting game logic will likely never change. If Lua really isn't your thing, then there are options to use other languages and transpile the code to Lua before compilation. The community has created support for [Haxe](https://github.com/hxdefold/hxdefold) and [TypeScript](https://github.com/ts-defold).

It is also possible, with some effort, to create an entire game using C++ and the [Defold SDK](https://defold.com/ref/stable/dmGameObject/). We will gradually expand on the Defold SDK, but it is unlikely that it will expose all aspects of the engine any time soon.

We also have [a task in our backlog](https://github.com/defold/defold/issues/6398) to explore the use of a typed Lua dialect such as [Luau](https://luau-lang.org/) (used in Roblox).


### Community is too small or not helpful enough

We will do what we can to grow our community, and while we do not have explosive growth, the community is growing! Hopefully the community will continue to grow as we improve the onboarding experience (see above) and as awareness of Defold increases among game developers thanks to successful Defold games and great community created tutorials. We also encourage existing users to help promote Defold in their respective game dev communities.


### Quality of manuals

This choice in the survey was vaguely worded and could be interpreted in a number of ways. The free form text of the survey revealed that some users find that the manuals are not always updated when new features are released in the engine or in the editor. We will try to do better in this regard. It is worth pointing out that all of the Defold manuals are [available on GitHub](https://github.com/defold/doc) and we encourage everyone to submit feedback directly on GitHub, or on the forum and on Discord.


### Editor features or performance

The free form text of the survey repeatedly mentioned editor workflows and lack of functionality as problems of the editor. Things such as editing input bindings, drag and drop, scene navigation and tilemap editing were highlighted. The last twelve months or so have been focused on improving the performance of the editor in really large projects. This has been critical but very time consuming work. Fortunately we are now reaching a point where the performance is significantly improved and we can start to look into other areas of the editor. A first couple of non-performance related improvements have been released recently:

* Code editor - [Goto definition](https://github.com/defold/defold/pull/7686)
* Code editor - [Find references](https://github.com/defold/defold/pull/7692)
* Android - [Install and launch APK](https://github.com/defold/defold/pull/7673)
* iOS - [Install and launch IPA](https://github.com/defold/defold/pull/7711)


### Cross platform support is not good enough

We were actually a bit surprised that this topic entered the top ten list and we need to investigate what users feel is not good enough. If you took part in the survey and selected this choice please let us know how we can improve!


### Too frequent releases

It would be quite easy to solve this by having longer development cycles and release less frequently, but the question is what the sweet spot is? One release every second month? One release per quarter? One per year? This becomes complicated by the fact that the choice **"Release cycle (new version every 4 weeks)"** received several votes in the survey but didn't make it into the top 10 of most liked features of Defold.

It is clear that the release cadence is something both liked and disliked with Defold and it might not be something where we can please everyone. It is also a matter of how disruptive we want each release to be. With frequent releases we get new code into the hands of users faster. The testing done during the two week beta period is valuable and we get user help detecting issues faster. It is also a well known fact that it is much simpler and faster to fix bugs soon after the code was written, since the code and the problem it was intended to solve is still fresh in the developer's mind. If we were to release less often there would potentially be more bugs and the bugs would take longer to fix.

Finally, most Defold releases are backward compatible and there is no need for developers to update their version of Defold every time a new version is released. It is usually perfectly fine to skip multiple releases and only update occassionaly. The only limitation to this rule is that games using native extensions must update every 6 months to still be able to build using the build servers.


## What platforms are the most important for you?

The platforms in order of importance to Defold developers:

* HTML5
* Android
* Windows
* iOS
* Nintendo Switch
* Linux
* MacOS
* PlayStation 4 / PlayStation 5
* Xbox

We are not really suprised by the order. We are well aware that Defold is praised by many web game developers, and we are happy to see the success of Defold games on web game portals such as Poki.com. The fact that Android and iOS score high is also no surprise, seeing that Defold was specifically marketed as a great engine for mobile games for many years. Finally we're also happy to see that the we are able to meet the expectation of support for Nintendo Switch, especially since [we made console access available free of charge](https://defold.com/2022/11/07/Nintendo-Switch-access-is-now-free/) end of last year.


## Final words

We would like to thank everyone who took the time to answer the survey. Your answers are really useful to us as they will help guide our decisions going forward.
