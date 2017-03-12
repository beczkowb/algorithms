import unittest


def segregate(A):
    if len(A) == 0:
        return A

    l, r = 0, len(A) - 1

    while r > l:
        while r > l and A[r] == 1:
            r -= 1

        while r > l and A[l] == 0:
            l += 1

        A[l], A[r] = A[r], A[l]

    return A


class SegregateTestCase(unittest.TestCase):
    def test(self):
        A = [1, 0, 0, 1, 1]
        A = segregate(A)
        self.assertEqual(A, [0, 0, 1, 1, 1])