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

- `options` (table) (optional) - table of command line options for bob, without the leading dashes (<code>--</code>). You can use snake_case instead of kebab-case for option keys. Only long option names are supported (i.e. <code>output</code>, not <code>o</code>). Supported value types are strings, integers and booleans. If an option takes no arguments, use a boolean (i.e. <code>true</code>). If an option may be repeated, you can use an array of values.
- `...commands` (string) (optional) - bob commands, e.g. <code>"resolve"</code> or <code>"build"</code>

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
Check if editor.tx.add() (as well as editor.tx.clear() and editor.tx.remove()) transaction with this property won't throw an error

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `value` (boolean)

### editor.can_get
*Type:* FUNCTION
Check if you can get this property so editor.get() won't throw an error

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `value` (boolean)

### editor.can_reorder
*Type:* FUNCTION
Check if editor.tx.reorder() transaction with this property won't throw an error

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `value` (boolean)

### editor.can_reset
*Type:* FUNCTION
Check if editor.tx.reset() transaction with this property won't throw an error

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `value` (boolean)

### editor.can_set
*Type:* FUNCTION
Check if editor.tx.set() transaction with this property won't throw an error

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `value` (boolean)

### editor.command
*Type:* FUNCTION
Create an editor command

**Parameters**

- `opts` (table) - A table with the following keys:<dl><dt><code>label <small>string, message</small></code></dt><dd>required, user-visible command name, either a string or a localization message</dd><dt><code>locations <small>string[]</small></code></dt><dd>required, a non-empty list of locations where the command is displayed in the editor, values are either <code>"Edit"</code>, <code>"View"</code>, <code>"Project"</code>, <code>"Debug"</code> (the editor menubar), <code>"Assets"</code> (the assets pane), or <code>"Outline"</code> (the outline pane)</dd><dt><code>query <small>table</small></code></dt><dd>optional, a query that both controls the command availability and provides additional information to the command handler functions; a table with the following keys:<dl><dt><code>selection <small>table</small></code></dt><dd>current selection, a table with the following keys:<dl><dt><code>type <small>string</small></code></dt><dd>either <code>"resource"</code> (selected resource) or <code>"outline"</code> (selected outline node)</dd><dt><code>cardinality <small>string</small></code></dt><dd>either <code>"one"</code> (will use first selected item) or <code>"many"</code> (will use all selected items)</dd></dl></dd><dt><code>argument <small>table</small></code></dt><dd>the command argument</dd></dl></dd><dt><code>id <small>string</small></code></dt><dd>optional, keyword identifier that may be used for assigning a shortcut to a command; should be a dot-separated identifier string, e.g. <code>"my-extension.do-stuff"</code></dd><dt><code>active <small>function</small></code></dt><dd>optional function that additionally checks if a command is active in the current context; will receive opts table with values populated by the query; should be fast to execute since the editor might invoke it in response to UI interactions (on key typed, mouse clicked)</dd><dt><code>run <small>function</small></code></dt><dd>optional function that is invoked when the user decides to execute the command; will receive opts table with values populated by the query</dd></dl>

**Returns**

- `command` (command)

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

- `resources` (string[) - ] Array of resource paths (strings starting with <code>/</code>) or resource definitions, lua tables with the following keys:<dl><dt><code>1 <small>string</small></code></dt><dd>required, resource path (starting with <code>/</code>)</dd><dt><code>2 <small>string</small></code></dt><dd>optional, created resource content</dd></dl>

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
- `options` (table) (optional) - Optional options table. Supported entries:                                            <ul>                                              <li>                                                <span class="type">boolean</span> <code>reload_resources</code>: make the editor reload the resources from disk after the command is executed, default <code>true</code>                                              </li>                                              <li>                                                <span class="type">string</span> <code>out</code>: standard output mode, either:                                                <ul>                                                  <li>                                                    <code>"pipe"</code>: the output is piped to the editor console (this is the default behavior).                                                  </li>                                                  <li>                                                    <code>"capture"</code>: capture and return the output to the editor script with trailing newlines trimmed.                                                  </li>                                                  <li>                                                    <code>"discard"</code>: the output is discarded completely.                                                  </li>                                                </ul>                                              </li>                                              <li>                                                <span class="type">string</span> <code>err</code>: standard error output mode, either:                                                <ul>                                                  <li>                                                    <code>"pipe"</code>: the error output is piped to the editor console (this is the default behavior).                                                  </li>                                                  <li>                                                    <code>"stdout"</code>: the error output is redirected to the standard output of the process.                                                  </li>                                                  <li>                                                    <code>"discard"</code>: the error output is discarded completely.                                                  </li>                                                </ul>                                              </li>                                            </ul>

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

### editor.external_file_attributes
*Type:* FUNCTION
Query information about file system path

**Parameters**

- `path` (string) - External file path, resolved against project root if relative

**Returns**

- `attributes` (table) - A table with the following keys:<dl>                                                  <dt><code>path <small>string</small></code></dt>                                                  <dd>resolved file path</dd>                                                  <dt><code>exists <small>boolean</small></code></dt>                                                  <dd>whether there is a file system entry at the path</dd>                                                  <dt><code>is_file <small>boolean</small></code></dt>                                                  <dd>whether the path corresponds to a file</dd>                                                  <dt><code>is_directory <small>boolean</small></code></dt>                                                  <dd>whether the path corresponds to a directory</dd>                                                </dl>

### editor.get
*Type:* FUNCTION
Get a value of a node property inside the editor.
Some properties might be read-only, and some might be unavailable in different contexts, so you should use editor.can_get() before reading them and editor.can_set() before making the editor set them.

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `value` (any) - property value

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

- `opts` (table) - Required opts: <dl><dt><code>item <small>schema</small></code></dt><dd>array item schema</dd></dl>  Optional opts: <dl><dt><code>default <small>item[]</small></code></dt><dd>default value</dd><dt><code>scope <small>string</small></code></dt><dd>preference scope; either: <ul><li><code>editor.prefs.SCOPE.GLOBAL</code>: same preference value is used in every project on this computer</li><li><code>editor.prefs.SCOPE.PROJECT</code>: a separate preference value per project</li></ul></dd></dl>

**Returns**

- `value` (schema) - Prefs schema

### editor.prefs.schema.boolean
*Type:* FUNCTION
boolean schema

**Parameters**

- `opts` (table) (optional) - Optional opts: <dl><dt><code>default <small>boolean</small></code></dt><dd>default value</dd><dt><code>scope <small>string</small></code></dt><dd>preference scope; either: <ul><li><code>editor.prefs.SCOPE.GLOBAL</code>: same preference value is used in every project on this computer</li><li><code>editor.prefs.SCOPE.PROJECT</code>: a separate preference value per project</li></ul></dd></dl>

**Returns**

- `value` (schema) - Prefs schema

### editor.prefs.schema.enum
*Type:* FUNCTION
enum value schema

**Parameters**

- `opts` (table) - Required opts: <dl><dt><code>values <small>any[]</small></code></dt><dd>allowed values, must be scalar (nil, boolean, number or string)</dd></dl>  Optional opts: <dl><dt><code>default <small>any</small></code></dt><dd>default value</dd><dt><code>scope <small>string</small></code></dt><dd>preference scope; either: <ul><li><code>editor.prefs.SCOPE.GLOBAL</code>: same preference value is used in every project on this computer</li><li><code>editor.prefs.SCOPE.PROJECT</code>: a separate preference value per project</li></ul></dd></dl>

**Returns**

- `value` (schema) - Prefs schema

