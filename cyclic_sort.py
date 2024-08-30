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

def main():
  input_array = [[1, 2, 3, 4], [-1, 3, 5, 7, 1], [1, 5, 4, 3, 2], [-1 , 0, 2, 1, 4], [1,4,3]]
  x = 1
  for i in range(len(input_array)):
    print(x, ".\tThe first missing positive integer in the list ", input_array[i], " is: ", sep = "")
    print("\t" + str(smallest_missing_positive_integer(input_array[i])))
    print("-" * 100)
    x = x + 1

if __name__ == '__main__':
  main()