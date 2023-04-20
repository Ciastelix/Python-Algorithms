import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(len(self.stack), 3)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(len(self.stack), 1)

    def test_str(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(str(self.stack), "3\n2\n1")

    def test_len(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.assertEqual(len(self.stack), 5)
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(len(self.stack), 3)


if __name__ == "__main__":
    unittest.main()
