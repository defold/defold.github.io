# Get and set a gui font resource

This example shows how to get and set a font resource on a gui component.

[Project files](https://github.com/defold/examples/tree/master/gui/get_set_font)

## Scripts

### get_set_font.script

```lua
-- create a script resource property 'myfont' referencing a font file
go.property("myfont", resource.font("/assets/text48.font"))

function init(self)
	msg.post(".", "acquire_input_focus")

	-- get the font file on the gui component which is assigned to
	-- the font with id 'default'
	self.default_font = go.get("#gui", "fonts", { key = "default" })
end

function on_input(self, action_id, action)
	if action_id == hash("touch") and action.pressed then
		-- get the font file currently assigned to the font with id 'default'
		local current_font = go.get("#gui", "fonts", { key = "default" })

		-- toggle between the default font and the font referenced by the
		-- script resource property 'myfont'
		if current_font == self.myfont then
			go.set("#gui", "fonts", self.default_font, { key = "default" })
		else
			go.set("#gui", "fonts", self.myfont, { key = "default" })
		end
	end
end
```
