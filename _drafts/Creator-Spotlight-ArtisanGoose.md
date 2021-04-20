---
layout: post
title:  Creator Spotlight - Artisan Goose
excerpt: In this Defold Creator Spotlight we invited Artisan Goose to tell us a little bit about himself and his latest Defold projects.
author: Björn Ritzl
tags: ["creator spotlight", "interview"]
---

In the Creator Spotlight posts we invite Defold users to present themselves and share a bit of their background, their work and things that inspire them. It is an excellent opportunity for the community to come together, to recognise achievements and to share some of the great work done by Defold users.

In this Defold Creator Spotlight we invited Artisan Goose to tell us a little bit about himself and his latest Defold projects.


##### What is your name?
👋 Hi, I'm Adam Engebretson.

##### What is your background?
After spending far too much money earning my Bachelor's in Biological Chemistry, I decided to become a freelance web developer. It started as simple Wordpress hosting for small business, then quickly evolved into working on projects with the likes of AAA and David Letterman. I was then hired by a small medical software company and proceeded to grow my "fullstack engineer" resume, featuring boring web languages like HTML, CSS, JS, and PHP.

My priorities at work then shifted to requiring software to run directly on workstations, so I decided to learn Golang. I haven't looked back at PHP since. The most significant aspect of this transition was learning the functional difference between interpreted and compiled languages. With no exposure to any of the C-flavored languages, Golang's type system was a fantastic way for me to understand this new (to me, anyway) way of programming.

I got really sick of writing B2B software for end-users, so I transitioned into a DevOps role where I have the luxury of having my fellow engineers as my end-users. My team focuses on enabling our feature teams to ship our software rapidly and effectively. This is comprised of Infrastructure as Code, Continuous Integration and Deployment, and Kubernetes as the infrastructure platform.

##### When and how did you learn of Defold?
I can't recall for certain, but it was either a Reddit or HackerNews post that caused me to open Defold.com as a tab on my phone. Weeks later, I came across said open tab and decided to give it a look!

##### What do you like the most about Defold?
As someone who comes from the world of web application development, game development appeared mysterious felt inaccessible to me. Defold's approach to object addressing (URL/path-style) and signaling (msg.post()) immediately made sense to me and I felt like I could grasp some of the concepts more easily than in some of the other game engines I've looked into.

<div align="center"><p style="font-size: larger"><i>"The syntax is stupidly simple to learn, and the APIs are beautifully documented"</i></p></div>

