#!/usr/bin/python3
import math

def load_program():
    with open("input.txt") as file:
        content = file.readlines()

    content = [x.strip() for x in content]

    program = []

    for line in content:
        items = line.split(",")
        program += [int(item) for item in items]

    return program

#program = load_program()
program = [1,1,1,4,99,5,6,0,99]

# restore gravity assist program to 1202
#program[1] = 12
#program[2] = 2

print(program)

# execute every forth opcode
for index in range(0, len(program), 4):
    opcode = program[index]
    print(opcode)
    print(program)
    if (opcode == 1):
        print("Adding", program[program[index + 2]], program[program[index + 1]])
        program[index + 3] = program[program[index + 2]] + program[program[index + 1]]
    elif(opcode == 2):
        print("Multiplying", program[program[index + 2]], program[program[index + 1]])
        program[index + 3] = program[program[index + 2]] * program[program[index + 1]]
    elif(opcode == 99):
        print("Program terminated. Final program:", program)
        break
    else:
        print("Error during program execution at position", index,
            "with opcode", opcode)
        break
