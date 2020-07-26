from .colorit import *

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
