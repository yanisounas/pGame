from Game import Game
from Game.CLI import *
from Game.Core.Settings.Settings import Settings
from Game.Core.Weapon.Weapon import Weapon


def main():
    # TODO: Battle() \
    #  (se lance lorsqu'un player souhaite attaquer tous les mobs de sa map ou \
    #  lorsque le player s'approche d'un mob et donc se fait agresser)

    # TODO: Système de Weapon

    # TODO: Système de Mob plus complet \
    #  (+ Les Mob spawn dès que le player arrive sur la map, pas la cellule, changer ça)

    # TODO: Les Settings

    # TODO: Loot() \
    #  (Argent, XP et Weapons qui se drop sur les Mob, après une Battle(), en fonction de leur nombre, du niveau)

    # TODO: Remplacer les exceptions built-in

    gm = Game.GameMaker("Test")
    gm.load_map()
    for row in gm.map.cells:
        for column in row:
            print(column.entities)
    pass


if __name__ == "__main__":
    main()
