from linked_list import LinkedList

def reverse(head):
    if head: # check for empty list     
        # declare pointers for current, previous and next 
        current = head
        previous = None
        nextNode = None
        # traverse list
        while current: 
            # set next to next node
            nextNode = current.next 
            # current next to previous node
            current.next = previous 
            # update previous 
            previous = current
            # update current
            current = nextNode 
        # point head pointer to previous  
        head.next = previous 
    return head