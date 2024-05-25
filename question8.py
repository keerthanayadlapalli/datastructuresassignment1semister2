class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

def interlink(l1, l2):
    if l1 is None:
        return l2  
    if l2 is None:
        return l1 
    
    ans = l1  
    while l1 is not None and l2 is not None:
        temp1 = l1.next  
        temp2 = l2.next  
        
        l1.next = l2  
        l2.next = temp1  
        
        l1 = temp1  
        l2 = temp2  
    
    return ans  
list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)
list2.next.next = Node(8)


merged_head = interlink(list1, list2)

current_node = merged_head
while current_node:
    print(current_node.data, end=" -> ")
    current_node = current_node.next
print("None")
