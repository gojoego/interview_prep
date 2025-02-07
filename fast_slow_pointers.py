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

time O(logn), space O(1) where n = number of nodes in linked list 
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
statement: check whether or not a linked list contains a cycle - if a cycle exists, 
return TRUE - otherwise, return FALSE, the cycle means that at least one node can be 
reached again by traversing the next pointer

algorithm: use fast/slow pointers to find cycle without requiring multiple traversals or 
additional data structures, no cycle -> fast pointer will reach end 

time O(logn), space O(1) where n = number of nodes in linked list 
'''
def detect_cycle(head):
    # edge case for empty lists 
    if head == None:
        return False 
    
    # initialize both slow and fast pointers to linked list head 
    slow = fast = head 
    
    # move slow 1, fast 2 nodes 
    while fast and fast.next: 

        slow = slow.next 
        fast = fast.next.next 

        # if both pointers reference same node, return True
        if fast == slow: 
            return True
        
    # if fast pointer reaches end of list, return False 
    return False 

def naive_cycle_detector(head):
    visited = set()
    current = head 
    
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next 
    return False 

'''
statement: given the head of a singly linked list, return the middle node of the linked list, 
if the number of nodes in the linked list is even, there will be two middle nodes, so return 
the second one

algorithm: fast/slow pointers used to find midpoint by leveraging speeds, both point at head
initially, slow moves 1, fast 2, when fast reaches Null or end -> slow at middle for odd numbered
and at second middle node for even length lists  

time O(logn), space O(1) where n = number of nodes in linked list 
'''
def get_middle_node(head):
    # create slow and fast pointers initialized to head of linked list 
    slow = fast = head 
    
    # traverse list, moving slow pointer 1 step, fast 2 steps 
    while fast and fast.next: 
        slow = slow.next 
        # when fast reaches end or Null -> slow pointing at middle of list 
        fast = fast.next.next 

    # return node that slow pointer points to 
    return slow 

# time/space O(n), use external array and return element at array.length/2 as middle node
def naive_middle_node(head):
    elements = []
    
    current = head 
    
    while current:
        elements.append(current.data)
        current = current.next 
    
    middle = len(elements) // 2
    
    return elements[middle]

'''
statement: we are given a circular array of non-zero integers, nums, where each integer represents 
the number of steps to be taken either forward or backward from its current index, positive values 
indicate forward movement, while negative values imply backward movement, when reaching either end 
of the array, the traversal wraps around to the opposite end

the input array may contain a cycle, which is a sequence of indexes characterized by the following:

    - the sequence starts and ends at the same index
    - the length of the sequence is at least two
    - the loop must be in a single direction, forward or backward
    
note: a cycle in the array does not have to originate at the beginning, it may begin from any point 
in the array

your task is to determine if nums has a cycle, return TRUE if there is a cycle, otherwise return FALSE

algorithm: initialize 2 pointers for each element of array with slow 1 step and fast 2 steps, position 
determined by current value, if movement results in pointer pointing to value with different sign or 
pointing to same index previously pointed to or fast pointer reached end and no cycle detected -> move 
to next element, both pointers eventually catch up if cycle

time O(n^2), time O(1)
'''
def circular_array_loop(nums):  
    size = len(nums)
    
    # traverse entire nums using slow/fast pointers, starting from index 0 
    for i in range(size):
        # set slow/fast pointers at same index value  
        slow = fast = i 
        
        # set true in forward if element positive, set False otherwise 
        forward = nums[i] > 0
        
        # if loop direction changes or taking a step returns to same location, continue to next element
        while True:
            # move slow pointer 1 step forward/backward
            slow = next_step(slow, nums[slow], size)
            
            # if cycle not possible, break loop and start from next element
            if is_not_cycle(nums, forward, slow):
                break 
            
            # move fast 2x forward/backward 
            fast = next_step(fast, nums[fast], size) # first move 
            
            # if cycle not possible, break loop and start from next element
            if is_not_cycle(nums, forward, fast):
                break
            
            fast = next_step(fast, nums[fast], size) # second move 
            
            # if cycle not possible, break loop and start from next element
            if is_not_cycle(nums, forward, fast):
                break
            
            # if fast/slow pointers meet -> loop found -> return True 
            if slow == fast:
                return True

    # return False if no loop encountered after traversing whole array     
    return False

# function to calculate next step 
def next_step(pointer, value, size):
    result = (pointer + value) % size
    
    if result < 0:
        result += size
        
    return result 

# function to detect if a cycle does not exist 
def is_not_cycle(nums, previous_direction, pointer):
    # set current direction to True if current element is positive, set False otherwise 
    current_direction = nums[pointer] >= 0 
    
    # if current & previous direction differ or moving pointer takes back it to same value...
    if (previous_direction != current_direction) or (nums[pointer] % len(nums) == 0):
        return True # ... cycle is not possible, return True,
    else: # otherwise return False 
        return False

'''
naive algorithm: iterate through each element of array, check for cycles in both directions with 
current element, use another array to track visited elements, return True for if cycle found, 
move to next iteration for direction change, inner loop for each element

