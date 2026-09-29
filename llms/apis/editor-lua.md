# Editor

**Namespace:** `editor`
**Language:** Lua
**Type:** Defold Lua

Editor scripting documentation

## API

### editor.bob
*Type:* FUNCTION
Run bob the builder program
For the full documentation of the available commands and options, see the bob manual.

**Parameters**

- `options` (table<string, string|integer|boolean|(string|integer|boolean)[]>) (optional) - table of command line options for bob, without the leading dashes (<code>--</code>). You can use snake_case instead of kebab-case for option keys. Only long option names are supported (i.e. <code>output</code>, not <code>o</code>). Supported value types are strings, integers and booleans. If an option takes no arguments, use a boolean (i.e. <code>true</code>). If an option may be repeated, you can use an array of values.
- `...` (string) (optional) - bob commands, e.g. <code>"resolve"</code> or <code>"build"</code>

**Examples**

Print help in the console:
```
editor.bob({help = true})

```

Bundle the game for the host platform:
```
local opts = {
    archive = true,
    platform = editor.platform
}
editor.bob(opts, "distclean", "resolve", "build", "bundle")

```

Using snake_cased and repeated options:
```
local opts = {
    archive = true,
    platform = editor.platform,
    build_server = "https://build.my-company.com",
    settings = {"test.ini", "headless.ini"}
}
editor.bob(opts, "distclean", "resolve", "build")

```

### editor.browse
*Type:* FUNCTION
Open a URL in the default browser or a registered application

**Parameters**

- `url` (string) - http(s) or file URL

### editor.can_add
*Type:* FUNCTION
Check whether this list property supports add, clear, and remove operations on the supplied node.

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `value` (boolean)

### editor.can_get
*Type:* FUNCTION
Check whether this property is exposed for reading on the supplied node or resource.

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `value` (boolean)

### editor.can_reorder
*Type:* FUNCTION
Check whether this list property supports reordering on the supplied node.

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `value` (boolean)

### editor.can_reset
*Type:* FUNCTION
Check whether this property supports reset on the supplied node.

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `value` (boolean)

### editor.can_set
*Type:* FUNCTION
Check whether this property is exposed for setting on the supplied node.

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `value` (boolean)

### editor.command
*Type:* TYPEDEF
An editor command

**Parameters**

- `value` (userdata) - an editor command

### editor.command
*Type:* FUNCTION
Create an editor command

**Parameters**

- `opts` (editor.command.options) - command options

**Returns**

- `command` (editor.command)

**Examples**

Print Git history for a file:
```
editor.command({
  label = "Git History",
  query = {
    selection = {
      type = "resource",
      cardinality = "one"
    }
  },
  run = function(opts)
    editor.execute(
      "git",
      "log",
      "--follow",
      "." .. editor.get(opts.selection, "path"),
      {reload_resources=false})
  end
})

```

### editor.command.context
*Type:* STRUCT
Context provided to editor command handler functions

**Members**

- `selection?` (string|userdata|(string|userdata)[]) - current selection, populated when requested by the command query
- `active_view?` (userdata) - current active editor view, populated when requested by the command query
- `argument?` (any) - command argument, populated when requested by the command query

### editor.command.location
*Type:* TYPEDEF
A location where an editor command can be displayed

**Parameters**

- `value` ("Assets" | "Bundle" | "Code" | "Debug" | "Edit" | "Help" | "Outline" | "Project" | "Scene" | "View") - a location where an editor command can be displayed

### editor.command.options
*Type:* STRUCT
Options used to create an editor command

**Members**

- `label` (string|editor.message) - user-visible command name, either a string or a localization message
- `locations` (editor.command.location[]) - non-empty list of locations where the command is displayed
- `query?` (editor.command.query) - query that controls command availability and provides context to its handler functions
- `id?` (string) - keyword identifier that may be used for assigning a shortcut to a command; should be a dot-separated identifier string, e.g. <code>"my-extension.do-stuff"</code>
- `active?` (fun(opts:editor.command.context):boolean) - function that additionally checks if a command is active in the current context; should be fast to execute since the editor might invoke it in response to UI interactions
- `run?` (fun(opts:editor.command.context):any) - function that is invoked when the user decides to execute the command

### editor.command.query
*Type:* STRUCT
A query that controls command availability and provides context to its handler functions

**Members**

- `selection?` (editor.command.query.selection) - current selection request
- `active_view?` (editor.command.query.active_view) - current active editor view request
- `argument?` (true) - set to true to provide the command argument to the handler functions

### editor.command.query.active_view
*Type:* STRUCT
Active editor view requested by an editor command

**Members**

- `type` ("code"|"scene"|"html"|"form") - active editor view type

### editor.command.query.selection
*Type:* STRUCT
Selection requested by an editor command

**Members**

- `type` ("resource"|"outline"|"scene") - selection type
- `cardinality` ("one"|"many") - either the first selected item or all selected items

### editor.component
*Type:* TYPEDEF
Editor UI component

**Parameters**

- `value` (userdata) - editor UI component

### editor.create_directory
*Type:* FUNCTION
Create a directory if it does not exist, and all non-existent parent directories.
Throws an error if the directory can't be created.

**Parameters**

- `resource_path` (string) - Resource path (starting with <code>/</code>)

**Examples**

```
editor.create_directory("/assets/gen")

```

### editor.create_resources
*Type:* FUNCTION
Create resources (including non-existent parent directories).
Throws an error if any of the provided resource paths already exist

**Parameters**

- `resources` ((string|editor.create_resources.resource)[]) - resource paths (strings starting with <code>/</code>) or pairs containing a resource path and optional content

**Examples**

Create a single resource from template:
```
editor.create_resources({
  "/npc.go"
})

```

Create multiple resources:
```
editor.create_resources({
  "/npc.go",
  "/levels/1.collection",
  "/levels/2.collection",
})

```

Create a resource with custom content:
```
editor.create_resources({
  {"/npc.script", "go.property('hp', 100)"}
})

```

### editor.create_resources.resource
*Type:* TYPEDEF
A resource definition used by editor.create_resources

**Parameters**

- `value` ({[1]:string, [2]?:string}) - a resource definition used by editor.create_resources

### editor.delete_directory
*Type:* FUNCTION
Delete a directory if it exists, and all existent child directories and files.
Throws an error if the directory can't be deleted.

**Parameters**

- `resource_path` (string) - Resource path (starting with <code>/</code>)

**Examples**

```
editor.delete_directory("/assets/gen")

```

### editor.editor_sha1
*Type:* VARIABLE
A string, SHA1 of Defold editor

### editor.engine_sha1
*Type:* VARIABLE
A string, SHA1 of Defold engine

### editor.execute
*Type:* FUNCTION
Execute a shell command.
Any shell command arguments should be provided as separate argument strings to this function. If the exit code of the process is not zero, this function throws error. By default, the function returns nil, but it can be configured to capture the output of the shell command as string and return it — set out option to "capture" to do it.By default, after this shell command is executed, the editor will reload resources from disk.

**Parameters**

- `command` (string) - Shell command name to execute
- `...` (string) (optional) - Optional shell command arguments
- `options` (editor.execute.options) (optional) - execution options

**Returns**

- `result` (nil | string) - If <code>out</code> option is set to <code>"capture"</code>, returns the output as string with trimmed trailing newlines. Otherwise, returns <code>nil</code>.

**Examples**

Make a directory with spaces in it:
```
editor.execute("mkdir", "new dir")

```

Read the git status:
```
local status = editor.execute("git", "status", "--porcelain", {
  reload_resources = false,
  out = "capture"
})

```

### editor.execute.options
*Type:* STRUCT
Options for editor.execute

**Members**

- `reload_resources?` (boolean) - whether the editor reloads resources from disk after the command is executed; defaults to true
- `out?` ("pipe"|"capture"|"discard") - standard output mode; defaults to <code>"pipe"</code>
- `err?` ("pipe"|"stdout"|"discard") - standard error output mode; defaults to <code>"pipe"</code>

### editor.external_file_attributes
*Type:* FUNCTION
Query information about file system path

**Parameters**

- `path` (string) - External file path, resolved against project root if relative

