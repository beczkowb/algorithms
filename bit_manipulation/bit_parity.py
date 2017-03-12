import unittest


def has_odd_parity(n):
    odd_parity = False
    while n:
        n &= (n-1)
        odd_parity = not odd_parity
    return odd_parity


class HasOddParityTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(has_odd_parity(0b1100), False)
        self.assertEqual(has_odd_parity(0b0), False)
        self.assertEqual(has_odd_parity(0b10), True)
        self.assertEqual(has_odd_parity(0b11), False)
        self.assertEqual(has_odd_parity(0b1), True)
        self.assertEqual(has_odd_parity(0b111), True)
        self.assertEqual(has_odd_parity(0b11111), True)
        self.assertEqual(has_odd_parity(0b11001), True)


if __name__ == '__main__':
    unittest.main()
