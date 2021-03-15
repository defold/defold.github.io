---
layout: post
title:  Releasing HTML5 games on Game Distribution
excerpt: In this blog post we'll look at how to add the Game Distribution SDK to an existing game or how to create one from scratch. We will also look at how to submit your game for distribution through the Game Distribution network.
author: Björn Ritzl
tags: ["tutorial", "gamedistribution", "html5"]
---

Game Distribution recently joined the Defold Foundation as a corporate partner. GameDistribution is the biggest broker of high quality, cross-platform games and their network serves over 300M users a month with top HTML5 content. As part of the partnership the foundation integrated the Game Distribution SDK as a Defold native extension and added a Defold template project to the Defold editor with the Game Distribution SDK integrated.

In this blog post we'll look at how to add the Game Distribution SDK to an existing game or how to create one from scratch. We will also look at how to submit your game for distribution through the Game Distribution network.

Are you ready? Ok, let's go!

## Register as a Game Distribution developer
Before you can start using GameDistribution you need to register as a developer:

https://developer.gamedistribution.com/register/developer/

When you have registered as a developer you also need to register your game in the GameDistribution developer portal:

https://developer.gamedistribution.com/games

When you have registered the game head to the Upload tab and copy the Game ID:

![](/images/posts/releasing-html5-games-on-game-distribution/gameid.png)

With this out of the way we are now ready to work on our game. Let's first look at what to do if you are creating a new game.


