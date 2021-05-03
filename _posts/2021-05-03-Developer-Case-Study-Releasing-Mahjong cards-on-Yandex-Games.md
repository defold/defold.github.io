---
layout: post
title:  Developer Case Study - Mahjong Cards
excerpt: In this developer case study we interview Artsiom Trubchyk from Indiesoft Llc about their game Mahjong Cards.
author: Björn Ritzl
tags: ["developer case study", "interview", "yandex"]
---

Yandex.Games has quickly turned into one of the favorite places for Defold developers to release their HTML5 games. Yandex.Games has a large player base, an easy to integrate SDK and fast and smooth publishing and review process. In this blog post we'll look at the development process for Mahjong Cards, a game developed by Indiesoft Llc and launched on Yandex.Games a few months ago. We will also take a look at the Yandes.Games SDK integration created by Indiesoft and shared for free in the Defold Asset portal.

We asked Artsiom Trubchyk, one of the founders of Indiesoft to help us out.


#### Artsiom, could you please tell us about yourself and the history of Indiesoft and the games you are making?
We are a two-person company, and we are developing web games. We have been developing games since 2010, in the middle of the Flash games era, but from time to time and under different studio names.

Since last year, Indiesoft has been making games with Defold full-time, and that’s why we have often been releasing assets for the engine. One of the latest is Yandex.Games SDK for Defold.


#### How did you first hear of Defold?
I used to hear about Defold from many sources. The most significant were [talks at the DevGAMM conference](https://www.youtube.com/watch?v=dMxjswSkMyc), and it was thanks to the noise about Defold made by [Oleg Pridiuk aka Olle Pridiuksson](https://twitter.com/iWozik), who was an evangelist of the engine at that time.


#### How many games have you released so far with Defold?
There are two games, [Puffy Cat](https://poki.com/en/g/puffy-cat) and [Mahjong Cards](https://yandex.ru/games/app/134586/), published on [Poki](https://poki.com/) and [Yandex.Games](https://yandex.ru/games/), and before that, we developed few classic card games for a card games website.

Also, we have lots of prototypes. They vary from hyper-casual games to a block-building 3D game that I hope to finish eventually. We like to develop well-polished games, and this is why we are not releasing them often.


#### So Mahjong Cards is the first game you have released on Yandex.Games? Could you tell us about the game?
Yes, Mahjong Cards is our first game on the Yandex.Games platform. We wanted to release something on Yandex.Games to [look over the publishing process](https://defold.com/2021/04/21/Releasing-games-on-Yandex/), and we decided to begin with a simple game. The mechanics of mahjong solitaire, where a player should find pairs of tiles on a board, fit the best. So, I made a prototype to estimate how much time the whole project would have taken, and we decided to finish it and release it.

![](/images/posts/developer-case-study-mahjong-cards/Mahjong-Cards.png)


#### What was the development process like for Mahjong Cards?
Thanks to Defold's Lua scripting language and overall engine's friendliness and simplicity, I did Mahjong Cards in a short period of time. Luckily, I made the right decision for the game's architecture and split the game's logic and view. This helped me to save a lot of time. When I started making levels, I found out that I had to make a level editor for this game, and I managed to use most of the game's logic for this tool. Everything else, such as the operating system's file dialogues and other system functions, were already done by the great Defold community.

![](/images/posts/developer-case-study-mahjong-cards/Editor.png)


#### How was the experience of releasing a game on Yandex.Games?
It wasn't hard to publish the game on Yandex.Games. At the same time, some things weren’t obvious because the platform is quite new, and it’s growing fast. To sum up, the whole process of publishing your game is:

1. Sign up as a developer, and sign up in their advertising network to monetize your games with ads.
2. Implement their SDK in your game, follow the guidelines, prepare all required assets.
3. Upload your game and wait for the approval.


#### You also shared your Yandex.Games SDK integration with the community. Why did you decide to share it with the Defold community?
Yes, I shared [the SDK integration for Defold](https://defold.com/assets/yagames/). The point is to raise the quality of its code and documentation because more than one developer will use it. If you write code that everyone can see, you will do all you can not to look like a code monkey. Also, sharing extensions, assets, and projects helps to grow the community.

<div align="center"><p style="font-size: larger"><i>"If you write code that everyone can see, you will do all you can not to look like a code monkey."</i></p></div>

The integration implements all SDK methods, and its bonus is a mocking API to debug SDK on desktop platforms easily. It saves lots of time because the process of building for HTML5 and uploading your game to the Yandex platform to debug isn’t quick at all.


#### What are you working on right now?
My current goal is to finish a 3D tank game where players will need to hunt each other in small arenas. The unique point of this game is a mode for 2-4 players. Players will love nice graphics of cute and small tanks which explode everything around them to win the round.


#### Thank you! How can the community follow your progress and learn of new games and developments?
Follow [me on Twitter](https://twitter.com/aglitchman)! I'm glad to follow anyone back.
