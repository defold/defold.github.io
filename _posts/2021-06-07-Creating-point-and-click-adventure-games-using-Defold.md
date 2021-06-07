---
layout: post
title:  Creating point and click adventure games using Defold
excerpt: In this post we will focus on how Defold game developer Marco Giorgini has created his own tools to create point and click adventure games in Defold.
author: Björn Ritzl
tags: ["developer case study", "interview"]
---

Defold is a very versatile game engine with a design and structure that lends itself well to creation of games in many genres. The Defold editor has a complete scene editor where you can arrange objects into complex hierarchies to build levels, rooms and other scenes in your games. Combine this with a complete GUI editor, tilemap editor and advanced particle effect editor and you get a very powerful and easy to use game creation tool. And the editor requires a single download with no installation and runs on Windows, macOS and Linux.

Additionally, if the capabilities of the Defold editor itself doesn't provide a good enough tooling process for your game it is quite easy to create your own external tools that operate on and modify the Defold data files since all of them are represented as human readable and merge friendly text files. One example of this can be seen [in the developer interview with Artsiom Trubchyk](/2021/05/03/Developer-Case-Study-Releasing-Mahjong-cards-on-Yandex-Games/#what-was-the-development-process-like-for-mahjong-cards) where Artsiom showed the custom editor that was created for Mahjong Cards. Another example which we will focus on in this post is how Defold game developer Marco Giorgini has created his own tools to create point and click adventure games in Defold.


### Hi Marco! Can you please tell us a little bit about yourself?

Hi Björn, and thanks for this post. Well, I'm an Italian programmer who started coding in the 80s with Home Computers and never stopped since then. My daily work involves doing R & D in the [Natural Language Understanding](https://en.wikipedia.org/wiki/Natural-language_understanding) field but one of my passions is still connected to the reason I've learned to use computers ages ago: creating video games.


### When and how did you learn of Defold?

