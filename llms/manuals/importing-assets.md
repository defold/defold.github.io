# Importing and editing assets {#manuals:importing-assets}

A game project usually consists of a large number of external assets that are produced in various specialized programs for producing graphics, 3D models, sound files, animations and so forth. Defold is built for a workflow where you work in your external tools and then import the assets into Defold as they are finalized.

## Importing assets

Defold needs all the assets used in your project to be located somewhere in the project hierarchy. You therefore need to import all assets before you can use them. To import assets, simply drag the files from the file system on your computer and drop them in an appropriate place in the Defold editor *Assets pane*.

Use PNG or JPEG images for atlases and tile sources. PNG support includes RGB, RGBA and indexed color (palette) images. [KTX2 source textures](https://defold.com/llms/manuals/importing-graphics.md) can also be imported for use as model textures.

## Using assets

When the assets are imported into Defold they can be used by the various component types supported by Defold:

* Images can be used to create many kinds of visual components frequently used in 2D games. Read more about [how to import and use 2D graphics here](https://defold.com/llms/manuals/importing-graphics.md).
* Sounds can be used by the [Sound component](https://defold.com/llms/manuals/sound.md) to play sounds.
* Fonts are used by the [Label component](https://defold.com/llms/manuals/label.md) and by [text nodes](https://defold.com/llms/manuals/gui-text.md) in a GUI.
* glTF models (*.gltf* and *.glb*) can be used by the [Model component](https://defold.com/llms/manuals/model.md) to show 3D models with animations. Expand these files in the *Assets* pane to browse their meshes, generated materials and embedded images. Embedded images can be used directly; include any externally referenced images and buffers as separate project files. [Draco- and Meshopt-compressed geometry](https://defold.com/llms/manuals/importing-models.md) is also supported and is decoded during import/build. When selecting a scene or mesh in a Model component, the editor can offer to fill its material and texture bindings. Choose `Auto Fill` to apply them, replacing existing bindings, or `Keep Current` to preserve your own. Read more about [how to import and use 3D models here](https://defold.com/llms/manuals/importing-models.md).

## Editing external assets

Defold does not provide editing tools for images, sound files, models or animations. Such assets need to be created outside of Defold in specialized tools and imported into Defold. Defold automatically detects changes to any asset among your project files and updates the editor view accordingly.

## Editing Defold assets

The editor saves all Defold assets in text based files that are merge friendly. They are also easy to create and modify with simple scripts. See [this forum thread](https://forum.defold.com/t/deftree-a-python-module-for-editing-defold-files/15210) for more information. Note though that we do not publish our file format details since they do change once in a while. You can also use [Editor Scripts](https://defold.com/llms/manuals/editor-scripts.md) to hook into certain life-cycle events in the Editor to run scripts to generate or modify assets.

Extra care should be taken when working with Defold asset files through a text editor or external tool. If you introduce errors those can prevent the file from opening in the Defold editor.

Some external tools such as [Tiled](https://defold.com/assets/tiled/) and [Tilesetter](https://www.tilesetter.org/beta) can be used to generate Defold Assets automatically.