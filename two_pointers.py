'''

two pointers
-traverse or manipulate sequential data structures like arrays and linked lists 
-2 pointers that traverse data structure in coordinated manner from different positions or moving in opposite directions 
-pointers dynamically adjust based on specific conditions or criteria
-allows for efficient exploration of data and enabling solutions with optimal time and space complexity 

examples
1. reversing an array
2. pair with given sum in sorted array 
3. given array of integers, move all zeros to end of array
4. find any 3 values in sorted array that sum up to number

does your problem match this pattern? 
-linear data structure
-process pairs
-dynamic pointer movement

real world problem: memory management

'''

# create function that determines whether or not a string is a palindrome, time O(n), space O(1) 
def palindrome_checker(string):
    # initialize 2 pointers at beginning and end of string 
    left = 0
    right = len(string) - 1
    
    # check whether or not the current pair fo characters identical 
    while left < right:
       # if not identical, return False
       if string[left] != string[right]: 
           return False
       else: # otherwise, move both pointers by 1 index toward middle
           left += 1
           right -= 1
        # keep traversing them toward middle until meeting 
    
    # if we reach middle of string without finding mismatch, return True
    return True

# given array nums and integer value target, create function that determines if there
# are 3 numbers that equal target, return True if so, time O(nlog(n) + n^2), space O(n)
def find_sum_of_three(nums, target):
    # sort input array in ascending order
    nums.sort()
    low = 0
    high = len(nums) - 1    
    
    # iterate over entire sorted array to find triplet whose sum is equal to target
    # fix 1 integer at a time and find other two 
    for i in range(0, len(nums) - 2): 
        # initialize 2 pointers
        low = i + 1
        high = len(nums) - 1
        
        # in each iteration, make triplet by storing current array element and other 2 elements
        # using pointers low and high and calculate sum
        while low < high:
            # adjust calculated sum value, until it becomes equal to target value
            # by conditionally moving pointers
            triplet = nums[i] + nums[low] + nums[high]
            
            # return True if required sum found
            if triplet == target:
                return True
            
            # sum of triplet less than target, increment low pointer forward
            elif triplet < target:
                low += 1
            # sum of triplet greater than target, move high pointer backward 
            else: 
                high -= 1
            
    return False

class LinkedListNode:
    # __init__ will be used to make a LinkedListNode type object.
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    # __init__ will be used to make a LinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a LinkedListNode at head
    # of a linked list.
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
            
# given linked list, remove nth node from end of list and return head, time O(n), space O(1) 
def remove_nth_last_node(head, n):
    # set right and left point at head of list 
    right = head
    left = head 
    
    # move right pointer n steps forward 
    for i in range(n):
        right = right.next 
        
    # remove of head node
    if not right: 
        return head.next 
    
    # move both right and left pointers forward until right pointer reaches last node
    # at this point, left pointer will be pointing to node behind nth last node 
    while right.next: 
        right = right.next 
        left = left.next 
    
    # relink left node to node next to left's next node
    left.next = left.next.next 
    
    # return head of linked list 
    return head 
    
'''

prompt: given array colors, sort array in place so that elemetns of same color are adjacent in
order of red, white, and blue, 0 = red, 1 = white, 2 = blue 

'''
def sort_colors(colors):
    # declare 3 pointers, initialize start, current, and end pointers
    start = 0
    current = 0
    end = len(colors) - 1
    
    # if colors[current] is 0, swap value with colors[start], increment current & start pointers
    while current <= end:
        if colors[current] == 0:
            colors[current], colors[start] = colors[start], colors[current]
            current += 1
            start += 1 
        # otherwise, if colors[current] is 1, increment current pointer 
        elif colors[current] == 1:
            current += 1
        # otherwise colors[current] will be 2, swap value with colors[end] and decrement end pointer
        else:
            colors[current], colors[end] = colors[end], colors[current]
            end -= 1 
        
    # keep iterating until current pointer exceeds end pointer 
    return colors

