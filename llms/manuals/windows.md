# Windows development {#manuals:windows}

Developing Defold applications for the Windows platform is a straight forward process with very few considerations to make.

## Project settings

Windows specific application configuration is done from the [Windows section](project-settings.md) of the *game.project* settings file.

## Application icon

The application icon used for a Windows game must be in the .ico format. You can easily create a .ico file from a .png file using an online tool such as [ICOConvert](https://www.icoconverter.com/) or [AConvert](https://www.aconvert.com/icon/png-to-ico/). Upload an image and use at least the following icon sizes: 16x16, 24x24, 32x32, 48x48, 256x256.

Source: [Microsoft - Windows app icon construction](https://learn.microsoft.com/en-us/windows/apps/design/style/iconography/app-icon-construction#icon-sizes-win32)

### Creating .ico file locally using ImageMagick software suite.
[ImageMagick](https://www.imagemagick.org/) is a free, open-source software suite, used for editing and manipulating digital images.

1. Install ImageMagick
  * Linux: Install using `apt`
```
sudo apt install imagemagick
```
  * Windows: Download from [https://imagemagick.org/script/download.php#windows](https://imagemagick.org/script/download.php#windows):
  * macOS: Install using `brew`:
```
brew install imagemagick
```

2. Prepare your PNG icon.
3. Convert PNG to ICO using [convert](https://www.imagemagick.org/script/convert.php) tool:
```bash
magick icon_256x256px.png -compress None -define icon:auto-resize=256,128,96,64,48,32,24,16 favicon.ico
```

## FAQ
#### Q: Why are GUI box nodes without a texture transparent in the editor but show up as expected when I build and run?

A: This error can happen on [computers using AMD Radeon GPUs](https://github.com/defold/editor2-issues/issues/2723). Make sure to update your graphics drivers.

#### Q: Why am I getting `com.sun.jna.Native.open.class java.lang.Error: Access is denied` when opening an atlas or a scene view?

A: Try running Defold as administrator. Right-click on the Defold executable and select "Run as Administrator".

#### Q: Why is my game not rendering properly on Windows using an Intel UHD integrated GPU (but my HTML5 build works)?

A: Make sure to update your driver to a version higher than or equal to 27.20.100.8280. Check with the [Intel Driver Support Assistant](https://www.intel.com/content/www/us/en/search.html?ws=text#t=Downloads&layout=table&cf:Downloads=%5B%7B%22actualLabel%22%3A%22Graphics%22%2C%22displayLabel%22%3A%22Graphics%22%7D%2C%7B%22actualLabel%22%3A%22Intel%C2%AE%20UHD%20Graphics%20Family%22%2C%22displayLabel%22%3A%22Intel%C2%AE%20UHD%20Graphics%20Family%22%7D%2C%7B%22actualLabel%22%3A%22Intel%C2%AE%20UHD%20Graphics%20630%22%2C%22displayLabel%22%3A%22Intel%C2%AE%20UHD%20Graphics%20630%22%7D%5D). Additional information can be found in [this forum post](https://forum.defold.com/t/sprite-game-object-is-not-rendering/69198/35?u=britzl).

#### Q: The Defold editor is crashing and the log shows `AWTError: Assistive Technology not found`

If the editor crashes with a log mentioning `Caused by: java.awt.AWTError: Assistive Technology not found: com.sun.java.accessibility.AccessBridge` then follow these steps:

* Navigate to `C:\\Users\\`
* Open the file called `.accessibility.properties` using a standard text editor (Notepad is fine)
* Find the following lines in the config:
```
assistive_technologies=com.sun.java.accessibility.AccessBridge
screen_magnifier_present=true
```

* Add a hash mark (`#``) in front of theses lines
* Save your changes to the file and restart Defold