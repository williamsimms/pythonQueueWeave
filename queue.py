
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
        return self.data[len(self.data) - 1]
