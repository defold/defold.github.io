local examples = require("examples._main.examples")

local function create_layout(items, bl, tr, max_dy)
	local xi = math.ceil(math.sqrt(items) / 1.5)
	local yi = math.ceil(items / xi)

	local dx = (tr.x - bl.x) / xi
	local dy = (tr.y - bl.y) / yi
	
	if dy > max_dy then
		dy = max_dy
	end
	
	local layout = {}
	local c = items
	for y = 1,yi do
		for x = 1,xi do
			local xp = bl.x + dx / 2 + dx * (x - 1)
			local yp = tr.y - dy / 2 - dy * (y - 1)
			table.insert(layout, vmath.vector3(xp, yp, 0))
		end
	end
	return layout
end

local function create_cat_nodes(self, layout)
	-- create category nodes
	self.categories = {}
	local c = 1
	for t, cat in ipairs(examples.categories()) do
		local p = layout[c]
		local n = gui.new_text_node(p, cat)
		gui.set_color(n, vmath.vector4(0.2, 0.2, 0.2, 1.0))
		gui.set_font(n, "text64")
		gui.set_scale(n, vmath.vector3(0.5, 0.5, 1.0))
		local m = gui.get_text_metrics_from_node(n)
		local size = vmath.vector3(m.width, m.height, 1)
		gui.set_size(n, size)
		table.insert(self.categories, { node = n, category = cat, pos = p, size = size * 0.5 })
		c = c + 1
	end
end

local function create_example_nodes(self, category, layout)
	-- create example nodes
	self.examples = {}
	local c = 1
	for t, ex in ipairs(examples.category(category)) do
		local name = ex.name
		local nobg = ex.nobg
		local p = layout[c]
		local n = gui.new_text_node(p, name)
		gui.set_color(n, vmath.vector4(0.2, 0.2, 0.2, 1.0))
		gui.set_font(n, "text48")
		gui.set_scale(n, vmath.vector3(0.5, 0.5, 1.0))
		local m = gui.get_text_metrics_from_node(n)
		local size = vmath.vector3(m.width, m.height, 1)
		gui.set_size(n, size)
		local example = hash(category .. "/" .. name)
		table.insert(self.examples, { node = n, example = example, nobg = nobg })
		c = c + 1
	end
end

local function show_categories(self)
	self.state = "categories"
	local closenode = gui.get_node("close")	
	gui.set_enabled(closenode, false)
	-- delete example nodes
	for i, ex in ipairs(self.examples) do
		gui.delete_node(ex.node)
	end
	self.examples = {}
	
	for i, cat in ipairs(self.categories) do
		gui.set_enabled(cat.node, true)
		gui.set_position(cat.node, cat.pos)
	end
end

local function cat_expand(self)
	local closenode = gui.get_node("close")
	gui.set_enabled(closenode, true)
	
	local ex = examples.category(self.current_category)
	local layout = create_layout(#ex, self.bl, self.tr, 100)
	create_example_nodes(self, self.current_category, layout)
end

local function show_category(self, category)
	self.state = "category"
	self.current_category = category
	for i, cat in ipairs(self.categories) do
		if cat.category == category then
			local pos = vmath.vector3(50, 600, 0)
			local m = gui.get_text_metrics_from_node(cat.node)
			pos.x = pos.x + cat.size.x / 2 + 20
			gui.animate(cat.node, "position", pos, gui.EASING_INOUTQUAD, 0.3, 0, cat_expand)
		else
			gui.set_enabled(cat.node, false)
		end
	end	
end

function init(self)
	self.examples = {}
	self.categories = {}

	self.bl = vmath.vector3(50, 50, 0)
	self.tr = vmath.vector3(670, 560, 0)

	local cat_layout = create_layout(#examples.categories(), self.bl, self.tr, 100)
	create_cat_nodes(self, cat_layout)
	
	show_categories(self)
	
	msg.post(".", "disable")
	msg.post("#", "release_input_focus")
end

function on_message(self, message_id, message, sender)
	if message_id == hash("show") then
		msg.post(".", "enable")
		msg.post("#", "acquire_input_focus")
	elseif message_id == hash("hide") then
		msg.post(".", "disable")
		msg.post("#", "release_input_focus")
	end
end

function on_input(self, action_id, action)
	if action_id == hash("touch") and action.pressed then
		if self.state == "categories" then
			for i, cat in ipairs(self.categories) do
				if gui.pick_node(cat.node, action.x, action.y) then
					show_category(self, cat.category)
				end
			end		
		end
	
		if self.state == "category" then
			local n = gui.get_node("close")	
			if gui.pick_node(n, action.x, action.y) then
				show_categories(self)
			end
			
			for i, ex in ipairs(self.examples) do
				if gui.pick_node(ex.node, action.x, action.y) then
					msg.post("/loader#script", "load_example", { example = ex.example, nobg = ex.nobg })
				end
			end
		end
	end
end

function on_reload(self)
	msg.post(".", "disable")
end
