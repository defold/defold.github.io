# Localization (RTL/LTR)

This example demonstrates how to handle localization in games, Unicode text layout, RTL rendering, and runtime font switching for localization.

[Project files](https://github.com/defold/examples/tree/master/gui/localization)

This example demonstrates how to handle localization in games, Unicode text layout, RTL rendering, and runtime font switching for localization.

Click the buttons (EN, AR, PT, JA) to switch between 4 languages.

Arabic demonstrates right-to-left layout, while English/Portuguese/Japanese show left-to-right layout.

## Approach overview

The example is intentionally modularized and the flow in the program is linear:

1. Read localized strings from a JSON file for the requested language.
2. If the language needs a non-default font, load the font collection proxy asynchronously.
3. Attach the font at runtime to the default GUI font resource.
4. Prewarm glyphs for the requested text so the first render is smooth.
5. Update the GUI text and layout (LTR/RTL) and restore input focus.

This illustrates a practical localization flow in Defold:

- Runtime font switching via `font.add_font()` / `font.remove_font()`.
- Asynchronous proxy loading for large font resources.
- Glyph prewarming with `font.prewarm_text()`.
- LTR/RTL layout using text node pivot and position.

To recreate such an example:

1. Add to your project an [App Manifest](https://defold.com/manuals/app-manifest/) file with the option `Use full font layout system` enabled. The rest of the settings doesn't matter for this example, so are left as default.

2. Use this App Manifest file in the `game.project` file in the `Native Extension` section in the `App Manifest` setting.

3. Then, also in the `game.project` file in the `Font` section enable the `Runtime Generation` setting.

4. In the end, add the localization of the used JSON files in the `Project` section in the `Custom Resources` setting.

Project setup used by this example:

- `game.project` with runtime font generation enabled and custom app manifest `main.appmanifest`.
- `main.collection` with:
    - game object `go` with:
        - `ar_proxy` - collection proxy component referring to `lang_ar.collection` file.
        - `ja_proxy` - collection proxy component referring to `lang_ja.collection` file.
        - `main.gui` - GUI component with `main.gui_script`.

The 2 mentioned collections (`lang_ar.collection` / `lang_ja.collection`) contain:
- `go` game object with:
    - `label` - component with `Font` property set to `noto_ar.font`/`noto_ja.font`

In the `assets` folder there are two subfolders:
- `fonts` - containing `.ttf` font files and `.font` Defold resources referencing those font files respectively
- `img` - containing images and atlas used for GUI nodes.
- `texts` - containing `.json` files with text examples and information about language used.

The separate Collections for components with fonts and Collection Proxies to load and unload them are added to show good practices on handling fonts - usually, you only need the one font that user selected in the settings, so rest of the fonts should be unloaded from memory.

Therefore, we have in the example only one font that is defined in the GUI component, that is `latin`. The rest (Arabic `noto_ar` and Japanese `noto_ja`) are loaded using respective Collection Proxy components `ar_proxy` and `ja_proxy`.

Those collections contain the game object with component in order to assign there a Font resource - `noto_ar` and `noto_ja`.

A [Collection Proxy](https://defold.com/manuals/collection-proxy/) in Defold is a special component that allows you to load and unload entire collections (groups of game objects, components and resources) dynamically at runtime. In this example, proxies are used to manage fonts, so that only the font needed by the user is kept in memory at any time.

### How are proxies loaded and unloaded?

1. **Loading a proxy:**
    - When the user clicks a language button (like "AR" or "JA"), the script checks if that language requires a special font.
    - If so, it determines which proxy to use (`ar_proxy` for Arabic, `ja_proxy` for Japanese, etc.).
    - The script sends the `async_load` message to the appropriate proxy, and Defold begins loading the target collection (`lang_ar.collection`, `lang_ja.collection`, etc.) asynchronously.
    - Once the collection is loaded, the related assets (mainly the font resource) are available in RAM.
    - The script receives a `proxy_loaded` message, and can now activate the font for GUI text.

2. **Unloading a proxy:**
    - When the user switches to another language that uses a different font (or goes back to a language using the default font), the no-longer-needed proxy should be unloaded.
    - The script sends the `unload` message to the relevant proxy.
    - After unloading, Defold automatically releases all resources from that collection—freeing the memory taken by the font and any related resources.
    - Once unloading is finished, the script receives a `proxy_unloaded` message and may proceed to load or activate the next font as needed.

### How are these collections (`lang_ar.collection`, `lang_ja.collection`) constructed?

- Each collection contains just a single game object with an empty label (or text) component.
- This component is configured to use the specific font file needed for that language (e.g., a TTF that supports Arabic or Japanese.)
- No additional game logic or nodes are needed inside—these collections simply act as packages for the required font resource.

This structure is a Defold best practice: the font is only referenced as long as the proxy is loaded. When the proxy is unloaded, Defold can fully release the font and its memory, keeping the application efficient. This is important for games with large multilingual font files; only the currently active font consumes RAM, even when switching languages at runtime.

The localized text strings are loaded from disk (`text_en.json`, `text_ar.json`, `text_pt.json`, `text_ja.json`) using `sys.load_resource()`.

## Helper modules

The logic is split into two small helpers to keep the GUI script concise and focused on flow:

- `localization_helper.lua`: Handles the language switch flow (load/unload proxies, attach runtime fonts, prewarm glyphs, finalize switch). It owns the small state machine around proxies and fonts and exposes a simple API to the GUI script.
- `ui_helper.lua`: Handles GUI node lookup, button states and visuals, LTR/RTL layout changes, and input handling details. It keeps GUI operations in one place so the core localization logic stays easy to follow.

## Assumptions and simplifications

This example intentionally trades robustness for clarity:

- Sequential flow only. It assumes one language switch at a time (unload old font, then load new font, then update UI). Because of this, `on_message` does not verify which proxy sent `proxy_loaded` / `proxy_unloaded`.
- No JSON caching. The JSON is small and read on demand via `sys.load_resource()` and `json.decode()`. For larger or frequent loads, caching should be demonstrated in a separate example.
- Data is trusted. The `languages` table is assumed to be correct and complete (including `json`, `layout`, `proxy`, and `ttf_hash` where required). The JSON is assumed to contain the expected fields (`title`, `text`).
- Minimal defensive checks. Assertions and guards are kept light to avoid clutter.

These choices keep the example readable and focused on the key idea.

## Scripts

### main.gui_script

```lua
-- Helper module for UI operations
-- Separated in order not to clutter the example.
local ui = require "example.ui_helper"

-- Helper module for localization operations
local loc = require "example.localization_helper"


function init(self)
	-- Per-language content path, layout (LTR/RTL),
	-- and an optional proxy with font resource to load,
	-- and a True Type Font (TTF) file pre-hashed path.
	self.languages = {
		en = {
			json = "/assets/texts/text_en.json",
			layout = ui.layout.ltr,
			proxy = false,
		},
		ar = {
			json = "/assets/texts/text_ar.json",
			layout = ui.layout.rtl,
			proxy = "#ar_proxy",
			ttf_hash = hash("/assets/fonts/NotoSansArabic-Medium.ttf"),
		},
		pt = {
			json = "/assets/texts/text_pt.json",
			layout = ui.layout.ltr,
			proxy = false,
		},
		ja = {
			json = "/assets/texts/text_ja.json",
			layout = ui.layout.ltr,
			proxy = "#ja_proxy",
			ttf_hash = hash("/assets/fonts/NotoSansJP-Regular.ttf"),
		},
	}

	-- We delegate UI handling to a separate helper module
	-- in order not to clutter the example.
	ui.initialize_ui(self)

	-- Store the font resource of the default font
	-- that is initally used for the text gui node.
	self.default_font_resource = ui.get_font_resource(self.text_node)

	-- Set the GUI initial current language.
	self.current_lang = "en"

	-- Set the initial requested language to the same one.
	self.requested_lang = "en"

	-- Get the text for the requested language from the JSON file.
	self.requested_text = loc.get_content_from_json(self)

	-- Clear texts and update after fonts are prewarmed.
	ui.clear_text_nodes(self)
	loc.finish_language_change(self, ui.update_ui_content_callback)
end

-- Pre-hashed message IDs.
local msg_proxy_loaded = hash("proxy_loaded")
local msg_proxy_unloaded = hash("proxy_unloaded")

function on_message(self, message_id, message, sender)
	-- React to proxy lifecycle messages and continue pending language switch.
	if message_id == msg_proxy_unloaded then

		-- Remove runtime font once its owning proxy is unloaded.
		font.remove_font(self.default_font_resource, self.languages[self.current_lang].ttf_hash)

		-- If old font resource was unloaded, load the new one (or finish with default).
		if self.languages[self.requested_lang].proxy then
			msg.post(self.languages[self.requested_lang].proxy, "async_load")
		else
			loc.finish_language_change(self, ui.update_ui_content_callback)
		end

	elseif message_id == msg_proxy_loaded then
		loc.finish_language_change(self, ui.update_ui_content_callback)
	end
end

-- Pre-hashed action ID.
local action_touch = hash("touch")

function on_input(self, action_id, action)
	-- Pointer move arrives with nil action_id in Defold.
	if action_id == nil and action.x and action.y then
		ui.on_pointer_moved(self, action.x, action.y)
	end

	-- If the action is not a touch:
	if action_id ~= action_touch then
		-- Skip the rest of the input handling.
		return
	end

	-- If the action is a touch and pressed:
	if action.pressed then
		-- Get the selected language on pressed.
		local selected_language = ui.get_selected_language_on_pressed(self, action.x, action.y)

		-- Set the requested language and text.
		self.requested_lang = selected_language or self.requested_lang

		-- If the requested language is different from the current language:
		if self.requested_lang ~= self.current_lang then
			-- Clear current texts while the new font is prepared.
			ui.clear_text_nodes(self)

			-- Get the text for the requested language from the JSON file.
			self.requested_text = loc.get_content_from_json(self)
		end

		-- Process the language change.
		loc.process_language_change(self, ui.update_ui_content_callback)
	end

	-- If the action is a touch and released:
	if action.released then
		-- Handle the touch released event.
		ui.on_touch_released(self, action.x, action.y)
	end
end
```

### localization_helper.lua

```
local M = {}

-- Attach the font resource to the default font resource
-- and prewarm the glyphs for smooth rendering.
function M.set_runtime_font_and_prewarm(self, on_font_ready_callback)

	-- If the requested language has a proxy, attach the runtime font:
	if self.languages[self.requested_lang].proxy then
		-- Add the runtime font to the default font resource.
		font.add_font(self.default_font_resource, self.languages[self.requested_lang].ttf_hash)
	end

	-- Prewarm the glyphs for smooth rendering for the given requested text.
	local text = self.requested_text.text
	font.prewarm_text(self.default_font_resource, text, on_font_ready_callback)
end

-- Finalize language switch once the required font can render requested text.
function M.finish_language_change(self, on_font_ready_callback)
	-- Prepare a callback function that will be called when fonts are ready.
	local on_language_changed = function()
		
		-- New language has been set, change the current language variable.
		self.current_lang = self.requested_lang

		on_font_ready_callback(self)
	end

	-- Set the runtime font and prewarm the glyphs for smooth rendering.
	M.set_runtime_font_and_prewarm(self, on_language_changed)
end

-- Process the language change.
function M.process_language_change(self, callback_on_font_ready)
	-- If the requested language is the same as the current language:
	if self.requested_lang == self.current_lang then

		-- No change needed, skip the rest of the language change process.
		return
	end

	-- Otherwise:
	-- Release the input focus during the language change,
	-- so the user cannot interact in the meantime.
	-- You can still allow it, if needed in your game,
	-- but in that case keep track of the status of (un)loading.
	msg.post(".", "release_input_focus")

	local requested_language_proxy = self.languages[self.requested_lang].proxy
	local current_language_proxy = self.languages[self.current_lang].proxy

	-- If the requested language font is the same as the current:
	if requested_language_proxy == current_language_proxy then
		-- Finish the language change with prewarm.
		M.finish_language_change(self, callback_on_font_ready)

		-- And skip the rest of the language change process.
		return
	end

	-- Otherwise:
	-- If the current language is with a loaded proxy:
	if current_language_proxy then

		-- Unload this collection with the font resource first.
		msg.post(current_language_proxy, "unload")

		-- And skip the rest of the language change process.
		return
	end

	-- Load the new font.
	msg.post(requested_language_proxy, "async_load")
end


-- JSON file handling ------------------------------------------

-- Get the text for the requested language from the JSON file.
function M.get_content_from_json(self)
	-- Load the JSON file for the requested language.
	local language = self.languages[self.requested_lang]
	local json_file = sys.load_resource(language.json)
	assert(json_file, "Failed to load JSON file for language: " .. self.requested_lang)

	-- Return the decoded JSON file as a table.
	return json.decode(json_file) or {}
end

return M
```

### ui_helper.lua

```
local M = {}

-- Font resource ------------------------------------------------

-- Get the font resource of the default font.
-- @param node_id The ID of the node to get the font resource of.
-- @return The font resource of the default font.
function M.get_font_resource(node_id)
	-- Get the font resource of the default font.
	return gui.get_font_resource(gui.get_font(node_id))
end

-- Buttons visuals ----------------------------------------------

-- Visual states used by language selection buttons.
M.button_state = {
	released = 1,
	hovered = 2,
	pressed = 3,
}

-- Predefined button colors for the given button state.
local button_color = {
	[M.button_state.released] = vmath.vector4(1, 1, 1, 0.7),
	[M.button_state.hovered] = vmath.vector4(1, 1, 1, 0.9),
	[M.button_state.pressed] = vmath.vector4(1, 1, 1, 1.0),
}

-- UI Initialization --------------------------------------------

-- Initialize UI with the given languages.
-- @param self The self table from the GUI script.
function M.initialize_ui(self)
	-- Resolve GUI text nodes for information display once during init.
	self.text_node = gui.get_node("text")
	self.language_name_node = gui.get_node("language_name")

	-- Create a table of all buttons with their language name, node, and state.
	self.buttons = {}
	for language_name, _ in pairs(self.languages) do
		-- Set initial button state to released.
		local state = M.button_state.released

		-- Get the button node.
		local node = gui.get_node("btn_" .. language_name)

		-- Add the button to the buttons table.
		self.buttons[language_name] = {
			language_name = language_name,
			node = node,
			state = state
		}

		-- Update initial button color according to the state.
		gui.set_color(node, button_color[state])
	end

	msg.post(".", "acquire_input_focus")
end

-- Layout definitions ------------------------------------------

-- Supported text flow directions used by language layout.
M.layout = {
	ltr = "LTR",
	rtl = "RTL",
}

-- Predefined text node positions for the given layout.
local text_position = {
	[M.layout.ltr] = vmath.vector3(-380, 0, 0),
	[M.layout.rtl] = vmath.vector3(380, 0, 0),
}

-- Predefined text node pivots for the given layout.
local text_pivot = {
	[M.layout.ltr] = gui.PIVOT_W,
	[M.layout.rtl] = gui.PIVOT_E,
}

-- Update UI content --------------------------------------------

-- Update the UI content with the requested language.
-- @param self The self table from the GUI script.
function M.update_ui_content_callback(self)
	-- Update the language text.
	gui.set_text(self.text_node, self.requested_text.text or "")

	-- Update the language name and layout information.
	local layout = self.languages[self.requested_lang].layout
	local header_text = string.format("%s (%s)", self.requested_text.title, layout)
	gui.set_text(self.language_name_node, header_text)

	-- Update the text layout.
	gui.set_pivot(self.text_node, text_pivot[layout])
	gui.set_position(self.text_node, text_position[layout])

	-- Update the input focus.
	msg.post(".", "acquire_input_focus")
end

-- Clear text nodes while a language change is in progress.
-- @param self The self table from the GUI script.
function M.clear_text_nodes(self)
	gui.set_text(self.text_node, "")
	gui.set_text(self.language_name_node, "")
end

-- Input handling -----------------------------------------------

-- Handle pointer move event.
-- @param self The self table from the GUI script.
-- @param x The x position of the pointer.
-- @param y The y position of the pointer.
function M.on_pointer_moved(self, x, y)
	-- Update the state of all buttons according to the pointer position.
	for _, button in pairs(self.buttons) do
		-- Check if the pointer is over the button.
		if gui.pick_node(button.node, x, y) then
			-- If so, set the button state to hovered.
			button.state = M.button_state.hovered
		else
			-- Otherwise, set the button state to released.
			button.state = M.button_state.released
		end
		-- Update the button color according to the new state.
		gui.set_color(button.node, button_color[button.state])
	end
end

-- Get the button pressed and return the language name.
-- @param self The self table from the GUI script.
-- @param x The x position of the pointer.
-- @param y The y position of the pointer.
function M.get_selected_language_on_pressed(self, x, y)
	local selected_language = nil
	-- Find the button pressed.
	for _, button in pairs(self.buttons) do
		-- Check if the pointer is over the button.
		if gui.pick_node(button.node, x, y) then
			-- If so, set the button state to pressed.
			button.state = M.button_state.pressed
			selected_language = button.language_name
		end
		-- Update the button color according to the new state.
		gui.set_color(button.node, button_color[button.state])
	end
	-- Return the language name of the button pressed, nil if not found
	return selected_language
end

-- Handle touch released event.
-- @param self The self table from the GUI script.
-- @param x The x position of the pointer.
-- @param y The y position of the pointer.
function M.on_touch_released(self, x, y)
	-- Find the button released.
	for _, button in pairs(self.buttons) do
		-- Check if the pointer is over the button.
		if gui.pick_node(button.node, x, y) then
			-- If so, set the button state to released.
			button.state = M.button_state.released
		end
		-- Update the button color according to the new state.
		gui.set_color(button.node, button_color[button.state])
	end
end

return M
```
