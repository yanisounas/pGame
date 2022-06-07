from Game.Core.Entity.Player import Player
from Game.Core.Map.Cell.Cell import Cell


class Battle:
    def __init__(self, player: Player, cell: Cell, **kwargs) -> None:
        self._player = player
        self._entities_up = kwargs if kwargs else cell.get_mobs()
        self._entities_down = {}
        self._cell = cell

    @property
    def player(self) -> Player: return self._player
    @property
    def entities_up(self) -> dict: return self._entities_up
    @property
    def entities_down(self) -> dict: return self._entities_down
    @property
    def cell(self) -> Cell: return self._cell
