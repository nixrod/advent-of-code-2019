import sys

from wire_path import Wirepath
import numpy as np


class GridSolver:

    @staticmethod
    def find_shortest_manhattan_distance_node(path1: Wirepath, path2: Wirepath) -> int:
        path_sum = np.add(path1.grid, path2.grid)
        nodes = np.where(path_sum == 2)
        lowest_distance = sys.maxsize

        for i in range(nodes[0].size):
            node = (nodes[0][i], nodes[1][i])
            distance = GridSolver._calculate_manhattan_distance(node)
            if distance < lowest_distance:
                lowest_distance = distance
        return lowest_distance

    @staticmethod
    def find_shortest_path_distance_node(path1: Wirepath, path2: Wirepath) -> int:
        # This would require some form of path finding algorithm.
        # Dijkstra or A* come to mind.
        return 3

    @staticmethod
    def _calculate_manhattan_distance(node: tuple) -> int:
        # see https://en.wikipedia.org/wiki/Taxicab_geometry
        zero = Wirepath.PATH_ZERO
        return np.abs(node[0] - zero[0]) + np.abs(node[1] - zero[1])

    def __init__(self) -> None:
        super().__init__()
