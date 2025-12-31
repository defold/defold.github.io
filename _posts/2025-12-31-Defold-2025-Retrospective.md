---
layout: post
title:  Defold in 2025 - A Year in Review
excerpt: Another year has gone by, and it’s time to reflect on the events and highlights of Defold in 2025.
author: Paweł Jarosz
tags: ["retrospective", "news"]
---

# Defold in 2025 --- A year in Review

Another year has gone by, and it’s time to reflect on the events and highlights of Defold in 2025. 

First of all, we want to thank our amazing and growing community! Many of the improvements delivered in 2025 were possible thanks to our community contributors, and we are genuinely grateful for the time, feedback, bug reports, pull requests, extensions, and examples you shared. And we want to thank our partners that made it possible for Defold to evolve this year and the Defold team to grow.

![Defold 2025 Retrospective](/images/posts/defold-2025-retrospective/header.png)

We maintained a steady release cadence throughout the year, aiming for (almost) monthly releases with a ~2 weeks of beta period for each. This predictable schedule helps ensure each release brings meaningful features, improvements, and fixes, while giving the community time to catch issues early during the beta window. To everyone who tested betas and provided feedback: thank you! Your help was essential to making 2025 another successful year for Defold.

## Breaking Changes

In keeping with our philosophy, we strive to avoid breaking changes unless absolutely necessary. A couple of updates in 2025 did however introduce breaking changes, but they were minor and affected only specific areas. We want to apologize if it caused any inconvenience.

### Box2D version 3

