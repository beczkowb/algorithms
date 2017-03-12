import random
import unittest


from . import selectionsort
from . import mergesort
from . import insertionsort
from . import bubblesort

functions = [bubblesort.sort]


def gen_test_case(sort_f):
    class SortTestCase(unittest.TestCase):
        def test_0(self):
            A = []
            B = sorted(A)
            sort_f(A)
            self.assertEqual(A, B)

        def test_1(self):
            A = [0]
            B = sorted(A)
            sort_f(A)
            self.assertEqual(A, B)

        def test_2(self):
            A = [1, 0]
            B = sorted(A)
            sort_f(A)
            self.assertEqual(A, B)

        def test_small(self):
            A = [3, 2, 5, 6]
            B = sorted(A)
            sort_f(A)
            self.assertEqual(A, B)

        def test_big_reversed(self):
            A = [i for i in range(10000, 1, -1)]
            B = sorted(A)
            sort_f(A)
            self.assertEqual(A, B)

        def trandom(self, min_size, max_size, a, b, number_of_subtests):
            for i in range(number_of_subtests):
                with self.subTest(i=i):
                    size = random.randint(min_size, max_size)
                    A = [random.randint(a, b) for i in range(size)]
                    B = sorted(A)
                    sort_f(A)
                    self.assertEqual(A, B)

        def test_small_random(self):
            self.trandom(0, 1000, -1000, 1000, 1000)

        def test_big_random(self):
            self.trandom(1000, 2000, -1000, 1000, 10)

    return SortTestCase


def run():
    suite = unittest.TestSuite()
    for f in functions:
        subsuite = unittest.defaultTestLoader.loadTestsFromTestCase(gen_test_case(f))
        suite.addTest(subsuite)

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
    return result