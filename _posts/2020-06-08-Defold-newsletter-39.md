---
layout: post
title:  Defold Newsletter 39
excerpt: Things are still very busy since the launch of the Defold Foundation and the source code for Defold was made available. This newsletter tries to sum up some of the great things that have happened since last time. Read on to learn about the Defold Foundation's first corporate partner, some great new games in the making, two very useful extensions and of course the latest Defold beta!
author: Björn Ritzl
---

Hello, Defolder! 👋

Things are still very busy since the launch of the Defold Foundation and the source code for Defold was made available. This newsletter tries to sum up some of the great things that have happened since last time. Read on to learn about the Defold Foundation's first corporate partner, some great new games in the making, two very useful extensions and of course the latest Defold beta!

## Games
### Rebel Squad
Ben James is at it again! This time it's a lovely mashup of Laser Squad and Rebelstar. The game is in active development and we can't wait to play it! [Follow Ben on Twitter](https://twitter.com/benjames171) for the latest updates. [READ](https://forum.defold.com/t/rebel-squad/65334)

### 3D experiments
Forum user Dragosha (creator of Look, Your Loot!) has been playing around with the Defold mesh component and made some great looking experiements with a mix of 3D and Spine elements. [Follow Dragosha on Twitter](https://twitter.com/dragosha) for the latest updates. [PLAY](https://dragosha.com/defold/3d/)


## Heroic Labs joins the Defold Foundation as a corporate partner
Heroic Labs have joined the Defold Foundation as a corporate partner. The Defold Foundation will work together with Heroic Labs to make the Nakama open-source realtime server for apps and games available to Defold developers. [LEARN MORE](https://defold.com/2020/05/26/Heroic-Labs-joins-as-a-corporate-partner/)


## Assets
### Nakama
Nakama is Heroic Labs' open-source server designed to power modern games and apps. Features include user accounts, chat, social, matchmaker, realtime multiplayer, and much more. The recently released Defold client implements the full API and socket options with the server. [LEARN MORE](https://defold.com/assets/nakama/)

### GoG Galaxy
If you plan to ship your game on GoG you will have to implement the GoG Galaxy SDK. Luckily for you the Defold community already got you covered. We thank forum user @dapetcu for the contribution! [LEARN MORE](https://defold.com/assets/gog-galaxy/)


## Defold 1.2.170 BETA
### Disclaimer
This is a BETA release, and it might have issues that could potentially be disruptive for you and your teams workflow. Use with caution. Use of source control for your projects is strongly recommended.

### Access to the beta
Download the editor and bob.jar from http://d.defold.com/beta/. Set the editor build server to https://build-stage.defold.com in the editor Preferences window.

#### Engine
* Issue-3381 - Added: Added support for Android App Bundles
* Issue-3189 - Added: Added support for physics scaling
* Issue-4845 - Fixed: Don't render while iconified
* Issue-3181 - Fixed: Refactor handling 9 slice gui node with no texture.
* Issue-4830 - Fixed: Add all keys input binding to builtins.
* Issue-4873 - Fixed: Added helpful information to script templates
* Issue-4710 - Fixed: physics.raycast now can return all results
* Issue-3315 - Fixed: Fix label rotation
* Issue-4821 - Fixed: Respect texture-compression setting when creating app bundle.
* Issue-3342 - Fixed: Fixed parsing issue with go.property(...) with regards to spaces
* Issue-4831 - Fixed: Pass nil to window.set_listener() to unsubscribe
* Issue-4849 - Fixed: NE: Remove GraphicsAdapterOpenGL symbol when linking headless builds
* Issue-1848 - Fixed: Fixed inconsistency between setting (0,0,0) and (0) as scale in factory create
* Issue-4784 - Fixed: Handle display cutout in immersive mode
* Issue-4775 - Fixed: Don't try to get the animation frame index if no animation is set

#### Editor
* Issue-4821 - Fixed: Add texture compression option to bundle dialog.
* Issue-4844 - Fixed: Added donate link to the editor help menu
* PR #4800 - Fixed: Specify exact JDK version to download
* PR #4813 - Fixed: Fix misplaced docstrings in the editor code

#### Defold source
* Issue-4803 - Fixed: Update to Emscripten 1.39.16
* Issue-4827 - Fixed: Package path can now point to a local folder
* Issue-4815 - Fixed: Detect missing sdk before engine build
* Issue-4822 - Fixed: Updated engine to use MSVC 2019
* Issue-4640 - Fixed: Added support to build/package our external libraries using waf
* Issue-4817 - Fixed: Updated the engine coding guidelines
* Issue-4640 - Fixed: Added script to build external packages using our build system
