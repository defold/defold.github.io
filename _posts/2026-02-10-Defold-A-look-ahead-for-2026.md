---
layout: post
title:  A look ahead for 2026
excerpt: This article outlines our plans for Defold.
author: The Defold Foundation
tags: ["roadmap"]
---

One of the most common questions we get is: “What’s next for Defold?”

We understand why: having a sense of direction helps teams plan ahead.

At the same time, building a game engine and editor means operating in a constantly shifting environment: platforms change their requirements, sometimes new opportunities appear, and sometimes some work turns out to be more complex than expected, while other work becomes more valuable and needed than we anticipated. That’s why we’ve repeated this many times over the years: a roadmap we present is just a plan, not a contract.

Nevertheless, we’d like to share a near-term snapshot of the areas we’re actively aiming to push forward over the coming quarters:

## Productivity and customised Editor workflows

A major theme for us is making Defold faster and more pleasant to use in real production. Especially when your project gets large, your content pipeline grows, or your team needs repeatable workflows.

Over the past period, we’ve steadily expanded editor scripting, first with interactive UI creation, and more recently with deeper scene-editing capabilities. The next step is to build on that foundation and **continue improving the day-to-day editor experience**, so we’ll be continuing to expand what you can automate and build inside the editor. We are very happy that the community is using and sharing a lot of useful Editor Scripts with some clever and inspiring ideas.

Therefore, we would like to allow users to add [custom images inside Editor UIs](https://github.com/defold/defold/issues/10220), so tools can become more visual and domain-specific - think custom icons, previews, and richer widgets.

We also plan to add [non-modal panels](https://github.com/defold/defold/issues/11671) created by editor scripts, so tool UIs can live alongside the editor (similar to other editor panes), instead of being limited to blocking dialogs. This might unlock better tools, like inspectors, guided workflows, interactive tutorials, and other kinds of “mini-editors” tailored to a project.

We’re also genuinely happy to see how the community is already using editor scripts in clever ways. A standout example was the [Asset Store](https://forum.defold.com/t/defold-in-editor-asset-store/81969) built by Insality using Editor scripts and UI. and we would like at some point to incorporate such a powerful asset browser into the Editor in some way. Longer term, ideas like this are exactly the kind of experimentation that can inspire improvements to the core editor experience.

We would also like to start changing how the Editor handles history and allow for **local undo** as a dedicated next step.

## Editor performance and size

A major theme for us is making Defold Editor faster to use in real game development projects, especially when your project gets large, your content pipeline grows, or your team needs repeatable workflows.

We’ve already made several fixes and changes in different areas, resulting in multiple improvements for loading time, responsiveness, and performance. Our partners are developing impressive games that are huge in terms of scope, help us focus on the performance for real projects, and we’d also like to improve the Editor for 3D projects. We already improved performance for handling huge 3D scenes in the Editor or scenes with many 3D models, and we’ll continue to make further improvements.

Defold has always cared about performance, stability, and staying lean. One concrete focus area is engine size optimizations, including reducing the shipped footprint by nulling out unused components where possible. This also aligns with our continued push toward better modularization.

We’re also planning to improve controller behavior across devices by integrating the **SDL gamepad database** to help normalize and recognize controllers more consistently across platforms.

## Further improvements for 3D

For 3D projects specifically, we want to keep reducing friction in scene authoring. On top of the other UI and UX improvements we made to the Editor for 3D projects, like Grid settings, camera component, and its frustum preview improvements, one of the closest examples is a new [Free Fly camera](https://github.com/defold/defold/issues/11185#issue-3380495023) in the Editor that we work on.

On the boundary between 3D and physics, we want to make collision authoring more flexible by allowing **any model to be used as a collision shape**, removing common pipeline friction when bringing complex geometry into Defold.

We’re also exploring a 3D multi-instance component aimed to improve performance with repeated scene elements such as vegetation, rocks, props, and other repeated scene elements. We think it can unlock meaningful performance and workflow wins.

## 3D Animations

We’ve seen increasing demand for richer animation workflows and more capable 3D features. Our approach remains focused on improving what matters most in production.

On animation, we’re targeting [morph targets and animation mixing](https://github.com/defold/defold/issues/8024), which are both foundational pieces for more expressive characters and smoother transitions between states.

## New Light component and rendering works

Lighting is one of the most requested building blocks for developers working in 3D, and it’s also an area where the community has filled gaps with impressive extensions and solutions over time. 

We’re planning to add a **new Light component** and supporting shader pipeline improvements. The intent is to make modern rendering workflows easier to set up and more consistent—especially in combination with existing rendering solutions and extensions.

We plan to allow the **PBR extension to use more built-in features** and make it feel easier to set up for the developers.

We also have in plans a continued **Metal-related work** to keep Apple platform support strong and future-proof. Defold has invested in modern graphics backends for years, and we’ll keep that momentum going.

## Extensions: Rive 2.0 and Photon Fusion

Extensions remain a core part of Defold’s strategy of keeping the engine focused, while enabling powerful opt-in integrations where they make sense.

Rive is a great example of that approach. The Foundation partnered with Rive early to bring real-time animation workflows to Defold, and it was one of the first game engines to support Rive. We’ve continued to update and improve the integration over time. In the meantime, Rive got so much traction that we were having trouble keeping our extension up to date with their new features and improvements. We did however do some work to change the approach for this extension that will allow us to keep up with the pace of Rive updates better, because it delegates more to the Rive renderer itself. We want to move the integration forward with **Rive 2.0** support.

We also want to reduce the friction for developers shipping multiplayer games. Last year we announced an official Photon Realtime integration, and we’ll continue investing in making networking more accessible in Defold projects. For the upcoming period, our intent is to **work toward a seamless netcode solution**, and we’ll communicate specifics when we’re confident we can do so responsibly.

## New platforms: Microsoft Xbox

In earlier roadmap communication, we described Xbox as something we wanted to add, and we continue to treat it as an important platform goal. We’ve been working on Xbox support for quite some time and added core features already, and we’re closer than ever to finalizing the work on supporting the platform, but bear in mind it is work being sponsored by the Defold Foundation only, and therefore, its pace is simply slow.

## Tutorials and examples

We know our tutorials and examples haven’t received the attention they deserve for some time, so we’re now investing steadily in improving onboarding and learning resources. This work has already started and includes refreshing and verifying our existing manuals, expanding the defold.com/examples collection with more practical, bite-sized projects, and adding new guides that help developers ramp up faster. A recent step in this direction is the [Defold for Unity users manual](https://defold.com/manuals/unity/), and we plan to create a similar manual for Godot users, and potentially later for GameMaker users, so that developers coming from other engines can more easily map familiar concepts to Defold and start building confidently.

We’ll also be organising new Community Challenges—like the current [Break it!](https://forum.defold.com/t/community-challenge-5-break-it/82303), which revolves around physics—as well as a Defold game jam, which we’ll start sharing more information about soon. We’re incredibly proud of our community: always eager to help others, share knowledge, and showcase interesting projects. Keeping things lighthearted, welcoming, and engaging is important to us, and we’re happy to have you with us on this journey!

## Future is bright!

We still have more great news to share, but you’ll have to wait just a little longer. As always, please keep in mind that everything outlined above reflects our current focus and intentions, not a set of promises. The priorities may shift, but with that said, we’re genuinely excited about what’s ahead, and we believe the future of Defold looks bright.