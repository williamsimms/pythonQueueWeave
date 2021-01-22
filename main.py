# --- Directions
# Implement the 'weave' function.  Weave
# receives two queues as arguments and combines the
# contents of each into a new, third queue.
# The third queue should contain the *alterating* content
# of the two queues.  The function should handle
# queues of different lengths without inserting
# 'undefined' into the new one.
# *Do not* access the array inside of any queue, only  use the 'add', 'remove', and 'peek' functions.
# --- Example
#    const queueOne = new Queue();
#    queueOne.add(1);
#    queueOne.add(2);
#    const queueTwo = new Queue();
#    queueTwo.add('Hi');
#    queueTwo.add('There');
#    const q = weave(queueOne, queueTwo);
#    q.remove() # 1
#    q.remove() # 'Hi'
#    q.remove() # 2
#    q.remove() # 'There'


from queue import Queue


def weave(queue_one: Queue, queue_two: Queue):
    queue = Queue()

    while queue_one.peek() or queue_two.peek():
        queue_one.peek() and queue.enqueue(queue_one.dequeue())
        queue_two.peek() and queue.enqueue(queue_two.dequeue())


if __name__ == '__main__':
    queue_one: Queue = Queue()
    queue_one.enqueue(3)
    queue_one.enqueue(5)
    queue_one.enqueue(7)

    queue_two: Queue = Queue()
    queue_two.enqueue(3)
    queue_two.enqueue(3)
    queue_two.enqueue(3)

    weave(queue_one, queue_two)