time O(n^2), space O(n)
'''
def naive_circular_array_loop(nums):
    size = len(nums)
    
    for i in range(size):
        visited = set() # keep track of visited indices to detect cycle 
        current = i 
        direction = nums[i] > 0 # determine direction - forward or backward 
        
        while current not in visited:
            visited.add(current)
            next_index = (current + nums[current]) % size 
            
            if next_index < 0:
                next_index += size # handle negative wrap-around 
                
            # if direction changes or next step lands on same element, stop checking 
            if (nums[next_index] > 0) != direction or next_index == current:
                break 
            
            current = next_index # move to next step 
            
            # if we return to starting point, cycle detected 
            if current == i:
                return True
            
    return False

'''
statement: given an array of positive numbers, nums, such that the values lie in the range [1,n], 
inclusive, and that there are n + 1 numbers in the array, find and return the duplicate number 
present in nums, there is only one repeated number in nums, but it may appear more than once in the 
array

note: you cannot modify the given array nums, you have to solve the problem using only constant 
extra space

algorithm: 

1.  ID cycle to confirm duplicate existence 
    - slow pointer moves 1, fast 2 until meeting 
    - intersection point of 2 pointers generally not entry point of cycle 

2.  locate entry point of cycle -> represents duplicate number 
    - fast pointer moves at same pace as slow 
    - slow starts at 0th, fast at intersection 
    - pointers meet at ending point 
    - common ending position will be entry point of cycle  
    
time O(logn), space O(1) where n = length of array 
'''
def find_duplicate(nums):
    # traverse in nums using fast and slow pointers 
    fast = slow = nums[0]
    
    # part 1 - traverse array until intersection point found 
    while True: # move pointers until they meet 
        # move slow pointer using nums[slow] flow 
        slow = nums[slow]
        
        # move fast pointer 2x as fast as slow point using nums[nums[fast]] flow 
        fast = nums[nums[fast]]
        
        # break loop when slow pointer becomes equal to fast -> intersection found 
        if slow == fast:
            break 
    
    # part 2 - after pointers meet, traverse nums again 
    slow = nums[0] # reset slow pointer to start of array
    
    # move slow from start of nums and fast from meeting point at same speed until meeting again 
    while fast != slow:
        # move slow pointer using nums[slow] flow 
        slow = nums[slow]   
            
        # move fast pointer same as slow point using nums[fast] flow 
        fast = nums[fast]
        
    # return fast pointer that points to duplicate number of array 
    return fast

'''
statement: given the head of a linked list, your task is to check whether the linked list is a 
palindrome or not, return TRUE if the linked list is a palindrome; otherwise, return FALSE

note: the input linked list prior to the checking process should be identical to the list after 
the checking process has been completed

algorithm: find midpoint of given list, reverse second half and compare halves for symmetry; if
halves match -> palindrome, reversing half allows use of next pointers for comparison 

time O(logn), space O(1) where n = length of array 
'''
def palindrome(head):
    # edge cases - single node or empty list = palindrome  
    if not head or not head.next: 
        return True
    
    # initialize fast and slow pointers to head of list 
    fast = slow = head 
    
    # traverse with slow pointer moving 1 node at a time, fast pointer 2 nodes 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        
    # slow pointer should now be pointing at middle of list - reverse 2nd half 
    revert_data = reverse_linked_list(slow)
    
    # compare first half of list with reversed second half 
    check = compare_two_halves(head, revert_data)
    
    # re-reverse second half of list to restore original linked list
    reverse_linked_list(revert_data)
    
    # if both halves of list match -> palindrome, return True, otherwise return False   
    if check:
        return True
    return False

def compare_two_halves(first_half, second_half):
    # compare corresponding nodes of first and second halves of linked list 
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        else:
            first_half = first_half.next 
            second_half = second_half.next 
    return True

def reverse_linked_list(slow_pointer):
    previous = None
    next = None
    current = slow_pointer
    while current is not None:
        next = current.next 
        current.next = previous
        previous = current
        current = next 
    return previous

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
    return max_sum

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