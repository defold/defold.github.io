---
layout: post
title: Making YouTube Playables with Defold - Green Train and Playgama interview
excerpt: Green Train Studio and Playgama share how Arrow Cube 3D was built with Defold, how its initial download is just 3 MB, and what it takes to bring a web game to YouTube Playables.
author: Paweł Jarosz
tags: ["spotlight", "interview", "web", "html5", "youtube", "playgama"]
---

We invited [Green Train Studio](https://greentrainstudio.com/) and [Playgama](https://playgama.com/) to talk about [Arrow Cube 3D](https://www.youtube.com/playables/UgkxnPqxcJUmgXjPvM1Tr8NDqX5rz2lUBUS3), a puzzle game made with Defold and published on web platforms including [YouTube Playables](https://www.youtube.com/playables). The game takes the familiar idea of removing arrows from a puzzle and wraps it around a rotating 3D cube.

Green Train Studio shares the development side of the story: how they were designing levels, why they chose Defold and how they kept the initial download small to meet the platform requirements. Playgama explains how its Bridge SDK and publishing support helped bring the game to YouTube, and what the platform offers developers.

![Arrow Cube 3D puzzles made with Defold](/images/posts/playgama/defold_playgama_green_train_yt_playables.webp)
<div align="center">
_Arrow Cube 3D, made with Defold by Green Train Studio_
</div>

##### Welcome! Who is behind Green Train Studio, and what experience does the team have?

**Green Train:** Green Train Studio currently consists of three people: a developer, a producer, and a UI/UX designer. Before starting the studio, we gained many years of experience creating mobile games. Now we have begun our independent journey into web gaming, applying our mobile development expertise while exploring new platforms, audiences, and distribution opportunities.

##### Where did the idea for Arrow Cube 3D come from, and what does a rotating 3D cube add to the arrow-removal mechanic?

**Green Train:** We are constantly researching mechanics that have proven to be engaging for players and looking for ways to introduce meaningful improvements to them. Moving the arrow-removal mechanic into a 3D environment was exactly this kind of significant change. It gives players a new perspective on an already familiar mechanic and can attract a new audience to the genre.

##### How are the puzzles created and validated? Are levels handcrafted, procedurally generated, or a combination of both?

**Green Train:** We use a combination of procedural generation and handcrafted level design. Because we want to provide players with a large amount of content, we first create a level generator. It defines the intended difficulty progression using a wide range of parameters. We use our experience to produce the initial version of the level sequence, and then use analytics to tune and improve the existing levels. However, the first-time user experience is especially important, so the first 20 to 40 levels are usually created manually and carefully validated by a game designer.

![Arrow Cube 3D puzzles made with Defold](/images/posts/playgama/arrow_cube_1.webp)
<div align="center">
_Arrow Cube 3D, made with Defold by Green Train Studio_
</div>

##### Why did you choose Defold for the game? What advantages do you see?

**Green Train:**

<div align="center"><p style="font-size: larger"><i>“We chose Defold because it is highly optimized for web games.”</i></p></div>

It allows us to keep the initial build size at approximately 3 MB, resulting in almost instant loading and minimizing frustration for players. Defold gives us a strong technical foundation for web distribution without requiring extensive additional optimization.

##### What were the most difficult technical challenges, and how did Defold help with 3D graphics, touch controls and performance?

**Green Train:** The biggest technical challenge was creating a level generator that was fast enough to produce a large amount of content while also supporting enough parameters to generate varied and interesting levels. In terms of 3D graphics, performance and touch controls, Defold handled everything very well. For these parts of development, we did not experience any significant limitations compared with more commonly used engines such as Unity.

![Arrow Cube 3D running alongside its project in the Defold editor](/images/posts/playgama/arrow_cube_defold_editor.webp)
<div align="center">
_Arrow Cube 3D in the Defold editor_
</div>

##### What were the game’s build size and loading time, and what optimizations were necessary to meet web and YouTube requirements?

**Green Train:** The core game build is approximately 3 MB. Most of the remaining content, around 20 MB, consists of level data. However, the levels are loaded in batches, so players only need to download the initial 3 MB when launching the game. As a result, the initial loading time is almost instant. Defold is already well optimized for web games, so we did not need to implement a large number of additional optimizations to meet the platform requirements.

<div align="center"><p style="font-size: larger"><i>“The core game build is approximately 3 MB.”</i></p></div>

##### Turning to Playgama: what is Playgama Bridge, and how does it help a Defold game work across platforms with different SDKs and requirements?

**Playgama:** Playgama Bridge is a unified SDK. A developer integrates it once, and the game can be shipped to dozens of instant-play platforms — YouTube Playables, Xiaomi, CrazyGames, MSN, Y8, Poki, Discord, Playgama.com and others — without a separate integration for each. When your game runs on a supported platform, Bridge automatically loads that platform's native scripts and routes API calls to it. In unsupported environments, including local development, Bridge uses a mock platform: calls return safe defaults (false, reject, etc.) instead of throwing, so you can develop and debug before publishing.

Every instant-play platform exposes the same handful of capabilities differently and supports a different subset of them, and that subset changes over time. YouTube Playables is a live example: monetisation is still rolling out by region, so ad calls have to check that a placement is actually supported before firing. Playgama Bridge is what keeps that kind of platform-specific behaviour out of the game code.

A unified SDK is broadly useful, but the advantages differ depending on studio size and resources. Indie developers, for example, benefit most from the time saved not having to build multi-platform tools from scratch, whereas mid-sized and larger studios mainly gain efficiency, cost savings, and quicker releases.

We’ve prepared clear instructions for developers ([in a special wiki section](https://wiki.playgama.com/playgama/bridge-sdk/getting-started)) and the Bridge SDK plugin for Defold ([on its GitHub page](https://github.com/playgama/bridge-defold)).

##### How did the Playgama Bridge integration go for Arrow Cube 3D?

**Green Train:** The Playgama Bridge integration was very quick because the project's infrastructure had already been fully prepared for easy integration. The SDK itself is very well designed and easy to work with.

<div align="center"><p style="font-size: larger"><i>“It also comes with excellent documentation for Defold.”</i></p></div>

As well as an AI agent that makes the integration process even smoother.

##### What made Arrow Cube 3D a promising candidate for YouTube Playables, and which performance metrics influenced its selection?

**Playgama:** Arrow Cube 3D had one unique advantage. Arrow puzzles are a popular format, but almost all of them are 2D, which made this one naturally stand out.

Also, on YouTube Playables, we only publish games that already have a good performance track record elsewhere, and the reason is analytics. Playables itself tracks only a few metrics: gameplays, with breakdowns by age, gender, and geography. There is no session length, no retention, and no DAU or MAU, and external analytics services are prohibited. So if a game underperforms on Playables, there is no way to find out why, let alone fix it. Conclusions can only be drawn from how a game performs elsewhere — on Playgama.com, CrazyGames, Poki, MSN, Playhop, or other platforms where proper analytics are available.

The metric we weigh most heavily when assessing a build is the first 30 seconds — how many players stay past them.

![Arrow Cube 3D running on YouTube Playables under Playgama’s account](/images/posts/playgama/arrow_cube_yt_playables.webp)
<div align="center">
_Arrow Cube 3D on YouTube Playables, published through Playgama_
</div>

##### What technical and content requirements must a game satisfy to reach YouTube Playables through Playgama?

**Playgama:**

* The initial load — everything before the game signals GameReady — must stay under 30 MB. No individual file may exceed 30 MB. Compression is not allowed, although a decompression fallback is fine. The ZIP archive itself can run up to 200 MB.
* The GameReady signal must be sent only when the player can genuinely interact.
* No external calls, which rules out third-party analytics, external multiplayer servers, and conventional IAPs.
* Pause and mute commands must be honoured immediately, and in-game audio settings must never override the platform's.
* Both portrait and a properly adapted landscape orientation must be supported, with no black bars at the sides, and elements must scale correctly at 1:1, 16:9 and 9:16. In the desktop version there must be no black or blurred sidebars at the edges of the game.
* The game must run across all device types, with Android S+ and iOS 14+ as targets and Chrome and Safari as the primary browsers.
* All assets must be original or properly licensed, with no traces of other IP — skins, characters, images and so on. YouTube does not accept reworks or outright copies of well-known studios' games.
* Visuals should be colourful and readable, interfaces legible, and the build free of bugs that break or obstruct play.

##### What did Playgama handle during testing, certification and communication with YouTube that Green Train would otherwise have needed to manage itself?

**Playgama:** Publishing directly means applying to Google for Developer Portal access through an interest form and waiting weeks or months for approval. It requires a registered legal entity, Channel Manager permissions in YouTube Studio, a direct SDK integration, and handling testing, certification and live operations yourself.

This whole process is much easier with a dedicated distributor. With Playgama’s help, Green Train only had to integrate the Bridge SDK for Defold and fix the build against the YouTube Playables requirements we flagged.

Moderation on YouTube Playables is thorough. Games are tested in depth, and even fairly obscure mistakes get caught. We ran QA using the official YouTube Test Suite, checked the build against every platform requirement, returned a specific list of what needed changing, and submitted the game for certification through our verified portal account.

All communication with YouTube's partnership team ran through us. Playgama has established connections with YouTube Playables and is now the number one distributor on the platform by gameplays, as well as among the top three by number of games published — which means games we distribute reach players faster. The route to live is two to four weeks rather than months, and new releases launch from an account with a substantial history behind it.

![Arrow Cube 3D showing different cube rotations and arrow layouts](/images/posts/playgama/arrow_cube_2.webp)
<div align="center">
_A familiar arrow-removal mechanic, seen from a new perspective_
</div>

##### How does Arrow Cube 3D perform across web portals, and how do their audiences differ?

**Green Train:** Arrow Cube 3D has shown strong engagement metrics, particularly in terms of playtime. On many platforms, the average playtime reaches 30 minutes or more. The game also maintains solid web retention, with D1 retention generally starting at approximately 7% and sometimes going higher. However, these metrics vary significantly depending on the platform and its audience. On platforms with younger audiences, such as CrazyGames and Poki, both playtime and retention were noticeably lower. On platforms with an older audience, average playtime exceeded 65 minutes and has remained consistently at that level.

##### Is YouTube Playables meaningful as a revenue channel, a discovery channel, or mainly an investment in future reach?

**Green Train:** For us, YouTube Playables is primarily an investment in the future because YouTube is an incredibly large platform. We have released only one game there so far, so we are still exploring the market and learning more about its audience. One of our next objectives is to create more games specifically for YouTube Playables, with mechanics and formats that are better suited to the YouTube audience.

**Playgama:** All three, in proportions that depend on where a studio starts from — and the balance is moving quickly. We launched our first few games there in September 2025 as a small pilot. In June 2026 alone our portfolio generated 57M gameplays across almost 50 active titles.

On revenue: YouTube began testing ad monetisation in March 2026, in limited geographies and only for a selected group of developers and publishers, which we were fortunate to be part of. Even inside that restricted test group, our games average $3.1k a month. gCPM for most games sits between $1 and $2, and a game earns roughly $10,000 gross per million gameplays — with a million gameplays a week an achievable benchmark here. Our best-performing title cleared $15,000 net in its first month. For a large mobile title that is an additional revenue stream; for an indie developer it can realistically become the main one.

The caveat is that monetisation is still rolling out. Ads are not served to every user or on every device — by our estimate the system is running at roughly 15–20% of its eventual capacity, and everything above is being earned under those conditions. As new countries onboard, those figures should rise substantially.

On discovery: games surface through algorithmic recommendations, which in our observation work much like YouTube's video recommendations, so a good game can reach millions of players with no acquisition spend at all.

Both of those point the same way. The intuitive move is to wait until monetisation is fully switched on, and we think that is the weaker play: once it is, competition will be considerably higher and breaking into recommendations much harder. Launching now means earning something immediately, building an audience the way a channel does on YouTube, and holding a position that keeps generating gameplays afterwards.

![Arrow Cube 3D with a highlighted arrow and increasingly dense puzzles](/images/posts/playgama/arrow_cube_3.webp)
<div align="center">
_Different arrow layouts in Arrow Cube 3D_
</div>

##### Did appearing on YouTube increase traffic elsewhere or improve the studio’s credibility with other publishers?

**Green Train:** We launched on YouTube less than two weeks ago, so we have not yet observed a noticeable effect on traffic to other platforms. However, we believe that releasing a game on YouTube is an important step toward strengthening the studio's reputation and credibility with publishers and other industry partners.

##### What are the most important lessons for Defold developers who want to build a web game for multiple platforms and eventually reach YouTube Playables?

**Green Train:**

<div align="center"><p style="font-size: larger"><i>“The main lesson for all developers, including those using Defold, is to focus first on creating engaging gameplay.”</i></p></div>

Developers should actively study the market and search for mechanics that genuinely interest players. At the same time, it is important to use tools that are well suited to multi-platform distribution. Because Defold is already highly optimized for the web, developers can spend more time improving the gameplay instead of investing excessive time in additional technical optimization.

**Playgama:** Whether you work in Defold or another engine, there are a few core lessons you need to internalize if you are aiming for multi-platform web distribution.

A game must be fundamentally fun and satisfying from the very first click. Pay close attention to the game feel: smooth controls, juicy visual feedback and responsive interactions. On the web, players expect instant gratification, so mechanics should be simple to learn but engaging to master.

Win your players in the first 30 seconds. Initial retention is crucial. If onboarding is slow or the game takes too long to explain itself, players will simply scroll away. Keep the visuals vivid and readable.

Plan your asset architecture early. Web platforms in general and YouTube have strict technical requirements. The initial load before the game signals "GameReady" must stay under 30 MB. While Defold is phenomenal at keeping the core engine size tiny, you must design your content to load in batches rather than packing everything into the initial launch.

Build a fluid, responsive UI. Plan your GUI layouts in Defold to be truly responsive from day one.

Design your monetization from the start. Monetization shouldn't be a bolted-on afterthought. Plan for natural pauses, reward loops, and ad placements that feel organic to the gameplay flow. As platforms roll out broader ad capabilities, a well-thought-out monetization design will dictate your game's commercial viability.

YouTube Playables currently provides limited analytics. To minimize risk, bring a game that already has a strong performance track record on other web portals where you can actually measure, tune and validate the core loop first.

<div align="center"><p style="font-size: larger"><i>“Win your players in the first 30 seconds.”</i></p></div>

##### What are your future plans?

**Green Train:** We plan to continue exploring YouTube Playables and release more games on the platform. In particular, we want to develop games specifically for its audience rather than simply adapting existing projects. Our goal is to better understand which mechanics, formats and types of content perform best on YouTube and use this knowledge in our future releases.

**Playgama:** We will maintain and grow our presence on the platform. In the immediate term that means the publishing pipeline: we are opening it up for H2 2026 and are actively looking for developers with web games that have strong retention metrics and who want an early distribution advantage on YouTube Playables. The window matters. The ecosystem is expanding as new countries onboard, and the infrastructure is on track to run at full capacity, which should raise revenue figures substantially.

##### Thank you both for sharing the development and publishing story behind Arrow Cube 3D. We wish you success with the game and your future releases!

For developers interested in integrating Playgama Bridge with Defold:

- [Playgama Bridge getting started guide](https://wiki.playgama.com/playgama/bridge-sdk/getting-started)
- [Playgama Bridge SDK for Defold on GitHub](https://github.com/playgama/bridge-defold)

*Note that the platform details and performance figures above reflect the teams' experience at the time of the interview.*