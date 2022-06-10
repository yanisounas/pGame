from typing import List, Dict

from Game.Core.Entity.Entity import Entity


class Cell:
    def __init__(self, cell_pos_x: int, cell_pos_y: int) -> None:
        self._id = None
        self._cell_pos = {'x': cell_pos_x, 'y': cell_pos_y}
        self._entities = {}

    def __add__(self, entities: Dict or List) -> object:
        self.add_entity(entities)
        return self

    def __sub__(self, entity_id: int) -> object:
        self.remove_entity(entity_id)
        return self

    def __repr__(self) -> str:
        return f"<Cell [{self._cell_pos['x']}, {self._cell_pos['y']}]>"

    def add_entity(self, entity: Dict[str, Entity]) -> None:
        self._entities[entity['id']] = entity['obj']

    def add_entities(self, entities: List[Dict[str, Entity]]) -> None:
        for entity in entities:
            self.add_entity(entity)

    def remove_entity(self, entity_id: int) -> int:
        try:
            del self._entities[entity_id]
            return 1
        except KeyError:
            return 0

    def clear_entities(self) -> None:
        self._entities = {}

    def get_mobs(self) -> List:
        tmp = []
        for entity in self._entities:
            if entity != 0:
                tmp.append({"entity_id": self._entities[entity].id, "obj": self._entities[entity]})
        return tmp

    @property
    def entities(self) -> Dict: return self._entities
    @property
    def cell_pos(self) -> Dict: return self._cell_pos
