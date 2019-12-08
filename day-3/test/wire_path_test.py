import unittest

from grid_solver import GridSolver
from wire_path import Wirepath


class Test(unittest.TestCase):

    def test_0_execute(self):
        path1 = Wirepath()
        path1.set_wires(["R8", "U5", "L5", "D3"])

        path2 = Wirepath()
        path2.set_wires(["U7", "R6", "D4", "L4"])

        grid_solver = GridSolver()
        solution = grid_solver.solve_grid(path1, path2)
        self.assertEqual(6, solution)

    def test_1_execute(self):
        path1 = Wirepath()
        path1.set_wires(["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"])

        path2 = Wirepath()
        path2.set_wires(["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"])

        grid_solver = GridSolver()
        solution = grid_solver.solve_grid(path1, path2)
        self.assertEqual(159, solution)

    def test_2_execute(self):
        path1 = Wirepath()
        path1.set_wires(["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"])

        path2 = Wirepath()
        path2.set_wires(["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"])

        grid_solver = GridSolver()
        solution = grid_solver.solve_grid(path1, path2)
        self.assertEqual(135, solution)


if __name__ == '__main__':
    unittest.main()
