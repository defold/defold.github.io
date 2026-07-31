---
layout: post
title: From tabletop mystery to mobile city - how Soft Boiled Games brought MicroMacro to Defold
excerpt: In this Defold Creator Spotlight we invited Felix Weiler from Soft Boiled Games to talk about adapting the hit MicroMacro board game series for mobile, building a huge zoomable city, and choosing Defold for the job.
author: Paweł Jarosz
tags: ["spotlight", "interview", "mobile", "steam", "optimization"]
---

In the Creator Spotlight posts we invite Defold users to present themselves and share a bit of their background, their work and things that inspire them. It is an excellent opportunity for the community to come together, to recognise achievements and to share some of the great work done by Defold users.

This time we invited Felix Weiler from Soft Boiled Games to talk about *MicroMacro: Downtown Detective* - a very successful mobile title made with Defold, adapted from the hit board game series, and an upcoming Steam release.

![MicroMacro: Downtown Detective](/images/posts/creator-spotlight-felix-weiler/mobile.png)
<div align="center">
_MicroMacro: Downtown Detective made with Defold and released on Google Play and App Store_
</div>

##### Hello Felix, introduce yourself to our community!

Hi, my name is Felix Weiler and I'm co-founder and developer at Soft Boiled Games. We're based in Düsseldorf, Germany. In August 2025 we released *MicroMacro: Downtown Detective*, our first commercial game, a continuation of the successful board game series, made for the most part by the same team.

##### What are your favorite games? Do you have some nice hobbies?

I'm drawn to clever puzzle games and deep narratives, ideally both at once. *Outer Wilds* is probably my all-time favorite for exactly that reason: knowledge-gated puzzles, a miniature solar system to explore, and a real sense of discovery driving the whole thing.

*Return of the Obra Dinn* and *The Witness* are favorites that scratch a similar itch, and I'll also always make room for *Factorio*, which is just so remarkably polished.

Right now I'm playing through *Lorelei and the Laser Eyes*, which I'm enjoying a lot for its striking visual style and how tightly the puzzles are woven into the narrative.

Outside of game development, I make music, and sometimes get away from screens with running, climbing, and hiking.

##### How did you get into game development? What did your journey look like?

Even as a kid I was more interested in taking games apart and figuring out how they worked than just playing them, so I got into programming early, before the internet made tutorials and resources as accessible as they are today. I was always tinkering on small game projects as a teenager, without any real plan to make a career of it.

I ended up studying and working as an electronics engineer in R&D, and later ran my own small consulting and development firm for electronic products. Game projects stayed a constant in the background the whole time.

The MicroMacro board game team and Soft Boiled Games are, at their core, friends who know each other from school and university, and had already worked together on other projects and businesses over the years. The board game's success gave us the opening to found Soft Boiled Games and finally bring MicroMacro to mobile, something we'd considered from very early on.

![MicroMacro board game series](/images/posts/creator-spotlight-felix-weiler/board_games.png)
<div align="center">
_MicroMacro board game series_
</div>

##### You described MicroMacro: Downtown Detective as “probably a bit of an unusual case.” That immediately sounds intriguing. What makes this project unusual?

MicroMacro breaks with a lot of mobile market conventions on purpose: no pay-to-win, no in-game currencies, no timers. Where a lot of mobile design is built around quick action and manufactured waiting, MicroMacro asks for the opposite, a kind of analog slowing-down, real attention and thinking-through rather than just tapping whatever's in front of you.

That same principle carries into the world itself: it's one huge, continuous city, drawn in a minimalist comic style, filled with handcrafted stories and carefully placed clues. At a glance it might look like a typical hidden-object game, but it really isn't about clicking around until something highlights: it's about looking closely, thinking, and connecting stories.

##### The starting point was a beloved physical board game! What was the first moment when you felt that MicroMacro could work as a digital game? What parts of that experience did you most want to preserve?

We actually had a very early iPad prototype before the board game even existed, and our biggest worry from the start was whether a map that size would translate to a small screen. But we were confident early on that the core mechanic and feel would carry over. The board game itself was already known for its broad appeal, approachable even for people who don't normally play board games, and going mobile only extended that further: a phone is in almost everyone's hands these days. The board game also works best with a small group, while on mobile you can dive into a case entirely on your own.

Above all, what we wanted to preserve was the main mechanic that everything else grows out of: the same characters turn up in multiple locations across the map, each showing a different point in time. Following those threads is what turns a big illustrated city into surprisingly deep crime stories, closer to reading a comic panel by panel. We also wanted to keep the distinct style and feel of the original: that the city stays the same and you get to know it over time, that there's always something interesting happening around you as you explore, and the humor and pop-culture references that run through it.

##### Designing detective cases for a zoomable screen must be very different from designing them for a printed map. How did that shape the way you approached development? What did you discover could not simply be translated one-to-one from the tabletop version to mobile?

