from Game.Core.Entity.Entity import Entity
from Game.Core.Entity.Player import Player
from Game.Core.Map.Cell.Cell import Cell


class Battle:
    def __init__(self, player: Player, cell: Cell, **kwargs) -> None:
        self._cell = cell
        self._player = player
        self._entities_up = kwargs if kwargs else self._cell.get_mobs()
        self._entities_down = {}
        self._turn = 0

    def attack(self, attacker: Entity, target: Entity):
        target.life_points -= attacker.damages * attacker.weapon.damages_mult
        self._turn += 1

    def next_turn(self):
        if self._turn == 0:
            return

        self.attack(self.entities_up[self._turn-1]["obj"], self._player)

        if self._turn == len(self.entities_up) + 1:
            self._turn = 0

        self.next_turn()



    @property
    def player(self) -> Player: return self._player
    @property
    def entities_up(self) -> dict: return self._entities_up
    @property
    def entities_down(self) -> dict: return self._entities_down
    @property
    def cell(self) -> Cell: return self._cell
