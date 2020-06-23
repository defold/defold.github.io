---
layout: post
title:  Interview with Defold Product Owner Björn Ritzl
excerpt: May 2020 was very important for Defold. First, the Defold source code was made available. Second, Defold officially separated from King. Björn Ritzl, Defold product owner, explains why and how this happened.
author: Björn Ritzl
type: blog
---

This interview was first published in [Game World Observer](https://gameworldobserver.com/2020/06/05/defold/).

---

Defold, the game engine from the makers of Candy Crush Saga, doesn’t make news quite as often as, for example, Unreal or Unity. Last May, however, was important for the engine. First, it made the source code available. Second, it officially separated from King. Björn Ritzl, Defold product owner, explains why and how this happened.

**Björn, a couple of words about yourself for our readers, please?**

My name is Björn Ritzl, and I currently work as the product owner for Defold and as a board member of The Defold Foundation. I have worked as a developer for almost two decades, primarily in the games industry, and even longer as a hobbyist writing my first lines of code on a C64 in the late 80s. I have worked with mobile game development since before the smart phones, and I’m a big fan of old school games from the days of the C64 and Amiga.

The last seven years I’ve worked at King where I joined the Defold team when Defold was acquired by King in 2014.

![](/images/foundation/thumbs/Bjorn%20Ritzl_2020_RW.jpg)

**In mid-May, two important decisions were made. One of them was switching the engine to an open source model. Could you tell us about the reasons for that decision? And also, why now? Why not, for example, four years ago?**

We have discussed the possibility to make the Defold source code available for quite some time, and over the course of the last year and a half we have gradually extracted parts of the engine into separate modules and open sourced those. We moved the Facebook integration, push notifications, in-app purchases, webview support and a couple more to basically “test the waters”. This had several positive outcomes: we received some community contributions, the engine got smaller and we were able to focus more of our efforts on the performance and stability of the core engine.

Another factor that contributed to the decision was the fact that we saw an increase in high production value games released by external teams using Defold. External teams investing many months, sometimes years, into an engine that is closed source is fairly high risk to take. We have also heard developers say that they are hesitant to use a game engine created by a competitor. Finally we also received feedback on the terms and conditions for the use of the engine.

When we weighed all of the above together, it was clear that making the source available with a developer-friendly license and moving Defold to a foundation was the right choice to make.

Also worth pointing out is that it’s a pretty massive undertaking to transition a code base developed over the last 10 years into the open. We had to go through every single commit, pull request and branch for anything that could potentially be seen as a security risk (project names, links, keys, certificates etc). Luckily for us, there’s good tools to do this kind of thing. And while we have always tried to keep very high standards when it comes to code quality, it becomes a different thing once you decide to share the code with the world.

![](/images/games/petrescue-half.png)

Pet Resque Puzzle Saga, 2019 (King)

**The new license agreement sounds quite relaxed. In fact, the only obvious limitation is that you can’t sell a modernized version of the engine itself, if I understand correctly? But there must be some additional pitfalls?**

The new Defold license is designed to be as developer friendly as we possibly can. There are no up-front costs, no licensing costs and no royalties. You are free to monetize games made with Defold any way you want. We wish you all the best and have no interest in directly profiting from the success of game developers. The only thing the license prevents you from doing is to package original or modified versions of Defold engine and/or editor and sell those. We want to always ensure that the Defold software is free.

The license we use is the standard Apache 2.0 license with the addition of a non-commercialization clause for the Editor and engine. You can [learn more about the license here](/license).

Now, the choice of this modified license and the addition of a non-commercialization clause means that the Defold source code isn’t Open Source according to the definition of the Open Source Initiative. We say that the source code is available and free to modify, to avoid any confusion. But I guess in a colloquial sense a lot of developers would say that Defold is open source. You can modify the source code any way you like and you don’t have to share the modifications if you don’t want to. And you can sell games made using the modified source code.

The second important decision was the launch of The Defold Foundation. Why did you have to set up a separate organization as opposed to doing everything within King?

Ever since Defold was released as a free to use engine at GDC in 2016, we have repeatedly heard developers say 1) Why isn’t Defold open source? 2) Why are the terms and conditions so strict? 3) What happens if King shuts down Defold? 4) I’m not sure I want to use a game engine created by a competitor.

These are all very valid questions and concerns, and it is understandable that developers ask these questions. You have to put a lot of faith into King as a company and into Defold as a product.

