---
layout: post
title:  Creator Spotlight - Sergey
excerpt: In the third Defold Creator Spotlight we invited Sergey, long time Defold user and creator of several Defold extensions, to tell us a little bit about himself and his projects.
author: Björn Ritzl
tags: ["creator spotlight", "interview"]
---

In the Creator Spotlight posts we invite Defold users to present themselves and share a bit of their background, their work and things that inspire them. It is an excellent opportunity for the community to come together, to recognise achievements and to share some of the great work done by Defold users.

In the third Defold Creator Spotlight we invited Sergey, long time Defold user and creator of several Defold extensions, to tell us a little bit about himself and his projects.

![Sergey](/images/posts/developer-spotlight-sergey-lerg/sergey-wide.jpg)

#### What is your name?
Sergey Lerg.


#### What is your background?
I am 34, living in Russia. When I was at school, computers were really rare in my city. I only got my hands on a Pentium III machine two years before graduation, with almost no internet. A productive usage of the computer only began during my university days. Even there we didn't have enough programming classes, my major was in radio engineering and we only studied Visual Basic and Assembly for microcontrollers. Now that I think of it that it's quite an odd choice of languages to teach students, hah!

<div align="center"><p style="font-size: larger"><i>"All hail the internet!"</i></p></div>

Only after university I was able to pick up C++, PHP, JavaScript and later on during the years Python, Lua, Java, Objective-C, Go and C#. All thanks to the internet and the great services it makes available like tutorials and getting help from the community. All hail the internet! Still after learning C++ I wasn't able to make games, I just didn't know how, the OpenGL book was too tough for me, all I could do is to rotate a few primitives with a keyboard.

Things changed when I came across Corona SDK and everything just snapped together. I was skilled enough, Corona was a breeze, Lua was just adorable and the IRC community was very helpful. In a week I learned how to make games. And I didn't stop learning new things.


#### When and how did you learn of Defold?
It got on my radar in 2016, I saw an article about it on [Habr](https://habr.com/) - Russian dev community. Back then I was actively using the Corona engine (now it's called Solar2D), it's a Lua 2D engine and Defold seemed like a good option. I was mostly making simple mobile games as a freelancer, also I made two mobile games of my own - [Laser Puzzle](https://apps.apple.com/us/app/laser-puzzle-logic-game/id1338580310) and [2048 Hex](https://apps.apple.com/us/app/2048-hex-match-numbers-puzzle/id841721448).

![Laser Puzzle](/images/posts/developer-spotlight-sergey-lerg/laserpuzzle.png)

<div align="center"><p style="font-size: larger"><i>"It was a challenge to wrap my head around Defold's API usage and development approach"</i></p></div>

I started learning Defold in 2017 and it was a challenge to wrap my head around Defold's API usage and development approach. I got used to doing everything with code and have OOP interfaces for game objects. Defold on the other hand doesn't provide such things out of the box, for its own reasons, mainly performance. Defold API is like a C API for kinda OOP framework - you have objects, but you don't have a direct access to them, they are somewhere in the RAM, you don't get C++ classes, only functions to work on the objects.

<div align="center"><p style="font-size: larger"><i>"The ability to change the cross-platform rendering pipeline with Lua is mind blowing"</i></p></div>

Thankfully, Defold is flexible enough and I wrote my own framework for it, bringing the stuff I like from Solar2D into Defold, which greatly reduces the amount of code I have to write for my projects and eases the development overall. There are things I don't agree with Defold, but for the most of it - I really like it. The thing that struck me the most is the render script, the ability to change the cross-platform rendering pipeline with Lua is mind blowing.

<div align="center"><p style="font-size: larger"><i>"I put my own Box2D extension into the box"</i></p></div>

Another great feature of Defold is being able to change parts of the engine. I didn't like the out of the box Box2D support, so I put my own Box2D extension into the box (pun intended). Or the audio system. Saying all that it's apparent that learning Defold is both easy and hard. Easy to learn if you intend to use the out of the box features, and hard to learn if you dive into the render script, native extensions and writing your own frameworks.


#### What do you like the most about Defold?
I like that Defold allows rapid development. When I need to make a change in a project, Defold allows me to quickly make the change and see the result in the game. Fast compilation and hot reload. It helps to quickly prototype mechanics and quickly layout the user interface with code. Slow iterations really get on your nerves. This doesn't happen with Defold.


#### What is your favourite game of all times?
I don't have one favorite. I like many games. Dune 1 & 2, StarCraft, [Hyper Light Drifter](https://store.steampowered.com/app/257850/Hyper_Light_Drifter/), [Nier Automata](https://store.steampowered.com/app/524220/NieRAutomata/), Doom 2, The Legend of Zelda: A Link to the Past and many others. I tend to like expressive games that have something unique in them. More recent examples of games that I like are [A Short Hike](https://store.steampowered.com/app/1055540/A_Short_Hike/) and [Townscaper](https://store.steampowered.com/app/1291340/Townscaper/).


#### What are you working on right now?
At the moment I am working at 7Spot Games, the creators of [Duo Survival](https://poki.com/en/g/duo-survival). Making a new game in a great team.

![Duo Survival by 7Spot Games](/images/posts/developer-spotlight-sergey-lerg/duosurvival.png)

In my spare time (like I have any spare time, haha, life stop it) I am working on my own game - a 3D village builder slash strategy game, heavily inspired by the irregular grid of Townscaper. Currently there is the first [devlog on my YouTube channel](https://youtu.be/Jm3pLya3d9c). Despite my affection to Defold, I am making this game in Godot because 3D support in Defold is far from what is desired. I don't like Unity, so Godot was an obvious choice. Unity is great and powerful, but sometimes illogical and a pain to work with compared to Defold or Godot. As a shameless self-promotion you should definitely subscribe to my channel, the next video is on procedural terrain generation with Defold.


#### Which part of your current project are you most proud of?
Well, if you watched the video, you can definitely say that I am very proud of implementing the grid. Just look at it! In this game I am focusing on the player's feelings rather than gameplay itself, that's one of the main selling points of many indie games. It's important to understand that and keep the focus on the player during the development.


#### How can the community follow your progress?
* First of all, you can subscribe to my [YouTube channel](https://www.youtube.com/channel/UCjkECP_YgfCXd6Y3j3rkY_g).
* You can also [follow me on Twitter](https://twitter.com/SergeyLerg).
* And if you wish to support me or use my premium extensions for Defold, you can do so [on Patreon](https://www.patreon.com/lerg).
* Also [I have a website](https://spiralcodestudio.com).
