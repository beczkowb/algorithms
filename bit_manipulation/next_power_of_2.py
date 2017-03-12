import unittest


def next_power_of_2(n):
    if ((n-1)&n) == 0 and n != 0:
        return n
    else:
        p = 1
        while p < n:
            p <<= 1
        return p


class NextPowerOf2TestCase(unittest.TestCase):
    def test(self):
        np2 = next_power_of_2
        self.assertEqual(np2(0), 1)
        self.assertEqual(np2(1), 1)
        self.assertEqual(np2(2), 2)
        self.assertEqual(np2(3), 4)
        self.assertEqual(np2(4), 4)
        self.assertEqual(np2(5), 8)
        self.assertEqual(np2(6), 8)
        self.assertEqual(np2(7), 8)
        self.assertEqual(np2(8), 8)
        self.assertEqual(np2(9), 16)


if __name__ == '__main__':
    unittest.main()
