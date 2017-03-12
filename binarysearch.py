import unittest


def search(A, p, r, x):
    if len(A) == 0:
        return None
    elif r < 0 or p > len(A):
        return None
    elif p == r:
        if A[p] == x:
            return p
        else:
            return None
    else:
        q = (r-p) // 2
        if A[q] == x:
            return q
        elif x > A[q]:
            return search(A, q+1, r, x)
        else:
            return search(A, p, q-1, x)


class SearchTestCase(unittest.TestCase):
    def test0(self):
        A = []
        p, r, x = 0, 0, 0
        self.assertIsNone(search(A, p, r, x))

    def test1(self):
        A = [1]

        p, r, x = 0, 0, 1
        self.assertEqual(0, search(A, p, r, x))

        p, r, x = 0, 0, 2
        self.assertEqual(None, search(A, p, r, x))

        p, r, x = 0, 0, 0
        self.assertEqual(None, search(A, p, r, x))

    def test2(self):
        A = [1, 2]

        p, r, x = 0, 1, 1
        self.assertEqual(0, search(A, p, r, x))

        p, r, x = 0, 1, 2
        self.assertEqual(1, search(A, p, r, x))

        p, r, x = 0, 1, 0
        self.assertEqual(None, search(A, p, r, x))

        p, r, x = 0, 1, 0
        self.assertEqual(None, search(A, p, r, x))

    def test3(self):
        A = [1, 2, 3]

        p, r, x = 0, 2, 1
        self.assertEqual(0, search(A, p, r, x))

        p, r, x = 0, 2, 2
        self.assertEqual(1, search(A, p, r, x))

        p, r, x = 0, 2, 3
        self.assertEqual(2, search(A, p, r, x))

        p, r, x = 0, 2, 0
        self.assertEqual(None, search(A, p, r, x))

        p, r, x = 0, 2, 4
        self.assertEqual(None, search(A, p, r, x))