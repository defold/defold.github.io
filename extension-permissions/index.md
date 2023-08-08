---
layout: manual
language: en
github: https://github.com/defold/extension-permissions
title: Defold Permissions documentation
brief: Extension to query for and request application permissions from the user or operating system.
---

# Defold Permissions documentation

This extension provides functions to query for and request application permissions from the user or operating system.
At the moment it supports only Android.


## Installation

To use this library in your Defold project, add the needed version URL to your `game.project` dependencies from [Releases](https://github.com/defold/extension-permissions/releases)

<img width="401" alt="image" src="https://user-images.githubusercontent.com/2209596/202223571-c77f0304-5202-4314-869d-7a90bbeec5ec.png">


## Defold Setup

To be able to use the extension, it's enough to install it. However, there are some limitations that exist. For example:
- to be able to request a permission, it should be added in AndroidManifest.xml;
- some permissions should be requested individually;
- etc

Read the official Android [Request runtime permissions documentation](https://developer.android.com/training/permissions/requesting) for a better understanding of the process.

## Usage

The API uses a callback based system where events and data coming from the OS are passed to the game client through a callback function.
[Example](https://github.com/defold/extension-permissions/blob/master/example/gui.gui_script) is availible in the repository.

## Source code

The source code is available on [GitHub](https://github.com/defold/extension-permissions)


## API reference
[API Reference](/extension-permissions/permissions_api)