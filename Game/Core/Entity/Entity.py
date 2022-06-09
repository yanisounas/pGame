from Game.Core.Weapon.Weapon import Weapon


class Entity:
    def __init__(self) -> None:
        self._id = 0
        self._pos = {'x': None, 'y': None}
        self._name = None
        self._life_points = 100
        self._damages = 10
        self._weapon = Weapon(0)
        self._level = 1
        self._cell = None

    @property
    def id(self) -> int: return self._id
    @property
    def pos(self) -> dict: return self._pos
    @property
    def name(self) -> str: return self._name
    @property
    def life_points(self) -> int: return self._life_points
    @property
    def damages(self) -> int: return self._damages
    @property
    def weapon(self) -> Weapon: return self._weapon
    @property
    def level(self) -> int: return self._level
    @id.setter
    def id(self, id: int) -> None: self._id = id
    @pos.setter
    def pos(self, pos: dict) -> None: self._pos = pos
    @name.setter
    def name(self, name: str) -> None: self._name = name
    @life_points.setter
    def life_points(self, life_points: int) -> None: self._life_points = life_points
    @damages.setter
    def damages(self, damages: int) -> None: self._damages = damages
    @weapon.setter
    def weapon(self, weapon: Weapon) -> None: self._weapon = weapon
    @level.setter
    def level(self, level: int) -> None: self._level = level

