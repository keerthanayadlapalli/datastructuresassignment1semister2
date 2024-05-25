class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  
            self.tail = new_node
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)

current_node = my_list.head
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("None")

        