**Returns**

- `attributes` (editor.external_file_attributes.result) - external file attributes

### editor.external_file_attributes.result
*Type:* STRUCT
External file attributes

**Members**

- `path` (string) - resolved file path
- `exists` (boolean) - whether there is a file system entry at the path
- `is_file` (boolean) - whether the path corresponds to a file
- `is_directory` (boolean) - whether the path corresponds to a directory

### editor.fetch_libraries
*Type:* FUNCTION
Download the latest version of the project library dependencies and reload library-provided editor scripts.
This function may replace library-provided editor commands, hooks, routes, and UI contributed by editor scripts, so it should typically be the last operation performed by a command.

### editor.get
*Type:* FUNCTION
Get a value of a node property inside the editor.
Some properties might be read-only, and some might be unavailable in different contexts, so you should use editor.can_get() before reading them and editor.can_set() before making the editor set them.

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `value` (any) - property value

### editor.image
*Type:* TYPEDEF
Image loaded for reading by an editor script

**Parameters**

- `value` (userdata) - image loaded for reading by an editor script

### editor.message
*Type:* TYPEDEF
Localizable editor message

**Parameters**

- `value` (userdata) - localizable editor message

### editor.open_external_file
*Type:* FUNCTION
Open a file in a registered application

**Parameters**

- `path` (string) - file path

### editor.platform
*Type:* VARIABLE
Editor platform id.
A string, either:
- "x86_64-win32"
- "x86_64-macos"
- "arm64-macos"
- "x86_64-linux"

### editor.prefs.get
*Type:* FUNCTION
Get preference value
The schema for the preference value should be defined beforehand.

**Parameters**

- `key` (string) - dot-separated preference key path

**Returns**

- `value` (any) - current pref value or default if a schema for the key path exists, nil otherwise

### editor.prefs.is_set
*Type:* FUNCTION
Check if preference value is explicitly set
The schema for the preference value should be defined beforehand.

**Parameters**

- `key` (string) - dot-separated preference key path

**Returns**

- `value` (boolean) - flag indicating if the value is explicitly set

### editor.prefs.schema.array
*Type:* FUNCTION
array schema

**Parameters**

- `opts` (editor.prefs.schema.array.options) - schema options

**Returns**

- `value` (editor.schema) - Prefs schema

### editor.prefs.schema.array.options
*Type:* STRUCT
Options for editor.prefs.schema.array

**Members**

- `item` (editor.schema) - array item schema
- `default?` (any[]) - default value
- `scope?` (editor.prefs.SCOPE) - preference scope; global values are shared by every project on this computer, while project values are stored separately per project

### editor.prefs.schema.boolean
*Type:* FUNCTION
boolean schema

**Parameters**

- `opts` (editor.prefs.schema.boolean.options) (optional) - schema options

**Returns**

- `value` (editor.schema) - Prefs schema

### editor.prefs.schema.boolean.options
*Type:* STRUCT
Options for editor.prefs.schema.boolean

**Members**

- `default?` (boolean) - default value
- `scope?` (editor.prefs.SCOPE) - preference scope; global values are shared by every project on this computer, while project values are stored separately per project

### editor.prefs.schema.enum
*Type:* FUNCTION
enum value schema

**Parameters**

- `opts` (editor.prefs.schema.enum.options) - schema options

**Returns**

- `value` (editor.schema) - Prefs schema

### editor.prefs.schema.enum.options
*Type:* STRUCT
Options for editor.prefs.schema.enum

**Members**

- `values` ((nil|boolean|number|string)[]) - allowed values, must be scalar (nil, boolean, number or string)
- `default?` (any) - default value
- `scope?` (editor.prefs.SCOPE) - preference scope; global values are shared by every project on this computer, while project values are stored separately per project

### editor.prefs.schema.integer
*Type:* FUNCTION
integer schema

**Parameters**

- `opts` (editor.prefs.schema.integer.options) (optional) - schema options

**Returns**

- `value` (editor.schema) - Prefs schema

### editor.prefs.schema.integer.options
*Type:* STRUCT
Options for editor.prefs.schema.integer

**Members**

- `default?` (integer) - default value
- `scope?` (editor.prefs.SCOPE) - preference scope; global values are shared by every project on this computer, while project values are stored separately per project

### editor.prefs.schema.keyword
*Type:* FUNCTION
keyword schema
A keyword is a short string that is interned within the editor runtime, useful e.g. for identifiers

**Parameters**

- `opts` (editor.prefs.schema.keyword.options) (optional) - schema options

**Returns**

- `value` (editor.schema) - Prefs schema

### editor.prefs.schema.keyword.options
*Type:* STRUCT
Options for editor.prefs.schema.keyword

**Members**

- `default?` (string) - default value
- `scope?` (editor.prefs.SCOPE) - preference scope; global values are shared by every project on this computer, while project values are stored separately per project

### editor.prefs.schema.number
*Type:* FUNCTION
floating-point number schema

**Parameters**

- `opts` (editor.prefs.schema.number.options) (optional) - schema options

**Returns**

- `value` (editor.schema) - Prefs schema

### editor.prefs.schema.number.options
*Type:* STRUCT
Options for editor.prefs.schema.number

**Members**

- `default?` (number) - default value
- `scope?` (editor.prefs.SCOPE) - preference scope; global values are shared by every project on this computer, while project values are stored separately per project

### editor.prefs.schema.object
*Type:* FUNCTION
heterogeneous object schema

**Parameters**

- `opts` (editor.prefs.schema.object.options) - schema options

**Returns**

- `value` (editor.schema) - Prefs schema

### editor.prefs.schema.object.options
*Type:* STRUCT
Options for editor.prefs.schema.object

**Members**

- `properties` (table<string, editor.schema>) - a table from property key (string) to value schema
- `default?` (table<string, any>) - default value
- `scope?` (editor.prefs.SCOPE) - preference scope; global values are shared by every project on this computer, while project values are stored separately per project

### editor.prefs.schema.object_of
*Type:* FUNCTION
homogeneous object schema

**Parameters**

- `opts` (editor.prefs.schema.object_of.options) - schema options

**Returns**

- `value` (editor.schema) - Prefs schema

### editor.prefs.schema.object_of.options
*Type:* STRUCT
Options for editor.prefs.schema.object_of

**Members**

- `key` (editor.schema) - table key schema
- `val` (editor.schema) - table value schema
- `default?` (table<any, any>) - default value
- `scope?` (editor.prefs.SCOPE) - preference scope; global values are shared by every project on this computer, while project values are stored separately per project

### editor.prefs.schema.one_of
*Type:* FUNCTION
one of schema

**Parameters**

- `opts` (editor.prefs.schema.one_of.options) - schema options

**Returns**

- `value` (editor.schema) - Prefs schema

### editor.prefs.schema.one_of.options
*Type:* STRUCT
Options for editor.prefs.schema.one_of

**Members**

- `schemas` (editor.schema[]) - alternative schemas
- `default?` (any) - default value
- `scope?` (editor.prefs.SCOPE) - preference scope; global values are shared by every project on this computer, while project values are stored separately per project

### editor.prefs.schema.password
*Type:* FUNCTION
password schema
A password is a string that is encrypted when stored in a preference file

**Parameters**

- `opts` (editor.prefs.schema.password.options) (optional) - schema options

**Returns**

- `value` (editor.schema) - Prefs schema

### editor.prefs.schema.password.options
*Type:* STRUCT
Options for editor.prefs.schema.password

**Members**

- `default?` (string) - default value
- `scope?` (editor.prefs.SCOPE) - preference scope; global values are shared by every project on this computer, while project values are stored separately per project

### editor.prefs.schema.set
*Type:* FUNCTION
set schema
Set is represented as a lua table with true values

**Parameters**

- `opts` (editor.prefs.schema.set.options) - schema options

**Returns**

- `value` (editor.schema) - Prefs schema

### editor.prefs.schema.set.options
*Type:* STRUCT
Options for editor.prefs.schema.set

**Members**

- `item` (editor.schema) - set item schema
- `default?` (table<any, true>) - default value
- `scope?` (editor.prefs.SCOPE) - preference scope; global values are shared by every project on this computer, while project values are stored separately per project

