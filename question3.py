class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def size(self):
        size = 0
        current_node = self.head
        while current_node:
            size += 1
            current_node = current_node.next
        return size

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
print("Size of the linked list:", my_list.size())  # Output: 3
