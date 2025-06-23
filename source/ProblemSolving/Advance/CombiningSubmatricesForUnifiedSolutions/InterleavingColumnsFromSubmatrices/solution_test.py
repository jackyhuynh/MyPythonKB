import unittest
from solution import solution

class TestSolution(unittest.TestCase):
    def test1(self):
        input_data = (
            [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]],

            [[-11, -12, -13],
            [-14, -15, -16],
            [-17, -18, -19]],

            [(2, 3, 2, 3),
            (1, 2, 1, 2)]
        )
        self.assertEqual(solution(*input_data), [[6, -11, 7, -12], [10, -14, 11, -15]])

    def test2(self):
        input_data = (
            [[1, -2],
            [-1, 2]],

            [[-1, 2],
            [1, -2]],

            [(1, 2, 1, 2),
            (1, 2, 1, 2)]
        )
        self.assertEqual(solution(*input_data), [[1, -1, -2, 2], [-1, 1, 2, -2]])

    def test3(self):
        input_data = (
            [[1],
            [2]],

            [[-1],
            [-2]],

            [(1, 1, 1, 1),
            (1, 1, 1, 1)]
        )
        self.assertEqual(solution(*input_data), [[1, -1]])

    def test4(self):
        input_data = (
            [[0, 0, 0]],

            [[1, 1, 1]],

            [(1, 1, 1, 1),
            (1, 1, 1, 1)]
        )
        self.assertEqual(solution(*input_data), [[0, 1]])

    def test5(self):
        input_data = (
            [[89, -34, 23],
            [1, -3, 0]],

            [[-12, -8, 2],
            [7, -6, 10]],

            [(2, 2, 1, 3),
            (1, 1, 1, 3)]
        )
        self.assertEqual(solution(*input_data), [[1, -12, -3, -8, 0, 2]])

if __name__ == '__main__':
    unittest.main()