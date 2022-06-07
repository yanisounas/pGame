import random

from Game.Core.Entity.Entity import Entity


class Mob(Entity):
    def __init__(self, pos_x: int, pos_y: int) -> None:
        super().__init__()
        self._id = random.randint(1, 10000)
        self._pos = {'x': pos_x, 'y': pos_y}