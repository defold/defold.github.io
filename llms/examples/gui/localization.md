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
