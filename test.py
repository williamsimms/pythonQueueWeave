from logging import warn
import queue
import unittest
from main import weave
from queue import Queue


class WeaveTest(unittest.TestCase):
    def test_queue_has_a_peek_function(self):
        queue = Queue()
        self.assertTrue(callable(queue.peek))

    def weave_is_a_function(self):
        self.assertTrue(callable(weave))

    def test_peek_returns_not_remove_first_value(self):
        queue = Queue()

        queue.enqueue(1)
        queue.enqueue(2)

        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)

    def test_weave_can_combine_two_queues(self):
        queue_one = Queue()
        queue_two = Queue()

        queue_one.enqueue(1)
        queue_one.enqueue(2)
        queue_one.enqueue(3)
        queue_one.enqueue(4)

        queue_two.enqueue('one')
        queue_two.enqueue('two')
        queue_two.enqueue('three')
        queue_two.enqueue('four')

        result = weave(queue_one, queue_two)

        self.assertEqual(result.dequeue(), 1)
        self.assertEqual(result.dequeue(), 'one')
        self.assertEqual(result.dequeue(), 2)
        self.assertEqual(result.dequeue(), 'two')
        self.assertEqual(result.dequeue(), 3)
        self.assertEqual(result.dequeue(), 'three')
        self.assertEqual(result.dequeue(), 4)
        self.assertEqual(result.dequeue(), 'four')
        self.assertIsNone(result.dequeue())


if __name__ == '__main__':
    unittest.main()
