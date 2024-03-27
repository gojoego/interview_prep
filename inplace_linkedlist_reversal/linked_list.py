class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None
    
    # insert_node_at_head method will insert a LinkedListNode at 
    # head of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    
    # create_linked_list method will create the linked list using the
    # given integer array with the help of InsertAthead method. 
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)
    
    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result
        
    def print_list_with_forward_arrow(self):
        temp = self
        while temp:
            print(temp.data, end=" ")  # print node value
            
            temp = temp.next
            if temp:
                print("→", end=" ")
            else:
                # if this is the last node, print null at the end
                print("→ null", end=" ")
    
    def reverse_link_list(head, k):
        previous, current, next_node = None, head, None
        for _ in range(k):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous, current