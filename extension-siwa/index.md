---
layout: manual
language: en
github: https://github.com/defold/extension-siwa
title: Sign in with Apple extension for Defold
brief: This manual covers how to setup and use Sign in with Apple in Defold.
---

# Sign in with Apple extension for Defold

This extension provides functions to use [Sign in with Apple](https://developer.apple.com/sign-in-with-apple/) to allow users to set up an account and sign in to your game with their Apple ID.

## Installation

To use this library in your Defold project, add the following URL to your `game.project` dependencies:

https://github.com/defold/extension-siwa/archive/master.zip

We recommend using a link to a zip file of a [specific release](https://github.com/defold/extension-siwa/releases).


## Setting up your app for Sign in with Apple

To get started you need to enable your app’s App ID with the Sign in with Apple capability. [Follow the official Apple developer instructions](https://help.apple.com/developer-account/?lang=en#/devde676e696) to get started.


## Usage

### Check Sign in with Apple support

```Lua
if siwa.is_supported() then
	print("Sign in with Apple is supported")
end)
```

### Trigger Sign in with Apple

```Lua
siwa.authenticate(id, function(self, data)
	print(data.identity_token)
	print(data.user_id)
	print(data.first_name, data.family_name)
	print(data.email)
	if data.user_status == siwa.STATUS_LIKELY_REAL then
		print("Likely a real person")
	end
end)
```

### Check credential state

```Lua
siwa.get_credential_state(id, function(self, data)
	if data.credential_state == siwa.STATE_AUTHORIZED then
		print("User has still authorized the application", data.user_id)
	elseif data.credential_state == siwa.STATE_REVOKED then
		print("User has revoked authorization for the application", data.user_id)
	end
end)
```


## Source code

The source code is available on [GitHub](https://github.com/defold/extension-siwa)


## API reference
[API Reference](/extension-siwa/api)