### editor.prefs.schema.string
*Type:* FUNCTION
string schema

**Parameters**

- `opts` (editor.prefs.schema.string.options) (optional) - schema options

**Returns**

- `value` (editor.schema) - Prefs schema

### editor.prefs.schema.string.options
*Type:* STRUCT
Options for editor.prefs.schema.string

**Members**

- `default?` (string) - default value
- `scope?` (editor.prefs.SCOPE) - preference scope; global values are shared by every project on this computer, while project values are stored separately per project

### editor.prefs.schema.tuple
*Type:* FUNCTION
tuple schema
A tuple is a fixed-length array where each item has its own defined type

**Parameters**

- `opts` (editor.prefs.schema.tuple.options) - schema options

**Returns**

- `value` (editor.schema) - Prefs schema

### editor.prefs.schema.tuple.options
*Type:* STRUCT
Options for editor.prefs.schema.tuple

**Members**

- `items` (editor.schema[]) - schemas for the items
- `default?` (any[]) - default value
- `scope?` (editor.prefs.SCOPE) - preference scope; global values are shared by every project on this computer, while project values are stored separately per project

### editor.prefs.SCOPE
*Type:* ENUM
Constants for scope enums

**Parameters**

- `value` (string) - enum value

**Members**

- `editor.prefs.SCOPE.GLOBAL` - <code>"global"</code>
- `editor.prefs.SCOPE.PROJECT` - <code>"project"</code>

### editor.prefs.set
*Type:* FUNCTION
Set preference value
The schema for the preference value should be defined beforehand.

**Parameters**

- `key` (string) - dot-separated preference key path
- `value` (any) - new pref value to set

### editor.properties
*Type:* FUNCTION
List property names for a node.
The result is context-sensitive and can vary by node/resource type and editor state. Returned names are readable with editor.get(node, property). Mutating capabilities are per-property; use editor.can_set(), editor.can_reset(), editor.can_add(), and editor.can_reorder() to check which operations are supported.

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor

**Returns**

- `properties` (string[]) - sorted unique editor property names available in the current context

### editor.resource_attributes
*Type:* FUNCTION
Query information about a project resource

**Parameters**

- `resource_path` (string) - Resource path (starting with <code>/</code>)

**Returns**

- `value` (editor.resource_attributes.result) - resource attributes

### editor.resource_attributes.result
*Type:* STRUCT
Project resource attributes

**Members**

- `exists` (boolean) - whether a resource identified by the path exists in the project
- `is_file` (boolean) - whether the resource represents a file with some content
- `is_directory` (boolean) - whether the resource represents a directory

### editor.save
*Type:* FUNCTION
Persist any unsaved changes to disk

### editor.schema
*Type:* TYPEDEF
Editor preference schema

**Parameters**

- `value` (userdata) - editor preference schema

### editor.tiles
*Type:* TYPEDEF
Unbounded two-dimensional grid of tiles

**Parameters**

- `value` (userdata) - unbounded two-dimensional grid of tiles

### editor.transact
*Type:* FUNCTION
Change the editor state in a single, undoable transaction

**Parameters**

- `txs` (editor.transaction_step[]) - An array of transaction steps created using <code>editor.tx.*</code> functions

### editor.transaction_step
*Type:* TYPEDEF
Editor transaction step

**Parameters**

- `value` (userdata) - editor transaction step

### editor.tx.add
*Type:* FUNCTION
Create a transaction step that will add a child item to a node's list property when transacted with editor.transact().

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)
- `value` (table<string, any>) - Added item for the property, a table from property key to either a valid <code>editor.tx.set()</code>-able value, or an array of valid <code>editor.tx.add()</code>-able values

**Returns**

- `tx` (editor.transaction_step) - A transaction step

### editor.tx.clear
*Type:* FUNCTION
Create a transaction step that will remove all items from node's list property when transacted with editor.transact().

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `tx` (editor.transaction_step) - A transaction step

