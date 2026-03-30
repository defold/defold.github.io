# GameSystem Gui

**Namespace:** `dmGameSystem`
**Language:** C++
**Type:** Defold C++
**File:** `gui.h`
**Source:** `engine/gamesys/src/dmsdk/gamesys/gui.h`
**Include:** `dmsdk/gamesys/gui.h`

Built-in scripting functions.

## API

### CompGuiNodeTypeCtx
*Type:* STRUCT
Gui component node type create/destroy context

### DM_DECLARE_COMPGUI_TYPE
*Type:* MACRO
Registers a new gui node type to the Gui component

**Parameters**

- `symbol` (symbol) - The unique C++ symbol name
- `name` (const char*) - The name of the node type
- `type_create_fn` (GuiNodeTypeCreateFunction) - the create function
- `type_destroy_fn` (GuiNodeTypeDestroyFunction) - the destroy function. May be 0

### GuiNodeType
*Type:* STRUCT
Gui component node type

### GuiNodeTypeCreateFunction
*Type:* TYPEDEF

### GuiNodeTypeDestroyFunction
*Type:* TYPEDEF
