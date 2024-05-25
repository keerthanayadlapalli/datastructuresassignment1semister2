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

    def delete_at_index(self, index):
        if index < 0 or index >= self.length():
            raise IndexError("Index out of bounds")

        if index == 0:
            self.head = self.head.next
            return

        trav = self.head
        current_index = 0
        while trav is not None and current_index < index - 1:
            trav = trav.next
            current_index += 1

        if trav.next is None:
            raise IndexError("Index out of bounds")


        trav.next = trav.next.next

    def length(self):
        length = 0
        trav = self.head
        while trav is not None:
            length += 1
            trav = trav.next
        return length

    def display(self):
        if self.head is None:
            print("None")
            return

        trav = self.head
        while trav:
            print(trav.value, end=" -> ")
            trav = trav.next
        print("None")


cde = LinkedList()
cde.append(1)
cde.append(2)
cde.append(3)
cde.append(4)

print("Original Linked List:")
cde.display()

cde.delete_at_index(3)  
cde.delete_at_index(2) 
cde.delete_at_index(1) 
cde.delete_at_index(0)

print("Linked List after deletions:")
cde.display()
