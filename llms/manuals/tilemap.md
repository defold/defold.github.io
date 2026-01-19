# Tile map {#manuals:tilemap}

A *Tile Map* is a component that allows you to assemble, or paint, tiles from a *Tile Source* onto a large grid area. Tile maps are commonly used to build game level environments. You can also use the *Collision Shapes* from the tile source in your maps for collision detection and physics simulation ([example](https://defold.com/examples/tilemap/collisions/)).

Before you can create a tile map you need to create a Tile Source. Refer to the [Tile Source manual](tilesource.md) to learn how to create a Tile Source.

## Creating a tile map

To create a new tile map:

- `Right click` a location in the *Assets* browser, then select `New... ▸ Tile Map`).
- Name the file.
- The new tile map automatically opens in the tile map editor.

- Set the *Tile Source* property to a tile source file that you have prepared.

To paint tiles on your tile map:

1. Select or create a *Layer* to paint on in the *Outline* view.
2. Select a tile to use as a brush (press `Space` to show the tile palette) or select a few tiles by clicking and dragging in the palette to create a rectangle brush with multiple tiles.

3. Paint with the selected brush. To erase a tile, either pick an empty tile and use it as brush, or select the eraser (`Edit ▸ Select Eraser`).

You can pick tiles directly from a layer and use the selection as a brush. Hold `Shift` and click a tile to pick it up as the current brush. While holding `Shift` you can also click and drag to select a block of tiles to use as a larger brush. Also, it is possible to cut tiles in a similar way by holding `Shift+Ctrl` or erase them by holding `Shift+Alt`.

For clockwise brush rotation, use `Z`. Use `X` for horizontal flipping and `Y` for vertical flipping of the brush.

## Adding a tile map to your game

To add a tile map to your game:

1. Create a game object to hold the tile map component. The game object can be in a file or created directly in a collection.
2. Right-click the root of the game object and select `Add Component File`.
3. Select the tile map file.

## Runtime manipulation

You can manipulate tilemaps in runtime through a number of different functions and properties (refer to the [API docs for usage](https://defold.com/ref/tilemap/)).

### Changing tiles from script

You can read and write the content of a tile map dynamically while your game is running. To do so, use the [`tilemap.get_tile()`](https://defold.com/ref/tilemap/#tilemap.get_tile) and [`tilemap.set_tile()`](https://defold.com/ref/tilemap/#tilemap.set_tile) functions:
```lua
local tile = tilemap.get_tile("/level#map", "ground", x, y)

if tile == 2 then
    -- Replace grass-tile (2) with dangerous hole tile (number 4).
    tilemap.set_tile("/level#map", "ground", x, y, 4)
end
```

## Tilemap properties

Apart from the properties *Id*, *Position*, *Rotation* and *Scale* the following component specific properties exist:

*Tile Source*
: The tilesource resource to use for the tilemap.

*Material*
: The material to use for rendering the tilemap.

*Blend Mode*
: The blend mode to use when rendering the tilemap.

### Blend modes
The *Blend Mode* property defines how the component graphics should be blended with the graphics behind it. These are the available blend modes and how they are calculated:

Alpha
: Normal blending: `src.a * src.rgb + (1 - src.a) * dst.rgb`

Add
: Brighten the background with the color values of the corresponding pixels of the component: `src.rgb + dst.rgb`

Multiply
: Darken the background with values of the corresponding pixels of the component: `src.rgb * dst.rgb`

Screen
: Opposite of Multiply. Brighten background and values of the corresponding pixels of the component: `src.rgb - dst.rgb * dst.rgb`

### Changing properties

A tilemap has a number of different properties that can be manipulated using `go.get()` and `go.set()`:

`tile_source`
: The tile map tile source (`hash`). You can change this using a tile source resource property and `go.set()`. Refer to the [API reference for an example](https://defold.com/ref/tilemap/#tile_source).

`material`
: The tile map material (`hash`). You can change this using a material resource property and `go.set()`. Refer to the [API reference for an example](https://defold.com/ref/tilemap/#material).

### Material constants

The default tilemap material has the following constants that can be changed using [go.set()](https://defold.com/ref/stable/go/#go.set) or [go.animate()](https://defold.com/ref/stable/go/#go.animate) (refer to the [Material manual for more details](material.md)). Examples:
```lua
go.set("#tilemap", "tint", vmath.vector4(1,0,0,1))
go.animate("#tilemap", "tint", go.PLAYBACK_LOOP_PINGPONG, vmath.vector4(1,0,0,1), go.EASING_LINEAR, 2)
```

`tint`
: The color tint of the tile map (`vector4`). The vector4 is used to represent the tint with x, y, z, and w corresponding to the red, green, blue and alpha tint.

## Project configuration

The *game.project* file has a few [project settings](project-settings#tilemap.md) related to tilemaps.

## External tools

There are external map/level editors that can export directly to Defold tilemaps:

### Tiled

[Tiled](https://www.mapeditor.org/) is a well-known and widely used map editor for orthogonal, isometric and hexagonal maps. Tiled has support for a wide array of features and can [export directly to Defold](https://doc.mapeditor.org/en/stable/manual/export-defold/). Learn more about how to export tilemap data and additional meta-data in [this blog post by Defold user "goeshard"](https://goeshard.org/2025/01/01/using-tiled-object-layers-with-defold-tilemaps/)

### Tilesetter

[Tilesetter](https://www.tilesetter.org/docs/exporting#defold) can be used to automatically create full tilesets from simple base tiles and it has a map editor which can export directly to Defold.