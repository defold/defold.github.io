---
layout: post
title:  Unpacking Armageddon
excerpt: Unpacking Armageddon is a game made for Ludum Dare 55. Learn how it was made in this blog post.
author: PlayMedusa
tags: ["creator spotlight", "game jam", "post mortem", "ludum dare"]
opengraph_image: https://www.defold.com/images/posts/unpackingarmageddon/unpacking-splash.png
twitter_image: https://www.defold.com/images/posts/unpackingarmageddon/unpacking-splash.png
---

In this guest post we invited forum user PlayMedusa to share the story of how Unpacking Armageddon was created using Defold for Ludum Dare 55. This post was originally [shared on itch.io](https://playmedusa.itch.io/unpacking-armageddon/devlog/724660/unpacking-armageddon-postmortem) and is reproduced here with approval from PlayMedusa.

---

![Splash](https://www.defold.com/images/posts/unpacking-armageddon/unpacking-splash.png)

"Unpacking Armageddon" is my entry for Ludum Dare 55, themed "SUMMONER". Given the theme’s specificity, it’s no wonder that many entries gravitated towards pentagrams and summoning demons. However, I’ve noticed a significant decrease in platformers and a broader diversity in game genres in this edition?


### DAY 1

For some reason I felt like making an arcade puzzle game. Fortunately, knowing I wouldn’t have much spare time that weekend, I came up with an idea much more quickly than in previous editions: Sokoban for someone who doesn’t really enjoy Sokoban puzzles, pushing and pulling boxes that are just in the way, so you are forced to constantly shuffle them around in a shrinking space. This allowed me to start working early on Saturday morning.

![Sketch](https://www.defold.com/images/posts/unpacking-armageddon/sketch.jpeg)

And thus, the story emerged from the mechanics and the theme: Armageddon has begun, you are a hell-designated summoner, but it caught you in the middle of moving into a new home. All your belongings are in cardboard boxes lying around the invocation basement! Demons are eager to enter our realm, but can’t do it if something is on top of the pentagram that serves as a gateway. You have to clear pentagrams free by pushing and pulling boxes in order to let demons enter our real and fullfill your summoning quota.

![Progress 1](https://www.defold.com/images/posts/unpacking-armageddon/game1.png)

After the Unity Fee mess last year I also started looking for alternative game engines, and found that Defold is pretty interesting for pure 2D games. Early this year I entered the Global Game Jam with Defold, making a ‘full’ game for the first time with this engine, and the experience was superb. So I have switched from Pico8 to Defold. I still miss Pico8, but Defold makes some things just easier. At some point I might try Picotron…

I enjoy, however, working with really low resolutions, so I stuck to Pico8’s 128x128 pixels and 16x16 sprites. It gives games a nice blocky look that reminds me of NAMCO games, which I love.

By 13:30 I had some final art (main character, boxes and the background), and the character could move and detect boxes.

![Progress 2](https://www.defold.com/images/posts/unpacking-armageddon/game2.gif)

A friend was visiting, so I left home to have lunch and didn’t come back until 19:00 - totally worth it, though. I still managed to work two more hours at night and finished the main mechanic: pushing boxes around to set pentagrams free. If not done quick enough, pentagrams explode- Otherwise they glow and disappeared, scoring.

Not much for the first day, but pretty good for roughly 5-7 hours of work, considering art was final already. I expected a hard second day.

![Progress 3](https://www.defold.com/images/posts/unpacking-armageddon/game3.gif)

### DAY 2

Woke up early on Sunday and went for the next basic mechanic, pulling boxes! And once that was working the whole thing started to actually feel like a game. Added some FX for pentagrams - when they are cleared, they glow, some arcane text floats up, a demon appears and flies upwards and a new pentagram is created. If too much time passes and a pentagram is not cleared, it explodes and a new one appears. With each pentagram a new box appears too (don’t know, maybe someone is throwing them to the basement for you to organize?)

By lunch time I came up with the last game mechanic: while you have to clear pentagrams from boxes, you have to place the Ritual Candle on them to complete the summoning. Game felt quite fun! So all that remained was adding sound, UI and good/bad endings.

![Progress 4](https://www.defold.com/images/posts/unpacking-armageddon/game4.gif)

[Freesound.org](https://freesound.org/) is great for sound effects, but one of the last things I added to the game wa the summoners’ chant when the Ritual Candle is placed on a pentagram. Shouting KLAATU BARADA NICTO! to the mic at 11pm while the family was already sleeping was too fun.

Extra points if you get the RIGHT movie reference!

![Gameplay](https://www.defold.com/images/posts/unpacking-armageddon/unpacking-armageddon.gif)


### WHAT WENT GOOD

Almost too much, to be honest! The game idea was fun to play even when the game was barebones. I don’t speacially enjoy trial-and-error Sokoban puzzles, but as you can move boxes around freely the game doesn’t feel so restricted. Sprites were easy to make, and programming was not too complex thanks to how Defold enforces certain behaviours, like message passing. Things are compartimentalized by design, but you can always resort to LUA modules to share critical information if needed.


### WHAT WENT BAD

With not much time to work on Saturday I couldn’t animate the main character nor demons. I like my game jam entries to have smooth character animations, they make the game feel much more polished. But I just did not have more time to draw them - yes, I could have lost sleep time, but… it’s a game jam, no need to stress things out!

There are some silly bugs around, like boxes falling on the character (although you can walk out from them) or pentagrams reappearing right where they just vanished from. But the most important issue is that most players DON’T READ INSTRUCTIONS (no surprise here), so they have no idea they can both push boxes - which is natural, just bump into them - AND PULL BOXES - which needs the player to press Z while moving. I should have made it clear in the first tutorial level by placing the candle by a wall, with an on-screen message or something like that.

Will probably add all that in a post-jam version at some point.


### LAST THOUGHTS

I’m specially happy with how this game plays and would love to revisit it at some point. I think I can add some new mechanics - maybe imps that run around pushing boxes and being a pest, rocks you can’t move, maybe larger pentagrams and more candles? Not too much, just a few things to make it last a bit longer.

Already looking forward to the next game jam!