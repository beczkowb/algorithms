import unittest


def find_smallest_missing_number(A, m):
    # http://www.geeksforgeeks.org/find-the-first-missing-number/
    if A[0] != 0:
        return 0

    for i in range(1, len(A)):
        if A[i] - 1 != A[i-1]:
            return A[i-1] + 1

    if A[-1] != m-1:
        return A[-1] + 1


class FindSmallestMissingNumber(unittest.TestCase):
    def test(self):
        self.assertEqual(1, find_smallest_missing_number([0], 10))
        self.assertEqual(1, find_smallest_missing_number([0, 5], 10))
        self.assertEqual(2, find_smallest_missing_number([0, 1], 10))
        self.assertEqual(7, find_smallest_missing_number([0, 1, 2, 3, 4, 5, 6, 10], 10))