### editor.tx.remove
*Type:* FUNCTION
Create a transaction step that will remove a child node from the node's list property when transacted with editor.transact().

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)
- `child_node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor

**Returns**

- `tx` (editor.transaction_step) - A transaction step

### editor.tx.reorder
*Type:* FUNCTION
Create a transaction step that reorders child nodes in a node list defined by the property if supported (see editor.can_reorder())

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)
- `child_nodes` (any[]) - array of child nodes (the same as returned by <code>editor.get(node, property)</code>) in new order

**Returns**

- `tx` (editor.transaction_step) - A transaction step

### editor.tx.reset
*Type:* FUNCTION
Create a transaction step that will reset an overridden property to its default value when transacted with editor.transact().

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `tx` (editor.transaction_step) - A transaction step

### editor.tx.set
*Type:* FUNCTION
Create transaction step that will set the node's property to a supplied value when transacted with editor.transact().

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)
- `value` (any) - A new value for the property

**Returns**

- `tx` (editor.transaction_step) - A transaction step

### editor.ui.ALIGNMENT
*Type:* ENUM
Constants for alignment enums

**Parameters**

- `value` (string) - enum value

**Members**

- `editor.ui.ALIGNMENT.TOP_LEFT` - <code>"top-left"</code>
- `editor.ui.ALIGNMENT.TOP` - <code>"top"</code>
- `editor.ui.ALIGNMENT.TOP_RIGHT` - <code>"top-right"</code>
- `editor.ui.ALIGNMENT.LEFT` - <code>"left"</code>
- `editor.ui.ALIGNMENT.CENTER` - <code>"center"</code>
- `editor.ui.ALIGNMENT.RIGHT` - <code>"right"</code>
- `editor.ui.ALIGNMENT.BOTTOM_LEFT` - <code>"bottom-left"</code>
- `editor.ui.ALIGNMENT.BOTTOM` - <code>"bottom"</code>
- `editor.ui.ALIGNMENT.BOTTOM_RIGHT` - <code>"bottom-right"</code>

### editor.ui.button
*Type:* FUNCTION
Button with a label and/or an icon

**Parameters**

- `props` (editor.ui.button.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.button.props
*Type:* STRUCT
Properties for editor.ui.button

**Members**

- `on_pressed?` (function) - button press callback, will be invoked without arguments when the user presses the button
- `text?` (string|editor.message) - the text, either a string or a localization message
- `text_alignment?` (editor.ui.TEXT_ALIGNMENT) - text alignment within paragraph bounds
- `icon?` (editor.ui.ICON) - predefined icon name
- `enabled?` (boolean) - determines if the input component can be interacted with
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.check_box
*Type:* FUNCTION
Check box with a label

**Parameters**

- `props` (editor.ui.check_box.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.check_box.props
*Type:* STRUCT
Properties for editor.ui.check_box

**Members**

- `value?` (boolean) - determines if the checkbox should appear checked
- `on_value_changed?` (function) - change callback, will receive the new value
- `indeterminate?` (boolean) - determines if the checkbox should appear in the mixed state
- `text?` (string|editor.message) - the text, either a string or a localization message
- `text_alignment?` (editor.ui.TEXT_ALIGNMENT) - text alignment within paragraph bounds
- `issue?` (editor.ui.issue|false) - issue related to the input, or false if there is no issue
- `tooltip?` (string|editor.message) - tooltip message shown on hover; either a string or a localization message
- `enabled?` (boolean) - determines if the input component can be interacted with
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.COLOR
*Type:* ENUM
Constants for color enums

**Parameters**

- `value` (string) - enum value

**Members**

- `editor.ui.COLOR.TEXT` - <code>"text"</code>
- `editor.ui.COLOR.HINT` - <code>"hint"</code>
- `editor.ui.COLOR.OVERRIDE` - <code>"override"</code>
- `editor.ui.COLOR.WARNING` - <code>"warning"</code>
- `editor.ui.COLOR.ERROR` - <code>"error"</code>

### editor.ui.component
*Type:* FUNCTION
Convert a function to a UI component.
The wrapped function may call any hooks functions (editor.ui.use_*), but on any function invocation, the hooks calls must be the same, and in the same order. This means that hooks should not be used inside loops and conditions or after a conditional return statement.
The grow, row_span, and column_span props are supported automatically.

**Parameters**

- `fn` (fun(props:T):editor.component) - function, will receive a single table of props when called

**Returns**

- `value` (fun(props:T):editor.component) - decorated component function that may be invoked with a props table to create a component

### editor.ui.dialog
*Type:* FUNCTION
Dialog component, a top-level window component that can't be used as a child of other components

**Parameters**

- `props` (editor.ui.dialog.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.dialog.props
*Type:* STRUCT
Properties for editor.ui.dialog

**Members**

- `title` (string|editor.message) - OS dialog window title, either a string or a localization message
- `header?` (editor.component|false) - top part of the dialog, defaults to <code>editor.ui.heading({text = props.title})</code>
- `content?` (editor.component|false) - content of the dialog
- `width?` (number) - initial width of the dialog window in pixels
- `height?` (number) - initial height of the dialog window in pixels
- `resizable?` (boolean) - determines if the dialog window can be resized by the user
- `buttons?` ((editor.component|false)[]) - array of <code>editor.ui.dialog_button(...)</code> components, footer of the dialog. Defaults to a single Close button
- `modal?` (boolean) - if set to <code>false</code>, the dialog window stays on top but does not block interaction with the editor

### editor.ui.dialog_button
*Type:* FUNCTION
Dialog button shown in the footer of a dialog

**Parameters**

- `props` (editor.ui.dialog_button.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.dialog_button.props
*Type:* STRUCT
Properties for editor.ui.dialog_button

**Members**

- `text` (string|editor.message) - button text, either a string or a localization message
- `result?` (any) - value returned by <code>editor.ui.show_dialog(...)</code> if this button is pressed
- `default?` (boolean) - if set, pressing <code>Enter</code> in the dialog will trigger this button
- `cancel?` (boolean) - if set, pressing <code>Escape</code> in the dialog will trigger this button
- `enabled?` (boolean) - determines if the button can be interacted with

### editor.ui.external_file_field
*Type:* FUNCTION
Input component for selecting files from the file system

**Parameters**

- `props` (editor.ui.external_file_field.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.external_file_field.props
*Type:* STRUCT
Properties for editor.ui.external_file_field

**Members**

- `value?` (string) - file or directory path; resolved against project root if relative
- `on_value_changed?` (function) - value change callback, will receive the absolute path of a selected file/folder or nil if the field was cleared; even though the selector dialog allows selecting only files, it's possible to receive directories and non-existent file system entries using text field input
- `title?` (string|editor.message) - OS window title, either a string or a localization message
- `filters?` (editor.ui.external_file_filter[]) - File filters
- `issue?` (editor.ui.issue|false) - issue related to the input, or false if there is no issue
- `tooltip?` (string|editor.message) - tooltip message shown on hover; either a string or a localization message
- `enabled?` (boolean) - determines if the input component can be interacted with
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.external_file_filter
*Type:* STRUCT
External file dialog filter

**Members**

- `description` (string|editor.message) - text explaining the filter, either a literal string like <code>"Text files (*.txt)"</code> or a localization message
- `extensions` (string[]) - file extension patterns, e.g. <code>"<em>.txt"</code>, <code>"</em>.*"</code>, or <code>"game.project"</code>

### editor.ui.grid
*Type:* FUNCTION
Layout container that places its children in a 2D grid

**Parameters**

- `props` (editor.ui.grid.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.grid.constraint
*Type:* STRUCT
Grid row or column constraint

**Members**

- `grow?` (boolean) - whether the row or column should grow to fill available space

### editor.ui.grid.props
*Type:* STRUCT
Properties for editor.ui.grid

**Members**

- `children?` (((editor.component|false)[]|false)[]) - array of arrays of child components
- `rows?` ((editor.ui.grid.constraint|false)[]) - separate configuration for each row
- `columns?` ((editor.ui.grid.constraint|false)[]) - separate configuration for each column
- `padding?` (editor.ui.PADDING|number) - empty space from the edges of the container to its children, either a predefined padding value or a non-negative number of pixels
- `spacing?` (editor.ui.SPACING|number) - empty space between child components, either a predefined spacing value or a non-negative number of pixels; defaults to <code>editor.ui.SPACING.MEDIUM</code>
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.heading
*Type:* FUNCTION
A text heading

**Parameters**

- `props` (editor.ui.heading.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.heading.props
*Type:* STRUCT
Properties for editor.ui.heading

**Members**

- `text?` (string|editor.message) - the text, either a string or a localization message
- `text_alignment?` (editor.ui.TEXT_ALIGNMENT) - text alignment within paragraph bounds
- `color?` (editor.ui.COLOR) - semantic color, defaults to <code>editor.ui.COLOR.TEXT</code>
- `word_wrap?` (boolean) - determines if the lines of text are word-wrapped when they don't fit in the assigned bounds, defaults to true
- `style?` (editor.ui.HEADING_STYLE) - heading style, defaults to <code>editor.ui.HEADING_STYLE.H3</code>
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.HEADING_STYLE
*Type:* ENUM
Constants for heading style enums

**Parameters**

- `value` (string) - enum value

**Members**

- `editor.ui.HEADING_STYLE.H1` - <code>"h1"</code>
- `editor.ui.HEADING_STYLE.H2` - <code>"h2"</code>
- `editor.ui.HEADING_STYLE.H3` - <code>"h3"</code>
- `editor.ui.HEADING_STYLE.H4` - <code>"h4"</code>
- `editor.ui.HEADING_STYLE.H5` - <code>"h5"</code>
- `editor.ui.HEADING_STYLE.H6` - <code>"h6"</code>
- `editor.ui.HEADING_STYLE.DIALOG` - <code>"dialog"</code>
- `editor.ui.HEADING_STYLE.FORM` - <code>"form"</code>

### editor.ui.horizontal
*Type:* FUNCTION
Layout container that places its children in a horizontal row one after another

**Parameters**

- `props` (editor.ui.horizontal.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.horizontal.props
*Type:* STRUCT
Properties for editor.ui.horizontal

**Members**

- `children?` ((editor.component|false)[]) - array of child components
- `padding?` (editor.ui.PADDING|number) - empty space from the edges of the container to its children, either a predefined padding value or a non-negative number of pixels
- `spacing?` (editor.ui.SPACING|number) - empty space between child components, either a predefined spacing value or a non-negative number of pixels; defaults to <code>editor.ui.SPACING.MEDIUM</code>
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.ICON
*Type:* ENUM
Constants for icon enums

**Parameters**

- `value` (string) - enum value

**Members**

- `editor.ui.ICON.OPEN_RESOURCE` - <code>"open-resource"</code>
- `editor.ui.ICON.PLUS` - <code>"plus"</code>
- `editor.ui.ICON.MINUS` - <code>"minus"</code>
- `editor.ui.ICON.CLEAR` - <code>"clear"</code>

### editor.ui.icon
*Type:* FUNCTION
An icon from a predefined set

**Parameters**

- `props` (editor.ui.icon.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.icon.props
*Type:* STRUCT
Properties for editor.ui.icon

**Members**

- `icon` (editor.ui.ICON) - predefined icon name
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.image
*Type:* FUNCTION
An image

**Parameters**

- `props` (editor.ui.image.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.image.props
*Type:* STRUCT
Properties for editor.ui.image

**Members**

- `image` (string) - either a resource path (starts with <code>/</code>), or an URL
- `width?` (number) - width of the image view, the image will be fit inside it while preserving its aspect ratio
- `height?` (number) - height of the image view, the image will be fit inside it while preserving its aspect ratio
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.integer_field
*Type:* FUNCTION
Integer input component based on a text field, reports changes on commit (Enter or focus loss)

**Parameters**

- `props` (editor.ui.integer_field.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.integer_field.props
*Type:* STRUCT
Properties for editor.ui.integer_field

**Members**

- `value?` (any) - value
- `on_value_changed?` (function) - value change callback, will receive the new value
- `issue?` (editor.ui.issue|false) - issue related to the input, or false if there is no issue
- `tooltip?` (string|editor.message) - tooltip message shown on hover; either a string or a localization message
- `enabled?` (boolean) - determines if the input component can be interacted with
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.issue
*Type:* STRUCT
Issue associated with an input component

**Members**

- `severity` (editor.ui.ISSUE_SEVERITY) - issue severity
- `message` (string|editor.message) - issue message shown in a tooltip, either a string or a localization message

### editor.ui.ISSUE_SEVERITY
*Type:* ENUM
Constants for issue severity enums

**Parameters**

- `value` (string) - enum value

**Members**

- `editor.ui.ISSUE_SEVERITY.WARNING` - <code>"warning"</code>
- `editor.ui.ISSUE_SEVERITY.ERROR` - <code>"error"</code>

### editor.ui.label
*Type:* FUNCTION
Label intended for use with input components

**Parameters**

- `props` (editor.ui.label.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.label.props
*Type:* STRUCT
Properties for editor.ui.label

**Members**

- `text?` (string|editor.message) - the text, either a string or a localization message
- `text_alignment?` (editor.ui.TEXT_ALIGNMENT) - text alignment within paragraph bounds
- `color?` (editor.ui.COLOR) - semantic color, defaults to <code>editor.ui.COLOR.TEXT</code>
- `tooltip?` (string|editor.message) - tooltip message shown on hover; either a string or a localization message
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.number_field
*Type:* FUNCTION
Number input component based on a text field, reports changes on commit (Enter or focus loss)

**Parameters**

- `props` (editor.ui.number_field.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.number_field.props
*Type:* STRUCT
Properties for editor.ui.number_field

**Members**

- `value?` (any) - value
- `on_value_changed?` (function) - value change callback, will receive the new value
- `issue?` (editor.ui.issue|false) - issue related to the input, or false if there is no issue
- `tooltip?` (string|editor.message) - tooltip message shown on hover; either a string or a localization message
- `enabled?` (boolean) - determines if the input component can be interacted with
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.open_resource
*Type:* FUNCTION
Open a resource using its primary or selected view, either in the editor or in a third-party app. Code and Text views accept a one-based cursor or range in args: {line = 42}, {line = 42, column = 12}, or {from = {line = 42, column = 12}, to = {line = 43, column = 4}}

**Parameters**

- `resource_path` (string) - Resource path (starting with <code>/</code>)
- `view` (string) (optional) - View to open: <code>"code"</code>, <code>"text"</code>, <code>"scene"</code>, <code>"html"</code>, or <code>"form"</code>
- `args` (any) (optional) - View-specific open arguments; requires <code>view</code>. Currently supported by Code and Text views.

### editor.ui.ORIENTATION
*Type:* ENUM
Constants for orientation enums

**Parameters**

- `value` (string) - enum value

**Members**

- `editor.ui.ORIENTATION.VERTICAL` - <code>"vertical"</code>
- `editor.ui.ORIENTATION.HORIZONTAL` - <code>"horizontal"</code>

### editor.ui.PADDING
*Type:* ENUM
Constants for padding enums

**Parameters**

- `value` (string) - enum value

**Members**

- `editor.ui.PADDING.NONE` - <code>"none"</code>
- `editor.ui.PADDING.SMALL` - <code>"small"</code>
- `editor.ui.PADDING.MEDIUM` - <code>"medium"</code>
- `editor.ui.PADDING.LARGE` - <code>"large"</code>

### editor.ui.paragraph
*Type:* FUNCTION
A paragraph of text

**Parameters**

- `props` (editor.ui.paragraph.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.paragraph.props
*Type:* STRUCT
Properties for editor.ui.paragraph

**Members**

- `text?` (string|editor.message) - the text, either a string or a localization message
- `text_alignment?` (editor.ui.TEXT_ALIGNMENT) - text alignment within paragraph bounds
- `color?` (editor.ui.COLOR) - semantic color, defaults to <code>editor.ui.COLOR.TEXT</code>
- `word_wrap?` (boolean) - determines if the lines of text are word-wrapped when they don't fit in the assigned bounds, defaults to true
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.resource_field
*Type:* FUNCTION
Input component for selecting project resources

**Parameters**

- `props` (editor.ui.resource_field.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.resource_field.props
*Type:* STRUCT
Properties for editor.ui.resource_field

**Members**

- `value?` (string) - resource path (must start with <code>/</code>)
- `on_value_changed?` (function) - value change callback, will receive either resource path of a selected resource or nil when the field is cleared; even though the resource selector dialog allows filtering on resource extensions, it's possible to receive resources with other extensions and non-existent resources using text field input
- `title?` (string|editor.message) - dialog title, either a string or a localization message, defaults to <code>localization.message("dialog.select-resource.title")</code>
- `extensions?` (string[]) - if specified, restricts selectable resources in the dialog to specified file extensions; e.g. <code>{"collection", "go"}</code>
- `issue?` (editor.ui.issue|false) - issue related to the input, or false if there is no issue
- `tooltip?` (string|editor.message) - tooltip message shown on hover; either a string or a localization message
- `enabled?` (boolean) - determines if the input component can be interacted with
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.scroll
*Type:* FUNCTION
Layout container that optionally shows scroll bars if child contents overflow the assigned bounds

**Parameters**

- `props` (editor.ui.scroll.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.scroll.props
*Type:* STRUCT
Properties for editor.ui.scroll

**Members**

- `content` (editor.component) - content component
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.select_box
*Type:* FUNCTION
Dropdown select box with an array of options

**Parameters**

- `props` (editor.ui.select_box.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.select_box.props
*Type:* STRUCT
Properties for editor.ui.select_box

**Members**

- `value?` (any) - selected value
- `on_value_changed?` (function) - change callback, will receive the selected value
- `options?` (any[]) - array of selectable options
- `to_string?` (function) - function that converts an item to a string (or a localization message); defaults to <code>tostring</code>
- `issue?` (editor.ui.issue|false) - issue related to the input, or false if there is no issue
- `tooltip?` (string|editor.message) - tooltip message shown on hover; either a string or a localization message
- `enabled?` (boolean) - determines if the input component can be interacted with
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.separator
*Type:* FUNCTION
Thin line for visual content separation, by default horizontal and aligned to center

**Parameters**

- `props` (editor.ui.separator.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.separator.props
*Type:* STRUCT
Properties for editor.ui.separator

**Members**

- `orientation?` (editor.ui.ORIENTATION) - separator line orientation, <code>editor.ui.ORIENTATION.VERTICAL</code> or <code>editor.ui.ORIENTATION.HORIZONTAL</code>
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.show_dialog
*Type:* FUNCTION
Show a dialog and await a result

**Parameters**

- `dialog` (editor.component) - a component that resolves to <code>editor.ui.dialog(...)</code>

**Returns**

- `value` (any) - dialog result, the value used as a <code>result</code> prop in a <code>editor.ui.dialog_button({...})</code> selected by the user, or <code>nil</code> if the dialog was closed and there was no <code>cancel = true</code> dialog button with <code>result</code> prop set

### editor.ui.show_external_directory_dialog
*Type:* FUNCTION
Show a modal OS directory selection dialog and await a result

**Parameters**

- `opts` (editor.ui.show_external_directory_dialog.options) (optional) - dialog options

**Returns**

- `value` (string | nil) - either absolute directory path or nil if user canceled directory selection

### editor.ui.show_external_directory_dialog.options
*Type:* STRUCT
Options for editor.ui.show_external_directory_dialog

**Members**

- `path?` (string) - initial file or directory path; resolved against project root if relative
- `title?` (string|editor.message) - OS window title, either a string or a localization message

### editor.ui.show_external_file_dialog
*Type:* FUNCTION
Show a modal OS file selection dialog and await a result

**Parameters**

- `opts` (editor.ui.show_external_file_dialog.options) (optional) - dialog options

**Returns**

- `value` (string | nil) - either absolute file path or nil if user canceled file selection

### editor.ui.show_external_file_dialog.options
*Type:* STRUCT
Options for editor.ui.show_external_file_dialog

**Members**

- `path?` (string) - initial file or directory path; resolved against project root if relative
- `title?` (string|editor.message) - OS window title, either a string or a localization message
- `filters?` (editor.ui.external_file_filter[]) - File filters

### editor.ui.show_resource_dialog
*Type:* FUNCTION
Show a modal resource selection dialog and await a result

**Parameters**

- `opts` (editor.ui.show_resource_dialog.options) (optional) - dialog options

**Returns**

- `value` (string | string[] | nil) - if user made no selection, returns <code>nil</code>. Otherwise, if selection mode is <code>"single"</code>, returns selected resource path; otherwise returns a non-empty array of selected resource paths.

### editor.ui.show_resource_dialog.options
*Type:* STRUCT
Options for editor.ui.show_resource_dialog

**Members**

- `extensions?` (string[]) - if specified, restricts selectable resources in the dialog to specified file extensions; e.g. <code>{"collection", "go"}</code>
- `selection?` ("single"|"multiple") - selection mode, defaults to <code>"single"</code>
- `title?` (string|editor.message) - dialog title, either a string or a localization message, defaults to <code>localization.message("dialog.select-resource.title")</code>

### editor.ui.SPACING
*Type:* ENUM
Constants for spacing enums

**Parameters**

- `value` (string) - enum value

**Members**

- `editor.ui.SPACING.NONE` - <code>"none"</code>
- `editor.ui.SPACING.SMALL` - <code>"small"</code>
- `editor.ui.SPACING.MEDIUM` - <code>"medium"</code>
- `editor.ui.SPACING.LARGE` - <code>"large"</code>

### editor.ui.string_field
*Type:* FUNCTION
String input component based on a text field, reports changes on commit (Enter or focus loss)

**Parameters**

- `props` (editor.ui.string_field.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.string_field.props
*Type:* STRUCT
Properties for editor.ui.string_field

**Members**

- `value?` (any) - value
- `on_value_changed?` (function) - value change callback, will receive the new value
- `issue?` (editor.ui.issue|false) - issue related to the input, or false if there is no issue
- `tooltip?` (string|editor.message) - tooltip message shown on hover; either a string or a localization message
- `enabled?` (boolean) - determines if the input component can be interacted with
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.tab
*Type:* FUNCTION
Tab used in the tabs prop of editor.ui.tabs(...)

**Parameters**

- `props` (editor.ui.tab.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.tab.props
*Type:* STRUCT
Properties for editor.ui.tab

**Members**

- `text` (string|editor.message) - tab header text, either a string or a localization message
- `content?` (editor.component) - tab content component
- `icon?` (editor.component) - tab header icon component
- `enabled?` (boolean) - determines if the tab can be selected

### editor.ui.tabs
*Type:* FUNCTION
Layout container that shows one selected tab content at a time

**Parameters**

- `props` (editor.ui.tabs.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.tabs.props
*Type:* STRUCT
Properties for editor.ui.tabs

**Members**

- `tabs?` ((editor.component|false)[]) - array of <code>editor.ui.tab(...)</code> components
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.ui.TEXT_ALIGNMENT
*Type:* ENUM
Constants for text alignment enums

**Parameters**

- `value` (string) - enum value

**Members**

- `editor.ui.TEXT_ALIGNMENT.LEFT` - <code>"left"</code>
- `editor.ui.TEXT_ALIGNMENT.CENTER` - <code>"center"</code>
- `editor.ui.TEXT_ALIGNMENT.RIGHT` - <code>"right"</code>
- `editor.ui.TEXT_ALIGNMENT.JUSTIFY` - <code>"justify"</code>

### editor.ui.use_memo
*Type:* FUNCTION
A hook that caches the result of a computation between re-renders.
See editor.ui.component for hooks caveats and rules. If any of the arguments to use_memo change during a component refresh (checked with ==), the value will be recomputed.

**Parameters**

- `compute` (function) - function that will be used to compute the cached value
- `...` (any) (optional) - args to the computation function

**Returns**

- `values` (any) - all returned values of the compute function

**Examples**

```
local function increment(n)
    return n + 1
