# Change sprite image

This example shows how to change the image of a sprite

[Project files](https://github.com/defold/examples/tree/master/sprite/changeimage)

The example shows a game object with a sprite and a script with three script properties to reference different tilesource images. The script lets the user change which image to use on the sprite.

It is also possible to use a script property to reference an atlas instead of a tilesource:
```lua
go.property("hero", resource.atlas("/assets/hero.atlas"))

function init(self)
	go.set("#sprite", "image", self.hero)
end
```

## Scripts

### changeimage.script

```lua
-- create script properties with references to three different tile sources
go.property("robot", resource.tile_source("/assets/robot.tilesource"))
go.property("zombie", resource.tile_source("/assets/zombie.tilesource"))
go.property("adventurer", resource.tile_source("/assets/adventurer.tilesource"))

local function update_tilesource(image_id)
	-- set the sprite image property to the specified tilesource
	go.set("#sprite", "image", image_id)
	-- play the run animation
	sprite.play_flipbook("#sprite", "run")
end

function init(self)
	msg.post(".", "acquire_input_focus")
	update_tilesource(self.robot)
end

-- change sprite image when key 1, 2 and 3 are pressed
function on_input(self, action_id, action)
	if action.pressed then
		if action_id == hash("key_1") then
			update_tilesource(self.robot)
		elseif action_id == hash("key_2") then
			update_tilesource(self.zombie)
		elseif action_id == hash("key_3") then
			update_tilesource(self.adventurer)
		end
	end
end
```
