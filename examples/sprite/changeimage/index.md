---
author: Defold Foundation
brief: This example shows how to change the image of a sprite
category: sprite
layout: example
opengraph_image: https://www.defold.com/examples/sprite/changeimage/changeimage_thumb.png
path: sprite/changeimage
scripts: changeimage.script
tags: sprite
thumbnail: changeimage_thumb.png
title: Change sprite image
twitter_image: https://www.defold.com/examples/sprite/changeimage/changeimage_thumb.png

---

The example shows a game object with a sprite and a script with three script properties to reference different tilesource images. The script lets the user change which image to use on the sprite.

It is also possible to use a script property to reference an atlas instead of a tilesource:

```lua
go.property("hero", resource.atlas("/assets/hero.atlas"))

function init(self)
	go.set("#sprite", "image", self.hero)
end
```

![tilesource](tilesource.png)