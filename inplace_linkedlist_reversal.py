def reorder_list(head):
    if not head: 
        return head 
    slow = fast = head 
    
    while fast and fast.next: # fast and slow pointers to find middle of list 
        slow = slow.next
        fast = fast.next.next 
    previous, current = None, slow 
    
    while current: # reverse second half of list 
        current.next, previous, current = previous, current, current.next 
    first, second = head, previous
    
    while second.next: # merging lists 
        first.next, first = second, first.next
        second.next, second = first, second.next 
    
    return head

def swap_nodes(head, k):
    # initialize pointer current with head node and count variable w/ 0 
    count = 0 # declare counter variable and initialize to 0 
    front, end = None, None # declare front and end pointer and initialize to None 
    current = head # declare current variable and initialize to head 
    
    while current: # traverse list using current pointer and increment count every step 
        count += 1 # increment count every step 
        if end != None: # 
            end = end.next # move end pointer along with current 
        if count == k: # when count equal to k -> kth node from start reached 
            front = current # set front pointer to current node 
            end = head # set end pointer to head in order to make end node exactly k nodes behind current 
        current = current.next # when current at end of list, end pointer will be pointing at kth node from end 
    
    swap(front, end) # call swap function to perform actual swap 
    return head 

def reverse_even_length_groups(head):
    previous = head # declare variable to point to previous node and initialize to head of list 
    group_length = 2 # declare varible to track current group length and initialize to 2 since 1 cannot be reversed/odd 
    while previous.next: # iterate nodes of list 
        node = previous # declare node variable and initialize to previous 
        num_nodes = 0 # number of nodes in current group 
        for i in range(group_length): # 
            if not node.next:
                break
            num_nodes += 1 # count nodes
            node = node.next 
        if num_nodes % 2: # for odd length groups, skip by pointing previous to current node to 
            previous = node
        else: # even node number
            reverse = node.next # points to next node of current group  
            current = previous.next # points to first node of current group 
            for j in range(num_nodes): # looping over group to reverse nodes 
                current_next = current.next  # reference to next node 
                current.next = reverse # reverses pointer
                reverse = current # move reverse to current node b/c next node in reversed group 
                current = current_next # continuing reversal process
            previous_next = previous.next 
            previous.next = node # update next of previous to last node
            previous = previous_next # updating previous to first node of current group 
        group_length += 1
    return head 

def swap_pairs(head):
    dummy = LinkedListNode(0) # dummy node handles edge cases like empty list or single node list 
    dummy.next = head # helps maintain consistent starting point for list 

    current = dummy # pointer used to traverse list - starts at dummy node
    
    while current.next and current.next.next: # loop through list while there are 2+ nodes to swap 
        first = current.next # first node of pair to be swapped 
        second = current.next.next # second node of pair to be swapped 
        
        first.next = second.next # swap nodes by reassigning next pointers, first node points to node after second
        second.next = first # make second node point to first node 
        current.next = second # connect previous part of list to second node, which is now first node of swapped 
         
        current = first # move current to end of swapped pair to prepare for next swap
    # return new head of list, which is next of dummy node 
    return dummy.next
def main():
    input = [
        [1, 2, 3, 4],
        [10, 11, 12, 13, 14],
        [15],
        [16, 17]
    ]

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(
            i+1, ".\tIf we reverse the even length groups of the linked list: ", end='\n\t')
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\n\tWe will get: ", end='\n\t')
        print_list_with_forward_arrow(
            reverse_even_length_groups(input_linked_list.head))
        print("\n")
        print("-" * 100)


if __name__ == '__main__':
    main()

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Template for the linked list
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
        
def print_list_with_forward_arrow(linked_list_node):
    temp = linked_list_node
    while temp:
        print(temp.data, end=" ")  # print node value

        temp = temp.next
        if temp:
            print("→", end=" ")
        else:
            # if this is the last node, print null at the end
            print("→ null", end=" ")
            
def swap(node1, node2):
    temp = node1.data
    node1.data = node2.data
    node2.data = temp