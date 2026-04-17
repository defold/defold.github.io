---
brief: This guide shows how to build a simple multiplayer game/application using the Photon Fusion extension for Defold.
github: https://github.com/defold/extension-photon-fusion
layout: manual
locale: en
title: Photon Fusion - Quick Start Guide
toc:
- Introduction
- Step 1 - Photon Account and App IDs
- Step 2 - Install Fusion
- Step 3 - Fusion Extension Settings
---

<div class='important' markdown='1'>
Fusion Defold SDK 3 is a development preview and is not intended for production use yet.
</div>

# Introduction
This guide shows how to build a simple multiplayer game/application using the Photon Fusion extension for Defold. It covers app id creation, connection, spawning, movement replication, custom properties and RPCs. By the end, two clients will move around the same room and see each other in real time.

[Requirements](installation): Installed Defold editor and basic knowledge of Lua and Defold.


## Step 1 - Photon Account and App IDs
Fusion runs on the Photon Cloud. The App ID ties your project to a backend that handles connection, authentication, matchmaking and finally state distribution. Follow these steps to create a new App ID to use for the rest of this guide:

1. Create or log on to an account at dashboard.photonengine.com.
2. Click Create a New App, select Fusion as the SDK, and Version 3 (used for both Unreal and Defold).
3. Copy the App ID.


## Step 2 - Install Fusion
To use Photon Fusion in your Defold project, add a version of the Photon Fusion extension to your `game.project` dependencies from the list of available [Releases](https://github.com/defold/extension-photon-fusion/releases). Find the version you want, copy the URL to ZIP archive of the release and add it to the project dependencies.

![](add-dependency.png)

Select `Project->Fetch Libraries` once you have added the version to `game.project` to download the version and make it available in your project.


## Step 3 - Fusion Extension Settings
Photon Fusion can conveniently use pre-defined values at startup when you call `fusion.initialize_from_settings()`. Set your credentials in **game.project** > Runtime > Fusion:

* App Id - your Photon App ID created on step 1.
* App Version - a version string can be used to isolate matchmaking (e.g. "1.0")
* Default Region - Photon region (e.g. "us", "eu")