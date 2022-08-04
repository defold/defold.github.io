---
layout: post
title:  The making of BoxRob
excerpt: In this post d954mas shares his experience of creating the game BoxRob
author: d954mas
tags: ["developer case study", "post mortem"]
---

BoxRob is a puzzle platform game created by forum user d954mas for 7Spot Games. d954mas did code and level design while idea, art, music, and all the rest come from 7Spot Games. In this blog post d954mas will share his experience working on the game, from initial idea to finished product.

In BoxRob the goal is to load cargo onto a truck using a flexible forklift. To complete the level, you need to collect all the boxes and put them in the appropriate slot. Some levels are easy and you just drive around collecting boxes, but as you go through the game the levels get more difficult. Perform special moves or follow sequences to solve the puzzle and complete the level.

The game consists of 3 parts, each consisting of 20 base levels, and 1 bonus level. A total of 63 levels. 

![](/images/posts/the-making-of-boxrob/boxrob-half.jpg)

![](/images/posts/the-making-of-boxrob/boxrob_1.mp4)

[You can play the game on Poki](https://poki.com/en/g/boxrob).


In BoxRob 2 ([PLAY](https://poki.com/en/g/boxrob-2)) there are conveyor belts and moving hooks.


![](/images/posts/the-making-of-boxrob/conveyorbelts.mp4)
![](/images/posts/the-making-of-boxrob/movinghooks.mp4)


BoxRob 3 ([PLAY](https://poki.com/en/g/boxrob-3)) introduced explosions:

![](/images/posts/the-making-of-boxrob/explosions.mp4)


### TIMELINE
It took about five and a half months to make the three parts.

* 03.05.2021 - Initial commit
* 17.07.2021 - Prototype is done. Levels can be completed.
* 22.09.2021 - BoxRob-1 is ready for soft launch.
* 19.10.2021 - BoxRob-2 and BoxRob-3 are done.

Polishing for release and creation of levels for parts 2 and 3 went in parallel.

### BUILD SIZE

Since the game target platform is HTML5 the build size was crucial. The final size of BoxRob 1 is 5.8 MB (3.8 MB gzipped). Approximately 900kb of the gzipped size is the Defold engine. The rest (2.91 MB) is assets:

![](/images/posts/the-making-of-boxrob/buildsize.png)

* 1.33 MB music + sounds
* 1.20 MB textures
* 216.20 KB scripts
* 63.21 KB fonts
* 46.65 KB levels (json)


### DEVELOPMENT

####  PHYSICS
Defold already has a built-in version of Box2d but the functionality is limited. Luckily you can take the built-in Box2d out of the engine and use a native extension to add full-fledged physics, in which everything is available. For physics the game used a fork of [Sergey Lerg's box2d native extension](https://github.com/Lerg/extension-box2d). Later this fork was used as a base for a [full Box2d native extension](https://github.com/d954mas/defold-box2d).

#### LEVEL EDITOR
It is possible to make levels in the Defold editor, but it was decided to use Tiled since it was more convenient and flexible. [Tiled](https://www.mapeditor.org/) is a cross-platform open-source tile map editor for games. From Tiled levels are exported to .lua and later converted to .json using a script. The script gets rid of the unused data, makes some fixes (for example, changes the coordinate system from y-down to y-up) and performs validation (checks that player spawn exists, that elevators use an existing trajectory, and that there are no objects with the same name, etc.)

![](/images/posts/the-making-of-boxrob/tiled.png)

#### ENTITY COMPONENT SYSTEM
BoxRob uses a data-oriented approach with a custom made entity component system (or ECS). In brief, ECS is a pattern for decomposition. The idea is that each game object (entity) consists of a set of components. For example, position component, acceleration component and so on.

All logic is written in the system. For example, the movement system takes all entities that have position and acceleration component, and performs the necessary operations with them.  In the end, the game has 44 systems, and even more components. This approach results in a flexible game architecture that is easy and pleasant to work with, easy to extend, and optimize. You can [read more about ECS here](https://www.gamedev.net/articles/programming/general-and-gameplay-programming/understanding-component-entity-systems-r3013/).

![](/images/posts/the-making-of-boxrob/ecs_systems.png)

#### SCRIPTS
All logic is written in Lua modules and there is only one .script file in scene, the `controller.script`. This script update ECS and captures input from player.

![](/images/posts/the-making-of-boxrob/scripts.png)


### PROTOTYPE

The creation of the game started with a prototype. The prototype was used to make sure that there are no problems with physics and that the game is fun to play. The Tiled level editor was also tested to create a level where the robot would move around. After that the physics was added, and the creation of the robot began. When working with physics, the box2d documentation helped a lot, as well as Google, and various tutorials for box2d.

Changing physical properties is painful. If the properties were changed in one place, it might require changing properties in another place, because physically the robot would start behaving differently. For example, when the density of the arm was increased, the arm became heavier, and the passability decreased. To adjust for this more strength was added to the wheels. But by adding more strength to the wheels something else was affected, and so on...

As a result, the way the robot behaves in the release version is a set of physical bodies and their properties, which was selected due to a large number of iterations :slight_smile:


Below is a number of stages of development show. Between each of these stages, there were a large number of iterations to select the necessary properties of physical bodies and to solve other problems:


#### WHEELBASE (11.05.21)
The wheelbase was created.

![](/images/posts/the-making-of-boxrob/wheelbase.mp4)


#### ART (18.05.21)
The art was added. The robot can jump and the hand was added. The hand is a physical rectangle that is always at a certain angle to the wheelbase. When turning the base, it keeps the right angle.

![](/images/posts/the-making-of-boxrob/addedart.mp4)


#### MOVING THE HAND (24.05.21)
The hand is a set of physical bodies. Now it’s moving. When making contact with the box, it connects to the hand.

![](/images/posts/the-making-of-boxrob/movingthehand.mp4)


#### CARRYING A BOX (7.06.21)
Passability increased. The hand can take the a and ride with it and when changing the direction of movement, the hand turns.

![](/images/posts/the-making-of-boxrob/carryingabox.mp4)


#### THROWING A BOX (09.06.21)
The first version of throwing a box. The hand swings and throws and the player has the ability to aim.

![](/images/posts/the-making-of-boxrob/throwingabox.mp4)


#### THROWING A BOX (AGAIN) (10.06.21)
The second version of throwing a box. The player can "shoot the box" and this option, without the ability to aim, is used in the game.

![](/images/posts/the-making-of-boxrob/throwingabox2.mp4)


#### PROTOTYPE COMPLETED (17.07.21)
The prototype is done and all mechanics work. It is possible to complete the level from the start until the victory screen appears.

![](/images/posts/the-making-of-boxrob/prototype_done.mp4)


### INTERESTING FACTS

#### ROUND BOXES
The box, when picked up by hand, changes its physical body from a rectangle to a circle, so it doesn’t get stuck in narrow places and cling to corners.

![](/images/posts/the-making-of-boxrob/round_boxes.png)


#### PLACING THE BOX INSIDE THE TRUCK
Throwing a box into the truck is tricky, and there are levels where you need to stack the boxes on top of each other. Therefore, when entering a truck, the throwing mechanics are replaced by the laying mechanics. Moreover, to make it obvious to the player, the hand changes its position and extends forward.

![](/images/posts/the-making-of-boxrob/in_truck.mp4)


#### INVISBLE WALLS
On one level you need to put the boxes in a pit and then press the button to push them into the car with the door. But there was a problem with the boxes clinging to the wall. So, the wall collider was made smaller than it looks. But a new problem appeared; the robot could enter this hole. To solve this an invisible wall that only collides with the robot was added.

Yellow is the wall collider. Red is an invisible wall:

![](/images/posts/the-making-of-boxrob/collider_wall.jpg)


#### TRUCK ON BONUS LEVELS
When you collect 60 stars, you open a bonus level. On the bonus level, you don’t need to load cargo. Instead you need to collect all the stars within a certain time. But the game logic expects a truck to be on the level. Therefore, at the bonus level, there is a truck, but it is out of the player’s sight!

![](/images/posts/the-making-of-boxrob/truck_bonus.png)


#### BUGS WITH PHYSICS
Physics bugs can look funny. For example, when the robot’s arm is torn apart, but it tries to get back together:

![](/images/posts/the-making-of-boxrob/physics_bug.mp4)


#### EXPLOSIONS
When the box exploded, a bunch of small round bodies with velocity were created. This is a simulation of what happens in an explosion. It is easy to implement and it looks realistic.

![](/images/posts/the-making-of-boxrob/explosion_physics.mp4)


#### PICKING UP THE BOX
When robot tries to take a box with hand, force is applied to the end of the hand, so the hand moves to the box. When the hand is near the box a distance joint is created between the hand and the box grip point. This joint is elastic. It tries to move the box to the hand. This makes it look juicier and faster.

![](/images/posts/the-making-of-boxrob/boxpickup.mp4)


### CONCLUSION
It turned out to be a cool game that was enjoyable to work on. There were a lot of difficult and funny moments when working with physics, and overall, this game was interesting to make. It was a pleasure to see the prototype getting better and better with each iteration!

Reach out to [d954mas on the forum](https://forum.defold.com/t/boxrob/71377) if you have any questions!




