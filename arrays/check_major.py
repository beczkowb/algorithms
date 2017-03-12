import unittest


def max_left_x(A, x, i, j):
    if i > j:
        return None

    c = (j-i) // 2 + i
    if A[c] == x:
        result = max_left_x(A, x, i, c-1)
        return result if result is not None else c
    else:
        return max_left_x(A, x, c+1, j)


def check_major(A, x):
    i = 0
    j = len(A) - 1
    c = (j-i) // 2
    result = max_left_x(A, x, i, j)

    return result is not None and A[c] == x and A[len(A) // 2 + result] == x


class MaxLeftXTestCase(unittest.TestCase):
    def test(self):
        A = [1, 1, 1, 3, 4]
        self.assertEqual(0, max_left_x(A, 1, 0, len(A) - 1))

        A = [0, 1, 1, 1, 3, 4]
        self.assertEqual(1, max_left_x(A, 1, 0, len(A) - 1))

        A = [0, 0, 1, 1, 1, 3, 4]
        self.assertEqual(2, max_left_x(A, 1, 0, len(A) - 1))

        A = [0, 0, 1, 1, 1, 3, 4]
        self.assertEqual(None, max_left_x(A, 10, 0, len(A) - 1))

        A = [0, 0, 1, 1, 1, 3, 4]
        self.assertEqual(None, max_left_x(A, -1, 0, len(A) - 1))

        A = [0]
        self.assertEqual(0, max_left_x(A, 0, 0, len(A) - 1))

        A = [0, 1]
        self.assertEqual(0, max_left_x(A, 0, 0, len(A) - 1))


class CheckMajorTestCase(unittest.TestCase):
    def test(self):
        A = [1, 1, 1, 3, 4]
        self.assertEqual(True, check_major(A, 1))
        self.assertEqual(False, check_major(A, 3))
        self.assertEqual(False, check_major(A, 4))
        self.assertEqual(False, check_major(A, 5))
        self.assertEqual(False, check_major(A, 0))

        A = [0, 1, 2, 2]
        self.assertEqual(False, check_major(A, 2))


if __name__ == '__main__':
    unittest.main()