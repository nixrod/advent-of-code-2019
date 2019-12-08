#!/usr/bin/env python3
from wire_path import Wirepath
from grid_solver import GridSolver


def solve_cable_routing():
    with open("input.txt") as file:
        content = file.readlines()

    content = [x.strip() for x in content]

    path1 = Wirepath()
    path1.set_wires(content[0].split(","))

    path2 = Wirepath()
    path2.set_wires(content[1].split(","))

    solution = GridSolver.find_shortest_manhattan_distance_node(path1, path2)
    print("Closest intersection has distance of", solution)


solve_cable_routing()
