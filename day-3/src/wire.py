class Wire:

    direction = ""
    size = 0

    def __init__(self, instruction: str) -> None:
        super().__init__()
        self.direction = instruction[0]
        self.size = int(instruction[1:])