# prompt: given sentence, reverse order of words w/o affecting order of letter within given word
import re
# time and space O(n)
def reverse_words(sentence):
    # remove extra spaces and strip leading/trailing spaces
    sentence = re.sub(' +', '', sentence.strip())
    
    # convert sentence to list of characters for in-place modifications as strings immutable in Python
    sentence = list(sentence)
    string_length = len(sentence) - 1
    
    # reverse entire string
    string_reverser(sentence, 0, string_length)
    start = 0
    
    # start iterating over reversed string using pointers, start and end, initialized to index 0
    for end in range(0, string_length + 1):
        # while iterating and when end points to space, reverse word pointed by start and end - 1
        if end == string_length or sentence[end] == ' ':
            # include end character for last word 
            end_index = end if end == string_length else end - 1
            
            # reverse current word 
            string_reverser(sentence, start, end_index)
            
            # once word has been reversed, update start and end to start index of next word
            start = end + 1 

    # repeat process until entire string iterated and return string 
    return ''.join(sentence)
    
# helper function that reverses characters from start to end in place
def string_reverser(string, start_rev, end_rev):
    while start_rev < end_rev:
        string[start_rev], string[end_rev] = string[end_rev], string[start_rev]
        start_rev += 1
        end_rev += 1
        
# prompt: given string word and abbreviation abbr, return True if abbreviation matches 
# given string, otherwise return False, time O(n), space O(1) 
def valid_word_abbreviation(word, abbr):
    # initialize 2 pointers, both set to 0, for word and abbreviation 
    word_index, abbr_index = 0, 0
    
    # iterate through abbreviation string until abbreviation pointer reaches its length
    while abbr_index < len(abbr):
        # if current character in abbr is a digit, validate and calculate number from 
        # consecutive digits, then skip that many characters in word 
        if abbr[abbr_index].isdigit():
            if abbr[abbr_index] == '0':
                return False
            num = 0

            while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                num = num * 10 + int(abbr[abbr_index])
                abbr_index += 1
            # skip number of characters in word as found in abbreviation 
            word_index += num
        # alternatively, if current character in abbr is a letter, ensure it matches 
        # corresponding character in word 
        else:
            # check if characters match, then increment pointers, return False if so 
            if word_index >= len(word) or word[word_index] != abbr[abbr_index]:
                return False
            word_index += 1
            abbr_index += 1
        # continue process above until either mismatch is found or end of abbr reached
    
    # once both pointers reach end of their strings, return True, otherwise False 
    return word_index == len(word) and abbr_index == len(abbr)

# determine if string num appears same when rotated 180 degrees, time O(n), space O(1)
def is_strobogrammatic(num):
    # dictionary to map each digit to its valid rotated counterpart 
    dict = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
    
    # 2 pointers: start and end of string 
    left = 0
    right = len(num) - 1 
    
    # iterate while left pointer less than or equal to right 
    while left <= right: # compare digits from both ends checking for match with valid rotation 
        # check if current digit valid and matches corresponding rotated value 
        if num[left] not in dict or dict[num[left]] != num[right]:
            return False # return False if number not strobogrammatic 
        
        # move both pointers inward until they cross 
        left += 1 
        right -= 1

    # return True if all pairs valid according to strobogrammatic rules 
    return True

# given string, return min number of moves to make palindromic, time O(n^2), space O(1) 
def min_moves_to_make_palindrome(s):
    # convert string to list for easier manipulation 
    s = list(s)
    
    # initialize moves with 0 to keep track of number of swaps required 
    moves = 0
    
    i = 0 # start pointer
    j = len(s) - 1 # end pointer 
    
    # start iterating string from either end, loop continues while i < j  
    while i < j: 
        k = j
        
        # inner loop searching backward from right/j to find character that matches s[i]
        while k > i:
            if s[i] == s[k]: # if matching character found
                # move matching character to correct position on right 
                for m in range(k, j):
                    s[m], s[m + 1] = s[m + 1], s[m] # swap
                    moves += 1 # increment count of swaps 
                # move right pointer inwards 
                j -= 1
                break
            k -= 1
            
        # no matching character found, increment moves by number of swaps needed 
        # to bring unique character to center 
        if k == i:
            moves += len(s) // 2 - i 
        i += 1 
        
    # return moves 
    return moves
    
