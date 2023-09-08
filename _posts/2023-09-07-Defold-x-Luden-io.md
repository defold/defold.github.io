---
layout: post
title: Defold x Luden.io
excerpt: Learn why Luden.io are using Defold for their games and prototypes.
author: Oleg Chumakov
tags: ["creator spotlight", "luden.io"]
---

Hi, Oleg from [Luden.io](http://luden.io/) here! In June 2023, I sat in a hotel lobby with Björn, Mathias, and Jhonny at [DevGAMM Vilnius](https://devgamm.com/vilnius2023/). We discussed the idea of writing a post about our experience and thoughts on Defold.

I asked the developers of Luden.io about it and recalled some memories from a few years ago. So here we are.

## Previous experience
We at Luden.io have been experimenting with Defold for a while now. We are a small studio focused on educational games, which we release on Steam, consoles, and mobile devices. Mostly our games are about tech, engineering, and system design. We have used Unreal Engine, Unity, and Defold. You can find all the titles [on our website](https://luden.io/).

![](/images/posts/ludenio/whiletruelearn.jpg)

<div align="center">
_while True: learn() is a game about machine learning and cats_
</div>


## Motivation for trying Defold

#### Education and Chromebooks
Most of our players are just regular players of video games, maybe a bit more interested in tech and engineering things than the average player. But also there are some educators who use our games in class or as homework or additional educational materials. That’s why there are a lot of emails in my inbox about Chromebooks which are quite popular in U.S. education. 

![](/images/posts/ludenio/chromebooks.png)

<div align="center">
_Chromebooks listed at [https://edu.google.com/chromebooks/find-a-chromebook/](https://edu.google.com/chromebooks/find-a-chromebook/)_
</div>

With some special magic, humanity worked out how to produce Chromebooks at extremely low prices like $60-$100 so you can easily imagine how powerful they are. There are much more expensive and powerful ones but not all schools have them.

So what is basically a Chromebook? It’s a laptop with Chrome OS. So users are running almost everything using Chrome Web Browser relying on web apps for all the tasks. Since hardware is not always top-notch and we are talking web apps here you can easily predict that we can’t go Unity web build or Unreal Engine web build - they are just too heavy.

![](/images/posts/ludenio/teamworkadventure.png)

<div align="center">
_Teamwork Adventure is a tiny experimental web game about cooperation_
</div>

I want to be transparent and honest here - our latest tests of using Unity for Chromebooks took place in 2019 with [Teamwork Adventure](https://blog.luden.io/teaching-communication-to-autistic-children-with-video-games-an-educators-experience-1ff90a3e1f44). Probably now in 2023 web builds in Unity or Unreal Engine are much more lightweight. I am full of respect for Unity and Unreal Engine, wonderful tech that made the industry much more welcome for newcomers.

![](/images/posts/ludenio/electron.png)

<div align="center">
_Electron is a framework that embeds Chromium and Node.js into an app_
</div>

Also since most of our players are just regular players of Steam, consoles, mobiles, and other game-related platforms it wasn’t an easy decision to go with some HTML5-based tech stack like Phaser and then compile it for non-web platforms with some browser container like Electron. This way seems too challenging, especially when I am trying to imagine putting that Frankenstein into PlayStation or Nintendo Switch.


#### Early playable versions
Another thing is the way we publish our games. Often we publish the playable version as soon as possible to start collecting as much feedback as we can. And of course, logging into some platform, downloading the game (which is far from the final polished version), and installing it - is not a piece of cake for players who are super busy with a lot of activities at once and have so many other things to have fun with. How many of them will go away during this process? Maybe 90% or even more. What if we can make this early playable version ready to play in one click and even from mobiles? 

![](/images/posts/ludenio/craftomation-early.jpg)

<div align="center">
_The early version of Craftomation 101_
</div>

Someone can say that there is a huge bias of expecting the web playable games to be something casual or IO games and definitely not the “big” games that you can find on Steam. But it’s changing thanks to a lot of super-talented developers like [Tobias Springer](https://tobspr.io/), author of [Shapez](https://store.steampowered.com/app/1318690/shapez/).


#### Pros and Cons
The decision formula for us was something like “Chromebooks + Early playtest conversion rate = we decided to give Defold a shot in production in 2020”. What did we know about Defold at this time?

We heard about this engine before thanks to Defold evangelist and our big friend [Olle Pridiuksson](https://twitter.com/iwozik). Some of us even used it on game jams. Also, some of the students from Game Development 101 (_we help with this introductory course in Neapolis University Paphos and Faculty of Computer Science - HSE University since 2013_) were using Defold, and some of our friends were using Defold and also making Defold :)

![](/images/posts/ludenio/naturalresources.jpg)

<div align="center">
_[Natural Resources](https://ludenio.itch.io/naturalresources) is one of the students’ games made with Defold_
</div>

Defold at this time was something like — the super lightweight 2D game engine with Lua and C++ which somehow made programmers fall in love with it. Maybe it’s because of the Swedish [Demoscene](https://en.wikipedia.org/wiki/Demoscene) background of the engine founders, maybe because of the super tiny build size — it’s a mystery. 

![](/images/posts/ludenio/generatedadventure.jpg)


<div align="center">
_Defold editor with a scene from Generated Adventure_
</div>

Since this article is mainly for developers we should stop on programming languages. Defold provides a combination of Lua and C/C++. A lot of developers can agree that the best combination for development is something for super quick fast iterative development (scripting) and something to have full control of performance.

![](/images/posts/ludenio/pointermeme.png)

<div align="center">
_I can’t stand not adding this meme here in the c++ section_
</div>

In the current state of the industry of 2023, C++ is still the king of the second one. The first one is always a product of your team experience, tastes, ability to hire, and a zillion other things. For some of us, C++-with-a-lot-of-macros of Unreal Engine is good, some of us think that even C# is too tight for moving fast. Python is great but the toolset is quite huge, JavaScript is now crazy fast but... This is an infinite series of options.

![](/images/posts/ludenio/luau.png)

<div align="center">
_Luau is syntactically backward-compatible with Lua 5.1_
</div>

Lua is the ultra-compact scripting language that in hard times of dealing with a huge codebase can be covered with statically typed TypeScript. Also, there is a [Luau](https://luau-lang.org/) made by folks from Roblox which seems great, but it’s [not supported by Defold as of August 2023](https://github.com/defold/defold/issues/6398).

I heard a number of stories about conversations with publishers when Defold is a thing publishers are not experienced with as well as their porting teams. In comparison with using Unity or Unreal Engine, it’s a risk for them, and that’s understandable. The only thing I can add here is that it probably makes sense to highlight what exact platforms are supported by Defold in your presentation for the publisher.

![](/images/posts/ludenio/craftomation-profiler.jpg)

<div align="center">
_Defold profiler and an early version of Craftomation 101_
</div>

Another thing we love in Defold is the community. Since it’s not too big we always succeed in finding the right practical advice from someone without getting into holy wars and off-topic. Along with it, there are some wonderful open-source additions like [Druid](https://github.com/Insality/druid) — UI component framework and [Tiled](https://github.com/mapeditor/tiled) map editor. Especially it’s a big benefit for students who can learn by making tiny improvements to the open-source projects not as huge as the engine itself. For example, one of our students implemented Integration Tests for the unit testing system of Defold and another one made Input Text Field for Druid UI component framework.

Defold development team is always super responsive and we can have a clear and transparent conversation about everything we are stuck with. This experience is more like customer support of a nice growing startup when you can see your issues being fixed in almost real time.


## Craftomation 101
Craftomation 101 is a craft automation game about funny programmable robots, CraftoMates, who can move, eat, and craft things needed to terraform a frozen planet. And they can build themselves, so we talk about [self-replicating machines](https://en.wikipedia.org/wiki/Self-replicating_machine) here.

![](/images/posts/ludenio/craftomation-selfreplicating.gif)

<div align="center">
_Self-replicating machines are a charming concept in the core of Craftomation 101_
</div>

As for August 2023, Craftomation 101 is in closed beta in [Discord](https://discord.gg/ludenio) with a free [web](https://ludenio.itch.io/craftomation101) and [Steam](https://store.steampowered.com/app/1724140/Craftomation_101_Programming__Craft/) demo available. The demo is about 40 minutes and the full version of the game is about 3–4 hours. Closer to release the game should become 6–8 hours long not counting the endless sandbox mode. ~50,000 sessions played Craftomation 101 so far and helped us by providing feedback.

The biggest technical challenge in this type of “system design” game is to make the game ready for really unexpected and huge player creations. We know a bit of our future with Craftomation 101 thanks to our other Unity game [Learning Factory](https://store.steampowered.com/app/1150090/Learning_Factory/) and its wonderful players who challenged us a lot in a good way.

Craftomation 101 is on a 2-week update cycle, players know that we’ll roll out a new update every 2 weeks. On this tight schedule, it’s wonderful to have Defold updates that are not destroying compatibility or bringing critical issues. That’s why we almost always followed the latest stable version of the engine which was not our regular practice with other game engines.

![](/images/posts/ludenio/craftomation-visualprogramming.png)

<div align="center">
_Visual programming of Craftomation 101_
</div>


#### Spine
As you probably already noticed, Craftomation 101 contains a lot of animations so you can see your CraftoMates work hard. We use the [Spine](http://esotericsoftware.com/) animation system and a while ago the Spine plugin for Defold was going through a change from the old one to the new shiny fresh one. This transition was quite a challenge for us, we broke “all the game” several times while updating. 

Once we faced “an interesting” thing about the Z axis, handling of which once was surprisingly changed so it took us to remake all the rigs. What was especially amusing in that all the CraftoMates started rolling their jaws at the game’s start. What a show to remember!

![](/images/posts/ludenio/craftomation-gameplay.gif)

<div align="center">
_What to expect from playing Craftomation 101_
</div>

Another one was when we investigated several issues because for some reason the version field of the animations was exported with a string like “4.0.04 from 4.1.23” instead of “4.1.23”. Surprisingly the depths of the Spine plugin code weren’t ready for that.

But at the end of the day Spine is a great tool. Maybe it should be added to the Hall of Fame for industry tools for making possible so many wonderful well-animated games. 


#### Outline
Several players who are also developers asked us about the universal sprite outline effect and how it’s made. So it’s quite a simple thing but it took some time for us to understand what we want. We played around with the good old outline shaders in Defold for a while, with Spine animated models and raw sprites. We ended up with just sprite duplicates, filled with the white color, and shifted several times to cover all 360 degrees. If you need one please feel free to drop us a line at info@luden.io, and we’ll be happy to share.

![](/images/posts/ludenio/craftomation-dynamictilemap.png)

<div align="center">
_Base expansion in Craftomation 101 based on dynamically changing tilemap_
</div>

And of course, Craftomation 101 showed the true potential of the web playable versions. Thanks to simplicity of start playing we collected a lot of feedback from more than 50,000 play sessions during alpha. The result conversion is hard to compare with all our experience with “download and install” alpha playtests.

Also, we are working on a series of short lightweight chapters of [Craftomation for Poki](https://poki.com/en/g/craftomation-1), a web-based games platform. Who knows where it’s gonna lead us but we feel positive about this having in mind how easier to use these “tiny chapters” in class than the full big games.

![](/images/posts/ludenio/craftomation-researchtree.png)

<div align="center">
_The research tree and other screens in Craftomation 101 are built with Druid UI framework_
</div>

Craftomation 101 is made completely on Lua and C++ but now, when we have around 43,000 lines of code we are considering using TypeScript just to win some stability and feel of control thanks to static typing and catching some possible issues during the compilation instead of the runtime. Who knows, maybe the day Craftomation 101 got too big Defold will support Luau and we’ll be able to choose it instead of TypeScript.


## Generated Adventure
Defold now is also our primary tool for experiments. Generated Adventure and Warnament are great games to illustrate what I mean.

![](/images/posts/ludenio/generatedadventure-levels.jpg)

<div align="center">
_Three levels of Generated Adventure_
</div>

[Generated Adventure](https://blog.luden.io/generated-adventure-the-postmortem-of-a-game-made-with-chatgpt-and-midjourney-prompts-included-f87e7e615204) is a Ludum Dare 53 game jam entry based on as much generated content as possible. There is a huge postmortem post over here which you probably already saw because it exploded on the internet after publication a bit. But actually, there’s not much I can say because the [postmortem](https://blog.luden.io/generated-adventure-the-postmortem-of-a-game-made-with-chatgpt-and-midjourney-prompts-included-f87e7e615204) covers everything in detail.

## Warnament
Warnament is a lightweight highly customizable grand strategy designed together with our super active community and mod makers.

My old friend [Alexey Gulev](https://twitter.com/AGulev) who is a wonderful game developer and now one part of the Defold engine team introduced me to the lead developer of Warnament. After a few calls, we decided to support his new project. I was especially hooked by the idea of making a community-driven highly customizable game. Call me a year from now and I will tell you if we succeed in making a turn-based grand strategy game in an “easy to start hard to master” way.

Warnament is now available as a closed beta and as a free demo for Android, Windows, macOS, and Linux. All the things are happening in our [Discord](https://discord.gg/2t6vqYjjG8) and [on the Steam page](https://store.steampowered.com/app/1201700/Warnament/).

![](/images/posts/ludenio/warnament-europe.jpg)

<div align="center">
_Map of Warnament is made with huge procedurally generated mesh_
</div>

Map Engine of Warnament is written half in plain Lua (not TypeScript) and half in C++. The combination is quite classic — Lua is for quick implementation of game logic and C/C++ is for high-loaded parts and bottlenecks.

Since Warnament is a community thing we can’t even imagine what maps they will decide to make. That’s why the map engine should be ready for everything, even for the highly detailed map of the whole planet (and not only the Earth to be honest). So there are a lot of high-performance C/C++ injections in this part.

![](/images/posts/ludenio/warnament-community.jpg)

<div align="center">
_Yes, it’s one of the community-made maps for Warnament_
</div>

And of course, you can enjoy the game 100% only in multiplayer. More than that — you can maintain your server with custom rules (e.g. no wars at all, only diplomacy). To make it easier to deploy and customize we put some parts of Lua logic into independent modules which can be run with Defold game client or server or any tool you want to build for Warnament. It shines bright for community events like Tournaments, Roleplay servers, and custom maps-based games.

![](/images/posts/ludenio/warnament-research.jpg)

<div align="center">
_Political research screen in Warnament_
</div>


## Plans 
All the game engines I worked with are full of pros and cons and there is no ideal one. The important part is how your team is enjoying the process. If the developers are happy with the tech your chances to keep a healthy and productive atmosphere are much better.

We are having so much fun working with Defold and turned a number of our old friends, really experienced developers into fans of Defold just by sharing our experience. Release of Craftomation 101 and Warnament is gonna be a huge stress test for Defold and our experience because we’re going to cover a lot of platforms.

At the end of the day, Defold is a wonderful and unique tool with a cozy community of great people around. We at Luden.io appreciate the titanic work that the developers of Defold are doing and their wish to keep making our industry a better place.


## Bonus
Since we work from different parts of the planet it’s impossible to invite all of you to “our cozy office”. But I hope you can get the feeling of visiting us by taking a look at the photos of the places where all the magic is happening.

![](/images/posts/ludenio/ludenio-home1.jpg)
![](/images/posts/ludenio/ludenio-home2.jpg)
![](/images/posts/ludenio/ludenio-home3.jpg)
![](/images/posts/ludenio/ludenio-home4.jpg)
