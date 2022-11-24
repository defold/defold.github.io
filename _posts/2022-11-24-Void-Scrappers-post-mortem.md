---
layout: post
title:  Void Scrappers post mortem
excerpt: Void Scrappers is a frantic space survival game released on Steam this year. Read on to learn about the development of the game.
author: Björn Ritzl
tags: ["creator spotlight", "interview"]
---

Alex, welcome back to another creator spotlight post! Last time we had the pleasure of interviewing you was in July 2020, [right after your Steam release of Fates of Ort](https://defold.com/2020/07/20/Creator-spotlight-Alex/). At that time you mentioned that you were in the very early stages of a space travel simulation game (codename Generation Ship) and from November 2021 we were able to follow the progress of this game in a [development diary on the Defold forum](https://forum.defold.com/t/generation-ship-game/69640). The game seemed to progress rather nicely up until sometime in April this year when the updates ceased and only two months later you made a surprise announcement of [Void Scrappers](https://store.steampowered.com/app/2005210/Void_Scrappers/), the frantic space survival game that we’ll focus on in this interview.

__Before we dive in, can you please tell us a bit more about the period after the release of Fates of Ort and the development of Generation Ship? What happened during that period of time and is Generation Ship still a game that you plan to release at some point?__

*Alex: The immediate aftermath following Fates of Ort’s release consisted mainly of frantic patches and bug fixing. I released some content updates, such as Hero Mode in September. There was also some time spent getting the game launched on [GOG](https://www.gog.com/game/fates_of_ort) (thanks to [dapetcu21](https://forum.defold.com/u/dapetcu21) for sharing the [GOG SDK implementation](https://forum.defold.com/t/gog-sdk/65210/19), without which I would not have been able to launch on GOG at all!)*

*As early as July 2020, I began working on a prototype for another [space game](https://forum.defold.com/t/space-game-title-tbd/65734). This was to be focused on a small crew of aliens on a centuries long journey, with a stylised depiction of the mutative havoc wrought on their genetic makeup leading to both upgrades and debuffs. The scope was significant: Endless open galaxy to explore, with combat and narrative encounters. It was quickly apparent that the game was too ambitious and the genetics based gameplay was too convoluted. The arrival of my firstborn daughter that autumn provided an excellent excuse to cancel the project.*

*The remainder of 2020 and beginning of 2021 was spent overhauling the gamepad controls for Fates of Ort, which culminated in the [release on Nintendo Switch](https://www.nintendo.com/store/products/fates-of-ort-switch/) and the fulfilment of a childhood dream to publish a Nintendo game.*

*Once the Switch release was completed, I began working on the Generation Ship game you mentioned. We took some of the ideas from the now cancelled mutation game, but opted to reduce the scope drastically and attempt to achieve an extremely abstracted experience. We actually got very far into the development life cycle. Most of the core features are implemented and we were slowly beginning to add final graphics. However, due to various reasons progress was slow, and in my opinion the core gameplay requires changes before it reaches a standard worthy of public release. Certainly, I had much more success sharing Void Scrappers with friends and family compared to Generation Ship. The latter required a lot of explanation (“what am I supposed to be doing?” was a common question) and seemed to require a fair bit of time for people to “get” the concept.*

__Thank you! Ok, let’s move on and talk about Void Scrappers. On Steam, the game is described like this:__

*“Blast hordes of alien ships into junk. Collect the scrap to upgrade your ship into an unstoppable force of destruction. Unlock new characters and weapons and upgrade your stats between runs.”*

![](/images/posts/void-scrappers-post-mortem/void-scrappers-game.png)

__If we disregard the official description of Void Scrappers for a while I’d like to start by asking what Void Scrappers means to you personally?__

*Alex: Void Scrappers, to me, is pure gameplay. It is a palate cleanser for someone that has jumped from one enormously ambitious project (Fates of Ort) to the next (various iterations of generation ship games). It is playing to the strengths of an indie team, where a small number of people can focus a large amount of energy on polishing a tiny bit of gameplay. This just isn’t possible for a AAA sized team, which must make games with extremely wide appeal in order to sell the millions of copies needed to recoup investment costs..*

*Commercially, Void Scrappers is also an attempt to find a viable niche where I can balance artistic expression with making a living. I have little interest in the mobile gaming space, but I also struggled with the scope of a game the size of Fates of Ort. Something like Void Scrappers is closer to what I see myself doing long term.*

__The description above mentions that you will be *“unlocking new characters and upgrading stats between runs”*. While this is an accurate description of the game it is also in my opinion only the tip of the iceberg and a rather underwhelming description of the number of possible combinations of character abilities and the semi random selection of weapons you get to choose from during each run.__

__The large number of combinations opens up the game to many different tactics and play styles. What was your approach to balancing all of these upgrade combinations?__

*Alex: One of the key concepts we try to convey in Void Scrappers is “power”. We want the player to start off feeling puny, but very rapidly escalate in power until the screen is covered in destructive chaos. So, the main concern is ensuring everything (weapons, upgrades, characters) have the potential to become really powerful. Very rarely did we nerf anything, but rather opted to buff everything up to the highest denominator. Indeed, we sometimes intentionally came up with features that combined with other features would “break” the game (i.e. make the player near invincible, or enable them to play beyond the intended end game). This is what players interested in this genre enjoy.*

__That’s a really fascinating approach to the problem. You can indeed become really powerful with the right combination of upgrades! Do you happen to know what the highest recorded threat level is in Void Scrappers?__

*Alex: I have seen users reporting threat 150 and upwards. Really, the limitation becomes resource related! I see evidence of sprites not rendering anymore (implying there are more than 32k active at one time, which is the setting I have in game.project). I could of course force an end somehow, but I get the sense that people really enjoying breaking the game (literally).*

__The launch seems like a pretty big success on Steam. Based on your experience releasing Fates of Ort and Void Scrappers on Steam, what are the most important things developers should do to have a successful game launch on Steam?__

*Alex: Unsurprisingly, there are a lot of factors!*

*The key art is extremely important, and it’s almost a science. It is worth paying a professional artist to make it, and indeed if you only spend money on one thing when launching on Steam - this is it.*

![](/images/posts/void-scrappers-post-mortem/void-scrappers-key-art.jpeg)

*A good trailer is important, but what “good” means in this context is quite specific to Steam. You want a trailer that jumps right into gameplay. Steam shoppers aren’t watching trailers for studio logos, narrative or slow cinematic shots. They want to know how the game plays, and that’s it.*

*Demos are extremely important for visibility. They enable you to participate in Steam Next Fest, get content creator coverage, and vital feedback from players that like the genre and aren’t your friends and family. Since the launch of the demo, Void Scrappers changed massively due to the player feedback and I honestly don’t think the game would have done as well as it did had we not had access to demo feedback and chose to act upon it.*

*Finally, and this may be a bit trite, the most important factor is a high quality game. Good marketing materials only serve as multipliers to the baseline standard set by the game itself.*

__The key art for Void Scrappers is fantastic and worth every penny! Who is the artist?__

*Alex: Definitely agree! The artist is called [Andaerz](https://twitter.com/Andaerz) (warning: link may be NSFW).*

__Another part of the game that is really good is the sound tracks. Who made the music in Void Scrappers?__

*Alex: The music was made by the very talented [Christoph Gray](https://twitter.com/waterytartt). He also did the soundtrack for Fates of Ort, and will hopefully make music for whatever we come up with next too!*

__It is inevitable to make comparisons between Void Scrappers and the hugely successful game [Vampire Survivors](https://store.steampowered.com/app/1794680/Vampire_Survivors/). How much inspiration was Vampire Survivors and what other sources of inspiration did you have when designing Void Scrappers?__

*Alex: The comparison is both inevitable and appropriate. Vampire Survivors is what triggered the project, and has been a huge influence in many of the core mechanics. However, the idea has been bubbling in my head for many years. Here is a prototype from 2016 (made in Flash, just before I discovered Defold):*

![](/images/posts/void-scrappers-post-mortem/old-flash-prototype.gif)

*This project never really went anywhere. As you can see from the minimap in the GIF, the intent was to have locations that could be visited and explored. This is a common thread in my recent projects: Overambitious scope!*

*I would also like to highlight the super addictive [Rabid Robots](https://www.kongregate.com/games/Ross_/rabid-robots) by [Ross Grams](https://forum.defold.com/u/ross.grams/summary). Ever since I played it I have been desperate to make something like it.*

*In terms of the style and flavour of the game, I am a fan of the earlier entries in the Borderlands franchise. This is the type of vibe we tried to capture with the tone of the dialogue provided by the scrappers in the game.*

__The game handles an impressive number of enemies and bullets. How are you handling collision detection between such high numbers of objects?__

*Alex: Credit goes to [Selim Anaç](https://forum.defold.com/u/selimanac/summary) and his fantastic [AABB extension](https://github.com/selimanac/DAABBCC). It’s a bunch of algorithms by people much smarter than me, packaged by Selim into a super useful extension. The performance is brilliant and it can handle thousands of objects. I can’t thank Selim enough for this.*

__What were the main technical challenges you were faced with during development and how did you solve them?__

*Alex: Performance has been the biggest hurdle for sure, and I think that is the case for most games in the “horde survival” genre. AABB was the biggest contributor to the fact that the game actually runs, but beyond that I made many choices with performance in mind.*

* *Enemy objects don’t have individual script components, but are instead all controlled by one central manager script. This script iterates over the enemies in batches, spreading updates over many frames. Enemies move using go.animate, meaning they don’t have to be updated every frame.*
* *Enemy behaviours are simple - they mostly just follow the player and shoot at you.*
* *I dipped my feet into manual control over the garbage collector for the first time, ensuring it runs in a designated frame where no enemy updates are performed.*
* *I followed some of [David Lannan’s](https://forum.defold.com/u/dlannan/summary) excellent [optimisation tips](https://forum.defold.com/t/lua-and-luajit-best-practices/68405), like creating local references to frequently called methods within tables (e.g. local table_remove = table.remove)*
* *Ensuring [frustum culling](https://forum.defold.com/t/defold-1-3-1-has-been-released/70673#frustum-culling-3) was enabled was a no brainer. This automatically prevents sprites being rendered if they are not visible, which saves on performance. I also applied simplifications to enemy behaviours when they are off screen. For instance, they do not fire bullets, and they do not perform any crowd position management.*

__As with Fates of Ort you decided to use the Defold game engine to create Void Scrappers. What makes Defold a good choice for a game such as Void Scrappers? And are there any areas where it could be improved?__

*Alex: The positive aspects of Defold from my previous interview remain the same:*

* *Lua*
* *Focus on 2D games*
* *Easy deployment to multiple platforms (add PlayStation to the mix soon!)*
* *Ease of use*
* *Free (though I am happy to [support the engine](https://defold.com/donate/), and you should too if you can!)*
* *Wonderful community*

*This time around I would also like to add that I am very happy with everyone on the Defold team. I feel the engine is in very good hands. The team is incredibly skilled and professional. There is a sense that every feature is deliberately considered and designed, which is in part evidenced by the rarity of breaking changes.*

*Because of all of these points, my next game will be made in Defold too.*

*In terms of improvements, I would generally love to see more developers targeting desktop/Steam. If it weren’t for users like [Pkeod](https://forum.defold.com/u/pkeod) and [dapetcu21](https://forum.defold.com/u/dapetcu21) I would have struggled to release on Steam and GOG. The more users targeting desktop, the more we will all benefit from community sourced improvements and feature requests.*

*Additionally, some of my pet topics:*

* *I would love to see more work on frustum culling. This is already a reason why Void Scrappers runs so well!*
* *While AABB is great, there are cases where I would like to use Defold’s collision objects. For those to work well for hordes of enemies, it would be a necessity to [process their collision results without requiring a script component](https://github.com/defold/defold/issues/7151).*

__Which is your favorite character in the game and why? And are there characters that didn’t make the cut?__

*Alex: I’ll nominate in a few different categories!*

*I think Remington is the best character (though hardcore players will likely make a case for Pyrek). The double damage coupled with some extremely powerful no-shield skills can quickly make him unstoppable.*

*Since lasers are my favourite weapon type, I enjoy playing Prismatrix a lot.*

*In terms of flavour, Murphy is my favourite. He’s been in the game the longest, and I really enjoy his personality.*

![](/images/posts/void-scrappers-post-mortem/void-scrappers-characters.png)

__What are your plans for Void Scrappers? Is the game done or can we hope for more updates? What about console support?__

*Alex: As of writing, we are working on a tenth character and a new weapon. For the moment, that is the last significant content update that we have scheduled. There may be more, but nothing is planned at the moment.*

*We expect to launch on the Nintendo Switch in 2023, and would love to try to get the game on the PlayStation as well when the time comes!*

__Are you able to share some insights into game statistics collected since the launch? I’m curious to learn more about things such as playtime, user demographics and technical market split (operating systems, screen size and so on).__

*Alex: Stats are fun!*

*The median playtime is 3 hours 52 minutes. This is absolutely fantastic! The average playtime is 7 hours, which means there are some superfans that are dragging the average upwards. 7% of players have played longer than 20 hours. Generally it seems like people are doing really well - with 36% of users having defeated the final boss. This is much higher than I expected.*

*We localised the game into eight languages (Simplified Chinese, Traditional Chinese, Japanese, Korean, French, German, Spanish, Brazilian Portuguese). Of these, Japan was the star performer, with 14% of all units sold, followed by France and Germany (7% and 6%). The biggest disappointment was China (2%). I don’t have any particular insight into why it worked so well in Japan but not China, other than that it seemed to have gained traction with Japanese content creators but failed to do so with their Chinese counterparts.*

*Anecdotally, I would say that the Steam Deck has driven some sales (especially since the game has been Verified for the Steam Deck by Valve!). However, Linux units sold are approximately the same as for Fates of Ort (which released long before the Steam Deck was available), coming in at about 5% of all copies for both games.*

*People seem to be happy with the game, with a refund rate of 5.4% (8.7% for Fates of Ort). I would have been happy with anything less than 10%, which I believe is near the Steam average refund rate.*

*Approximately 36% of players have played Void Scrappers with a controller. 59% of those are Xbox controllers, followed by 23% Steam controllers, 14% PlayStation, and 2% Switch (!).*

*Where the operating system is reported, Windows represents a staggering 94.2% of users, with Linux coming in at  3.2% and Mac at 2.5% (this data is from wishlists, hence the difference compared to the Linux number mentioned above). Other hardware data is opt-in, and unfortunately not enough users have done this for the data to be of any interest.*

__Thank you for the detailed answers on stats! The average playtime numbers are very impressive indeed (and I must confess that with 25 hours of logged playtime I’m one of the players dragging the average upwards!)__

__You mentioned early in the interview that Void Scrappers is “an attempt to find a viable niche where I can balance artistic expression with making a living”. My last question before ending this interview is if Void Scrappers lives up to this goal? Do you consider it a financial success?__

*Alex: Some friends and family have asked me - “can you stop working now?” and my answer has been: “Yes!”*

*“…for a few weeks.”*

*The serious answer to the question is that yes, Void Scrappers is so far a financial success. This does depend on long term sales of course, and how the game performs on the Nintendo Switch and other platforms. It is most certainly looking like it will significantly outperform the results of Fates of Ort.*

*What this means is that my current arrangement of being a stay-at-home dad / indie developer can continue for at least another few years even without any further releases. Of course, I am hoping to release one or more games in that time, and hopefully they can perform reasonably well also.*

*Thanks for the interview and for the insightful questions!*
