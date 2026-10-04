# Queue using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.front_node = None
        self.rear_node = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear_node is None:
            self.front_node = new_node
            self.rear_node = new_node
            return

        self.rear_node.next = new_node
        self.rear_node = new_node

    def dequeue(self):
        if self.front_node is None:
            return "Queue is empty"

        value = self.front_node.data

        self.front_node = self.front_node.next

        if self.front_node is None:
            self.rear_node = None

        return value

    def front(self):
        if self.front_node is None:
            return "Queue is empty"

        return self.front_node.data


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front:", queue.front())
print("Removed:", queue.dequeue())
print("Front:", queue.front())