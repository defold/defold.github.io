---
layout: post
title:  Monkey Mart is bananas!
excerpt: Moneky Mart is Tiny Dobbins latest hit-game released on Poki. Learn about the development process in this interview.
author: Björn Ritzl
tags: ["creator spotlight", "interview", "poki"]
---

Welcome to the Defold blog. This time we'll take a look at [Monkey Mart](https://poki.com/en/g/monkey-mart), a new resource management game released on Poki.com and made with Defold. We've invited Nikita and Stanislav Borisov from [TinyDobbins](https://tinydobbins.com/) to learn more.

![Monkey Mart](/images/games/monkeymart-half.png)

__Nikita and Stanislav, thank you for taking the time to answer our questions! The release of Monkey Mart seems to have kept you quite busy lately. Before we dive in and talk about Monkey Mart maybe you could tell us a bit more about your background and some of the other games you have released?__

*N & S: We started our journey into game development with flash games in 2008. It's a very warm feeling of nostalgia to remember how a market of flash games worked. Maybe someone remembers there was such a site as FGL.com where you could upload the game, and publishers were making offers on the basis of an auction.*

*At that time we released Lazerman or Tesla Defense games.*

![Tesla Defense 2](/images/posts/monkey-mart/game_tesladefense2.gif)

<div align="center">
[ Tesla Defense 2 ]
</div>

![Lazerman](/images/posts/monkey-mart/game_lazerman.gif)

<div align="center">
[ Lazerman ]
</div>

*After the end of the era of flash technology, we focused on html5 game development, using the Phaser framework. Here one of our early and very favorite project is a multiplayer game the Gunfight (the project is paused but not closed):*

![Gunfight.io](/images/posts/monkey-mart/game_gunfight.gif)

<div align="center">
[ Gunfight.io ]
</div>

*On Poki we have the following games: [Monkey Mart](https://poki.com/en/g/monkey-mart), [Stick Merge](https://poki.com/en/g/stick-merge), [Stick Defenders](https://poki.com/en/g/stick-defenders), [Party Toons](https://poki.com/en/g/partytoons), [Merge Round Racers](https://poki.com/en/g/merge-round-racers) and other car merge games. We also took part in the [Raft Wars](https://poki.com/en/g/raft-wars-multiplayer) series of games.*


__What can you tell us about Monkey Mart? Where did you come up with the idea? What were your sources of inspiration?__

*N & S: Our favorite toys in early childhood were monkey soft toys. But when they got lost somewhere in an airport we were very upset 😀 and after many years we decided to recover them in games instead!*

*We also had a popular flash game Monkey’n’Bananas where the goal of the game is to steal the bananas while the gorilla looks the other way.*

![MnB](/images/posts/monkey-mart/mnb1.gif)
![MnB 2](/images/posts/monkey-mart/mnb2.gif)

*Here is an illustration from Stanislav where you can see how the style of the main character for Monkey Mart was created:*

![Monkey Mart design](/images/posts/monkey-mart/monkey-design.png)

*We've had this idea for a long time, "we definitely need to make a game about monkeys!"*

*There was a very popular game mechanics of idle/management in the mobile market last year, we were very fascinated by such mechanics and we decided to do something with our vision. Moreover, on the web market, games in such genres have not yet been, at least of this quality.*


__What did the development process look like? Any particular challenges along the way?__

*N & S: When we get an idea for a game, Stanislav starts working on the style of the game, and I make a prototype for the main control of the monkey and that he can collect bananas and take them to the warehouse. Then one of the fascinating tasks was, to write the logic of the buyers and helpers, a small primitive artificial intelligence. the implementation is more like a FSM (Finite-state machine), plus "if...else" also :) It was very cool to see how everything on the screen worked by itself.*

*As for the graphics and art, it's also a new experience, where the background elements are in trimetric projection and the character in 2d.*


__How did you approach the challenge of balancing game-play in Monkey Mart? Isn't there a risk in idle/management games that they can become repetitive and have a steep curve of progression?__

*N & S: Good question. While balancing the game, we were guided by a "playtime per level" value, in our case "playtime per mart". We wanted the player to set up the first store in about 20-25 minutes (with the advertising reward faster) and it was important to us that, within the first 5-10 minutes, the player "got into the game" without getting bored somewhere. This is a very important indicator for web games, which is why the balance in our web version is very casual.*

*But for mobile devices (I mean, for the version that we will release in mobile stores) we will have to redesign the balance, because here players are willing to spend more time. I.e. we will have to focus on a different "playtime". The difficulty curve for mobile players will be different. Working on the balance takes a lot of time and you have to play your own game for hours.*


__What can you say about the launch? The game seems to be very popular on Poki.com. Has the launch met your expectations?__

*N & S: The launch went very well! We knew that the game was good, but the analytics numbers were even higher than our expectations. Players really liked the monkeys and asked for new content in comments on Poki, on Twitter and in emails. A very cute and funny moment happened recently, a kid asked his mother to write an email to us, to ask when the update will be available. It was very touching and sweet!*


__So, is this the end of Moneky Mart, or do you have more things planned for the title?__

*N & S: The project has a future, it is obvious for us based on feedback we have received. We've recently added a new update. And now we're working on some minor improvements. In addition we will publish the game on mobile app stores soon.*



__Will Monkey Mart Mobile be your first released mobile game?__

*N & S: Yes! All our games can be played from mobile browsers, but we’re going to mobile stores for the first time. Also this is the reason why we chose to develop the engine on Defold, cross-platform development, small final size of builds, very good performance on various mobile devices. This allows us to do web releases and to have publishing opportunities in mobile markets at the same time.*


__Nikita and Stanislav, thank you so much for answering our questions! Best of luck with the mobile release of Monkey Mart!__
