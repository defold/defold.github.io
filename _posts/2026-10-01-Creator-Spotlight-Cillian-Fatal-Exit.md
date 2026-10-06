---
layout: post
title: Creator Spotlight - Cillian - Fatal Exit
excerpt: "In this Defold Creator Spotlight we invited Cillian, known as Fatal Exit, to talk about web game development, game jams, audio, coding agents, and making Death Cascade, Dopaminer, Juggernaut: Siegebreaker, and other games with the Defold game engine."
author: Paweł Jarosz
tags: ["spotlight", "interview", "web", "html5", "game jam", "audio", "ai"]
---

In the Creator Spotlight posts we invite Defold users to present themselves and share a bit of their background, their work and things that inspire them. It is an excellent opportunity for the community to come together, to recognise achievements and to share some of the great work done by Defold users.

This time we invited Cillian, known on social media and publishing platforms as Fatal Exit, to talk about web game development, game jams, audio, coding agents, tools, game engines, and making *Death Cascade*, *Dopaminer*, *Juggernaut: Siegebreaker* and other games with Defold game engine.

![Fatal Exit creates a lot of webgames, recently with Defold](/images/posts/creator-spotlight-cillian-fatal-exit/fatal-exit-games.webp)
<div align="center">
_Fatal Exit creates a lot of webgames, recently with Defold_
</div>

## Introduction and background

##### Hi Cillian! Could you introduce yourself to the Defold community and tell us a little about your history and what you're working on today?

Hello and thanks for having me. I’m Cillian, known on my socials and publishing platforms as Fatal Exit. I’m based in Ireland and I’ve been working on this craft for almost a decade at this point, shipping primarily web games and competing at a high level in jams. I came into gamedev from a design, art, and music background. The first engine I shipped a game with was Construct back in 2017, and I later experimented with more code-focused engines and frameworks.

RTS games have been my favorite genre since I played them in the late 90s and early 2000s, and becoming a tournament-level player in a few of the newer ones later in life has been a lot of fun. Outside of that niche, I love to play (and make) a huge variety of indie games. I love oddball ideas and things that challenge the status quo. If I had to name one game that changed how I thought about making and enjoying games, it’d be *Baba Is You* by Hempuli.

One piece of trivia about me: despite my past educational struggles, one of the things that keeps me in the “gamedev ring”, so to speak, is the deliberate choice to learn new things every day. I love to keep an open mind, experiment with new technologies, and adopt them if they fit my workflow.

##### And you've now completed more than 50(?) game jams over almost a decade! What keeps bringing you back to them?

Yes, I am significantly past 50 game jam releases at this point, counting games I made on my own (mostly as a solo dev) and a few I completed while helping other teams, either as a musician/composer or a 3D/pixel artist. Game jams are, in my opinion, one of the most fun experiences you can have in gamedev if you detach top placement or winning a prize from being your primary motivation.

I see many beginners struggle with that, but as a regular, you win some and you lose some. For every prize winner or top placement, the vast majority of games don’t place. That’s just the reality of any sort of competition. What mainly inspires me to work on jams is the creative limitations imposed by the theme, the chance to try many varied ideas, and seeing an end result live on my screen that my friends and family can play.

##### Audio seems to be a particularly important part of your work. Draft Punks ranked first for audio among 486 Gamedev.js Jam entries! And you've created music and sound for many of your own and other developers' games. Does audio usually come after the game design for you, or does it determine the game you decide to make?

It doesn’t usually determine the game, but when I am first writing my game design docs, I am already imagining a specific soundtrack vibe in my head.

*Draft Punks* was an edge case because I knew from the start that I wanted it to be a DJ-focused card game, so I wanted the feeling of being a DJ while playing a deckbuilder to come through. Sounds a little wild, but that distinction and my music knowledge shaped most of the game’s design, and I built each “card” as a loop or one-shot sample sequence in my DAW (Digital Audio Workstation).