We had to rethink how we design cases, mostly around readability on a small screen. What doesn't translate at all is the immediate full overview you get on a printed map, the way one player can keep a finger on one corner while someone else is finding something in another place across the table. On mobile you're always looking through a much smaller window into the world, so we introduced interactive elements and markers to help players navigate cases without losing that sense of the whole city.

During development we had time to really settle into designing cases for mobile. The new cases for the upcoming expansion, our second, are in our opinion the biggest and most complex we've built yet, and make full use of the whole nine-district city.

![MicroMacro: Downtown Detective on mobile](/images/posts/creator-spotlight-felix-weiler/mobile_1.png)
<div align="center">
_Mobile version has been released on Google Play and App Store_
</div>

##### The game gives players digital affordances such as zooming, touch navigation, guidance, and interactive progression. How did you make sure these features helped the detective experience without making it feel too automated?

Compared to our earliest drafts, before we'd really learned what worked on a small screen, we ended up adapting the storytelling quite a bit: shorter texts, fewer guided camera movements, more situations that leave room for freer investigation.

Getting the balance right between free investigation and gentle guidance took a lot of fine-tuning, and a lot of playtesting with real players. The feedback shows it lands well for a lot of player types, though some would want it freer and harder, and for others it's already fairly challenging. We're currently exploring new ways to allow more open investigation without players getting lost, something like the “hard mode” the board game offers, which isn't really possible in quite the same form on mobile.

##### The app uses its own city map and new cases. What made original content the right choice for the digital version? How do you approach the design of these?

Cases for the digital version are designed a bit differently, and we wanted to make good use of what the format allows. Search Warrants, letting players look inside houses, uncover crime scenes, find hideouts, and what we call “Superzoom”, where the player can zoom in very far in certain spots to find tiny details, are both good examples of things that simply aren't possible in the physical version.

More importantly, we wanted to offer genuinely new content for fans of the series rather than a re-skin of something they'd already solved. Planning a new city and bringing it to life is something we really enjoy, and a lot of fans end up playing every version, board game and app alike.

![Search Warrants and Superzoom in MicroMacro: Downtown Detective](/images/posts/creator-spotlight-felix-weiler/mobile_2.png)
<div align="center">
_Digital version is designed a bit differently than board games_
</div>

##### What are the plans for the Steam version? How do you think it will be different from mobile and board games? Are you preparing it with Defold too?

There's been demand from players for a Steam version since early on, and the format suits the game well, sitting down at a PC to work through a few cases is a mode we enjoy ourselves, even though MicroMacro started as a mobile game. There are also players who just aren't interested in mobile and want it on PC in a more familiar form.

On the technical side, the main adaptation is the interface: the mobile version is built around portrait orientation with a necessarily minimal UI, while the larger screen just gives us more room to work with, and removes some of the constraints we're designing around on mobile.

We're building the Steam version in Defold as well, we know the engine well by now, and it's been a good, productive environment to work in. It also means the mobile version can benefit from any improvements made along the way, which should be especially useful for tablet play.

![MicroMacro: Downtown Detective on Steam](/images/posts/creator-spotlight-felix-weiler/steam_1.png)
<div align="center">
_Upcoming Steam release is also being made with Defold_
</div>

##### When you started thinking about the technical side, what were the biggest requirements for the engine? Why did Defold become the right engine for this project?

Performance mattered a lot to us. It's not a technically demanding game in the traditional sense, but we didn't want to limit support to only the newest devices, and we realized fairly early on that quick, low-latency feedback on touch input is essential to how the game feels and how well players can concentrate while working through a case. It directly affects players' ability to focus on finding clues and solving cases.

It also felt like a natural match: Defold started out as a mobile-focused engine, and that focus is still very much built into it.

##### What did Defold make easier than expected?

Defold's regular updates are rarely breaking, you can usually take new features and improvements without worry, and when something does break compatibility, it's clearly documented.

Cross-platform build workflows have been solid, and native extensions give us flexibility to go beyond the built-in functionality when needed. Overall it doesn't feel bloated: the detailed control is there when you actually need it, and you don't have to think about it when you don't.

##### The game is built around a very detailed, zoomable city map. How did you approach rendering, memory, and performance for something like that?

The city map is genuinely large, and the total data footprint for the whole city ends up being bigger than you'd intuitively expect, even accounting for our fairly minimalist black-and-white style. Since we also wanted to support somewhat older, less powerful devices well, this became a core technical challenge.

Defold usually expects most of a game's objects and their counts to be defined ahead of time, with memory preallocated accordingly. We do things a bit differently: we create and manage the relevant game objects and image data dynamically at runtime instead. I think it’s not the most common pattern in Defold projects, but it's supported, and it's what made our approach possible.

