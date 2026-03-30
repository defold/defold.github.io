# b2d

**Namespace:** `b2d`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_box2d.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/box2d/script_box2d.cpp`

Functions for interacting with Box2D.

## API

### b2Body
*Type:* TYPEDEF
Box2D body

**Parameters**

- `value` (userdata)

### b2d.get_body
*Type:* FUNCTION
Get the Box2D body from a collision object

**Parameters**

- `url` (string | hash | url) - the url to the game object collision component

**Returns**

- `body` (b2Body) - the body if successful. Otherwise <code>nil</code>.

### b2d.get_world
*Type:* FUNCTION
Get the Box2D world from the current collection

**Returns**

- `world` (b2World) - the world if successful. Otherwise <code>nil</code>.

### b2World
*Type:* TYPEDEF
Box2D world

**Parameters**

- `value` (userdata)
