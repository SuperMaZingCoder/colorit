import os
import sys


class Colors:
    red = (245, 90, 66)
    orange = (245, 170, 66)
    yellow = (245, 252, 71)
    green = (92, 252, 71)
    blue = (71, 177, 252)
    purple = (189, 71, 252)
    white = (255, 255, 255)


def init_colorit():
    if sys.platform.startswith("win32"):
        os.system("cls")
    elif sys.platform.startswith("darwin") or sys.platform.startswith("linux"):
        os.system("clear")


def color(text, rgb):
    return "\033[38;2;{};{};{}m{}\033[0m".format(
        str(rgb[0]), str(rgb[1]), str(rgb[2]), text
    )


def background(text, rgb):
    return "\033[48;2;{};{};{}m{}\033[0m".format(
        str(rgb[0]), str(rgb[1]), str(rgb[2]), text
    )

if __name__ == '__main__':
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
            color("This text is blue with a white background", Colors.BLUE), Colors.WHITE
        )
    )

    # If you are using Windows Command Line, this is so that it doesn't close immediately
    input()
