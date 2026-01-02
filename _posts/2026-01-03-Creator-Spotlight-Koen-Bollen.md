---
layout: post
title:  Creator Spotlight - Koen Bollen
excerpt: In this Defold Creator Spotlight we invited Koen Bollen to tell us a little bit about himself and his latest Defold project - Sprint City.
author: Paweł Jarosz
tags: ["creator spotlight", "interview", "madewithdefold", "steam"]
---

In the Creator Spotlight posts we invite Defold users to present themselves and share a bit of their background, their work and things that inspire them. It is an excellent opportunity for the community to come together, to recognise achievements and to share some of the great work done by Defold users.

In this Defold Creator Spotlight we invited Koen Bollen to tell us a little bit about himself and his latest Defold project - Sprint City - a competitive platformer from the original creators of SpeedRunners now being developed with Defold!

![Sprint City Made with Defold](/images/posts/developer-spotlight-koen-bollen/header.png)

##### Hello Koen! Introduce yourself to our community!

Hello! My name is Koen Bollen, or *Kaji* in-game. I’m the co-founder and lead engineer of the Second Stage Studio.

##### What is your favorite game of all time?

My favorite games, with a healthy amount of recency-bias are *Half-Life: Alyx*, *Minecraft* and *Hollow Knight: Silksong*.

##### We know you’ve had an interesting journey. Tell us a bit about your experience prior to forming Second Stage Studio. What is your background in game development?

