import unittest
import math
from .rightmost_set_bit import get_rightmost_set_bit


# another way is: log2(n&-n)+1
def get_position_of_rightmost_set_bit(n):
    rsb = get_rightmost_set_bit(n)
    return math.log2(rsb) + 1


class GetPositionOfRightmostSetBit(unittest.TestCase):
    def test(self):
        self.assertEqual(get_position_of_rightmost_set_bit(0b1010), 2)
        self.assertEqual(get_position_of_rightmost_set_bit(0b1011), 1)
        self.assertEqual(get_position_of_rightmost_set_bit(0b1100), 3)
        self.assertEqual(get_position_of_rightmost_set_bit(0b1), 1)
        self.assertEqual(get_position_of_rightmost_set_bit(0b111), 1)


if __name__ == '__main__':
    unittest.main()