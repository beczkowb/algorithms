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
