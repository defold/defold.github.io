# Tilemap collisions

This example shows how to detect collisions on tilemaps

Source: [https://github.com/defold/examples/tree/master/tilemap/collisions](https://github.com/defold/examples/tree/master/tilemap/collisions)

This example uses a tilesource with two collision groups: "ground" and "danger". The tilesource uses the `tilesheet_complete.png` image for the tiles and the collision shapes (traced as outlines around the transparent pixels of each tile).

The tiles belonging to the two groups have been "painted" as can be seen by the outline around each tile. The tiles belonging to the "danger" group are purple and the tiles belonging to the "ground" group are green. Tiles with a white outline does not belong to a collision group.



The tilemap component uses the tilesource:



The tilemap is added to the example together with a collision object which uses the tilemap itself as collision shape. Note that there is no need to specify any collsion groups on the collision object itself. The groups defined in the tilesource (ie "ground" and "danger") will be used:



Click/tap on the screen to spawn game objects that will fall and interact with the tilemap.

## Scripts

### collisions.script

```lua
function init(self)
	msg.post(".", "acquire_input_focus") -- <1>
	for i=1,10 do
		factory.create("#enemyfactory", vmath.vector3(math.random(100, 700), 600, 1))  -- <2>
	end
end


function on_input(self, action_id, action)
	if action_id == hash("mouse_button_left") and action.pressed then
		factory.create("#enemyfactory", vmath.vector3(action.x, action.y, 1))  -- <3>
	end
end


function on_message(self, message_id, message, sender)
	if message_id == hash("collision_response") then  -- <4>
		if message.own_group == hash("danger") then  -- <5>
			go.delete(message.other_id)  -- <6>
		end
	end
end

--[[
1. Acquire input for the script
2. Spawn 10 game objects at random positions near the top of the screen
3. Spawn a game object when the left mouse button (or touch) is pressed
4. Something collided with the tilemap if the received message was a `collision_response`
5. Check if something collided with a tile belonging to the collision group "danger"
6. Delete the game object that collided with the tilemap
--]]
```
