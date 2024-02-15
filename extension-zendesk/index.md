---
layout: manual
language: en
github: https://github.com/defold/extension-zendesk
title: Zendesk extension documentation
brief: This manual covers how to setup and use Zendesk in Defold.
---

# Zendesk extension documentation

This extension provides a unified, simple to show and interface with Zendesk conversations on iOS and Android.


## Installation
To use this library in your Defold project, add the following URL to your `game.project` dependencies:

https://github.com/defold/extension-zendesk/archive/master.zip

We recommend using a link to a zip file of a [specific release](https://github.com/defold/extension-zendesk/releases).


## Configuration
The extension can be configured by adding the following fields to game.project:

```
[zendesk]
channel = Add your Zendesk channel id here
```

## Example

```lua
function init(self)
    if not zendesk then
        print("Zendesk is not supported on this platform")
        return
    end

    zendesk.set_callback(function(self, event, data)
        if event == zendesk.MSG_ERROR then
            print("An error occured")
            pprint(data)
        elseif event == zendesk.MSG_INITIALIZED then
            print("Initialized")
            pprint(data)
            zendesk.show_messaging()
        end
    end)

    local channel = sys.get_config_string("zendesk.channel")
    zendesk.initialize(channel)
end

```

## Source code

The source code is available on [GitHub](https://github.com/defold/extension-zendesk)


## API reference
[API Reference - zendesk](/extension-zendesk/zendesk_api)
