---
layout: post
title:  Creator Spotlight - Marius
excerpt: In the third Defold Creator Spotlight we invited Marius, lead developer at Critique Gaming, to tell us a little bit about himself and his current project.
author: Björn Ritzl
---

In the Creator Spotlight posts we invite Defold users to present themselves and share a bit of their background, their work and things that inspire them. It is an excellent opportunity for the community to come together, to recognise achievements and to share some of the great work done by Defold users.

In the third Defold Creator Spotlight we invited Marius, lead developer at [Critique Gaming](https://critique-gaming.com/), to tell us a little bit about himself and his current project.



#### What is your name?
Marius Petcu.


#### What is your background (age, country, occupation or anything else you like to share)?
Hi! I'm 25, I'm a software dev and I'm currently working at [Critique Gaming](https://critique-gaming.com/), a small indie studio we founded in Bucharest 3 years ago, wanting to make the kind of games we love to play ourselves: pointful, socially aware games that don't shy away from mature topics.


#### When and how did you learn of Defold?
If I remember correctly (it was 4 years ago, I think), I believe somebody told a colleague about it at ComicCon or some other local game-dev related event and then he told me.


#### What do you like the most about Defold?
It's simple and easy to grasp. I love the fact that I can mentally keep track of all of its features so when I need to do something, I know exactly where to look. Also, we can prototype things really fast in Defold.


#### What is your favourite game of all times?
Really hard to say... There's just so many good games! First few games that pop into mind are [The Stanley Parable](https://store.steampowered.com/app/221910/The_Stanley_Parable/) and [NieR: Automata](https://store.steampowered.com/app/524220/NieRAutomata/). Oh! And [Vampire the Masquerade: Bloodlines](https://store.steampowered.com/app/2600/Vampire_The_Masquerade__Bloodlines/) (because I'm a bit of a VtM nerd).


#### What are you working on right now?
We're not really at a stage where we can share more details, but it's really exciting (and maybe a bit related to one of the previous games I mentioned). It's a bit different from what we've done in the past, but still very close to our hearts.

Meanwhile, maybe check out our previous project, [Interrogation: You will be deceived](https://interrogation-game.com/).

![Interrogation: You will be deceived](/images/posts/interrogation.png)

#### Which part of your current project are you most proud of?
If I'm talking personal pride, probably the way the data propagates through the game. It's quite a numbers-heavy game with a lot of data dependencies. I made a small Observable module that allows you to pub/sub to other values, which makes reacting to data changes or calculating derived values quite easy. I'm going to open source it in Crit pretty soon. ([Crit is a small, open source](https://github.com/critique-gaming/crit), poorly documented but quite thrifty collection of modules that we made and tweaked over the years and that we carry over from project to project).

If I'm talking pride I take in the game overall, I think I like the way the UI looks the most. It still has some rough edges and some awfully terrible UX in some places (hence why it's a work in progress), but the general direction is pretty awesome. Cătălin, one of our colleagues, spearheads this and he's amazingly efficient at it. He would make something in Photoshop, show us the mock on Discord one day, then it would be a fully functional GUI scene with working widgets the next day.


#### Tell us about your ugliest hack to get a job done!
I'm sure I've done worse transgressions, but these two are the only ones that come to mind right now:

In Interrogation, we had some unrelated music cutting off after a sound bank change at one point. After a few hours of fruitless debugging, I just commented the line that would free the sound bank. It's leaking memory to this day if you go past Episode 8, but hey, it works!

Still in Interrogation, I remember having an issue with Defold on macOS Mojave or so that would draw a blank screen if we activated Dark Mode from Info.plist. Resizing the window would fix it. I still wanted dark mode to work, so, at startup, I'm using [DefOS](https://github.com/subsoap/defos) to shrink the window by 1px, then enlarge it back to its original size. This is still in production.


#### How can the community follow your progress (Twitter, blog, website etc)?
* Our website (you can find our Social Media links over there): https://critique-gaming.com
* Our GitHub: https://github.com/critique-gaming
* My GitHub: https://github.com/dapetcu21
