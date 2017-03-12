import unittest
from functools import reduce


def get_number_occurring_odd_number_of_times(A):
    if len(A) == 0:
        raise ValueError('A len must be greater than 0')
    else:
        # current_value = A[0]
        # for i in range(1, len(A)):
        #     current_value ^= A[i]
        # return current_value

        # return reduce(lambda x, y: x ^ y, A)

        current_value = 0
        for x in A:
            current_value ^= x

        return current_value


class GetNumberOccurringOddNumberOfTimes(unittest.TestCase):
    def test(self):
        self.assertEqual(get_number_occurring_odd_number_of_times([1,1, 2]), 2)
        self.assertEqual(get_number_occurring_odd_number_of_times([1, 2, 1]), 2)
        self.assertEqual(get_number_occurring_odd_number_of_times([1]), 1)
        self.assertEqual(get_number_occurring_odd_number_of_times([1, 2, 2, 1, 5, 6, 5, 6, 9, 3, 9]), 3)
        self.assertEqual(get_number_occurring_odd_number_of_times([3, 2, 2, 1, 5, 6, 5, 6, 9, 1, 9]), 3)