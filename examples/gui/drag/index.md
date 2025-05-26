---
author: Defold Foundation
brief: This example shows how to drag a GUI box node.
category: gui
layout: example
path: gui/drag
scripts: drag.gui_script
tags: gui
title: Drag

---

This example shows how to drag a GUI box node. The example has a list of box nodes that can be dragged. It uses `gui.pick_node()` to detect if a click is within the bounds of a box and then moves the box as long as the mouse button is pressed.