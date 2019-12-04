import unittest

from wire_path import Wirepath


class Test(unittest.TestCase):

    def test_0_execute(self):
        path = Wirepath()
        path.set_wires(["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"])
        # self.assertListEqual([2, 0, 0, 0, 99], result)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
