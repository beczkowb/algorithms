import unittest
from .stack import Stack


def next_larger_element(A):
    stack = Stack()
    stack.push(A[0])
    next_elements = {}
    for x in A[1:]:
        if stack.peek() > x:
            stack.push(x)
        else:
            while not stack.is_empty() and stack.peek() < x:
                next_elements[stack.pop()] = x
            stack.push(x)

    while not stack.is_empty():
        next_elements[stack.pop()] = -1

    ordered_next_elements = []
    for x in A:
        ordered_next_elements.append(next_elements[x])
    return ordered_next_elements


class NextLargerElementTestCase(unittest.TestCase):
    def test(self):
        # A = [4, 1, 5, 2, 10]
        # expected_result = [5, 5, 10, 10, -1]
        # self.assertEqual(next_larger_element(A), expected_result)
        #
        # A = [4]
        # expected_result = [-1]
        # self.assertEqual(next_larger_element(A), expected_result)

        A = [5, 3, 2, 10, 6, 8, 1, 4, 12, 7]
        expected_result = [10, 10, 10, 12, 8, 12, 4, 12, -1, -1]
        self.assertEqual(next_larger_element(A), expected_result)