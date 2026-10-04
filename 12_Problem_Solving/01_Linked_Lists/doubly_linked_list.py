# Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node
        new_node.previous = current

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is not None:
            new_node.next = self.head
            self.head.previous = new_node

        self.head = new_node

    def delete(self, value):
        current = self.head

        while current:
            if current.data == value:

                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.previous = current.previous

                return

            current = current.next

    def display_forward(self):
        current = self.head

        while current:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")


linked_list = DoublyLinkedList()

linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.insert_at_beginning(5)

print("Doubly Linked List:")
linked_list.display_forward()

linked_list.delete(20)

print("After deletion:")
linked_list.display_forward()