Well, since the iPhone I've done a lot of mobile games - with my own multiplatform (mainly C + OpenGL) engine. I used it even for some jams but for them, a web version of the game seemed a really wise idea. So I've started both using [Emscripten](https://emscripten.org/) AND looking around for a different engine with an easier and faster workflow - and that is how I found Defold. That, for me, was really cool. No complex installation, multiplatform builds without external dependencies and (at least at the beginning) even a web page with the remote build (I just needed to submit my code and I could try a web version, built remotely). I never used Lua before Defold, but I found it easy and nice, so when my brother asked me for a little mobile game for a social initiative, I did it with Defold and have since then used it for most of my game dev projects. Love at first sight - or something similar.


### Looking at the games you have released you're obviously a big fan of point and click adventure games. What is it about adventure games that makes you come back to this specific genre over and over again?

I've always loved adventure games - mainly point'n'click ones - but I've never really finished one before [The Child of the Hill House](https://gamejolt.com/games/thechildofthehillhouse/337760) - a game I did in 2018 with Defold with the first version of the framework I'm still improving and using even now. That was great - I mean, not necessarily the game, even if I still think it's good, but the fact that I've seen I was able to mix up TWO passions at the same time - game programming AND writing. And I love the group of people I met online then, for the jam. So well, I've kept doing point'n'click jam games every time I can. But I didn't just do this kind of game. Another game I'm proud of (also done with Defold) is for instance Fork vs Monzie - a platform game related to a specific episode of [Happy Days](https://en.wikipedia.org/wiki/Happy_Days) (a serial quite common when I was young) [Fork vs Monzie by Marco Giorgini](https://marcogiorgini.itch.io/mork-vs-monzie).


### You recently shared some information about your workflow and it is intriguing because you use Defold for your games but you are actually not using the Defold editor when creating the games. Can you tell us a bit more about this?

Well, I don't work INSIDE Defold. I mean, Defold is the PLAYER of the game, but it's scripted elsewhere because I find that adventure game needs a specific structure AND because I'm used to working with [Aseprite](https://www.aseprite.org/) as a graphic editor. So I've got a source folder with my scripted game, and its resources and a Defold project with my Lua code. I also have a tool that creates Defold's elements which is possible and "easy" because Defold stores everything as text files.


### This sounds like a really cool setup! Can you give us an example of how it looks?

Sure, inside my game, there's a tutorial session. Let's see how it's done!

![](/images/posts/creating-point-and-click-adventure-games-using-defold/ase-training.jpg)

As you can easily see I've got an image with layers, and the layer names have prefixes which my build program will use to know how to handle things. First, the `bkg` prefix indicates NOT ONLY the background image, but the **Name** in which I want to put all the elements I'll use for this scene - and for that I mean in which [Defold Atlas](https://defold.com/manuals/atlas/) I want to have the pieces I take from this Aseprite file and write as png. As you can see the background image - called `bkg.past` becomes part of `bkg_past.atlas` - and its elements part of `props_past.atlas`.

![](/images/posts/creating-point-and-click-adventure-games-using-defold/defold-atlas.jpg)

I do the same things for actors - I draw them in Aseprite with layers and animation (and timing) - and I convert them to an atlas file with the same characteristics.

![](/images/posts/creating-point-and-click-adventure-games-using-defold/ase-anim.jpg)

For this game, I've decided to handle some layers as separate sprites inside a game object - and so I've changed the generating code (and handling one) to let me do that.

![](/images/posts/creating-point-and-click-adventure-games-using-defold/defold-anim.jpg)


As you can see my game has a lot of animations - but that's very easy to handle, considering I just do things in Aseprite and then build the corresponding atlas in Defold. Last, but not least, here's how I handle game code. I use a [TreePad Lite](https://treepad-lite.en.lo4d.com/windows) file (because it's handy!) which I convert in a json file (because it works very well inside Defold) and then scan its content to build Defold resources (including sounds and game project data).

![](/images/posts/creating-point-and-click-adventure-games-using-defold/treepad-script.jpg)

In the image above my script attach a scene to a scene in an Aseprite files - and let me use elements in layers - so that I can do something like `if:drawer,opened and setstatus:drawer,opened` - and that's connected to elements defined in the Aseprite file - like hotspot, or object, or graphic version of elements, for a specific state. Another example is `setstatus:drawer,opened` which will activate the `drawer.opened` image - that will start as NOT shown, because of layer visibility attributes.


### This sounds like a really great setup - taking advantage of tools you know and integrating them with Defold. Are there things you could improve?

This is ONE of the things that's possible to do with Defold that I love - to use it for its great power - taking advantage of its flexibility to put it inside a more complex workflow. The fact that Defold uses Lua as scripting language means that I could probably shift from generating data in json format for my script (that's handled by Lua code - as interpreter) to directly generating Lua code - that will use functions present inside my framework.

This could improve the "only" thing that still isn't optimal in my way of work - because even if (for me) it's fundamental to "compile" resources from my preferred formats to Defold's ones - it's slow to have to rebuild the json to test a single change in the gameplay - considering that [Defold has hot reload of its Lua code](https://defold.com/manuals/hot-reload/).


### What could be changed in Defold to make your workflow even more optimised?

It's hard to tell because you already allow MORE than I already use - like building games outside of the editor. It would be great to be able to connect things more between all my parts but that would more mean to be able to work INSIDE Aseprite than inside Defold editor.

Maybe a thing that could be nice to have would be a way to build some files in the project folder with external compilers (based on extension) - I mean, that way I could build the Aseprite file to an atlas each time I build the project. But it's not necessary - surely not for me for this kind of project - but may be useful on other occasions. I mean I'll probably start to have hot rebuilds from the outside based on files changed in folders - and if I'll do that I can already update (some) things on the fly in Defold while it's running. So everything's already more than good here.


#### Thank you Marco for taking the time to share how you work with Defold! How can the community follow your progress and learn of new games and other developments?

I'm not constantly active - because of my daily work and of other personal projects - but when I do game programming I surely talk about that on [Twitter (@marcogiorgini)](https://twitter.com/marcogiorgini) - so if you want to, you can connect with me there!
