---
layout: text
title:  Defold Newsletter 37
excerpt: This newsletter contains three great new Defold games well worth spending a couple of hours (or more!) on. We also have some new shader assets to pimp up your Defold fonts with and two new YouTube videos to learn from.  Finally we also cover the public web monetization Call for Proposals from Grant for the Web. And the latest Defold beta release notes!
author: Björn Ritzl
---

Hello, Defolder! 👋

I hope you are well. This newsletter contains three great new Defold games well worth spending a couple of hours (or more!) on. We also have some new shader assets to pimp up your Defold fonts with and two new YouTube videos to learn from.  Finally we also cover the public web monetization Call for Proposals from Grant for the Web. And the latest Defold beta release notes!

## Games
### Faerie Solitaire Dire
Faerie Solitaire Dire is the upcoming new solitaire game by Subsoap, made with Defold. The new game promises an immersive story and plenty of challenges. [WISHLIST IT ON STEAM](https://store.steampowered.com/app/556530/Faerie_Solitaire_Dire/)

### Crystal Caverns 2
Cystal Caverns 2 is a classic platformer game creatted by Ben James. Dive deep into three caverns full of loot and dangerous hazards. Find secrets and collect crystals and power ups. [PLAY IT](https://benjames171.itch.io/crystal-caverns-2)

### Four distant daughters
Four Distant Daughters is a small point'n'click horror-sci-fi adventure game created by Marco Giorgini in 14 days for [Adventure Jam 2020](https://jams.gamejolt.io/advjam2020). [PLAY IT](https://gamejolt.com/games/four_distant_daughters/488839)


## Videos
### New games by Sergey
Forum user Sergey Lerg has been working together with DashApps on two great mobile titles: [Taxi Town](https://apps.apple.com/app/taxi-town/id1501324428) and [Lunar Orbit](https://apps.apple.com/app/lunar-orbit-space-strategy/id1486762718). In this video Sergey walks us through some of the technical details of the games. [WATCH](https://www.youtube.com/watch?v=sK4pJ8A3YS4)

### Criação de Jogos com Defold
This new Portuguese video tutorial series will cover game development using Defold and other free tools. [WATCH](https://www.youtube.com/watch?v=AsVSeza6oJ4)


## Assets
### DSFonts
The DSFonts asset is a collection of shaders for distance field fonts. You can create gradients, bevel and glow effects on your fonts with ease using the shaders provided by this asset. [LEARN MORE](https://defold.com/assets/dsfonts/)


## Monetization
### Grant for the Web first public Call for Proposals
Grant for the Web, a collaborative partnership between Mozilla, Creative Commons, and Coil, was launched to champion a web that provides openness and opportunity for everyone.

With $100 million to distribute globally over five years, this initial public Call for Proposals will fund projects that contribute to an ecosystem of web monetized content. If you have an idea that explores the use of web monetization in a Defold game (or otherwise!) you should definitely take a look. [LEARN MORE](https://www.grantfortheweb.org/post/announcing-first-public-call-for-proposals)


## Defold 1.2.169 BETA
The latest beta is now released, and we invite those interested in beta testing the new features in the editor and engine to join now. The beta period will be 2 weeks and the next planned stable release is two weeks from now.

We hope this new workflow will highlight any issues earlier, and also get valuable feedback from our users. And please comment if you come up with ideas on improving on this new workflow.

Please report any engine issues using Help > Report Issue.

### Disclaimer
This is a BETA release, and it might have issues that could potentially be disruptive for you and your teams workflow. Use with caution. Use of source control for your projects is strongly recommended.

### Access to the beta
Download the editor and bob.jar from http://d.defold.com/beta/. Set the editor build server to https://build-stage.defold.com in the editor Preferences window.

#### Engine
4773 - Added: Added sound.pause function
4725 - Fixed: Fix for getting sound properties before playing sounds
4697 - Fixed: Fixed issue with calculating the font cache cell size
4586 - Fixed: Make sure collection proxies get an update before rendering
4778 - Fixed: The tilemap does not flip tiles when created
3721 - Fixed: Ignore arrow keys as text events
4758 - Fixed: Generate character/text event for spacebar
4719 - Fixed: IE 11 compatibility (sounds and gamepads)
4742 - Fixed: Configure CFBundleDevelopmentRegion and CFBundleLocalizations in game.project
4747 - Fixed: Check that there’s a world before creating a collision object
4727 - Fixed: Potential fix for writing save file that on rare occasions became corrupt
4715 - Fixed: Updated android build tools to 29.0.3
3712 - Fixed: Box2D crashes when setting a rotation with NaN (DEF-3177)

#### Editor
4753 - Added: Added native extension template to editor
4755 - Fixed: DEFEDIT-4754 Crash when signing mobile dev app for iOS
