class IntcodeComputer:
    program = []

    def execute(self) -> list:
        program = self.program
        # iterate between the opcodes, which are always on every forth position
        for instruction_pointer in range(0, len(program), 4):
            opcode = program[instruction_pointer]
            if opcode == 1:
                addition = self.get_param_value(instruction_pointer, 1) + self.get_param_value(instruction_pointer, 2)
                self.set_param_value(instruction_pointer, 3, addition)
            elif opcode == 2:
                multiplication = self.get_param_value(instruction_pointer, 1) * self.get_param_value(
                    instruction_pointer, 2)
                self.set_param_value(instruction_pointer, 3, multiplication)
            elif opcode == 99:
                print("Program terminated.")
                return program
            else:
                print("Error during program execution at position", instruction_pointer,
                      "with opcode", opcode)
                return program

    def get_param_value(self, opcode_address: int, param_number: int):
        """
        Returns the param belonging to a specific opcode
        :param opcode_address: The address of the opcode in the program
        :param param_number: An opcode always has 3 parameters. The value ranges from 1-3
        :return: the current value of the param
        """
        return self.program[self.program[opcode_address + param_number]]

    def set_param_value(self, opcode_address: int, param_number: int, value: int):
        """
        Updates the param belonging to a specific opcode
        :param opcode_address: The address of the opcode in the program
        :param param_number: An opcode always has 3 parameters. The value ranges from 1-3
        :param value: The value to write to the param
        """
        self.program[self.program[opcode_address + param_number]] = value

    def __init__(self, program: list, noun: int = None, verb: int = None):
        self.program = program
        if noun is not None:
            self.program[1] = noun
        if verb is not None:
            self.program[2] = verb
