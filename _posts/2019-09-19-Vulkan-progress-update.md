---
layout: post
title:  Vulkan progress update
excerpt: We built a proof-of-concept this spring and it is now being reworked into a stable version
author: Jhonny Göransson
type: blog
---

Defold is quite a deterministic engine where more or less everything about a game is known up front. Materials, textures, meshes and other engine resources are compiled into our own formats and very little (if any) is generated ad-hoc, which makes Defold a very good fit for Vulkan. We don't rely that much on device extensions (except for maintenance1) or any shader modules other than vertex and fragment. Since the current rendering API is based on OpenGL 2.1 to target as many of the low-end devices as possible the first iteration on Vulkan will not introduce anything new in terms of rendering features to our users. On the other hand, we drive all rendering by user-authored rendering scripts that configure the rendering pipeline on a per frame basis, which means that we must take into account that things can change quite a lot between two frames. The rendering script is a slight abstraction on top of the OpenGL API, with functions to change a single render state, disabling texture units, setting the framebuffer and so on. One of the more challenging aspects for us is to maintain the script API and somehow mangle the Vulkan conststructs into an OpenGL centric architecture while not draining performance or waste memory.

At least that's step one, and where we are currently in development. Going forward, we would like to overhaul the render scripts and make a completely new API based around more modern rendering constructs, but first step is to add Vulkan on top of what we have now. We built a proof-of-concept this spring that is now being reworked into a stable version, which is going quite well :)

If there's any questions about our implementation please let us know!
