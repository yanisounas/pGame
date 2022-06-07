from Game.Core.Entity.Entity import Entity


class Player(Entity):
    def __init__(self, name: str) -> None:
        super().__init__()
        self._name = name
