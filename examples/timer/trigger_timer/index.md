---
author: Pawel Jarosz
brief: This example shows how to create timer that triggers counting every 1s and can be triggered manually and asynchronously as a reaction to user input.
category: timer
layout: example
opengraph_image: https://www.defold.com/examples/timer/trigger_timer/trigger_timer.png
path: timer/trigger_timer
scripts: trigger_timer.gui_script
tags: timer
thumbnail: trigger_timer.png
title: Trigger timer example
twitter_image: https://www.defold.com/examples/timer/trigger_timer/trigger_timer.png

---

The example shows how to use Defold built-in timer and trigger it asynchronously and uses two indicators:

1. A counter text increased every 1s created using a text node.
2. A text node with information displayed.

The timer triggers update of the counter every 1s.
Click anywhere to trigger the callback of the timer asynchronously.

![trigger_timer](trigger_timer.png)