### Creating a new game
If you are creating a new game it is recommended that you use the GameDistribution project template from the Defold editor Welcome screen. The GameDistribution template includes the [GameDistribution SDK extension](https://github.com/GameDistribution/gd-defold):

![GameDistribution template](/images/posts/releasing-html5-games-on-game-distribution/gamedistribution-template.png)

Add your Game ID to the GameDistribution section of the **game.project** file:

![Adding game id game.project](/images/posts/releasing-html5-games-on-game-distribution/adding-gameid.png)

That's it! We now have an empty project with the Game Distribution SDK included and with your Game ID set. But what if you have an existing game? Don't worry, it is easy!


## Configuring an existing game
If you wish to use GameDistribution with an existing game you can open the **game.project** file and in the [Dependencies field in the Project section](https://defold.com/manuals/project-settings/#dependencies) add:

```
https://github.com/GameDistribution/gd-defold/archive/main.zip
```

Open the **game.project** file using a text editor and add a new section with your Game ID:

```
[gamedistribution]
game_id = ADD YOUR GAME ID HERE
```

Ok, your game now has the Game Distribution SDK included and your Game ID set. Let's look at how to use the Game Distribution SDK in Defold to show ads and earn some money!


## Using Game Distribution
Game Distribution supports a number of different ad formats, each with their own use-case. The supported ad formats are:

* **Rewarded Ads** - Use Rewarded Ads to give the user premium content, extra lives, in-game currency and so on. This type of ad is typically shown when the player dies or fails a level and you wish to give the player another chance to continue playing. Rewarded Ads can't be skipped.
* **Interstitial Ads** - Use Interstitial Ads at screen transitions, between sessions and in other situations where there is a natural pause in game play. Interstitial Ads can be skipped.
* **Display Ads** - Use Display Ads (also known as a banner ad) at your discretion but make sure to not cover any of your game content.

It is important to be smart about placement of ads and not show them too frequently or else the players may grow tired of constant breaks in the game play and in the game immersion. The Game Distribution SDK has built in limits on the frequency of ads and at times you may request to show an ad but the SDK will reject the request.

Ok, let's look at how to actually show these ads. Step one is to provide the SDK with a listener function. The function will be used to give you information about when an ad starts and the game should pause and when it stops and gameplay can resume.

```Lua
gdsdk.set_listener(function(self, event, message)
	print(event, message)
	if event == gdsdk.SDK_GAME_PAUSE then
		-- pause your game
	elseif event == gdsdk.SDK_GAME_START then
		-- resume your game
	end
end)
```

There are [additional events](https://github.com/GameDistribution/gd-defold/blob/main/gamedistribution/src/gamedistribution.cpp#L143-L179) besides the two shown above, but it is unlikely that you need to care about them.


### Showing ads
Once you have the listener function set up you can start showing ads. For Rewarded and Interstitial ads there are a couple of important things to keep in mind:

1. The most important is to only display ads as an immediate reaction to user input (click, key or touch input) as the ad may not function properly without it due to restrictions imposed by modern browsers.
2. The second thing to keep in mind is to pause game play and sounds while the ad is shown and resume the game only when the ad has been closed. The listener function will help us here as you will receive the `gdsdk.SDK_GAME_PAUSE` event when the ad starts playing and the `gdsdk.SDK_GAME_START` when the ad has been closed.


#### Showing a Rewarded ad
You show a Rewarded Ad like this:

```
gdsdk.show_rewarded_ad()
```

That's it! The ad will load and automatically start playing.


#### Showing an Interstitial Ad
You show an Interstitial Ad like this:

```
gdsdk.show_interstitial_ad()
```


#### Showing a Display Ad
In order to show a Display Ad you need to manually add a `<div>` [to your index.html](https://defold.com/manuals/html5/#customizing-html5-bundle) where the Display Ad will be shown. Example:

```html
<!-- center and anchor to bottom of page -->
<div style="position: absolute; bottom: 0px; left: 50%;">
	<div id="canvas-ad" style="width: 728px; height:90px; margin-left: -50%;"/>
</div>
```

Give the `<div>` a size that matches one of the [supported display ad sizes](https://github.com/GameDistribution/GD-HTML5/wiki/Display-Ads).

You show and hide a Display Ad like this:

```
-- show it
gdsdk.show_display_ad("canvas-ad")

-- hide it
gdsdk.hide_display_ad("canvas-ad")
```


## Submitting your game
When the game is finished and the Game Distribution SDK has been integrated according to the instructions above it's time to submit your game. The first step is to [export the game as an HTML5 game bundle from the Defold editor](https://defold.com/manuals/html5/#creating-html5-bundle).

![Export HTML5](/images/posts/releasing-html5-games-on-game-distribution/html5_bundle.png)

Zip the folder containing the exported files and head back to the Game Distribution Developer Portal and select your game and the Upload tab.

Drag and drop the zip file on the page to upload it.

![Export HTML5](/images/posts/releasing-html5-games-on-game-distribution/gamedistribution-upload.png)

To verify your SDK implementation; make sure to completely view an advertisement, while viewing your game through an iframe launched from the Upload tab of the GameDistribution developer portal page for you game.

When the SDK implementation has been validate press the Request Activation button to submit the game. You will be notified via email of any problems or if the game passed review.

### Checklist
Make sure to test your game against the follow checklist:

* **All menu options are working**
  * The game can be paused and resumes from where it was paused.
  * The game supports targeted web and mobile operating systems.
  * The page loading indicator works.
  * All progress indicators within the game function correctly (Level, point, time etc.)
  * Sound preferences are restored after restarting the game.
  * Language preferences are restored after restarting the game.
  * The game is running with stable speed and FPS.
  * Game does not freeze or crash.

* **Control and buttons**
  * Controls are supported for both touch devices and mouse/keyboard devices and these must follow the design.
  * Every button within the game function according to design.

* **Background Music and Sound Effects**
  * User is able to switch ON/OFF the background/SFX sound.
  * Object/Character actions and audio are synchronized.
  * Check for sounds that are not triggered or triggered wrong.
  * Check for bad sounds, instruments, and music mix.

* **Screen**
  * Game works in both landscape and portrait mode.
  * Objects/Characters do not move out of the screen/specified area.
  * Game has no clipping, overlapping etc. issues.
  * Any change in browsers (like Minimize, Restore Down, Maximize, Size Scaling or Other Interuptions) does not trigger any issues.
  * Font family, typography, size, color and other visual effects are consistent
  * Texts don't have any spelling errors.

* **Ads**
  * Ad does not interrupt game and cause game over.
  * Game sound does not overlap with ad sound.
  * Make sure the banner ad isn't covering any UI components. Test your game with different screen resolutions.

### Localization
Make sure to translate your game for better performance on local markets. Focus on these languages:

* German
* Dutch
* Spanish
* Portuguese
* French
* Polish

Optionally also translate to Italian, Norwegian and Russian


## Final words
We hope this tutorial will kickstart your journey towards success on Game Distribution. If you have any questions be sure to reach out to us on [the Defold forum](https://forum.defold.com/).

If you have specific questions regarding the Game Distribution SDK or if you think you have found a bug please [file an issue on GitHub](https://github.com/GameDistribution/gd-defold/issues).

Good luck with your game!
