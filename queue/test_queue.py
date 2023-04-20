import unittest
from queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(len(self.queue), 3)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(len(self.queue), 1)

    def test_peek(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.peek(), 1)
        self.queue.dequeue()
        self.assertEqual(self.queue.peek(), 2)

    def test_str(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(str(self.queue), "1, 2, 3")

    def test_len(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.assertEqual(len(self.queue), 5)
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(len(self.queue), 3)


if __name__ == "__main__":
    unittest.main()
