---
layout: post
title:  Releasing HTML5 games on Yandex.Games
excerpt: In this blog post we'll look at how to release Defold games on Yandex.Games using the Yandex.Games SDK.
author: Björn Ritzl
tags: ["tutorial", "yandex", "html5"]
---

Yandex.Games is a catalog of browser-based online games that can be played on smartphones or desktop devices and require no installation. Most games are also available offline (code for these games is added to the device cache during the first gaming session).

![](/images/posts/releasing-games-on-yandex/yandex-games.png)

Games from the catalog are displayed in Yandex recommendation systems (for example, in the Yandex app feed and in Yandex Browser), which have a total audience of more than 50 million users per month.

In this blog post we'll look at how to add the Yandex.Games SDK to a Defold game and how to submit your game to the Yandex.Games catalog.

Are you ready? Ok, let's go!


## Creating a Yandex account
Before anything else you need to create a Yandex account. Head over to the [registration page](https://passport.yandex.com/registration?mode=register) to get started.

![](/images/posts/releasing-games-on-yandex/create-account.png)

Next you also need to [create a developer account](https://games.yandex.ru/console) for Yandex.Games.

The two steps above are also described in [the official Yandex documentation](https://yandex.ru/dev/games/doc/dg/console/get-access.html#get-access) in case you need to go back and verifying anything.

Once you have a Yandex.Games developer account you have access to the Yandex.Games dashboard from where you can submit games. The only requirement to release a game on Yandex.Games is that the game integrates the Yandex.Games SDK. Let's see how this is done!


## Add the Yandex.Games SDK to your game
The first step to integrating the Yandex.Games SDK is to add the Defold version of the SDK to your project. Open your project in the Defold editor and open the **game.project** file and in the [Dependencies field in the Project section](https://defold.com/manuals/project-settings/#dependencies) add:

```
https://github.com/indiesoftby/defold-yagames/archive/refs/heads/master.zip
```

Your game now has the Yandex.Games SDK integrated and it is ready for release to the Yandex.Games portal. Before you release the game it is recommended that you also configure your game to show ads and earn some money!


## Initialising Yandex.Games SDK
Before you can use the Yandex.Games SDK in Defold you need to initialise it:

```
local yagames = require("yagames.yagames")

local function init_handler(self, err)
    if err then
        print("Something went wrong:", err)
    end
end

function init(self)
    yagames.init(init_handler)
end
```


## Using Yandex.Games SDK to show ads
Yandex supports a number of different ad formats, each with their own use-case. The supported ad formats are:

* **Rewarded Ads** - Use Rewarded Ads to give the user premium content, extra lives, in-game currency and so on. This type of ad is typically shown when the player dies or fails a level and you wish to give the player another chance to continue playing. Rewarded Ads can't be skipped.
* **Interstitial Ads** - Use Interstitial Ads at screen transitions, between sessions and in other situations where there is a natural pause in game play.
* **Real Time Bidding Ads** - Use Real Time Bidding Ads (also known as banner ads) at your discretion but make sure to not cover any of your game content.

When showing interstitial and rewarded ads it is important that you pause your game and mute sounds while the ad is shown.


### Showing Interstitial Ads
Interstitial ads are displayed in full-screen mode. To make ads less obtrusive, [Yandex recommends](https://yandex.ru/dev/games/doc/dg/console/work-with-adv.html) that you limit ads to three inserts: before the game starts, before the user proceeds to the next level, and at the end of the game (for example, after the user has lost).

You show an Interstitial Ad like this:

```
local yagames = require("yagames.yagames")

local function adv_open(self)
    -- You should switch off all sounds!
end

local function adv_close(self, was_shown)
    -- You can switch sounds back!
end

local function adv_offline(self)
    -- Internet is offline
end

local function adv_error(self, err)
    -- Something wrong happened :(
end

yagames.adv_show_fullscreen_adv({
    open = adv_open,
    close = adv_close,
    offline = adv_offline,
    error = adv_error
})
```

The different callback functions works as follows:

* `open` - Called when an ad is opened successfully.
* `close` - Called when an ad is closed, an error occurred, or on ad failed to open due to too frequent calls. Used with the was_shown argument (type boolean), the value of which indicates whether an ad was shown.
* `offline` - Called when the network connection is lost (when offline mode is enabled).
* `error` - Called when an error occurs. The error object is passed to the callback function.

The close callback is called in any situations, even if there was an error.


### Showing Rewarded Ads
Rewarded videos are video ads used to give the player a reward or in-game currency for watching an ad. As opposed to the limitations on frequency of interstitial ads you can show rewarded ads as often as you want.

You show a Rewarded Ad like this:

```
local yagames = require("yagames.yagames")

local function rewarded_open(self)
    -- You should switch off all sounds!
end

local function rewarded_rewarded(self)
    -- Add coins!
end

local function rewarded_close(self)
    -- You can switch sounds back!
end

local function rewarded_error(self, err)
    -- Something wrong happened :(
end

yagames.adv_show_rewarded_video({
    open = rewarded_open,
    rewarded = rewarded_rewarded,
    close = rewarded_close,
    error = rewarded_error
})
```

The different callback functions works as follows:

* `open` - Called when a video ad is displayed on the screen.
* `rewarded` - Called when a video ad impression is counted. Use this function to specify a reward for viewing the video ad.
* `close` - Called when a user closes a video ad or an error happens.
* `error` - Called when an error occurs. The error object is passed to the callback function.

The close callback is called in any situations, even if there was an error.


### Showing Banner Ads
Showing banner ads is a little bit more involved and it is recommended that you [check the official documentation](https://github.com/indiesoftby/defold-yagames#banner-ads) to learn how to set this up in your game.


### Expanding beyond ads
The Yandex.Games SDK contain many additional features besides ads. You can use the SDK to do user authentications, read player information and handle payments and sale of in-game goods.

Learn more about the full capabilities in the [documentation of the Yandex.Games SDK integration for Defold](https://github.com/indiesoftby/defold-yagames#lua-api).


## Submit your game
When your game has integrated the Yandex.Games SDK and implemented the functionality to initialise the SDK and show ads it is ready to be submitted to Yandex.Games. Before we can submit the game we need to register the game on the Yandex.Games developer dashboard. Login to the Yandex.Games developer dashboard and select the "Add app" option and fill out the form. All of the field of the form are described in the ["Add new game" manual in the official documentation](https://yandex.ru/dev/games/doc/dg/console/add-new-game.html).

![](/images/posts/releasing-games-on-yandex/add-app.png)

![](/images/posts/releasing-games-on-yandex/add-app-form.png)


### Test your game
Once the game has been submitted it must pass moderation before it can be added to the Yandex.Games catalog. This will take up to three business days. Make sure to test the game before sending it for moderation to catch simple mistakes.

To open a game in test mode:

1. Add a game through the developer dashboard and click Save.
2. Update the Draft tab. After that, the File verified link is activated in the Sources section.
3. Follow this link.

More on testing in the [official Yandex.Games documentation](https://yandex.ru/dev/games/doc/dg/console/test-game.html).


### Localization
It is highly recommended that you translate your game to Russian for the best performance on Yandex.


## Final words
We hope this tutorial will kickstart your journey towards success on Yandex.Games. If you have any questions be sure to reach out to us on [the Defold forum](https://forum.defold.com/).

Below you will find a list of games made with Defold on Yandex. We wish you good luck with your own game!

* [Sea of ​​Words](https://yandex.ru/games/app/98073/) by OpenMyGame
* [Mahjong Fruit: Connect Pairs](https://yandex.ru/games/app/100734/) by Potato Jam
* [Catapult](https://yandex.ru/games/app/96919/) by MaratGiliazov
* [Mahjong Cards](https://yandex.ru/games/app/134586/) by Indiesoft
