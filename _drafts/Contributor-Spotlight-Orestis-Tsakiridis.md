---
layout: post
title:  Contributor Spotlight - Orestis Tsakiridis
excerpt: In this Defold Contributor Spotlight we invited Orestis Tsakiridis to tell us a little bit about himself and why he is contributing to the Defold source code.
author: Björn Ritzl
tags: ["contributor spotlight", "interview"]
---

It is amazing how much the video games industry has changed in the last decade. Modern game engines have made game development accessible on a level that was completely unheard of fifteen years ago. Back then, game developers had to spend a significant amount of time on low level system integrations, rendering technology and performance optimizations while at the same time trying to create the games we love to play. The purpose of modern game engines is to take care of all of these nitty gritty details and complicated optimizations and integrations with the platforms on which games are run. Game developers can nowadays focus on creating awesome games and let game engine developers worry about rest. Today game engines are taken for granted; they are expected to "just work". And at the same time game engines are some of the most complex pieces of software written, created over the course of many years and thousands of man hours of work. And they are usually available for free.

In the Contributor Spotlight posts we put the unsung heroes of game development in the limelight and invite Defold game engine contributors to present themselves and share a bit of their background, their work and what got them into game engine development. It is an excellent opportunity for the community to give recognition to the developers of their favorite game engine!

In this Defold Contributor Spotlight we invited Orestis Tsakiridis to tell us a little bit about himself and why he decided to contribute to Defold.


##### What is your name?
I'm Orestis Tsakiridis.


![](/images/posts/contributor-spotlight-orestis-tsakiridis/bubble-bobble-future-crew.png)

##### What is your background?
I am 44. Currently living in Greece. My first contact with computers was at the age of 8 playing 'Bubble Bobble' on Amstrad CPC 464 with a friend. Next to the "computer" was a "BASIC" book. That was enough to get me started. The next memorable milestone was seeing the Future Crew demos back in the '90s. Namely 'Unreal' and 'Second Reality'. Spectacular stuff for the time. They were mostly written in 8086 assembly and some C and they worked as a drive and a guide for many years later, both in their technical and psychological respect. I was working on a small sprites library some time later, counting the CPU clock cycles on reference books and pushing it until FPS would drop under the optimal screen frame rate. Ok, that was a burnout, I admit :-)

Τhen, there was the college, the rise of the Web and the market that came with it. It was the Web Development era. Working in the field wasn't ideal but kept the boat afloat. I worked on various relevant technologies in both front/back-end fields and ended up in a voip company writing open source Java/JS. I typically was in contact with OpenGL and DirectX graphics APIs at their initial stages working on minor side projects. I disliked the fact that there were often politics involved and a lot of proprietary stuff in graphics library and drivers. This kept my enthusiasm at bay.

Other notable moments were when I discovered the Lua programming language and the open source practice. With Lua, it was love at first sight. Minimal, fast, easily coupled with C and truly open. But not very popular, unfortunately. Free software ideas and practice seemed the right way to move forward. Not always easy, but it helped me sleep better at night :-).


##### When and how did you learn of Defold?
Well, I don't really recall when I first came across it. It surely took some years to get involved after first contact. I imagine I bumped into it when searching something like "Lua game framework" or so. I followed [the Defold Twitter account](https://twitter.com/defold) and monitored its newsletter for a long time afterwards.


##### What made you decide to contribute to Defold?
I was looking for a game related project to get involved in to move away from web stuff. Defold fit the bill. It seemed light, scripted with Lua, written in C++ and had an active community that seemed to care for the product. In terms of marketing direction, it seemed to have a place and a future. The license seemed open enough to justify spending effort on it. So, I made the move.


##### Can you tell us a bit about the contributions you have made to Defold so far?
I have mostly [dealt with sound issues](https://github.com/defold/defold/issues?q=is%3Aissue+assignee%3Aotsakir+). I decided to narrow down the scope of my involvement so that I could build some technical experience and minimize my effort while offering something back to the team. Sound was a field needing help, it had some entry level issues available in the "TODO" list and was easy to troubleshoot in Linux (where I am more comfortable in). After the first couple of issues it got easier and I got more productive.


##### What is your recommendation to someone wanting to contribute to Defold for the first time?
Before recommending, to make things easier, I'd say that the community is warm and supportive. The infrastructure for development is well established and really helpful. The product has some dark spots but it's generally well written.

That being said, I'd recommend to focus. Use a single platform for development. It's also crucial to pick appropriate issues for starters. If you can't [find them on GitHub](https://github.com/defold/defold/issues?q=is%3Aissue+label%3A%22good+first+issue%22+is%3Aopen), ask on [Discord](https://discord.gg/cHBde7J) #source-code channel. I'd suggest to stick to the core engine and avoid the editor (unless one is already experienced with [Clojure](https://clojure.org/)).

Lastly, it's better to work on bugs than on features. The latter require discussion, more experience with existing design patterns etc. Use discord #source-code channel for quicker support. Use the [forum #source-code category](https://forum.defold.com/c/source-code) if you want your discussion to also work as a knowledge base and reference for others.


##### What did you struggle with when you first decided to contribute to Defold?
Building the whole product, setting up a quick workflow for development iterations, finding the proper issues to work with and getting the first push from the team were all very crucial at the start. Having a hard time there will possibly deter a newcomer.

Once these were dealt with, came the lack of engine documentation. Although, in terms of user documentation Defold shines brightly, when it comes to developing the engine itself it is not optimal.

_(Editor side-note: This and some other feedback from Orestis will be looked at to make the startup process for new contributors smoother)_


![](/images/posts/contributor-spotlight-orestis-tsakiridis/qt_developmenttools_main.png)
[ Source: https://www.qt.io/product/development-tools ]

##### What does your development setup look like? Any essential tools that help you get the job done?
I typically work on Linux. I've used [Geany](https://www.geany.org/) as a text editor but recently moved to [Qt Creator IDE](https://www.qt.io/product/development-tools) in an effort to accelerate. I'm still not very satisfied. In general, since the project is relatively big, it's important to have proper code navigation built into the IDE to quickly jump from one location to another. The rest is done from the console.

Git console client, grep, gdb for debugging (gdb is a life saver and Defold cooperates seamlessly with it). There is also having a Defold editor to play with as well as some custom bash scripts to buy me some more time in boilerplate operations.


##### Are you also using Defold to create any games?
No, not currently. At present I'm more interested in the engineering side of things than in the purely creative side. I tend to believe that I can do it better too. My target is to get a decent job in the field.


##### Thank you so much for participating! Can the Defold community follow your work somehow?
