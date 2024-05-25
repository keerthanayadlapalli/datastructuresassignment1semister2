class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

# Example usage:
my_list = LinkedList()
print(my_list.is_empty())  # Output: True

my_list.append(1)
print(my_list.is_empty())  # Output: False