By making the source code available with a developer friendly license we solved concern 1, 2 and 3.

We could of course have made the Defold source code available on GitHub and kept ownership at King, but that would not solve concern number 4. The only real solution was to move Defold outside of King into a separate legal entity, and this is where The Defold Foundation comes in.

The Defold Foundation was created in May 2020 and it is the current owner of the Defold trademark and source code. The foundation is a completely independent legal entity from King. King has a single seat on the board of the foundation, but no other control. When the foundation was created it was given a number of objectives:

* Make the Defold software available to the public
* Make the Defold source code available free of charge to a third-party
* Manage the Defold software through updates, modifications, development and support
* Prevent the Defold software from being commercialised by a third-party

It is registered in Sweden as a foundation and not as a corporation, which means that it has a separate legal status from a corporation. According to Swedish law, the objectives of a foundation cannot be changed once a foundation has been created. And this is important since it guarantees that the Defold source code and product will be made available and kept updated.

![](/images/games/interrogation-half.png)

Interrogation, 2019 (Critique Gaming)

**I can’t help but ask this: making the engine open source, as well as launching a separate organization outside of King to handle all the legal issues related to the engine — does all this mean that the Defold team will become smaller over time?**

This is an interesting question. We have never really talked about the size of the Defold team or the team members themselves. Members have come and gone over the years, and the team has grown and shrunk. I’m guessing that frequent users of the Defold Forum have noticed some names go missing and new names arrive, but overall I don’t think it has been very obvious how many and who has worked on Defold. The initial founders of Defold, Christian Murray and Ragnar Svensson, did for instance take a step back and leave King quite some time ago, and I honestly don’t think anyone noticed (at least no one said anything!). The Defold team was maybe 20 people strong at its peak in 2017 when we worked on so many things at once (website and services, analytics, editor, engine, trainings and onboarding, events, tutorials and manuals). Now that we have a stable product used by developers across the world to ship high quality games, a good website with manuals, tutorials and examples and we have stable backend services there is obviously not the same need and the team size has been adjusted accordingly.

We are currently in a transition phase where we have entered a kind of startup mode for the foundation with only me and one other team member working full time. The rest of the team are still employed by King and working on the engine when time permits. The ambition is of course that this will change once we secure a stable stream of revenue for the foundation. King made a very generous donation when the foundation was created, but it would not be financially responsible to spend all of it at once on a big team.

The foundation will work together with industry partners and enter into corporate partnerships to strengthen the position of Defold as a financially stable and solid game engine. The first corporate partnership was announced last week when Heroic Labs joined as a corporate partner. We are confident to be able to announce more partnerships during the year.

Another thing worth mentioning is that the Defold Foundation has no employees of its own. The foundation will contract developers to work on the engine and editor. This is the setup for me and my colleague and the same kind of opportunity will be possible for contributors from the community in the future. This puts everyone on equal standing with the foundation and I believe it’s another thing that will build trust in the community.

**Let’s talk about the position of the engine itself on the market. How would you rate it?**

The competition is fierce! There are a lot of good engines out there, but if I’m going to try to be objective for a while I believe Defold has a couple of really good things going for it.

There is a significant focus in the industry on AAA 3D console, PC and mobile games right now. If you look at the roadmap of some of the major engines and their recent development updates it’s clear that many engines are putting a lot of effort and money into competing in this space. This is not for Defold. Defold is a 3D engine, but our focus has primarily been on 2D games for web and mobile. We will continue to focus our efforts on staying very competitive in this space. Our engine is really tiny compared to a lot of our competitors (the HTML5 build takes around 800kb gzipped and an Android or iOS build is around 2Mb). This is not to say that we will completely ignore desktop and 3D and we have some things planned to improve in this space without compromising on our key strengths. We also have plans for console support which I believe will make Defold an even more interesting choice…

![](/images/games/fatesofort-half.png)

Fates of Ort, 2020 (8bitskull)

**Since you mentioned competitors… Take Unreal, for example. They regularly give out money and have their own large inventory of assets. It must be difficult for Defold to keep teams from defecting to other engines?**

Yes, this is obviously a challenge. But we don’t want to compete with Unity and Unreal. They have almost infinite resources, BUT they also have products that are very different from Defold. Unity for instance is like a Swizz-army knife. You can use it for almost anything, but not always with the best result. Sometimes there are tools that do a better job of solving certain problems, and that is where Defold comes in. And in the case of Unreal there is a very clear focus on high quality 3D content and games. If a developer is looking for an engine to create a 3D game Defold isn’t the best choice, and I have no problem saying that. But if a developer is looking for an engine to create a 2D game using a performant and small engine then Defold is a very good choice!