end

local function make_listener(set_count)
    return function()
        set_count(increment)
    end
end

local counter_button = editor.ui.component(function(props)
    local count, set_count = editor.ui.use_state(props.count)
    local on_pressed = editor.ui.use_memo(make_listener, set_count)
    return editor.ui.text_button {
        text = tostring(count),
        on_pressed = on_pressed
    }
end)
```

### editor.ui.use_state
*Type:* FUNCTION
A hook that adds local state to the component.
See editor.ui.component for hooks caveats and rules. If any of the arguments to use_state change during a component refresh (checked with ==), the current state will be reset to the initial one.

**Parameters**

- `init` (any | function) - local state initializer, either initial data structure or function that produces the data structure
- `...` (any) (optional) - used when <code>init</code> is a function, the args are passed to the initializer function

**Returns**

- `state` (any) - current local state, starts with initial state, then may be changed using the returned <code>set_state</code> function
- `set_state` (function) - function that changes the local state and causes the component to refresh. Pass a value to set the new state directly, or pass an updater function that receives the current state and any additional arguments; the updater's return value becomes the new state.

**Examples**

```
local function increment(n)
  return n + 1
end

local counter_button = editor.ui.component(function(props)
  local count, set_count = editor.ui.use_state(props.count)
  return editor.ui.text_button {
    text = tostring(count),
    on_pressed = function()
      set_count(increment)
    end
  }
end)
```

### editor.ui.vertical
*Type:* FUNCTION
Layout container that places its children in a vertical column one after another

**Parameters**

- `props` (editor.ui.vertical.props) - component properties

**Returns**

- `value` (editor.component) - UI component

### editor.ui.vertical.props
*Type:* STRUCT
Properties for editor.ui.vertical

**Members**

- `children?` ((editor.component|false)[]) - array of child components
- `padding?` (editor.ui.PADDING|number) - empty space from the edges of the container to its children, either a predefined padding value or a non-negative number of pixels
- `spacing?` (editor.ui.SPACING|number) - empty space between child components, either a predefined spacing value or a non-negative number of pixels; defaults to <code>editor.ui.SPACING.MEDIUM</code>
- `alignment?` (editor.ui.ALIGNMENT) - alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>
- `grow?` (boolean) - determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container
- `row_span?` (integer) - how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.
- `column_span?` (integer) - how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.

### editor.version
*Type:* VARIABLE
A string, version name of Defold

### http.request
*Type:* FUNCTION
Perform an HTTP request

**Parameters**

- `url` (string) - request URL
- `opts` (http.request.options) (optional) - request options

**Returns**

- `response` (http.request.response) - HTTP response

### http.request.method
*Type:* TYPEDEF
HTTP request method, either a common method or a custom method string

**Parameters**

- `value` ("GET" | "POST" | "PUT" | "PATCH" | "DELETE" | "HEAD" | "OPTIONS" | string) - hTTP request method, either a common method or a custom method string

### http.request.options
*Type:* STRUCT
Options for http.request

**Members**

- `method?` (http.request.method) - request method, defaults to <code>"GET"</code>
- `headers?` (table<string, string>) - request headers
- `body?` (string) - request body
- `as?` ("string"|"json") - response body converter; mutually exclusive with <code>path</code>
- `path?` (string) - destination file path, resolved against project root if relative; mutually exclusive with <code>as</code>

### http.request.response
*Type:* STRUCT
Response returned by http.request

**Members**

- `status` (integer) - response code
- `headers` (table<string, string|string[]>) - response headers, where keys are lowercase and repeated headers have arrays of values
- `body?` (any) - response body, present only when the <code>as</code> option was provided
- `path?` (string) - resolved absolute destination path, present after a successful response was written using the <code>path</code> option

### http.response
*Type:* TYPEDEF
HTTP server response

**Parameters**

- `value` (userdata) - hTTP server response

### http.route
*Type:* TYPEDEF
HTTP server route

**Parameters**

- `value` (userdata) - hTTP server route

### http.server.external_file_response
*Type:* FUNCTION
Create HTTP response that will stream the content of a file defined by the path

**Parameters**

- `path` (string) - External file path, resolved against project root if relative
- `status` (integer) (optional) - HTTP status code, an integer, default 200
- `headers` (table<string, string>) (optional) - HTTP response headers, a table from lower-case header names to header values

**Returns**

- `response` (http.response) - HTTP response value, userdata

### http.server.handler
*Type:* TYPEDEF
HTTP server request handler

**Parameters**

- `value` (fun(request:http.server.request):(http.response|integer|nil, table<string, string>|nil, string|nil)) - hTTP server request handler

### http.server.json_response
*Type:* FUNCTION
Create HTTP response with a JSON value

**Parameters**

- `value` (any) - Any Lua value that may be represented as JSON
- `status` (integer) (optional) - HTTP status code, an integer, default 200
- `headers` (table<string, string>) (optional) - HTTP response headers, a table from lower-case header names to header values

**Returns**

- `response` (http.response) - HTTP response value, userdata

### http.server.local_url
*Type:* CONSTANT
Editor's HTTP server local url

**Parameters**

- `value` (string)

### http.server.port
*Type:* CONSTANT
Editor's HTTP server port

**Parameters**

- `value` (integer)

### http.server.request
*Type:* STRUCT
HTTP server request

**Members**

- `[string]` (any) - route path parameter extracted from a path pattern
- `path` (string) - full matched path, starting with <code>/</code>
- `method` (string) - HTTP request method, e.g. <code>"POST"</code>
- `headers` (table<string, string|string[]>) - request headers, keyed by lowercase header name
- `query?` (string) - query string
- `body?` (any) - request body, whose type depends on the route's <code>as</code> argument

### http.server.resource_response
*Type:* FUNCTION
Create HTTP response that will stream the content of a resource defined by the resource path

**Parameters**

- `resource_path` (string) - Resource path (starting with <code>/</code>)
- `status` (integer) (optional) - HTTP status code, an integer, default 200
- `headers` (table<string, string>) (optional) - HTTP response headers, a table from lower-case header names to header values

**Returns**

- `response` (http.response) - HTTP response value, userdata

### http.server.response
*Type:* FUNCTION
Create HTTP response

**Parameters**

- `status` (integer) (optional) - HTTP status code, an integer, default 200
- `headers` (table<string, string>) (optional) - HTTP response headers, a table from lower-case header names to header values
- `body` (string) (optional) - HTTP response body

**Returns**

- `response` (http.response) - HTTP response value, userdata

### http.server.route
*Type:* FUNCTION
Create route definition for the editor's HTTP server

**Parameters**

- `path` (string) - HTTP URI path, starts with <code>/</code>; may include path patterns (<code>{name}</code> for a single segment and <code>{*name}</code> for the rest of the request path) that will be extracted from the path and provided to the handler as a part of the request
- `method` (string) (optional) - HTTP request method, default <code>"GET"</code>
- `as` ("string" | "json") (optional) - Request body converter, either <code>"string"</code> or <code>"json"</code>; the body will be discarded if not specified
- `openapi` (table<string, any>) (optional) - Optional OpenAPI Operation Object for this route method, exposed from <code>/openapi.json</code>. Must follow <code>https://spec.openapis.org/oas/v3.0.3.html#operation-object</code>.
- `handler` (http.server.handler) - Request handler. Return either a single response value or arguments accepted by <code>http.server.response()</code>.

**Returns**

- `route` (http.route) - HTTP server route

**Examples**

Receive JSON and respond with JSON:
```
http.server.route(
  "/json", "POST", "json",
  function(request)
    pprint(request.body)
    return 200
  end
)

