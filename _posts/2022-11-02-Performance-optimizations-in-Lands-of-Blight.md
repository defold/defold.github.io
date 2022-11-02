---
layout: post
title:  Performance optimizations in Lands of Blight
excerpt: In this post d954mas shares how Lands of Blight was optimized to support a thousand active enemies in a single game
author: d954mas
tags: ["developer case study", "code", "poki", "html5"]
---

Lands of Blight is an action adventure game where you take control of a character that automatically attacks every few seconds, and you need to survive the continuous waves of monsters. Simply walk around the area and attack as many monsters as you can while trying to escape their clutch.

[Try the game on Poki.com](https://poki.com/en/g/lands-of-blight)


Lands of Blight was developed by forum user d954mas for 7Spot Games. In this blog post d954mas will share his experience optimising the game to run in a mobile browser with stable FPS and more than 1000 enemies.

<video width="640" height="480" controls>
  <source src="/images/posts/performance-optimizations-in-lands-of-blight/landsofblight.mp4" type="video/mp4">
</video>

In Lands of Blight there are three critical parts for performance:

1. Rendering (WebGL)
2. Logic (Lua and C++)
3. Garbage collection (Lua)

### Rendering

Defold has a really fast renderer which can draw a lot of sprites per frame. Overall, the render was not a blocker for the game, but there was one problem with the rendered; the enemy blinking on hit. The blink effect can either be made using a shader or by a flipbook animation. The shader uses a uniform variable for blink which means that it would break batching and dramatically increase draw calls.

<video width="640" height="480" controls>
  <source src="/images/posts/performance-optimizations-in-lands-of-blight/lob-enemy-blink.mp4" type="video/mp4">
</video>

Instead of a shader for the blink effect, we decided to create an animation for every enemy. All enemy animations (blink, die etc) were made in [JuiceFx](https://codemanu.itch.io/juicefx). Thanks to [@CodeManuPro](https://twitter.com/CodeManuPro) for an awesome animation generation tool!

![](/images/posts/performance-optimizations-in-lands-of-blight/lob-enemy-blink-flipbook.png)

### Logic

The main language in Defold is Lua, but for some parts of this game C++ was used to increase performance. In Lands of Blight we use an Entity Component System (ECS) with 63 different systems. The draw systems are actually not rendering objects, instead they create game objects with sprites, start animations, move sprites to actual entity positions and so on.

![](/images/posts/performance-optimizations-in-lands-of-blight/lob-ecs.png)

For ECS we use the awesome [tiny-ecs](https://github.com/bakpakin/tiny-ecs) library.

To test the performance of the game we use an HTML5 build using a scene with 2048 enemies while in the release version of the game we have a limit of 1024 enemies. As you can see from the screenshot below it is hard to see more than a few hundred enemies:

![](/images/posts/performance-optimizations-in-lands-of-blight/lob-many-enemies.jpeg)

For collisions we use Box2D, but it turned out to be a bad choice as thosands of enemies simply was too much for Box2D to handle. To increase performance we use two Box2D worlds:

1. One world for the player, enemies and projectiles
2. Another world for pickups

With ECS it is very easy to find bottlenecks by measuring the time spent in each system. The most time consuming systems are:

1. `UpdateBox2dSystem` - Average: 4.67ms
2. `UpdatePositionFromBodySystem` - Average: 0.9ms
3. `DrawEnemySystem` - Average: 0.81ms
4. `EnemyMoveSystem` - Average: 0.78ms
5. `UpdateDynamicZSystem` - Average: 0.3ms


#### System updates

Some systems do not need to update every frame. For example the `EnemyRemoveDistanceSystem` is updated only one time per second. Another way to increase performance was to update some systems on odd frames and other systems on even frames.

The `UpdateBox2dSystem` system updates Box2D and it is the most time consuming system. We decided to update the system only in odd frames (ie 30 times per second). In an odd frame it takes 9.34ms and in an even frame it takes 0ms which gives an average of 4.67ms. Some other systems, such as `UpdatePositionFromBodySystem`, are updated in even frames.


#### Moving from Lua to C++

The `UpdatePositionFromBodySystem` and `EnemyMoveSystem` systems were moved from Lua to C++ which resulted in a big performance boost. In a desktop build where LuaJIT is used we got between 15-40% performance boost and in an HTML5 build where standard Lua 5.1 is used we saw got between 150-250% boost in performance! 💪

System update written in Lua:

![](/images/posts/performance-optimizations-in-lands-of-blight/lob-system-lua.jpeg)


System update written in C++:

![](/images/posts/performance-optimizations-in-lands-of-blight/lob-system-cpp.jpeg)



#### Animations

To make enemies look better when they move we use a squash animation:

```
scale.x = 1 + amplitude * math.sin( time * speed )
scale.y = 1 / scale.x
```

The problem with this is that if we run this calculation for every enemy every frame it will be slow.

<video width="640" height="480" controls>
  <source src="/images/posts/performance-optimizations-in-lands-of-blight/lob-enemy-squash-animation.mp4" type="video/mp4">
</video>


Instead of calculating it every frame we precalculate 100 points and let the engine do the animation using `go.animate()` instead of doing it in Lua code. We start by calculating the points in system init and in a second step we start the scale animation and let `go.animate()` linearly interpolate the scale between the precalculated points.

![](/images/posts/performance-optimizations-in-lands-of-blight/lob-enemy-squash-animation.jpeg)


### Garbage collection

Lua is a garbage collecting language, meaning that it does automatic memory management where allocated but no longer used memory is deallocated at regular intervals. The problem with this is that if you create a lot of objects every frame you can see some freezes when the GC will work. The main idea to avoid object creation is to reuse objects as much as possible.

We create a lot of enemies and projectiles so using an object pool is good idea. The idea behind an object pool is that unused objects are returned to the pool for later use instead of immediately being deallocated by the system.

![](/images/posts/performance-optimizations-in-lands-of-blight/lob-object-pool.png)

In Defold when you add one vector to another it will create a new vector which means that if you do a lot of vector math operations each frame you will create a lot of new vectors. To avoid this we use the [defold-xmath](https://github.com/thejustinwalsh/defold-xmath) native extension by Justin Walsh. The extension uses the same API for vector math as Defold but instead of returning a new vector it modifies an existing vector:

```lua
-- create a new vector
local v = e.position + TEMP_V

-- reuse v to store the result of e.position + TEMP_V
xmath.add(v, e.position, TEMP_V)
```

### Questions

If you have any questions about the contents of this blog post please [reach out to d954mas on Twitter](https://twitter.com/d954mas)!