**When I recently wrote a piece about Defold (re open-sourcing the engine), I made an unfortunate mistake. Since I hadn’t heard a great deal about Defold from the news, I concluded that it never became a popular tool in the first place. That no hits were made on it. Of course, our readers immediately responded, some of them working with your engine. ‘What about Family Island?’ they said. Following that, I discovered some great games made on the engine. Still, these are comparatively few. It’s almost like Defold does not generate quite as much buzz as GameMaker or Cocos. What do you think is stopping you from exponential growth?**

King never made it a goal to expand the user base of Defold. Most of the growth has been organic and slow, and this has been perfectly fine. We had the luxury of slowly refining a product with the help of a small group of external users. We are now ready for prime-time and it is a priority for the Defold Foundation to grow the user base in 2020 and 2021.

**Do you know many games have been made on the engine to date and how many are in development?**

No idea! We tried to keep track right when Defold was launched in 2016 and we quickly passed 100 released games. That number was based on games we knew about where developers had announced the game on the Defold Forum. A lot of games got released without us ever knowing about them. Now, four years later I’m sure we’re talking thousands of games.

**Can you name the projects made on the engine that you think are the coolest, as well as share the most interesting ones that are only being prepared for release?**

Family Island is a really impressive mobile title with a lot of polish. Nice graphics, good gameplay and an excellent showcase for what you can do with Defold.

