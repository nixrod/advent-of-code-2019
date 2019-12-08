class PasswordChecker:
    @staticmethod
    def has_adjacent_digits(num: int) -> bool:
        num_str = str(num)
        last_char = "X"
        for char in num_str:
            if char == last_char:
                return True
            last_char = char
        return False

    @staticmethod
    def has_adjacent_digits_strict(num: int) -> bool:
        # find a group of exactly two
        num_str = str(num)
        last_char = "X"
        counter = 1
        for char in num_str:
            if char == last_char:
                counter += 1
                continue
            if counter == 2:
                return True
            counter = 1
            last_char = char
        if counter == 2:
            return True
        return False

    @staticmethod
    def digits_all_increase(num: int) -> bool:
        num_str = str(num)
        int_list = [int(d) for d in num_str]

        last_digit = 0
        for digit in int_list:
            if digit < last_digit:
                return False
            last_digit = digit
        return True
