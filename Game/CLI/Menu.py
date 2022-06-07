import re
import time
# from art import *

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


def _replace_colors(colors, value, regx) -> str:
    _colors = []
    [_colors.append(_COLORS[c] if c in _COLORS else _ALIASES[c]) if c in _COLORS or c in _ALIASES else regx.remove(f"%{c}%") for c in colors]

    for i in range(len(regx)):
        value = value.replace(regx[i], _colors[i])
    return value


def colored_print(value: str) -> None:
    regx = re.findall(r"%\w+%", value)
    print(_replace_colors([c.split('%')[1].upper() for c in regx], value, regx))


def delay_print(value: str, delay: float) -> None:
    for letter in value:
        print(letter, end='')
        time.sleep(delay)
