---
layout: post
title:  Working with both public and private repos
excerpt: We'll explain a bit about how we maintain both a public repository as well as several private ones in order to comply with agreements from different vendors.
author: Mathias Westerdahl
tags: ["code", "engine", "repos", "github"]
---

# The need for privacy

The Defold game engine is maintained by the Defold Foundation, and it's [code is available on GitHub](https://github.com/defold/defold) under a permissive source-availablelicense and is available for anyone to use. It supports the common major platforms for desktop, mobile and web platforms.

Knowing we also wanted to have console support, we had to figure out how to work with our public source code and at the same time work with vendor specific code.

To work with certain partners, you have to enter written agreements to not share implementation details with the public, which of course affects what may or may not be visible in the public facing code.

# Different approaches

Depending on your resources the approach may vary. There are problably other companies out there that do variations of this here

In our case, we have a small team of 6 people so we need to minimize the time spent on maintaining code.


Source code access for registered developers

We currently have 3 private repos for our console support, but it may grow if we enter other agreements with new partners.

Working with a small team of 6 people, we need to make it as easy as possible for us to maintain these codebases.


### Implementation details

First and foremost, the

Also, none of the vendors want to be singled out when it comes to implementation details.


The vendors we currently work with support the standard C and C++ libraries.
Often they have their own custom toolchains to produce object files and

## Our current guidelines

### Platform names in files + directorys