### editor.prefs.schema.integer
*Type:* FUNCTION
integer schema

**Parameters**

- `opts` (table) (optional) - Optional opts: <dl><dt><code>default <small>integer</small></code></dt><dd>default value</dd><dt><code>scope <small>string</small></code></dt><dd>preference scope; either: <ul><li><code>editor.prefs.SCOPE.GLOBAL</code>: same preference value is used in every project on this computer</li><li><code>editor.prefs.SCOPE.PROJECT</code>: a separate preference value per project</li></ul></dd></dl>

**Returns**

- `value` (schema) - Prefs schema

### editor.prefs.schema.keyword
*Type:* FUNCTION
keyword schema
A keyword is a short string that is interned within the editor runtime, useful e.g. for identifiers

**Parameters**

- `opts` (table) (optional) - Optional opts: <dl><dt><code>default <small>string</small></code></dt><dd>default value</dd><dt><code>scope <small>string</small></code></dt><dd>preference scope; either: <ul><li><code>editor.prefs.SCOPE.GLOBAL</code>: same preference value is used in every project on this computer</li><li><code>editor.prefs.SCOPE.PROJECT</code>: a separate preference value per project</li></ul></dd></dl>

**Returns**

- `value` (schema) - Prefs schema

### editor.prefs.schema.number
*Type:* FUNCTION
floating-point number schema

**Parameters**

- `opts` (table) (optional) - Optional opts: <dl><dt><code>default <small>number</small></code></dt><dd>default value</dd><dt><code>scope <small>string</small></code></dt><dd>preference scope; either: <ul><li><code>editor.prefs.SCOPE.GLOBAL</code>: same preference value is used in every project on this computer</li><li><code>editor.prefs.SCOPE.PROJECT</code>: a separate preference value per project</li></ul></dd></dl>

**Returns**

- `value` (schema) - Prefs schema

### editor.prefs.schema.object
*Type:* FUNCTION
heterogeneous object schema

**Parameters**

- `opts` (table) - Required opts: <dl><dt><code>properties <small>table&lt;string, schema&gt;</small></code></dt><dd>a table from property key (string) to value schema</dd></dl>  Optional opts: <dl><dt><code>default <small>table</small></code></dt><dd>default value</dd><dt><code>scope <small>string</small></code></dt><dd>preference scope; either: <ul><li><code>editor.prefs.SCOPE.GLOBAL</code>: same preference value is used in every project on this computer</li><li><code>editor.prefs.SCOPE.PROJECT</code>: a separate preference value per project</li></ul></dd></dl>

**Returns**

- `value` (schema) - Prefs schema

### editor.prefs.schema.object_of
*Type:* FUNCTION
homogeneous object schema

**Parameters**

- `opts` (table) - Required opts: <dl><dt><code>key <small>schema</small></code></dt><dd>table key schema</dd><dt><code>val <small>schema</small></code></dt><dd>table value schema</dd></dl>  Optional opts: <dl><dt><code>default <small>table</small></code></dt><dd>default value</dd><dt><code>scope <small>string</small></code></dt><dd>preference scope; either: <ul><li><code>editor.prefs.SCOPE.GLOBAL</code>: same preference value is used in every project on this computer</li><li><code>editor.prefs.SCOPE.PROJECT</code>: a separate preference value per project</li></ul></dd></dl>

**Returns**

- `value` (schema) - Prefs schema

### editor.prefs.schema.one_of
*Type:* FUNCTION
one of schema

**Parameters**

- `opts` (table) - Required opts: <dl><dt><code>schemas <small>schema[]</small></code></dt><dd>alternative schemas</dd></dl>  Optional opts: <dl><dt><code>default <small>any</small></code></dt><dd>default value</dd><dt><code>scope <small>string</small></code></dt><dd>preference scope; either: <ul><li><code>editor.prefs.SCOPE.GLOBAL</code>: same preference value is used in every project on this computer</li><li><code>editor.prefs.SCOPE.PROJECT</code>: a separate preference value per project</li></ul></dd></dl>

**Returns**

- `value` (schema) - Prefs schema

### editor.prefs.schema.password
*Type:* FUNCTION
password schema
A password is a string that is encrypted when stored in a preference file

**Parameters**

- `opts` (table) (optional) - Optional opts: <dl><dt><code>default <small>string</small></code></dt><dd>default value</dd><dt><code>scope <small>string</small></code></dt><dd>preference scope; either: <ul><li><code>editor.prefs.SCOPE.GLOBAL</code>: same preference value is used in every project on this computer</li><li><code>editor.prefs.SCOPE.PROJECT</code>: a separate preference value per project</li></ul></dd></dl>

**Returns**

- `value` (schema) - Prefs schema

### editor.prefs.schema.set
*Type:* FUNCTION
set schema
Set is represented as a lua table with true values

**Parameters**

- `opts` (table) - Required opts: <dl><dt><code>item <small>schema</small></code></dt><dd>set item schema</dd></dl>  Optional opts: <dl><dt><code>default <small>table&lt;item, true&gt;</small></code></dt><dd>default value</dd><dt><code>scope <small>string</small></code></dt><dd>preference scope; either: <ul><li><code>editor.prefs.SCOPE.GLOBAL</code>: same preference value is used in every project on this computer</li><li><code>editor.prefs.SCOPE.PROJECT</code>: a separate preference value per project</li></ul></dd></dl>

**Returns**

- `value` (schema) - Prefs schema

### editor.prefs.schema.string
*Type:* FUNCTION
string schema

**Parameters**

- `opts` (table) (optional) - Optional opts: <dl><dt><code>default <small>string</small></code></dt><dd>default value</dd><dt><code>scope <small>string</small></code></dt><dd>preference scope; either: <ul><li><code>editor.prefs.SCOPE.GLOBAL</code>: same preference value is used in every project on this computer</li><li><code>editor.prefs.SCOPE.PROJECT</code>: a separate preference value per project</li></ul></dd></dl>

**Returns**

- `value` (schema) - Prefs schema

### editor.prefs.schema.tuple
*Type:* FUNCTION
tuple schema
A tuple is a fixed-length array where each item has its own defined type

**Parameters**

- `opts` (table) - Required opts: <dl><dt><code>items <small>schema[]</small></code></dt><dd>schemas for the items</dd></dl>  Optional opts: <dl><dt><code>default <small>any[]</small></code></dt><dd>default value</dd><dt><code>scope <small>string</small></code></dt><dd>preference scope; either: <ul><li><code>editor.prefs.SCOPE.GLOBAL</code>: same preference value is used in every project on this computer</li><li><code>editor.prefs.SCOPE.PROJECT</code>: a separate preference value per project</li></ul></dd></dl>

**Returns**

- `value` (schema) - Prefs schema

### editor.prefs.SCOPE.GLOBAL
*Type:* VARIABLE
"global"

### editor.prefs.SCOPE.PROJECT
*Type:* VARIABLE
"project"

### editor.prefs.set
*Type:* FUNCTION
Set preference value
The schema for the preference value should be defined beforehand.

**Parameters**

- `key` (string) - dot-separated preference key path
- `value` (any) - new pref value to set

### editor.resource_attributes
*Type:* FUNCTION
Query information about a project resource

**Parameters**

- `resource_path` (string) - Resource path (starting with <code>/</code>)

**Returns**

- `value` (table) - A table with the following keys:<dl><dt><code>exists <small>boolean</small></code></dt><dd>whether a resource identified by the path exists in the project</dd><dt><code>is_file <small>boolean</small></code></dt><dd>whether the resource represents a file with some content</dd><dt><code>is_directory <small>boolean</small></code></dt><dd>whether the resource represents a directory</dd></dl>

