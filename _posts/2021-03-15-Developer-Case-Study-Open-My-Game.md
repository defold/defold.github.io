---
layout: post
title:  Developer case study - Open My Game
excerpt: In this developer case study we'll take a look at how Belarusian game developer OpenMyGame are using Defold to create web games on Yandex.Games.
author: Björn Ritzl
tags: ["developer case study", "interview", "html5", "yandex"]
---

One would think that the long and agonizing death of Flash spelled the end for games played in the browser and that the heyday of browser games was long gone. Fortunately this couldn't be further from the truth!

Browser games have seen a tremendous growth thanks to the technological advances made by browser vendors. JavaScript is blazingly fast nowadays and Flash has been replaced by modern web technologies adopted by all major browsers. This new set of standardised browser APIs are often referred to as HTML5. The HTML5 APIs have support for hardware accelerated graphics, low-latency sound playback, gamepads and the ability to play games in fullscreen.

In parallel with the advancements done in the browser we have also seen more and more game engines, especially those focusing on cross platform game development, adopting new technology to create highly optimized games for the web.

We are also seeing a strong movement to democratize game development and make it available to developers across the globe. With the ubiquity of browsers it is no surprise that open source HTML5 game engines such as Phaser and Pico-8 are in the forefront together with a few cross platform game engines also operating in the open source space.

Finally, let's not forget about the players! Numbers show that players are playing browser games like never before on a growing selection of popular game portals offering high quality games as well as quirky and fun games made during game jams.

In this developer case study we'll take a look at how Belarusian game developer OpenMyGame are using the cross platform and source available Defold game engine to create web games on [Yandex.Games](https://yandex.com/games/), one of the leading platforms for high quality web games. We reached out to [Vladimir Timoshkov](https://www.linkedin.com/in/tsimox/), CEO at [OpenMyGame](https://www.openmygame.com/), to learn more.


![](/images/posts/developer-case-study-open-my-game/openmygamebig-logo.png)

**Björn**: Vladmir, can you tell us about the history of OpenMyGame and the games you are making?

