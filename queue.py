
import queue


class Queue:

    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def enqueue(self, data):
        self.data.insert(0, data)

    def dequeue(self):
        return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            return None

        length = len(self.data)

        return self.data[length - 1]


if __name__ == '__main__':
    queue = Queue()
