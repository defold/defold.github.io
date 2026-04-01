---
layout: post
title:  From Unity to Defold: How Orenji Spark rebuilt Jane's Fashion Studio for Poki
excerpt: In this Defold Creator Spotlight we invited Iwan from Orenji Spark to talk about rebuilding Jane's Fashion Studio in Defold and what changed when moving from Unity to a web-first workflow.
author: Paweł Jarosz
tags: ["creator spotlight", "interview", "madewithdefold", "web", "poki"]
---

In this Defold Creator Spotlight we invited Iwan from Orenji Spark to tell us about his journey from a decade of mobile and web development to independent game creation, and about rebuilding *Jane's Fashion Studio* in Defold during its Poki soft-launch.

Orenji Spark is a two-person team, with Iwan handling development and his wife shaping the art and creative direction. Together they have already released several smaller Defold projects such as [Capybara Suika](https://orenjispark.com/play/b7fd521a631c4fe2a9bc97de3b89bb2b/), [Pool Merge Mania](https://orenjispark.com/play/c62767db6c984841a95341d73ff498b5/), and [Tiny Farm](https://gamedistribution.com/games/tiny-farm/), while continuing to grow [Jane's Fashion Studio](https://poki.com/en/g/janes-fashion-studio) for the web.

![Jane's Fashion Studio cover art](/images/posts/creator-spotlight-orenji-spark/Jane%27s%20fashion%20studio%20-%20cover.png)
<div align="center">
_Jane's Fashion Studio_
</div>

##### Hello! Introduce yourself to the Defold community - who is behind Orenji Spark?

Hi! First of all, thank you for the opportunity. I really appreciate being featured in the Creator Spotlight.

I’d also like to thank [Poki](https://poki.com/), not just as a platform, but also the team behind it. Their support and guidance throughout the process have been very helpful.

I’m Iwan, the developer behind Orenji Spark. I’ve been building games and applications for around 10 years now, mostly across mobile and web platforms. More recently, I decided to move into independent development.

Orenji Spark is actually a team of two. My wife is also a big part of it. She handles the art and creative design for our games, so it’s a collaborative effort between us. I focus more on the technical and development side, while she shapes the visual identity and overall feel of the games.

##### You’ve spent a decade building games and applications. How did that experience shape you as a developer, and what pushed you toward independent development?

Over the years, my mindset has shifted quite a lot. Earlier in my career, I tended to focus on building systems that were flexible and feature-rich, sometimes a bit over-engineered.

But with experience, I’ve learned to value simplicity, iteration speed, and clarity much more. Shipping something playable and improving it step by step has become more important than trying to perfect everything upfront.

Moving toward independent development felt like a natural step. I wanted more control over both the creative and technical direction, and also the freedom to experiment with different ideas more quickly.

##### Which game engines have you worked with so far?

I’ve explored quite a few engines over the years, including Cocos Creator, Construct, and Godot.

But the ones I’ve spent the most time with are Unity, Phaser, Cocos Creator, and now Defold. Unity was one of my primary engines for many years.

More recently, I’ve been leaning toward engines that are better suited for lightweight and performant web games, which is what led me to Defold. I’ve also released a few small games using Defold on platforms like Google Play and web portals, such as *Capybara Suika*, *Pool Merge Mania*, and *Tiny Farm*.

![Capybara Suika](/images/posts/creator-spotlight-orenji-spark/ss-2.png)
<div align="center">
_Capybara Suika_
</div>

##### Looking back, how did your priorities change as you shifted more toward web games and performance-sensitive platforms?

The biggest shift was putting performance at the center of decision making.

For web games, things like build size, loading time, and stability across devices have a direct impact on player retention. Even small delays can affect whether a player stays or leaves.

So I started designing with constraints in mind from the beginning, keeping assets lean, simplifying systems, and making sure the game runs well even on lower-end devices.

##### For readers who haven’t played it yet, what is Jane's Fashion Studio, and what kind of player experience were you aiming for with the game?

*Jane's Fashion Studio* is a casual dress-up and styling game where players help different characters by choosing outfits and styling combinations.

Each character also has their own small storyline, so the experience is not just about dressing up, but also progressing through these character moments.

The goal was to create something relaxing, cozy, and accessible, while still giving players a sense of progression and creativity.

![Jane's Fashion Studio gameplay](/images/posts/creator-spotlight-orenji-spark/jfs-2.png)
<div align="center">
_Jane's Fashion Studio gameplay_
</div>

##### You shared on the Defold Forum that Jane's Fashion Studio started in Unity and was later rebuilt in Defold during the Poki soft-launch phase. What feedback or warning signs made you realize that porting the game was the right move?

During the soft-launch phase on Poki, we started to see clear signals that something needed improvement, especially around loading time and performance.

We also received direct feedback from players mentioning that the loading felt too long.

[Poki’s dashboard](https://sdk.poki.com/) was really helpful. It provides very detailed insights, gameplay metrics, engagement, conversion (C2P), device breakdowns, error tracking, and even player feedback.

Seeing all of that together made it much easier to identify where the issues were and how impactful they were. At that point, it became clear that we needed a more optimized approach for the web, which led me to try rebuilding the game in Defold.

##### Which of the improvements mattered most in practice, and how did they affect the game’s path to a global Poki release?

The improvements were quite significant.

The build size was reduced by around 65%, which had a big impact on initial loading time. The game became noticeably faster to start and more responsive overall, especially on lower-end devices.

We could also see the impact reflected in the Poki dashboard. Engagement and C2P started improving.

These changes made the experience more consistent across devices and gave more confidence moving toward a wider, global release.

<div align="center"><p style="font-size: larger"><i>"The build size was reduced by around 65%, which had a big impact on initial loading time."</i></p></div>

##### Which parts of the project were the most straightforward to recreate in Defold, and which parts forced you to rethink your approach from scratch?

The core gameplay logic was relatively straightforward to recreate.

The biggest difference was in data flow and structure. In Unity, I relied a lot on component-based patterns, ScriptableObjects, and prefabs to manage data and mappings.

In Defold, I approached it differently, using atlases and carefully structured naming for mapping. It required a bit of rethinking at first, but it actually made the workflow feel cleaner and lighter, with less overhead.

One feature I really like is GUI Layouts, which makes it much easier to handle different layouts like portrait and landscape without complicating the setup.

I also want to highlight the Defold community here. The extensions and libraries created by the community made the migration process much smoother and very enjoyable. They were genuinely helpful and saved a lot of time.

![Jane's Fashion Studio in the Defold Editor](/images/posts/creator-spotlight-orenji-spark/jfs-1.png)
<div align="center">
_Jane's Fashion Studio in the Defold Editor_
</div>

##### For developers who currently have a 2D game in Unity and are considering Defold for web deployment, what would you tell them based on your own experience?

I’d definitely recommend trying it, especially if your focus is web, performance, or reaching a wide range of devices, including lower-end ones.

It’s not a one-to-one transition from Unity, and you may need to rethink some systems. But that process can actually lead to simpler and more efficient solutions.

##### What kinds of projects do you think are especially well suited to Defold?

I’m still learning Defold myself, but from my experience so far, it works especially well for 2D games that require good performance, particularly on web platforms and across a wide range of devices.

That said, I’ve also seen developers create very impressive and diverse projects with Defold across different genres. It definitely has more flexibility and capability than I initially assumed.

![Tiny Farm in the Defold Editor](/images/posts/creator-spotlight-orenji-spark/tf.png)
<div align="center">
_Tiny Farm in the Defold Editor_
</div>

##### You’ve now released multiple smaller Defold games, including Capybara Suika, Pool Merge Mania, and Tiny Farm, and you also shared work in the community challenge and the Defold showreel. What have these smaller projects taught you?

These smaller projects have been really valuable for learning and experimentation.

They allow me to try different ideas quickly, test workflows, and understand the engine better without the pressure of a large project.

One key takeaway is the importance of keeping scope manageable and focusing on the core experience first. Each project becomes a stepping stone for improving both technical decisions and game design.

##### Your Tiny Worlds challenge entry and your other community posts show that you’re not just using Defold privately, but also engaging with the community. How has being part of the Defold community influenced the way you learn, experiment, or choose what to build next?

The Defold community has been a really positive experience for me.

The forum is especially helpful. I often find solutions there, and what’s interesting is that even posts from years ago are still relevant and still work well today. That consistency makes it much easier to learn and troubleshoot.

Participating in community activities like the Tiny Worlds challenge has also been very meaningful for me. My entry was selected for the Rookie Award, which was a really encouraging experience as someone still exploring Defold.

Being part of the community makes learning more enjoyable. Seeing what others are building and how they approach problems often inspires me to explore new ideas and different approaches.

The community is also very supportive, and the available resources are solid and reliable. Many older tutorials still work today, which reflects how stable and well-structured Defold’s fundamentals are.

![Pool Merge Mania in the Defold Editor](/images/posts/creator-spotlight-orenji-spark/pm.png)
<div align="center">
_Pool Merge Mania in the Defold Editor_
</div>

##### What are you most excited to explore next, either in this project or in future games?

Right now, I’m mainly excited to continue growing *Jane's Fashion Studio*, adding more stories, new characters, and more outfit variations so the experience can keep expanding over time.

At the same time, I also want to keep creating and publishing more games on web platforms using Defold. I really enjoy the process of building smaller projects, learning from each release, and gradually improving both the technical and design side.

I’m also interested in deepening my understanding of Defold itself. Seeing other developers create really impressive projects with it makes me realize there’s still a lot of potential I haven’t explored yet.

![Capybara Suika in the Defold Editor](/images/posts/creator-spotlight-orenji-spark/cs-2.png)
<div align="center">
_Capybara Suika in the Defold Editor_
</div>

##### Finally, how can our community follow you?

If you’re interested, you can find our work and updates here:

- Website: [https://orenjispark.com](https://orenjispark.com)
- Instagram: [https://instagram.com/orenjibrush](https://instagram.com/orenjibrush)
- X (Twitter): [https://x.com/orenjibrush](https://x.com/orenjibrush)
- TikTok: [https://www.tiktok.com/@orenji.brush](https://www.tiktok.com/@orenji.brush)

I’ll be sharing updates about our games and new releases there.

##### Thank you very much for the interview, and we wish you a success with Jane's Fashion Studio and your future Defold games!
