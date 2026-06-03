---
layout: post
title: Building Mad Skills Motocross 2 for Poki with Defold
excerpt: In this Creator Spotlight interview, the Refold Games team explains how they rebuilt Mad Skills Motocross 2 for Poki with Defold, from the native physics engine and runtime meshes to the backend wrappers and Live Update strategy that improved loading time.
author: Defold Foundation
tags: ["spotlight", "interview", "web", "poki", "html5", "mobile"]
---

In this Creator Spotlight interview, we invited Björn, Eugene, Sergey and Paweł from [Refold Games](https://www.refold.io/) to talk about what it actually took to bring [Mad Skills Motocross 2](https://poki.com/en/g/mad-skills-motocross-2) to Poki with [Defold](https://defold.com/).

![Mad Skills Motocross 2 mesh components](/images/games/madskillsmotocross2-half.webp)
<div align="center">
_Mad Skills Motocross 2 was created for Poki with Defold_
</div>

#### Tell us a little bit about what Mad Skills Motocross 2 is.

**Paweł:** [Mad Skills Motocross 2](https://www.turborilla.com/mad-skills-motocross-2) is a super fun, fast, side-scrolling motocross racing game built around short competitive sessions, tight realistic physics, and skill-based bike control. It was originally created for mobile phones in Unity by *Mad Skills* series creators [Turborilla](https://www.turborilla.com/).

The core appeal is easy to understand but hard to master. You race across bumpy dirt tracks, manage jumps, landings, acceleration, and momentum, and try to beat rivals, friends, or leaderboard times. It is part arcade racer, part physics challenge, and it has a very loyal audience among players who like motocross games and especially the whole Mad Skills franchise.

The web version brought the series to Poki's audience with daily competitive modes and a rebuilt from scratch in the Defold engine experience by Refold Games, a game studio of the founders of the Defold Foundation.

![Mad Skills Motocross 2 gameplay](/images/posts/msm2/gameplay.webp)
<div align="center">
_Mad Skills Motocross 2 can be played now for free on Poki_
</div>

#### Why did Turborilla specifically choose Defold for this port?

**Björn:** Turborilla and Poki had been discussing for quite some time various alternatives to bring *Mad Skills Motocross* and other games from Turborilla to the web. One option was to strip down a Unity version of the game and make a WebGL export, but it would be a challenge to get it down to a small enough size to make it load fast.

Performance was another concern. If you start from scratch with Unity and build the game with the web in mind you can get something that works decently well, but the size will still be an issue. 

Thanks to the Defold and Poki partnership it was decided to use Defold and to make a port from scratch, rather than trying to adapt the existing Unity version.

#### So this was not only a simple port, but rebuilding the game from scratch in Defold suited specifically for the web games market. How did you manage to do so? What changed in the architecture? And how did you preserve the original game's feel?

**Eugene:** Since we had an original mobile project as a reference, we could reuse many useful modules from there. Separate classes from Unity could be easily represented as Lua modules, which made the structure easier to understand and easier to maintain.

For the web version the main motto was: *simplify*. The original game has more modes and more functionality. For the web release, we wanted a concentrated experience.

On the other hand we’ve added several features aimed to satisfy the (not so hardcore) Poki audience. Namely, it’s landing and flip assistance. These systems help players to perform tricks like backflips and frontflips and have fun, while still being able to land smoothly.

**Paweł:** I joined the project at the very end, but I was happy to see the same architecture approach I was using previously all the time - that separates view (audiovisual representation of the game) from logic (everything related to movement, controls, AI behaviour and other code-only related things) that is simply a result of years making games and coming to the same conclusions each time. And of course we were suiting everything to how Defold operates to make it most optimal.

Also, making GUI was super easy and efficient, as we utilised the powerful [Druid Framework by Insality](https://defold.com/assets/druid/).

![Mad Skills Motocross 2 leaderboards](/images/posts/msm2/leaderboards_gui.webp)
<div align="center">
_Mad Skills Motocross 2 Leaderboards GUI in Defold Editor_
</div>

#### What should developers be aware of when porting a game to web? What is the hardest part?   

**Sergey:** When porting a game to the web, there are several important factors to consider. Players may use low-performance devices or slow internet connections, and both affect whether they will stay. That means you have to optimize gameplay systems and reduce the overall build size as much as possible.

I would not say there was one single hardest part. The real challenge was choosing the right approach for each system and knowing how to solve performance and optimization problems efficiently.

##### Mad Skills Motocross 2 uses Turborilla's own great custom physics engine. How does it work and how did you port it as a native extension in Defold?

**Björn:** We were fortunate that the custom physics engine in MSM2 was implemented as a clean, isolated C++ library with a small API surface. That made it much easier to extract the physics engine into a standalone [native extension](https://defold.com/manuals/extensions/) and expose it through Lua bindings.

The physics engine defines track geometry as a list of height data. The bikes are defined as a bike frame, wheels and rider, each with their own physics control points, weights, spring coefficients and other constraints. Both track data and bike data were read from a binary format and passed to the physics engine through the Lua API before the simulation started.

The player controls the bike by pressing throttle or brake and by leaning forward or backward with the rider.

At every update, the simulation advances with a fixed delta time and receives the current throttle, brake and lean inputs. After the update, we fetch the new state through Lua and position and rotate the individual bike and rider pieces according to the physics result.

<div align="center"><p style="font-size: larger"><i>"We had an initial version of the physics engine up and running in Defold in a matter of days."</i></p></div>

After that, iit took some additional time to match the bike and rider positions from the physics engine with the Defold game objects and to generate the meshes for the track from the track geometry, but thanks to Eugene’s efforts this was also achieved with great results!

##### And for the visual part, you rebuilt the biker and tracks as dynamic meshes. Why did you choose meshes over sprites or prebaked animation?

**Eugene:** For the track ground, we dynamically create the track surface using [mesh components](https://defold.com/manuals/mesh/) based on a one-dimensional array of track heights. Then we attach a repeated ground image, with different variants for different environments.

![Mad Skills Motocross 2 mesh components](/images/posts/msm2/msm2_track.webp)
<div align="center">
_On the left, a simple line representation of the 1D track height array, on right with an aligned mesh for the track_
</div>

We also add shadows below the rider with another mesh curved according to the track height. On top of that, there are several more meshes for foreground and background grass, rocks, and the black area below the track. The result looks and feels pleasant without requiring a large amount of prebaked art.

At first we tried an orthographic camera, but it did not feel right and result didn't satisfy us. The image looked too flat and lacked depth, so we moved to a perspective camera instead.

<div align="center"><p style="font-size: larger"><i>"As the game has pretty long tracks with long meshes, we were concerned a bit that this might affect performance, and had a few possible optimizations on our mind already, BUT in practice, Defold handled it extremely well, and meshes don’t influence game performance at all."</i></p></div>

Meshes did not become a bottleneck, and that gave us the freedom to build the scene the way the game actually needed it.

I also want to mention [RenderDoc](https://renderdoc.org/). It helped a lot when debugging graphics and render-related issues.

**Paweł:** And later on Eugene was invited to the Made with Defold Jam 2025 as a speaker and presemted a great lecture about [Meshes in Defold that you can now watch online here](https://www.youtube.com/watch?v=mveAyod93cA), and trust me, it's worth watching, if you would like to do anything with meshes. Check out also the [open source online examples](https://github.com/mozok/Meshes-In-Defold)!

**Sergey:** For the bike and rider, we also used a mesh. Initially we used regular sprites, but with a perspective camera the wheels and other elements started to flicker as the rotation angles and positions changed. Unfortunately, adjusting the Z positions pushed sprites noticeably farther away in a way that did not feel right.

In the end, we decided to render the entire bike and rider as a single mesh while keeping the center of each element in the same place. One of the trickier parts was that the wheels still needed to rotate relative to the bike, so we had to recalculate vertex positions manually.

![Mad Skills Motocross 2 development with Defold](/images/posts/msm2/msm2_track_grass.webp)
<div align="center">
_Foreground and background elements are meshes too_
</div>

##### The game also introduces daily challenges and leaderboards. How did you integrate the custom server functionality?

**Paweł:** Turborilla had already done a very good job describing the API, and the client-side documentation was clear. We only needed to integrate it into the game. In Defold we could control the method, headers and body directly from Lua.

**Sergey:** For request handling, we used [`ludobits.m.flow`](https://github.com/britzl/ludobits) based on coroutines wrapping the HTTP requests in a small backend transaction module with retries, error handling and coroutine support.

**Paweł:** Precisely, so the rest of the game could treat server calls like normal sequential logic. Daily Dash is a good example. The game downloads the current season data from Turborilla's content server. Those requests are started in parallel where possible, and the results are cached in local save data. The gameplay code does not need to know much about networking - it just asks for today's challenge or today's opponents, and the backend layer handles the rest.

Leaderboards use the same pattern. Scores are sent to Turborilla's server, and we only upload when the player improves their previous local best. Fetching ranks and leaderboard pages is handled by the same Lua wrapper, including pagination for the UI.

There was also one small trick around player names. The leaderboard service needed each user to have a valid, unique username matching a specific regular expression, but for the Poki web version we did not want to interrupt the player with account creation or a name-entry flow. So we generated a compact server-safe guest name automatically. If the server rejected it, we simply generated a new one and retried. In the UI, we decoded that internal name back into something more readable. From the player's perspective it looked like a normal leaderboard name, but technically it satisfied Turborilla's backend requirements without adding friction.

That is a good example of why Defold worked so well here: the whole solution stayed as a thin Lua layer around Defold's built-in HTTP API. Notice also, that on the screenshots from the development we have a huge button in the bottom right corner with letter "D" - which was a "Debug" button simply used to open a popup with different settings and cheats for faster testing.

![Mad Skills Motocross 2 leaderboards](/images/posts/msm2/leaderboards.webp)
<div align="center">
_Leaderboards with randomly generated names_
</div>

##### What did you have to do to make the game load fast enough and still preserve quality?

**Sergey:** To achieve faster loading times, we had to reduce the build size. For that, we used Defold's [Live Update](https://defold.com/manuals/live-update/) feature - a very convenient technology that allows separate collections to be downloaded after the main build has loaded.

The game contains many different skins and backgrounds, so we split them into separate collections and loaded through Live Update mounts and proxies at runtime instead of stuffing everything into the first download. In practice, that meant we could keep the initial package small and stream in content when needed and it made a real difference.

**Paweł:** This is one of the clearest Defold advantages for web games.

<div align="center"><p style="font-size: larger"><i>"You can build a focused initial payload, then bring in the rest of the content when the player actually needs it, in the background. That is pretty much how the web should work."</i></p></div>

**Sergey:** We also used compression through [texture profiles](https://defold.com/manuals/texture-profiles/) for images and [TexturePacker extension for Defold](https://defold.com/extension-texturepacker/) to save space. [TexturePacker](https://www.codeandweb.com/texturepacker) was especially helpful because it accounts for transparent and empty pixels, which meant less wasted texture memory and a smaller bundle.

![Mad Skills Motocross 2 gameplay](/images/posts/msm2/haunted_race.webp)
<div align="center">
_Mad Skills Motocross 2 Haunted Race_
</div>

##### What do you think Defold brought to this project that would have been harder in another engine?

**Paweł:** The short answer is: a lot less friction. Defold give us a small, web-friendly base, a powerful path for low-level code functionalities through native extensions, and runtime meshes that were great for the whole visual approach. That combination made it realistic to rebuild the game for the web from scratch without dragging a lot of mobile baggage along with it. And iteration speed while developing games in Defold is incredible. It also helped that the project stayed readable. We were not dealing with huge callback chains or a lot of platform-specific glue. The code stayed modular, and the important systems remained easy to reason about.

**Eugene:** Defold is small, fast and efficient.

<div align="center"><p style="font-size: larger"><i>"Engine functionality works great, and if something is slow - it's a question to my own implementation."</i></p></div>

##### Looking back, what is the main lesson from this project?

**Eugene:** As we already ported many projects, rebuilding some from scratch, one important thing is that porting project is much easier if you have access to original code! And one more: Mesh component is a great tool, one just need to figure it out.

**Paweł:** It was very scary for me to add any online features like leaderboards, online features, stuff like this, but when you face it, it's not so difficult. Maybe because we already had a nicely working server infrastructure, because now only this part sounds scary to me, but there are a lot of solutions, also for Defold, that simplifies it a lot. Client side implementation is usually very simple and straightforward.

##### Thank you very much for the interview, and we wish Refold and Turborilla continued success with Mad Skills Motocross 2 on Poki!

Check the game online for free: [Mad Skills Motocross 2 on Poki](https://poki.com/en/g/mad-skills-motocross-2)