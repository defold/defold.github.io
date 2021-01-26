---
layout: post
title:  The Defold engine code overview
excerpt: An overview of the components of the Defold game engine runtime
author: Mathias Westerdahl
tags: ["engine", "code"]
---

From time to time we get questions about how the Defold game engine runtime works in certain areas. And since we also accept contributions to our source code,
I feel it's time to give some insight into the structure of our engine. I'd like to start at a fairly high level, describing the bigger systems, and in later posts, go into more detail about some key systems.

To properly describe a graph detailing all dependencies and libraries in a game engine would be quite daunting, so I'll try to give a much higher overview of it.
This graph tries to balance between showing what systems are used, and also some key libraries that they use. It also tries to convey a sense of "layers", where a top layer depends on functionality from a bottom layer (but never the other way around).

[Full source code](https://github.com/defold/defold/)

<br>

![Engine overview schematic](/images/posts/engine-overview/engine_layout.svg)

<br>

### Base functionality

At the base level, we have libraries that provide core functionality to the other libraries and systems.
Examples are C++ containers, threading support, network support, loading/saving files and data formats.

#### Defold Data Format (DDF)

This a format implemented on top of Google's [Protobuf](https://developers.google.com/protocol-buffers). We generate bindings to C++, Java and Python, which we use in our tools as well as the game runtime.

#### Network support

The engine supports (secure) sockets, which we build upon to implement http(s) support. This allows games to request information or store game session information such as user info, high scores etc.

#### Compression

We use several types of compression in the engine. We expose ZLib deflate to the developers (for decompressing custom files).
And we use LZ4 to compress the game archives. For textures, we also have WebP as an option.

#### Hashes

For the base hash function, we use MurmurHash2A which is very small, and works very well for our purposes.
We use it to hash short strings and file paths. It's also used to generate unique ID's for game objects when they're spawned.
We store the hash state (a `uint32_t`) for later use, which allows us to incrementally hash more data.

Hashes are also stored in the save games, which is one reason we haven't updated the hash function to any newer version.

#### C++ containers

We use only a few types of C++ containers in our engine: Array, HashTable, Object/Index Pool.
They are not "modern C++", and they're implemented to support POD types.

*You can read more about our [code style and c++ here]({% post_url 2020-05-31-The-Defold-engine-code-style %}).*


### Graphics


#### Backends

We've supported OpenGL for quite some time, but we've recently added support for Vulkan. This transition was fairly straight forward, as we already had our own graphics api, with an OpenGL backend. Our graphics api is currently geared towards how OpenGL works, but we'll add a more modern api later on to reflect the newer functionalities of the Vulkan backend.

#### Rendering

The rendering itself is done by issuing commands to the renderer. E.g. Clear or Draw.
The Draw command uses a predicate, which is used to gather all the render objects with a material that match the predicate.
Once all matching objects are gathered, calculate a "render key", which is used to sort objects with similar characteristics.
This allows us to batch similar objects into a single draw call.

*See ["Order your graphics draw calls around!"](https://realtimecollisiondetection.net/blog/?p=86) by Christer Ericsson for more details about batch keys*

#### Scriptable render pipeline

One of the most powerful features of Defold is that the rendering pipeline is scriptable.
It allows the developer to control the flow of a render frame by clearing rendertargets, setting materials, settings camera matrices, doing multiple render passes etc.

*See the [documentation page](https://defold.com/manuals/render/#the-render-script) for some practical examples*

### Sound

Our sound engine is quite small and doesn't have a ton of features.
It supports multiple voices and groups, different speeds and panning.
Supported formats are Wav and Ogg. Depending on platform, the backends are OpenAL, OpenSL or WebAudio.

### Input

Our input is split into two libraries: HID and Input.
HID is the hardware abstraction, and Input is the high level processing.

### Physics

For legacy reasons we have two physics engines in the vanilla engine (Box2D and Bullet 3D).
This will likely change in the near future, as we're working on moving more and more functionality into separate extensions of the engine instead.
The physics is currently updated on the main thread, and this is also something we'll be working on.


### Native Extensions

Extensions are implementations of a certain api in the engine. In this case we refer to implementations that hook into the life cycle of the app.
These are the current functions available: AppInitialize/Initialize/Update/OnEvent/Finalize/AppFinalize
Using these functions, it's easy to add new functionality to the engine, using either C++, Objective-C or Java.

We are continuously working on moving parts of the engine into extensions. This allows for better decoupling, removing parts a certain game doesn't need, slimming down the executable size.
It also adds the possibility for our users to help out updating the extension, and finding/fixing bugs.

In the future, we'll support more api's to hook into, e.g. resources, components etc.

#### Defold SDK

We expose the extension api to 3rd party developers, via our [Defold SDK](https://defold.com/ref/stable/dmExtension/).
This allows them to implement features that they require for their games. These extensions are then either shared with other users via our [Asset Portal](https://defold.com/assets/) or via Github.

Some examples are:

* [https://github.com/dapetcu21/defold-fmod](https://github.com/dapetcu21/defold-fmod) - Adds support for FMod sound engine
* [https://github.com/AGulev/defold-poki-sdk](https://github.com/AGulev/defold-poki-sdk) - Adds support for the Poki sdk
* [https://github.com/defold/extension-websocket](https://github.com/defold/extension-websocket) - Adds support for WebSockets

These extensions also work as a test project for the functionality they provide.

#### Extender server

The extender server is our cloud build server, where the developer will eventually build their custom engine (if they're using native extensions).
This is done automatically when they press "Build and Run" from the editor (or command line toolchain).
The server supports all our platforms, and it means a zero setup process for the team.


### Script

Defold is using Lua for scripting game logic.
We support Lua 5.1 and also LuaJIT on those platform where it's supported/allowed.
Native extensions usually also register new Lua modules for the developers to script with.

### Resources

Our resource types (textures, sprites, sound files etc), are registered at startup of the engine, with functions for creating a resource, or to destroy it.
We use reference counting for our resources.
The resources can be requested by any system that needs the resource, and the reference count will increase.

#### Dependency graph

A Defold project always has a clear dependency graph between all resources in the game. At the top, we have `game.project`, which in turn references other source files. This gives us a complete scene graph to traverse and compile. It also makes sure we don't include anything redundant into the game archives.

#### Hot reload

A key feature of our resource system is that you can change a source file in our editor, and then choose to "hot reload" the new changes into a running game instance.
To support this, the resource system also has a special function to recreate a resource, since it might need some special care.

#### Live Update

Our Live Update system allows the game to be split into two when being bundled into the distribution form.
One part will be the build uploaded to the app store, the second part (a .zip file) contains any resources marked for exclusion.

This allows games to have a small initial download size, and allows the developer to download the rest of the resources later on.
This system works on all platforms (where allowed).

### Game System

#### Collections and Game Objects

We call a level a "collection", and each collection contains one or more game objects.
A game object is very light weight to create and destroy. We preallocate a certain number of game objects into a pool, when the collection is loaded.
The game object holds a transform at it's bare minimum, but it can also hold one or more components.

#### Components

Examples of components are Collision Object and Sprites.
A component usually handles updating the properties of an instance (e.g. the tint color of a sprite). updating the component instance itself, and registering the visible render objects.

The components are updated on a per-type basis, i.e. it updates all the sprites (per collection) at the same time, in a for-loop.
All component types are updated in the order they were registered to the game object system.

#### Gui

The Gui component is a special type of component, which essentially has its own set of sub components (box node, pie node etc).
Editing a gui file is treated specially in the editor, using an orthogonal view, and also provides layout switching (landspace, portrait etc) for easy previewing.

#### Messages + URLs

The Defold engine relies heavily on passing messages between internal systems. It helps keep systems decoupled internally, and also when scripting game logic.
A key component in our messaging system is the URL. If consists of a "socket", a "path" and a "fragment" (Example: `level1:/player#sprite`).
Internally, the url is converted into 3 hashes, for faster lookups.

*Read more about [addressing and urls here](https://defold.com/manuals/addressing/)*


### Engine

At the top level, we have the startup and the main loop of the game engine.
Although most of it is fairly generic, on some platforms we need to take special care to setup and/or update the engine in a way that works for that platform.

The update loop updates all the registered systems (physics, sound, gameobjects)

We also start some special helper services, such as [the web profiler](https://defold.com/manuals/profiling/#the-web-profiler) and the screen recorder.


## Wrap up

This was a very brief, first look at what types of systems we have in the engine.
Going forward, I wish to explain some of the areas in more detail (e.g. Components and Extensions)

If you're curious, don't hesitate to [look at the source code](https://github.com/defold/defold/)
