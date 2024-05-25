class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous
my_list = LinkedList()
my_list.head = Node(1)
my_list.head.next = Node(2)
my_list.head.next.next = Node(3)

print("Original linked list:")
current_node = my_list.head
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("None")

my_list.reverse()

print("Reversed linked list:")
current_node = my_list.head
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("None")

my_list.reverse()
    
        