import unittest


def max_center_subarray(arr, mid):
    current_sum = 0
    left_max = mid
    max_sum_left = arr[mid]
    for i in range(mid, -1, -1):
        current_sum += arr[i]
        if max_sum_left < current_sum:
            max_sum_left = current_sum
            left_max = i

    current_sum = 0
    right_max = mid
    max_sum_right = arr[mid]
    for i in range(mid, len(arr)):
        current_sum += arr[i]
        if max_sum_right < current_sum:
            max_sum_right = current_sum
            right_max = i

    return left_max, right_max, max_sum_right+max_sum_left-arr[mid]


def max_subarray(A):
    if len(A) == 0:
        raise ValueError('len(A) must be greater than 0')

    cm, cmi, cmj = 0, 0, 0
    m, mi, mj = 0, 0, 0

    for i, x in enumerate(A):
        cm += x
        cmj = i

        if cm < 0:
            cm = 0
            cmi, cmj = i+1, i+1

        if cm > m:
            m = cm
            mi, mj = cmi, cmj

    return mi, mj


class MaxSubarrayTestCase(unittest.TestCase):
    def test_center(self):
        arr = [-1, 2, 0, -3, 5, 6, -2, -4, 10]
        expected_result = (4, 8)

        self.assertEqual(expected_result, max_subarray(arr))

    def test_2(self):
        arr = [1, 20, 1, -3, 1, 1, -2, -4, 1]
        expected_result = (0, 2)

        self.assertEqual(expected_result, max_subarray(arr))

    def test_3(self):
        arr = [1, 20, 1, -3, 30, 9, -2, -4, 1]
        expected_result = (0, 5)

        self.assertEqual(expected_result, max_subarray(arr))

    def test_4(self):
        arr = [1, 20, 1, -3000, 30, 9, -2, -4, 1]
        expected_result = (4, 5)

        self.assertEqual(expected_result, max_subarray(arr))

    def test_5(self):
        arr = [1]
        expected_result = (0, 0)

        self.assertEqual(expected_result, max_subarray(arr))

    def test_6(self):
        arr = [1, -1]
        expected_result = (0, 0)

        self.assertEqual(expected_result, max_subarray(arr))

    def test_7(self):
        arr = [1, -2, 9]
        expected_result = (2, 2)

        self.assertEqual(expected_result, max_subarray(arr))


if __name__ == '__main__':
    unittest.main()