---
author: Defold Foundation
brief: This example shows how to generate pseudo-random numbers in Defold using built-in math API.
category: basics
layout: example
opengraph_image: https://www.defold.com/examples/basics/random_numbers/thumbnail.png
path: basics/random_numbers
scripts: random_numbers.script
tags: basics
thumbnail: thumbnail.png
title: Random numbers
twitter_image: https://www.defold.com/examples/basics/random_numbers/thumbnail.png

---

In this example you'll learn how to generate pseudo-random numbers in Defold using built-in math API.

In the example there is only a game object containing:
- *Label* component where we show the text information
- *Script* component where we generate random numbers

![collection](collection.png)

Script sets the built-in random generator with a value of os.time() - which should be different every time you run it.
Then produces 3 random numbers using math.random().

For more details refer to Defold API: [https://defold.com/ref/stable/math-lua/#math.random:m-n](https://defold.com/ref/stable/math-lua/#math.random:m-n)