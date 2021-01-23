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
    queue: Queue = Queue()

    while queue_one.peek() or queue_two.peek():
        if queue_one.peek():
            queue.enqueue(queue_one.dequeue())

        if queue_two.peek():
            queue.enqueue(queue_two.dequeue())

    return queue


if __name__ == '__main__':
    queueone: Queue = Queue()
    queueone.enqueue(3)
    queueone.enqueue(5)
    queueone.enqueue(7)

    queuetwo: Queue = Queue()
    queuetwo.enqueue(11)
    queuetwo.enqueue(22)
    queuetwo.enqueue(112)
    queuetwo.enqueue(117)

    print(weave(queueone, queuetwo))
