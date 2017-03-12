import unittest


class LinkedList:
    def __init__(self):
        self.head = None

    def __getitem__(self, key):
        current_node = self.head
        i = 0

        while current_node is not None:
            if i == key:
                return current_node.data

            current_node = current_node.next_node
            i += 1

        raise IndexError('index out of bound')

    def __len__(self):
        current_node = self.head
        i = 0
        while current_node is not None:
            i += 1
            current_node = current_node.next_node

        return i

    def append(self, data):
        new_node = Node(data=data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node is not None:
                current_node = current_node.next_node

            current_node.next_node = new_node


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedListTestCase(unittest.TestCase):
    def test_creating_and_adding_one_element(self):
        l = LinkedList()
        l.append(1)
        self.assertEqual(l[0], 1)

    def test_adding_few_element(self):
        l = LinkedList()
        l.append(1)
        l.append(2)
        l.append(3)
        self.assertEqual(l[0], 1)
        self.assertEqual(l[1], 2)
        self.assertEqual(l[2], 3)

    def test_list_len(self):
        l = LinkedList()
        l.append(99)
        l.append(20)
        l.append(8)
        self.assertEqual(len(l), 3)

        l2 = LinkedList()
        self.assertEqual(len(l2), 0)

        l3 = LinkedList()
        l3.append(48)
        self.assertEqual(len(l3), 1)

        l4 = LinkedList()
        l4.append(48)
        l4.append(48)
        self.assertEqual(len(l4), 2)

if __name__ == '__main__':
    unittest.main()