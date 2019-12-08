import unittest

from intcode_computer5 import IntcodeComputer


class Test(unittest.TestCase):

    def test_0_execute(self):
        executor = IntcodeComputer([1, 0, 0, 0, 99])
        result = executor.execute()
        self.assertListEqual([2, 0, 0, 0, 99], result)

    def test_1_execute(self):
        executor = IntcodeComputer([2, 3, 0, 3, 99])
        result = executor.execute()
        self.assertListEqual([2, 3, 0, 6, 99], result)

    def test_2_execute(self):
        executor = IntcodeComputer([2, 4, 4, 5, 99, 0])
        result = executor.execute()
        self.assertListEqual([2, 4, 4, 5, 99, 9801], result)

    def test_3_execute(self):
        executor = IntcodeComputer([1, 1, 1, 4, 99, 5, 6, 0, 99])
        result = executor.execute()
        self.assertListEqual([30, 1, 1, 4, 2, 5, 6, 0, 99], result)

    def test_4_execute(self):
        executor = IntcodeComputer([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        result = executor.execute()
        self.assertListEqual([3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50], result)


if __name__ == '__main__':
    unittest.main()
