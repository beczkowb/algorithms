import unittest


def find_pair_with_sum(A, x):
    A = list(sorted(A))
    i, j = 0, len(A) - 1
    while i != j:
        s = A[i] + A[j]
        if s == x:
            return True
        elif s > x:
            j -= 1
        else:
            i += 1
    else:
        return False


class FindPairWithSum(unittest.TestCase):
    def test(self):
        A = [1, 2, 1, 5, 6, 3, 20, 11, 11, 10]
        self.assertEqual(find_pair_with_sum(A, 5), True)