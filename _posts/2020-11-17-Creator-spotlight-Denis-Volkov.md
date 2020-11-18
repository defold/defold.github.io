---
layout: post
title:  Creator Spotlight - Denis Volkov
excerpt: In this Defold Creator Spotlight we invited Denis Volkov to tell us a little bit about himself and his ambitious project "Zoo Economy".
author: Björn Ritzl
---

In the Creator Spotlight posts we invite Defold users to present themselves and share a bit of their background, their work and things that inspire them. It is an excellent opportunity for the community to come together, to recognise achievements and to share some of the great work done by Defold users.

In this Defold Creator Spotlight we invited Denis Volkov to tell us a little bit about himself and his ambitious project "Zoo Economy".


#### What is your name?
Denis Volkov.

![Zoo Economy world map](/images/posts/developer-spotlight-denis-volkov/denis-volkov.png)

#### What is your background?
I'm 26. I live in Russia and right now I am mostly working on games and work part time on sport events and as a teacher. I have a technical background and from the age 15 or 16 I've wanted to make games. Over the years I experimented with UE 3 UDK, UE 4 and a little bit with Unity. One of the project from that time is now on the 'shelf' waiting for better times and money. I transitioned to Defold to make smaller but finished games :)


#### What would you say is the biggest difference between UE or Unity compared to Defold?
The main difference is in engine purpose. UE and Unity mostly focused on cutting-edge 3D games, with advanced techniques in rendering and visuals. Yes, you can build 2D games as well, but you will be limited in some ways (may vary from one game genre/style to another), and not using engine 100%.

<div align="center"><p><i>"You can shoot a bird with both a rifle and with a cannon, but what will be reasonable to do?"</i></p></div>

And yes you can also build 3D games with Defold, but you will probably lack some features available in UE and Unity. My point is that you need to find suitable tool for your work and use it. You can shoot a bird with both a rifle and with a cannon, but what will be reasonable to do?


#### When and how did you learn of Defold?
In December it will be 2 years since I first heard of Defold. I was looking for replacement for Corona SDK, which I used for a small game. Unfortunately, the idea and main concept of that game was restricted by phone's screen sizes and with 5 levels it wasn't worth releasing it in the app stores.

Almost exactly at that time I got the idea for Zoo Economy and I wanted to make a quick prototype. I knew that it would be 2D and mostly consist of UI and while Corona SDK was good at creating 'quick and dirty' 2D prototypes, it lacked a good visual editor. A quick search of similar engines brought to my attention Defold and that's when it all started.


#### What do you like the most about Defold?
It's light, it's fast, has a good editor and covers pretty much all of my needs right now. Lua is mostly a good language to work with.


#### What is your favourite game of all times?
Oh, it is hard to pick! But I really love the latest [Arkane Studios](https://www.arkane-studios.com/en) games: Dishonored 1 & 2 and Prey. They a very systematic with clever level-design and a lot of ways to accomplish tasks.


#### What are you working on right now?
For now my one and only project is Zoo Economy. It is almost 2 years old and I hope to finish it in the third. It is a game about exchanging animals without (almost) using money. It has historic campaign based on true events and sandbox mode with customizable settings. It is a 2D game with a lot UI elements and menus. I also use factories for Zoo objects on the map and planes travelling with animals. You can check my [devlog](https://forum.defold.com/t/zoo-economy-strategy-puzzle-play-new-steam-demo/65466) or [visit the Steam store page](https://store.steampowered.com/app/1358110/Zoo_Economy/). After Steam I want to port it to Nintendo Switch and mobile devices.

![Zoo Economy world map](/images/posts/developer-spotlight-denis-volkov/zoo-economy-3.png)

#### The game does indeed have a lot of UI elements! What is your recommendation to someone planning to start a very UI heavy game in Defold?
Research everything and plan first. I already knew that I needed scroll functionality, so I was looking for extension with such functionality. I think it is also better to build dirty prototype and try different extensions and methods before you start ‘main’ production. Game jams are good too, to try something new and experiment. Of course it is very important to [read the gui documentation](/manuals/gui) to have an understanding about what it is capable of. And I can say that the gui in Defold is a very powerful tool in the right hands and with knowledge.


#### How many people are working on the game?
Right now only me. Some art is drawn by me (mostly UI), but I’m not an artist and it’s hard for me. Other images, like animals, mission, events etc are drawn by outsourced artists. Sounds are ordered when I need them. Music as well. It is pretty costly, so there are only 4 track in the game right now, but there should be more on release.

![Zoo Economy world map](/images/posts/developer-spotlight-denis-volkov/zoo-economy-2.png)


#### Which part of your current project are you most proud of?
It is probably the way how I manage nodes in scroll elements. The game is heavily UI centered and often uses scroll elements to store and show animals and other data. And this data itself has additional elements, like images, text, buttons and so on. So to overcome node limits and at the same time optimise the game a little bit I track what elements fits in scroll view and draw only those. You can read about it in more detail with gifs and images in the [devlog](https://forum.defold.com/t/zoo-economy-strategy-puzzle-play-new-steam-demo/65466).

I'm also proud of the way I handle progress bars. I wanted to create a progress bar with round edges, as a base texture it was just rounded elements, but stencils can't use alpha channel to 'cut' things. So I use rectangular stencil mask and I move bar and mask at the same time, keeping the bar to the left side aligned with base and moving mask to the right, exposing more parts of that bar as it is filling.


#### Tell us about your ugliest hack to get a job done!
Almost whole game :) But jokes aside, I use too many global variables, which are stored in main.script.

And the first iteration of the progress bar I mentioned earlier. I used circle node on one of the ends to create round stencil mask. But it was round, so the 'bar' moving inside the mask will end in the beginning of the progress bar. That's why behind it was a second bar, now inside rectangular stencil mask which move simultaneously with first bar in circle stencil mask. And together they create an illusion of rounded progress bar. Yes it was very messy and not well optimised, as around 20 of such bars can present on the scene, but it worked, until I wanted to remake it from scratch.


#### How can the community follow your progress?
You can [follow my studio's Twitter feed](https://twitter.com/cur_foxes). If you speak Russian you can also [follow us on VK](https://vk.com/curiousfoxes). And [our website](https://www.curiousfoxes.com/).

And of course you can follow Zoo Economy's devlog [on the Defold forum](https://forum.defold.com/t/zoo-economy-strategy-puzzle-play-new-steam-demo/65466)!
