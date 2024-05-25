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

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

def merge(l1, l2):
    if l1.head is None:
        return l2
    if l2.head is None:
        return l1

    merged_list = LinkedList()
    current_node = l1.head
    while current_node:
        merged_list.append(current_node.data)
        current_node = current_node.next

    current_node = l2.head
    while current_node:
        merged_list.append(current_node.data)
        current_node = current_node.next

    return merged_list

list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(4)

list2 = LinkedList()
list2.append(2)
list2.append(5)
list2.append(6)

merged_list = merge(list1, list2)
merged_list.display()
