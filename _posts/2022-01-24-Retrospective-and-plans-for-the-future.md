---
layout: post
title:  Defold in 2021 - Retrospective and plans for the future
excerpt: In this blog post we take a look at the year that has passed and the plans for next year
author: Björn Ritzl
tags: ["news", "roadmap"]
---

# A changing landscape
Creating a one year roadmap for something as complex as a game engine is no easy task. Not only does a game engine span many different technologies and systems but it also does not exist in a vacuum. The platforms on which game engines and other software runs are constantly evolving, with new releases happening at least once a year. And with these releases comes changes and new requirements, often fairly easy to adapt to but sometimes of a very disruptive nature.

Each year we try to take this ever changing technological landscape into account when we draw up high level plans for Defold, and while we’ve done this for many years and learned a lot on the way, we know that things may change suddenly and without much notice, forcing us to adjust course and abandon planned work in favour of new opportunities or new requirements.

<div align="center"><p style="font-size: larger"><i>"The roadmap is our plan for the year, not a contract"</i></p></div>


We try to communicate this as best we can; the roadmap is our plan for the year, not a contract to deliver exactly everything in the roadmap. As a developer it may be disappointing to not see that specific item in the roadmap delivered by the end of the year, but it usually happens for a good reason.

In this blog post we’ll try to explain some of the reasons why things don't always go according to plan and how we try our best to adapt to changes and new opportunities. We will also compare the roadmap of 2021 with the actual delivered features, and finally also reveal some of our plans for this year. Before we start the retrospective of the year that has passed we need to go further back in time and set the stage so to speak.


# Two years of independence
This year marks the two year anniversary of Defold operating as a fully independent organisation without a corporate owner. Ownership rests with the Defold Foundation, a for-profit foundation with its headquarters in Stockholm. There are no ties to the former owner King, and any and all decisions made by the foundation are made with full autonomy.

The goal of the Defold Foundation is to oversee continued development of Defold in an open and transparent way and to ensure that Defold is available for free for anyone to use.

The foundation is working with a group of companies to execute on the vision and the goals for Defold:

