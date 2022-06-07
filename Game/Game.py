import random

from Game.Core.Battle.Battle import Battle
from Game.Core.Entity.Player import Player
from Game.Core.Entity.Mob import Mob
from Game.Core.Map.Map import Map
from Game.Core.Settings.Settings import Settings


class GameMaker:
    def __init__(self, player_name: str, map_x: int = 5, map_y: int = 5) -> None:
        self._settings = Settings("./Game/Core/Settings/Data/",
                                  conf="__conf.json",
                                  entities="__entities.json",
                                  weapons="__weapons.json")
        self._player = Player(player_name)
        self._map_size = [map_x, map_y]
        self._map = Map(self._map_size[0], self._map_size[1])
        self._current_battles = []

    def load_game(self):
        self.map.create()
        self.map.attach(self._player)

    def move_player(self, dest_x: int, dest_y: int):
        self.map.clear_entities()
        self.map.move(self._player, dest_x, dest_y)
        [self.map.attach(Mob(dest_x, dest_y), dest_x, dest_y) for _ in range(random.randint(2, 5))]

    def begin_battle(self, player) -> Battle:
        pass

    @property
    def player_cell(self): return self.map.cells[self._player.pos["x"]][self._player.pos["y"]]
    @property
    def settings(self) -> Settings: return self._settings
    @property
    def map_x(self) -> int: return self._map_size[0]
    @property
    def map_y(self) -> int: return self._map_size[1]
    @property
    def player(self) -> Player: return self._player
    @property
    def map(self) -> Map: return self._map
    @map_x.setter
    def map_x(self, x: int) -> None: self._map_size[0] = x
    @map_y.setter
    def map_y(self, y: int) -> None: self._map_size[1] = y
