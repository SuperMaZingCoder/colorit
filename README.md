# ColorIt
A simple library to add color to your output.

Have you ever wanted to print Colors to the console? I certainly have. There comes a time when you realize it is a necessity. That's why I created ColorIt. ColorIt is a super simple way to print color to the console. 

## How it works

Interally, the library creates custom ANSI sequences with RGB values. This means there will never be a problem where a color changes. For example if I were to use pre-defined ANSI sequence, `\033[34m`, it would not print blue as it previously did. But, this problem is avoided because it doesn't use predefined values, each one is custom made.

## Installation
To install `colorit`. Run `pip install color-it` on Windows, or `pip3 install color-it` on macOS and Linux, from there it can be imported with `import colorit`

## How to use it

To use ColorIt:

```python
from colorit import *

# Use this to ensure that ColorIt will be usable by certain command line interfaces
init_colorit()

# Foreground
print(color("This text is red", Colors.RED))
print(color("This text is orange", Colors.ORANGE))
print(color("This text is yellow", Colors.YELLOW))
print(color("This text is green", Colors.GREEN))
print(color("This text is blue", Colors.BLUE))
print(color("This text is purple", Colors.PURPLE))
print(color("This text is white", Colors.WHITE))

# Background
print(background("This text has a background that is red", Colors.RED))
print(background("This text has a background that is orange", Colors.ORANGE))
print(background("This text has a background that is yellow", Colors.YELLOW))
print(background("This text has a background that is green", Colors.GREEN))
print(background("This text has a background that is blue", Colors.BLUE))
print(background("This text has a background that is purple", Colors.PURPLE))
print(background("This text has a background that is white", Colors.WHITE))

# Custom
print(color("This color has a custom grey text color", (150, 150, 150)))
print(background("This color has a custom grey background", (150, 150, 150)))

# Combination
print(
    background(
        color("This text is blue with a white background", Colors.BLUE), Colors.WHITE
    )
)

# If you are using Windows Command Line, this is so that it doesn't close immediately
input()
```

As output you get:

![demo](https://user-images.githubusercontent.com/55718659/88487218-1fbcf800-cf51-11ea-8a27-678407774a37.png)

If you would like to try this for yoyr self, you can download `demo.py` and try it out. 

And that's it. That's really all there is to it.

## Release Log
* Released the first version of ColorIt (v1.0.0)
* Added a license

## Support me on patreon!
Here is the link to my patreon page: https://www.patreon.com/supermazingcoder :D
