import re
import platform
import os
import sys
import time
import multiprocessing

from art import *
from Game.Core.Settings import *

_COLORS = {
    "PURPLE": "\033[95m",
    "BLUE": "\033[94m",
    "CYAN": "\033[96m",
    "SUCCESS": "\033[92m",
    "WARNING": "\033[93m",
    "FAIL": "\033[91m",
    "END": "\033[0m",
    "BOLD_": "\033[1m",
    "UNDERLINE_": "\033[4m",
}

_ALIASES = {
    "P": _COLORS["PURPLE"],
    "B": _COLORS["BLUE"],
    "C": _COLORS["CYAN"],
    "GREEN": _COLORS["SUCCESS"],
    "G": _COLORS["SUCCESS"],
    "S": _COLORS["SUCCESS"],
    "ORANGE": _COLORS["WARNING"],
    "O": _COLORS["WARNING"],
    "W": _COLORS["WARNING"],
    "RED": _COLORS["FAIL"],
    "R": _COLORS["FAIL"],
    "F": _COLORS["FAIL"],
    "BOLD": _COLORS["BOLD_"],
    "B_": _COLORS["BOLD_"],
    "UNDERLINE": _COLORS["UNDERLINE_"],
    "U_": _COLORS["UNDERLINE_"]
}


def get_history(item: str):
    settings = Settings("./Game/Core/Settings/Data/", history="__history.json")
    return settings["history"][item]


def _replace_colors(colors, value, regx) -> str:
    _colors = []
    [_colors.append(_COLORS[c] if c in _COLORS else _ALIASES[c]) if c in _COLORS or c in _ALIASES else regx.remove(f"%{c}%") for c in colors]

    for i in range(len(regx)):
        value = value.replace(regx[i], _colors[i])
    return value


def colored_print(value: str) -> None:
    regx = re.findall(r"%\w+%", value)
    print(_replace_colors([c.split('%')[1].upper() for c in regx], value, regx))


def delay_print(value: str, delay: float = .04, end: str = "") -> None:
    count = 0

    for letter in value:
        if count == len(value)-1:
            print(letter, end=end)
        else:
            print(letter, end='')
        sys.stdout.flush()
        time.sleep(delay)
        count += 1


def input_delay_print(value: str, delay: float = .04, end: str = "") -> None:
    d_print = multiprocessing.Process(target=delay_print, args=(value, delay, end, ))
    d_print.start()
    input("Press enter to continue\n")
    d_print.terminate()
    d_print.join()
    clear_screen()
    print(value)


def clear_screen(delay: float = .5):
    time.sleep(delay)
    os.system('cls' if platform.system() == "Windows" else "clear")
