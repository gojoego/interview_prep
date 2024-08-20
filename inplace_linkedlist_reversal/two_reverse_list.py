from linked_list import LinkedList
from linked_list import LinkedListNode
from reverse_list import reverse
            
# time O(n), space O(1)
def reverse_between(head, left, right):
    # if list empty or left position same as right, return original list 
    if not head or left == right: 
        return head
    
    # create dummy node to handle edge case when left = 1
    dummy = LinkedListNode(0)
    dummy.next = head 
    previous = dummy 
    
    # move previous to node just before left position 
    for _ in range(left - 1):
        print("previous: ", previous.data)
        previous = previous.next
    
    # current node is node at left position 
    current = previous.next
    
    # reverse portion of list between left and right positions 
    for _ in range(right - left):
        next_node = current.next # assign next node 
        print("next_node: ", next_node.data)
        current.next = next_node.next # update current's next pointer 
        # print("current.next: ", current.next.data)
        next_node.next = previous.next 
        # print("next_node.next: ", next_node.next.data)
        previous.next = next_node
        # print("previous.next: ", previous.next.data)
    
    # return updated head of list 
    return dummy.next 

def traverse_linked_list(head):
    current, nxt = head, None
    while current:
      nxt = current.next
      current = nxt