Where to start? Well, I started tinkering with computers at the age of 11, breaking my parents’ computer often enough to get my own. I started making games at around age 21 whilst teaching gamedev and computer science. Later I did a lot of backend engineering, most notably at [Poki](https://poki.com/) (a web games platform) and I’ve been making Sprint City for about two years now.

##### What is Sprint City about? What can players expect from the game and its core gameplay?

The core of our game is movement and momentum, “got to go fast!”. When you race against others, you try to drain their clocks by finishing a lap first and clock them out! Or you time trial alone and set the world record on every track.

![Sprint City Climbing](/images/posts/developer-spotlight-koen-bollen/sprint_city_climbing.gif)

##### What are you working on in the project?

I’m responsible for all things tech-heavy: The backend, hosting, net-code. But also shaders, the render pipeline and designing more complicated game systems.

##### With an official SpeedRunners 2 in development by another studio, what led your team to create Sprint City independently as a spiritual successor?

Casper van Est (the creator of Speedrunners) and I decided to do a week-long gamejam (just us, not a public event). The result of that was so much fun, and it inspired Casper to maybe make a new game or even a sequel. So we started a new studio and worked on our game, codenamed Playground.

In parallel, tinyBuild, who owns Speedrunners, got a proposal for Speedrunners 2 and went ahead with this.
Because of this mismatch we decided to pivot into a new IP, Sprint City!

##### SpeedRunners became a cult hit in the competitive platformer genre. What lessons from that game are you carrying over into Sprint City, and in what ways are you pushing the concept further or in a new direction?

The main thing we want to carry over is the feel of movement; you need to be flying through the city. Just traversal on its own should be fun, other gameplay is just extra.

Something we wanted to improve on is waiting in menus to start playing the game (while waiting for matchmaking for example), so in Sprint City you are always gaming! At the end of a race, you just stay in the game and can hang around with friends and show off your moves.

![Sprint City Grapling Hooks](/images/posts/developer-spotlight-koen-bollen/sprint_city_hooks.gif)
 
##### We’re curious about the story behind the studio’s name. Does Second Stage Studio have a special meaning?

Ha. Not a lot of thought went into this. This is the second game studio for both Casper and me, and we like space and rockets. “Second Stage Studio? As in the second stage of a rocket? Sounds good!”

##### Sprint City is planned for Early Access on Steam in 2026. Do you have additional launch plans or platforms in mind?

We are focusing on Steam during development and early access. This platform is the easiest to update on frequently.
When the game is fully released we plan to launch on the major consoles as well.

##### The game will let players invite friends via a web browser to play for free – a very unique feature! How does that system work, and what was the motivation behind it?

A couple of things came together for this idea. We wanted to support cross-play between platforms. I had a lot of experience with WebRTC (the browser network technology that Discord and Zoom use). And Defold has excellent support for the web.

And we feel it’s super fair if you can have your friends play without having to convince them to buy and download/install it first.

![Sprint City Sliding](/images/posts/developer-spotlight-koen-bollen/sprint_city.gif)

##### What have been the biggest technical challenges in developing Sprint City, and how did you overcome them? Every developer sometimes has a funny horror story. Did you have to resort to any “ugly” hacks or quick-and-dirty tricks during Sprint City’s development to make something work in a pinch?

Three categories:
1. The most work: The networking code. We created a custom extension that allows for WebRTC P2P communication. And a backend that dynamically has players connect to each other when they are in proximity in the game world.
2. The hardest to get to work: The shader based parallaxing and Defold’s frustum culling. We do parallaxing using a vertex shader, since we have too big of a world to do it based on the game-object position. But far away objects got culled by the rendering frustum. We, and mostly our intern Leo, designed a way to make a perspective projection matrix that would include all objects in rendering, even though the game objects are technically far offscreen
3. The hackiest: Our in-game shadows use a very hacky rendering trick to insert them in a postshader phase. I already have a better system cooked up, but who has time to improve on an already working system?

##### Sprint City’s art style and animation are striking – the game is set in a seemingly vibrant solarpunk city with cool and funky character animations. Can you tell us about your art pipeline and tools?

Our artists and animator just work in our Git repository, they use Defold to add images to atlases and use our in-game level editor to place decals and other visuals like shadows. Then they make a pull-request(PR) and one of the coders checks their work before we merge it. We also have a bunch of automated checks (like naming conventions on animation names and no capital letters in filename).

Super useful feature: We use a github Action to automatically build a PR and host that somewhere, so we can play that version without having to pull it and build it locally.

![Sprint City Solarpunk](/images/posts/developer-spotlight-koen-bollen/sprint_city.png)

##### Being based in the Netherlands, how do you find the local game development scene?

The indie scene here is very nice and active, there are plenty of meetups and other get-togethers. We sometimes have people over to work from our office for a day. Sadly, there are not many AAA studios in the Netherlands.

##### When and how did you first discover Defold, and why did you choose Defold as the engine for Sprint City? What made Defold stand out for this project?

I learned about Defold in my time at Poki. And I have a soft spot for web games. Defold is very light weight, 2D friendly and very flexible in extending. Making an extension was very important for our network stack, using (crossplatform) WebRTC was not possible in other engines (at least not super easy). Then having a build-server was a big plus for the rest of the team.

![Sprint City Defold GUI](/images/posts/developer-spotlight-koen-bollen/sprint_city_gui.png)

##### What do you like the most about working with Defold? Are there particular features, workflows or aspects of Defold that you and your team appreciate during development?

Mostly ease of use, and fast build speed. You just need to install Defold and you can build our project, even though we use a lot of custom extensions and C++ code.
We don’t use the Defold editor a lot - we code in VSCode and only use the Defold editor for atlases, particles and GUIs, and we use it to build the game during development of course.

![Sprint City Defold Editor](/images/posts/developer-spotlight-koen-bollen/sprint_city_defold_editor.png)

##### What would be your recommendations for Defold developers?

- Add [Lua type annotations](https://luals.github.io/wiki/annotations/) to everything, from the start! Lua is a great language for hacking, not so great for larger engineering projects.. Adding annotation later on in the project is just not going to happen. Having types (and a system that checks them) will prevent a lot of bugs from being introduced, and helps auto-complete while developing.
- I also recommend setting up a repository wide formatter like [StyLua](https://github.com/JohnnyMorganz/StyLua) to never have to think about it again (and enforce it with a Github Action).
- Have dynamic loading from the start, or very early on. We added dynamic loading (having the game in a Collection Proxy) later on in the process and it was very hard to get it to work and have the communication working in our game. Later we also added large open world loading (where regions load/unload as you run around) and that would have been 100x easier, if created from the start.
- Your game will be played in different aspect-ratios, make sure you support that from the beginning.
- Protip: Use [defos](https://github.com/subsoap/defos) to randomize the window size every time you run your game in debug while developing.

##### Finally, how can the community follow your progress and get their hands on Sprint City?

Wishlist the game on Steam: [https://store.steampowered.com/app/4191250/Sprint_City](https://store.steampowered.com/app/4191250/Sprint_City)

Join us on Discord:
[https://discord.com/invite/sprintcity](
https://discord.com/invite/sprintcity)

##### Thank you very much for the interview, and we wish you a tremendous success with Sprint City!

###### Official Sprint City announcement trailer:

[https://www.youtube.com/watch?v=2M4SkQLFRGM](https://www.youtube.com/watch?v=2M4SkQLFRGM)
