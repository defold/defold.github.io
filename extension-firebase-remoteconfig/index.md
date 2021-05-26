---
layout: manual
language: en
github: https://github.com/defold/extension-firebase-remoteconfig
title: Defold Firebase Remote Config documentation
brief: This manual covers how to setup and use Firebase Remote Config in Defold.
---

# Defold Firebase Remote Config documentation

This extension allows you to interact with Firebase Remote Config in a uniform way for games on iOS and Android.


## Installation
To use this library in your Defold project, add the following URLs to your `game.project` dependencies:

| Firebase C++ SDK       | Dependencies |
|------------------------|--------------|
| Firebase C++ SDK 7.3.0 | [https://github.com/defold/extension-firebase/archive/refs/tags/1.1.2.zip](https://github.com/defold/extension-firebase/archive/master.zip)<br>[https://github.com/defold/extension-firebase-remoteconfig/archive/refs/tags/1.0.0.zip](https://github.com/defold/extension-firebase-remoteconfig/archive/refs/tags/1.0.0.zip) |


## Setup
Follow the [main setup guide for integration of Firebase in Defold](https://www.defold.com/extension-firebase).


## Usage

```lua
function init(self)
    -- use firebase only if it is supported on the current platform
    if not firebase then
        return
    end

    -- initialise firebase and check that it was successful
    local ok, err = firebase.init()
    if not ok then
        print(err)
        return
    end

    firebase.remoteconfig.init(function(self, event)
        if event == firebase.remoteconfig.CONFIG_ERROR then
            return
        elseif event == firebase.remoteconfig.CONFIG_INITIALIZED then
            firebase.remoteconfig.set_defaults({ hello = "world" })
        elseif event == firebase.remoteconfig.CONFIG_DEFAULTS_SET then
            print(firebase.remoteconfig.get_string("hello")) -- world
            firebase.remoteconfig.fetch_and_activate()
        elseif event == firebase.remoteconfig.CONFIG_ACTIVATED then
            print(firebase.remoteconfig.get_string("hello")) -- (depends on if it has changed on the server or not)
        end
    end)
end
```

## Source code

The source code is available on [GitHub](https://github.com/defold/extension-firebase-analytics)


## API reference
[API Reference](/extension-firebase-remoteconfig/api)