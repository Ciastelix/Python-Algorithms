import unittest
from linkedlist import LinkedList
from node import Node


class TestLinkedList(unittest.TestCase):
    def test_push(self):
        linked_list = LinkedList()
        linked_list.push(1)
        linked_list.push(2)
        linked_list.push(3)
        self.assertEqual(str(linked_list), "3 -> 2 -> 1")

    def test_append(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        self.assertEqual(str(linked_list), "1 -> 2 -> 3")

    def test_node(self):
        linked_list = LinkedList()
        linked_list.push(1)
        linked_list.push(2)
        linked_list.push(3)
        self.assertEqual(linked_list.node(0).value, 3)
        self.assertEqual(linked_list.node(1).value, 2)
        self.assertEqual(linked_list.node(2).value, 1)

    def test_insert(self):
        linked_list = LinkedList()
        linked_list.push(1)
        linked_list.push(2)
        linked_list.push(3)
        linked_list.insert(4, 1)
        self.assertEqual(str(linked_list), "3 -> 4 -> 2 -> 1")

    def test_pop(self):
        linked_list = LinkedList()
        linked_list.push(1)
        linked_list.push(2)
        linked_list.push(3)
        value = linked_list.pop()
        self.assertEqual(value, 3)
        self.assertEqual(str(linked_list), "2 -> 1")

    def test_remove_last(self):
        linked_list = LinkedList()
        linked_list.push(1)
        linked_list.push(2)
        linked_list.push(3)
        value = linked_list.remove_last()
        self.assertEqual(value, 1)
        self.assertEqual(str(linked_list), "3 -> 2")

    def test_remove(self):
        linked_list = LinkedList()
        linked_list.push(1)
        linked_list.push(2)
        linked_list.push(3)
        value = linked_list.remove(Node(2))
        self.assertEqual(value, 1)
        self.assertEqual(str(linked_list), "3 -> 2")

    def test_length(self):
        linked_list = LinkedList()
        linked_list.push(1)
        linked_list.push(2)
        linked_list.push(3)
        self.assertEqual(len(linked_list), 3)

    def test_str(self):
        linked_list = LinkedList()
        linked_list.push(1)
        linked_list.push(2)
        linked_list.push(3)
        self.assertEqual(str(linked_list), "3 -> 2 -> 1")


if __name__ == "__main__":
    unittest.main()
