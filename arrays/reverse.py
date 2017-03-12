import unittest


def reverse(A):
    if len(A) <= 1:
        return A

    for i in range(len(A) // 2):
        tmp = A[len(A) - 1 - i]
        A[len(A) - 1 - i] = A[i]
        A[i] = tmp

    return A


class ReverseTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse([]), [])
        self.assertEqual(reverse([1]), [1])
        self.assertEqual(reverse([1, 2]), [2, 1])
        self.assertEqual(reverse([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse([1, 2, 3, 4]), [4, 3, 2, 1])