We upgraded the built-in physics engine to [Box2D version 3](https://defold.com/2025/04/14/Defold-1-10-0/). To make adoption safe and gradual, we shipped Box2D 3 as an optional feature, so developers can opt in via an app manifest and test their projects with the new physics. It behaves similarly in most cases, but due to internal changes, you may notice subtle differences in collision reporting or require minor tuning of physics settings. We plan to make Box2D 3 the default in the near future once we iron out all remaining edge cases, as it was almost a rewrite from scratch.

### Removal of Scale Along Z

We [removed the “scale along Z”](https://defold.com/2025/09/08/Defold-1-11-0/) feature to simplify the engine and avoid confusion. This was a long-overdue cleanup, because it required changes in users' projects in some cases, but we needed to do so.

There were some other small fixes that could be breaking in certain situations (e.g. [passing nil to go.delete() now throws an error](https://defold.com/2025/05/12/Defold-1-10-1/) or a [fix for sys.load() for corrupt files](https://defold.com/2025/07/07/Defold-1-10-3/)) and there were some other breaking changes that [affected only Native Extensions](https://defold.com/2025/05/12/Defold-1-10-1/). As always, we communicated breaking changes clearly in release notes and worked to ensure migrations were as smooth as possible.

## Releases

The 10 Defold releases in 2025 included dozens of new features and hundreds of fixes and tweaks. We decided to publish the 11th release in a few days, so it will be technically in 2026, but we cover some of its most important features in this retrospective too.

| Month | Version |
|---|---|
| February | (1.9.7)[https://forum.defold.com/t/defold-1-9-7-has-been-released/79650] |
| March | (1.9.8)[https://forum.defold.com/t/defold-1-9-8-has-been-released/80012] |
| April | (1.10.0)[https://forum.defold.com/t/defold-1-10-0-has-been-released/80264] |
| May | (1.10.1)[https://forum.defold.com/t/defold-1-10-1-has-been-released/80481] |
| June | (1.10.2)[https://forum.defold.com/t/defold-1-10-2-has-been-released/80687] |
| July | (1.10.3)[https://forum.defold.com/t/defold-1-10-3-has-been-released/80882] |
| August | (1.10.4)[https://forum.defold.com/t/defold-1-10-4-has-been-released/81160] |
| September | (1.11.0)[https://forum.defold.com/t/defold-1-11-0-has-been-released/81515] |
| October | (1.11.1)[https://forum.defold.com/t/defold-1-11-1-has-been-released/81704] |
| November | (1.11.2)[https://forum.defold.com/t/defold-1-11-2-has-been-released/81884] |

## Rendering and 3D support

We continued moving Defold’s rendering architecture forward with the goal of improving GPU utilization and enabling stronger 3D support. We aim to provide better 3D support and significantly improve GPU usage. We are obviously not moving away from 2D support, but it doesn’t change the fact that we are very happy that more and more devs started making 3D projects in Defold in 2025.

A key step was the shader pipeline refactor. Defold now uses a [single combined shader resource](https://github.com/defold/defold/pull/10097) per program, allowing multiple materials to share the same underlying program and reducing memory usage.

Later releases expanded the new pipeline with [shader resource merging](https://github.com/defold/defold/pull/10351) across stages and automatic remapping of vertex outputs to fragment inputs, improving correctness on non-OpenGL backends.

The Vulkan backend has now [improved performance for texture uploads](https://github.com/defold/defold/pull/11180) and few other fixes and clean ups.

We added support for [structs in uniforms](https://github.com/defold/defold/pull/9680), which is a small addition, yet allows for some fine grained, cleaner and more scalable shader implementations. We also added helpful rendering-adjacent APIs and runtime capabilities, including [model AABB queries](https://github.com/defold/defold/pull/9946), [dynamic GUI textures](https://github.com/defold/defold/pull/10823) and [improved web viewport behaviour](https://github.com/defold/defold/pull/10794).

### GPU Skinning

We expanded GPU-driven rendering capabilities, including [GPU skinning](https://github.com/defold/defold/pull/9983) for model animations. Model components can be rendered with vertex shaders that perform skinning on the GPU, freeing the CPU from animation work and improving performance for animated characters and complex scenes.

![GPU skinning](/images/posts/defold-2025-retrospective/gpu_skinning.png)

To complement this, we added an [option to disable the creation of game objects for each skeleton bone](https://github.com/defold/defold/pull/10885), that allows reducing overhead when instancing animated models and enabling much larger crowds of animated entities. Combined with the model instancing capability introduced earlier (allowing many copies of a mesh to be drawn efficiently), Defold’s 3D rendering stack can now handle significantly more content per frame.

## Xbox support

We made significant progress toward bringing Xbox support to Defold, we shipped [initial work on a DirectX 12 adapter](https://github.com/defold/defold/pull/10100) and added [Wasapi sound backend](https://github.com/defold/defold/pull/9456) to support future Xbox-related efforts, but had to pause work mid-year due to team capacity constraints. The good news is that development will resume soon, and we are well-positioned to finish and announce official Xbox support next year.

## Platforms

We kept all platform SDKs up to date. These updates are routine but crucial. They ensure that Defold apps meet Google’s and Apple’s latest requirements and can take advantage of new OS features.

## Live Update

We continued expanding what can be excluded from the initial build and downloaded later – either as optional content, a patch, or a post-install update, allowing developers to reduce initial download size and ship updates more efficiently.

To support this, we added the ability for more components (now [sounds](https://github.com/defold/defold/pull/9969), [fonts](https://github.com/defold/defold/pull/10627), [GUI](https://github.com/defold/defold/pull/10631), [textures](https://github.com/defold/defold/pull/10547)) to define their resources at runtime and, where appropriate, create those resources. Live Update was also extended with support for [ZIP files and folders](https://github.com/defold/defold/pull/9910), simplifying how projects can structure and deliver updates.

We also created [Play Assets Delivery extension](https://defold.com/extension-pad/), letting developers ship large or optional content as Google Play hosted asset packs instead of relying on a separate CDN. PAD supports install-time, fast-follow, and on-demand delivery modes, and asset packs can be used to distribute Live Update ZIP archives or individual files.

## Fonts

Signed-distance field (SDF) fonts can now also be [generated at runtime](https://github.com/defold/defold/pull/10627). This is especially useful for games that download fonts or support multiple locales dynamically – you can now create high-quality text on the fly.

![Fonts](/images/posts/defold-2025-retrospective/fonts.png)

In late 2025 we also took a major step toward proper international typography by introducing runtime Unicode [Text Shaping](https://github.com/defold/defold/pull/11014), including right-to-left (RTL) layout, correct kerning pairs, and ligatures. The feature ships together with a revamped runtime font workflow and Font Collections, so a single font resource can dynamically associate multiple .ttf files per locale, and you can prewarm the glyph cache asynchronously to ensure shaped text is ready before it appears on screen.

## Sound

We added the ability to [create sound data at runtime](https://github.com/defold/defold/pull/9969) and “sound” property, making it possible to assign and play audio assets that were downloaded via Live Update, and some new options for playing sounds, like [start_time and start_frame](https://github.com/defold/defold/pull/11239).

We also added powerful [Sound Streaming](https://defold.com/manuals/sound-streaming/), allowing audio to be loaded and played in chunks instead of being fully loaded into memory up front. It’s useful both for reducing runtime memory usage and for scenarios where audio content is delivered dynamically (for example, streamed from an HTTP URL to avoid an initial download and enable updates on the server side).

## Camera

In 2025 we made the Camera component more predictable and production-friendly – both in runtime behavior and in the Editor workflow. [Camera is now taking precedence](https://github.com/defold/defold/pull/9847) in the default render script.

We also improved the Scene View navigation including smarter zooming behaviour ([zooming towards the cursor in 2D mode](https://github.com/defold/defold/pull/10200)), making day-to-day scene navigation faster and refined the editor’s orthographic camera UX so what you see is what you get: correct gizmo sizing based on display dimensions and zoom, sensible property disabling in orthographic mode, validation of zoom values, and a pixel-stable camera icon.

![](/images/posts/defold-2025-retrospective/camera.png)

We revamped the [camera aspect-ratio APIs](](https://github.com/defold/defold/pull/11077)) so they finally reflect what developers expect. We also have functions to [convert between world and screen coordinates](https://github.com/defold/defold/pull/11403) or to [set orthographic zoom](https://github.com/defold/defold/pull/10624).

Orthographic cameras got also a major upgrade with [orthographic projection modes](https://forum.defold.com/t/defold-1-11-1-has-been-released/81704): Fixed, Auto Fit (contain), and Auto Cover (zoom) – including editor support and dedicated Lua APIs.

## Editor

The Defold Editor received a lot of attention in 2025, continuing our focus on workflow, usability, and extensibility.

### Performance and Quality of Life

We added several User Experience and Quality of Life improvements, including better [grid configuration](https://forum.defold.com/t/defold-1-10-4-has-been-released/81160), expanded drag-and-drop workflows, color picker improvements, curve color enhancements, build cancellation, and more.

We also improved atlas and GUI workflows and performance – particularly for projects with large numbers of GUI nodes – while reducing memory usage in key scenarios. Recent changes also significantly improved editor performance when [working with scenes containing many large 3D models](https://github.com/defold/defold/pull/11508) and we will continue to improve the performance in the next year.

### Customizability - Editor Scripts and UI

We continued pushing the Editor in the direction of customization and tooling. Editor Scripts and UI capabilities were expanded and enabled in more contexts ([Project, Debug](https://github.com/defold/defold/pull/10494) and [Scene](https://github.com/defold/defold/pull/10263)), have [HTTP server routes](https://github.com/defold/defold/pull/10314). With Editor Scripts we can edit ParticleFX emitters and modifiers, GUI ParticleFX, GUI nodes, layers, layouts and fonts, tilesource animations, tilemaps, collision groups, collision shapes, collections and game objects and even game.project and many more properties. We can also unpack ZIPs in editor scripts. And the community has already created impressive productivity tools on top of these APIs.

![](/images/posts/defold-2025-retrospective/editor_ui.png)

### Templates

We also enabled [templates](https://github.com/defold/defold/pull/9854) for newly created files of a given type, allowing teams to improve setup speed and standardize project conventions.

The editor continues to grow stronger for smoother, more customizable development and we have more planned for 2026.

## Languages

In 2025 we experimented with both C# and Teal support for Defold, both in two different approaches.

### Teal support

Perhaps the biggest boost for scripting in Defold was the leap towards first-class Teal support. The updated [Teal extension](https://github.com/defold/extension-teal) released in September integrates a Teal language server for real-time type checking and auto-completion. As you write scripts in Teal, the editor can highlight type issues, offer completions and documentation, and format Teal code on the fly.

### C# support

In 2025 we also announced [experimental C# support](https://forum.defold.com/t/defold-c-support/79479) for Defold, aimed primarily at studios with existing, battle-tested C# codebases who want a more realistic migration path to Defold. To be clear, it’s not scripting, C# can be used in the same “low-level” way as C/C++ to build native extensions or even game logic, compiled via the build server. We are interested however, if there will be more interest to use C# in Defold.

## Web

Our partnership with [Poki](https://defold.com/2025/04/25/Defold-Foundation-And-Poki-Integration/) has made web game development with Defold smoother than ever. Defold developers can now bundle and publish their games to Poki with [a single click from the editor](https://forum.defold.com/t/defold-x-poki-integration/80349).

We also created an official Poki SDK template for new Defold projects, so key platform features (such as ad pausing, progress saving, and other Poki APIs) are available out of the box. By lowering the barrier to entry, we hope more Defold developers will bring their games to web portals—and that more web game developers will discover Defold’s performance and workflow. This work also came with a substantial set of performance and memory improvements for HTML5 builds.

### Web GPU

We also made significant progress toward next-generation web graphics with [WebGPU](https://github.com/defold/defold/pull/9951). Defold’s HTML5 builds have traditionally used WebGL, but this year we added experimental WebGPU support as an optional graphics backend. You can enable WebGPU via project settings or an app manifest. Early results are promising, particularly in performance-sensitive content. We expect WebGPU support to mature further in 2026 as browser support expands and the ecosystem stabilizes.

## Extensions

Defold is built around a rich ecosystem of native extensions, and 2025 was another fruitful year for extending the engine’s capabilities. We actively maintain a set of official extensions and welcome several important improvements and additions.

### Photon Realtime

We teamed up with Exit Games to create a [Photon Realtime extension](https://defold.com/2025/08/14/Photon-Realtime-Available-For-Defold/) for Defold, making it easier to add multiplayer features to games. Photon Realtime handles matchmaking, real-time communication, and room management. With the extension, developers can access Photon services through a straightforward Lua API.

![](/images/posts/defold-2025-retrospective/photon.png)

### Spine

With [Spine Extension 4.0.0](https://forum.defold.com/t/spine-extension-4-0-0/81483) bringing **multi-track support** for GUI Spine nodes, blending, mixing, enabling layered animations, and so on, it is now much easier to maintain complex character rigs and UI animation workflows.

GUI Spine callbacks now receive both animation completion and Spine events, allowing richer event-driven workflows directly from Spine timelines.

It’s now possible to create spine_scene resources at runtime using resource.create_spinescene(), making it easier to generate or swap Spine content dynamically.

We also added better control over animation blending via **mix blend settings** per track, new physics helper functions for translating/rotating Spine physics, and improved editor-script support, so tooling can programmatically edit GUI Spine scenes and nodes. Finally, runtime character customisation got stronger with APIs for mixing/copying/clearing skins, and several stability and workflow fixes.

### Rive

Last but not least, we updated the [Rive Extension](https://github.com/defold/extension-rive) to use Rive’s newer high-performance renderer on all supported platforms. We shipped an [Autobind](https://github.com/defold/extension-rive/releases/tag/8.2.0) option in the editor (enabled by default) for automatically binding the default view model, updated build scripts, and moved the previously hardcoded blit setup into an explicit asset. We also focused on correctness across modern render backends.

Rive continues to evolve quickly, and we’re proud of the improvements and new features it brings to Defold-powered UI and animation workflows. We did some rework on our side and plan to catch up with additional Rive features next year.

### Other extensions

We also improved the Firebase extension to keep pace with SDK changes. The AdMob extension was updated, our Facebook Instant Games extension received a patch, and on the analytics side we integrated newer SDK versions for GameAnalytics.

We also made a fork of community [FMOD extension](https://github.com/dapetcu21/defold-fmod) and created the[official Defold FMOD extension](https://github.com/defold/extension-fmod) out of it - updated to work with FMOD 2.03.09 and it works on more platforms, there’s still some work to be done, but it’s getting closer.

## Community

Defold’s philosophy is to keep the core engine lean and let developers opt in to the features they need through extensions. The community has truly embraced this approach. Many extensions, tools, and improvements were built or improved through community contributions, and we want to thank everyone who created or maintained Defold extensions in 2025.

We also continue to be amazed by the games our community releases each year. 2025 was no exception – a steady stream of Defold-powered games launched across PC, consoles, web, and mobile. More than ever, developers chose to share their releases with us, and we’ll wrap up many of them in our [yearly showreel](https://forum.defold.com/t/defold-showreel-2025-call-for-videos/82028).

We are also proud of one of our flagship Defold titles: **Family Island**. It remains a major success and continues to be supported and updated by our partner MoonActive. This partnership pushes Defold hard in real production conditions and helps us deliver top performance and stability – particularly on mobile and in editor workflows.

In June, we collaborated with **CrazyGames** to host a weekend-long [CrazyGames x Defold Web Jam](https://forum.defold.com/t/join-the-crazygames-x-defold-web-jam/80578) focused on HTML5 games. We love partnering with platforms to showcase what Defold can do – expect more of these events in the future, as they are a great way to grow the community and highlight web development strengths.

There was also the annual community [Made With Defold Jam](https://forum.defold.com/t/madewithdefold-jam-2025/80624), with lots of games and discussion around Defold and game development. The theme was **“Twist on a Classic,”** and participants certainly delivered. We’ve [brought the jam’s organizer onto our team](https://forum.defold.com/t/pawel-jarosz-joins-the-defold-team/81840), so next year it will become the official Defold Jam – and we plan to make it bigger than ever.

## What’s next?

Defold has come a long way, and we didn’t even properly celebrate its 5-year anniversary of becoming source-available. Yes, Defold was first released in 2015 and its source code was released publicly in 2020!

If you want to, you can always [contribute to Defold](https://defold.com/contribute/) or [support Defold](https://defold.com/donate/), we really appreciate your help!

Time flies, but even though we ship Defold in frequent, incremental, but usually small and not so shouting steps, a retrospective makes it clear how much work and care went into the engine and its ecosystem.

We will mainly focus on further Editor customisation options with Editor Scripts and UI and Editor performance, better rendering and 3D support (animations, physics), Xbox platform, engine size optimisations and further modularization, new extensions and many more! Stay tuned for 2026 - there’s a lot ahead!
