from ColorIt import *

# Use this to ensure that ColorIt will be usable by certain command line interfaces
initColorIt()

# Foreground
print (color ('This text is red', colors.RED))
print (color ('This text is orange', colors.ORANGE))
print (color ('This text is yellow', colors.YELLOW))
print (color ('This text is green', colors.GREEN))
print (color ('This text is blue', colors.BLUE))
print (color ('This text is purple', colors.PURPLE))
print (color ('This text is white', colors.WHITE))

# Background
print (background ('This text has a background that is red', colors.RED))
print (background ('This text has a background that is orange', colors.ORANGE))
print (background ('This text has a background that is yellow', colors.YELLOW))
print (background ('This text has a background that is green', colors.GREEN))
print (background ('This text has a background that is blue', colors.BLUE))
print (background ('This text has a background that is purple', colors.PURPLE))
print (background ('This text has a background that is white', colors.WHITE))

# Custom
print (color ("This color has a custom grey text color", (150, 150, 150)))
print (background ("This color has a custom grey background", (150, 150, 150)))

# Combination
print (background (color ("This text is blue with a white background", colors.BLUE), colors.WHITE))

# If you are using Windows Command Line, this is so that it doesn't close immediately
input()