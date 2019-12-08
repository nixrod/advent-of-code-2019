import unittest

from password_checker import PasswordChecker


class Test(unittest.TestCase):

    def test_0_execute(self):
        self.assertTrue(PasswordChecker.has_adjacent_digits_strict(112233))

    def test_1_execute(self):
        self.assertFalse(PasswordChecker.has_adjacent_digits_strict(123444))

    def test_2_execute(self):
        self.assertTrue(PasswordChecker.has_adjacent_digits_strict(111122))

    def test_3_execute(self):
        self.assertFalse(PasswordChecker.digits_all_increase(223450))


if __name__ == '__main__':
    unittest.main()
