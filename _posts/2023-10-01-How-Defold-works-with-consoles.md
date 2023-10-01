---
layout: post
title:  How does Defold provide console support?
excerpt: How can Defold provide console support and stay compliant with Sony and Nintendo NDAs when the source code is available on GitHub?
author: Björn Ritzl
tags: ["blog", "tech", "nintendo switch", "playstation"]
---

In a recent [post on LinkedIn](https://www.linkedin.com/posts/bugaj_in-response-to-my-game-engine-roundup-posts-activity-7113173425568808960-Vra_), Defold was mentioned as one of the few game engines with free console support. The author of the post, Stephan Vladimir Bugaj, writes that _"Of all the community supported engines, only Defold has core support for consoles (Switch and PS4 currently, PS5 and Xbox coming soon and in mid-2024, respectively). This is a major point in favor of Defold, and frankly I have no idea how they're doing this given the onerous requirements around securing PS and Xbox devkits, including SDK NDAs. If someone from the foundation wants to enlighten us, I'm keen to know."_

It is true that developers can build games for Nintendo Switch and PlayStation 4 using Defold. PS5 will be available in October and Xbox during next year. Access to console compatible versions of Defold will be given for free to anyone approved by the console manufacturer. 

Non-console enabled versions of Defold are available to download for free on [our webpage](www.defold.com/defold), on [Steam](https://store.steampowered.com/app/1365760/Defold/) and on [GitHub](https://github.com/defold/defold/releases). 

While the full engine, editor and tools source code is available on [GitHub](www.github.com/defold), the proprietary console specific parts of the code is not. Instead, the Nintendo Switch and PlayStation versions of the source code are forked from the main open GitHub repository into private repositories. The source code architecture makes it relatively painless to separate the proprietary and platform specific code for core functionality (rendering, file operations, input, sound etc) from the non-proprietary code. This setup works well and it is easy to push fixes made in the open project to the private ones and vice versa. We go into more detail about our setup in [this blog post](https://defold.com/2023/09/18/Working-with-both-public-and-private-repos/).

On top of the engine we also have a plugin system, which makes it super easy to extend the core engine functionality with additional native code. In the case of consoles we have one plugin per platform to take care of console specific functionality, for instance user management, achivements/trophies etc. These plugins are also in private repositories. Plugins are integrated into the engine [using a cloud build server](https://defold.com/manuals/extensions/).

When we receive a Defold access request from the tools and middleware directory of a console manufacturer we provide the developer with GitHub access to the console plugin, a username and an authorization token to use when building the plugins on the cloud builder. Without access to the plugin and without an authorization token it is not possible to build for console.

That is basically it. There's no magic to it!

Head over to the Learn section of the website to read more about how to develop Defold games for [Sony PlayStation](https://defold.com/manuals/sony-playstation/) and [Nintendo Switch](https://defold.com/manuals/nintendo-switch/).



