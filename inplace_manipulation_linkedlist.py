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

algorithm: directly adjusting node pointers to ensure efficient in-place manipulation without
using additional memory, use dummy node to simplify edge cases (i.e. if sublist starts at first
node), link dummy to head, iterate to node before left and mark as previous node, move 

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

'''
naive approach for reverse between function: 2 pointers initialized to head 
in order to track sublist and reverse it 

time O(n ^ 2), space O(1)
'''
def naive_reverse_between(head, left, right):
    if not head or left == right:
        return head 
    
    left_pointer = head 
    for _ in range(left - 1):
        left_pointer = left_pointer.next 
        
    for _ in range((right - left + 1) // 2):
        right_pointer = head 
        for _ in range(right - 1):
            right_pointer = right_pointer.next 
    
        left_pointer.data, right_pointer.data = right_pointer.data, left_pointer.data 
        left_pointer = left_pointer.next 
        right -= 1
    
    return head 

'''
statement: given the head of a singly linked list, reorder the list as if it were 
folded on itself - for example, if the list is represented as follows:

L0 → L1 → L2 → … → Ln-2 → Ln-1 → Ln

this is how you'll reorder it:

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

no need to modify the values in the list's nodes, only the links between nodes need to be changed

algorithm: reorganize list in 3 steps, slow/fast pointers to reach middle node, 
reverse second half of list, each node points to 1 before it, order of second half
flipped, merge 2 halves from heads alternatively linking nodes by adjusting pointers, 
each node in first half points to node in second, each node from second half 
linked to subsequent node in first half 

summary of algorithm:  
    1. find middle node -> choose second if 2 
    2. reverse second half of list 
    3. merge both halves of linked list alternatively 
    
time O(n) where n = number of nodes in list, space O(1)
'''
def reorder_list(head):
    if not head:
        return head
    
    # find middle node, 2 middle nodes -> choose 2nd  
    slow = fast = head
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next  
    
    # reverse second half of linked list 
    previous = None
    current = slow 
    while current:
        current.next, previous, current = previous, current, current.next 
        
    # merge first and second half of linked list 
    first = head
    second = previous
    
    while second.next:
        first.next, first = second, first.next 
        second.next, second = first, second.next 
        
    return head 

'''
naive approach to reverse list: traverse list, 1st start from head using current pointer, 
traverse list and add last node in front of current, move to next node, each node added
current node move ahead, find last occurring nodes n times

time O(n ^ 2), space O(1) 
'''
def naive_reorder_list(head):
    if not head or not head.next:
        return head
    
    current = head 
    
    while current and current.next: 
        # find last node and its previous node 
        previous = None
        last = current
        while last.next:
            previous = last 
            last = last.next 
        
        # move last node to be after current node 
        if previous:
            previous.next = None # disconnect last node from previous position 
            last.next = current.next # point last node to next of current node 
            current.next = last # insert last node after current node 
        
        # move current to next node in reordered list 
        current = last.next 

    return head 

'''
statement: given the linked list and an integer, k, return the head of the linked 
list after swapping the values of the kth node from the beginning and the kth node 
from the end of the linked list.

note: we'll number the nodes of the linked list starting from 1 to n

algorithm: find kth node from start and kth node from end, find 2 nodes using in-place manipulation 
mthod, use 2 pointers to traverse list, swap values 
    - 1 pass: enables swap without determining length, advancing 2 pointers maintaining k gap, both 
      pointers start at head, current moves k, end starts moving from head, front pointer stores current 
      position of current, traversal continued until current reaches end, ensures end points kth node 
      from end, swap nodes pointed by front and end pointers 
    - 3 pass: front/end pointers, 1st pass to find kth from start, 2nd to find length, 3rd to find end
      by taking length - k and iterating to that node 
    - 2 pass: find length and kth node from start in first pass 

time O(n) where n = number of nodes in list, space O(1)
'''
def swap_nodes(head, k):
    # initialize pointer current with head
    current = head 
    # variable count with 0 
    count = 0 
    # front and end pointers used to track kth node from start/end of list 
    front = None
    end = None 
    
    # traverse list using current while incrementing count in each iteration 
    while current:
        count += 1
        
        # if end not null = kth node from beginning foun
        if end is not None:
            # move end pointer to find kth node from end of list 
            end = end.next 
            
        # when count equals k, kth node from start reached, save node as front
        if count == k:
            # set end pointer at head of linked list 
            front = current 
            end = head 
        
        # continue traversing list by moving both end and current forward
        current = current.next # when current @ last node, end @ kth node from list end
    
    # swap values of front and end nodes     
    temp = front.data 
    front.data = end.data
    end.data = temp
    
    return head

'''
statement: given the head of a linked list, the nodes in it are assigned to each group in a sequential manner. The length of these groups follows the sequence of natural numbers. Natural numbers are positive whole numbers denoted by 
(
1
,
2
,
3
,
4...
)
(1,2,3,4...)
.

In other words:

The 
1
s
t
1 
st
 
 node is assigned to the first group.

The 
2
n
d
2 
nd
 
 and 
3
r
d
3 
rd
 
 nodes are assigned to the second group.

The 
4
t
h
4 
th
 
, 
5
t
h
5 
th
 
, and 
6
t
h
6 
th
 
 nodes are assigned to the third group, and so on.

Your task is to reverse the nodes in each group with an even number of nodes and return the head of the modified linked list.

Note: The length of the last group may be less than or equal to 1 + the length of the second to the last group.
'''