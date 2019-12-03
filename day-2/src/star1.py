#!/usr/bin/python3
from program_executor import Executor

def load_program():
    with open("input.txt") as file:
        content = file.readlines()

    content = [x.strip() for x in content]

    program = []

    for line in content:
        items = line.split(",")
        program += [int(item) for item in items]

    return program


# program = load_program()
program = [1, 1, 1, 4, 99, 5, 6, 0, 99]

# restore gravity assist program to 1202
# program[1] = 12
# program[2] = 2


print(program)

executor = Executor(program)
executor.execute()


