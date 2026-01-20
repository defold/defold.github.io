# Health Bar

This example demonstrates how to add different health bars.

[Project files](https://github.com/defold/examples/tree/master/gui/healthbar)

Overview : Example shows 3 pairs of nodes each forming a "health bar" with different pivots.

Create a pair of Box nodes, so that child node is smaller than the parent:

Example contains 3 such pairs - each with different `Pivot` and `X Anchor` settings for inner health bars:

- `West` + `Left`
- `East` + `Right`
- `Center` + `None`

Health is indicated as the size on X Axis of the inner node, so define what can be maximum and minimum width here.

Create a collection with such GUI component and add it and your game object with script to collection:

Example shows communication between `controller#main` script component (`healthbar.script`) and `hud#main` gui component with gui_script (`healthbar.gui_script`).

## Scripts

### healthbar.script

```lua
function init(self)
	-- < 1 >
	self.player_one_health = 1.0
	self.player_two_health = 1.0
	self.game_boss_health = 1.0

	-- < 2 >
	timer.delay(1, true, function()
		-- < 3 >
		self.player_one_health = math.max(self.player_one_health - 0.1, 0)
		self.player_two_health = math.max(self.player_two_health - 0.1, 0)
		self.game_boss_health = math.max(self.game_boss_health - 0.1, 0)
		-- < 4 >
		msg.post("hud", "update_health", { health_name = "left_health", health_percentage = self.player_one_health })
		msg.post("hud", "update_health", { health_name = "right_health", health_percentage = self.player_two_health })
		msg.post("hud", "update_health", { health_name = "center_health", health_percentage = self.game_boss_health })
	end)
end

--[[
1. Set initial health percentage (1.0 = 100%, 0.0 = 0%).
2. Start a timer that will call every 1 second (first argument) repeateadly (second argument being true) a callback function (3rd argument)
3. Reduce each health percentage by 0.1 (10%), but no less than 0 (using math.max to select `0`, if `self.player_one_health - 0.1` is less than `0`).
4. Send messages to hud (gui component) to "updated_health" with health name and percentage to be set in GUI script.
]]
```

### healthbar.gui_script

```lua
-- < 1 >
local min_size = 48
local max_size = 235 - min_size

-- < 2 >
local function set_healthbar(healthbar_node_name, health_percentage)
	local healthbar_node = gui.get_node(healthbar_node_name)	-- < 3 >
	local healthbar_size = gui.get_size(healthbar_node)			-- < 4 >
	healthbar_size.x = health_percentage * max_size + min_size	-- < 5 >
	gui.set_size(healthbar_node, healthbar_size)				-- < 6 >
end

function init(self)
	-- < 7 >
	set_healthbar("left_health", 1.0)
	set_healthbar("right_health", 1.0)
	set_healthbar("center_health", 1.0)
end

function on_message(self, message_id, message, sender)
	-- < 8 >
	if message_id == hash("update_health") then
		set_healthbar(message.health_name, message.health_percentage)
	end
end

--[[
1. Define minimum and maximum size of GUI healthbar (only width is changed).
2. Define a local helper function to update healthbar.
3. Get node of given name passed as "healthbar_node_name" and store it in local variable "healthbar_node".
4. Get size of this node and store it in local variable "healthbar_size".
5. Change size along X axis (width) of the node to given "health_percentage" scaled times "max_size" and added to "min_size", so that it can be no smaller than it.
6. Set the newly updated size of the node.
7. In init function, for each of three defined nodes set initial health_percentage to 1.0 (100%).
8. In on_message function, if the GUI component receives message "update_health" call helper function to update given health bar.
]]
```