```

Extract parts of the path:
```
http.server.route(
  "/users/{user}/orders",
  function(request)
    print(request.user)
  end
)

```

Simple file server:
```
http.server.route(
  "/files/{*file}",
  function(request)
    local attrs = editor.external_file_attributes(request.file)
    if attrs.is_file then
      return http.server.external_file_response(request.file)
    elseif attrs.is_directory then
      return 400
    else
      return 404
    end
  end
)

```

### http.server.url
*Type:* CONSTANT
Editor's HTTP server url

**Parameters**

- `value` (string)

### image.load_file
*Type:* FUNCTION
Load an image file for reading

**Parameters**

- `path` (string) - External file path, resolved against project root if relative

**Returns**

- `image` (editor.image) - image userdata

### image.pixel
*Type:* FUNCTION
Return the color of a pixel from a loaded image.
Coordinates are 1-based, with 1, 1 at the top-left corner.

**Parameters**

- `image` (editor.image) - image userdata returned by <code>image.load_file()</code>
- `x` (integer) - 1-based horizontal pixel coordinate
- `y` (integer) - 1-based vertical pixel coordinate

**Returns**

- `r` (integer) - red channel, 0-255
- `g` (integer) - green channel, 0-255
- `b` (integer) - blue channel, 0-255
- `a` (integer) - alpha channel, 0-255

### image.pixels
*Type:* FUNCTION
Iterate over pixels in a loaded image.
The iterator returns pixels row by row from top-left to bottom-right. Coordinates are 1-based.

**Parameters**

- `image` (editor.image) - image userdata returned by <code>image.load_file()</code>

**Returns**

- `iterator` (function) - iterator function returning <code>x, y, r, g, b, a</code> for each pixel

**Examples**

```
local img = image.load_file("assets/source.png")
local width, height = image.size(img)
for x, y, r, g, b, a in image.pixels(img) do
  print(x, y, r, g, b, a)
