import numpy as np
from wire import Wire


class Wirepath:
    grid = np.zeros([2000, 2000], dtype=int)
    zero = (1000, 1000)
    current = (1000, 1000)

    def set_wires(self, instructions: list):
        for instruction in instructions:
            wire = Wire(instruction)
            if wire.direction == "U":
                print("U")
            elif wire.direction == "D":
                print("D")
            elif wire.direction == "L":
                print("L")
            elif wire.direction == "R":
                print("R")
            else:
                print("Error. Unknown direction", wire.direction, "skipping wire")

    def __init__(self) -> None:
        super().__init__()
