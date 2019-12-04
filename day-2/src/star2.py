#!/usr/bin/python3
from intcode_computer import IntcodeComputer


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

# Bruteforce the noun verb combination
noun = 0
verb = 0

for noun in range(0, 99):
    for verb in range(0, 99):
        executor = IntcodeComputer(program.copy(), noun, verb)
        terminated_program = executor.execute()
        if terminated_program[0] == 19690720:
            print("Found noun verb combination:", noun, "/", verb)
            break

