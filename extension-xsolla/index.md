---
brief: This manual covers how to integrate and use Xsolla services in Defold.
github: https://github.com/defold/extension-xsolla
language: en
layout: manual
title: Xsolla documentation
toc:
- Xsolla documentation
- Installation
- Usage
- Shop Builder API
- Example
- Source code
---

# Xsolla documentation

This extension provides an integration with the Xsolla services for Defold. [Xsolla](https://xsolla.com) is an American financial technology company that makes payment software for video games. Xsolla solutions work in 200+ geographies, with 1,000+ payment methods, and with 130+ currencies in 20+ languauges. The integration currently supports the following Xsolla services:

* [Shop Builder API](https://developers.xsolla.com/api/shop-builder/overview/)


## Installation
To use Xsolla services in your Defold project, add a version of the Xsolla integration to your `game.project` dependencies from the list of available [Releases](https://github.com/defold/extension-xsolla/releases). Find the version you want, copy the URL to ZIP archive of the release and add it to the project dependencies.

![](add-dependency.png)

Select `Project->Fetch Libraries` once you have added the version to `game.project` to download the version and make it available in your project.


## Usage

### Shop Builder API

The Shop Builder API provides a third-party solution for implementing the server side for your store interface. Use the API to list sellable items, create and pay for orders and track the order status. A typical payment flow looks like this:

1. Authenticate the user (see below)
2. List sellable items using `shop.get_sellable_items()`
3. Create an order using `shop.create_order_with_item()`
4. Open a payment url for the order to initiate the payment process
5. Poll for status updates for the order `shop.get_order()`


#### Authentication

Most of the Shop Builder API functions require authentication and a valid user token before use. Xsolla provides [many options for user authentication](https://developers.xsolla.com/api/login/overview/#section/Authentication/Getting-a-user-token), ranging from basic username and password authentication to authentication via a social network or publishing platform such as Steam. Developers releasing games via Crazy Games can generate an Xsolla token using the [`crazygames.get_xsolla_user_token()` API function of the Crazy Games for Defold SDK](https://defold.com/extension-crazygames/crazygames_api/#crazygames.get_xsolla_user_token:callback).

Once you have an Xsolla user token you can pass it to the Shop Builder API:

```lua
local shop = require("xsolla.shop")

shop.set_bearer_token(token)
```


#### Requests

The Shop Builder API uses a REST API where each endpoint is represented by a Lua function. Each function takes a number of arguments and optional callback function, retry policy and cancellation token. Example:

```lua
local shop = require("xsolla.shop")

local function on_sellable_items(items, err)
  -- do something with the sellable items
  pprint(items)
end

local function get_sellable_items()
  local project_id = "123456"
  local limit = 5
  local offset = 0
  local locale = "en"
  local additional_fields = nil
  local country = "US"
  local promo_code = "WINTER2021"
  local show_inactive_time_limited_items = 1
  shop.get_sellable_items(project_id, limit, offset, locale, additional_fields, country, promo_code, show_inactive_time_limited_items, on_sellable_items)
end
```

It is also possible to use synchronous requests (using Lua coroutines). Example:

```lua
local function get_sellable_items()
  -- run the request within a coroutine
  shop.sync(function()
    local project_id = "123456"
    local limit = 5
    local offset = 0
    local locale = "en"
    local additional_fields = nil
    local country = "US"
    local promo_code = "WINTER2021"
    local show_inactive_time_limited_items = 1
    local items, err = shop.get_sellable_items(project_id, limit, offset, locale, additional_fields, country, promo_code, show_inactive_time_limited_items)

    -- do something with the sellable items
    pprint(items)
  end)
```

### Example

[Refer to the example project](https://github.com/defold/extension-xsolla/tree/master/example) to see a complete example of how the intergation works.


### Source code

The source code is available on [GitHub](https://github.com/defold/extension-xsolla)
## API reference
[API Reference - shop](/extension-xsolla/shop_api)
