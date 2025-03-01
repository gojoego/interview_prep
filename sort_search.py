'''
sort and search 
- organizing data to find optimal solution 
- sorting and efficient searching to simplify problem-solving 
- sort data first to create ordered structure that enhances searching, comparing, 
  and optimizing processes to reduce time complexity 
- can utilize binary or 2 pointer techniques for searching/validation after sorting

benefits of sort/search 
- quicker determine if values smaller/larger/equal for element comparisons/condition checks 
- narrows ranges / data boundaries for binary search or other efficient techniques 
- reduced need for repetitive comparisons 
- sorts group related items together 
- more easily uncover data patterns 

search post-sort 
- apply efficient search techniques after sorting 
- binary search: narrows search space by constantly halfing it, useful for locating 
  or matching elements within sorted dataset 
- two pointer: 2 oppositely positioned pointers move towards each other based on 
  specific conditions or criteria; reduces need to check every possible combo 
- sliding window: searching through subsets data within fixed range or size; 
  used to process continuous subarrays or substrings 
- greedy algorithms: best choice at each stage to achieve best overall outcome 

examples: 
1. two sum less than k 
2. valid triangle number 

does your problem match this pattern? yes, if... 
- sortable data 
- pairwise and ordered comparisons 
- range-based values 
- optimization based on relationships 
- efficient searching methods 

real-world problems 
- e-commerce inventory management 
- logistics and transportation 
- stock market analysis 
  
'''

'''
Find the Distance Value Between Two Arrays

statement: you are given two integer arrays, arr1 and arr2, along with an integer d; 
your task is to find and return the distance value between these arrays

note: the distance value is defined as the count of elements in arr1 for which there 
is no element in arr2 such that |arr1[i] - arr2[j]| <= d

algorithm: find distance between 2 arrays using sort/search pattern; sort 2nd array; 
for each 1st array element perform binary search to find closest element in 2nd array
without checking all values and avoiding brute-force comparisons; condition = check 
whether abs difference between element in 1st array and closest in 2nd greater than 
threshold d; elements further from closest values will always have greater absolute 
difference and cannot violate condition; binary search helps identify these closest 
high and low values; if no such element in 2nd array violates condition for given 
element in 1st array, increment distance 

time O((m + n)logm) where n = 1st array length, m = 2nd array length, space O(1)
'''
def find_the_distance_value(arr1, arr2, d): 
    # sort 2nd array to enable binary search 
    arr2.sort()
    distance = 0 # tracking how many elements from 1st array meet criteria
    
    # iterate through 1st array and binary search 2nd to find closest element to current in 1st
    for i in range(len(arr1)):
        left = 0 
        right = len(arr2) - 1 
        valid = True 
        
        while left <= right:
            mid = (left + right) // 2 
            if arr2[mid] == arr1[i]:
                valid = False
                break
            elif arr2[mid] < arr1[i]:
                left = mid + 1 
            else: 
                right = mid - 1 
        
        # check closest higher or equal elements
        if left < len(arr2) and abs(arr2[left] - arr1[i]) <= d:
            valid = False
        
        # check closest lower element
        if right >= 0 and abs(arr2[right] - arr1[i]) <= d:
            valid = False
        
        if valid:
            distance += 1
    
    return distance

