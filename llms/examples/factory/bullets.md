# Shoot bullets

This example shows how to dynamically spawn bullet game objects using a factory component.

[Project files](https://github.com/defold/examples/tree/master/factory/bullets)

This example shows how to dynamically spawn bullet game objects using a factory component and how to also move and delete the bullets. The setup consists of two game objects; one for the player and one for the bullet that is spawned using a factory component.

Combine this example with some of the examples from the movement and physics categories to create a shoot 'em up game!

player
: The red ship at the bottom. Contains:
  - A *Sprite* component with the spaceship image.
  - A *Factory* component to spawn bullet game objects
  - A script to handle spawning of bullets.

bullet
: The bullet fired by the player. Contains:
  - A *Sprite* component with a bullet image.

## Scripts

### player.script

```lua
function init(self)
	-- make sure the script will receive user input
	msg.post(".", "acquire_input_focus")
end

function on_input(self, action_id, action)
	-- mouse or spacebar
	if (action_id == hash("touch") or action_id == hash("key_space")) and action.pressed then
		-- position bullet somewhat offset from the player position
		local pos = go.get_position()
		pos.y = pos.y + 50

		-- spawn a bullet
		local bullet_id = factory.create("#bulletfactory", pos)

		-- animate the bullet
		local distance = 1000                   -- distance in pixels
		local speed = 800                       -- pixels per second
		local duration = distance / speed       -- time in second to travel the full distance
		local to = pos.y + distance
		-- start animation and delete bullet when it has reached its destination
		go.animate(bullet_id, "position.y", go.PLAYBACK_ONCE_FORWARD, to, go.EASING_LINEAR, duration, 0, function()
			go.delete(bullet_id)
		end)
	end
end
```
