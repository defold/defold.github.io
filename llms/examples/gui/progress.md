# GUI progress indicators

This example shows how to create various types of progress indicators

[Project files](https://github.com/defold/examples/tree/master/gui/progress)

The example shows three different types of progress indicators:

1. A horizontal progress bar created using a box node with a texture and 9-slice scaling
2. A numerical progress text created using a text node
3. A circular progress created using a pie node

## Scripts

### progress.gui_script

```lua
-- set the width of the horizontal progress bar
local function update_horizontal(p)
	local node = gui.get_node("horizontal")
	local size = gui.get_size(node)
	size.x = p * 400 -- max width is 400 pixel
	gui.set_size(node, size)
end

-- set value of numeric progress indicator (in percent from 0% to 100%)
local function update_numeric(p)
	local node = gui.get_node("numeric")
	local percent = math.floor(p * 100)
	gui.set_text(node, tostring(percent) .. "%")
end

-- update radial/circle progress by changing the fill angle
local function update_radial(p)
	local node = gui.get_node("radial")
	local angle = p * 360 -- full circle is 360 degrees
	gui.set_fill_angle(node, angle)
end

function init(self)
	self.time = 0
end

function update(self, dt)
	self.time = self.time + dt

	-- calculate a value between 0.0 and 1.0
	-- the value will gradually increas from 0 to 1 during 3 seconds
	local p = (self.time % 3) / 3
	update_numeric(p)
	update_horizontal(p)
	update_radial(p)
end
```
