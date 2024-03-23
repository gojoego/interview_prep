from linked_list import LinkedList

# The code in "linked_list.py" can be used to create a linked list out of a list. 
# The code in "linked_list_traversal.py" can be used to traverse the linked list.
# The code in "linked_list_reversal.py" can be used to reverse the linked list.

# time O(n), space O(1)
def get_middle_node(head):

    slow, fast = head, head 
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow