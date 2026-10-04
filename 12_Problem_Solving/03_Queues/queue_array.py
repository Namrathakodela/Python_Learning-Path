# Queue using Array

from collections import deque


class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"

        return self.queue.popleft()

    def front(self):
        if self.is_empty():
            return "Queue is empty"

        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(list(self.queue))


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue:")
queue.display()

print("Front:", queue.front())
print("Removed:", queue.dequeue())

queue.display()