![Draft Punks gameplay](/images/posts/creator-spotlight-cillian-fatal-exit/draft-punks-wavedash.webp)
<div align="center">
_Draft Punks ranked first for audio among 486 Gamedev.js Jam entries. [Playable now on Wavedash](https://wavedash.com/games/draft-punks?utm_source=defold&utm_medium=referral&utm_campaign=creator_spotlight_cillian_fatal_exit&utm_content=draft_punks)._
</div>

## Web platforms

##### You've moved strongly toward browser-first games. What attracted you to the web as a distribution platform?

There are two things I love most about the web as a platform. First, there is a massive reduction in the risk associated with downloadable games. I’m currently not in a position where I can release Steam games for bureaucratic/legal reasons (Steam tends to be a bit safer for downloadable games than more open platforms), so my biggest exposure to downloadable games is on itch.io. At least five good friends of mine have had accounts hacked and taken over, or worse, due to malware on itch.io. Because of that, if I cannot ship a web game on itch.io, I don’t even want to bother.

Second is the ease of sharing games with the world and even with those very close to me. Many of my family members are getting older, and that influences some of the choices I make in my games. An amazing thing about the web is that you can support desktop and mobile with a single build, which makes it dramatically easier to playtest a game and get feedback. Supporting mobile in most of my games, where viable, is important to me even though I personally prefer desktop as a platform. Arthritis is common in my family, and getting to watch a parent with limited finger mobility learn my games and eventually start to find the fun is another huge win for me.

##### Wavedash has become a recurring part of your recent work, from Draft Punks and Dead Sun to Death Cascade. What do you think about it?

I think Wavedash is a wonderful platform, and I wish more folks knew about it (thank you for working with them on the wonderful Defold SDK support).

For those out of the loop, Wavedash is probably the closest platform on the web to feature parity with Steamworks. It offers things like leaderboards, achievements, player identity, even P2P multiplayer and lobbies like Steam has, and good support for UGC (think Steam Workshop). It’s still in its early stages, but there’s huge potential there. It’s also very open to smaller projects and game jam games, which you can monetize simply by opting into the creator fund and earning money from player engagement.

It’s just a super cool platform and the founders and team members who work on it are incredibly helpful and open to feedback from both developers and players.

![Fatal Exit games on Wavedash](/images/posts/creator-spotlight-cillian-fatal-exit/fatal-exit-wavedash.webp)
<div align="center">
_Fatal Exit publishes many browser-first games on Wavedash_
</div>

##### How do you assess the modern web games market?

I think it’s a somewhat untapped market with huge potential. There’s more competition than ever before, especially with the recent rise of agentic coding and the booming popularity of web technologies to build on top of, such as Three.js, but there’s an important point most people miss.

The reality is that, with any serious dev project, you aren’t competing with the majority of releases that end up on the internet or in stores. Even five or six years ago, long before the current changes in tech markets, the vast majority of games on platforms such as Steam were never really discovered because they just weren't up to the standard of a release that engages players.

On the other hand, don’t expect your very first game to make you massive amounts of cash, because that is an exceptionally rare event that most people without generational wealth will never experience. Instead, focus on building up your portfolio and brand, and play the longer game.

##### What do you enjoy about working with web games?

Some of that I mentioned above. The other thing I really like is that people don’t usually expect a crazy scope from games on the web. A single polished mechanic or a very refined, understandable game loop can be enough to engage people, with the depth and complexity becoming something you slowly dip into as you master the game.

##### What do you find frustrating or worrying about web games?

My biggest frustration is the fact that many people don’t treat the web as a “real platform” and use derogatory terms towards web games or simply label them as inferior. But that’s not exclusive to web games by any means. People have labeled mobile as an inferior platform (it’s true that there are many awful examples of games there, but there are also many insanely good indie titles that play great), and as a musician for over 16 years, the “real music” debates (production, DAWs, synthesizers as instruments, etc.) make me roll my eyes too. It’s just pure tribalism that has been around in some form since long before the days of the modern internet.

##### Has earning money directly from browser games changed how seriously you view it as a commercial path?

It’s certainly changed my perspective. I’m now mostly looking for platforms that accommodate my development velocity, and Wavedash and the web in general fit me well. I am less interested in jumping through the hoops I’d need to get my games on Steam, especially with the optimal slow-burn lead-up to release. If a publisher wanted to work with me to publish my games on Steam, I’d be very much down to work with them. But for my independent output, given everything I like about the web as a platform, I’m going to make it here or die trying.

##### What tips do you have for new developers?

Keep the scope small but elegant, ship often, and start playtesting as early in your development cycle as possible. Don’t be afraid to kill an idea if you can’t find the fun. And don’t be quick to give up - play the long game.

![Death Cascade gameplay](/images/posts/creator-spotlight-cillian-fatal-exit/death-cascade.webp)
<div align="center">
_Death Cascade was created for Defold Game Jam 2026. You can [play it on Wavedash](https://wavedash.com/games/death-cascade?utm_source=defold&utm_medium=referral&utm_campaign=creator_spotlight_cillian_fatal_exit&utm_content=death_cascade_gameplay)._
</div>

## Game engines and Death Cascade

##### Looking through your career is almost like looking through the history of game development tools: Construct, GDevelop, Unity, Godot, DragonRuby, Phaser, PixiJS, Defold and others. What can you say now about all of these? Have you been searching for an engine or workflow that you actually want to settle on?

This has been a process akin to pulling teeth for half my gamedev journey. The reality is that there’s no perfect engine; you have to make compromises in some regard. But some come closer to what I value, and I’ve learned that others don’t fit me as well, and that is okay.

I’ve experienced everything from the ease of use but limitations of the visual-scripting-based Construct and GDevelop, to Unity’s gargantuan project sizes and huge engine installs, Godot’s depressingly poor web performance and limitations involving things like .NET, and the limitations of web-based platforms such as Pixi, Phaser, and Three.js when making native apps (no, Tauri or Electron don’t count performance-wise).

Personally, out of all of these, the two I loved most were DragonRuby in the past and, more recently, Defold once again. Both have good cross-platform support, good web exports, and small project and build sizes.

<div align="center"><p style="font-size: larger"><i>“Defold is significantly more mature feature-wise, and Lua is a more popular language for gamedev.”</i></p></div>

Another thing I value is whether it’s possible to use these engines with coding assistants. As an early adopter, from the beginnings of GitHub Copilot to tools like Claude Code now working with Defold’s Automation Bridge extension, I’ve found that the current generation works massively better with Defold than previous ones ever did. I (maybe controversially) think that is an important consideration when judging which technologies are more or less likely to be adopted in the future of gamedev. You can see that right now with the moment Three.js is having.

##### You actually tried Defold before: A Floof's Quest For Cheese was your first Defold game in the 2024 Made With Defold Jam. What do you remember about that first experience?

My best memory of that jam (and a huge win for Defold) is that I had recently, maybe a few weeks prior, made a similar game concept in Godot that I shipped on the web. Both had a similar amount of stuff going on, and both used Spine animations I had handcrafted, but Defold’s performance absolutely bullied what Godot managed. The Godot game was barely playable on decent mobile devices at the time, while the Defold one was perfect. It was just a wildly different experience between the Spine implementations of the two engines.

##### Two years later you came back for Defold Game Jam 2026 and created Death Cascade. What made you give Defold another try?

Partly because of that memory of the performance and what I mentioned earlier about valuing mobile as a platform for my family to experience my web games. I also made a point on my socials earlier this year that I was going to try my best to battle-test Defold as part of my newer tools workflow, and this was a good opportunity to push it. I couldn’t be happier that I tried.

![Death Cascade in Defold editor](/images/posts/creator-spotlight-cillian-fatal-exit/death-cascade-defold.webp)
<div align="center">
_Death Cascade was made with Defold. You can [play it on Wavedash](https://wavedash.com/games/death-cascade?utm_source=defold&utm_medium=referral&utm_campaign=creator_spotlight_cillian_fatal_exit&utm_content=death_cascade_editor)._
</div>

##### And what do you think now about Defold? What do you like about it?

The main things I love about it are the great cross-platform support (really second only to Unity, which doesn’t suit me) and the ability to push live entity counts that other web-based tools I have used may struggle with, especially on mobile.

<div align="center"><p style="font-size: larger"><i>“It’s genuinely so rewarding to go from playtesting my game on my Mac Mini for many hours to running it on my Android phone and seeing performance that matches the same frame-rate cap, even with the web build. I don’t think many engines can match it. ”</i></p></div>

The great license, the interaction and support from the Defold account and team on platforms like X, and the openness to things without being judgemental (cough cough blue robot) are just extra wins on top.

##### We appreciated it! In Death Cascade you took the Chain Reaction theme of Defold Game Jam 2026 very literally. How did you come up with this idea and design? How did you approach building it?

I had two ideas before this one that failed miserably at very early prototype stages: a game tentatively called “Minelayer Delivery Service”, where you transported a package through a level with explosives, and another unnamed game, a deckbuilder where your deck was a house of cards and you played as many cards as you could before it collapsed.

The problem with both concepts was that they approached the chain reaction theme through a point of frustration or failure. I know from jam experience that this is an easy way to sour people and make them annoyed about how the game interprets the theme. So I decided to make a game in which the chain reaction mechanic makes you feel godlike by deleting screens upon screens of enemies at once. I’ve been a fan of bullet heaven games since *Vampire Survivors* was first released and always wanted to make one with a unique spin.

##### Game jams and prototypes are all about development speed, but long-term projects introduce a different problem: maintainability. How do you deal with it?

I’m personally not the best person to ask about that, if I admit it myself. My most successful projects are usually small in scope. I have a WIP autobattler RTS titled *Lane Protocol* that has gone through more than five iterations in different game engines, and I may bring it to Defold at some point. It’s been my longest-running dev project and the closest thing I have to a “dream game”.

## Porting to Defold

##### You've now ported existing projects to Defold rather than always starting from scratch. For developers who already have a game running in another engine or framework, how approachable is moving it to Defold?

With today’s development tools and assistance, porting is much more feasible than it was even six to twelve months ago, let alone further in the past, even if you have to change languages in the process. My main advice for doing a one-to-one port, or getting as close as possible, is to begin by targeting the same primary platform as the previous version. So, if you were building a web game in another engine, I would definitely suggest testing a Defold web build as a first step. This lets you compare performance and game feel in the same environment. The biggest gotcha with Defold involves render scripts when targeting web builds. If you try to port the functionality of shaders from an HTML5 engine, you may encounter errors, but they are not difficult to work around.

##### You've described Dopaminer as a game you were close to abandoning because you simply couldn't find the fun in it. What changed after porting it to Defold?

It was a combination of things. The old build had performance issues, and over time, technical debt and failed features were literally rotting the codebase. The boost in performance let me add more features and build systems around the game without destabilizing it, while maintaining the core idea of “visual feedback overload” that I wanted to be the hook for *Dopaminer*. Approaching the design with a fresh codebase also allowed me to explore ideas in different ways, which worked out for the better.


![Death Cascade gameplay](/images/posts/creator-spotlight-cillian-fatal-exit/dopaminer.webp)
<div align="center">
_Porting Dopaminer to Defold gave the project a fresh start._
</div>

## Ongoing and future Defold projects

##### Juggernaut: Siegebreaker was another experiment, but in a very different direction: you used it as an opportunity to explore Defold's 3D features. What did working on this title look like?

I have a bit of a love-hate relationship with *Juggernaut: Siegebreaker*, but only because of the dumb constraints that the jam imposed on exports; it has nothing to do with Defold. It’s a game I want to revisit to better realize its potential. The actual process of building the game was tons of fun. I designed a set of pixel art templates and used them both to texture 3D assets and as billboard sprites for the in-game units and environment art. Because it was an AI-focused jam with a very short submission timeframe, I operated the Defold editor primarily with Claude Code.

![Juggernaut: Siegebreaker gameplay](/images/posts/creator-spotlight-cillian-fatal-exit/juggernaut-siegebreaker.webp)
<div align="center">
_Juggernaut: Siegebreaker combines 3D assets with pixel art and billboard sprites. Made with Defold._
</div>

##### What other projects do you have that you would like to develop using Defold and can share with us?

As I stated, I may reboot *Juggernaut: Siegebreaker* as a PC-focused strategy game down the line, likely with significantly reworked gameplay. It may end up being an entirely different game with a different title by the time it is released.

You mentioned *Dopaminer*, which is another game of mine that I recently released. I will likely continue to update it or use what I learned from it to build a deeper incremental game that is less focused on pure visuals and juice overload.

I also have several WIP games that you might be interested in:

*Another Path* (named after one of my first released songs back over a decade ago) is a 2D pixel art roguelite loosely inspired by the indie hit *Loop Hero*, but instead of following a preset loop you build and customize the loop as you go.

*Daemon Snake* was an idea I had for a meme game, but it ended up being kinda fun and will likely be the first of these to be released. It’s a 2D top-down game using pre-rendered 3D graphics that mixes elements of classic snake, the bullet heaven genre, and classic Diablo-style hack-and-slash/ARPG vibes with a roguelite edge.

![Daemon Snake gameplay](/images/posts/creator-spotlight-cillian-fatal-exit/daemon-snake.webp)
<div align="center">
_Daemon Snake mixes classic snake, bullet heaven and action RPG gameplay. Also made with Defold._
</div>

*Magnetogether: Apart* (working title) is a full remake of one of my most successful games from a large jam. The original *Magnetogether* placed fourth in Innovation out of more than 1,800 games in Brackeys Game Jam 2021.1 and was made with Construct. In the past, I attempted to remake it as a full game in Construct, GameMaker, and even Unreal Engine. That process spanned several years, but I could never focus on taking it beyond a prototype.

<div align="center"><p style="font-size: larger"><i>“Now, with Defold, I am making good progress on taking it beyond its origins and bringing it to a polished standard for a commercial web release.”</i></p></div>

Instead of pixel art, I have been experimenting with sprites rendered from Blender outputs and a wider range of colors than the original one-bit game.

![Magnetogether: Apart gameplay](/images/posts/creator-spotlight-cillian-fatal-exit/magnetogether.webp)
<div align="center">
_Magnetogether: Apart is a full Defold remake of the highly ranked 2021 jam game coming soon._
</div>

As to a project I’d most like to build, I love autobattlers as a genre, particularly ones with asynchronous multiplayer so that’s something I’d really love to explore.

All of these games will initially be released on Wavedash. Steam is possible down the line, but we’ll have to wait and see.

## AI

##### Now, a bit of a touchy subject, but for Death Cascade you explicitly disclosed its use of AI-assisted code while its art and music remain your own work. Where do you personally draw the line between using an agent as an implementation tool and handing creative authorship over to generative AI?

I think it depends on the task and the objective. With some games, I want to have much more creative control over literally everything; with others, where I have very tight deadlines, I am more willing to take a higher-level director’s seat.

Personally, I am not judgemental about how anyone chooses to use tech, but I still love the artistic elements of gamedev enough to work on them. I’ve also used coding agents to extend tools such as Aseprite and Blender with my own custom extensions for faster, almost kitbash-style art prototyping, batch processing and conversions, better adherence to things like color direction, procedural animation tooling for squash and stretch, and similar looping motions. Other tooling lets me procedurally turn my own pixel art slices into nine-patch graphics for buttons and UI, etc. I also take advantage of custom Python scripts and tools using things like Pillow (a Python imaging library) for even more batch operations and sorting tasks for which using Aseprite would be overkill.

##### You had already been experimenting seriously with agentic game development before. Where are coding agents genuinely useful in game development, and where do they still fail?

I think they are an incredible power multiplier in the hands of someone who knows what they are doing. However, they can hurt people who are less experienced. I think having a plan for what you want to build is imperative. The more specific the goal you want to achieve, the less likely you are to want to flame the agent afterwards.

##### You've described Defold as something of a sweet spot for agentic development. How do you assess the newer Claude Code models with Defold?

Both Opus 5.5 and the new Sonnet 5.5 are incredible at working with it. Previous generations struggled to make things work, but they seem to have added some secret sauce that helps the models learn new things much better. I’ve even experimented with newer 3D and 2.5D workflows on newer projects, and they have maintained the same wow level.

##### Could you walk us through your actual workflow on Death Cascade?

The process was akin to “efficient creative chaos”. It started with a series of design docs, then I basically let the agent do its own thing for 30-minute chunks while I worked on the game’s artwork in Aseprite, UI element graphics and audio with FL Studio and Bitwig, and copy for things like the skills in a text editor. It meant having many programs open at once, and I am thankful to have a computer that can kind of handle it.

<div align="center"><p style="font-size: larger"><i>“The lightweight nature of Defold definitely helped.”</i></p></div>

I knew from a very early stage that, to make the visuals stand out, I wanted to create chunky pixel art somewhat inspired by less pixel-esque games such as *The Binding of Isaac* and *Brotato*, and enhance it with heavy use of shaders, blending, procedural graphics drawing, etc. This combination ended up being less time-consuming than I had worried it would be and helped with the game’s fast turnaround.

I also used the coding agents to do some of the busywork, such as setting up atlases and tilesets with my own art and setting up the UI—all things I inherently hate doing in other engines. I don’t see any reason to spend 30 minutes on the repetitive tasks of importing and setting up assets. I can leave an agent for five minutes and make fewer mistakes.

##### How much context do you prepare for the agent? Do you maintain project instructions, architecture documents, etc?

I brainstorm either alone or with the help of AI tools, then I write a series of documents specific to different areas of the project. It helps the agent read the details only when it needs them and avoids polluting the context of specific requests.

##### What advice would you give to an experienced programmer who is skeptical of coding agents?

My best advice is not to bury your head in the sand. It’s true that someone with zero programming, design, or logic experience might not make a solidly implemented project when they “vibe code”. But if you give those tools to an expert in any of those fields and compete against them to make the same project while totally rejecting the tools yourself, the difference in results will be stark.

It’s not 2023 anymore, and preconceptions you may have formed when ChatGPT was new—about things such as its ability to count and reason—belong in the past. A developer experienced with current frontier coding models can accomplish weeks of implementation and engineering work in a day or two of focused work while producing performant, well-built results.

![Dopaminer in Defold editor](/images/posts/creator-spotlight-cillian-fatal-exit/dopaminer-defold.webp)
<div align="center">
_Dopaminer was made with Defold. You can [play it on Wavedash](https://wavedash.com/games/dopaminer?utm_source=defold&utm_medium=referral&utm_campaign=creator_spotlight_cillian_fatal_exit&utm_content=dopaminer)._
</div>

## Defold wishes

##### From the Defold side, what would make agentic automated workflows better?

I’ve discussed this with some of the Defold team members, but my number one request—which is already in the works—would be porting the Automation Bridge extension to a CLI similar to the Unity CLI. It is a wonderful piece of tooling and the best release Unity has produced in half a decade.

##### Yes, we remember this discussion and we'll be improving it! Next thing you seem to appreciate about Defold is that its core is relatively small while additional functionality comes through extensions or systems you build yourself. How do you feel about Defold’s ecosystem? What is useful? What would you like to see more?

I like the lightweight nature, so I’d love to see more extensions rather than core engine features. I detest the level of bloat in engines like Unity and UE, where 90% of what they contain is irrelevant to most people’s games. I even feel that Godot could be better structured in terms of modularity. It’s part of why I really enjoyed working with Pixi for a while and just building everything. However, I then found the inverse to be true: building everything from scratch each time was also a detriment. I’d love to see more extensibility on the renderer side of things, especially when it comes to 2D and 3D post-processing.

##### What other tips do you think you can give for developers working with Defold?

Take advantage of its strengths.

<div align="center"><p style="font-size: larger"><i>“Embrace the Defold's performance headroom and, when relevant, take advantage of its incredible cross-platform nature.”</i></p></div>

Enjoy your blazing-fast web games. Be open to learning new things, revisiting misconceptions, and refining your judgement.

##### And finally, where can people follow your work and play your games?

- Wavedash: [https://wavedash.com/FatalExit](https://wavedash.com/FatalExit?utm_source=defold&utm_medium=referral&utm_campaign=creator_spotlight_cillian_fatal_exit&utm_content=wavedash_profile)
- itch.io: [https://fatalexit.itch.io/](https://fatalexit.itch.io/?utm_source=defold&utm_medium=referral&utm_campaign=creator_spotlight_cillian_fatal_exit&utm_content=itch_profile)
- X: [https://x.com/FatalExit](https://x.com/FatalExit?utm_source=defold&utm_medium=referral&utm_campaign=creator_spotlight_cillian_fatal_exit&utm_content=x_profile)
- YouTube (I hope to post some Defold-themed tutorials here in the coming months so people can see how I work with it): [https://www.youtube.com/@FatalExit](https://www.youtube.com/@FatalExit?utm_source=defold&utm_medium=referral&utm_campaign=creator_spotlight_cillian_fatal_exit&utm_content=youtube_profile)

##### Thank you very much for the interview, and we wish you tremendous successes with your games!
