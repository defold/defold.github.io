---
layout: post
title:  Defold Newsletter 40
excerpt: Things have slowed down somewhat since the very busy launch of the Defold Foundation but we still have some exciting things to share.
author: Björn Ritzl
---

Hello, Defolder! 👋

Things have slowed down somewhat since the very busy launch of the Defold Foundation but we still have some exciting things to share!

## Games
### Zoo Economy
Zoo economy is a strategy-puzzle game where you exchange animals. Animals are your currency. Complete historic based story missions or play in a sandbox. Get animals, breed them, attract visitors, sponsor expeditions for unique animals, upgrade your zoo and much more. [LEARN MORE](https://forum.defold.com/t/zoo-economy-strategy-puzzle/65466)

## The Defold Foundation is awarded a grant from Grant for the Web
The Defold Foundation has been awarded a grant from Grant for the Web to explore the use of Web Monetization in games. The Defold Foundation will use the grant to integrate, promote and support the use of Web Monetization in web games created using Defold. The Defold Foundation will integrate Web Monetization through its plugin system, promote it through examples and tutorials and host a game jam focused on Web Monetization. [LEARN MORE](https://defold.com/2020/06/09/Defold-is-awarded-a-grant-from-Grant-for-the-Web/)


## Support the Defold Foundation
The foundation invites individuals and teams of developers to support Defold development through one-time or recurring donations. Depending on the size of your contribution you get access to a number of different rewards and benefits.

We thank our latest supporters:

* Grify
* oleg4442
* parke


## Defold 1.2.170

#### Engine
* Issue-3381 - Added: Added support for Android App Bundles
* Issue-3189 - Added: Added support for physics scaling
* Issue-4845 - Fixed: Don’t render while iconified
* Issue-3181 - Fixed: Refactor handling 9 slice gui node with no texture.
* Issue-4830 - Fixed: Add all keys input binding to builtins.
* Issue-4873 - Fixed: Added helpful information to script templates
* Issue-4710 - Fixed: physics.raycast now can return all results
* Issue-3315 - Fixed: Fix label rotation
* Issue-4821 - Fixed: Respect texture-compression setting when creating app bundle.
* Issue-3342 - Fixed: Fixed parsing issue with go.property(…) with regards to spaces
* Issue-4831 - Fixed: Pass nil to window.set_listener() to unsubscribe
* Issue-4849 - Fixed: NE: Remove GraphicsAdapterOpenGL symbol when linking headless builds
* Issue-1848 - Fixed: Fixed inconsistency between setting (0,0,0) and (0) as scale in factory create
* Issue-4784 - Fixed: Handle display cutout in immersive mode
* Issue-4775 - Fixed: Don’t try to get the animation frame index if no animation is set
* Issue-4901 - Fixed: Fixed issue of uploading font vertex buffer multiple times

#### Editor
* Issue-4821 - Fixed: Add texture compression option to bundle dialog.
* Issue-4844 - Fixed: Added donate link to the editor help menu
* PR #4800 - Fixed: Specify exact JDK version to download
* PR #4813 - Fixed: Fix misplaced docstrings in the editor code

#### Defold source
* Issue-4803 - Fixed: Update to Emscripten 1.39.16
* Issue-4827 - Fixed: Package path can now point to a local§ folder
* Issue-4815 - Fixed: Detect missing sdk before engine build
* Issue-4822 - Fixed: Updated engine to use MSVC 2019
* Issue-4640 - Fixed: Added support to build/package our external libraries using waf
* Issue-4817 - Fixed: Updated the engine coding guidelines
* Issue-4640 - Fixed: Added script to build external packages using our build system
