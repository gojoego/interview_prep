'''
fast/slow pointers 
-uses 2 pointers to traverse iterable data structure at different speeds to 
ID patterns, detect cycles, or find specific elements 
-speeds adjusted according to problem statement 
-often used to determine specific pattern or structure in data 
-pointers start at same location and move at different speeds 
-slow pointer usually moves by factor of one, fast by two 
-allows detection of patterns or properties within data structure (like cycles & intersections)
-for cycles, pointers will meet eventually 

examples
1. middle of linked list 
2. detect cycle in array 
3. identify if repeatedly computing sum of squares of digits of number 19 results in 1 

does your problem match this pattern? yes, if...
-linear data structure 
-cycle or intersection detection
-find starting element at second quantile 

real-world problems
-symlink verification
-compiling object-oriented program 

'''

class LinkedListNode: 
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_node_at_head(self, node):
        if self.head: 
            node.next = self.head
            self.head = node
        else:
            self.head = node 
    
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)
    
    def get_length(self, head):
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next 
        return length
    
    def get_node(self, head, position):
        if position != -1:
            p = 0
            pointer = head 
            while p < pointer:
                pointer = pointer.next 
                p += 1 
            return pointer
    
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next 
            if temp: 
                result += ", "
        result += ""
    
'''
statement: write an algorithm to determine if a number n is a happy number, use the 
following process to check if a given number is a happy number:

- starting with the given number n, replace the number with the sum of the squares 
of its digits
- repeat the process until:
    - the number equals 1, which will depict that the given number n is a happy number
    - the number enters a cycle, which will depict that the given number n is not a 
      happy number
- return TRUE if n is a happy number, and FALSE if not

algorithm: advance 2 pointers through sequence at 2 different speeds, slow at 1 step, 
fast at 2 steps, happy numbers eventually reach 1, unhappy will cycle 

time O(logn), space O(1)
'''
def is_happy_number(n):
    # set up 2 pointers
    slow = n # slow pointer @ input number
    fast = sum_of_squared_digits(n) # fast pointer @ sum of squared digits of input number
    
    # start loop until fast reaches 1 and both pointers meet indicating cycle 
    while fast != 1 and slow != fast:
        # update slow by adding squares of its digits 
        slow = sum_of_squared_digits(slow)
        # update fast by adding squares of its digits twice 
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))      
    
    # return boolean that evaluates if fast pointer equals 1 
    return fast == 1
 
def sum_of_squared_digits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit ** 2
    return total_sum

def naive_happy(n):
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum_of_squared_digits(n)
    
    return n == 1

'''
statement: Check whether or not a linked list contains a cycle. If a cycle exists, return TRUE. Otherwise, return FALSE. The cycle means that at least one node can be reached again by traversing the next pointer.
'''


'''
statement: in a linked list of even length n, the node at position i (0-based indexing) 
is considered the twin of the node at position (n - 1 - i) for all 0 ≤ i < n/2, for 
example, if n = 4, node 0 and node 3 are twins, and node 1 and node 2 are twins, these 
pairs are the only twins in a linked list of size 4

twin sum: sum of a node's value and its twin's value

given the head of a linked list with an even number of nodes, 
return the maximum twin sum of the linked list

algorithm: reverse second half of list and sum corresponding values from both halves, 
utilize fast and slow pointers to find middle

time O(n) where n = length of input linked list, space O(1)
'''

def twin_sum(head):
    # initialize fast and slow pointers at head of linked list 
    slow = head
    fast = head 
    
    # find middle node of linked list using fast and slow pointers 
    while fast and fast.next: 
        # move slow pointer 1 step forward 
        slow = slow.next 
        # move fast pointer 2 steps forward 
        fast = fast.next.next 
        
    # set current at middle node (slow) to reverse second half of linked list 
    current = slow 
    previous = None
    
    # using middle node, reverse second half of linked list 
    while current: # iterate through list until current reaches NULL 
        # save next of current for later use 
        temp = current.next 
        current.next = previous
        previous = current
        current = temp
        
    # initialize max_sum with 0 to track max twin sum
    max_sum = 0
    
    # initialize current at head, previous already pointing at head of reversed second half 
    current = head 
    
    # iterate through list until previous reaches NULL 
    while previous:        
        # using current and previous, calculate twin sums by adding values of nodes from start 
        # of list and reversed second half while updating max_sum if greater twin sum found 
        max_sum = max(max_sum, current.data + previous.data)
        
        # move both previous and current pointers forward 
        previous = previous.next 
        current = current.next 
    
    # return max_sum as max twin sum of given linked list 
    return

'''
statement: given a circular linked list, list, of positive integers, your task is to split it into 
two circular linked lists, first circular linked list should contain the first half of the nodes 
(exactly ⌈list.length / 2⌉ nodes), in the same order they appeared in the original list, while the 
second circular linked list should include the remaining nodes in the same order

return an array, answer, of length 2, where:
    answer[0] is the circular linked list representing the first half
    answer[1] is the circular linked list representing the second half

note: a circular linked list is a standard linked list where the last node points back to the first node

algorithm: fast and slow pointers to find middle and split in single 

time O(n) where n = total number of nodes in circular linked list, space O(1)
'''

def split_circular_linked_list(head):
    # initialize 2 pointers at start of circular linked list 
    fast = head
    slow = head 
    
    # use 2 pointers to traverse circular linked list, 1 moves 1 step, other 2 
    while fast.next != head and fast.next.next != head: # iterate until head, ensures slow at midpoint 
        slow = slow.next 
        fast = fast.next.next 
    
    # 2 pointers to split list 
    first = head # start of first half 
    second = slow.next # start of second half 
    
    # link midpoint back to start of first half, maintaining circular nature of first half 
    slow.next = first
    
    # find ending node of second half and connect it back to its starting point of second half to remain circular 
    fast = second
    
    while fast.next != head:
        fast = fast.next 
    
    fast.next = second
    
    return [first, second] 