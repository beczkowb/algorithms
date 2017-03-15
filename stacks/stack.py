import unittest


class Node:
    def __init__(self, data, prev=None):
        self.prev = prev
        self.data = data


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            self.top = Node(data, prev=self.top)

    def pop(self):
        if self.top:
            prev_top = self.top
            self.top = prev_top.prev
            return prev_top.data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None

    def is_empty(self):
        return self.peek() is None

    def __str__(self):
        elements = []
        current_node = self.top
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.prev
        return ' '.join([str(x) for x in elements])

    def __repr__(self):
        return self.__str__()


class SpecialStack:
    """
    [1, 2, 3]
    ---------
    [1]
    [1]
    ---------
    [1, 2]
    [1, 1]
    --------
    [1, 2, 3]
    [1, 1, 1]

    [5, 2, 1, 5, 6, 7, 6]
    --------------------
    [5]
    [5]
    --------------------
    [5, 2]
    [5, 2]
    ------------------
    [5, 2, 1]
    [5, 2, 1]
    ---------------
    [5, 2, 1, 5]
    [5, 2, 1, 1]
    --------------
    [5, 2, 1, 5, 6]
    [5, 2, 1, 1, 1]
    --------------
    [5, 2, 1, 5, 6, 7]
    [5, 2, 1, 1, 1, 1]
    """
    def __init__(self):
        self.main_stack = Stack()
        self.auxiliary_stack = Stack()

    def push(self, data):
        if self.main_stack.is_empty():
            self.auxiliary_stack.push(data)
        elif not self.main_stack.is_empty() and self.auxiliary_stack.peek() >= data:
            self.main_stack.push(data)
            self.auxiliary_stack.push(data)
        elif not self.main_stack.is_empty() and self.auxiliary_stack.peek() < data:
            self.auxiliary_stack.push(self.auxiliary_stack.peek())

        self.main_stack.push(data)

    def pop(self):
        self.auxiliary_stack.pop()
        return self.main_stack.pop()

    def is_empty(self):
        return self.main_stack.is_empty()

    def get_min(self):
        return self.auxiliary_stack.peek()


class DoubleStack:
    """
    [null, null]
    push1(4)
    [4, null]
     ^
     sprawdzic czy jest jakis null po prawej, jesli tak to spoko, jesli nie to rozszerzamy tablice
     push1(5)
     [4, 5]
         ^
    nie ma nulla wiec rozszerzam
    [4, 5, null, null]
        ^
    push1(8)
    [4, 5, 8, null]
    push1(23)
    [4, 5, 8, 23, null, null, null, null]
               ^
    push2(9)
    [4, 5, 8, 23, null, null, null, 9]
              ^                     ^
    push2


    """
    def __init__(self):
        self.data = [None]
        self.left = -1
        self.right = 1

    def push1(self, x):
        if self._stack_is_full():
            self._extend_stack_size()

        self._push_to_left(x)

    def _stack_is_full(self):
        return self.left == self.right - 1

    def _extend_stack_size(self):
        # [1] r = 0
        # [None, None]
        # rs = 2 - 1
        extended_stack = [None] * (len(self.data) * 2)
        right_shift = len(extended_stack) - len(self.data)
        self._rewrite_stack(extended_stack, right_shift)
        self.right += right_shift
        self.data = extended_stack

    def _rewrite_stack(self, new_stack, right_shift):
        self._rewrite_left_stack(new_stack)
        self._rewrite_right_stack(new_stack, right_shift)

    def _rewrite_left_stack(self, new_stack):
        for i, x in enumerate(self.data[:self.left+1]):
            new_stack[i] = x

    def _rewrite_right_stack(self, new_stack, right_shift):
        for i in range(self.right, len(self.data)):
            new_stack[i + right_shift] = self.data[i]

    def _push_to_left(self, x):
        self.left += 1
        self.data[self.left] = x

    def push2(self, data):
        if self._stack_is_full():
            self._extend_stack_size()

        self._push_to_right(data)

    def _push_to_right(self, x):
        self.right -= 1
        self.data[self.right] = x

    def pop1(self):
        x = self.data[self.left]
        self.data[self.left] = None
        self.left -= 1
        return x

    def pop2(self):
        x = self.data[self.right]
        self.data[self.right] = None
        self.right += 1
        return x


