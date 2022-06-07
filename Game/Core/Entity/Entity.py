class Entity:
    def __init__(self) -> None:
        self._id = 0
        self._pos = {'x': None, 'y': None}
        self._name = None
        self._life_points = 100
        self._damages = 10
        self._weapon_type = None
        self._weapon_id = 0
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
    def weapon_id(self) -> int: return self._weapon_id
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
    @weapon_id.setter
    def weapon_id(self, weapon_id: int) -> None: self._weapon_id = weapon_id
    @level.setter
    def level(self, level: int) -> None: self._level = level

