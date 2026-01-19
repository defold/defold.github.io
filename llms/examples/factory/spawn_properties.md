# Spawn enemies with script properties

This example shows how to spawn enemy game objects using a factory component with different properties.

Source: [https://github.com/defold/examples/tree/master/factory/spawn_properties](https://github.com/defold/examples/tree/master/factory/spawn_properties)

This example shows how to dynamically spawn enemy game objects using a factory component with different properties. The setup consists of three main components: a player ship, enemy spawner, and different enemy types with customizable properties.

Press keys `1`, `2`, or `3` to spawn different enemy types.

Example collection consists of 2 game objects:



### Ship
The red ship at the bottom that automatically moves and shoots. Consists of:
- A *Factory* component `bulletfactory` to spawn bullet game objects
- A *Script* `ship` that handles automatic movement (ping-pong animation) and bullet spawning every 0.25 seconds
- A *Sprite* component with the spaceship image

Bullets are simply animated upward and automatically deleted when they reach the top.

### Spawner
Controls enemy spawning with keyboard input. Consists of:
- A *Factory* `enemyfactory` to spawn enemies with different properties
- A *Label* `example_description` with instructions text displayed on top
- A *Script* `spawner` that spawns enemies.


The spawner script defines three different enemy types: `random`, `diagonal`, and `straight`.
Uses factory to create enemies with specific properties:

```lua
local properties = ENEMY_TYPES[enemy_type]
factory.create("#enemyfactory", position, nil, properties)
```

### Enemy Types

**Random Enemy** (Key 1):
- Green UFO sprite
- 1 health point
- Random horizontal movement that changes every second
- Speed: 40 horizontal, -100 vertical

**Diagonal Enemy** (Key 2):
- Red enemy sprite
- 2 health points
- Fixed diagonal movement
- Speed: 120 horizontal, -80 vertical

**Straight Enemy** (Key 3):
- Blue enemy sprite
- 3 health points
- Straight downward movement
- Speed: 0 horizontal, -40 vertical

### Enemy Script Properties
Properties defined in `enemy.script` control enemy behavior:
- `sprite` - Which sprite to display
- `health_points` - How many hits before destruction
- `speed` - Movement velocity vector
- `is_random` - Whether to use random movement changes

When enemies have `go.property` defined in their script, these properties are visible in the *Properties* pane and can be customized per enemy type.

Combine this example with other movement and physics examples to create a complete shoot'em up game!

## Scripts

### ship.script

```lua
function init(self)
	-- Animate automatic player position
	go.animate(".", "position.x", go.PLAYBACK_LOOP_PINGPONG, 620, go.EASING_LINEAR, 6.0)

	-- Create a timer to tick every 0.25 second:
	timer.delay(0.25, true, function()

		-- Create a simple bullet bullet using the factory
		local bullet_id = factory.create("#bulletfactory", go.get_position())

		-- Animate the created bullet towards top of screen, where it is deleted
		if bullet_id then
			go.animate(bullet_id, "position.y", go.PLAYBACK_ONCE_FORWARD, 600, go.EASING_LINEAR, 1, 0, function()
				go.delete(bullet_id)
			end)
		end
	end)
end
```

### enemy.script

```lua
-- Define different properties of the script:
go.property("sprite", hash("ufoGreen"))
go.property("health_points", 1)
go.property("speed", vmath.vector3(100, 100, 0))
go.property("is_random", true)

function init(self)

	-- Set animation of the sprite to the one defined by its property self.sprite:
	sprite.play_flipbook("#sprite", self.sprite)

	-- Add randomness to horizontal direction - this way enemy horizontal speed may be inverted or cleared:
	-- -1 * self.speed.x - inverted direction
	--  0 * self.speed.x - cleared direction
	--  1 * self.speed.x - regular direction
	self.speed.x = math.random(-1, 1) * self.speed.x

	-- If self.is_random boolean property is true:
	if self.is_random then
		-- add a timer to randomly switch horizontal speed every second:
		timer.delay(1, true, function()
			self.speed.x = math.random(-1, 1) * self.speed.x
		end)
	end
end

function update(self, dt)
	-- Update enemy position based on its current speed:
	local pos = go.get_position()
	pos = pos + self.speed * dt
	go.set_position(pos)

	-- Bounce enemy off "walls":
	if pos.x > 600 or pos.x < 50 then
		self.speed.x = -self.speed.x
	end

	-- Remove enemy if it goes out of screen:
	if pos.y < -50 then
		go.delete()
	end
end

function on_message(self, message_id, message, sender)

	-- React to collision with bullet:
	if message_id == hash("trigger_response") and message.enter then

		-- Remove one health point
		self.health_points = self.health_points - 1

		-- Play particlefx for damage taken:
		particlefx.play("#boom")

		-- When no health points left - remove this ship
		if self.health_points <= 0 then
			go.delete()
		end
	end
end
```

### spawner.script

```lua
-- Define different properties for different enemies:
local ENEMY_TYPES = {
	random = {
		sprite = hash("ufoGreen"),
		health_points = 1,
		speed = vmath.vector3(40, -100, 0),
		is_random = true
	},
	diagonal = {
		sprite = hash("enemyRed2"),
		health_points = 2,
		speed = vmath.vector3(120, -80, 0),
		is_random = false
	},
	straight = {
		sprite = hash("enemyBlue4"),
		health_points = 3,
		speed = vmath.vector3(0, -40, 0),
		is_random = false
	}
}

function init(self)
	-- Acquire input focus here, so we can handle inputs:
	msg.post(".", "acquire_input_focus")
end

-- Helper function to spawn given enemy by its type:
local function spawn_enemy(enemy_type)

	-- Select properties of the enemy by type:
	local properties = ENEMY_TYPES[enemy_type]

	-- Set initial position of the spawned ship.
	local position = go.get_position()

	-- This will make the position one out of (-180, -90, 0, 90, 180):
	position.x = position.x + math.random(-2,2) * 90

	-- Create enemy with passed properties
	factory.create("#enemyfactory", position, nil, properties)
end

function on_input(self, action_id, action)

	-- React to different key presses with spawning different enemies:
	if action_id == hash("key_1") and action.released then
		spawn_enemy("random")
	elseif action_id == hash("key_2") and action.released then
		spawn_enemy("diagonal")
	elseif action_id == hash("key_3") and action.released then
		spawn_enemy("straight")
	end
end
```