**Vladmir**: OpenMyGame was started by three mobile developers, who were a team on programming contests held by [ACM ICPC](https://icpc.global/) while at University. We wanted to create our own projects and decided on games. Games, which is our passion to play, are not boring and challenging to code, which was also a decisive factor for us.

In 2011 there was a rise of mobiles and we found it was a good opportunity to try. We made about 20 single screen puzzle games in a year just for fun. We used [Andengine](https://en.wikipedia.org/wiki/AndEngine) and published them on Android Market (the olds remember this name). We earned our first money from ads, but it wasn't enough to leave our full-time jobs.

At that time the market was shifting to games of better quality and we fully embraced it! In 2012 we developed the most challenging game for our team: Draw & Guess Online. It was native Android, native iOS, native web and with a big server side written in Java. And still it was just a hobby for three guys having full-time jobs not connected with game development!

During the three following years we struggled to make our games earn enough money. It took a lot of efforts in game design and the business part of game development, but we didn't have the funds we needed to make the game to perform.

In early 2016 we decided to quit our jobs just because we got tired of saying "I have no time" to ourselves. We just wanted to check our lottery ticket - are we able to become profitable on the market where we have so much experience if we can use all our energy and time? The answer was found in three months. And luckily it was Yes!

At OpenMyGame we are developing games for a casual audience who wants to use their intellect and brains to play - word games, quizzes, puzzles.


**Björn**: When did you first hear of Defold?

**Vladimir**: I met Alexey Gulev at a local game development event in Belarus in 2018. We found a lot in common to talk about and one of the topics was game engines. He told me that he was playing with a new engine from King and described the advantages of Defold against Unity (one of our main development tools still). So it was a kind of debate, where I was mostly on the Unity side because of business reasons - hiring, community, plugins. It's important to point out that we were talking only about mobiles.  


**Björn**: What made you choose Defold for some of the games your studio is working on?

**Vladmir**: I was following [Alexey's updates on Twitter](https://twitter.com/agulev) and was a witness to his pioneering of Defold. His regular updates were refreshing and upvoting knowledge about Defold in my everyday context.

<div align="center"><p style="font-size: larger"><i>"We can surely say that the basics of Defold can be picked up very easily if a developer has made at least one game before."</i></p></div>

So when in 2019 we decided to port our top game [Sea of Words](https://yandex.ru/games/play/98073/?app-id=98073) to the new platform Facebook Instant, we chose Defold because of its strong HTML5 support. Soon after a very skilled engineer joined our team. He had a huge experience in several engines (but not Defold) and in three months the game was ported. We can surely say that the basics of Defold can be picked up very easily if a developer has made at least one game before.

![](/images/posts/developer-case-study-open-my-game/seaofwords.png)

Unfortunately the outcome on Facebook was negative, we didn't succeed in getting organic traffic and paid users were far away from payback level, but despite that we gained experience and had a game ready to be published elsewhere on the web.

And that's how we bumped into Yandex.Games.


![](/images/posts/developer-case-study-open-my-game/yandex_eng_logo.png)

**Björn**: Can you tell us about your experience releasing games on Yandex.Games?

**Vladmir**: Sure. After getting a lemon (fail on Facebook) we tried to make a lemonade (publishing on other HTML5 platforms). We had several options, primarily Russian big social networks OK and VK. Publishing on both of them is not an easy task because you are supposed to have a server for user data and payments. Also you have to put your game on your static server.

<div align="center"><p style="font-size: larger"><i>"And it boomed! The game has reached top-5 on the platform by downloads."</i></p></div>

We started dealing with that and randomly I found that there was a young but promising platform called Yandex.Games. It took us 2 weeks to add support for their API and the game was there, because user data storage and game hosting is a part of the platform provided by Yandex.Games.

And it boomed! The game has reached top-5 on the platform by downloads. Our first and all of our following games have received the Editor's Choice badge!


<div align="center"><p style="font-size: larger"><i>"Our main rule is if you need an explanation for a feature - it is a bad feature."</i></p></div>

**Björn**: How do you approach game design for the kind of games you do? Are you prototyping a lot of different concepts, working with small groups of testers? How do you make your games stand out from the crowd?

**Vladmir**: It took us some time to realise how to be effective in the niche of word and quiz games. The main idea is not to concentrate on the advanced or mid-core features. It is not important to impress other game developers or colleagues with some rare or difficult mechanics. So our main rule is if you need an explanation for a feature - it is a bad feature. Everything should be picked up on the go, it is a perfect game design for a casual game in our vision. So listen to the target audience and make the game for them, not for yourself personally.

We do not do a lot of prototyping because of the team size. But we are lucky enough to have almost all of our games go global and start to perform.


**Björn**: Yandex.Games offers several monetization options. What is your monetization strategy for the games you release?

**Vladmir**: For now Yandex.Games supports in-app purchases and a good inventory of ads (banner, interstitials, rewarded). We support both ads and IAPs, but advertisement is the most important for us just because of the genre we are in.


**Björn**: What is the publishing process like on Yandex.Games? I'm thinking of things such as review time, QA and analytics

**Vladmir**: Shipping time is measured in minutes for us, as we know the best time to send games for moderation (working hours in Russia). And also we have good relations with the Yandex.Games platform team. We usually tell them about a new cool feature to come, and they are always eager to check it very fast.

Simple QA is done by the platform team for every update to accept a new version of the game. Because Yandex.Games tend to be a place for high quality games, they have to check that the game is still the same as described and it supports all the technical requirements. Product QA is on the publisher side.

Analytics tools can be used according to the publisher’s choice. We use [Yandex.Metrica](https://metrica.yandex.com/) as a basic tool and also [GameAnalytics](https://defold.com/assets/gameanalytics/) because it is perfect for games.

![](/images/posts/developer-case-study-open-my-game/yandex-metrica.jpeg)

<div align="center"><p>Source: https://metrica.yandex.com</p></div>


**Björn**: What are your predictions for the next few years when it comes to browser based games?

**Vladmir**: The future is bright at least for our niche - smart casual games. I think just a little more integration is needed from mobile operating systems to put an icon on the screen, support notifications and other platform specific features.


**Björn**: What are your top three arguments for using Defold for your HTML5 games?

**Vladmir**:

1. Small build size
2. Fast and stable runtime
3. Good editor


<div align="center"><p style="font-size: larger"><i>"There is no critical issue or missing feature from my perspective and for our engine usage"</i></p></div>

**Björn**: If you could wish for one new feature to be added to Defold what would that be?

**Vladmir**: For me it is hard to say because I am not responsible for development, but what I see is that even if there is a problem our team can deal with it. There is no critical issue or missing feature from my perspective and for our engine usage.


**Björn**: What does the game development community in Belarus look like?

**Vladmir**: The professional gamedev community is not very big and active. We have several events in a year, but they are usually organized from outside the country. So for now gamedev Belarus is a bright part of the big Russian gamedev society.


<div align="center"><p style="font-size: larger"><i>"We decided to start an internship program in our city with a quite sophisticated approach"</i></p></div>

**Björn**: I've heard that you have a serious approach to hiring with your own internal game developer academy. Can you tell us about your hiring process to find new promising talent?

**Vladmir**: Yes, we faced a problem of hiring Defold developers, there are not so many of them, and the biggest part of them are indie developers who want to make their own games and don't want to be hired or can't pass our technical interview. So we decided to start an internship program in our city with a quite sophisticated approach.

At first we send a questionnaire of five small functions to code in any language. If it is done correctly we have an interview to check tech skills more deeply. Then we invite top-3 applicants to a 2-month internship.

During the first two weeks students solve algorithmic problems chosen from [HackerRank](https://www.hackerrank.com/). It is very important for us to produce efficient code and we always encourage developers to think about performance.

Next two weeks are set aside for the first project on Defold. We use [Fruit Ninja](https://www.halfbrick.com/games/fruit-ninja) gameplay as a base. The main goal is to create a complete project with a new tool.

The last month is for a "diploma" project, where we pay much attention to project structure, OOP, and extendability.


**Björn**: Are you currently hiring?

**Vladmir**: Yes, and we hire remotely, so feel free to [contact us](https://www.openmygame.com/#_contacts).


![](/images/posts/developer-case-study-open-my-game/openmygame2.jpeg)

<div align="center"><p>Check out the Defold t-shirt!</p></div>


**Björn**: Thank you! How can the community follow the progress of OpenMyGame to learn of new games and developments?

**Vladmir**: Thank you very much for the talk. Follow us on [Instagram @openmygame](https://www.instagram.com/openmygame/).
