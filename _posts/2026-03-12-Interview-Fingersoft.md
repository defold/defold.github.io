---
layout: post
title:  Why did Fingersoft use Defold to bring Hill Climb Racing to Poki?
excerpt: We invited Shiho Kaneko from Fingersoft, to tell us about their adventure with Defold to create Hill Climb Racing Lite for Poki.
author: Paweł Jarosz
tags: ["creator spotlight", "interview", "madewithdefold", "steam"]
---

We invited Shiho Kaneko from Fingersoft, to tell us about their adventure with Defold to create [Hill Climb Racing Lite](https://poki.com/pl/g/hill-climb-racing-lite) for [Poki](https://poki.com/).

![Hill Climb Racing Lite made with Defold](/images/posts/interview-fingersoft/hill_climb_racing_lite_banner.png)
<div align="center">
_Hill Climb Racing Lite made with Defold_
</div>

#### Hello Shiho! Introduce yourself to our community! What is your role at Fingersoft? What are your favorite games?

Hi, I’m Shiho Kaneko, producer of Hill Climb Racing Lite. I love games like *Rhythm Heaven*, *Gorogoa*, and *Don’t Starve Together*.

#### For readers who know Fingersoft, but not Hill Climb Racing Lite on the web, what kind of game is it, and what were your goals for making a web version?

Hill Climb Racing Lite on the web is based on the original [Hill Climb Racing](https://play.google.com/store/apps/details?id=com.fingersoft.hillclimb), but it’s not just the classic endless driving mode. We kept the infinite mode that players already know, but we also added a new mode called **World Tour**. This mode has a more linear progression and focuses more on skill-based challenge levels. In the World Tour, there are no unlocks or upgrades. Players can jump in and use powerful vehicles right away, without needing to grind first. The idea was to let players focus purely on mastering their skills. 

Hill Climb Racing has always had a lot of hidden mechanics and depth that not all players notice at first. With the web version, one of our goals was to make those mechanics more visible. At the same time, we wanted to create something that feels **fresh for modern web players, while still keeping the core feeling** of the original game.

#### Preserving the classic feel of the mobile game is definitely noticeable when playing Hill Climb Racing Lite, yet what had to change for modern browsers and audiences?

During the soft launch, we learned or at least formed a hypothesis that our original format might not be the best fit for modern browser audiences. We noticed that **browser players tend to prefer short-term goals** rather than long-term commitments, and they expect more frequent changes in gameplay.

<div align="center"><p style="font-size: larger"><i>"Based on this, we designed the World Tour mode around three key ideas: a clear sense of progression, minimal decision-making friction, and strong variety."</i></p></div>

In addition to offering different vehicles and levels, this mode shifts the focus from simply driving as far as possible. Instead, players are given different objectives and win conditions, encouraging skill-based play and alternative play styles.

![Hill Climb Racing Lite World Tour](/images/posts/interview-fingersoft/hill_climb_racing_lite_map.png)
<div align="center">
_Hill Climb Racing Lite - World Tour_
</div>

#### Why web and why now? What did you see in the web games market that made this release a reality?

The Hill Climb Racing franchise is evergreen on mobile, and the original is one of the incumbents of the free-to-play mobile gaming era. We realized that web gaming, after the decline of Flash, was making a comeback and we wanted to offer an **authentic Hill Climb Racing experience** for the players who’d rather play short, instant sessions on web platforms like Poki.

#### Why did you choose Defold for porting the game to the web?

We **evaluated several different engines before selecting Defold** — in fact, it was the last one we tested. Previously, we had released a predecessor of Hill Climb Racing Lite on YouTube (YouTube Playables), so we were already familiar with platform-agnostic technical requirements.

There were a few key constraints. The game had to run in HTML5, the **engine size needed to be very small, and solid Box2D integration was essential** for our physics-based gameplay. Another important requirement was support for portrait orientation, as the game needed to be fully playable in that format.

We shortlisted around five HTML5-capable engines and built prototypes with each of them. Many had significant limitations when it came to Box2D support. While Defold does not offer built-in Box2D integration at the same level as some native engines, we discovered that someone had implemented a full Box2D conversion using Defold’s native extensions. This made it viable for our needs.
Additionally, **Defold’s visual editor was a major advantage.**

The original Hill Climb Racing still doesn’t use visual tools, so having a proper visual UI editor, especially for portrait layout, significantly improved our workflow.

<div align="center"><p style="font-size: larger"><i>"Considering all these factors, Defold turned out to be the best fit for our technical and production requirements."</i></p></div>

![Hill Climb Racing Lite in the Defold Editor](/images/posts/interview-fingersoft/hill_climb_racing_lite_defold.png)
<div align="center">
_Hill Climb Racing Lite in the Defold Editor_
</div>

#### That's awesome to hear! How did Defold feel in production at your scale? What did the day-to-day workflow look like?

Our production team is small and agile, typically consisting of one to three programmers. In that setup, **Defold worked well for collaboration**, especially since all project files are stored as text. This made version control and merging much smoother compared to engines that rely heavily on binary files.

That said, the beginning was quite frustrating. Initially, we tried to use Defold the same way we had used other engines like Unity or Godot. Over time, we realized that this approach didn’t work well. Defold is fundamentally different in its architecture, and once we accepted that and started using it as intended, things improved significantly.

One of the biggest mindset shifts was adapting to Defold’s strong emphasis on decoupling through its message-passing system between objects. Instead of tightly connected components, communication happens via explicit messages, which **encourages a more modular structure**. After adjusting to this paradigm, the workflow became more predictable and efficient for our small team.

#### What challenges have you faced during the development of Hill Climb Racing Lite, if any, and how did you overcome them?

One of the day-to-day challenges was actually the built-in Defold code editor — particularly the undo functionality, which didn’t feel up to modern standards. This sparked multiple heated internal debates :)

In the end, we handled it in two different ways: one of us accepted the situation and adapted, while the others “escaped” to Visual Studio Code. Moving to VS Code significantly improved the development experience and solved most of the frustration.

#### Good that we have options then! By the way this undo functionality change is our priority in the Defold roadmap now - we hope it will be satisfying then. And how was the release workflow?

We found the [Poki Playtesting](https://sdk.poki.com/playtesting.html) feature very helpful. It helped us to identify potential UX related issues.

![Hill Climb Racing Lite made with Defold](/images/posts/interview-fingersoft/hill_climb_racing_lite_title.png)
<div align="center">
_Hill Climb Racing Lite - main menu_
</div>

#### What did you learn about a “web-first” game design during this project? Was there anything particularly surprising?

On mobile, it’s relatively safe to design for multi-day progression and deeper meta systems, since players have already committed by downloading the game. You can rely on longer retention loops and layered progression.On the web, however, player behavior is very different. Users tend to look for quick gratification and immediate fun. Sessions are shorter, and the commitment level is much lower.

As a result, deep multi-layered meta systems don’t work as well — players are less willing to invest time before the game becomes rewarding. What surprised us most was how quickly web players decide whether to stay or leave.

<div align="center"><p style="font-size: larger"><i>"A “web-first” design needs to deliver value almost instantly, rather than building up slowly over time."</i></p></div>

This forced us to rethink onboarding, pacing, and reward timing.

##### What would be your recommendation for developers new to Defold?

**Just try it yourself, it’s free!** Give it at least a week before forming an opinion. Defold has a different architecture and mindset compared to engines like Unity or Godot, and it can feel unfamiliar at first.

![Hill Climb Racing Lite made with Defold](/images/posts/interview-fingersoft/hill_climb_racing_lite_moon.png)
<div align="center">
_Hill Climb Racing Lite - to the moon!_
</div>
 
##### Can you share with us what’s next with Hill Climb Racing and/or Fingersoft?

Our company’s main focus is still on supporting the growth of Hill Climb Racing and Hill Climb Racing 2, but in addition we’re developing and iterating on the next title of the franchise, Hill Climb Racing 3. That being said, we are keeping a keen eye on what platforms and distribution opportunities emerge, and aim to provide supply wherever there is demand for Hill Climb Racing.

##### Thank you very much for the interview, and we wish you a tremendous success with Hill Climb Racing Lite!

Check out the game on Poki:

[Hill Climb Racing Lite](https://poki.com/pl/g/hill-climb-racing-lite)

Follow Fingersoft on social media:

- [Facebook](https://facebook.com/fingersoft)
- [X](https://x.com/fingersoft)
- [LinkedIn](https://www.linkedin.com/company/3127905)
- [Instagram](https://www.instagram.com/fingersoft_official/)
- [YouTube](http://www.youtube.com/c/FingersoftLtd)

Join Hill Climb Racing Discord:

- [Discord](http://www.discord.gg/hillclimbracing)

And subreddit:

- [Reddit](https://www.reddit.com/r/HillClimbRacing/)

And follow Hill Climb Racing accounts:

- [Facebook](https://www.facebook.com/HillClimbRacing)
- [X](https://x.com/HCR_Official_)
- [Instagram](https://www.instagram.com/hillclimbracing_official/)
- [TikTok](https://www.tiktok.com/@hillclimbracing_game )


