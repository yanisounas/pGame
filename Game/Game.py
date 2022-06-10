import random

from Game.Core.Battle.Battle import Battle
from Game.Core.Entity.Player import Player
from Game.Core.Entity.Mob import Mob
from Game.Core.Map.Cell.Cell import Cell
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

    def next_map(self, map_x: int, map_y: int) -> None:
        self._map = Map(map_x, map_y)
        self._map_size = [map_x, map_y]
        self.load_map()

    def load_map(self) -> None:
        self.map.create()
        self.map.attach(self._player)
        for _ in range(random.randint(2, 5)):
            x = random.randint(1, self._map_size[0]-1)
            y = random.randint(1, self._map_size[1]-1)
            self.map.attach(Mob(x, y), x, y)

    def move_player(self, dest_x: int, dest_y: int) -> None:
        self.map.clear_entities()
        self.map.move(self._player, dest_x, dest_y)

    def begin_battle(self) -> Battle:
        battle = Battle(self._player, self.player_cell)
        self._current_battles.append(battle)
        return battle

    @property
    def player_cell(self) -> Cell: return self.map.cells[self._player.pos["x"]][self._player.pos["y"]]
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
