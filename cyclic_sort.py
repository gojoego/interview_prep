"""
cyclic sort interview practice problems 
-   use cyclic sort algorithm when problem has a limited range integer array or 
    finding missing or duplicate elements 
-   do NOT use with problems containing noninteger array correct_spots, nonarray format, or requiring stable sorting 
"""

# given array of numbers, find first missing number 
def find_missing_number(nums):
    length_nums = len(nums)
    index = 0
    
    # start list traversal from first element 
    while index < length_nums:
        correct_spot = nums[index]
        
        # if list element not equal to its index, swap it with number on the correct index
        if correct_spot < length_nums and correct_spot != nums[correct_spot]:
            nums[index], nums[correct_spot] = nums[correct_spot], nums[index] # swapping 
        # else, if element at correct index or great than length of array, skip it and move 1 step forward     
        else: 
            index += 1
            
    # once iterated over entire array, compare each number with its index 
    # first occurrence of index that's not equal to its list element is missing number 
    for i in range(length_nums):
        if i != nums[i]:
            return i
    return length_nums

# time O(n), space O(1)
def smallest_missing_positive_integer(nums):
    len_nums = len(nums)
    i = 0
    
    # iterate over all elements in nums and swap them with correct position 
    # until all elements in correct position 
    while i < len_nums:
        correct_spot = nums[i] - 1 # determining correct position of current element 
        if 0 <= correct_spot < len_nums and nums[i] != nums[correct_spot]:
            nums[i], nums[correct_spot] = nums[correct_spot], nums[i] # swap current element to correct position 
        else:
            i += 1 # move on to next element if current element already at correct position 
            
    # iterate over nums again and check if each element equal to index + 1
    for i in range(len_nums):
        # if element not in correct position, return index + 1 of element that is
        # out of order, as smallest missing positive number
        if i + 1 != nums[i]:
            return i + 1 
    
    # if all elements in order, return length of array + 1 as smallest missing positive integer 
    return len_nums + 1

# first solution that passed all test cases 
def finding_corrupt_pair(nums):
    len_nums = len(nums)
    i = 0
    
    # apply cyclic sort to array 
    while i < len_nums:
        correct_spot = nums[i] - 1 # determining correct position of current element 
        if correct_spot < len_nums and nums[i] != nums[correct_spot]:
            nums[i], nums[correct_spot] = nums[correct_spot], nums[i] # swap current element to correct position 
        else:
            i += 1
    
    dup_num = 0
    miss_num = 0
    # after sorting, traverse array and find number that isn't at correct position - this is the duplicate number 
    for i in range(len_nums):
        if i + 1 != nums[i]:
            dup_num = nums[i]
            miss_num = i + 1 # add 1 to index of duplicate number - this is the missing number
    
    # return pair containing missing and duplicated number 
    return [miss_num, dup_num]

# second solution that also passes all test cases 
def find_corrupt_pair(nums):
    # declare and initialize variables for missing and duplicated numbers
    missing = None
    duplicated = None
    
    i = 0 # apply cyclic sort on array 
    while i < len(nums): # traversing whole array 
        correct_spot = nums[i] - 1 # determine what position specific element should be at 
        if nums[i] != nums[correct_spot]: # check if number is at wrong position 
            nums[i], nums[correct_spot] = nums[correct_spot], nums[i] # swapping number to its correct position 
        else:
            i += 1 
            
    for j in range(len(nums)): # finding corrupt pair (missing, duplicated)
        if nums[j] != j + 1:
            duplicated = nums[j]
            missing = j + 1
    
    return [missing, duplicated]
    

def first_k_missing_numbers(arr, k):
    len_arr = len(arr)
    i = 0
    
    # traverse arr and place each element at its correct position while ignoring 
    # negative elements and elements greater than length of arr
    while i < len_arr:
        correct_spot = arr[i] - 1
        if 0 <= correct_spot < len_arr and arr[i] != arr[correct_spot]:
            arr[i], arr[correct_spot] = arr[correct_spot], arr[i]
        else:
            i += 1
    
    # create set to store elements of arr that are not at their correct position and array to store missing elements 
    misplaced_set = set()
    missing_elements = []
    
    # iterate through arr again to find elements that are not at correct position
    for i in range(len_arr):
        if arr[i] != i + 1:
            # insert those elements in set and add respective positions in missing elements array 
            misplaced_set.add(arr[i])
            if len(missing_elements) < k:
                missing_elements.append(i + 1)
                
    # find additional missing numbers if we haven't found k missing numbers yet 
    extra_num = len_arr + 1
    while len(missing_elements) < k:
        if extra_num not in misplaced_set:
            missing_elements.append(extra_num)
        extra_num += 1
    
    return missing_elements 