end

```

### image.size
*Type:* FUNCTION
Return the width and height of a loaded image.

**Parameters**

- `image` (editor.image) - image userdata returned by <code>image.load_file()</code>

**Returns**

- `width` (integer) - image width in pixels
- `height` (integer) - image height in pixels

### json.decode
*Type:* FUNCTION
Decode JSON string to Lua value

**Parameters**

- `json` (string) - json data
- `options` (json.decode.options) (optional) - decoding options

### json.decode.options
*Type:* STRUCT
Options for json.decode

**Members**

- `all?` (boolean) - if true, decodes all JSON values in a string and returns an array

### json.encode
*Type:* FUNCTION
Encode Lua value to JSON string

**Parameters**

- `value` (any) - any Lua value that may be represented as JSON

### localization.and_list
*Type:* FUNCTION
Create a message pattern that renders a list with the "and" conjunction (for example: a, b, and c) once it is stringified

**Parameters**

- `items` ((nil|boolean|number|string|editor.message)[]) - array of values; each value may be <code>nil</code>, <code>boolean</code>, <code>number</code>, <code>string</code>, or another <code>message</code> instance

**Returns**

- `message` (editor.message) - a userdata value that, when stringified with <code>tostring()</code>, will produce a localized text according to the currently selected language in the editor

### localization.concat
*Type:* FUNCTION
Create a message pattern that concatenates values (similar to table.concat) and performs the actual concatenation when stringified

**Parameters**

- `items` ((nil|boolean|number|string|editor.message)[]) - array of values; each value may be <code>nil</code>, <code>boolean</code>, <code>number</code>, <code>string</code>, or another <code>message</code> instance
- `separator` (nil | boolean | number | string | editor.message) (optional) - optional separator inserted between values; defaults to an empty string

**Returns**

- `message` (editor.message) - a userdata value that, when stringified with <code>tostring()</code>, will produce a localized text according to the currently selected language in the editor

### localization.message
*Type:* FUNCTION
Create a message pattern for a localization key defined in an .editor_localization file; the actual localization happens when the returned value is stringified

**Parameters**

- `key` (string) - localization key defined in an <code>.editor_localization</code> file
- `vars` (table<string, nil|boolean|number|string|editor.message>) (optional) - optional table with variables to be substituted in the localized string that uses <a href="https://unicode-org.github.io/icu/userguide/format_parse/messages/">ICU Message Format</a> syntax; keys must be strings; values must be either <code>nil</code>, <code>boolean</code>, <code>number</code>, <code>string</code>, or another <code>message</code> instance

**Returns**

- `message` (editor.message) - a userdata value that, when stringified with <code>tostring()</code>, will produce a localized text according to the currently selected language in the editor

### localization.or_list
*Type:* FUNCTION
Create a message pattern that renders a list with the "or" conjunction (for example: a, b, or c) once it is stringified

**Parameters**

- `items` ((nil|boolean|number|string|editor.message)[]) - array of values; each value may be <code>nil</code>, <code>boolean</code>, <code>number</code>, <code>string</code>, or another <code>message</code> instance

**Returns**

- `message` (editor.message) - a userdata value that, when stringified with <code>tostring()</code>, will produce a localized text according to the currently selected language in the editor

### pprint
*Type:* FUNCTION
Pretty-print Lua values

**Parameters**

- `...` (any) - Lua values to pretty-print

### tilemap.tiles.clear
*Type:* FUNCTION
Remove all tiles

**Parameters**

- `tiles` (editor.tiles) - unbounded 2d grid of tiles

**Returns**

- `tiles` (editor.tiles) - unbounded 2d grid of tiles

### tilemap.tiles.get_info
*Type:* FUNCTION
Get full information from a tile at a particular coordinate

**Parameters**

- `tiles` (editor.tiles) - unbounded 2d grid of tiles
- `x` (integer) - x coordinate of a tile
- `y` (integer) - y coordinate of a tile

**Returns**

- `info` (tilemap.tiles.get_info.result | nil) - full tile information, or nil if no tile is set at the coordinate

### tilemap.tiles.get_info.result
*Type:* STRUCT
Full tile information returned by tilemap.tiles.get_info

**Members**

- `index` (integer) - 1-indexed tile index of a tilemap's tilesource
- `h_flip` (boolean) - horizontal flip
- `v_flip` (boolean) - vertical flip
- `rotate_90` (boolean) - whether the tile is rotated 90 degrees clockwise

### tilemap.tiles.get_tile
*Type:* FUNCTION
Get a tile index at a particular coordinate

**Parameters**

- `tiles` (editor.tiles) - unbounded 2d grid of tiles
- `x` (integer) - x coordinate of a tile
- `y` (integer) - y coordinate of a tile

**Returns**

- `tile_index` (integer) - 1-indexed tile index of a tilemap's tilesource

### tilemap.tiles.iterator
*Type:* FUNCTION
Create an iterator over all tiles in a tiles data structure
When iterating using for loop, each iteration returns x, y and tile index of a tile in a tile map

**Parameters**

- `tiles` (editor.tiles) - unbounded 2d grid of tiles

**Returns**

- `iter` (function) - iterator

**Examples**

Iterate over all tiles in a tile map:
```
local layers = editor.get("/level.tilemap", "layers")
for i = 1, #layers do
  local tiles = editor.get(layers[i], "tiles")
  for x, y, i in tilemap.tiles.iterator(tiles) do
    print(x, y, i)
  end
