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

| Firebase C++ SDK        | Firebase iOS SDK        | Dependencies |
|-------------------------|-------------------------|--------------|
| Firebase C++ SDK 8.10.0 | Firebase iOS SDK 8.13.0 | [https://github.com/defold/extension-firebase/archive/refs/tags/1.4.2.zip](https://github.com/defold/extension-firebase/archive/refs/tags/1.4.2.zip)<br>[https://github.com/defold/extension-firebase-remoteconfig/archive/refs/tags/1.3.1.zip](https://github.com/defold/extension-firebase-remoteconfig/archive/refs/tags/1.3.1.zip) |


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

    -- initialise remote config and set up a listener to react to
    -- remote config state changes
    firebase.remoteconfig.init(function(self, event)
        -- an error was detected when performing a remote config operation
        if event == firebase.remoteconfig.CONFIG_ERROR then
            return
        end

        -- remote config is initialized and ready for use
        -- setup default values for your remote config
        -- these values will be used until you have loaded updated values from
        -- the server
        if event == firebase.remoteconfig.CONFIG_INITIALIZED then
            firebase.remoteconfig.set_defaults({
                score_bonus = 0,
                score_multiplier = 1,
                holiday_theme = "Christmas",
                holiday_promo_enabled = false,
            })
            return
        end

        -- the defaults have been set and we're now ready to use remote config
        if event == firebase.remoteconfig.CONFIG_DEFAULTS_SET then
            -- you can use get_string(), get_boolean(), get_number() and get_data()
            print("Theme:", firebase.remoteconfig.get_string("holiday_theme"))                  -- Christmas
            print("Promo enabled:", firebase.remoteconfig.get_boolean("holiday_promo_enabled")) -- false
            print("Score multiplier:", firebase.remoteconfig.get_number("score_multiplier"))    -- 1

            -- get and activate new remote config values from the server
            firebase.remoteconfig.fetch_and_activate()
            return
        end

        -- a recently fetched remote config has been activated and is now ready
        -- for use
        if event == firebase.remoteconfig.CONFIG_ACTIVATED then
            print(firebase.remoteconfig.get_string("holiday_theme")) -- Easter
            return
        end
    end)
end
```

## Source code

The source code is available on [GitHub](https://github.com/defold/extension-firebase-remoteconfig)


## API reference
[API Reference](/extension-firebase-remoteconfig/firebase-remoteconfig_api)