# ColorIt
A simple library to add color to your output.

Have you ever wanted to print Colors to the console? I certainly have. There comes a time when you realize it is a necessity. That's why I created ColorIt. ColorIt is a super simple way to print color to the console. 

## How it works
Interally, the library creates custom ANSI sequences with RGB values. This means there are 16 million colors that can be used with `colorit`!

## Installation
To install `colorit`. Run `pip install color-it` on Windows, or `pip3 install color-it` on macOS and Linux, from there it can be imported with `import colorit`

## How to use it

To use ColorIt:

```python
from colorit import *

# Use this to ensure that ColorIt will be usable by certain command line interfaces
init_colorit()

# Foreground
print(color("This text is red", Colors.red))
print(color("This text is orange", Colors.orange))
print(color("This text is yellow", Colors.yellow))
print(color("This text is green", Colors.green))
print(color("This text is blue", Colors.blue))
print(color("This text is purple", Colors.purple))
print(color("This text is white", Colors.white))

# Background
print(background("This text has a background that is red", Colors.red))
print(background("This text has a background that is orange", Colors.orange))
print(background("This text has a background that is yellow", Colors.yellow))
print(background("This text has a background that is green", Colors.green))
print(background("This text has a background that is blue", Colors.blue))
print(background("This text has a background that is purple", Colors.purple))
print(background("This text has a background that is white", Colors.white))

# Custom
print(color("This color has a custom grey text color", (150, 150, 150)))
print(background("This color has a custom grey background", (150, 150, 150)))

# Combination
print(
    background(
        color("This text is blue with a white background", Colors.blue), Colors.white
    )
)

# If you are using Windows Command Line, this is so that it doesn't close immediately
input()
```

As output you get:

![demo](https://user-images.githubusercontent.com/55718659/88487218-1fbcf800-cf51-11ea-8a27-678407774a37.png)

If you would like to try this for yoyr self, you can download `demo.py` and try it out. 

And that's it. That's really all there is to it.

**Additional Note**: `init_colorit()` clears the console, so put this somewhere in your code before printing output.

## Release Log
* Released the first version of ColorIt (v1.0.0)
* Added a license

## Support me on patreon!
Here is the link to my patreon page: https://www.patreon.com/supermazingcoder :D
