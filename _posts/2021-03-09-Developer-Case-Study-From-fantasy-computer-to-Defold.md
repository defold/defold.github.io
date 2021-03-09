---
layout: post
title:  Developer case study - From fantasy computer to Defold
excerpt: In this developer case study we'll take a look at how Brasilian game developer Jeferson R. Silva ported a game from TIC-80 to Defold.
author: Björn Ritzl
tags: ["developer case study", "interview"]
---

The world of 8-bit computers and consoles is almost as alive today as it was back when sales of the ZX Spectrum, C64, NES and Atari 800 peaked 30 years ago. Proof of this can be seen in the sale of "mini" versions of the original computers and consoles ([C64 Mini](https://retrogames.biz/thec64-mini), [NES Classic](https://www.nintendo.com/nes-classic/) etc), in the creation of new "8-bit" systems such as the [MEGA-65](https://mega65.org/) and in the many fantasy computer systems and console such as the [TIC-80](https://tic80.com/) and [PICO-8](https://www.lexaloffle.com/pico-8.php).

Fantasy computer systems have become a very approachable way of experiencing the joy and the challenges of game development for resource constrained hardware without having to learn things such as 6502 assembly language. Both TIC-80 and PICO-8 simulate the restricted hardware of an old 8-bit system packaged into a user friendly experience with integrated tools for asset creation and the use of Lua for writing game logic.

The TIC-80, PICO-8 and similar fantasy systems are amazing pieces of software and they introduced countless aspiring developers to world of game development. While it is possible to create all kinds of amazing games and tools using fantasy computers and consoles they also have their limitations and there are many examples of developers porting their creations over to other game engines to unlock new capabilities and platforms. One recent example is Slipways which was ported from PICO-8 ([itch.io build](https://krajzeg.itch.io/slipways)) to Unity ([Steam build](https://store.steampowered.com/app/1264280/Slipways/)) and another older example is [Hook, Line and Thinker](https://forum.defold.com/t/hook-line-and-thinker-11-devlogs/15963) which was ported to Defold.

In this developer case study we'll look at how Jeferson R. Silva ported his game nullptr from TIC-80 to Defold. Let's jump in and meet Jeferson!


#### What is your name and your background?

My name is Jeferson Rodrigues da Silva, born in 1981 and living in Brazil. I started coding when my father bought a MSX in 1986 (or 1987?). It came with a BASIC manual with lots of short code examples and I really liked copying those codes and seeing stuff happening. Since then I've been learning a lot of programming languages and making small games as a hobby.

![](/images/posts/developer-case-study-from-fantasy-computer-to-defold/jeferson-msx.png)

[ that's me and the MSX ]


#### When and how did you learn of Defold?

According to a post I made on Twitter, it was right after it was publicly released in 2016. At that time, I was creating another game using Unity so I didn't get to test Defold. In 2017, I tried to port Pac-man as faithfully as possible in Defold but I abandoned this project soon after implementing basic movement and eating. My memories from that first try tell me that I felt a bit restricted by the engine since I wanted to have full control over things like doing sprite animation via code. Also, the message passing approach was something that I was not used to based on my previous experience on game development. (totally my fault, sorry!)


#### Can you tell us a bit about your game "nullptr"?

nullptr (read as "null pointer") is an action puzzle game where you play the role of a hacker trying to take down some mega-corporations by hacking their servers to download and destroy data. In each level you have limited time to find a safe route to the databases while manipulating and dodging defensive programs and server systems. It is a fast paced game that requires careful planning and precise execution.

![](/images/posts/developer-case-study-from-fantasy-computer-to-defold/nullptr-tic80.png)
[ TIC-80 prototype ]


#### Why did you decide to port the game to Defold?

First of all, TIC-80 is a great tool and made it possible for me to have a working prototype without having to learn a lot of new things. Since I already knew Lua and had a lot of experience in creating games using libs like [SDL](https://www.libsdl.org/) in C++, it was really easy to focus on the game ideas I wanted to implement.

As the prototype evolved and I was having fun playtesting the game, I thought that maybe I could try to release a polished version as my first commercial game. Moving from TIC-80 to Defold would also allow me to add things like achievements, a level editor and some accessibility options. Knowing that Defold could easily deploy to multiple platforms was also a big plus.

![](/images/posts/developer-case-study-from-fantasy-computer-to-defold/nullptr-defold.png)
[ current defold version ]


#### What was it like porting the game from the TIC-80 to Defold?

At first I thought it would be an easy job and that I'd only have to change parts of the code that dealt with drawing sprites and primitives to the screen. I lazily skimmed through the documentation and tried to replicate the procedural approach of the TIC-80 version to Defold. It seemed to work but I soon found out that things were not looking so good on the [web profiler](https://defold.com/manuals/profiling/#the-web-profiler). It turned out that I had a lot of game objects with their own scripts and update functions and that was not the way I should be doing stuff in Defold. This is something that is explained in the documentation and had I not been lazy, I would have saved some time starting with the right approach.

Now that I changed my mindset to the reactive approach of Defold, the rewriting process is much faster even not reusing old code from the TIC-80 prototype. I am much happier with the resulting code quality too.

Both TIC-80 and Defold use Lua which I guess helped during the porting process. A lot of other things are probably quite different between the two engines.


#### What, if anything, did you struggle with when moving from TIC-80 to Defold?

I think the most difficult part for me was resisting the urge to use the update function to manipulate game objects every frame, especially coming from a fantasy console. Never before I thought about game development in a reactive way and now I had to convert everything I had in the prototype to this approach that was not familiar to me. The funny thing is that the reactive approach is perfect for a game like this and I've been positively surprised by how easy things became to implement.

One of the things I'd like to keep from the prototype was the look and feel of the game and for that I'd have to replicate all the random movements that made the game objects feel "alive". For the prototype, this was done by calculating some random displacement every frame before drawing the objects. In Defold, I knew that I would have to use the animate function and that I would have to work with simple interpolations. So I had the idea to pre-calculate some random arrays with 60 elements (one for each frame) and use that as an easing function in go.animate. So for each object I could select one of these random easing functions and have something that behaved exactly like the prototype. I don't know if this is the best way but things are looking good in the profiler and the look and feel I want is there!

Finally, there are some things that are incredibly simple in fantasy consoles like defining a clipping region to limit drawing area. In order to do this in Defold, you have to write a [custom render script](https://defold.com/manuals/render/). I'm not an expert in this, having only some limited experience working with OpenGL, but I knew that I needed to use a fragment shader to combine what I wanted to draw with a clipping mask. Fortunately the documentation covers the topic of creating a render target for post-processing and this was enough to get me started. Beginners that need this functionality may find it to be a daunting task.


#### Which part of "nullptr" are you most proud of?

In nullptr there are defensive programs you must evade when trying to reach the databases. Each one of these programs have their own rules based on how data (colored tiles) is located and manipulated in the level. For example, one of the most basic programs moves by following the red tiles. The player can manipulate this path by getting the color of a tile and placing it in a white tile. Other programs react to the number of green tiles you crossed on your route. In this case, you can manipulate their movement by changing your route. Every program can be manipulated by some action performed by the player. This creates a situation even if you know how to solve a level based on the core mechanics, the presence of a new program is exciting since it changes the way you execute your plan. First you must discover how it works and it may interact with the elements present in the level. Then you need to find out how to manipulate it to create a safe route to the goal. Different programs can also be present on the same level so there are a lot of possibilities for great level design. Having said that, I'm really proud of the game as a whole and I find it really fun to play! (even after playtesting it a lot hahaha)


#### What are your plans for the game? You mentioned achievements, a level editor and releasing for multiple platforms.

The finished game should have 120+ handcrafted levels, a level editor, achievements and maybe leaderboards for some sort of speedrun mode. I'm planning to launch it on Steam late 2021 (Windows, Linux and macOS) and after that I'll probably try to release it on Switch too. I'm also planning to release a demo version on TIC-80 based on the prototype that I have today.


#### How can the community follow your progress?

You can [follow @jefrsilva on Twitter](https://twitter.com/jefrsilva) for more updates on nullptr!