I also want to highlight the games from the very productive long time Defold user Ben James. He’s released [a ton of small games over the years](https://benjames171.itch.io/). A lot of the games were created during the course of a week or two which really goes to show how much that can be accomplished using Defold in a short period of time.

Interrogation by Critique Gaming Studios is a very impressive title for desktop and mobile. The retro fantasy RPG, Fates of Ort, currently released on Steam is also impressive.

Look Your Loot is a game that almost stopped all development in the Defold team for a week or two as everyone at the office was competing for the highest scores.

There are so many great games worth a mention that I feel bad for not spending the rest of this interview listing them!

![](/images/games/familyisland-half.jpg)

Family Island, 2019 (Melsoft)

**A few years ago, there was news that Russia ranked second for the number of developers using Defold. Is it still the case?**

Yes, Russia is still an important market. A lot of Defold developers are from that area of the world. But we have users all over (except for maybe Antarctica).

**What would you say is the reason for the engine’s popularity in Russia?**

Not sure. I’m guessing it is a combination of factors. Some early adopters of Defold have their roots in or close to Russia, and they have stayed with the engine for many years, organised the local communities and worked as Defold ambassadors.

**When you attract new developers today, what things do you emphasise, what do you do best?**

It’s very quick to get started with Defold. We have a zero-setup policy. You will be able to download Defold, launch it, select a project template and have a build up on your phone in minutes. There is no need to install any additional tools to create application bundles for any platform. No need for Android Studio. No need for XCode. No need for Visual Studio or any other tool. This is a real strength and something people are amazed at and give us praise for.

Another powerful thing is our extension system. We have a small engine core with the essentials and then provide an easy to use system of extensions/plugins to extend the engine. If you want to use In-App Purchases on mobile or Facebook you add one line in your project settings. If you want to monetize using ads you add another line. And when you build your project we automatically include these dependencies into a custom engine with only the things you need. This ensures that the engine is kept small and that build times are reduced as much as possible. All of this is taken care of automatically as well.

Finally I’d like to highlight the focus on an iterative workflow where we try to reduce build times as much as possible and where it is possible to modify game content and update it while the game is still running. This really helps to reduce friction and it enables developers to work more iteratively on their games as they don’t have to wait for new builds and install those to test their changes.

![](/images/games/bouncer_story-half.png)

Bouncer Story, 2019 (Helmi Games)

**Four years ago, King was ready to support Defold developers in terms of marketing. What can developers working with the engine count on today?**

We can no longer promise free marketing or any such thing, but that was also never a big thing while Defold was owned by King. What we can do is to help promote new games through our social media channels and in newsletters and when talking to corporate partners.

**In one of the old interviews, Oleg Pridyuk said that when creating Defold, King, among other things, wanted to create a toolset that would allow devs to make non-resource-intensive games. How relevant is it today, when even low-end devices have 4 GB of RAM?**

I would say that it is still highly relevant. Sure, the low-end devices available to the rich part of the world are actually pretty powerful, but this is not the case everywhere in the world.

Also worth remembering is that Apple and Google have defined application size limits when downloading over mobile networks. And why waste perhaps 20Mb out of the available 100 or 150Mb on a bloated engine when you can use one that is 2Mb?

And a Facebook Instant Game should start in less than 5 seconds, a feat which is impossible if you have a large engine.

**Another thing highlighted at the dawn of the engine was its HTML5 capabilities. How important is it today? Would you say developers are willing to support this technology in games?**

HTML5 support is *very* important to us. Game portals such as Poki and Facebook Instant Games have shown that there is a lot of potential in games on the web. And with Flash dead, there is room for new technology to take its place.

**We’ve just talked about the advantages of the engine, but there are probably disadvantages. What do you think are its shortcomings?**

One which I’ve mentioned before is the fairly basic support for 3D. We provide enough to create shaders and post processing effects and it’s easy to add basic 3D models and custom meshes, but if you want to do more complex things in 3D or create a big 3D game it’s going to be harder. This is something we have in our roadmap for 2020 to improve on, but currently we’re not there yet.

Defold is also not as well known as for instance Unity, which means that there isn’t as much help to get. The Defold Forum combined with the Defold manuals and learn section on the website is usually enough, but if you compare it with the amount of resources available to Unity developers it is obviously a disadvantage. But on the other hand there’s also a lot of outdated Unity snippets and content that won’t work in the latest version of Unity…

![](/images/games/witchcrafter-half.png)

Witchcrafter: Empire Legends, late 2020 (Paweł Jarosz)

**I also really want to discuss King’s own experience with Defold. As far as I know, not all the company’s games are made on Defold. Why is it? I mean, it would be quite logical and would be such a strong advertising campaign.**

King acquired Defold at a time (in 2014) when Unity wasn’t a thing and when all King games were either created using Flash or another internal engine. This other engine was at the time used by most of the successful titles, such as Candy Crush and Bubble Witch. As with most internal tools, the internal engine had a lot of rough edges and it wasn’t very artist (or developer) friendly at the time. Defold was a fresh new alternative that promised to solve a lot of the problems we had with the internal engine.

At the time, Defold also had some rough edges, but it was light years ahead in many regards but still a huge difference from the polished product that Defold is today. While development of Defold continued at King, some initial games and prototypes were created and released using Defold. For a while, an entire studio was dedicated to rapid prototyping and development of new games concepts using Defold. Some of the games created reached public playtests and the first real hit, Blossom Blast Saga, was released. Blossom was also developed at a record time and with a smaller team than other King games which really proved that Defold solved a lot of problems with game development.

While all of this happened, a new version of Candy Crush and some of the other big hits were created. These games were more or less based on the same codebase as the first versions and thus developed using the internal King engine and not Defold. One exception to this rule was Pet Rescue Puzzle Saga, the sequel to Pet Rescue Saga, which was created using Defold.

I don’t think anyone at the time when Defold was acquired expected Candy Crush and the whole franchise to still be a massive hit eight years later (and still based on the internal King engine). What has also happened is that the expectations on new titles have grown exponentially and with that also the production time, which means that the number of released games have gone down. At the same time, the cost of releasing a game has also gone up, not just because of the increased production time but also in terms of marketing efforts and so on.

I would have loved to see more King games made using Defold, but the lack of Defold games at King is not due to any particular problem with Defold but rather a sign that the game production process and the whole industry has changed a lot these last few years.

**How many of King’s released projects are made on Defold? Will there be more of them?**

Blossom Blast Saga and Pet Rescue Puzzle Saga are the two games currently live. The first Defold game that was released was a world puzzler called Keyword, but that game is no longer available. And for every live game there’s probably 5 to 10 games that reached various stages of production, some cancelled early, others taken as far as public playtests (LifeStories and Stellar: Galaxy Commander are the ones I remember). King is also using Defold to port a lot of old Flash games at the RoyalGames skill games site (this was part of the old testing ground for game concepts).

**What should we expect from Defold in the next six months or a year?**

We have outlined our plans in the 2020 roadmap. We will continue to improve on the mobile platforms, with a particular focus on platform integrations for iOS and Android. On HTML5 we will focus on size and performance. In the editor and engine we will focus on improved 3D support. In the engine we’ll also continue to work on stability and modularisation. It is also very likely that we will launch support for a new platform fairly soon 🙂
