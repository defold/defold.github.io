---
layout: post
title:  Defold Newsletter 43
excerpt: This week we have some new games to share, a community driven game jam for you to join, an interview with one of our community members and finally also the latest Defold release notes.
author: Björn Ritzl
tags: ["newsletter"]
---

Hello, Defolder! 👋

This week we have some new games to share, a community driven game jam for you to join, an interview with one of our community members and finally also the latest Defold release notes.

## Games
### Basketball Dunk
 _"Basketball Shoot Hoops and Slam Dunk is a basketball game where you tap the screen to make your basketball bounce. Shoot a score before the timer runs out. Make a slam dunk if you can."_

[INSTALL](https://play.google.com/store/apps/details?id=com.madelephantstudios.flappybasketball)

### Cold Path
Cold Path is a new turn-based multiplayer strategy game in development by forum user Denis Makhortov. The game promises a rich and very detailed game play, perfect for all fans of strategy games!

[LEARN MORE](https://forum.defold.com/t/cold-path-turn-based-multiplayer-strategy/65722)

### Interrogation - soon on Nintendo Switch!
We are very proud to share the news that "Interrogation: You will be deceived" will make its debut on Nintendo Switch on the 28th of July! This will be the first Defold game released on the Nintendo Switch.

[WISHLIST](https://www.nintendo.co.uk/Games/Nintendo-Switch-download-software/Interrogation-You-will-be-deceived-1810591.html)


## Creator Spotlight: Alex
In the Creator Spotlight posts we invite Defold users to present themselves and share a bit of their background, their work and things that inspire them. In the first ever Creator Spotlight we invited Alex (aka Topbraj), the creator of Fates of Ort, to tell us a little bit about himself and his current project.

[MEET ALEX](https://defold.com/2020/07/20/Creator-spotlight-Alex/)


## #MadeWithDefold Jam

The #MadeWithDefold jam is running from July 18 to July 31. The jam is a community driven initiative by forum user Pawel Jarosz (thank you Pawel!). There are several prices for the winner and runner-ups and since the jam just started there's still time to join and create something cool!

[JOIN](https://itch.io/jam/madewithdefold-jam)


## Updated community sponsor goal
The Defold Foundation announced a new community sponsor goal for community sponsors on GitHub:

**GOAL: COVER 50% OF NATIVE EXTENSION BUILD SERVER COSTS FROM GITHUB SPONSORS**
The Defold native extension build servers are hosted with AWS and provided completely free of charge to all of our users. The cost is roughly $1300/month and paid for in full by the Defold Foundation. If you wish to support us and help keep the servers running then please [join as a monthly sponsor](https://github.com/sponsors/defold) or increase your existing monthly donation.

We thank our latest community donors: piXelicidio, MamontRussel, David Chadwick and Evgeniy Kolpakov!

[BECOME A COMMUNITY DONOR](https://defold.com/community-donations/)


## Defold 1.2.171

The latest Defold version has been released. Read the [full release notes](https://forum.defold.com/t/defold-1-2-171-has-been-released/65837) to learn more.

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
