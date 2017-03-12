import unittest


def get_rightmost_set_bit(n):
    if n <= 0:
        raise ValueError('n must be greater than 0')
    else:
        return ~(n-1) & n


class GetRightmostSetBitTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(get_rightmost_set_bit(0b1010), 2)
        self.assertEqual(get_rightmost_set_bit(0b1011), 1)
        self.assertEqual(get_rightmost_set_bit(0b1000), 8)
        self.assertEqual(get_rightmost_set_bit(0b10000), 16)
        self.assertEqual(get_rightmost_set_bit(0b11111), 1)


if __name__ == '__main__':
    unittest.main()