def merge_sorted(nums1, m, nums2, n):
    # initialize 2 pointers that point to end of each array 
    p1 = m - 1
    p2 = n - 1
    
    for p in range(n + m - 1, -1, -1):
        if p2 < 0: 
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]: 
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
    return nums1

from heapq import *


def k_smallest_number(lists, k): 
    list_length = len(lists) # storing length of lists to use in loop later 
    kth_smallest = [] # declaring min heap to keep track of smallest elements 
    # push 1st element of each list in min heap 
    for index in range(list_length):
        if len(lists[index]) == 0: # if no elements in input list, continue to next iteration 
            continue
        else: # placing first element of each list in min heap 
            heappush(kth_smallest, (lists[index][0], index, 0))
    numbers_checked, smallest_number = 0, 0 # set counter to match if kth element equals, return that number
    # remove root of min heap
    while kth_smallest: # iterating over elements pushed in min heap 
        smallest_number, list_index, num_index = heappop(kth_smallest) # get smallest number from top of heap and its corresponding list and index 
        numbers_checked += 1 
        
        # if k elements removed from heap, return last popped element
        if numbers_checked == k:
            break
  
        # if popped element has next element in list, push next element to min heap 
        if num_index + 1 < len(lists[list_index]): # if more elements in list of top element
           heappush(kth_smallest, (lists[list_index][num_index + 1], list_index, num_index + 1)) # add next element of list to min heap 
    return smallest_number # return kth number found in input lists 

def k_smallest_pairs(list1, list2, k):
    list_length = len(list1) # storing length of lists to use in loop later
    pairs = [] # store pairs with smallest sums 
    # initialize heap to store pairs sum and respective indices 
    k_smallest = [] # declare min hep track smallest sums 
    
    # start making pairs by pairing only 1st element of second list with each element of first 
    for i in range(min(k, list_length)):
        # computing sum of pairs all elements of list1 with first index of list2 and placing in min heap 
        heappush(k_smallest, (list1[i] + list2[0], i, 0)) # push pairs onto min heap 
    
    counter = 1
    # loop to pop smallest pair from min heap (not sum and index) and add pair to result list 
    while k_smallest and counter <= k: # iterate over elements of min heap and only go up to k 
        sum_of_pairs, i, j = heappop(k_smallest) # placing sum of top element of min heap and its corresponding pairs in i and j
        
        pairs.append([list1[i], list2[j]])
        
        # increment index 2nd list since we've compared all possible pairs with 1st index of list2
        next_element = j + 1
        
        # pair next element in second list with each element of first 
        # push pair onto min heap 
        if len(list2) > next_element:
            heappush(k_smallest, (list1[i] + list2[next_element], i, next_element))    
        
        counter += 1
         
    # push and pop until k smallest pairs in result list, which we return 
    return pairs

def merge_k_lists(lists):
    # traverse input lists in pairs using head pointers 
    if len(lists) > 0: 
        step = 1 
        while step < len(lists):
            for i in range(0, len(lists) - step, step * 2):
                lists[i].head = merge_2_lists(lists[i].head, lists[i + step].head)
            step *= 2
        return lists[0].head 
    return                
                
    # compare node values of lists in each pair and add smaller one to dummy list 
    # repeat until all values from lists in pair added
    # compare this new list w resultant list of next pair 

def merge_2_lists(head1, head2):
    dummy = LinkedListNode(-1)
    previous = dummy
    
    while head1 and head2:
        if head1.data <= head2.data: 
            previous.next = head1
            head1 = head1.next 
        else:
            previous.next = head2
            head2 = head2.next 
        previous = previous.next
        
    if head1 is not None:
        previous.next = head1
    else:
        previous.next = head2
        
    return dummy.next

def kth_smallest_element(matrix, k):
    row_count = len(matrix) # store number of rows in matrix for use later 
    min_numbers = [] # declare min heap to track smallest elements 
    # push first element of each row of matrix in min heap 
    for index in range(min(row_count, k)): # heappush() method pushes element into heap
        heappush(min_numbers, (matrix[index][0], index, 0)) # and maintains heap property 
        
    numbers_checked, smallest_element = 0, 0
    
    while min_numbers:
        # get smallest number from top of heap and corresponding row and column 
        smallest_element, row_index, col_index = heappop(min_numbers)
        numbers_checked += 1
        if numbers_checked == k: # if k elements removed, return last popped element 
            break 
        
        # if current popped element has next element in its row
        if col_index + 1 < len(matrix[row_index]): # add next element of that row to min-heap 
            heappush(min_numbers, (matrix[row_index][col_index + 1], row_index, col_index + 1))
    
    
    return smallest_element

def main():

    # multiple inputs for efficient results
    matirx = [
        [[2, 6, 8],
         [3, 7, 10],
         [5, 8, 11]],

        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]],

        [[5]],

        [[2, 5, 7, 9, 10],
        [4, 6, 8, 12, 14],
        [11, 13, 16, 18, 20],
        [15, 17, 21, 24, 26],
        [19, 22, 23, 25, 28]],

        [[3, 5, 7, 9, 11, 13],
        [6, 8, 10, 12, 14, 16],
        [15, 17, 19, 21, 23, 25],
        [18, 20, 22, 24, 26, 28],
        [27, 29, 31, 33, 35, 37],
        [30, 32, 34, 36, 38, 40]]
    ]

    k = [3, 4, 1, 10, 15]

    # loop to execute till the length of list k
    for index in range(len(k)):
        print(index + 1, ".\t Input matrix: ",
              matirx[index], f"\n\t k = {k[index]}", sep="")
        print("\t Kth smallest number in the matrix is: ",
              kth_smallest_element(matirx[index], k[index]), sep="")
        print("-" * 100)

if __name__ == '__main__':
    main()
    
class traversal: 
    def __init__(self):
        self.array = []
    
    def forward_traversal(self):
        for element in self.array:
            print(element)
            
    def backward_traversal(self):
        for i in range(len(self.array) - 1, -1, -1):
            print(self.array[i])

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

def reverse_linked_list(head):
	prev, curr = None, head
	while curr:
		nxt = curr.next
		curr.next = prev
		prev = curr
		curr = nxt
	return prev

def traverse_linked_list(head):
    current, nxt = head, None
    while current:
      nxt = current.next
      current = nxt
