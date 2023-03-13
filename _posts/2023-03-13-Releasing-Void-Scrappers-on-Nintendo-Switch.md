---
layout: post
title:  Releasing Void Scrappers on Nintendo Switch
excerpt: Void Scrappers was recently released for Nintendo Switch. What where the challenges and what can you do to make your own porting experience smoother?
author: Björn Ritzl
tags: ["creator spotlight", "interview", "nintendo switch"]
---

__It's been a few months since the release of [Void Scrappers on Steam](https://store.steampowered.com/app/2005210/Void_Scrappers/) and [our initial interview](https://defold.com/2022/11/24/Void-Scrappers-post-mortem/). The game received very positive reviews on Steam and seems to have been well received overall. How has these post-launch period been?__

*Alex: The first month after launch was intense. We spent a lot of time fixing bugs and frantically implementing the community's feature requests. The effort was well worth it, as the new features significantly improved the reception of the game. After that we took a break for the holidays, then changed our focus to releasing on the Nintendo Switch. We also tentatively started thinking about our next project (watch this space)...*

![](/images/posts/void-scrappers-post-mortem/void-scrappers-key-art.jpeg)

__Exactly, the game was recently also released on Nintendo Switch (on March 3rd to be precise). What can you tell us about the release?__

*Alex: The release went well! The main difference to the Fates of Ort release on Nintendo Switch was that Void Scrappers has been localised, and we therefore released it in Japan as well as in the Europe and Americas regions. We were pleased to note that the game is performing really well in Japan.*


__Have you done any deeper analysis of why the game is performing really well in Japan?__

*Alex: Not really! I am told the translation is done to a really high standard (thanks Kohei!), which may very well have helped with word of mouth.*

*It is possible that the game genre appeals to the Japanese audience, and that the market may not have a ton of options in Japanese.*


__What did the porting process look like? Did you have to change much in the game to get it running on Nintendo Switch hardware?__

*Alex: Void Scrappers pushes performance to the limit, and this was immediately noticeable on the Switch. We were forced to make actual changes to the gameplay in order to make the game run smoothly. The effect of this was to push performance to a tolerable level, thankfully without sacrificing enjoyment. Users that have played both the Switch version and desktop version have not commented on any apparent differences, which is great!*

*On the technical porting side, things went very smoothly - and we owe this to Defold. It doesn't escape our notice that other indie devs have to get a publisher to port their games, where thanks to Defold we are able to do it ourselves! I wouldn't even call myself a hardcore programmer. My Lua skills are strong, but that's pretty much it.*

*It does take a bit of work, however. For example, the Switch uses Vulkan which can cause issues. For Void Scrappers, these were minor and were resolved quickly thanks to help from the Defold team.*

*We can't comment too much on how hard it is to implement Switch functionality, such as accessing/using user accounts and gamepads. Our games tend to not need this!*


__What is your advice when developing a game that you also intend to release on consoles? Are there any tricks to making the porting and/or release process as smooth as possible?__

*Alex: __Staggered releases__. This might not work for everyone of course, but we tend to release on desktop (Steam) first and consoles later. This gives us an opportunity to correct all post-release bugs and issues, and also implement some additional features based on community feedback. Nintendo's lotcheck process is quite rigorous, and patching is a bit harder than on Steam. Releasing on Switch some time after Steam means the process is much smoother, as a lot of problems have already been addressed.*

*__Plan for consoles early__. This means things like ensuring controls are well suited for gamepads, and that text and UI elements are readable on small screens. "An ounce of prevention is worth a pound of cure" definitely holds true here. It is much easier to set things up well in advance, than fixing them later on. For Switch specifically, this might also mean loading the game on Switch during development, to assess performance.*

__Thank you Alex for sharing your post-launch experience and your advice on console development__