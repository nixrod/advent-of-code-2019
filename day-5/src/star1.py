#!/usr/bin/env python3
from intcode_computer5 import IntcodeComputer


def load_program():
    with open("input.txt") as file:
        content = file.readlines()

    content = [x.strip() for x in content]

    program = []

    for line in content:
        items = line.split(",")
        program += [int(item) for item in items]

    return program


program = load_program()

executor = IntcodeComputer(program, 12, 2)
terminated_program = executor.execute()

print(terminated_program)
