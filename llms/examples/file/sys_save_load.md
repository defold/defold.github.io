# Save and Load

This example shows how to save and load data using sys.save() and sys.load()

Source: [https://github.com/defold/examples/tree/master/file/sys_save_load](https://github.com/defold/examples/tree/master/file/sys_save_load)

The example will save and load a file containing a Lua table with a single value key-value pair representing a highscore. Loading and saving is done using sys.load() and sys.save(). Also refer to the [Working with files manual](https://defold.com/manuals/file-access/).

## Scripts

### sys_save_load.script

```lua
local function load_highscore()
	local filename = sys.get_save_file("sys_save_load", "highscore") -- <1>
	local data = sys.load(filename) -- <2>
	return data.highscore or 0  -- <3>
end

local function save_highscore(highscore)
	local filename = sys.get_save_file("sys_save_load", "highscore")
	sys.save(filename, { highscore = highscore })  -- <4>
end

local function update_labels(score, highscore)
	label.set_text("score#score", tostring(score))
	label.set_text("score#highscore", "HIGH SCORE\n" .. tostring(highscore))
end

function init(self)
	msg.post(".", "acquire_input_focus")
	self.score = 0
	self.highscore = load_highscore()
	update_labels(self.score, self.highscore)
end

function update(self, dt)
	if self.pressed then
		self.score = self.score + math.ceil(100 * dt)
		update_labels(self.score, self.highscore)
	end
end

function on_input(self, action_id, action)
	if action_id == hash("touch") then
		if action.pressed then
			self.score = 0
			self.pressed = true
		elseif action.released then
			self.pressed = false
			if self.score > self.highscore then
				self.highscore = self.score
				save_highscore(self.highscore)
				update_labels(self.score, self.highscore)
			end
		end
	end
end

--[[
1. Get an application specific path for the file "highscore"
2. Load saved data.
3. The returned data is a Lua table with the saved values or an empty table if nothing has been saved.
4. Save data. The data to save must be stored in a Lua table.
--]]
```
