---
layout: post
title: Power Fantasies - 8BitSkull on Skull Horde and Sustainable Indie Development
excerpt: We invited Alex Asvegren from 8BitSkull back to the Defold blog to talk about Skull Horde, Steam launches, scope, sustainability, and why Defold remains the right engine for the studio.
author: Paweł Jarosz
tags: ["spotlight", "interview", "steam", "consoles", "nintendo switch", "indie", "8bitskull"]
---

We invited Alex Asvegren from [8BitSkull](https://www.8bitskull.com/) back to the Defold blog. Since our first interview after the release of [Fates of Ort](https://store.steampowered.com/app/895480/Fates_of_Ort/), 8BitSkull has shipped [Void Scrappers](https://store.steampowered.com/app/2005210/Void_Scrappers/), [Bore Blasters](https://store.steampowered.com/app/2398170/BORE_BLASTERS/), and now [Skull Horde](https://store.steampowered.com/app/3199360/Skull_Horde/).

This time we talked about the studio strategy behind those games, the launch of Skull Horde, Steam marketing, localization, console plans, Defold performance, and what it means for a small indie studio to build a sustainable rhythm around compact power fantasies.

![8BitSkull games made with Defold](/images/posts/newsletter-may-2026/8bitskull.webp)
<div align="center">
_8BitSkull has shipped four commercial Defold games: Skull Horde, Bore Blasters, Void Scrappers, and Fates of Ort_
</div>

### Introduction

##### Alex, welcome back to our blog! We first spoke when Fates of Ort had just released and you were just starting with Defold. Later, we talked about releasing Void Scrappers on Nintendo Switch. Now you are here with four commercial Defold games shipped as 8BitSkull, an established and successful indie game studio. How would you introduce 8BitSkull today, especially to new readers?

Thanks for having me yet again! I hope I have something sufficiently interesting to say that warrants a third interview.

8BitSkull is a small indie studio based in Scotland. We focus on games that deliver compact and exciting power fantasies, often with elements of action and destruction. We primarily target the PC market via Steam, but also sometimes consoles like Nintendo Switch, thanks to Defold for making that easy!

##### You have now released four games made with Defold: Fates of Ort, Void Scrappers, Bore Blasters, and now Skull Horde. All are on PC, and some are already on Nintendo Switch. Your games feel very different on the surface: fantasy RPG, space survivor, mining roguelite, and necromancer auto-battler. But they share a strong sense of escalation and power. Is "satisfying power fantasy" now a deliberate 8BitSkull design pillar?

Yes. Our first commercial project, Fates of Ort, was a naive labour of love. We did not particularly concern ourselves with market research or anything like that, and I think the reason the game did even moderately well was through the sheer amount of earnestness poured into it. It was not a sustainable approach though. With a development time in excess of 2.5 years, we would not be able to continue as a studio with games like this.

We tried to scope out a new direction, abandoning a few prototypes on the way. Finally, Void Scrappers ended up being our next released title. In many ways it was the polar opposite of Fates of Ort: tight scope, pure gameplay, and a focus on replayability. Crucially, development time was less than a year. I realised we had stumbled upon the centre of this diagram:

![8BitSkull studio strategy diagram](/images/posts/interview-8bitskull/studio-strategy.webp)
<div align="center">
_The studio strategy diagram behind 8BitSkull's current direction_
</div>

In order to formalise this learning and make sure it would not be forgotten, I wrote a document I refer to as our studio strategy. This details our approach as a studio, and in terms of gameplay elements it includes these four pillars:

- **Power** - enjoyment through gaining strength in the game world
- **Excitement** - fast pace, intensity, and thrills
- **Destruction** - joy through causing chaos, mayhem, and destruction
- **Completion** - upgrades, unlocks, and achievements

I think the existence of this strategy becomes readily apparent when evaluating Bore Blasters and Skull Horde.

##### What has changed most in how you think about game scope, production, and sustainability as an indie developer?

The aforementioned studio strategy document covers this area as well. Every game idea we come up with is assessed against this document. A game does not have to meet every criterion. For example, we would not reject a game idea just because it does not have enough "destruction".

Beyond gameplay, we also assess factors like scope and production requirements, which directly inform sustainability. We consider how many systems we can carry over from project to project, whether a game idea leverages our experience, and so on. We design with gamepad input in mind so that our games work flawlessly on the Steam Deck and are trivial to bring to consoles like Nintendo Switch. We develop with localisation in mind from the start. We know how important demos are as a marketing tool, so we make sure to pick game ideas that demo well.

The final factor is scope. How much development time is required to launch? Every unit of development time is a cost that needs to be recovered, and thus increased scope needs to come with an increase in expected returns. Our soft target is about a year of development per game, though this often slips. We think we can strike a balance between a scope sufficiently large to make a meaningful game, but not so large that an unexpected failure would damage the studio.

### Skull Horde

##### Skull Horde is described as an auto-battler dungeon crawler where you play as a flying skull necromancer. What was the original spark for that idea?

I have always been drawn to minion-managing roles in ARPGs. I love the feeling of summoning a horde of minions and having them do the fighting for me. At its core, we are trying to recreate the feeling of playing a Diablo 2 summoner necromancer, just modernised and with our own twist.

![Skull Horde made with Defold](/images/posts/interview-8bitskull/dungeon1.webp)
<div align="center">
_Skull Horde is a real-time auto-battler dungeon crawler where you play as a flying skull necromancer_
</div>

##### How did you decide which systems should be automatic and which should stay under direct player control?

Simple and limited input is called out as something desirable in our studio strategy. We do not like tutorials, as both designers and players, so we like to aim for designs that minimise the amount of tutorialisation needed. Automated systems help achieve this goal.

##### In Void Scrappers, you talked about letting players become absurdly powerful rather than nerfing everything into balance. Did that same philosophy carry into Skull Horde?

To an extent! We keep it in mind, but sometimes it is not possible. I was quite concerned with players finding a favourite build and always heading straight for it, neglecting the joy of discovering other builds. Skull Horde is quite generous with rerolling and banishing, which means this is very achievable for players. As a result, we did need to nerf away some properly unbeatable builds, such as hordes of rats causing chill on hit and an infinite invulnerability engine.

However, when designing, I try not to be too heavy handed. One mechanic I am quite pleased with is the Curse system. At higher difficulties, players are forced to pick Curses that add additional challenges. Multiple Curses beyond the minimum can be selected, which gives access to Rites, powerful boons.

The game detects what builds a player uses a lot and offers up related Curses. Using Burn a lot? One of the Curses on offer will steer you away from it while buffing something else. This gives the player the opportunity to intentionally avoid a certain build trope in exchange for a reward. There are always enough options to choose from, so the player is not forced to abandon their favourite playstyle, but the design nudges them to give other builds a try.

<div align="center"><p style="font-size: larger"><i>"The player is not forced to abandon their favourite playstyle, but the design nudges them to give other builds a try."</i></p></div>

![Skull Horde builds](/images/posts/interview-8bitskull/summon3.webp)
<div align="center">
_Various builds in Skull Horde_
</div>

##### What was the hardest part of making summoned minions feel readable, useful, and satisfying without turning the screen into visual noise, especially because there are hordes of enemies approaching as well?

We have some experience with this, partly from Bore Blasters but particularly from Void Scrappers. It is difficult to fully solve this because the visual carnage is part of the fun, but here are a few things we implemented in Skull Horde:

- Single-pixel-thickness outlines for units, so they are distinct from each other
- Squad units have colour accents matched to their type, such as Rogue or Beast, that make them distinct from other classes
- An option to highlight the player by rendering an animated circle around the character
- An option to turn off things like health bars or stack icons

![Skull Horde minions and enemies](/images/posts/interview-8bitskull/skull-horde-gameplay.webp)
<div align="center">
_The visual carnage is part of the fun, but readability still matters_
</div>

### Steam

##### Skull Horde launched with strong reception and a very warm welcome. What did players understand immediately, and what did you have to patch, explain, or improve after launch?

The single biggest post-launch issue we experienced was an issue where some Windows users with unicode characters in their username encountered a crash when launching the game, particularly impacting East Asian users. As confused and disappointed players began leaving negative reviews, our score started dropping and threatened to go below 80% positive. At 70%, the score would turn into a "Mixed" rating, which would have been disastrous for the launch.

In a panic, I reached out to the Defold team, who kindly generated a hotfix on a Saturday morning to resolve the issue for me! I am extremely thankful for this as it had a huge impact on the success of our launch. Our score has now stabilised at 82% positive.

There were a few additional crashes happening as well. The Defold team helped me resolve the ones caused by my implementation, and fixed the ones that were a problem on the Defold side.

Beyond that, I have been hard at work over the past few weeks, doing daily updates with bug fixes, performance improvements, and quality of life features. As the pace of these has slowed down, I have started working on the first big post-launch content update.

##### Your games tend to sit in crowded genres, but you always manage to find a sharp appeal: space horde survival, machine-gun mining, skull necromancer auto-battling. How do you come up with those ideas? How do you test whether an idea is marketable enough before committing to production?

Actually, I am moving away from hooks a little bit! I think all the hooks for my games have been fairly weak. I am not even sure what the hook was for Void Scrappers - "Vampire Survivors in space", maybe? Now I try to frame the appeal of a game in terms of the "fantasy" the player gets to experience.

Blasting swarms of enemies in space in an unstoppable racing ship, mining thousands of gems with a ridiculous gatling gun, amassing a huge horde of skeletal warriors... These are not really hooks, but they are super appealing fantasies.

If you are interested in this concept, I can strongly recommend this video by Jonas Tyroller: [What Sells on Steam: You Don't Need a Hook](https://www.youtube.com/watch?v=uiBDyZ-Pf2M).

##### How much do you follow genre trends, such as survivor-likes, roguelites, and auto-battlers, and how much do you try to deliberately move close to or away from them?

I do not tend to particularly chase or avoid genre trends. I do get inspiration from contemporary games, but I do not intentionally set out to quickly chase trends. I am fairly comfortable that the audience I have identified for my games will continue having the same preferences, so I do not need to worry too much about trends.

##### Did the demo, wishlists, festivals, streamers, or early community feedback play a major role in shaping the final release? What would you do the same again?

Here is a chart of the wishlists gathered before release:

![Skull Horde wishlists before release](/images/posts/interview-8bitskull/wishlists.webp)
<div align="center">
_Skull Horde wishlists before release_
</div>

Notably, we did not rely on festivals, other than Next Fest, or social media at all. The marketing strategy should be tailored to the type of game you are developing. A game trying to go viral should probably focus more on social media, but our gameplay-first approach is more suited for a demo and content creator strategy.

We had the demo out for about a year before release, which was tremendously valuable in terms of gameplay feedback, but also for bug fixing and spotting technical issues.

##### Which markets are most important to you, and which languages would you recommend other developers consider for localization?

Skull Horde unit sales are distributed as follows:

- United States - 28%
- China* - 16%
- Japan* - 9%
- Germany* - 8%
- Korea* - 5%
- Canada - 3%
- United Kingdom - 3%
- France* - 3%
- Australia - 2%
- Poland* - 2%

\* = localised

Due to regional pricing, the US will have contributed way more than 28% of revenue. Nevertheless, this distribution shows the importance of localising into languages beyond English.

We tend to localise into the following languages:

- Simplified Chinese
- Japanese
- Korean
- French
- German
- Spanish
- Brazilian Portuguese
- Polish

We intentionally do not bother with Traditional Chinese, Spanish (LATAM), and Portuguese. I think there is a high degree of mutual intelligibility for these languages, and if not, we have not ever received any complaints!

There are more languages we could add, such as Italian or Turkish, but you have to draw the line somewhere. We use human translators, so each language is a cost and an administrative burden.

When choosing what languages to localise into, you should consider:

- How big is the market?
- How well does that market speak English?

For example, it might not be worth it to translate into Dutch or Swedish, as the markets are not huge and English proficiency in the population is very high.

##### What do you think indie developers misunderstand most about Steam launches?

Good question! Here are a few things people should know:

- Do not shadowdrop your game! Your Steam page should be up throughout your development cycle, gathering wishlists. Your launch is really important, and it is very hard to recover from a bad one.
- Make sure you release a demo long before launch, and participate in a Steam Next Fest. Pick a Next Fest late in your development cycle so that your demo is in a polished state.
- You can be successful without posting on social media. I mention this because I have always struggled to get traction on social media, and it has felt like a waste of time posting daily into the void. So I give you permission to ignore it, if it does not suit you or your game. Instead, treat the demo itself as a very powerful marketing tool.
- Make sure to get 10 reviews from paying customers, meaning free keys do not count, quickly after launch. Same day if possible! This unlocks base visibility on Steam. Not explicitly, but it seems having a review score is required for certain visibility mechanisms. You are not allowed to reward people for leaving reviews, or ask for them in game, but you are allowed to yell at people in your community!
- If it is feasible, try to aim for more than 5,000 wishlists to have a shot at appearing in the Popular Upcoming widget. You can verify whether you have enough by going to your game on [steamdb.info](https://steamdb.info/) and checking the "Store data" section under the Charts tab. If you have a "top wishlists" ranking, you will appear in Popular Upcoming. Note that there is currently a change in the Steam beta client that might remove Popular Upcoming altogether, so it is possible this information is stale when you read it!

I am not sure I have covered everything, so if anyone is interested in discussing this, the #business channel in the community Discord is a place you will find me.

### 8BitSkull Studio

##### How early do you bring artists and musicians into a project? Do you prototype alone first, or do visuals and audio shape the core loop from the beginning? Christoph Gray's music has been part of earlier 8BitSkull titles. How important is continuity with collaborators when building a recognizable studio identity?

Collaborator continuity is super important. I have worked with the same people for years, and losing any one of them would be a big setback. They are reliable, quality people with detailed knowledge of the workflow.

I tend to take ownership of project selection myself, because I am the one running the business side and will be investing the most in terms of man-hours and money. Once a project is selected, I involve the rest of the team early. We develop things like visual identity cooperatively.

![Skull Horde concept art](/images/posts/interview-8bitskull/concept.webp)
<div align="center">
_Skull Horde concept art sketches_
</div>

##### From the outside, 8BitSkull looks like a studio that has found a repeatable rhythm. Is that accurate, or is every project still a leap into uncertainty?

Since the development of the studio strategy, we have definitely managed to hit our stride with multiple consecutive successful projects. I think in large part we owe that to the intentionality we apply to project selection, ensuring the games we develop suit our strengths and expertise. This is a creative industry though, so every project is still a risk. This is why we try to keep scope tight, so that any failures do not have an excessive impact on the survival chances of the studio as a whole.

##### You previously spoke candidly about cancelled or paused projects. What did those projects teach you that directly improved Void Scrappers, Bore Blasters, or Skull Horde? And what does success mean for 8BitSkull now?

I think they taught me a few things that we have already touched on. Primarily, this was about tight scope, with reasonably defined project boundaries in place before development starts. The abandoned projects were more aligned with Fates of Ort, in that we had a vibe we were going for and then just started developing without a plan in mind.

It was in the middle of development of one of the abandoned projects that I spent two weeks laying the foundation for Void Scrappers. I was frustrated with spinning my wheels on a poorly defined project with no end in sight. In contrast, the progress on Void Scrappers in two short weeks was exhilarating, and it was easy to visualise the finished project. I think the ability to imagine what the final product will be is a crucial aspect of actually delivering a completed game. Without this, you will be endlessly polishing and adding new features.

![Void Scrappers](/images/posts/interview-8bitskull/void-scrappers.webp)
<div align="center">
_Void Scrappers gameplay_
</div>

##### In the earlier interview, you described the Fates of Ort Switch release as fulfilling a childhood dream. I bet you still have it deeply in your heart, but how do you feel about your other games now?

There is definitely a higher degree of cynicism in the games I have released after Fates of Ort, but I think I have struck a healthy balance. Fates of Ort is more a work of art than a commercial product, but it was a naive approach to game development as a business. I get way more fulfillment and artistic expression from developing Skull Horde than I would if I had to go back to working as an accountant.

That said, I will still be making games when I retire, so I can lean more heavily into the artistic side again then!

### Practices

##### Your games often involve many enemies, projectiles, loot objects, terrain chunks, or minions. Is Defold helpful for these kinds of games? What are your current best practices for high-object-count games in Defold?

Defold is very performant in this sense, so it benefits me tremendously. I also lean heavily on the work of more skilled developers for performance-heavy tasks, for example using Selim Anaç's A* and AABB extensions. Things like pathfinding and collision detection are really expensive, particularly in a game like this, so my biggest recommendation is outsourcing these to extensions that perform these tasks very well.

##### Has your technical architecture evolved since then? What Defold patterns have survived across all your games, and what did you completely rewrite?

There are a lot of modules and components I have developed over the years that I carry with me from project to project. Things like game saving, input, menus and settings, collection proxy management, and so on. With each project, I naturally end up tweaking these to make them progressively better and more robust. I rarely throw anything out entirely, and end up making huge development time savings by reusing old code.

![Bore Blasters](/images/posts/interview-8bitskull/explosion.webp)
<div align="center">
_Bore Blasters gameplay_
</div>

### Defold

##### You have been using Defold for almost 10 years, and you have created a sustainable indie studio that is now a Corporate Partner of the Defold Foundation, which we are very proud of! What still makes Defold the right engine for 8BitSkull? Why was now the right moment to formalize that relationship?

Why fix what is not broken! Defold is really performant, I love Lua, and have tons of experience using the engine. I want to keep using it for years to come and so I am happy to finally be able to contribute more. I have been sponsoring Defold at the community level for years, and the reason we are going up to the corporate level now is simply because of the success of Skull Horde.

##### The announcement mentions performance improvements and desktop-specific functionality. Without revealing anything confidential, what kinds of improvements matter most to a studio like yours?

Our top priority is a big overhaul to the gamepad mapping functionality to leverage the SDL game controller database. I believe this is almost ready to ship!

We also want to see improved sound functionality in the engine so there is not a need to use sound engines like FMOD. I would also love to see some more features in the particlefx component, as we use it a lot for our juicy effects.

##### What does a good partnership look like from the developer side? Is it about feature requests, technical dialogue, funding specific work, roadmap influence, or simply supporting a tool you depend on? What would you like other commercial Defold developers to understand about supporting the engine financially or technically?

A big part of the benefit to me is simply contributing to the continued existence of the engine. Even without any other perks, this is a good enough reason to contribute financially. If I had to switch from the Defold engine to another one, this would represent a significant financial hit to my business, and I really want to avoid that happening.

I do not have the technical ability to support the engine, so financial support suits me better. Those that do have technical skills should get involved! The Defold team is quite small, and I have it on good authority that pull requests are very welcome and help lighten the workload.

### Consoles

##### Fates of Ort and Void Scrappers both reached Nintendo Switch, but Bore Blasters was PC only. Do you plan to release Skull Horde on consoles? Maybe on other consoles as well? How do you decide now whether a game is worth porting to Switch or other consoles? Is it sales potential, controls, performance, genre fit, or something else?

We are not experts on the console market, and so our basic approach is to just release on the Switch and hope for the best. Our plan is to move on to porting Skull Horde to Switch after post-launch fixes and updates are more or less stable. We may also explore other consoles, but that is very uncertain at the moment.

##### Are there particular design choices you now make earlier because you know a game may later go to console?

Absolutely. This is a core part of the studio strategy document. When you develop a game with these things in mind from the beginning, things like porting to consoles become much easier.


![Fates of Ort](/images/posts/interview-8bitskull/fungal2_wide.webp)
<div align="center">
_Fates of Ort gameplay_
</div>

##### What advice would you give to Defold developers who want to move from jams and prototypes to their first serious releases?

Start small. You do not have to make a tiny project, but you should be able to create a development roadmap with a sensible timeframe and clearly defined end goal. If you are targeting Steam, release this project even if you know it will not be successful. There is a tremendous amount to learn about the Steam release process, so it is worth doing a trial run first.

##### What is next for 8BitSkull: updates, ports, expansions, experiments, or moving on to the next game?

For the past few weeks, we have been swamped with fixes, and have now finally moved on to post-launch content updates. We will do this for a while until interest cools down, then we will port to Switch and start considering the next game project.

##### Thank you very much for the interview, Alex! Finally, how can the community follow you and the studio?

You are welcome! You can follow our Steam developer page and subscribe to our newsletter. You can also find me in the Defold forums and community Discord.

- [8BitSkull website](https://www.8bitskull.com/)
- [8BitSkull newsletter](https://www.8bitskull.com/newsletter/)
- [8BitSkull on Steam](https://store.steampowered.com/developer/8bitskull/)
- [Defold forum](https://forum.defold.com/)
- [Defold Discord](https://defold.com/discord/)
