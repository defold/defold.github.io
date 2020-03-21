---
layout: text
title:  Defold in 2019 - A Year in Review
excerpt: Another year has gone by, but before we put the old year completely behind us we should look at some of the great accomplishments of 2019
author: Björn Ritzl
type: blog
---

# Defold in 2019 - A Year in Review
Another year has gone by, but before we put the old year completely behind us we should look at some of the great accomplishments of 2019.

## Defold releases
During 2019 we made [20 full Defold releases](https://forum.defold.com/c/releasenotes) and while we usually try to keep a two week release cycle throughout the year we sometimes need to stop and take a little bit more time between specific releases. This year we saw the release of iOS 13 where we ran into a couple of unforeseen problems during the migration process forcing us to slow down and spend a bit more time on a few releases. Despite these delays we managed to keep a good development pace with some really great new functionality being released. Let’s take a look at some of the new features shipped this year.

#### Resource Properties
The new resource properties functionality was first mentioned quite some time ago, but as with any development project priorities shift over time and the feature was postponed a number of times until finally released in version 1.2.163. The new functionality allows developers to set multiple resource properties on a script and then assign them to components at runtime. [Learn more in the script properties manual](https://defold.com/manuals/script-properties/#resource-properties).

#### Vulkan
Since the announcement from Apple to deprecate OpenGL in favour of Metal on macOS and iOS we’ve worked on migration plan. In our case the choice was made to add support for the new Vulkan API and use this as a springboard to also access Metal via MoltenVK. With Vulkan in place we not only get access to Metal but it opens up a lot of exciting new possibilities during 2020 and beyond.

#### Editor Extensions Scripts
We want to provide a way for developers to extend the functionality of the editor to build their own tools. The editor extension script support is the first step towards this goal and we have already seen some useful scripts being shared between users on our forum. [Learn more about editor extension scripts in the manual](https://defold.com/manuals/editor-scripts/).

#### Physics Joints
A long requested addition to the physics system has been support for joints and in 2019 we were finally able to add support for several types of both 2D and 3D joints. Joints can be used to create ropes, chains, springs and also motors. [Learn more about joints in the physics manual](https://defold.com/manuals/physics/#joints).

#### Reduced engine size and improved engine modularity
During the year we have trimmed down the engine size and modularized the engine by moving non-critical components into extensions. The Facebook and Google Game Services integrations along with support for push notifications, in-app purchase and the web view have all been moved into separate native extensions. This gives developers a smaller engine core and a choice of which additional components to include in their games.

#### A stable editor for everyone
The editor has received a ton of stability improvements and updates over the course of the year. We have updated to a much more recent Java and JavaFX version, added a perspective camera when working in 3D, cleaned up the game project editor, improved the debugger and reduced build times.

#### Website updates
This year we released a new version of our site. The content is mostly the same but it should load a lot faster and also allows us to build and expand the content much quicker during 2020.

## A great community
Our fantastic community of developers have continued to amaze us and make us proud. We have seen a lot of great games, too many to list in this retrospective, but here’s a few that stood out.

* [Family Island](https://play.google.com/store/apps/details?id=com.test.familyage&hl=en)
* [Interrogation: You will be deceived](https://interrogation-game.com/)
* [Faerie Solitaire Harvest](https://store.steampowered.com/app/348910/Faerie_Solitaire_Harvest)
* [Raft Wars Multiplayer](https://poki.com/en/g/raft-wars-multiplayer)
* [Bouncer Story](https://www.helmigames.com/bouncer-story/)
* [Monkey Kick](https://fb.gg/play/monkeykickinstant)

We should also give special mention to Ben James and [all of the great games](https://benjames171.itch.io/) he created in 2019.

Besides all the great games released last year we’ve also seen quite a few new assets released in our [asset portal](https://defold.com/assets/). And we keep seeing great interaction in our forum and on Slack. We are very thankful for our super-friendly and helpful community. Forum members such as Pkeod, ross.grams, selimanac, amel, gianmichel, Insality, Jerakin, dapetcu21, TheKing009, 88.josh and sergey.lerg earn special mention for all the help they give to their fellow Defold users. Thank you!

## What’s in store for 2020?
We’re really looking forward to 2020 as we have several exciting things planned for Defold. We're not quite ready to reveal anything yet, but we promise to share our plans with you soon. Until then we wish you a great 2020 and we wish all of you good luck with your projects!
