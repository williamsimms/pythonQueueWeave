import queue
import unittest
from main import weave
from queue import Queue


class WeaveTest(unittest.TestCase):
    def test_queue_has_a_peek_function(self):
        queue = Queue()
        self.assertTrue(callable(callable(queue.peek)))