class DoubleStackTestCase(unittest.TestCase):
    def test_stack1(self):
        stack = DoubleStack()
        stack.push1(1)
        self.assertEqual(len(stack.data), 1)
        self.assertEqual(stack.data[0], 1)
        stack.push1(89)
        self.assertEqual(len(stack.data), 2)
        self.assertEqual(stack.data[0], 1)
        self.assertEqual(stack.data[1], 89)
        stack.push1(99)
        self.assertEqual(len(stack.data), 4)
        self.assertEqual(stack.data[0], 1)
        self.assertEqual(stack.data[1], 89)
        self.assertEqual(stack.data[2], 99)
        self.assertEqual(stack.data[3], None)

        self.assertEqual(stack.pop1(), 99)
        self.assertEqual(stack.pop1(), 89)
        self.assertEqual(stack.pop1(), 1)

    def test_stack2(self):
        stack = DoubleStack()
        stack.push2(1)
        self.assertEqual(len(stack.data), 1)
        self.assertEqual(stack.data[0], 1)
        stack.push2(89)
        self.assertEqual(len(stack.data), 2)
        self.assertEqual(stack.data[0], 89)
        self.assertEqual(stack.data[1], 1)
        stack.push2(99)
        self.assertEqual(len(stack.data), 4)
        self.assertEqual(stack.data[1], 99)
        self.assertEqual(stack.data[2], 89)
        self.assertEqual(stack.data[3], 1)
        self.assertEqual(stack.data[0], None)

        self.assertEqual(stack.pop2(), 99)
        self.assertEqual(stack.pop2(), 89)
        self.assertEqual(stack.pop2(), 1)

    def test_both_stacks(self):
        stack = DoubleStack()
        stack.push1(1)
        stack.push2(9)
        self.assertEqual(stack.pop1(), 1)
        self.assertEqual(stack.pop2(), 9)
        stack.push1(2)
        stack.push1(3)
        stack.push1(4)
        stack.push1(5)
        stack.push2(6)
        stack.push2(7)
        stack.push2(8)
        stack.push2(9)
        self.assertEqual(stack.pop1(), 5)
        self.assertEqual(stack.pop1(), 4)
        self.assertEqual(stack.pop1(), 3)
        self.assertEqual(stack.pop1(), 2)

        self.assertEqual(stack.pop2(), 9)
        self.assertEqual(stack.pop2(), 8)
        self.assertEqual(stack.pop2(), 7)
        self.assertEqual(stack.pop2(), 6)



class StackTestCase(unittest.TestCase):
    def test(self):
        stack = Stack()
        self.assertIsNone(stack.peek())
        self.assertIsNone(stack.pop())
        self.assertTrue(stack.is_empty())

        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.pop(), 1)

        self.assertIsNone(stack.peek())
        self.assertIsNone(stack.pop())
        self.assertTrue(stack.is_empty())

        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.pop(), 2)

        self.assertEqual(stack.peek(), 1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.pop(), 1)

        self.assertIsNone(stack.peek())
        self.assertIsNone(stack.pop())
        self.assertTrue(stack.is_empty())


class SpecialStackTestCase(unittest.TestCase):
    def test(self):
        special_stack = SpecialStack()
        special_stack.push(1)
        self.assertEqual(special_stack.get_min(), 1)
        special_stack.push(2)
        self.assertEqual(special_stack.get_min(), 1)
        special_stack.push(0)
        special_stack.push(3)
        self.assertEqual(special_stack.get_min(), 0)
        special_stack.push(3)
        special_stack.push(6)
        special_stack.push(9)
        self.assertEqual(special_stack.get_min(), 0)
        special_stack.pop()
        special_stack.pop()
        special_stack.pop()
        special_stack.pop()
        special_stack.pop()
        self.assertEqual(special_stack.get_min(), 1)