end

```

### tilemap.tiles.new
*Type:* FUNCTION
Create a new unbounded 2d grid data structure for storing tilemap layer tiles

**Returns**

- `tiles` (editor.tiles) - unbounded 2d grid of tiles

### tilemap.tiles.remove
*Type:* FUNCTION
Remove a tile at a particular coordinate

**Parameters**

- `tiles` (editor.tiles) - unbounded 2d grid of tiles
- `x` (integer) - x coordinate of a tile
- `y` (integer) - y coordinate of a tile

**Returns**

- `tiles` (editor.tiles) - unbounded 2d grid of tiles

### tilemap.tiles.set
*Type:* FUNCTION
Set a tile at a particular coordinate

**Parameters**

- `tiles` (editor.tiles) - unbounded 2d grid of tiles
- `x` (integer) - x coordinate of a tile
- `y` (integer) - y coordinate of a tile
- `tile_or_info` (integer | tilemap.tiles.set.info) - Either 1-indexed tile index of a tilemap's tilesource or full tile information

**Returns**

- `tiles` (editor.tiles) - unbounded 2d grid of tiles

### tilemap.tiles.set.info
*Type:* STRUCT
Tile information accepted by tilemap.tiles.set

**Members**

- `index` (integer) - 1-indexed tile index of a tilemap's tilesource
- `h_flip?` (boolean) - horizontal flip
- `v_flip?` (boolean) - vertical flip
- `rotate_90?` (boolean) - whether the tile is rotated 90 degrees clockwise

### zip.METHOD
*Type:* ENUM
Constants for zip compression methods

**Parameters**

- `value` (string) - enum value

**Members**

- `zip.METHOD.DEFLATED` - <code>"deflated"</code> compression method
- `zip.METHOD.STORED` - <code>"stored"</code> compression method, i.e. no compression

### zip.ON_CONFLICT
*Type:* ENUM
Constants defining conflict resolution strategies for zip archive extraction

**Parameters**

- `value` (string) - enum value

**Members**

- `zip.ON_CONFLICT.ERROR` - <code>"error"</code>, any conflict aborts extraction
- `zip.ON_CONFLICT.SKIP` - <code>"skip"</code>, existing file is preserved
- `zip.ON_CONFLICT.OVERWRITE` - <code>"overwrite"</code>, existing file is overwritten

### zip.pack
*Type:* FUNCTION
Create a ZIP archive

**Parameters**

- `output_path` (string) - output zip file path, resolved against project root if relative
- `opts` (zip.pack.options) (optional) - compression options
- `entries` (zip.pack.entries) - files and folders to include in the archive

**Examples**

Archive a file and a folder:
```
zip.pack("build.zip", {"build", "game.project"})

```

Change the location of the files within the archive:
```
zip.pack("build.zip", {
  {"build/wasm-web", "."},
  {"configs/prod.json", "config.json"}
})

```

Create archive without compression (much faster to create the archive, bigger archive file size, allows mmap access):
```
zip.pack("build.zip", {method = zip.METHOD.STORED}, {
  "build",
  "resources"
})

```

Don't compress one of the folders:
```
zip.pack("build.zip", {
  {"assets", method = zip.METHOD.STORED},
  "build/wasm-web"
})

```

Include files from outside the project:
```
zip.pack("build.zip", {
  "build",
  {"../secrets/auth-key.txt", "auth-key.txt"}
})

```

### zip.pack.entries
*Type:* TYPEDEF
Entries included in a ZIP archive

**Parameters**

- `value` ((string|zip.pack.entry)[]) - entries included in a ZIP archive

### zip.pack.entry
*Type:* TYPEDEF
ZIP entry containing a source path, optional archive target path, and optional compression settings

**Parameters**

- `value` ({[1]:string, [2]?:string, method?:zip.METHOD, level?:integer}) - zIP entry containing a source path, optional archive target path, and optional compression settings

### zip.pack.options
*Type:* STRUCT
Options for zip.pack

**Members**

- `method?` (zip.METHOD) - compression method, defaults to <code>zip.METHOD.DEFLATED</code>
- `level?` (integer) - compression level from 0 to 9 for deflated entries; defaults to 6

### zip.unpack
*Type:* FUNCTION
Extract a ZIP archive

**Parameters**

- `archive_path` (string) - zip file path, resolved against project root if relative
- `target_path` (string) (optional) - target path for extraction, defaults to parent of <code>archive_path</code> if omitted
- `opts` (zip.unpack.options) (optional) - extraction options; conflict handling defaults to <code>zip.ON_CONFLICT.ERROR</code>
- `paths` (string[]) (optional) - entries to extract, relative string paths

**Examples**

Extract everything to a build dir:
```
zip.unpack("build/dev/resources.zip")

```

Extract to a different directory:
```
zip.unpack(
  "build/dev/resources.zip",
  "build/dev/tmp",
)

```

Extract while overwriting existing files on conflict:
```
zip.unpack(
  "build/dev/resources.zip",
  {on_conflict = zip.ON_CONFLICT.OVERWRITE}
)

```

Extract a single file:
```
zip.unpack(
  "build/dev/resources.zip",
  {"config.json"}
)

```

### zip.unpack.options
*Type:* STRUCT
Options for zip.unpack

**Members**

- `on_conflict` (zip.ON_CONFLICT) - conflict resolution strategy

### zlib.deflate
*Type:* FUNCTION
Deflate (compress) a buffer

**Parameters**

- `buf` (string) - buffer to deflate

**Returns**

- `buf` (string) - deflated buffer

### zlib.inflate
*Type:* FUNCTION
Inflate (decompress) a buffer

**Parameters**

- `buf` (string) - buffer to inflate

**Returns**

- `buf` (string) - inflated buffer
