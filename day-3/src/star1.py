#!/usr/bin/python3
from wire_path import Wirepath


def load_program():
    with open("input.txt") as file:
        content = file.readlines()

    content = [x.strip() for x in content]

    program = []

    for line in content:
        items = line.split(",")
        program += [int(item) for item in items]

    return program


grid = Wirepath()
