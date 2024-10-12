---
layout: post
title:  The Defold engine code style
excerpt: Since we opened up our source code to contributors, we also get some questions from time to time regarding our choice of coding conventions. These are some of our experiences over the years, and what has led us to our way of developing today.
author: Mathias Westerdahl
tags: ["engine", "code"]
---

Since we opened up our source code to contributors, we also get some questions from time to time regarding our choice of coding conventions. We recently updated our [code guidelines](https://github.com/defold/defold/blob/dev/README_ENGINE.md#code) to be a bit more specific. But we also feel that it might be good to add some context to how we settled on our particular approach.

These are some of our experiences over the years, and what has led us to our way of developing today.

## Background

Defold has been around for 10+ years, and it sprung out of the founders' (Ragnar Svensson and Christian Murray) ideas that there has to be a better way of developing and maintaining a game engine (and a game). Many of those ideas came about when they worked together at Avalanche Studios, a game studio in Stockholm, developing features in the engine and the games.

I worked with both Ragnar and Christian at the same studio, but I started a bit earlier than them, back in 2004. Back then, the engine we were developing was very much the "modern" programming equivalent of what people think of today. Or, it wasn't to begin with, but it soon became that way. (I certainly was on the "Modern C++" band wagon)

This was a big part of the struggles that ensued. The codebase became very large and perhaps more importantly, it became hard to make changes to it and to iterate on it. As we closed in on the shipping date, it was a real struggle to make the game fit onto the DVD. And at the same time, the performance wasn't very good.

## A "modern" engine

I think it helps to understand what a "modern" engine could look like 15 years ago. This is of course not to talk trash about the engine, or the work we did, but to understand the journey we took. A lot of brilliant developers worked on the engine, and we shipped great games with it. But looking back, we could have done certain things differently, and that's what inspired a lot ideas behind Defold.

### C++ patterns

When I started working at Avalanche Studios in 2004, the "Modern C++" way of doing things was already very strong, and not only at our company.

We used C++ patterns to the left and right. Everyone on the team had to read "Effective C++". We felt a fresh breeze of "this is awesome" and rapidly added more and more code to the engine, containers and smart pointers etc. Perhaps you remember Singletons?

The scene graph consisted of a virtual GameObject base class, and it had a list of child game objects. Each game object type inherited from the base class, and often implemented some variation of the virtual base class functions. The inheritance tree was deep, and sometimes you inherited from two base classes. There were a lot of game object types, and it became difficult to keep track of all the variations and nuances that the implementations added.

The data flow problem also became more and more prominent. When _was_ the transform of an object actually updated, and safe to use?

The effects of adding all these "best C++ practices" haunted the engine for many years, and it took a long while until they were replaced with something more fitting for the tasks.

### Standard Template Library (`std::`)

At this time, the `stl` was still very new. It was exciting, and we were very eager to learn and use it. The promise of simply avoiding "reinventing the wheel" ever again was very attracting.

Understandably, we used the containers all over the place. After all, that's what they're there for, right? The cost of all this accumulated over time, and over a couple of years, the technical debt grew significantly.

Performance of the game also suffered a lot. All those tiny allocations that the `stl` containers made, were like a death by a thousand needles. At one point I remember Christian profiling the usage of `std::string`, and before the menu screen of the game showed, it had made 1 million allocations. Not ideal. Allocations cost, even today.

And smart pointers were a big problem too. Not only that each `weak_ptr.lock()` was very expensive, it was also symptom of unclear ownership of the data.

The stream api's was another big source of performance issues (e.g. `<iostream>`, `<stringstream>`).

Another problem was that all compilers also implemented `stl` a bit differently, with subtle changes. Either because the specification allowed it, or because of a bug.

### Shipping time!

Compilation times wasn't really on our minds back at the beginning, but they had grown for sure. Waiting for a change on the autobuilders took forever. The team was already quite large, so waiting was costly!

And code size grew as well. When we closed in on our first shipping date, we _really_ had to struggle to fit the engine onto the DVD, it was more than a whopping 20+MB! (was it 27?).

So, as many developers do, we worked very long and hard to meet our requirements. And indeed, we finally shipped the game, and it became a success, allowing us to continue development of the engine.

## The Defold engine

Seeing certain struggles repeat themselves over time, in the engine and the game development, led to numerous discussions between Christian and Ragnar. After realising they were both developing their own engines at home, they decided to join forces. This creation is what became `Defold`.

At this point, Christian had worked as a tech lead for the company for some years, and we had already started to move away from the old way of doing things. A lot of the technical choices made are very similar to what Defold still uses today.

Some years earlier, in 2006, an article about [God of War](https://www.gamedeveloper.com/design/gdc-i-god-of-war-i-how-the-left-and-right-brain-learned-to-love-one-another) was published, and it was truly inspiring to read that such a game could fit into 1.5mb of executable code. As a big bonus, the small code also seemed to yield a much lower bug count than usual. After many years of AAA engine development, these ideas would influence a lot of the choices made by Christian and Ragnar when creating Defold.

### Small codebase, small engine

The Defold engine always strives to be as [small](https://github.com/britzl/dmengine_size) and fast as possible. That goes for both development and the final product, as it helps both developers and ultimately the players.

To achieve this goal, we use a simple rule: "If we don't need it, we don't use it". We apply this idea to both the design and implementation phase, in both large and small.

For instance, we don't add features no user has asked for, nor try to solve more than the problem at hand.

One example of this is our GUI system, which is quite rudimentary. This is due to the fact that different users often have very different views on what a GUI system should support. So, we provide basic building blocks, and a way for our users to build their own gui system on top of it.

And, before we add third party libraries to the engine, we do a due diligence first to see what options we have. One option being, to implement the feature ourselves.

### C-like C++

Although we technically _do_ use `C++` (we cannot compile using only a C compiler), we don't use _all_ the features of C++ as soon as they come out. In fact, we only use a very few features, like `namespaces`, `RAII` and a few `templates`.

I would describe this style more like C than full C++. The term `C-like C++` is pretty common, and describes our engine well.

Most of our internal libraries have some public headers, that are used by other systems in the engine. These libraries usally have functions to create/destroy a context. This context can then be passed to the rest of the library's functions:

```c++
HContext ctx = dmSomeLibrary::Create(params);
float value = dmSomeLibrary::CalcValue(ctx);
```

Here's another good resource on the topic of simplistic use of C++: [C+](https://gist.github.com/bkaradzic/2e39896bc7d8c34e042b) (It also lists some more reading materials)

### No classes

Defold uses a `component` based way of adding functionality to a game object. This decouples the dependencies between owner (the game object), and the data itself (e.g. a sprite). This allows us to have a much clearer chain of dependencies, where each component type is updated after another. And, it also removes the need for a base game object class.

And, since we don't use classes or inheritance, we don't have any need for RTTI.

Apart from some container classes we have, the only cases where we _do_ implement a class type, is when we have to interact with a third party (E.g. Box2D).

### No exceptions

In a game you most often know all the data you are about to use before you use it. You have preprocessed it through a data pipeline, and transformed it from source data to compiled data, ready for consumption by the engine. In this process, you can take any steps necessary to ensure that you catch any data errors. This is beneficial since the earlier you catch the problem (preferably in the authoring process), the less it costs.

It also has another benefit; since all data is already verified to be ok by the data pipeline, you don't need C++ exceptions in the engine. And you can get rid of a lot of defensive programming, by assuming that the data is always ok.

### No STL

People often associate STL with C++, like they're one and the same.

They're not. C++ is the language, while STL is a _library_.

The usage of any library is a choice, and should pass the due diligence just like anything else in your workflow. In our case, we have chosen to not use it, for performance reasons (compile time, code size, runtime, memory).

Another feature we have is our extension system (plugins), allowing users hook into the engine. If we were to add `stl` as a dependency, we'd have to enforce the same version of compiler onto all developers, due to the ABI of `stl`. This has already been a problem in the past, and we simply don't want to be in that position again.

We do have some exceptions to the rule (for the time being), which is `std::sort()` which we haven't found a good replacement for (yet). In the future, I hope we can remove the dependency altogether.

### Containers

At Avalanche, we eventually replaced our containers with low foot print, cache friendly containers. In fact, the [dmArray](https://github.com/defold/defold/blob/dev/engine/dlib/src/dmsdk/dlib/array.h) and [dmHashTable](https://github.com/defold/defold/blob/dev/engine/dlib/src/dlib/hashtable.h) are similar to how they looked when Christian first wrote them in the Avalanche engine.

These containers are written for POD (plain old data) types, since that's what we use them for.

Often you hear people say that writing your own containers would introduce bugs, and that you should stick with `stl`. I find this problematic, since this is coming from engineers that should know quite well how to write an array/hashtable container. Yes, you might have some initial issues, but those are usually along the way of design issues (since you probably allow youself to implement an api that _you_ prefer for _your_ task). But, since you wrote the code, you are well equipped to fix these issues.

Our [array.h](https://github.com/defold/defold/blob/dev/engine/dlib/src/dmsdk/dlib/array.h) is 219 lines of code. There's really not that much code to worry about. It's short and fast, with respect to both compile time and run time, and serves our use case perfectly.

Our [hashtable.h](https://github.com/defold/defold/blob/dev/engine/dlib/src/dlib/hashtable.h) is 321 lines of code, and it's _really_ fast. It's not very complex either, so please have a look.

### Pointers

Someone once told me that pointers are dangerous, and I frankly don't understand that. The pointer itself doesn't do anything, it's just data. It is up to the developer to decide what to do with that data, and perhaps more importantly, _when_ to use the data.

One of the main fears seem to be "null pointers", but in my experience they're the most easy to catch and fix. They happen rarely (usually when developing a new feature), and are quickly fixed.

A more justified fear is a dangling pointer, where the pointer no longer points to what it originally pointed to. These do happen on rare occasions, but are most often also fairly easy to fix.

#### Pointer alternatives

To mitigate the pointer danger, some developers use other mechanisms:

* One popular pattern is to use `const Data&` to "be safe", but those are really also just a pointer, and susceptible to the same issues.

* Smart pointers are another tool many express that they want to use. One cost is of course the added if-statements that are required, but most of all the latency of the `lock()` call, and the added [code size](https://godbolt.org/z/W-rmpz) of it. I don't recall the exact numbers from back in the day, but the lock takes a lot of time. I don't need to measure it to know that it's a lot more than just accessing a raw pointer. Especially from different threads.

* Unique pointers are another pattern, and in fact, a bit more inline with the RAII we sometimes use.
However, we _would_ only need them in short scopes, thus it's just as easy to deallocate the pointer manually. Manual deallocation also helps with readability.

### Data life time

Continuing on the `Pointers` track, the most important thing to remember is that the pointers _aren't_ passed around to different systems at random. We know what system owns a certain pointer, we know what systems may have access to that pointer, and we know the life time of that data.

Each system knows about its own resources, and is said to be the "owner" of the data.
This ownership _may_ be passed to another system, but this is clearly communicated via the api.
Having a clear owner of the data is important, because it allows you to make important assumptions about your data, such as "the data will always be alive when I reach this code".

That, in turn, is very significant:

* It means you don't have to do "if (data != 0)" all the time (defensive programming).
* It means you don't have to protect the data in any smart pointer.
* You don't have to pay any extra overhead for accessing the pointer.

### Modern C++

Around 10-15 years ago, I was super interested in what C++11 had to offer and back then it was manageable to keep up to date with and asses the new features.

Each new feature was a hammer, and I was eagerly looking for nails to use it on. Then I (amongst others), realized that we were simply doing the old dance again, where we went in head first into new features without thinking about what we actually needed or wanted from our code.

Nowadays, there are more and more features being pumped into the C++ language, and an honest question is: "Who is it for?". I haven't seen any new feature that would make this engine (or any code that I've written for the last 10 years) significantly better.
Convenient perhaps, but not better in terms of compile time, code size and runtime or readability. As such, we'll just stick to the proven way that we've been on for the last 11 years.

We are still using the feature set of `-std=c++98` for the engine code, and although I'd like to enforce it in the compiler flags, some platforms require us to use `-std=c++11`.
So it's just easier to leave the compiler flags at its default, and just stay clear of the recent features of the language. If there was a way to set the standard to "C-like C++", it would be great.

`auto` is one example I've seen first hand completely take over a code base. In the end, it just became unreadable and basically typeless. We are _never_ in such a hurry that we cannot type a few characters extra.

## Final thoughts

I hope this gives some insight as to why _our_ code looks like it does, and why _we_ are not looking to change it. Keep in mind that our use case might not fit your use case

---

If you want to learn more about our contribution process and how to help out then please [head over to our Contribution page](/contribute/).

If you want to discuss the source code please join [the discussions in the sourcecode category on the Defold forum](https://forum.defold.com/c/source-code).
