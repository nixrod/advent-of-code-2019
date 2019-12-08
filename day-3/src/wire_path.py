import numpy as np
from wire import Wire


class Wirepath:
    # This is not the best performing solution ;)
    PATH_SIZE = (20000, 20000)
    PATH_ZERO = (10000, 10000)

    grid = []
    _current_row = PATH_ZERO[0]
    _current_col = PATH_ZERO[1]

    def set_wires(self, instructions: list):
        for instruction in instructions:
            wire = Wire(instruction)
            self._set_wire_points(wire)

    def _set_wire_points(self, wire: Wire):
        for _ in range(wire.size):
            if wire.direction == "U":
                self._current_row -= 1
            elif wire.direction == "D":
                self._current_row += 1
            elif wire.direction == "L":
                self._current_col -= 1
            elif wire.direction == "R":
                self._current_col += 1
            else:
                print("Error. Unknown direction", wire.direction, "skipping wire")
                return

            self.grid[self._current_row, self._current_col] = 1

    def __init__(self) -> None:
        self.grid = np.zeros([self.PATH_SIZE[0], self.PATH_SIZE[1]], dtype=int)
        super().__init__()
