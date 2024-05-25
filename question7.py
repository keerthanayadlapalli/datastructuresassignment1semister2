class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def prepend(self,data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node   
            
my_list = LinkedList()
my_list.prepend(3)
my_list.prepend(2)
my_list.prepend(1)

# Print the linked list to verify the elements have been prepended
current_node = my_list.head
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("None")