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
To use Firabase in your Defold project, add a version of the Firebase extension to your `game.project` dependencies from the list of available [Firebase Releases](https://github.com/defold/extension-firebase/releases) and corresponding [Firebase Config Release](https://github.com/defold/extension-firebase-remoteconfig/releases).
Find the version you want for both extensions, copy the URLs to ZIP archive of the release and add it to the project dependencies.

![](add-dependency.png)

## Setup
Follow the [main setup guide for integration of Firebase in Defold](https://www.defold.com/extension-firebase).


## Usage

```lua
local function firebase_config_callback(self, message_id, message)
    if message_id == firebase.remoteconfig.MSG_ERROR then
        -- an error was detected when performing a remote config operation
        print("Firebase Remote Config error: ", message.error)
        return
    end
    if message_id == firebase.remoteconfig.MSG_INITIALIZED then
        -- remote config is initialized and ready for use
        -- setup default values for your remote config
        -- these values will be used until you have loaded updated values from
        -- the server
        firebase.remoteconfig.set_defaults({
            score_bonus = 0,
            score_multiplier = 1,
            holiday_theme = "Christmas",
            holiday_promo_enabled = false,
        })
    elseif message_id == firebase.remoteconfig.MSG_DEFAULTS_SET then
        -- you can use get_string(), get_boolean(), get_number() and get_data()
        print("Theme:", firebase.remoteconfig.get_string("holiday_theme"))                  -- Christmas
        print("Promo enabled:", firebase.remoteconfig.get_boolean("holiday_promo_enabled")) -- false
        print("Score multiplier:", firebase.remoteconfig.get_number("score_multiplier"))    -- 1

        -- get and activate new remote config values from the server
        firebase.remoteconfig.fetch_and_activate()
    elseif message_id == irebase.remoteconfig.MSG_FETCHED then
        print("Data Fetched")
        pprint("KEYS:", firebase.remoteconfig.get_keys())
    elseif message_id == firebase.remoteconfig.MSG_ACTIVATED then
        -- a recently fetched remote config has been activated and is now ready
        -- for use
        print(firebase.remoteconfig.get_string("holiday_theme")) -- Easter
    elseif message_id == firebase.remoteconfig.MSG_SETTINGS_UPDATED then
        print("Settings updated")
    end
end

function init(self)
    -- use firebase only if it is supported on the current platform
    if not firebase then
        return
    end

    -- initialise firebase and check that it was successful
     firebase.set_callback(function(self, message_id, message)
        if message_id == firebase.MSG_INITIALIZED then
            firebase.remoteconfig.set_callback(firebase_config_callback)
            firebase.remoteconfig.initialize()
        end
    end)
     firebase.initialize()
end
```

## Source code

The source code is available on [GitHub](https://github.com/defold/extension-firebase-remoteconfig)


## API reference
[API Reference - firebase](/extension-firebase-remoteconfig/firebase_api)
