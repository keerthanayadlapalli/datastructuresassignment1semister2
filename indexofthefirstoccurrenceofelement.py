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
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def index_of(self, data):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.data == data:
                return index
            current_node = current_node.next
            index += 1
        return -1  

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(3)
my_list.append(3)

print("Original linked list:")
my_list.display()

value_to_find = 3
index = my_list.index_of(value_to_find)
if index != -1:
    print(f"The index of {value_to_find} is:", index)
else:
    print(f"{value_to_find} is not found in the linked list.")