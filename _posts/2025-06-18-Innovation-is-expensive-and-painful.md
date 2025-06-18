---
layout: post
title:  Innovation is expensive and painful. Start with copying a decent bike.
excerpt: Piece of Cake Merge & Bake is one of the most successful games in the Merge 2 genre. Joined by our friends from Playgama, we talked with Rustam Batyrkhanov, founder of HG Point - the great minds behind the game. Read on to learn about failed projects, get free insights on the web dev market and find out who really brings the big bucks to Activision Blizzard.
author: Björn Ritzl
tags: ["creator spotlight", "interview", "Playgama", "HG Point"]
---

# Rustam Bayrkhanov, HG Point: ‘Innovation is expensive and painful. Start with copying a decent bike’

[Piece of Cake: Merge & Bake](https://playgama.com/game/piece-of-cake-merge--bake) is one of the most successful games in the ‘Merge 2’ genre. Joined by our friends from [Playgama](https://playgama.com/), we talked with Rustam Batyrkhanov, founder of HG Point — the great minds behind the game. Read on to learn about failed projects, get free insights on the web dev market and find out who really brings the big bucks to Activision Blizzard.


## How it all began
For me, making games was a long-standing desire, one that appeared right after graduating. HG Point is the third studio we've started — the first two didn’t survive the market test. That, I think, is a typical story for those who start making games. The notion ‘I’m about to materialize my dream project — my very own game with blows and whistles’ is flawed. I only realized this on the third try, before I began analyzing market realities, target audiences, monetization depth across genres, and the purchasing power of different audience segments.

The first project we made is still alive. It’s the multiplayer HaxBall-inspired game, MegaBall, [launched 10 years ago](https://www.youtube.com/watch?v=8kAyVhkfKEA) at the pinnacle of the social media craze, and, thus, very casual. But not all projects were so lucky: at some point, we’d always run out of money/patience/motivation, and the studio would have to be shut down.

The third time, in 2016, we approached things more thoughtfully but focused on the web direction, specifically on the casual puzzle segment. The main reason — even at that point, the mobile market was turning into a red ocean.

That was around the time Fishdom appeared and the metagame became an important part of design. We were probably among the first ones to add this feature to a ‘Match 3’ game. The English-speaking market knows it under the name [Ranch Adventures](https://playgama.com/br/jogo/ranch-adventures-amazing-match-three. It didn’t take off at the start, but eventually, it started to grow organically, and with some luck as well as external help, things got better.

![](/images/posts/playgama/ranchadventure1.jpg)

![](/images/posts/playgama/ranchadventure2.jpg)
Gameplay screenshots from Ranch Adventure


## The right technologies are half the success
We chose the right technology this time. In brief: in previous projects, we went through Unity, Unity Web Player, and the death of Adobe Flash Player. In HG Point's history, we also tried PixiJS and COCOS, but ultimately settled with Defold. Although we wrote the first project in PixiJS, we adapted it for mobile platforms using Unity, which at the time was probably the most popular engine.

As a result, we had to maintain two codebases and allocate an additional tech team. Trying to sit on two chairs of cross-platform gaming turned out to be a massive headache. Even though both projects were developed in-house, we learnt that it's impossible to rewrite a game and keep it exactly the same. It’s like we lost some of the magic along the way. At the very least, each engine generates pseudo-random numbers differently — even that alone can cause the gameplay to misfire.

Given all that, we started looking for a solution that would let us develop a game for multiple platforms using a single engine. Around that time, Unity added support for code compilation for web platforms. Today, this feature is greatly improved, but back in 2016, builds were monstrously large due to Unity artifacts. A blank white screen weighed 60 MB. Utter nonsense.

Looking back, the chances of success weren’t even 30%. Five percent at most, because even back then, ’Match 3’ was a tough niche. Complex genre, complex marketing — everything was complicated. That project is still in the stores but has never found success. Still, we decided not to stop and started exploring other genres. For example, "Five Differences Online" (built in Unity) saw local success in the mobile market. It was even marginally profitable, even though not so much, way less than the ‘Match 3’ game we did in PixiJS.

After two years of working with Unity, it became clear that the technology didn’t suit us, purely on an intuitive level. That said, it has a great ecosystem and legions of developers. The latter, by the way, are Unity’s blessing and curse, because their quantity doesn't always translate into quality and professionalism. We received resumes from 15-year-olds who had simply watched some YouTube tutorials. In my time in the industry, I’ve met very few truly talented Unity developers. That’s when I realized that this is the fact of life for any engine. Whether it’s Unity or Defold, great specialists are worth their weight in gold.

Defold was suggested to me by our CTO. We initially prototyped using Godot, COCOS, and Defold. We simply liked the latter the most. Godot, despite its popularity, just didn’t click. I don’t remember the exact arguments — better to ask our CTO. We didn’t like COCOS because it came with a lot of hard-to-comprehend documentation, sometimes in Chinese. Maybe a lot has changed in five years, but we stuck with Defold on our CTO’s recommendation.

Personally, what I like about Defold is its large, awesome, responsive community. There’s a Telegram chat, and one of the top contributors, Alexey Gulev — a cool dude — is actually a co-founder. You can either donate to Defold for them to implement specific features for your projects or write your own, since the project is open-source. It has a low entry threshold with support for multiple languages, although the initial focus on Lua got mixed reactions from experienced developers, if I remember correctly.

It's disheartening that too few devs see these advantages. I wish that more awesome teams would work with Defold, infrastructure being a concern for later. It boggles my mind that some SDKs lack its support while backing up, say, Godot. From the top of my head, I can name dev2dev and Adjust, but overall, I’m convinced that Defold is better than many other engines out there. Again, I wish that more gaming platforms would support it. And it’s not that Defold is a lesser-known tool — it upholds projects like Family Island, a half-a-million-dollars-a-day game. The engine is flexible, suitable for both local and large-scale projects. The authors recently added support for various languages, including C# and TypeScript, afaik, so it’s also a boon. We’ve been in the business for a while, and our codebase is in Lua. Yet we’re curious about static typing add-ons for the language — it’s time to patch our current projects to smash some bugs.

It's great to see Playgama Bridge embracing the potential of Defold along with various other engines. We’ve complemented their open-source SDK (namely the JavaScript part) with our layer, and it’s been up and running ever since.


## HTML5 market’s perspectives, monetization and quality freakiness
As I’ve mentioned before, we are a mature studio, and it helps to connect faster with renowned platforms such as MSN and Crazy Games. Most of these resources are managed by our biz dev team. Yet when it comes to approaching hidden gem platforms — Y8, Lagged, etc. — our friends from Playgama are of great help. I want all our games to be presented on as many platforms as possible. By the way, I’m a great believer in their platform, we hope to grow not only through them but rather with them.

Overall, there is some moderate optimism regarding HTML5 games in our studio. We’re in this niche already, connected and networked, hoping for this segment to grow year by year. So far, it’s puny in comparison to mobile, so we’re looking forward to it reaching 10% of its size.
The larger the market, the more users will come, the higher the competition, the better games we’ll see. Not to pat ourselves on the back too much, but in our studio, quality has always been an obsession. I believe it to be one of the key factors for a game. So, we try to bring out the best that we have. I once asked our team to ship faster at the expense of quality, and we just couldn’t. Again, a blessing and a curse.

Iteration makes perfect. Piece of Cake: Merge & Bake is our latest flagship project, but before that, there was a ‘Merge 2 male-oriented game — Merge Hotel. It didn’t do so well due to the piling up of small mistakes (mainly targeting the wrong audience), but it was a milestone of sorts, since we were the first ones to introduce the genre on the web.

![](/images/posts/playgama/pieceofcake1.jpg)

![](/images/posts/playgama/pieceofcake2.jpg)
Gameplay screenshots from Piece of Cake: Merge & Bake

The Merge Hotel’s legacy let us build Piece of Cake: Merge & Bake. To be honest, I did not expect it to be such a success. So yeah, we’re mostly focused on Piece of Cake: Merge & Bake — there are so many things we can do with it! Just as most of the casual games, we’re monetizing via in-apps. It’s a crucial part of business — I’m talking 60-70-80% of revenue. Platforms are catching up to this idea, since it’s good for retention.

Getting back to Ranch Adventures, some of its players have been in the game for six years. Some of the players have spent thousands of dollars. One of the top players has spent $38,000 over a few years. What drives them is beyond me, but here we are. I choose to believe that the game is THAT good, and some senior citizens in Colorado spend half an hour with our project every day as a ritual. We don’t compare ourselves to AAA PC titles, but we’re more complex than crosswords or 2048s. The gameplay is deeper, the content is far more diverse, and it entails deeper engagement with the game, bordering on loyalty.

Overall context of the gaming industry backs up casual games dominance. Activision Blizzard’s subsidiary, King.com (developers of Candy Crush Saga — author’s note), is the most profitable within the conglomerate, according to the holding’s financial reports. Even though gameplay-wise their game is not as sophisticated as, say, Overwatch 2, King.com sticks it to the holding company in terms of revenue. A ‘match 3’ wipes the floor with Call of Duty. How cool is that?

Circling back: I see great potential in puzzles on the web; the demand will not only stay the same but grow. The market is ample enough for both ‘Match 3’ and ‘Call of Duty’ players.


## The hardest parts of game development and hints for those who dare
Every studio is going to face issues at every stage of development. In my experience, the most common are:

- For startups — to find a talented art director, a gifted developer and a manager/producer/game designer. The latter is usually a founder. The cost of a mistake at this stage is astronomical — I saw many studios that were built on a shaky foundation, and it would inevitably come up later. One may pick the wrong direction and burn through thousands of dollars for quite a while, all for naught. Thankfully, it took me only three times to find the right comp. Of course, there are one-man studios, such as Potion Craft, but it’s a very rare case. There’s only one Minecraft and only one Terrarium.
- When the studio gets on its feet, the hardest part is to define the project that it’s going to work on. Will there be any demand for it? Is there a market fit? One could build a space-themed game for the web, but it’d have an audience of three people.

- In the later stages, it might be a task in itself to analyze metrics. If it’s all zeros or all in green — good, the project has failed or succeeded fast. But what is there to do when one gets mixed signals? Playtime is gorgeous, but with almost no paying users — is it a good or a bad thing? First day retention is high, yet by the end of the week, everybody’s gone — why?! And if you think that building a hypothesis is hard, wait until you get into testing scenarios. Is there any sense in proceeding at all if nothing works? This issue is relevant for all the platforms and markets. We encountered it with Merge Hotel, and that experience influenced Piece of Cake: Merge & Bake heavily. 

I’d recommend thinking deeply about the project idea. It’s easy to fall into the trap of a ‘dream game’ (been there!), so it’s crucial to evaluate the demand on mobile and work your way from there. Make a good clone of a good mobile game that is not on the web. Innovation is expensive and painful. Start with copying a decent bike.

When it comes to distribution, there’s no such thing as too many platforms. Their number is growing, and the volume of the audience follows. Some games perform better on specific platforms, and this way, you might get more traffic and engagement for your projects. I would hedge bets across every single one.

![](/images/posts/playgama/rustambatyrkhanov.jpg)
Rustam Batyrkhanov — COO at HG Point

Luck is a large part of this business, even if no one talks about it. Nothing is guaranteed, and there are no silver bullets. Among 20 well-to-do studios, some might say that they knew what they were doing all along. They would lie, or rather, they would rely on 20/20 hindsight. Two principles that will likely prop up the success rate: reflection and analysis after every attempt, and the constant testing of ideas. The more of them you disprove, the sooner you find the one that works. Once again, it’s better to fail in a month rather than in a year and a half. These worked for me.


## What’s next
It would be foolish to abandon the genre that brought us success, so we’ll focus on creating the best ‘Merge 2’ web game out there. And I feel that we’re pretty close — the market of high-quality projects is undersaturated. The next steps are improving what we have already built while introducing new features to please the users and market — stay tuned!

I have some extra free time, and R&D has always been one of my core interests. I play many jaw-dropping mobile games and wonder: ‘Why aren’t they on the web?’. My idea is that the demand can flow between the two platforms, so we conduct experiments. I’m shocked that there is only one web version of Hero Wars — just one game (namely, BattleArena) for the whole genre! To me, it looks like an uncharted territory of users, money and glory.

At the same time, we’re witnessing a renaissance of mobile puzzles — hybrid approaches that, for some reason, are not relayed to the web. Everything is the same, and I attribute it to devs' mental inertia. One sees the top of the game platform and goes, ‘I’ll do exactly the same!’. Someone is reading this thinking, “This guy’s onto something. I should launch a ‘Merge 2’ project!”. This is a mistake. Every new player shrinks the market. Find something that’s missing. I wonder why no one has made a ‘Capybara Go!’ web clone yet! The possibilities are limitless — casual puzzles for the win!

Even if the web versions fail, there is still a mobile audience that is already conditioned to these types of games. I want to storm this market as well, and it is the core idea of our studio, all the way down to the tech stack. While we have extra resources, we’re going to take risks.
