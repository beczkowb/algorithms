import unittest


def to_decimal(x: int, base: int):
    x = str(x)
    result = 0
    for i in range(len(x)-1, -1, -1):
        digit = x[i]
        digit = int(digit)
        result += digit * (base**(len(x)-1-i))

    return result


def r_decimal(x: str, p: int):
    l, r = x.split(".")
    l = to_decimal_horner(int(l), p)
    z = len(r)
    r = to_decimal_horner(int(r), p)
    r /= (p**z)
    return l+r


def change_system(x, p, result=None):
    if result is None:
        result = []
        change_system(x, p, result)
        return ''.join([str(d) for d in result])
    else:
        result.insert(0, x % p)
        if x // 2 != 0:
            change_system(x//2, p, result)


def to_decimal_horner(number, p, i=None):
    if i is None:
        number = str(number)
        number = [int(x) for x in number]
        i = len(number) - 1

    if i == 0:
        return number[i]
    else:
        return p*to_decimal_horner(number, p, i-1) + number[i]


class ToDecimalTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(7210, to_decimal(53214, 6))
        self.assertEqual(4, to_decimal(100, 2))
        self.assertEqual(1000, to_decimal(1111101000, 2))
        self.assertEqual(1000, to_decimal(1101001, 3))


class ToDecimalHornerTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(7210, to_decimal_horner(53214, 6))
        self.assertEqual(4, to_decimal_horner(100, 2))


class ChangeSystemTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual('1111101000', change_system(1000, 2))
        self.assertEqual('11', change_system(3, 2))
        self.assertEqual('0', change_system(0, 2))


class RDecimalTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(r_decimal('0.4231', 5), 566/625)

if __name__ == '__main__':
    unittest.main()