Additionally, Lua came very easy to me having used it for a handful of work-related and [Computercraft](https://www.computercraft.info/)-related applications. The syntax is stupidly simple to learn, and the APIs are beautifully documented on [Defold.com](https://defold.com/ref/stable/go/). Following the quick-start guides and tutorial projects was an absolute breeze, and I was able to follow the logic of the simple examples enough to become dangerous.

I should also mention... Before I decided to dive in, I did notice that [Haxe](https://haxe.org/) was listed in the [Asset Portal](https://defold.com/assets/haxesupport/). Even though I said all the nice things I said about Lua, I hate Lua lol! I've been spoiled by the static typing and "it-just-works" IDE Intellisense that comes with Golang, that I wouldn't feel confident at all in my code if I had to write it all in Lua. Knowing that I'd be able to learn the platform/concepts in Lua quickly and easily, then subsequently reimplement it in a statically typed language, was the deal maker.


##### What are you working on right now?
I find myself to be a "less than creative" individual. I have no design skills, and coming up with game ideas is not my strong suit. Thus, as an exercise in learning, I'm attempting to re-implement Minecraft in Defold using Haxe. I'll also probably progress to writing server-authoritative multiplayer (for me, that’s the easy part) using [Nakama from Heroic Labs](https://heroiclabs.com/) and their [Golang plugin support](https://heroiclabs.com/docs/runtime-code-basics/).

I did spend some time trying to write a Nakama server plugin in Haxe and then compile it down to Lua, but I decided against it since Nakama's types are already declared in Golang, and I'd have to go through the process of doing that myself if I wanted to work in Haxe.


##### What is your experience with Haxe?
Haxe gives me confidence in my code. Additionally, the IDE Intellisense brings the Defold API to my fingertips. I just type GoMessages., and the IDE auto-recommends acquire_input_focus. Typing Msg.post( presents me with a tooltip documenting the method's arguments. Saving my .hx files automatically lints the code and shows me where my typos are.

<div align="center"><p style="font-size: larger"><i>"But with Haxe, I feel like I've '🏆 Achievement Unlocked'"</i></p></div>

I'm also able to take advantage of the Haxe language features to artificially accomplish things that don't appear to be possible (or are much harder, or I'm dumb) in Lua. I bet someone who is more fluent in Lua implementations could comment on this in more detail, and maybe I'm missing a part of the bigger picture here. But with Haxe, I feel like I've "🏆 Achievement Unlocked".


##### What does the development process look like when using Haxe with Defold? Build process, tools, that sort of thing.
It's really quite simple to set up, but it took me a little bit of time to get fancy with the Haxe compiler. This is purely an artifact of me not knowing Haxe before this process.

1. Install [Haxe](https://haxe.org/download/): `brew install haxe`
2. Install [hxdefold](https://github.com/hxdefold/hxdefold#quick-start): `haxelib git hxdefold https://github.com/hxdefold/hxdefold`
3. Initialize hxdefold in your project: `haxelib run hxdefold init`
4. Run `haxe build.hxml`
5. Attach the generated script at `scripts/Hello.script` to your Game Object

I tried creating a `hooks.editor_script` that would trigger the Haxe build at compile time, however the Defold engine appears to load the generated `app.lua` file before this hooks gets called, so you effectively have to compile your game twice to see your changes. Something tells me, however, that there will soon be an update that provides a solution to this problem.


##### Which part of your current project are you most proud of?
I'm most proud of the confidence I have in my code every time I go to run my game. That is not to say I'm confident in my game logic, but that's a different conversation entirely (on which I'm not qualified to comment lol).

I know many readers out there might say something like, "well if you want a statically typed language, use a game engine that utilizes one." That's sound advice, for certain. However, I've gone down that road before with minimal success. Perhaps now that I have a better understanding of Haxe, I'd be more effective in a C-flavored language (I have noticed quite a few similarities between them, and have certainly been able to interpreted C-flavored code better since learning Haxe).

The success story here is the approachability of Defold for folks new to game development, whether you have experience with coding or not. Addressing Game Objects with a URL/Path-style identifier is genius, and passing named messages back and forth is so flexible and easy to understand.


##### Tell us about your ugliest hack to get a job done!
I'll be keeping an eye on the comments section for a solution to his one...

Since Haxe is a statically-typed language, declaring variables requires you to consider the type of the variable. In my use-case, I'm trying to call the `Buffer.create` method. For the life of me, I couldn't get the Haxe compiler to produce a type that it would accept as the 2nd argument to this method: `lua.Table<Int, defold.BufferStreamDeclaration>`. In the end, I was able to tell Haxe to ignore that part of my code and treat it as vanilla Lua. The workaround looks like this:

```lua
var buf = Buffer.create(self.vertices.length, untyped __lua__('{
  { name = hash("position"), type=buffer.VALUE_TYPE_FLOAT32, count = 3 },
  { name = hash("normal"), type=buffer.VALUE_TYPE_FLOAT32, count = 3 },
  { name = hash("texcoord0"), type=buffer.VALUE_TYPE_FLOAT32, count = 2 }
}'));
var pos = Buffer.get_stream(buf, "position");
var nor = Buffer.get_stream(buf, "normal");
var tex = Buffer.get_stream(buf, "texcoord0");

// do stuff to these streams to draw a mesh

var res:Hash = Go.get("#mesh", "vertices");
Resource.set_buffer(res, buf);
```


##### How can the community follow your progress?
As I have time to hack away at this project, I'm uploading my code to [GitHub](https://github.com/adamgoose/haxecraft) and posting updates in [Discord](https://discord.gg/cHBde7J). This conversation began in the #rendering channel, but I'll float between there and #game-jams. If you're lucky, you'll catch me streaming in Voice 1.
