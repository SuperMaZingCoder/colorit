import colorama
import sys


class Colors:
    red = (245, 90, 66)
    orange = (245, 170, 66)
    yellow = (245, 252, 71)
    green = (92, 252, 71)
    blue = (71, 177, 252)
    purple = (189, 71, 252)
    white = (255, 255, 255)


class ColorsFG:
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    bright_black = "\033[90m"
    bright_red = "\033[91m"
    bright_green = "\033[92m"
    bright_yellow = "\033[93m"
    bright_blue = "\033[94m"
    bright_magenta = "\033[95m"
    bright_cyan = "\033[96m"
    bright_white = "\033[97m"


class ColorsBG:
    black = "\033[40m"
    red = "\033[41m"
    green = "\033[42m"
    yellow = "\033[43m"
    blue = "\033[44m"
    magenta = "\033[45m"
    cyan = "\033[46m"
    white = "\033[47m"
    bright_black = "\033[100m"
    bright_red = "\033[101m"
    bright_green = "\033[102m"
    bright_yellow = "\033[103m"
    bright_blue = "\033[104m"
    bright_magenta = "\033[105m"
    bright_cyan = "\033[106m"
    bright_white = "\033[107m"


# Uses colorama's init method to initialize
def init_colorit():
    colorama.init()


def color_ansii(text, color):
    return "{}{}\033[0m".format(color, text)


def color(text, rgb):
    return "\033[38;2;{};{};{}m{}\033[0m".format(
        str(rgb[0]), str(rgb[1]), str(rgb[2]), text
    )


def background(text, rgb):
    return "\033[48;2;{};{};{}m{}\033[0m".format(
        str(rgb[0]), str(rgb[1]), str(rgb[2]), text
    )