### editor.save
*Type:* FUNCTION
Persist any unsaved changes to disk

### editor.transact
*Type:* FUNCTION
Change the editor state in a single, undoable transaction

**Parameters**

- `txs` (transaction_step[) - ] An array of transaction steps created using <code>editor.tx.*</code> functions

### editor.tx.add
*Type:* FUNCTION
Create a transaction step that will add a child item to a node's list property when transacted with editor.transact().

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)
- `value` (any) - Added item for the property, a table from property key to either a valid <code>editor.tx.set()</code>-able value, or an array of valid <code>editor.tx.add()</code>-able values

### editor.tx.clear
*Type:* FUNCTION
Create a transaction step that will remove all items from node's list property when transacted with editor.transact().

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `tx` (transaction_step) - A transaction step

### editor.tx.remove
*Type:* FUNCTION
Create a transaction step that will remove a child node from the node's list property when transacted with editor.transact().

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)
- `child_node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor

**Returns**

- `tx` (transaction_step) - A transaction step

### editor.tx.reorder
*Type:* FUNCTION
Create a transaction step that reorders child nodes in a node list defined by the property if supported (see editor.can_reorder())

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)
- `child_nodes` (table) - array of child nodes (the same as returned by <code>editor.get(node, property)</code>) in new order

**Returns**

- `tx` (transaction_step) - A transaction step

### editor.tx.reset
*Type:* FUNCTION
Create a transaction step that will reset an overridden property to its default value when transacted with editor.transact().

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)

**Returns**

- `tx` (transaction_step) - A transaction step

### editor.tx.set
*Type:* FUNCTION
Create transaction step that will set the node's property to a supplied value when transacted with editor.transact().

**Parameters**

- `node` (string | userdata) - Either resource path (e.g. <code>"/main/game.script"</code>), or internal node id passed to the script by the editor
- `property` (string) - Either <code>"path"</code>, <code>"text"</code>, or a property from the Outline view (hover the label to see its editor script name)
- `value` (any) - A new value for the property

**Returns**

- `tx` (transaction_step) - A transaction step

### editor.ui.ALIGNMENT.BOTTOM
*Type:* VARIABLE
"bottom"

### editor.ui.ALIGNMENT.BOTTOM_LEFT
*Type:* VARIABLE
"bottom-left"

### editor.ui.ALIGNMENT.BOTTOM_RIGHT
*Type:* VARIABLE
"bottom-right"

### editor.ui.ALIGNMENT.CENTER
*Type:* VARIABLE
"center"

### editor.ui.ALIGNMENT.LEFT
*Type:* VARIABLE
"left"

### editor.ui.ALIGNMENT.RIGHT
*Type:* VARIABLE
"right"

### editor.ui.ALIGNMENT.TOP
*Type:* VARIABLE
"top"

### editor.ui.ALIGNMENT.TOP_LEFT
*Type:* VARIABLE
"top-left"

### editor.ui.ALIGNMENT.TOP_RIGHT
*Type:* VARIABLE
"top-right"

### editor.ui.button
*Type:* FUNCTION
Button with a label and/or an icon

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>on_pressed <small>function</small></code></dt><dd>button press callback, will be invoked without arguments when the user presses the button</dd><dt><code>text <small>string, message</small></code></dt><dd>the text, either a string or a localization message</dd><dt><code>text_alignment <small>string</small></code></dt><dd>text alignment within paragraph bounds; either: <ul><li><code>editor.ui.TEXT_ALIGNMENT.LEFT</code></li><li><code>editor.ui.TEXT_ALIGNMENT.CENTER</code></li><li><code>editor.ui.TEXT_ALIGNMENT.RIGHT</code></li><li><code>editor.ui.TEXT_ALIGNMENT.JUSTIFY</code></li></ul></dd><dt><code>icon <small>string</small></code></dt><dd>predefined icon name; either: <ul><li><code>editor.ui.ICON.OPEN_RESOURCE</code></li><li><code>editor.ui.ICON.PLUS</code></li><li><code>editor.ui.ICON.MINUS</code></li><li><code>editor.ui.ICON.CLEAR</code></li></ul></dd><dt><code>enabled <small>boolean</small></code></dt><dd>determines if the input component can be interacted with</dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.check_box
*Type:* FUNCTION
Check box with a label

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>value <small>boolean</small></code></dt><dd>determines if the checkbox should appear checked</dd><dt><code>on_value_changed <small>function</small></code></dt><dd>change callback, will receive the new value</dd><dt><code>text <small>string, message</small></code></dt><dd>the text, either a string or a localization message</dd><dt><code>text_alignment <small>string</small></code></dt><dd>text alignment within paragraph bounds; either: <ul><li><code>editor.ui.TEXT_ALIGNMENT.LEFT</code></li><li><code>editor.ui.TEXT_ALIGNMENT.CENTER</code></li><li><code>editor.ui.TEXT_ALIGNMENT.RIGHT</code></li><li><code>editor.ui.TEXT_ALIGNMENT.JUSTIFY</code></li></ul></dd><dt><code>issue <small>table</small></code></dt><dd>issue related to the input; table with the following keys (all required):<dl><dt><code>severity <small>string</small></code></dt><dd>either <code>editor.ui.ISSUE_SEVERITY.WARNING</code> or <code>editor.ui.ISSUE_SEVERITY.ERROR</code></dd><dt><code>message <small>string, message</small></code></dt><dd>issue message that will be shown in a tooltip; either a string or a localization message</dd></dl></dd><dt><code>tooltip <small>string, message</small></code></dt><dd>tooltip message shown on hover; either a string or a localization message</dd><dt><code>enabled <small>boolean</small></code></dt><dd>determines if the input component can be interacted with</dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.COLOR.ERROR
*Type:* VARIABLE
"error"

### editor.ui.COLOR.HINT
*Type:* VARIABLE
"hint"

### editor.ui.COLOR.OVERRIDE
*Type:* VARIABLE
"override"

### editor.ui.COLOR.TEXT
*Type:* VARIABLE
"text"

### editor.ui.COLOR.WARNING
*Type:* VARIABLE
"warning"

### editor.ui.component
*Type:* FUNCTION
Convert a function to a UI component.
The wrapped function may call any hooks functions (editor.ui.use_*), but on any function invocation, the hooks calls must be the same, and in the same order. This means that hooks should not be used inside loops and conditions or after a conditional return statement.
The following props are supported automatically:grow booleandetermines if the component should grow to fill available space in a horizontal or vertical layout containerrow_span integerhow many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a grid container.column_span integerhow many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a grid container.

**Parameters**

- `fn` (function) - function, will receive a single table of props when called

**Returns**

- `value` (function) - decorated component function that may be invoked with a props table create component

### editor.ui.dialog
*Type:* FUNCTION
Dialog component, a top-level window component that can't be used as a child of other components

**Parameters**

- `props` (table) - Required props: <dl><dt><code>title <small>string, message</small></code></dt><dd>OS dialog window title, either a string or a localization message</dd></dl>  Optional props: <dl><dt><code>header <small>component</small></code></dt><dd>top part of the dialog, defaults to <code>editor.ui.heading({text = props.title})</code></dd><dt><code>content <small>component</small></code></dt><dd>content of the dialog</dd><dt><code>buttons <small>component[]</small></code></dt><dd>array of <code>editor.ui.dialog_button(...)</code> components, footer of the dialog. Defaults to a single Close button</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.dialog_button
*Type:* FUNCTION
Dialog button shown in the footer of a dialog

**Parameters**

- `props` (table) - Required props: <dl><dt><code>text <small>string, message</small></code></dt><dd>button text, either a string or a localization message</dd></dl>  Optional props: <dl><dt><code>result <small>any</small></code></dt><dd>value returned by <code>editor.ui.show_dialog(...)</code> if this button is pressed</dd><dt><code>default <small>boolean</small></code></dt><dd>if set, pressing <code>Enter</code> in the dialog will trigger this button</dd><dt><code>cancel <small>boolean</small></code></dt><dd>if set, pressing <code>Escape</code> in the dialog will trigger this button</dd><dt><code>enabled <small>boolean</small></code></dt><dd>determines if the button can be interacted with</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.external_file_field
*Type:* FUNCTION
Input component for selecting files from the file system

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>value <small>string</small></code></dt><dd>file or directory path; resolved against project root if relative</dd><dt><code>on_value_changed <small>function</small></code></dt><dd>value change callback, will receive the absolute path of a selected file/folder or nil if the field was cleared; even though the selector dialog allows selecting only files, it's possible to receive directories and non-existent file system entries using text field input</dd><dt><code>title <small>string, message</small></code></dt><dd>OS window title, either a string or a localization message</dd><dt><code>filters <small>table[]</small></code></dt><dd>File filters, an array of filter tables, where each filter has following keys:<dl><dt><code>description <small>string, message</small></code></dt><dd>text explaining the filter, either a literal string like <code>"Text files (<em>.txt)"</code> or a localization message</dd><dt><code>extensions <small>string[]</small></code></dt><dd>array of file extension patterns, e.g. <code>"</em>.txt"</code>, <code>"<em>.</em>"</code> or <code>"game.project"</code></dd></dl></dd><dt><code>issue <small>table</small></code></dt><dd>issue related to the input; table with the following keys (all required):<dl><dt><code>severity <small>string</small></code></dt><dd>either <code>editor.ui.ISSUE_SEVERITY.WARNING</code> or <code>editor.ui.ISSUE_SEVERITY.ERROR</code></dd><dt><code>message <small>string, message</small></code></dt><dd>issue message that will be shown in a tooltip; either a string or a localization message</dd></dl></dd><dt><code>tooltip <small>string, message</small></code></dt><dd>tooltip message shown on hover; either a string or a localization message</dd><dt><code>enabled <small>boolean</small></code></dt><dd>determines if the input component can be interacted with</dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.grid
*Type:* FUNCTION
Layout container that places its children in a 2D grid

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>children <small>component[][]</small></code></dt><dd>array of arrays of child components</dd><dt><code>rows <small>table[]</small></code></dt><dd>array of row option tables, separate configuration for each row:<dl><dt><code>grow <small>boolean</small></code></dt><dd>determines if the row should grow to fill available space</dd></dl></dd><dt><code>columns <small>table[]</small></code></dt><dd>array of column option tables, separate configuration for each column:<dl><dt><code>grow <small>boolean</small></code></dt><dd>determines if the column should grow to fill available space</dd></dl></dd><dt><code>padding <small>string, number</small></code></dt><dd>empty space from the edges of the container to its children; either: <ul><li><code>editor.ui.PADDING.NONE</code></li><li><code>editor.ui.PADDING.SMALL</code></li><li><code>editor.ui.PADDING.MEDIUM</code></li><li><code>editor.ui.PADDING.LARGE</code></li><li>non-negative number, pixels</li></ul></dd><dt><code>spacing <small>string, number</small></code></dt><dd>empty space between child components, defaults to <code>editor.ui.SPACING.MEDIUM</code>; either: <ul><li><code>editor.ui.SPACING.NONE</code></li><li><code>editor.ui.SPACING.SMALL</code></li><li><code>editor.ui.SPACING.MEDIUM</code></li><li><code>editor.ui.SPACING.LARGE</code></li><li>non-negative number, pixels</li></ul></dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.heading
*Type:* FUNCTION
A text heading

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>text <small>string, message</small></code></dt><dd>the text, either a string or a localization message</dd><dt><code>text_alignment <small>string</small></code></dt><dd>text alignment within paragraph bounds; either: <ul><li><code>editor.ui.TEXT_ALIGNMENT.LEFT</code></li><li><code>editor.ui.TEXT_ALIGNMENT.CENTER</code></li><li><code>editor.ui.TEXT_ALIGNMENT.RIGHT</code></li><li><code>editor.ui.TEXT_ALIGNMENT.JUSTIFY</code></li></ul></dd><dt><code>color <small>string</small></code></dt><dd>semantic color, defaults to <code>editor.ui.COLOR.TEXT</code>; either: <ul><li><code>editor.ui.COLOR.TEXT</code></li><li><code>editor.ui.COLOR.HINT</code></li><li><code>editor.ui.COLOR.OVERRIDE</code></li><li><code>editor.ui.COLOR.WARNING</code></li><li><code>editor.ui.COLOR.ERROR</code></li></ul></dd><dt><code>word_wrap <small>boolean</small></code></dt><dd>determines if the lines of text are word-wrapped when they don't fit in the assigned bounds, defaults to true</dd><dt><code>style <small>string</small></code></dt><dd>heading style, defaults to <code>editor.ui.HEADING_STYLE.H3</code>; either: <ul><li><code>editor.ui.HEADING_STYLE.H1</code></li><li><code>editor.ui.HEADING_STYLE.H2</code></li><li><code>editor.ui.HEADING_STYLE.H3</code></li><li><code>editor.ui.HEADING_STYLE.H4</code></li><li><code>editor.ui.HEADING_STYLE.H5</code></li><li><code>editor.ui.HEADING_STYLE.H6</code></li><li><code>editor.ui.HEADING_STYLE.DIALOG</code></li><li><code>editor.ui.HEADING_STYLE.FORM</code></li></ul></dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.HEADING_STYLE.DIALOG
*Type:* VARIABLE
"dialog"

### editor.ui.HEADING_STYLE.FORM
*Type:* VARIABLE
"form"

### editor.ui.HEADING_STYLE.H1
*Type:* VARIABLE
"h1"

### editor.ui.HEADING_STYLE.H2
*Type:* VARIABLE
"h2"

### editor.ui.HEADING_STYLE.H3
*Type:* VARIABLE
"h3"

### editor.ui.HEADING_STYLE.H4
*Type:* VARIABLE
"h4"

### editor.ui.HEADING_STYLE.H5
*Type:* VARIABLE
"h5"

### editor.ui.HEADING_STYLE.H6
*Type:* VARIABLE
"h6"

### editor.ui.horizontal
*Type:* FUNCTION
Layout container that places its children in a horizontal row one after another

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>children <small>component[]</small></code></dt><dd>array of child components</dd><dt><code>padding <small>string, number</small></code></dt><dd>empty space from the edges of the container to its children; either: <ul><li><code>editor.ui.PADDING.NONE</code></li><li><code>editor.ui.PADDING.SMALL</code></li><li><code>editor.ui.PADDING.MEDIUM</code></li><li><code>editor.ui.PADDING.LARGE</code></li><li>non-negative number, pixels</li></ul></dd><dt><code>spacing <small>string, number</small></code></dt><dd>empty space between child components, defaults to <code>editor.ui.SPACING.MEDIUM</code>; either: <ul><li><code>editor.ui.SPACING.NONE</code></li><li><code>editor.ui.SPACING.SMALL</code></li><li><code>editor.ui.SPACING.MEDIUM</code></li><li><code>editor.ui.SPACING.LARGE</code></li><li>non-negative number, pixels</li></ul></dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.icon
*Type:* FUNCTION
An icon from a predefined set

**Parameters**

- `props` (table) - Required props: <dl><dt><code>icon <small>string</small></code></dt><dd>predefined icon name; either: <ul><li><code>editor.ui.ICON.OPEN_RESOURCE</code></li><li><code>editor.ui.ICON.PLUS</code></li><li><code>editor.ui.ICON.MINUS</code></li><li><code>editor.ui.ICON.CLEAR</code></li></ul></dd></dl>  Optional props: <dl><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.ICON.CLEAR
*Type:* VARIABLE
"clear"

### editor.ui.ICON.MINUS
*Type:* VARIABLE
"minus"

### editor.ui.ICON.OPEN_RESOURCE
*Type:* VARIABLE
"open-resource"

### editor.ui.ICON.PLUS
*Type:* VARIABLE
"plus"

### editor.ui.integer_field
*Type:* FUNCTION
Integer input component based on a text field, reports changes on commit (Enter or focus loss)

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>value <small>any</small></code></dt><dd>value</dd><dt><code>on_value_changed <small>function</small></code></dt><dd>value change callback, will receive the new value</dd><dt><code>issue <small>table</small></code></dt><dd>issue related to the input; table with the following keys (all required):<dl><dt><code>severity <small>string</small></code></dt><dd>either <code>editor.ui.ISSUE_SEVERITY.WARNING</code> or <code>editor.ui.ISSUE_SEVERITY.ERROR</code></dd><dt><code>message <small>string, message</small></code></dt><dd>issue message that will be shown in a tooltip; either a string or a localization message</dd></dl></dd><dt><code>tooltip <small>string, message</small></code></dt><dd>tooltip message shown on hover; either a string or a localization message</dd><dt><code>enabled <small>boolean</small></code></dt><dd>determines if the input component can be interacted with</dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.ISSUE_SEVERITY.ERROR
*Type:* VARIABLE
"error"

### editor.ui.ISSUE_SEVERITY.WARNING
*Type:* VARIABLE
"warning"

### editor.ui.label
*Type:* FUNCTION
Label intended for use with input components

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>text <small>string, message</small></code></dt><dd>the text, either a string or a localization message</dd><dt><code>text_alignment <small>string</small></code></dt><dd>text alignment within paragraph bounds; either: <ul><li><code>editor.ui.TEXT_ALIGNMENT.LEFT</code></li><li><code>editor.ui.TEXT_ALIGNMENT.CENTER</code></li><li><code>editor.ui.TEXT_ALIGNMENT.RIGHT</code></li><li><code>editor.ui.TEXT_ALIGNMENT.JUSTIFY</code></li></ul></dd><dt><code>color <small>string</small></code></dt><dd>semantic color, defaults to <code>editor.ui.COLOR.TEXT</code>; either: <ul><li><code>editor.ui.COLOR.TEXT</code></li><li><code>editor.ui.COLOR.HINT</code></li><li><code>editor.ui.COLOR.OVERRIDE</code></li><li><code>editor.ui.COLOR.WARNING</code></li><li><code>editor.ui.COLOR.ERROR</code></li></ul></dd><dt><code>tooltip <small>string, message</small></code></dt><dd>tooltip message shown on hover; either a string or a localization message</dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.number_field
*Type:* FUNCTION
Number input component based on a text field, reports changes on commit (Enter or focus loss)

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>value <small>any</small></code></dt><dd>value</dd><dt><code>on_value_changed <small>function</small></code></dt><dd>value change callback, will receive the new value</dd><dt><code>issue <small>table</small></code></dt><dd>issue related to the input; table with the following keys (all required):<dl><dt><code>severity <small>string</small></code></dt><dd>either <code>editor.ui.ISSUE_SEVERITY.WARNING</code> or <code>editor.ui.ISSUE_SEVERITY.ERROR</code></dd><dt><code>message <small>string, message</small></code></dt><dd>issue message that will be shown in a tooltip; either a string or a localization message</dd></dl></dd><dt><code>tooltip <small>string, message</small></code></dt><dd>tooltip message shown on hover; either a string or a localization message</dd><dt><code>enabled <small>boolean</small></code></dt><dd>determines if the input component can be interacted with</dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.open_resource
*Type:* FUNCTION
Open a resource, either in the editor or in a third-party app

**Parameters**

- `resource_path` (string) - Resource path (starting with <code>/</code>)

### editor.ui.ORIENTATION.HORIZONTAL
*Type:* VARIABLE
"horizontal"

### editor.ui.ORIENTATION.VERTICAL
*Type:* VARIABLE
"vertical"

### editor.ui.PADDING.LARGE
*Type:* VARIABLE
"large"

### editor.ui.PADDING.MEDIUM
*Type:* VARIABLE
"medium"

### editor.ui.PADDING.NONE
*Type:* VARIABLE
"none"

### editor.ui.PADDING.SMALL
*Type:* VARIABLE
"small"

### editor.ui.paragraph
*Type:* FUNCTION
A paragraph of text

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>text <small>string, message</small></code></dt><dd>the text, either a string or a localization message</dd><dt><code>text_alignment <small>string</small></code></dt><dd>text alignment within paragraph bounds; either: <ul><li><code>editor.ui.TEXT_ALIGNMENT.LEFT</code></li><li><code>editor.ui.TEXT_ALIGNMENT.CENTER</code></li><li><code>editor.ui.TEXT_ALIGNMENT.RIGHT</code></li><li><code>editor.ui.TEXT_ALIGNMENT.JUSTIFY</code></li></ul></dd><dt><code>color <small>string</small></code></dt><dd>semantic color, defaults to <code>editor.ui.COLOR.TEXT</code>; either: <ul><li><code>editor.ui.COLOR.TEXT</code></li><li><code>editor.ui.COLOR.HINT</code></li><li><code>editor.ui.COLOR.OVERRIDE</code></li><li><code>editor.ui.COLOR.WARNING</code></li><li><code>editor.ui.COLOR.ERROR</code></li></ul></dd><dt><code>word_wrap <small>boolean</small></code></dt><dd>determines if the lines of text are word-wrapped when they don't fit in the assigned bounds, defaults to true</dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.resource_field
*Type:* FUNCTION
Input component for selecting project resources

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>value <small>string</small></code></dt><dd>resource path (must start with <code>/</code>)</dd><dt><code>on_value_changed <small>function</small></code></dt><dd>value change callback, will receive either resource path of a selected resource or nil when the field is cleared; even though the resource selector dialog allows filtering on resource extensions, it's possible to receive resources with other extensions and non-existent resources using text field input</dd><dt><code>title <small>string, message</small></code></dt><dd>dialog title, either a string or a localization message, defaults to <code>localization.message("dialog.select-resource.title")</code></dd><dt><code>extensions <small>string[]</small></code></dt><dd>if specified, restricts selectable resources in the dialog to specified file extensions; e.g. <code>{"collection", "go"}</code></dd><dt><code>issue <small>table</small></code></dt><dd>issue related to the input; table with the following keys (all required):<dl><dt><code>severity <small>string</small></code></dt><dd>either <code>editor.ui.ISSUE_SEVERITY.WARNING</code> or <code>editor.ui.ISSUE_SEVERITY.ERROR</code></dd><dt><code>message <small>string, message</small></code></dt><dd>issue message that will be shown in a tooltip; either a string or a localization message</dd></dl></dd><dt><code>tooltip <small>string, message</small></code></dt><dd>tooltip message shown on hover; either a string or a localization message</dd><dt><code>enabled <small>boolean</small></code></dt><dd>determines if the input component can be interacted with</dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.scroll
*Type:* FUNCTION
Layout container that optionally shows scroll bars if child contents overflow the assigned bounds

**Parameters**

- `props` (table) - Required props: <dl><dt><code>content <small>component</small></code></dt><dd>content component</dd></dl>  Optional props: <dl><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.select_box
*Type:* FUNCTION
Dropdown select box with an array of options

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>value <small>any</small></code></dt><dd>selected value</dd><dt><code>on_value_changed <small>function</small></code></dt><dd>change callback, will receive the selected value</dd><dt><code>options <small>any[]</small></code></dt><dd>array of selectable options</dd><dt><code>to_string <small>function</small></code></dt><dd>function that converts an item to a string (or a localization message); defaults to <code>tostring</code></dd><dt><code>issue <small>table</small></code></dt><dd>issue related to the input; table with the following keys (all required):<dl><dt><code>severity <small>string</small></code></dt><dd>either <code>editor.ui.ISSUE_SEVERITY.WARNING</code> or <code>editor.ui.ISSUE_SEVERITY.ERROR</code></dd><dt><code>message <small>string, message</small></code></dt><dd>issue message that will be shown in a tooltip; either a string or a localization message</dd></dl></dd><dt><code>tooltip <small>string, message</small></code></dt><dd>tooltip message shown on hover; either a string or a localization message</dd><dt><code>enabled <small>boolean</small></code></dt><dd>determines if the input component can be interacted with</dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.separator
*Type:* FUNCTION
Thin line for visual content separation, by default horizontal and aligned to center

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>orientation <small>string</small></code></dt><dd>separator line orientation, <code>editor.ui.ORIENTATION.VERTICAL</code> or <code>editor.ui.ORIENTATION.HORIZONTAL</code>; either: <ul><li><code>editor.ui.ORIENTATION.VERTICAL</code></li><li><code>editor.ui.ORIENTATION.HORIZONTAL</code></li></ul></dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.show_dialog
*Type:* FUNCTION
Show a modal dialog and await a result

**Parameters**

- `dialog` (component) - a component that resolves to <code>editor.ui.dialog(...)</code>

**Returns**

- `value` (any) - dialog result, the value used as a <code>result</code> prop in a <code>editor.ui.dialog_button({...})</code> selected by the user, or <code>nil</code> if the dialog was closed and there was no <code>cancel = true</code> dialog button with <code>result</code> prop set

### editor.ui.show_external_directory_dialog
*Type:* FUNCTION
Show a modal OS directory selection dialog and await a result

**Parameters**

- `opts` (table) (optional) - <dl><dt><code>path <small>string</small></code></dt><dd>initial file or directory path used by the dialog; resolved against project root if relative</dd><dt><code>title <small>string, message</small></code></dt><dd>OS window title, either a string or a localization message</dd></dl>

**Returns**

- `value` (string | nil) - either absolute directory path or nil if user canceled directory selection

### editor.ui.show_external_file_dialog
*Type:* FUNCTION
Show a modal OS file selection dialog and await a result

**Parameters**

- `opts` (table) (optional) - <dl><dt><code>path <small>string</small></code></dt><dd>initial file or directory path used by the dialog; resolved against project root if relative</dd><dt><code>title <small>string, message</small></code></dt><dd>OS window title, either a string or a localization message</dd><dt><code>filters <small>table[]</small></code></dt><dd>File filters, an array of filter tables, where each filter has following keys:<dl><dt><code>description <small>string, message</small></code></dt><dd>text explaining the filter, either a literal string like <code>"Text files (*.txt)"</code> or a localization message</dd><dt><code>extensions <small>string[]</small></code></dt><dd>array of file extension patterns, e.g. <code>"*.txt"</code>, <code>"*.*"</code> or <code>"game.project"</code></dd></dl></dd></dl>

**Returns**

- `value` (string | nil) - either absolute file path or nil if user canceled file selection

### editor.ui.show_resource_dialog
*Type:* FUNCTION
Show a modal resource selection dialog and await a result

**Parameters**

- `opts` (table) (optional) - <dl><dt><code>extensions <small>string[]</small></code></dt><dd>if specified, restricts selectable resources in the dialog to specified file extensions; e.g. <code>{"collection", "go"}</code></dd><dt><code>selection <small>string</small></code></dt><dd>either <code>"single"</code> or <code>"multiple"</code>, defaults to <code>"single"</code></dd><dt><code>title <small>string, message</small></code></dt><dd>dialog title, either a string or a localization message, defaults to <code>localization.message("dialog.select-resource.title")</code></dd></dl>

**Returns**

- `value` (string | string[) - |nil] if user made no selection, returns <code>nil</code>. Otherwise, if selection mode is <code>"single"</code>, returns selected resource path; otherwise returns a non-empty array of selected resource paths.

### editor.ui.SPACING.LARGE
*Type:* VARIABLE
"large"

### editor.ui.SPACING.MEDIUM
*Type:* VARIABLE
"medium"

### editor.ui.SPACING.NONE
*Type:* VARIABLE
"none"

### editor.ui.SPACING.SMALL
*Type:* VARIABLE
"small"

### editor.ui.string_field
*Type:* FUNCTION
String input component based on a text field, reports changes on commit (Enter or focus loss)

**Parameters**

- `props` (table) - Optional props: <dl><dt><code>value <small>any</small></code></dt><dd>value</dd><dt><code>on_value_changed <small>function</small></code></dt><dd>value change callback, will receive the new value</dd><dt><code>issue <small>table</small></code></dt><dd>issue related to the input; table with the following keys (all required):<dl><dt><code>severity <small>string</small></code></dt><dd>either <code>editor.ui.ISSUE_SEVERITY.WARNING</code> or <code>editor.ui.ISSUE_SEVERITY.ERROR</code></dd><dt><code>message <small>string, message</small></code></dt><dd>issue message that will be shown in a tooltip; either a string or a localization message</dd></dl></dd><dt><code>tooltip <small>string, message</small></code></dt><dd>tooltip message shown on hover; either a string or a localization message</dd><dt><code>enabled <small>boolean</small></code></dt><dd>determines if the input component can be interacted with</dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.ui.TEXT_ALIGNMENT.CENTER
*Type:* VARIABLE
"center"

### editor.ui.TEXT_ALIGNMENT.JUSTIFY
*Type:* VARIABLE
"justify"

### editor.ui.TEXT_ALIGNMENT.LEFT
*Type:* VARIABLE
"left"

### editor.ui.TEXT_ALIGNMENT.RIGHT
*Type:* VARIABLE
"right"

### editor.ui.use_memo
*Type:* FUNCTION
A hook that caches the result of a computation between re-renders.
See editor.ui.component for hooks caveats and rules. If any of the arguments to use_memo change during a component refresh (checked with ==), the value will be recomputed.

**Parameters**

- `compute` (function) - function that will be used to compute the cached value
- `...` (...any) (optional) - args to the computation function

**Returns**

- `values` (...any) - all returned values of the compute function

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
- `...` (...any) (optional) - used when <code>init</code> is a function, the args are passed to the initializer function

**Returns**

- `state` (any) - current local state, starts with initial state, then may be changed using the returned <code>set_state</code> function
- `set_state` (function) - function that changes the local state and causes the component to refresh. The function may be used in 2 ways:                         <ul>                           <li>to set the state to some other data structure: pass the data structure as a value</li>                           <li>to replace the state using updater function: pass a function to <code>set_state</code> — it will be invoked with the current state, as well as with the rest of the arguments passed to <code>set_state</code> after the updater function. The state will be set to the value returned from the updater function</lia>                         </ul>

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

- `props` (table) - Optional props: <dl><dt><code>children <small>component[]</small></code></dt><dd>array of child components</dd><dt><code>padding <small>string, number</small></code></dt><dd>empty space from the edges of the container to its children; either: <ul><li><code>editor.ui.PADDING.NONE</code></li><li><code>editor.ui.PADDING.SMALL</code></li><li><code>editor.ui.PADDING.MEDIUM</code></li><li><code>editor.ui.PADDING.LARGE</code></li><li>non-negative number, pixels</li></ul></dd><dt><code>spacing <small>string, number</small></code></dt><dd>empty space between child components, defaults to <code>editor.ui.SPACING.MEDIUM</code>; either: <ul><li><code>editor.ui.SPACING.NONE</code></li><li><code>editor.ui.SPACING.SMALL</code></li><li><code>editor.ui.SPACING.MEDIUM</code></li><li><code>editor.ui.SPACING.LARGE</code></li><li>non-negative number, pixels</li></ul></dd><dt><code>alignment <small>string</small></code></dt><dd>alignment of the component content within its assigned bounds, defaults to <code>editor.ui.ALIGNMENT.TOP_LEFT</code>; either: <ul><li><code>editor.ui.ALIGNMENT.TOP_LEFT</code></li><li><code>editor.ui.ALIGNMENT.TOP</code></li><li><code>editor.ui.ALIGNMENT.TOP_RIGHT</code></li><li><code>editor.ui.ALIGNMENT.LEFT</code></li><li><code>editor.ui.ALIGNMENT.CENTER</code></li><li><code>editor.ui.ALIGNMENT.RIGHT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_LEFT</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM</code></li><li><code>editor.ui.ALIGNMENT.BOTTOM_RIGHT</code></li></ul></dd><dt><code>grow <small>boolean</small></code></dt><dd>determines if the component should grow to fill available space in a <code>horizontal</code> or <code>vertical</code> layout container</dd><dt><code>row_span <small>integer</small></code></dt><dd>how many rows the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd><dt><code>column_span <small>integer</small></code></dt><dd>how many columns the component spans inside a grid container, must be positive. This prop is only useful for components inside a <code>grid</code> container.</dd></dl>

**Returns**

- `value` (component) - UI component

### editor.version
*Type:* VARIABLE
A string, version name of Defold

### http.request
*Type:* FUNCTION
Perform an HTTP request

**Parameters**

- `url` (string) - request URL
- `opts` (table) (optional) - Additional request options, a table with the following keys:<dl><dt><code>method <small>string</small></code></dt><dd>request method, defaults to <code>"GET"</code></dd><dt><code>headers <small>table</small></code></dt><dd>request headers, a table with string keys and values</dd><dt><code>body <small>string</small></code></dt><dd>request body</dd><dt><code>as <small>string</small></code></dt><dd>response body converter, either <code>"string"</code> or <code>"json"</code></dd></dl>

**Returns**

- `response` (table) - HTTP response, a table with the following keys:<dl><dt><code>status <small>integer</small></code></dt><dd>response code</dd><dt><code>headers <small>table</small></code></dt><dd>response headers, a table where each key is a lower-cased string, and each value is either a string or an array of strings if the header was repeated</dd><dt><code>body <small>string, any, nil</small></code></dt><dd>response body, present only when <code>as</code> option was provided, either a string or a parsed json value</dd></dl>

### http.server.external_file_response
*Type:* FUNCTION
Create HTTP response that will stream the content of a file defined by the path

**Parameters**

- `path` (string) - External file path, resolved against project root if relative
- `status` (integer) (optional) - HTTP status code, an integer, default 200
- `headers` (table&lt;string,string&gt;) (optional) - HTTP response headers, a table from lower-case header names to header values

**Returns**

- `response` (response) - HTTP response value, userdata

### http.server.json_response
*Type:* FUNCTION
Create HTTP response with a JSON value

**Parameters**

- `value` (any) - Any Lua value that may be represented as JSON
- `status` (integer) (optional) - HTTP status code, an integer, default 200
- `headers` (table&lt;string,string&gt;) (optional) - HTTP response headers, a table from lower-case header names to header values

**Returns**

- `response` (response) - HTTP response value, userdata

### http.server.local_url
*Type:* VARIABLE
Editor's HTTP server local url

### http.server.port
*Type:* VARIABLE
Editor's HTTP server port

### http.server.resource_response
*Type:* FUNCTION
Create HTTP response that will stream the content of a resource defined by the resource path

**Parameters**

- `resource_path` (string) - Resource path (starting with <code>/</code>)
- `status` (integer) (optional) - HTTP status code, an integer, default 200
- `headers` (table&lt;string,string&gt;) (optional) - HTTP response headers, a table from lower-case header names to header values

**Returns**

- `response` (response) - HTTP response value, userdata

### http.server.response
*Type:* FUNCTION
Create HTTP response

**Parameters**

- `status` (integer) (optional) - HTTP status code, an integer, default 200
- `headers` (table&lt;string,string&gt;) (optional) - HTTP response headers, a table from lower-case header names to header values
- `body` (string) (optional) - HTTP response body

**Returns**

- `response` (response) - HTTP response value, userdata

### http.server.route
*Type:* FUNCTION
Create route definition for the editor's HTTP server

**Parameters**

- `path` (string) - HTTP URI path, starts with <code>/</code>; may include path patterns (<code>{name}</code> for a single segment and <code>{*name}</code> for the rest of the request path) that will be extracted from the path and provided to the handler as a part of the request
- `method` (string) (optional) - HTTP request method, default <code>"GET"</code>
- `as` (string) (optional) - Request body converter, either <code>"string"</code> or <code>"json"</code>; the body will be discarded if not specified
- `handler` (function) - Request handler function, will receive request argument, a table with the following keys:<dl><dt><code>path <small>string</small></code></dt><dd>full matched path, a string starting with <code>/</code></dd><dt><code>method <small>string</small></code></dt><dd>HTTP request method, e.g. <code>"POST"</code></dd><dt><code>headers <small>table&lt;string,(string|string[])&gt;</small></code></dt><dd>HTTP request headers, a table from lower-case header names to header values</dd><dt><code>query <small>string</small></code></dt><dd>optional query string</dd><dt><code>body <small>string, any</small></code></dt><dd>optional request body, depends on the <code>as</code> argument</dd></dl> Handler function should return either a single response value, or 0 or more arguments to the <code>http.server.response()</code> function

**Returns**

- `route` (route) - HTTP server route

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
*Type:* VARIABLE
Editor's HTTP server url

### json.decode
*Type:* FUNCTION
Decode JSON string to Lua value

**Parameters**

- `json` (string) - json data
- `options` (table) (optional) - A table with the following keys:<dl><dt><code>all <small>boolean</small></code></dt><dd>if <code>true</code>, decodes all json values in a string and returns an array</dd></dl>

### json.encode
*Type:* FUNCTION
Encode Lua value to JSON string

**Parameters**

- `value` (any) - any Lua value that may be represented as JSON

### localization.and_list
*Type:* FUNCTION
Create a message pattern that renders a list with the "and" conjunction (for example: a, b, and c) once it is stringified

**Parameters**

- `items` (any[) - ] array of values; each value may be <code>nil</code>, <code>boolean</code>, <code>number</code>, <code>string</code>, or another <code>message</code> instance

**Returns**

- `message` (message) - a userdata value that, when stringified with <code>tostring()</code>, will produce a localized text according to the currently selected language in the editor

### localization.concat
*Type:* FUNCTION
Create a message pattern that concatenates values (similar to table.concat) and performs the actual concatenation when stringified

**Parameters**

- `items` (any[) - ] array of values; each value may be <code>nil</code>, <code>boolean</code>, <code>number</code>, <code>string</code>, or another <code>message</code> instance
- `separator` (nil | boolean | number | string | message) (optional) - optional separator inserted between values; defaults to an empty string

**Returns**

- `message` (message) - a userdata value that, when stringified with <code>tostring()</code>, will produce a localized text according to the currently selected language in the editor

### localization.message
*Type:* FUNCTION
Create a message pattern for a localization key defined in an .editor_localization file; the actual localization happens when the returned value is stringified

**Parameters**

- `key` (string) - localization key defined in an <code>.editor_localization</code> file
- `vars` (table) (optional) - optional table with variables to be substituted in the localized string that uses <a href="https://unicode-org.github.io/icu/userguide/format_parse/messages/">ICU Message Format</a> syntax; keys must be strings; values must be either <code>nil</code>, <code>boolean</code>, <code>number</code>, <code>string</code>, or another <code>message</code> instance

**Returns**

- `message` (message) - a userdata value that, when stringified with <code>tostring()</code>, will produce a localized text according to the currently selected language in the editor

### localization.or_list
*Type:* FUNCTION
Create a message pattern that renders a list with the "or" conjunction (for example: a, b, or c) once it is stringified

**Parameters**

- `items` (any[) - ] array of values; each value may be <code>nil</code>, <code>boolean</code>, <code>number</code>, <code>string</code>, or another <code>message</code> instance

**Returns**

- `message` (message) - a userdata value that, when stringified with <code>tostring()</code>, will produce a localized text according to the currently selected language in the editor

### pprint
*Type:* FUNCTION
Pretty-print a Lua value

**Parameters**

- `value` (any) - any Lua value to pretty-print

### tilemap.tiles.clear
*Type:* FUNCTION
Remove all tiles

**Parameters**

- `tiles` (tiles) - unbounded 2d grid of tiles

**Returns**

- `tiles` (tiles) - unbounded 2d grid of tiles

### tilemap.tiles.get_info
*Type:* FUNCTION
Get full information from a tile at a particular coordinate

**Parameters**

- `tiles` (tiles) - unbounded 2d grid of tiles
- `x` (integer) - x coordinate of a tile
- `y` (integer) - y coordinate of a tile

**Returns**

- `info` (table) - full tile information table with the following keys:<dl><dt><code>index <small>integer</small></code></dt><dd>1-indexed tile index of a tilemap's tilesource</dd><dt><code>h_flip <small>boolean</small></code></dt><dd>horizontal flip</dd><dt><code>v_flip <small>boolean</small></code></dt><dd>vertical flip</dd><dt><code>rotate_90 <small>boolean</small></code></dt><dd>whether the tile is rotated 90 degrees clockwise</dd></dl>

### tilemap.tiles.get_tile
*Type:* FUNCTION
Get a tile index at a particular coordinate

**Parameters**

- `tiles` (tiles) - unbounded 2d grid of tiles
- `x` (integer) - x coordinate of a tile
- `y` (integer) - y coordinate of a tile

**Returns**

- `tile_index` (integer) - 1-indexed tile index of a tilemap's tilesource

### tilemap.tiles.iterator
*Type:* FUNCTION
Create an iterator over all tiles in a tiles data structure
When iterating using for loop, each iteration returns x, y and tile index of a tile in a tile map

**Parameters**

- `tiles` (tiles) - unbounded 2d grid of tiles

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

- `tiles` (tiles) - unbounded 2d grid of tiles

### tilemap.tiles.remove
*Type:* FUNCTION
Remove a tile at a particular coordinate

**Parameters**

- `tiles` (tiles) - unbounded 2d grid of tiles
- `x` (integer) - x coordinate of a tile
- `y` (integer) - y coordinate of a tile

**Returns**

- `tiles` (tiles) - unbounded 2d grid of tiles

### tilemap.tiles.set
*Type:* FUNCTION
Set a tile at a particular coordinate

**Parameters**

- `tiles` (tiles) - unbounded 2d grid of tiles
- `x` (integer) - x coordinate of a tile
- `y` (integer) - y coordinate of a tile
- `tile_or_info` (integer | table) - Either 1-indexed tile index of a tilemap's tilesource or full tile information table with the following keys:<dl><dt><code>index <small>integer</small></code></dt><dd>1-indexed tile index of a tilemap's tilesource</dd><dt><code>h_flip <small>boolean</small></code></dt><dd>horizontal flip</dd><dt><code>v_flip <small>boolean</small></code></dt><dd>vertical flip</dd><dt><code>rotate_90 <small>boolean</small></code></dt><dd>whether the tile is rotated 90 degrees clockwise</dd></dl>

**Returns**

- `tiles` (tiles) - unbounded 2d grid of tiles

### zip.METHOD.DEFLATED
*Type:* VARIABLE
"deflated" compression method

### zip.METHOD.STORED
*Type:* VARIABLE
"stored" compression method, i.e. no compression

### zip.ON_CONFLICT.ERROR
*Type:* VARIABLE
"error", any conflict aborts extraction

### zip.ON_CONFLICT.OVERWRITE
*Type:* VARIABLE
"skip", existing file is overwritten

### zip.ON_CONFLICT.SKIP
*Type:* VARIABLE
"skip", existing file is preserved

### zip.pack
*Type:* FUNCTION
Create a ZIP archive

**Parameters**

- `output_path` (string) - output zip file path, resolved against project root if relative
- `opts` (table) (optional) - compression options, a table with the following keys:<dl><dt><code>method <small>string</small></code></dt><dd>compression method, either <code>zip.METHOD.DEFLATED</code> (default) or <code>zip.METHOD.STORED</code></dd><dt><code>level <small>integer</small></code></dt><dd>compression level, an integer between 0 and 9, only useful when the compression method is <code>zip.METHOD.DEFLATED</code>; defaults to 6</dd></dl>
- `entries` (string | table) - entries to compress, either a string (relative path to file or folder to include) or a table with the following keys:<dl><dt><code>1 <small>string</small></code></dt><dd>required; source file or folder path to include, resolved against project root if relative</dd><dt><code>2 <small>string</small></code></dt><dd>optional; target file or folder path in the zip archive. May be omitted if source is a relative path that does not go above the project directory.</dd><dt><code>method <small>string</small></code></dt><dd>compression method, either <code>zip.METHOD.DEFLATED</code> (default) or <code>zip.METHOD.STORED</code></dd><dt><code>level <small>integer</small></code></dt><dd>compression level, an integer between 0 and 9, only useful when the compression method is <code>zip.METHOD.DEFLATED</code>; defaults to 6</dd></dl>

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

### zip.unpack
*Type:* FUNCTION
Extract a ZIP archive

**Parameters**

- `archive_path` (string) - zip file path, resolved against project root if relative
- `target_path` (string) (optional) - target path for extraction, defaults to parent of <code>archive_path</code> if omitted
- `opts` (table) (optional) - extraction options, a table with the following keys:<dl><dt><code>on_conflict <small>string</small></code></dt><dd>conflict resolution strategy, defaults to <code>zip.ON_CONFLICT.ERROR</code></dd></dl>
- `paths` (table) (optional) - entries to extract, relative string paths

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
