import unittest


def move_to_end(A):
    j = len(A) - 1
    for i in range(len(A)-1, -1, -1):
        if A[i] is not None:
            A[j] = A[i]
            j -= 1


def merge(MN, N):
    move_to_end(MN)
    i = len(N)
    j = 0
    k = 0
    while j < len(N) and i < len(MN):
        if N[j] < MN[i]:
            MN[k] = N[j]
            j += 1
        else:
            MN[k] = MN[i]
            i += 1

        k += 1

    if j != len(N):
        while j < len(N):
            MN[k] = N[j]
            k += 1
            j += 1
    elif i != len(MN):
        while i < len(MN):
            MN[k] = N[i]
            k += 1
            i += 1

    return MN


class MergeTestCase(unittest.TestCase):
    def test(self):
        MN = [2, None, 7, None, None, 10, None]
        N = [5, 8, 12, 14]
        merge(MN, N)
        self.assertEqual(MN, [2, 5, 7, 8, 10, 12, 14])

        MN = []
        N = []
        merge(MN, N)
        self.assertEqual(MN, [])

        MN = [None, 1]
        N = [2]
        merge(MN, N)
        self.assertEqual(MN, [1, 2])

        MN = [None, 2, 3, None]
        N = [2, 3]
        merge(MN, N)
        self.assertEqual(MN, [2, 2, 3, 3])