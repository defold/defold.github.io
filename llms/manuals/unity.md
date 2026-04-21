# Defold for Unity users {#manuals:unity}

If you have prior experience with Unity, this guide helps you become productive in Defold quickly. It focuses on essentials and points you to the official Defold manuals whenever deeper details are needed.

## Introduction

Defold is a completely free, truly cross-platform 3D game engine with an Editor for Windows, Linux, and macOS. The full source code is available on [Github](https://github.com/defold/defold/).

Defold is focused on performance, even on low-end devices. Its component-based and data-driven architecture is a bit similar to Unity’s DOTS approach.

Defold is much smaller than Unity. Engine size with empty project is between 1-3 MB on all platforms. You can strip out additional parts of the engine, and move some game content into [Live Update](https://defold.com/llms/manuals/live-update.md) to download separately later. A size comparison and other reasons to choose Defold are described on the [Why Defold webpage](https://defold.com/why/).

To customize Defold to your needs, you can write your own or use existing:

1. Fully scriptable rendering pipeline (render script + materials/shaders) with few backends to choose from (OpenGL, Vulkan, etc.).
2. Code and components as Native Extensions (C++/C#).
3. Editor Scripts and UI widgets to customize Editor.
3. Altered build of the engine and editor, as the full source code and a build pipeline is available.

We also recommend checking out a video by Game From Scratch about [Defold for Unity developers](https://www.youtube.com/watch?v=-3CzCbd4QZ0).

## Welcome screen

Defold greets you with a welcome screen similar to the Unity Hub, where you can open recent projects:

Or start a new one from:
- `Templates` - basic empty projects for quicker setup for a specific platform or genre,
- `Tutorials` - guided learning tours that help you take your first steps,
- `Samples` - official or community-contributed use cases and examples,

When you create your first project and/or open it, it will open in the Defold Editor.

## Hello World

This is a quick way to get something done in Defold quickly, follow the steps, and then get back to read the rest of the manual.

1. Select an empty project from `Templates`, name it in `Title`, choose location and create it by clicking `Create New Project`. It will open in the Defold Editor.

2. On the left side, in the `Assets` pane, open the `main` folder and double click on the `main.collection` to open it.
3. On the right side, in the `Outline` pane right-click on the `Collection` and select `Add Game Object`.

4. Right-click on the created `go` game object and select `Add Component`, and then `Label`.

5. Below, on the left side, in the `Properties` pane type something in the `Text` property.
6. In the main, central scene view, drag, move and drop the label to position around `(480,320,0)`, or change it in `Properties`: `Position`.

7. After changing the label position, save the project by clicking `File` -> `Save All` or shortcut `Ctrl`+`S` (`Cmd`+`S` on Mac).
8. Built your project by clicking `Project` -> `Build` or shortcut `Ctrl`+`B` (`Cmd`+`B` on Mac).

You just build your first project in Defold and should see your text in the window. The concepts of game object and component should be familiar to you. The collections, outline, properties and why we needed to move the label a bit in the top-right direction are explained below.

## Key Concepts

If you generalize enough, the key concepts behind most game engines are very similar. They’re meant to help developers build games more easily, like assembling blocks, while handling complex and platform related tasks on their own.

### Building Blocks

Defold operates with just a few basic building blocks:

For more details, check the full manual about [Defold building blocks](https://defold.com/llms/manuals/building-blocks.md).

### Game Objects
Defold uses **"Game Objects"**, similar to Unity. In both engines, game objects are containers for data with an ID, and they all have transforms: position, rotation, and scale, but in Defold, the transform is built-in rather than a separate component.

You can create parent-child relationships between game objects. In Defold, this can be done only in the Editor inside a "Collection" (explained below) or dynamically in script. Game objects cannot contain other game objects as nested objects the way they can in Unity.

### Components
In both engines, Game Objects can be extended with **"Components"**. Defold provides a minimal set of essential components. There is less distinction between 2D and 3D than in Unity (e.g., colliders), so there are fewer components overall, and some from Unity you may miss.

Read more about [Defold Components here](https://defold.com/llms/manuals/components.md).

The table below presents similar Unity components for quick lookup, with links for each Defold component manual:

| Defold | Unity | Differences |
|---|---|---|
| [Sprite](https://defold.com/llms/manuals/sprite.md) | Sprite Renderer | In Defold, you can change the tint (color property) only via code. |
| [Tilemap](https://defold.com/llms/manuals/tilemap.md) | Tilemap / Grid | Defold has a built-in Tilemap Editor that supports square grids (but there’s an extension for, e.g. [Hexagon](https://github.com/selimanac/defold-hexagon/)) and has no built-in autotiling rules. Tools like [Tiled](https://defold.com/assets/tiled/), [TileSetter](https://defold.com/assets/tilesetter/) or [Sprite Fusion](https://defold.com/assets/spritefusion/) have export to Defold options. |
| [Label](https://defold.com/llms/manuals/label.md) | Text / TextMeshPro | Defold has a [RichText extension](https://defold.com/assets/richtext/) for rich formatting (similar to TextMeshPro). |
| [Sound](https://defold.com/llms/manuals/sound.md) | AudioSource | Defold has only a global sound source (not spatial). There is an official [FMOD extension](https://github.com/defold/extension-fmod) for Defold. |
| [Factory](https://defold.com/llms/manuals/factory.md) | Prefab Instantiate() | In Defold, a Factory is a component with a specific prototype (prefab). |
| [Collection Factory](https://defold.com/llms/manuals/collection-factory.md) | - (No direct component equivalent) | A Collection Factory component in Defold can spawn multiple Game Objects with parent-child relationships at once. |
| [Collision Object](https://defold.com/llms/manuals/physics-object.md) | Rigidbody + Collider | In Defold, physics objects and collision shapes are combined in a single component. |
| [Collision Shapes](https://defold.com/llms/manuals/physics-shapes.md)  | BoxCollider / SphereCollider / CapsuleCollider | In Defold, shapes (box, sphere, capsule) are configured inside the Collision Object component. Both support collision shapes from tilemaps and convex hull data. |
| [Camera](https://defold.com/llms/manuals/camera.md) | Camera | In Unity, the camera has some more built-in rendering and post-processing settings, while Defold delegates it for custom control for user via the render script. |
| [GUI](https://defold.com/llms/manuals/gui.md) | UI Toolkit / Unity UI / uGUI Canvas | Defold GUI is a powerful component for building complete UIs and templates. Unity doesn’t have an equivalent single UI component, rather multiple UI frameworks. Defold has an extension for [Extension](https://github.com/britzl/extension-imgui) too. |
| [GUI Script](https://defold.com/llms/manuals/gui-script.md) | Unity UI / uGUI scripts | Defold GUI can be controlled via GUI scripts using the dedicated `gui` API. |
| [Model](https://defold.com/llms/manuals/model.md) | MeshRenderer + Material | In Defold, a Model component bundles a 3D model file, textures, and a material with shaders. |
| [Mesh](https://defold.com/llms/manuals/mesh.md) | MeshRenderer / MeshFilter / Procedural Mesh | In Defold, Mesh is a component for managing a vertex set via code. It’s similar to a Defold Model, but even more low-level. |
| [ParticleFX](https://defold.com/llms/manuals/particlefx.md) | Particle System | Defold’s particle editor supports 2D/3D particle effects with many properties, and lets you animate them over time using curves in the Curve Editor. It has no Trails or Collisions. |
| [Script](https://defold.com/llms/manuals/script.md) | Script | More details on programming differences explained below. |

#### Extensions and custom components

Defold also has an official [Spine](https://defold.com/llms/manuals/extension-spine.md) and [Rive](https://defold.com/llms/manuals/extension-rive.md) components available via extensions.

You can also create your own [custom Components](https://github.com/defold/extension-simpledata) using Native Extensions, like e.g. this community created [Object Interpolation Component](https://github.com/indiesoftby/defold-object-interpolation).

Some Unity components have no out-of-the-box equivalent in Defold, for example: Audio Listener, Light, Terrain, LineRenderer, TrailRenderer, Cloth or Animator. However, all of this functionality can be implemented in scripts, and there are already solutions available—for example, different lighting pipelines, the Mesh component for generating arbitrary meshes (including terrain), or [Hyper Trails](https://defold.com/assets/hypertrails/) for customizable trail effects. Defold may also add new built-in components in the future, such as lights.

### Resources

Some Components require **"Resources"**, similar to Unity, for example, sprites and models need textures. A few of them are compared in the table below:

| Defold | Unity | Differences |
|---|---|---|
| [Atlas](https://defold.com/llms/manuals/atlas.md) | Sprite Atlas / Texture2D | Defold also has an [extension for Texture Packer](https://defold.com/extension-texturepacker/). |
| [Tile source](https://defold.com/llms/manuals/tilesource.md) | Tile Palette + Asset | In Defold, a tile source can be used as the texture for tilemaps, but also for sprites or particles. |
| [Font](https://defold.com/llms/manuals/font.md) | Font | Used by the Defold Label component or text nodes in GUI, similar to Text/TextMeshPro in Unity. |
| [Material](https://defold.com/llms/manuals/material.md) | Material | In Defold, shaders are named: vertex program and fragment program. |

### Collection vs Scene

In Defold Game Objects and Components can be placed in separate files, like Unity prefabs, or be defined in a combining **"Collection"** file.

A Collection in Defold is essentially a text file with a static scene description. It is **not** a runtime object. It only defines what Game Objects should be instantiated in the game and how parent-child relationships between those objects should be established.

#### Game Worlds

Unity scenes share by default the same global game state and physics simulation, effectively the same *world*. In Defold, you have two options:
1. Instantiate game objects from a single game object file via a `Factory` or a collection file via a `Collection Factory` to a given, instantiated already *world*, like prefabs.
2. Create a separate game *world* at runtime, with its own game objects, physics world, engine operations and addressing namespace via a collection loaded at bootstrap or via a `Collection Proxy` component.

Factories and Proxy components are also explained below.
Read more about Collections in the [Building Blocks manual](/manual/building-blocks/#collections).

## Code Writing

A common pitfall for developers coming from Unity is treating Defold scripts like `MonoBehaviour` and attaching one to *every* game object. While you can definitely write in an object oriented way, there are even libraries to help you with this, the recommended way, especially with many of the same game objects is to use scripts as systems or managers. A single script can control hundreds or thousands of objects and their components, while having no scripts of their own, thanks to powerful addressing and messaging in Defold. Creating a separate script for each object is rarely necessary and can lead to a counterproductive complexity.

An example showing how to utilise Defold script properties, factories, addressing, and messaging to control multiple units can be found [here](https://defold.com/examples/factory/spawn_manager/).

Good manuals on code writing:
- [Script manual](https://defold.com/llms/manuals/script.md)
- [Writing code](/manual/writing-code)
- [Debugging](https://defold.com/llms/manuals/debugging.md)

### Lua

Defold scripts are written in a dynamically typed, multi-paradigm [Lua](https://www.lua.org/) language.

There are few types of Lua scripts: `*.script`, `*.gui_script`, `*.render_script`, `*.editor_script`, and `*.lua` modules.

### Teal

Defold supports the usage of transpilers that emit Lua code, such as [Teal](https://teal-language.org/) - a statically-typed dialect of Lua, but this functionality is more limited and requires additional setup. Details are available in the [Teal Extension Repository](https://github.com/defold/extension-teal).

### C++/C# Native Extensions

In Defold you can write Native Extensions in C++ and C#. If you are very comfortable with C#, it’s technically possible to structure most of your game logic in a C# extension and just call it from a small Lua bootstrap script, though this requires some advanced API knowledge and is not recommended for beginners.

Read more about extensions in [Defold Native Extensions manual](/manual/extensions.md).

### Built-in Code Editor

Defold Editor includes a built-in code editor with code completion, syntax highlighting, quick documentation lookup, linting, and a built-in debugger.

### VS Code and other editors

You can still use your own external editor if you prefer. All Defold components and related files are text based, so you can edit them with any text editor, but you must follow the proper formatting and element structure, since they are Protobuf-based.

If you are used to VS Code and want to use it to write your game’s code, we recommend installing [Defold Kit](https://marketplace.visualstudio.com/items?itemName=astronachos.defold) or [Defold Buddy](https://marketplace.visualstudio.com/items?itemName=mikatuo.vscode-defold-ide) from the Visual Studio Marketplace.

You can also configure Defold Editor preferences to open text files by default in VS Code (or any other external editor). See [Editor Preferences](https://defold.com/llms/manuals/editor-preferences.md) for details.

### Shaders - GLSL

Defold uses GLSL (the OpenGL Shading Language) for shaders - `Vertex Programs` and `Fragment Programs`, similar to Unity. Although Defold doesn’t offer a Shader Graph like Unity (which may be a downside), you can still create equivalent shaders by writing code.

Read more about shaders in the [Shaders manual](https://defold.com/llms/manuals/shader.md).

#### Materials

Defold uses a concept of `Material` that connects `.fp` and `.vp` shaders, samplers (textures) and other things like Vertex Attributes or Constants.

Read more about materials in the [Materials manual](https://defold.com/llms/manuals/material.md).

## Prefabs and instances

Unity can instantiate anything in the Scene statically or dynamically, and Defold can do the same. In Unity you take a Prefab and call `Instantiate(prefab)`. In Defold you have 3 components for instantiating content:

- `Factory` - instantiates a **single Game Object** from a given prototype: a `*.go` file (prefab).
- `Collection Factory` - instantiates a **set of Game Objects** with parent-child relationships from a given prototype: a `*.collection` file.
- `Collection Proxy` - **loads** and instantiates a new *world* from a `*.collection` file.

### Factory

Once you have a `Factory` component defined with its `Prototype` property set to the appropriate Game Object file, spawning is as simple as calling in code:
```lua
factory.create("#my_factory")
```

This uses the address of the component, in this case - a relative path using the identifier `"#my_factory"`.

It returns the identifier of the newly created instance, so if you need to use it later, it’s worth storing it in a variable:
```lua
local new_instance_id = factory.create("#my_factory")
```

Remember that in Defold you don’t need to manually pool objects - the engine itself does pooling internally for you.

Check more details in the [Factory manual](https://defold.com/llms/manuals/factory.md).

### Collection Factory

The difference between `Factory` and `Collection Factory` component is that Collection Factory can spawn **multiple** game objects at once, and define at creation the parent-child relationships as defined in the `*.collection` file.

Such a distinction is not present in Unity, it doesn't have a dedicated concept that matches Defold's Collection Factory. The closest analogy is just a nested Prefab that contains a hierarchy of objects.

It returns a **table** with ids of all spawned instances:
```lua
local spawned_instances = collectionfactory.create("#my_collectionfactory")
```

Check more details in the [Collection Factory manual](https://defold.com/llms/manuals/collection-factory.md).

#### Custom properties of instances

When calling `factory.create()` or `collectionfactory.create()` you can also specify optional parameters such as position, rotation, scale and script properties, so you can control exactly how and where the instance appears, and how it behaves e.g.:
```lua
factory.create("#my_factory", my_position, my_rotation, my_scale, my_properties)
```

#### Dynamic Loading

In both `Factory` and `Collection Factory` components you can mark a Prototype for dynamic resource loading so that its heavy assets are only pulled into memory when needed, and unloaded when they’re no longer used.

Check more details in the [Resource Management manual](https://defold.com/llms/manuals/resource.md).

### Collection Proxy

The `Collection Proxy` refers to a specific `*.collection` file, but instead of injecting the objects into the *current world* (like factories), it **loads and instantiates a new game world**. This is somewhat similar to loading an entire scene in Unity, but with stricter separation.

In Unity you might load an additive scene like this:
```c#
SceneManager.LoadSceneAsync("Level2", LoadSceneMode.Additive);
```

In Defold you load the new collection just by sending a message to the `Collection Proxy` component:
```lua
msg.post("#myproxy", "load")
```

1. When you send the proxy a message `"load"` (or `"async_load"` for asynchronous loading), the engine allocates a new world, instantiates everything in that collection there, and keeps it isolated.
2. Once loaded, the proxy sends back a `"proxy_loaded"` message indicating the world is ready.
3. You then typically send `"init"` and `"enable"` messages so the objects in that new world begin their normal lifecycle.

To communicate between the loaded worlds, you have to use explicit messaging with URLs that include the world name (`collection:`, the first part of the URL).

This isolation can be a huge advantage when implementing level transitions, mini-games, or large modular systems, because it prevents unintended interactions, and also allows separate control over update timing if needed (e.g. for pause or slow motion).

If you’ve ever used multiple scenes in Unity and needed them to behave independently, think of a `Collection Proxy` as a way to bring that concept directly into Defold.

Check more details in the [Collection Proxy manual](https://defold.com/llms/manuals/collection-proxy.md).

## GUI

Defold’s GUI is a whole single dedicated framework for User Interfaces - menus, overlays, dialogs, and other elements, similar to UI Toolkit or uGUI with Canvas.

GUI is a Component, and is separate from Game Objects and Collections. Instead of Game Objects, you work with GUI nodes arranged in a hierarchy, driven by a GUI script.

### GUI Nodes

When you open a `*.gui` component file in Defold, you are presented with canvas where you place `"GUI nodes"`. These are the building blocks of the GUI. You can add GUI nodes of type:

- Box (rectangular shape with a texture)
- Text (with any font)
- Pie (radial fill pie-slice element with a texture)
- ParticleFX
- Template (another whole nested `.gui` file, like a GUI prefab)
- and Spine node, when using Spine extension.

### GUI Script

GUI component have a special property for GUI scripts - you assign one `*.gui_script` file per component and it allows to modify the behaviour of the component, so it's very similar to regular scripts, except it doesn’t use the `go.*` namespace (which is for game object scripts). Instead, it uses a special `gui.*` namespace API that only works inside GUI scripts (`*.gui_script`). You can think of it like a separate Scene. Unity UI (uGUI) with Canvas.

### GUI Rendering

GUI elements are rendered independently of the game camera, typically in screen-space, but this behavior can be changed in custom rendering pipelines.

For further details read the [GUI Manual](https://defold.com/llms/manuals/gui.md).

## Where are Sorting Layers?

This is a very common Unity migration confusion.

GUI components have `Layers` and this works almost the same as "Sorting Layers" in Unity, but for other components, like `Sprites`, `Tilemaps`, `Models`, etc, there is no direct equivalent.

Instead, you typically combine:
- Fine ordering via Z axis when using a default camera or depth when using a Camera component.
- Coarse ordering via the render script using render predicates - to select what to draw by material tags.

But you shouldn’t mimic Unity Sorting Layers with lots of tags, because in Defold, tags are a render-level mechanism. Overusing them can break batching and raise draw overhead.

---

## Where to go from here?

- [Defold examples](https://defold.com/examples)
- [Tutorials](/tutorials)
- [Manuals](/manuals)
- [API References](https://defold.com/ref/go)
- [FAQ](https://defold.com/faq/faq)

If you have questions or get stuck, the [Defold Forum](//forum.defold.com) or [Discord](https://defold.com/discord/) are great places to reach out for help.