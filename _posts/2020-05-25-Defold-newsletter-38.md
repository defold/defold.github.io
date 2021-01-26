---
layout: post
title:  Defold Newsletter 38
excerpt: What a week we have had! In case you missed it we're happy to let you know that last week we announced that the Defold source code was made available free of charge and that Defold was transferred to the Defold Foundation. We've seen a tremendous interest in Defold since the announcement and we are happy to welcome so many new developers. We will share more exciting news later this week and until then we invite you to read this newsletter. We have a new Defold release, some fresh new Defold games and a pretty cool new feature.
author: Björn Ritzl
tags: ["newsletter"]
---

Hello, Defolder! 👋

What a week we have had! In case you missed it we're happy to let you know that last week we announced that the Defold source code was made available free of charge and that Defold was transferred to the Defold Foundation. We've seen a tremendous interest in Defold since the announcement and we are happy to welcome so many new developers. We will share more exciting news later this week and until then we invite you to read this newsletter. We have a new Defold release, some fresh new Defold games and a pretty cool new feature.


## Support the Defold Foundation
The Defold Foundation works together with industry partners to provide developer-friendly software and services to game developers across the globe.

The foundation invites individuals and teams of developers to support Defold development through one-time or recurring donations. Depending on the size of your contribution you get access to a number of different rewards and benefits.

❤️ We thank our latest supporters:

| | | |
|-|-|-|
|subsoap	|Jerakin		|Insality		|
|cauli		|TinyDobbins	|dapetcu21		|
|Taure		|paweljarosz	|totebo			|
|K-Klear	|AGulev			|reneclavijo	|
|Shinose1	|thejustinwalsh	|tigerteeth		|
|yeqwep	|Bjorn Toft Madsen	|Connor Halford	|

[SUPPORT THE FOUNDATION](/community-donations)

## Games
### Hook, Line and Thinker
Connor Halfor has shared two new dev logs for his great little puzzle game Hook, Line and Thinker. [READ](https://forum.defold.com/t/hook-line-and-thinker-10-devlogs/15963/39)

### Hyperloops
Fun little puzzle game where you build long loops of connected tiles [PLAY IT](https://y444.itch.io/hyperloops)

### NoName Shooter 2.5D
Forum user d954mas has continued working on his Wolfenstein inspired NoName 2.5 shooter. He recently added different kinds of light sources, minimap and doors and keys. [LEARN MORE](https://forum.defold.com/t/noname-2-5-shooter-open-source/57417/30)

### Malas Decisiones
Forum user 88.josh shared Malas Decisiones, which is Spanish for Bad Decisions, which involves predicting how your friends would respond to certain ethical dilemmas. [LEARN MORE](https://forum.defold.com/t/malas-decisiones-my-new-weird-game-social-experience/65125)


## Mesh Component
The 1.2.169 release includes a new buffer based mesh component which allows developers to create and manipulate meshes at runtime. [LEARN MORE](https://defold.com/manuals/mesh/)


## Defold 1.2.169
#### Engine
* 3410 - Added: Mesh component
* 4773 - Added: Added sound.pause function
* 4725 - Fixed: Fix for getting sound properties before playing sounds
* 4697 - Fixed: Fixed issue with calculating the font cache cell size
* 4586 - Fixed: Make sure collection proxies get an update before rendering
* 4778 - Fixed: The tilemap does not flip tiles when created
* 3721 - Fixed: Ignore arrow keys as text events
* 4758 - Fixed: Generate character/text event for spacebar
* 4719 - Fixed: IE 11 compatibility (sounds and gamepads)
* 4742 - Fixed: Configure CFBundleDevelopmentRegion and CFBundleLocalizations in game.project
* 4747 - Fixed: Check that there’s a world before creating a collision object
* 4727 - Fixed: Potential fix for writing save file that on rare occasions became corrupt
* 4715 - Fixed: Updated android build tools to 29.0.3
* 3712 - Fixed: Box2D crashes when setting a rotation with NaN (DEF-3177)

#### Editor
* 4753 - Added: Added native extension template to editor
* 4755 - Fixed: DEFEDIT-4754 Crash when signing mobile dev app for iOS

[DOWNLOAD](/download)
