import unittest


def binary_sum(A, B, C):
    borrow = 0
    for j in range(len(A)-1, -1, -1):
        x = A[j] + B[j] + borrow
        if x == 0:
            C[j+1] = 0
            borrow = 0
        elif x == 1:
            C[j+1] = 1
            borrow = 0
        elif x == 2:
            C[j+1] = 0
            borrow = 1
        else:
            C[j+1] = 1
            borrow = 1

    C[0] = borrow


class BinarySumTestCase(unittest.TestCase):
    def test(self):
        C = [0, 0, 0]
        A = [1, 1]
        B = [1, 1]
        binary_sum(A, B, C)
        self.assertListEqual(C, [1, 1, 0])
