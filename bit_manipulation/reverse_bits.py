import unittest


def reverse_bits(x):
    n = 32
    result = x
    
    while x:
        result |= x & 1
        x >>= 1
        result <<= 1
        n -= 1
        
    result <<= n
    return result


class ReverseBitsTestCase(unittest.TestCase):
    def test(self):
        x = 0b1000
        
