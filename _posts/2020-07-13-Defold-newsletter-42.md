---
layout: post
title:  Defold Newsletter 42
excerpt: This week we have several new games to share and an update on Web Monetization in games made with Defold. We also have the latest Defold beta release notes.
author: Björn Ritzl
---

Hello, Defolder! 👋

This week we have several new games to share and an update on Web Monetization in games made with Defold. We also have the latest Defold beta release notes.

## Games
### Juump!
Forum user Totebo released Juump! last week in collaboration with Winkel Games.

_"JUUMP is a fast-paced, endless arcade climber. Super quick to learn but highly rewarding to master. Jump, slide and dodge through a dangerous world. How far can you get?"_

[INSTALL](https://forum.defold.com/t/juump/65743)

### Hyper Dash
_"Hyper Dash is a simple hyper-casual game where you need to aim carefully and dash back and forth between the colored walls."_

[PLAY](https://shapeshiftjm.itch.io/hyper-dash)

### Librarian Barbarians
Forum user Klear made this fighting game about him and his colleagues at the Municipal Library of Prague. You better not be late returning books unless you're willing to risk your life against Bohouš, Lukáš and the other bad-ass librarians!

[PLAY](https://kklear.itch.io/librarian-barbarians)

### Brain Please Don't
Critique Gaming (developers of Interrogation) created "Brain Please Don't", a game about mental health, at the last Global Game Jam. The game has now been released on Steam.

_"Brain Please Don’t lets you try Cameron’s week with various different versions of the teenager, and each choice made along the way changes Cameron’s inner universe, and the deck that represents it."_

[CHECK IT OUT](https://store.steampowered.com/app/1324360/Brain_Please_Dont/)


## Web Monetization update
The Defold Foundation was [awarded a grant from Grant for the Web](https://defold.com/2020/06/09/Defold-is-awarded-a-grant-from-Grant-for-the-Web/) on the 9th of June. The Defold Foundation will use the grant to integrate, promote and support the use of Web Monetization in web games created using Defold.

The first milestone of the project has been reached with the launch of the Web Monetization extension, template project and new manual. With the help of the new [Web Monetization manual and the extension](https://defold.com/manuals/web-monetization/) developers can now get started with Web Monetization in Defold games.

Next milestone is the release of a sample game and the announcement of the web monetization game jam.

[LEARN MORE](https://defold.com/manuals/web-monetization/)


## Updated community sponsor goal
The Defold Foundation announced a new community sponsor goal for community sponsors on GitHub:

**GOAL: COVER 50% OF NATIVE EXTENSION BUILD SERVER COSTS FROM GITHUB SPONSORS**
The Defold native extension build servers are hosted with AWS and provided completely free of charge to all of our users. The cost is roughly $1300/month and paid for in full by the Defold Foundation. If you wish to support us and help keep the servers running then please [join as a monthly sponsor](https://github.com/sponsors/defold) or increase your existing monthly donation.


## Defold 1.2.171 beta

Defold 1.2.171 beta

The latest Defold beta has been released. Read the [full release notes](https://forum.defold.com/t/defold-1-2-171-beta/65779) to learn more.

#### Engine
* Issue-4856 - Added: Added gamepad name to input connected event
* Issue-3771 - Added: Added support for iOS storyboard
* Issue-4977 - Fixed: Fix bug with new Apple provisioning profile
* Issue-3381 - Fixed: Android app AAB bundle fixes
* Issue-4983 - Fixed: Sounds don’t crash if they have invalid bitdepth/channel * countfailed message.
* Issue-4946 - Fixed: Fixes for 3D collision/trigger event inconsistencies with 2D events
* Issue-4934 - Fixed: Use correct box size when creating 3d physics with non unit scale
* Issue-4953 - Fixed: Make sure scaling isn’t applied twice on 2D physics circle shapes
* Issue-4908 - Fixed: Crash fix for loading collections with the same name
* Issue-4882 - Fixed: Allow more than 16 collision shapes
* Issue-3181 - Fixed: Optimized rendering of 9-sliced untextured gui boxes
* PR #4931 - Fixed: Add missing rendering profiles for vulkan

#### Editor
* PR #4978 - Fixed: Make editor report a build error on non-existent custom resource
* PR #4935 - Fixed: Panel resize handle fixes (DEFEDIT-4875)
* PR #4891 - Fixed: Backspace now works in editorwith shift pressed
* PR #4905 - Fixed: Support building SPIR-V from editor (Vulkan)
* Issue-4886 - Fixed: Set ui elements in bundle dialog to same size on different OSX systems
