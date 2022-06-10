from Game.Core.Map.Cell.Cell import *


class Map:
    def __init__(self, map_size_x: int, map_size_y: int) -> None:
        self._map_size = {'x': map_size_x, 'y': map_size_y}
        self._cells = []

    def __str__(self) -> str:
        return f"{self._cells}"

    def create(self) -> None:
        for i in range(self._map_size['x']):
            self._cells.append([])
            for j in range(self._map_size['y']):
                self._cells[i].append(Cell(i, j))

    def attach(self, entity: Entity, cell_x: int = 0, cell_y: int = 0) -> None:
        cell_x = 0 if cell_x > len(self._cells) - 1 else cell_x
        cell_y = 0 if cell_y > len(self._cells[0]) - 1 else cell_y
        entity.pos = {'x': cell_x, 'y': cell_y}
        self._cells[cell_x][cell_y] += {"id": entity.id, "obj": entity}

    def move(self, player: Entity, dest_x: int, dest_y: int) -> None:
        dest_x = 0 if dest_x > len(self._cells) - 1 else dest_x
        dest_y = 0 if dest_y > len(self._cells[0]) - 1 else dest_y
        self._cells[player.pos['x']][player.pos['y']] -= 0
        player.pos = {'x': dest_x, 'y': dest_y}
        self._cells[dest_x][dest_y] += {"id": 0, "obj": player}

    def clear_entities(self) -> None:
        for row in self._cells:
            for column in row:
                column.clear_entities()

    @property
    def cells(self) -> list: return self._cells
