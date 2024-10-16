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

# palindrome check string if 1 character removed, time O(n), space O(1)
def is_palindrome(s):
    # initialize 2 pointers at opposite ends of string 
    left = 0
    right = len(s) - 1
    
    removed = False # track whether character removed to allow at most one removal 
    
    # while loop that runs while pointers do not cross 
    while left < right:
        # if values at left and right indexes match, move both toward middle until they meet
        if s[left] == s[right]:
            left += 1
            right += 1
        # if mismatch occurs, skip one of the elements from either left or right side 
        # check rest of string for palindrome 
        else:
            if removed: # if character already removed, no longer valid palindrome 
                return False
            # check if removing left character makes remaining substring palindrome
            if s[left + 1] == s[right]:
                left += 1
            # skip element from otherside and check for palindrome
            # check if removing right character makes remaining substring palindrome 
            elif s[left] == s[right - 1]:
                right -= 1
            # if neither removal helps, cannot be valid palindrome 
            else: # if no palindrome obtained, return False 
                return False
            # mark that character has been removed 
            removed = True

    # return True if no more than 1 mismatch occurs 
    return True