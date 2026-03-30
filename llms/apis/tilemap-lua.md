# Tilemap

**Namespace:** `tilemap`
**Language:** Lua
**Type:** Defold Lua
**File:** `script_tilemap.cpp`
**Source:** `engine/gamesys/src/gamesys/scripts/script_tilemap.cpp`

Functions and messages used to manipulate tile map components.

## API

### material
*Type:* PROPERTY
The material used when rendering the tile map. The type of the property is hash.

**Examples**

How to set material using a script property (see resource.material)
```
go.property("my_material", resource.material("/material.material"))
function init(self)
  go.set("#tilemap", "material", self.my_material)
end

```

### tile_source
*Type:* PROPERTY
The tile source used when rendering the tile map. The type of the property is hash.

**Examples**

How to set tile source using a script property (see resource.tile_source)
```
go.property("my_tile_source", resource.tile_source("/tilesource.tilesource"))
function init(self)
  go.set("#tilemap", "tile_source", self.my_tile_source)
end

```

### tilemap.get_bounds
*Type:* FUNCTION
Get the bounds for a tile map. This function returns multiple values:
The lower left corner index x and y coordinates (1-indexed),
the tile map width and the tile map height.
The resulting values take all tile map layers into account, meaning that
the bounds are calculated as if all layers were collapsed into one.

**Parameters**

- `url` (string | hash | url) - the tile map

**Returns**

- `x` (number) - x coordinate of the bottom left corner
- `y` (number) - y coordinate of the bottom left corner
- `w` (number) - number of columns (width) in the tile map
- `h` (number) - number of rows (height) in the tile map

**Examples**

```
-- get the level bounds.
local x, y, w, h = tilemap.get_bounds("/level#tilemap")

```

### tilemap.get_tile
*Type:* FUNCTION
Get the tile set at the specified position in the tilemap.
The position is identified by the tile index starting at origin
with index 1, 1. (see tilemap.set_tile())
Which tile map and layer to query is identified by the URL and the
layer name parameters.

**Parameters**

- `url` (string | hash | url) - the tile map
- `layer` (string | hash) - name of the layer for the tile
- `x` (number) - x-coordinate of the tile
- `y` (number) - y-coordinate of the tile

**Returns**

- `tile` (number) - index of the tile

**Examples**

```
-- get the tile under the player.
local tileno = tilemap.get_tile("/level#tilemap", "foreground", self.player_x, self.player_y)

```

### tilemap.get_tile_info
*Type:* FUNCTION
Get the tile information at the specified position in the tilemap.
The position is identified by the tile index starting at origin
with index 1, 1. (see tilemap.set_tile())
Which tile map and layer to query is identified by the URL and the
layer name parameters.

**Parameters**

- `url` (string | hash | url) - the tile map
- `layer` (string | hash) - name of the layer for the tile
- `x` (number) - x-coordinate of the tile
- `y` (number) - y-coordinate of the tile

**Returns**

- `tile_info` (table) - index of the tile

**Examples**

```
-- get the tile under the player.
local tile_info = tilemap.get_tile_info("/level#tilemap", "foreground", self.player_x, self.player_y)
pprint(tile_info)
-- {
--    index = 0,
--    h_flip = false,
--    v_flip = true,
--    rotate_90 = false
-- }

```

### tilemap.get_tiles
*Type:* FUNCTION
Retrieves all the tiles for the specified layer in the tilemap.
It returns a table of rows where the keys are the
tile positions (see tilemap.get_bounds()).
You can iterate it using tiles[row_index][column_index].

**Parameters**

- `url` (string | hash | url) - the tilemap
- `layer` (string | hash) - the name of the layer for the tiles

**Returns**

- `tiles` (table) - a table of rows representing the layer

**Examples**

```
local left, bottom, columns_count, rows_count = tilemap.get_bounds("#tilemap")
local tiles = tilemap.get_tiles("#tilemap", "layer")
local tile, count = 0, 0
for row_index = bottom, bottom + rows_count - 1 do
    for column_index = left, left + columns_count - 1 do
        tile = tiles[row_index][column_index]
        count = count + 1
    end
end

```

### tilemap.H_FLIP
*Type:* CONSTANT
flip tile horizontally

### tilemap.ROTATE_180
*Type:* CONSTANT
rotate tile 180 degrees clockwise

### tilemap.ROTATE_270
*Type:* CONSTANT
rotate tile 270 degrees clockwise

### tilemap.ROTATE_90
*Type:* CONSTANT
rotate tile 90 degrees clockwise

### tilemap.set_tile
*Type:* FUNCTION
Replace a tile in a tile map with a new tile.
The coordinates of the tiles are indexed so that the "first" tile just
above and to the right of origin has coordinates 1,1.
Tiles to the left of and below origin are indexed 0, -1, -2 and so forth.

+-------+-------+------+------+
|  0,3  |  1,3  | 2,3  | 3,3  |
+-------+-------+------+------+
|  0,2  |  1,2  | 2,2  | 3,2  |
+-------+-------+------+------+
|  0,1  |  1,1  | 2,1  | 3,1  |
+-------O-------+------+------+
|  0,0  |  1,0  | 2,0  | 3,0  |
+-------+-------+------+------+

The coordinates must be within the bounds of the tile map as it were created.
That is, it is not possible to extend the size of a tile map by setting tiles outside the edges.
To clear a tile, set the tile to number 0. Which tile map and layer to manipulate is identified by the URL and the layer name parameters.
Transform bitmask is arithmetic sum of one or both FLIP constants (tilemap.H_FLIP, tilemap.V_FLIP) and/or one of ROTATION constants
(tilemap.ROTATE_90, tilemap.ROTATE_180, tilemap.ROTATE_270).
Flip always applies before rotation (clockwise).

**Parameters**

- `url` (string | hash | url) - the tile map
- `layer` (string | hash) - name of the layer for the tile
- `x` (number) - x-coordinate of the tile
- `y` (number) - y-coordinate of the tile
- `tile` (number) - index of new tile to set. 0 resets the cell
- `transform_bitmask` (number) (optional) - optional flip and/or rotation should be applied to the tile

**Examples**

```
-- Clear the tile under the player.
tilemap.set_tile("/level#tilemap", "foreground", self.player_x, self.player_y, 0)

-- Set tile with different combination of flip and rotation
tilemap.set_tile("#tilemap", "layer1", x, y, 0, tilemap.H_FLIP + tilemap.V_FLIP + tilemap.ROTATE_90)
tilemap.set_tile("#tilemap", "layer1", x, y, 0, tilemap.H_FLIP + tilemap.ROTATE_270)
tilemap.set_tile("#tilemap", "layer1", x, y, 0, tilemap.V_FLIP + tilemap.H_FLIP)
tilemap.set_tile("#tilemap", "layer1", x, y, 0, tilemap.ROTATE_180)

```

### tilemap.set_visible
*Type:* FUNCTION
Sets the visibility of the tilemap layer

**Parameters**

- `url` (string | hash | url) - the tile map
- `layer` (string | hash) - name of the layer for the tile
- `visible` (boolean) - should the layer be visible

**Examples**

```
-- Disable rendering of the layer
tilemap.set_visible("/level#tilemap", "foreground", false)

```

### tilemap.V_FLIP
*Type:* CONSTANT
flip tile vertically
