import unittest


from .stack import Stack


def insert_at_bottom(stack, item):
    if stack.is_empty():
        stack.push(item)
    else:
        tmp = stack.pop()
        insert_at_bottom(stack, item)
        stack.push(tmp)


def reverse(stack):
    if stack.is_empty():
        return None
    else:
        tmp = stack.pop()
        reverse(stack)
        insert_at_bottom(stack, tmp)


class ReverseTestCase(unittest.TestCase):
    def test(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)

        reverse(stack)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 4)


class InsertAtBottomTestCase(unittest.TestCase):
    def test(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)

        insert_at_bottom(stack, 5)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 5)