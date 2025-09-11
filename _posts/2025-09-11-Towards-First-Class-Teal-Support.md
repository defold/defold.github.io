---
layout: post
title:  Towards First-Class Teal Support
excerpt: We made a big step towards a first-class Teal support
author: Vladislav Protsenko
tags: ["news", "teal"]
---

We are happy to announce the [release of Teal extension v1.4](https://github.com/defold/extension-teal/releases/tag/v1.4) for Defold! Defold uses Lua for scripting and integrates with the [excellent Lua language server](https://luals.github.io/), which supports type annotations and warns you about potential type issues during development. However, these annotations in the Lua language server are only warnings and do not enforce type safety. For developers who require robust, project-wide type checking, there is the [Teal](https://teal-language.org/) language — a statically-typed, minimalistic, and pragmatic dialect of Lua.

Until now, Defold's Teal integration was quite basic: it could only compile Teal files to Lua and otherwise treated them as plain text. With this new release, Teal support in Defold has improved dramatically:
- The Teal extension now provides syntax formatting.
- It also bundles a Teal language server, enabling code completion and other features.

Demo:

<video controls style="width: 100%">
  <source src="https://github.com/user-attachments/assets/dceed97a-ac84-4f99-ad27-357a5053ba6c" type="video/mp4">
  Your browser does not support the video tag.
</video>

What's next for Teal support (no ETA yet, but these features are planned):
- Debugger support (breakpoints)
- Type annotations for Defold Lua runtime APIs