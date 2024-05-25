class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_index(self, index, value):
        new_node = Node(value)
        
        # If inserting at the head (index 0)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse the list to find the position before the insertion point
        trav = self.head
        current_index = 0
        
        while trav is not None and current_index < index - 1:
            trav = trav.next
            current_index += 1
        
        # If trav is None, it means the index is out of bounds
        if trav is None:
            raise IndexError("Index out of bounds")
        
        # Insert the new node
        new_node.next = trav.next
        trav.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
        

abc=LinkedList()
abc.insert_at_index(0,1)
abc.insert_at_index(1,1)
abc.insert_at_index(2,1)
abc.insert_at_index(3,1)
abc.insert_at_index(4,1)
abc.insert_at_index(5,1)
abc.insert_at_index(3,8)

abc.display()