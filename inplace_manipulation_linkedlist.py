'''
in-place manipulation of a linked list
- pattern that allows modification of a linked list without using additional memory 
- in-place: algorithm that processes or modifies data structure using only existing memory space,
  without requiring additional memory proportional to input size 
- best suited for problems where we need to modify linked list structure 
- time O(n), space O(1)

examples
1. reverse second half of linked list 
2. rotate linked list clockwise k times 
3. given linkted list, bring all nodes with negative values to start of list 
4. sort a given linked list 
5. given a linked list of length 10, reverse nodes from position 3 to 7

does your problem match this pattern? yes, if...
- linked list restructuring 
- in-place modification

real-world problems
- file system management
- memory management 

'''

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    # insert a LinkedListNode at head of a linked list
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
    
    # create the linked list using the given integer array with the help of InsertAthead method 
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)
    
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

'''
statement: given head of singly linked list, reverse linked list and return updated head

algorithm: reverses by traversing list from head to tail while systematically reversing
direction of pointers between successive nodes, point next pointer to previous node for each
node, store next node in temp pointer, head pointer to last node

time O(n) where n = number of nodes in linked list, space O(1)
'''
def reverse(head):
    # initialize previous and next pointers to None  
    previous = None
    next = None
    # set current pointer to head node 
    current = head 
    
    # traverse linked list until current pointer reaches end of list 
    while current is not None: # while current pointer is not None loop
        # set next pointer to next node in list 
        next = current.next 
        # reverse current node's pointer to point to previous node
        current.next = previous
        
        # update previous and current pointers 
        previous = current
        current = next
    
    # after loop, previous pointer will point to last node of original list, set head pointer to previous
    head = previous
    
    return head

'''
naive approach to reversing linked list: create new list by traversing original list in reverse 
order, copy nodes into another data structure

time and space O(n) where n = length of original list 

possible memory issues if list is very large 
'''
def naive_reverse(head):
    if not head or not head.next:
        return head
    
    stack = []
    current = head 

    # push all nodes onto stack 
    while current:
        stack.append(current)
        current = current.next
    
    # pop nodes to reconstruct reversed list 
    new_head = stack.pop()
    current = new_head
    
    while stack:
        current.next = stack.pop()
        current = current.next 
    
    current.next = None
    
    return new_head

'''
statement: the task is to reverse the nodes in groups of k in a given linked list, where k 
is a positive integer, and at most the length of the linked list - if any remaining nodes 
are not part of a group of k, they should remain in their original order

it is not allowed to change the values of the nodes in the linked list, 
only the order of the nodes can be modified

note: use only O(1) extra memory space

algorithm: each k group is a mini-linjked list for in-place reversal,
ID contiguous groups of exactly k nodes and reverse nodes within group in place,
reattach reversed group segment back to body of list 

time O(n) where n = number of nodes, space O(1)
'''

def reverse_k_groups(head, k):
    # pointer to traverse k nodes in linked list 
    dummy = LinkedListNode(0)
    dummy.next = head 
    pointer = dummy
    
    while pointer != None:
        tracker = pointer
        
        # if pointer successfully traverses group of k nodes, reverse this group
        for i in range(k):
            if tracker == None:
                break
            tracker = tracker.next 
            
        if tracker == None:
            break 
        
        previous, current = reverse_linked_list(pointer.next, k)
        
        # reconnect reversed group of k nodes with rest of linked list
        last_node_reversed_group = pointer.next
        last_node_reversed_group.next = current
        pointer.next = previous
        pointer = last_node_reversed_group

    return dummy.next 

'''
naive approach to reversing groups of k: use another data structure to reverse nodes
and create new linked list with reversed nodes 

time O(n) where n = length of list, space O(n + k) where k = length of stack 
'''
def k_groups_reverse_naive(head, k):
    if not head or k <= 1:
        return head 
    
    dummy = LinkedListNode(0)
    new_head = dummy
    stack = []
    pointer = head 
    
    # iterate linked list 
    while pointer:
        count = 0 
        temp = pointer
        
        # push k group of nodes onto stack 
        while temp and count < k:
            stack.append(temp)
            temp = temp.next 
            count += 1 
        
        if count == k:
            while stack:
                new_head.next = stack.pop()
                new_head = new_head.next 
        else:
            while stack:
                new_head.next = stack.pop(0)
                new_head = new_head.next 
        
        pointer = temp
    
    new_head.next = None
    return dummy.next 

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

def reverse_linked_list(head, k):
	previous, current, next = None, head, None
	for _ in range(k):
		# temporarily store the next node
		next = current.next
		# reverse the current node
		current.next = previous
		# before we move to the next node, point previous to the
        # current node
		previous = current
		# move to the next node 
		current = next
	return previous, current         

'''
statement: given a singly linked list with n nodes and two positions, left and right, the 
objective is to reverse the nodes of the list from left to right, return the modified list

time O(n) where n = number of nodes in list, space O(1)
'''
def reverse_between(head, left, right):
    # if list empty or left position or left position same as right, return original list 
    if not head or left == right:
        return head 
    
    # create dummy node to handle edge case when left is 1 
    dummy = LinkedListNode(0)
    dummy.next = head 
    previous = dummy
    
    # move previous to node just before left position 
    for _ in range(left - 1):
        previous = previous.next 
    
    # current node is node at left position 
    current = previous.next 
    
    # reverse portion of linked list between left and right positions 
    for _ in range(right - left):
        next_node = current.next 
        current.next = next_node.next 
        next_node.next = previous.next 
        previous.next = next_node
    
    # return modified list / updated head of linked list 
    return dummy.next 

# Driver Code
def main():
    input_list = [
        [1, 2, 3, 4, 5, 6, 7],
        [6, 9, 3, 10, 7, 4, 6],
        [6, 9, 3, 4],
        [6, 2, 3, 6, 9],
        [6, 2]
    ]
    left = [1, 3, 2, 1, 1]
    right = [5, 6, 4, 3, 2]

    for i in range(len(input_list)):

        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input_list[i])

        print(i + 1, ".\tOriginal linked list: ", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tleft:", left[i], ", right:", right[i])

        if left[i] <= 0:
            print("\n\tThe expected 'left' and 'right' to have \
            value from 1 to length of the linked list only.")
        else:
            result = reverse_between(input_linked_list.head, left[i], right[i])
            print("\n\tReversed linked list: ", end="")
            print_list_with_forward_arrow(result)
        print("\n", "-"*100, sep="")


if __name__ == '__main__':
    main()