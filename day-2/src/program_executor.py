class Executor:
    program = []

    def execute(self):
        program = self.program
        # execute every forth opcode
        for index in range(0, len(program), 4):
            opcode = program[index]
            print(opcode)
            print(program)
            if opcode == 1:
                print("Adding", program[program[index + 2]], program[program[index + 1]])
                program[index + 3] = program[program[index + 2]] + program[program[index + 1]]
            elif opcode == 2:
                print("Multiplying", program[program[index + 2]], program[program[index + 1]])
                program[index + 3] = program[program[index + 2]] * program[program[index + 1]]
            elif opcode == 99:
                print("Program terminated. Final program:", program)
                break
            else:
                print("Error during program execution at position", index,
                      "with opcode", opcode)
                break

    def __init__(self, program):
        self.program = program