Loading and preparing data works against a per-frame budget, so we spread the cost out over time while still using that time efficiently, without stalling any other part of the game. Because the visible area can change very quickly during scrolling and zooming, we also try to predict which not-yet-visible parts of the city are likely to become visible next, and preload those where possible, including using idle time to load a bit further ahead. For unavoidable delays, we fall back to lower-resolution image tiles so there's never a visible gap in the map, even briefly. The overall goal is to keep the experience free of stutters or distractions.

##### Looking back, what is the biggest design or technical lesson from the development?

Playtesting, above everything else: starting early, doing it often, and using it to actually check whether the core mechanic holds up and is fun, and whether every element in a case is really serving that, not just to find and remove friction. A lot of the case design decisions that mattered most only became clear once we watched real players get stuck, or breeze past something we expected to be a challenge, or once we realized something we liked just wasn't pulling its weight.

And the tools you build your game with matter almost as much as the engine itself. Since our levels are really cases laid out across the city map, we ended up building a kind of level editor outside of Defold, for map and case configuration, and how good that tool was directly shaped how well, and how fast, we could design and iterate on cases.

##### What did you learn from testing and launching the game on mobile? How do you see the mobile games market nowadays?

We went in knowingly pushing back against some norms of the market, we wanted to make a mobile game we'd actually want to play ourselves. Honestly, there aren't that many of those, and most of them are ports of PC games rather than mobile-first designs.

What we found is that a lot of our players really respond to a game that's monetized fairly and transparently, no ads, no currencies, no subscriptions, you buy the game and own the content. Players also often highlight the relaxed pace paired with genuinely engaging content and puzzles, as a contrast to the louder, more aggressive side of the mobile games market.

I do hope, and I think I see some signs of it, that there's growing room for games that don't lean on the more aggressive end of monetization, where the experience matters more than squeezing every session for revenue. The indie space seems especially well-suited to that, particularly for more story-driven, mid-core games, it's still a place where care and passion can carry a game.

![The city map in MicroMacro: Downtown Detective](/images/posts/creator-spotlight-felix-weiler/steam_2.png)
<div align="center">
_The game's huge, continuous city map_
</div>

##### What advice would you give to developers considering Defold for making a game? What kinds of games do you think Defold is especially well suited for after making MicroMacro: Downtown Detective?

I'd really encourage looking closely at which engine fits the specific game you're planning, including alternatives that might not be the obvious first choice, and making that decision independent of what's currently fashionable in the market. For us, it was clear early on that dynamically loading and rendering a huge, multi-scale city map would be the core technical challenge, so we built proof-of-concept versions in a few different engines and compared performance directly, which also gave us a first feel for what day-to-day development would be like in each.

In conversations with other developers, I keep noticing that Defold still isn't very well known. It's probably not the first choice for huge 3D AAA projects any time soon, but for more modestly scoped games, it's certainly worth putting on the list, and for mobile games specifically, the performance really stood out, especially on older devices.

##### You mentioned that you built proof-of-concept versions in several engines before choosing Defold. What exactly did you test, or what results made Defold stand out? Were there any measurable differences between the prototypes?

We tested a handful of core metrics across all the prototypes: initial loading time (from opening the map to the first view being fully loaded), tile processing time (how long it takes for a tile to fully load once it enters the visible area), time to a full view after zooming or panning, frame rate and how consistent it stayed, and memory footprint. We ran all of this on high-end, mid-range, and older, low-end devices too, I generally like testing a bit below our actual target spec, and we also paid attention to perceived speed and smoothness, plus how the development experience itself felt in each engine.

With Defold, the implementation turned out to be surprisingly straightforward, including the dynamic tile loading. Initial load time was great, and the per-tile timings and full-view-after-interaction times were solid too. But what mattered most was that it just felt noticeably snappier to users, especially on older, less powerful hardware. Looking ahead to building the whole game on top of that, the decision was an easy one.

<div align="center"><p style="font-size: larger"><i>“What mattered most was that it just felt noticeably snappier to users, especially on older, less powerful hardware.”</i></p></div>

##### And finally, what are your future plans that you can share and how can we follow your progress and next games?

Next up is the second expansion pack for *Downtown Detective*, which will finally complete the nine city districts we've been hinting at, we're hoping to release that by the end of the year.

After that comes the Steam version, which we think will open the game up to a good chunk of players who'd otherwise never have touched it on mobile.

Beyond that, we've just started early work on a next title in the series, built around a new, or heavily reworked, core mechanic. It's still some way off, but it's something we're really excited about.

To stay up to date with any news and upcoming games:

- Join the [MicroMacro Discord](https://discord.com/invite/448xjpajfh)
- [Wishlist the game on Steam](https://store.steampowered.com/app/4543500/MicroMacro_Downtown_Detective/)
- Follow [MicroMacro on Instagram](https://www.instagram.com/micromacro_game/)

##### Thank you very much for the interview, and we wish you tremendous success with MicroMacro: Downtown Detective and your future games!
