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


'''
Longest Subsequence With Limited Sum

statement: you are given an integer array, nums, of length n, and an integer array, queries, 
of length m

for each element in queries, determine the maximum number of elements that can be selected from 
nums to form a subsequence such that the sum of the selected elements is less than or equal to 
the query value

return an array answer of length m, where answer[i] represents the size of the largest subsequence 
of nums whose sum is less than or equal to queries[i]

algorithm: 
- sort array in ascending order to facilitate binary search operations 
- prefix sum array where each element represents cumulative sum of elements in nums to that index 
- allows quick calculation of sum of any contiguous subsequence 
- use binary search on prefix sum array to determine max length of subsequence sum <= query value
- binary search finds largest index where cumulative sum does not exceed query 
- all elements from start of array to index form valid subseq and index corresponds to length 

time O((n + m)logn), space 0(n) where m = queries and n = number of elements in nums
'''
def answer_queries(nums, queries):
    # sort input array nums in ascending order 
    nums.sort()
    
    # calculate prefix sums for sorted array, prefix_sum[i] = cumulative elements sum from start to i 
    prefix_sum = [0] * len(nums)
    prefix_sum[0] = nums[0]
    for i in range(1, len(nums)):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i] 
    
    # for each query, binary search on prefix sum to find largest k where sum of k + 1 elements <= query value 
    output = []

    for query in queries:
        index = binary_search(prefix_sum, query)
        # store subsequence length (determined from binary search) for all queries in list
        output.append(index)      
        
    # return final output 
    return output

def binary_search(prefix_sum, target):
    low = 0 
    high = len(prefix_sum) - 1
    
    while low <= high: 
        mid = (low + high) // 2 
        if prefix_sum[mid] <= target:
            low = mid + 1 
        else:
            high = mid - 1
    return high + 1

'''
Find Target Indices After Sorting Array

statement: you are given a 0-indexed array of positive integers, nums, and a value, target; the target represents an index 
i
i
 in the array such that nums[i] == target.

Your task is to return a list of indexes of nums where the value equals target after sorting the array in nondecreasing order. If no such indexes exist, return an empty list. Ensure the returned list is sorted in increasing order.
'''