* __Development and operations__ - The foundation is working with [Refold](https://www.refold.io/) to oversee the day-to-day operations of Defold. Refold is an independent game technology company and it currently has three full time employees working with Defold and its partners.
* __Accounting__ - View Ledger, in collaboration with Grant Thornton, is handling all of the accounting on behalf of the foundation.
* __Legal__ - The foundation is working with an expert in video game and game tech law to handle any legal needs that may arise.

<div align="center"><p style="font-size: larger"><i>"We wouldn’t be able to continue working on Defold at this pace without the support of our corporate partners!"</i></p></div>

The work done by this group of companies has to be funded, and while the foundation itself received some funds when it was created two years ago, that money only covered a relatively short runway. Without additional sources of income the foundation would have been bankrupt by now. Fortunately the foundation has so far been successful at securing additional funding to pay for the continued development of Defold. The main sources of funding are:

* __Corporate Partnerships__ - The Defold Foundation is supported by [Melsoft Games](https://defold.com/2020/08/11/Melsoft-Games-partners-with-the-Defold-Foundation/), [Rive](https://defold.com/2021/02/16/The-Defold-Foundation-partners-with-Rive-Inc/), [Heroic Labs](https://defold.com/2020/05/26/Heroic-Labs-joins-as-a-corporate-partner/) and [Game Distribution](https://defold.com/2020/12/15/GameDistribution-joins-the-defold-foundation/).
* __Donations and grants__ - During 2021 Defold, Phaser and Godot each received a generous donation from [OP Games](https://defold.com/2021/11/09/The-Defold-Foundation-receives-a-generous-donation-from-OP-Games/). And in 2020 the foundation applied for and received a grant from [Grant for the Web](https://defold.com/2020/06/09/Defold-is-awarded-a-grant-from-Grant-for-the-Web/).
* __Community sponsors__ - The Defold community of independent developers help offset some of the operational costs [through Patreon and GitHub Sponsor donations](https://defold.com/community-donations/).

The bulk of the funding comes from the corporate partnerships. We wouldn’t be able to continue working on Defold at this pace without the support of our corporate partners! The corporate partners fund general development of Defold and sometimes also work closely with us on specific projects, tasks and integrations.

The partnership with Rive is one such example where their funding allowed us to make significant improvements to the way the engine and editor can be extended with new functionality, and where the Rive integration was the first example of one such extension.

Another example is the partnership with Melsoft Games where their funding has resulted in very significant improvements to the stability and performance on both Android and iOS. The improvements we’ve made had an immediate impact on Melsoft’s hit game Family Island and over time also greatly helped Defold developers world wide through our regular release cycles.

The work done in collaboration with our corporate partners is also part of the reason why the roadmap diverges over the year as new partners are welcomed and feature requests are received from existing partners.

This option is obviously available to anyone. If you require a specific feature you have three main options:

1. Implement the feature yourself (the source code is after all [available on GitHub](https://github.com/defold/defold))
2. Wait for it to be implemented by the team or
3. Fast track it through a corporate partnership.


# Reviewing 2021 from a roadmap perspective
In the 2021 roadmap (https://defold.com/2021/02/09/A-first-look-at-the-2021-roadmap/) we focused on four main areas of work. Let's have a look at how we performed in each of these areas:

* Platforms
* Extensions
* Stability and performance
* New features

## Platforms
When it comes to platforms we made several planned improvements. Let’s start by looking at what we planned for Android and what we ended up with:

* We did update to Android API level 30 as promised
* We did not upgrade to Android 12
* We did migrate from the old dx tools to d8
* We did not add support for Play Asset Delivery

We did also deliver massive improvements to reduce crash and ANR frequency. We also delivered support for controllers and gamepads even though we considered it a stretch goal for the year.

Our plans for iOS were more modest:

* We did updated to iOS 15 as promised
* We didn’t solve the iOS simulator issues in time (but the fix is included in the first release of 2022)
* We did not add support for controllers and gamepads.

We also planned for additional console support and while we did not deliver support for PlayStation this year it is something we guarantee will happen in 2022.


## Extensions
Another area we planned to put a lot of emphasis on in 2021 was that of Defold extensions:

* We delivered updates to Facebook and Firebase Analytics as planned
* We added an official AdMob extension as planned
* We did not deliver a Firebase Crashlytics extension

We also planned for a move of the physics engines and Spine to extensions:

* We did not move the physics engines to extensions
* We did move Spine to an extension (some work remains but it can be used in production already)

It might be worth mentioning that the community came through on this one instead as forum user d95mas released a [full Box2D extension](https://defold.com/assets/defold-box2d/).


## Stability and Performance
The focus on stability and performance is a never ending task, and last year was no exception:

* We did deliver an updated texture compression pipeline
* We did not add support for culling (but there are interesting and recent design discussions taking place [on GitHub](https://github.com/defold/defold/issues/3406))
* We did not fix issues with variable and high refresh rate screens
* We did make the planned performance improvements for meshes and fonts
* We did not make the planned improvements for draw call reduction on sprites
* We did some improvements to the editor performance for large projects but we still have quite a bit of work left


<div align="center"><p style="font-size: larger"><i>"The fact that we did not deliver on these planned features is the largest disappointment to us as a team"</i></p></div>

## New features
We had plans for several exciting improvements to Defold, but unfortunately did not deliver on several of them:

* We did not release support for multiple textures on sprites
* We did not release 9-slice support on sprites
* We did not add support for mesh based physics collisions
* And we did not add support for an initial disable state on game objects and nodes from the editor
* We did however add support for run-time modification of collision object groups and masks

The fact that we did not deliver on these planned features is the largest disappointment to us as a team. The reason is mainly due to the work that we did together with our corporate partners. This work added a lot of new functionality to Defold as a product, only not the functionality we had planned at the beginning of the year.

# Looking ahead
So what is in store for this year? A lot! But we have decided to be a bit more conservative with our plans and also communicate changes to the plans better. We will still group work into four areas:

* Platforms
* Extensions
* Stability and performance
* New features


## Platforms
Besides the standard platform updates that we do each year we will also release PlayStation support. We are unable to commit to a date, but it is very likely that you will see support for PS4 announced before the summer.

## Extensions
We will continue to work on various extensions in 2022. We will update existing extensions as needed and add new official extensions when the opportunity arises.

Our plan is to work actively on securing funding for development of editor extensions that go beyond the existing editor scripting capabilities today. We want developers to be able to create new tool windows and gizmos in the editor.

## Stability and Performance
Our top priority in this department is to fix the known issues in Defold when using screens with variable or high refresh rates. Culling is still very much in our plans as it ties into some of our goals for this year in terms of new features.


<div align="center"><p style="font-size: larger"><i>"There is very high value in improving the 3D support in Defold, without sacrificing anything in terms of performance, stability or engine size"</i></p></div>

## New features
We’ve seen some amazing work done by our community to advance the use of 3D elements in Defold. Here are some examples:

* [Blender Sync Tool](https://forum.defold.com/t/building-a-sync-tool-for-blender-to-defold/69920)
* Advanced rendering setups
   * [Shadow map filtering](https://forum.defold.com/t/shadow-map-filtering-pcf-poisson-pcss/70142)
   * [SSAO/SSLR/Deferred shading](https://forum.defold.com/t/ssao-sslr-deferred-shading/70100)
* Physics
   * [DAE mesh collisions](https://forum.defold.com/t/using-a-dae-mesh-for-collision/69434)
* Games
   * [First Person Shooter](https://twitter.com/aglitchman/status/1479924964425801729)
   * [F18 Interceptor](https://forum.defold.com/t/f18-interceptor-building-my-favorite-old-amiga-game/69851)
   * [Foggy Fox](https://yandex.ru/games/?app-id=181065)

Our goal will never be to take Defold in a direction where we try to directly compete with Unity or Godot in terms of 3D capabilities, but we do believe there is very high value in improving the 3D support in Defold, without sacrificing anything in terms of performance, stability or engine size.

For 2022 we’d like to take a step back and identify where we can get the most bang for the buck. Some of our current ideas include:

* Improving the model importer
* Redesigning our atlas/texture system
* Expose advanced rendering features
* Mesh collisions

This part of the roadmap is still a work in progress. We will share more with you as soon when we have fleshed out the details.


# Final thoughts
It’s hard to summarise a full year of product development in a single post, and this post turned out way longer than initially planned! It is safe to say that working on Defold is amazingly fun most of the time and incredibly frustrating on occasion. With us on this rollercoaster of a ride we have our amazing community of passionate developers and our generous corporate partners. We thank you for sticking with us in 2021 and we look forward to working with you in 2022.
