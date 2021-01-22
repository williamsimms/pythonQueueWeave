
class Queue:

    def __init__(self):
        self.data = []

    def __str__(self):
        return str(self.data)

    def enqueue(self, data):
        self.data.insert(0, data)

    def dequeue(self):
        return self.data.pop()


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(5)
    queue.enqueue(3)
    print(queue)
    queue.dequeue()
    print(queue)