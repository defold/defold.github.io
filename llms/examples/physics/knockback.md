# Knockback

This example shows how to create a knockback effect when hit.

Source: [https://github.com/defold/examples/tree/master/physics/knockback](https://github.com/defold/examples/tree/master/physics/knockback)

This example shows how to create a knockback effect when hit. The setup consists of three game objects; one for the player, one for the enemy and one for the bullet that is spawned using a factory (see example on how to spawn bullets).

player
: The red ship at the bottom. Contains:
  - A *Sprite* component with the spaceship image.
  - A *Factory* component to spawn bullet game objects
  - A script to handle spawning of bullets.

bullet
: The bullet fired by the player. Contains:
  - A *Sprite* component with a bullet image.
  - A *Collision object* component. *Type* is set to `KINEMATIC`. It has a sphere *Shape* matching image.

enemy
: The black ship at the top. Contains:
  - A *Sprite* component with the spaceship image.
  - A *Collision object* component. *Type* is set to `KINEMATIC`. It has a sphere *Shape* matching image.
  - A script to handle collisions with bullets.

## Scripts

### enemy.script

```lua
-- move game object back and forth from the current position to a target position
local function move()
	local pos = go.get_position()
	local to = vmath.vector3(pos.x, 300, 0)
	local distance = pos.y - to.y
	local speed = 40
	local duration = distance / speed
	go.animate(".", "position", go.PLAYBACK_LOOP_PINGPONG, to, go.EASING_INOUTQUAD, duration)
end

function init(self)
	move()
end

function on_message(self, message_id, message, sender)
	if message_id == hash("contact_point_response") then
		if message.other_group == hash("bullet") then
			-- delete the bullet
			go.delete(message.other_id)

			-- get the position of the game object
			local pos = go.get_position()
			-- set a pushback direction based on the collision normal
			local to = pos + message.normal * 30
			-- knockback animation, then continue moving
			go.animate(".", "position", go.PLAYBACK_ONCE_FORWARD, to, go.EASING_OUTQUAD, 0.1, 0, move)
		end
	end
end
```
