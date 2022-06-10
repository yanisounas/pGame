from Game import Game
from Game.CLI import *
from Game.Core.Settings.Settings import Settings
from Game.Core.Weapon.Weapon import Weapon


def main():

    # TODO: Système de Mob plus complet

    # TODO: Loot() \
    #  (Argent, XP et Weapons qui se drop sur les Mob, après une Battle(), en fonction de leur nombre, du niveau)

    # TODO: Remplacer les exceptions built-in

    gm = Game.GameMaker("Test")
    gm.load_map()
    for row in gm.map.cells:
        for column in row:
            print(f"{column.cell_pos['x']};{column.cell_pos['y']} {column.entities}")
    pass


if __name__ == "__main__":
    main()