'''
statement: given string num_str representing palindrome only containing digits, return next possible 
palindrome using same digits, returned palindrome would be the next largest palindrome, 
meaning there can be more than one way to rearrange the digits to make a larger palindrome 
return an empty string if no greater palindrome can be made.

space and time O(n)

'''

def find_next_palindrome(num_str):
    n = len(num_str)
    
    if n == 1:
        return ""
    
    # split input into its left half, 2 halves if even, leave middle unchanged for odd 
    half_length = n // 2 
    left_half = list(num_str[:half_length])
    
    
    # apply next permutation on left half by finding first decreasing digit
    # swapping with next larger digit and reversing remaining digits 
    if not find_next_permutation(left_half):
        return ""
    
    if n % 2 == 0:
        next_palindrome = ''.join(left_half + left_half[::-1])
    # mirror rearranged left half to form right half of palindrome, retain middle for odd
    else:
        middle_digit = num_str[half_length]
        next_palindrome = ''.join(left_half + [middle_digit] + left_half[::-1])
    
    # return new palindrome if larger than original input, otherwise return empty string
    if next_palindrome > num_str:
        return next_palindrome
    return ""

def find_next_permutation(digits):
    # step 1: find first digit smaller after it
    i = len(digits) - 2
    
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i == -1:
        return False
    
    # step 2: find next largest digit to swap with digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1 
        
    # step 3: swap and reverse rest to get smallest next permutation 
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1]) 
    
    return True

'''
statement: you are given two nodes, p and q - the task is to return their 
lowest common ancestor (LCA), both nodes have a reference to their parent node,
the tree's root is not provided; you must use the parent pointers to find the 
nodes' common ancestor

note: the lowest common ancestor of two nodes, p and q, is the lowest node in the 
binary tree, with both p and q as descendants

in a tree, a descendant of a node is any node reachable by following edges downward 
from that node, including the node itself

algorithm: why reset pointers? 
1. balancing the distance 
2. ensuring the nodes meet 

time O(h) where h = height of tree, space O(1)
'''
def lowest_common_ancestor(p, q):
    # initialize 2 points, one on each given node
    pointer1 = p
    pointer2 = q 
    
    # move both pointers upward along the tree using parent node, 1 step at a time
    while pointer1 != pointer2: # traverse until they meet 
        
        # if pointer reaches top of tree (NULL), move it to starting position of other node
        if pointer1.parent: # move pointer 1 to parent node or switch to other node if root reached 
            pointer1 = pointer1.parent 
        else: 
            pointer1 = q 
        
        # move pointer 2 to parent node or switch to other node if root reached 
        if pointer2.parent:
            pointer2 = pointer2.parent
        else: 
            pointer2 = p 
            
    # continue moving until these pointers meet, meeting point is LCA of nodes 
    return pointer1 # you can return either pointer since they are the same now 

'''
statement: write a function that takes a string as input and checks whether it can be a 
valid palindrome by removing at most one character from it

'''
def is_palindrome(string):
    # initialize 2 pointers at opposite ends of string 
    left = 0
    right = len(string) - 1 
    
    while left < right: 
        # if values at left and right indexes match, move both toward middle until meeting
        if string[left] == string[right]:
            left += 1
            right -= 1
        # mismatch -> skip element from left/right and check rest of string for palindrome
        else: 
            skip_left = string[left + 1:right + 1]
            skip_right = string[left:right]
            # check for palindromes on either end
            return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            
    # no mismatches or only 1 mismatch 
    return True 