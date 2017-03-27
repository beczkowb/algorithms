import unittest
import math


def pow(a, n):
    if n == 1:
        return a
    else:
        return pow(a, n-1) * a


def fast_pow(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        return pow(a, n//2)**2
    else:
        return pow(a, n-1) * a



class PowTestCase(unittest.TestCase):
    def test(self):
        a, n, expected = 2, 3, 8
        self.assertEqual(expected, pow(a, n))

        a, n, expected = 3, 2, 9
        self.assertEqual(expected, pow(a, n))

        a, n, expected = 8, 10, math.pow(8, 10)
        self.assertEqual(expected, pow(a, n))

        a, n, expected = 8, 300, math.pow(8, 300)
        self.assertEqual(expected, pow(a, n))

    def test_fast(self):
        a, n, expected = 2, 3, 8
        self.assertEqual(expected, fast_pow(a, n))

        a, n, expected = 3, 2, 9
        self.assertEqual(expected, fast_pow(a, n))

        a, n, expected = 8, 10, math.pow(8, 10)
        self.assertEqual(expected, fast_pow(a, n))

        a, n, expected = 8, 300, math.pow(8, 300)
        self.assertEqual(expected, fast_pow(a, n))
