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

statement: you are given a 0-indexed array of positive integers, nums, and a value, target; 
the target represents an index i in the array such that nums[i] == target

your task is to return a list of indexes of nums where the value equals target after sorting 
the array in nondecreasing order; if no such indexes exist, return an empty list; ensure the 
returned list is sorted in increasing order

algorithm: sort array from lowest to highest, search through sorted array and collect indices 
where values matches target 

time O(nlogn) where n = number of elements in array, space O(1)
'''
def target_indices(nums, target):
    output = []
    
    # sort nums in ascending order so target value's positions easier to find 
    nums.sort()
    
    # iterate through all elements of sorted array and for each element, check if it matches target value 
    for i in range(len(nums)):
        if nums[i] == target:
            # store index in new array when element matches target value 
            output.append(i)

    # after iterating through all elements, return array of stored indexes 
    return output

'''
Count Pairs in Two Arrays

statement: you are given two positive integer arrays, nums1 and nums2, both of length n;
your task is to count and return the number of pairs of indexes (i,j) where:
    
    i < j, and
    nums1[i] + nums1[j] > nums2[i] + nums2[j]

in simpler terms, the sum of two elements from nums1 must be greater than that of the 
corresponding elements from nums2

algorithm: 
    simplify condition to (nums1[i] - nums2[i]) + (nums1[j] - nums2[j]) > 0
    reduce condition to difference[i] + difference[j] > 0
    
time O(nlogn) and space(n) where n = number of elements in the array 
'''

def count_pairs(nums1, nums2):
    n = len(nums1)
    
    # create an array to store difference between corrsponding elements of arrays 
    diffs = [nums1[i] - nums2[i] for i in range(n)]

    # initialize counter to store number of valid pairs 
    valid_count = 0 
    
    # sort difference array to efficiently ID valid pairs 
    diffs.sort()
    
    # iterate over differences 
    for i in range(n):
        # if difference at index > 0 
        if diffs[i] > 0: # add count of indices after current index to counter
            valid_count += n - i - 1  # all subsequent elements will form valid pairs 
            
        # otherwise, binary search to find 1st position after current index where sum of 
        # differences satisfies condition of being greater than zero 
        else: 
            left = i + 1 
            right = n - 1 
            while left <= right: 
                mid = (left + right) // 2 
                # if difference at mid valid pair, search in left half 
                if diffs[i] + diffs[mid] > 0:
                    right = mid - 1 
                # if difference at mid not valid, search in right 
                else:
                    left = mid + 1 
        
            # add count of indices from this position onward to the counter
            valid_count += n - left 

    # after processing all indices, return total count of valid pairs stored in counter     
    return valid_count

def brute_force_count_pairs(nums1, nums2):
    n = len(nums1)
    count = 0 
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums1[i] + nums1[j] > nums2[i] + nums2[j]:
                count += 1
    return count

'''
Valid Triangle Number

statement: given an array of integers, nums, determine the number of unique triplets that can 
be selected from the array such that the selected values can form the sides of a valid triangle;
return this count as the result

valid triangle: a triangle is valid if the sum of the lengths of any two smaller sides is strictly 
greater than the length of the third largest side; for three sides a, b, c (such that a ≤ b ≤ c), 
the condition to form a valid triangle is a + b > c

algorithm: 
- triangle inequality rule: sum of 2 smaller sides > largest 
- sort array in ascending order -> largest side always at end 
- iterate backward from end to search for valid combos 
- ID valid combos while iterating -> fix current element as largest and explore potential pairs 
  for small sides 

time O(nlogn + n ^ 2) where n = size of array, space O(1)
'''
def triangle_number(nums): 
    # sort the values of nums in ascending order to simplify checking the triangle inequality
    nums.sort()

    count = 0 
    
    # begin evaluating potential combinations by treating the largest value as the third side of the 
    # triangle aka iterate backward through array treating nums at i as largest side    
    for i in range(len(nums) - 1, 1, -1):
        # select two other values(sides) from the remaining array, one from the start and the other 
        # from one position, before selecting the largest value (third side) -> these two values act 
        # as the first two sides of the triangle
        left = 0
        right = i - 1 
        
        # search to find all valid pairs (nums[left], nums[right]) for nums[i]
        while left < right:
            # check if the sum of the first two sides exceeds the third; all combinations between 
            # these first two sides are valid if this condition is met; count these combinations and 
            # move to smaller potential sides
            if nums[left] + nums[right] > nums[i]:
                count += (right - left)
                right -= 1 
            #  if the condition is not met, adjust the choice by exploring larger values from the start
            else:
                left += 1 
                
    # continue this process for all possible groupings and return the total number of combinations 
    # that satisfy the triangle condition
    return count

'''
Minimum Operations to Make All Array Elements Equal

statement: you are given an array, nums, consisting of positive integers of size n and another array 
queries of size m; for each query i in queries, the goal is to make all elements of nums equal to 
queries[i]; to achieve this, you can perform the following operation any number of times:

    increase or decrease an element of nums by 1

return an array answer of size m, where answer[i] is the minimum number of operations needed to make 
all elements of nums equal to queries[i]; after processing each query, the nums array is reset to its 
original state

algorithm: 
- sort array and use prefix sum array for range sum calculations 
- prefix sum stores cumulative sums of sorted array -> iterate through and maintain running total
- for each query, split array into elements smaller than / greater than or equal to using binary search 
- find smallest index where element greater than or equal to query value 
- range adjust during search: if middle element smaller move right, if greater/equal to left 
- left cost = (query * count of smaller elements) - sum of smaller elements
- right cost = (sum of larger elements ) - (query * count of larger elements)
- total cost = left + right

time O((n + m)logn), space O(n) where n = number of elements in nums and m = number of queries 
'''
def min_operations(nums, queries):
    n = len(nums)
    
    # sort nums array 
    nums.sort()
    
    # compute prefix sum array for cumulative sums
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]
    
    output = []
    for query in queries:
        index = binary_search_minops(nums, query)
        
        # calculcate cost to adjust all elements smaller than query
        # (query×count of smaller elements) − sum of smaller elements
        left_operations = query * index - prefix_sums[index]
        
        # compute cost to adjust all elements larger than or equal to query using 
        # (sum of larger elements) − (query×count of larger elements)
        right_operations = (prefix_sums[n] - prefix_sums[index]) - query * (n - index)
        
        # append sum of left and right costs for each query to result array 
        output.append(left_operations + right_operations)
        
    return output

def binary_search_minops(array, target):
    low = 0 
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2 
        if array[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1 
            
    return low 

'''
Sum of Mutated Array Closest to Target

statement: given an integer array arr and a target value target, find an integer value such that 
if all the numbers in arr greater than value are replaced with a value, the sum of the array gets 
as close as possible to the target

choose the smaller value if there's a tie (two value options are equally close to the target)

note: the answer doesn't have to be a number from the array

algorithm:
- sort array in ascending order -> smaller numbers evaluated first 
- evaluate whether replacing all subsequent numbers with current number would minimize gap between 
  modified array sum and target for each number in array 
- maintain remaining target to determine if replacing all subsequent numbers with current would 
  minimize gap 
- initially, remaining target equal to original target value 
- during traversal, subtract each processed number from target to update remaining target 
- running total helps evaluate how much more is needed to match target 
- at each step, check if remaining target small enough to be achieved by replacing all remaining 
  numbers in array with current number: 
  
  remaining target ≤ current value * number remaining of elements
  
- recalculate replacement value if condition true 
- replacement value determined by dividing remaining target by number of remaining elements in array: 

  replacement value = remaining target / count of remaining elements 
  
- calculate replacement value instead of simply using current number because remaining target may not 
  be exact multiple of current number, especially remaining target smaller than 
  
  current_value * number_of_remaining_elements

- can adjust replacement value more precisely to minimize gap between target and modified array sum 

time O(nlogn) where n = number of elements in array, space O(1)

'''

def find_best_value(arr, target):
    # 1: sort array in ascending order to make it easier to process elements from smallest to largest 
    arr.sort()
    
    # array length variable to calculate how many elements left to process at each step
    n = len(arr)
    
    remaining_target = target
    
    # 2: iterate through sorted array 
    for i, num in enumerate(arr):
        # check if remaining target can be distributed evenly among remaining numbers 
        if remaining_target <= num * (n - i):
            # calculate replacement value by dividing remaining target by remaining count
            replacement_value = remaining_target / (n - i)
            
            # handle tie cases: if fractional part exactly 0.5 -> choose smaller integer
            if replacement_value - int(replacement_value) == 0.5:
                return int(replacement_value)

            # otherwise, round to nearest integer
            return round(replacement_value)

        # subtract current number from remaining target since it is fully used 
        remaining_target -= num
    
    # 3: if target exceeds sum of array, return largest element in array 
    return arr[-1]

'''
Range Sum of Sorted Subarray Sums

statement: you are given an integer array nums containing n positive integers along with left and 
right; calculate the sum of its elements for every non-empty continuous subarray of nums; collect 
these sums into a new array and sort it in nondecreasing order; this will result in a new array of 
size n * (n + 1) / 2

your task is to return the sum of the elements in this sorted array from the index left to right 
(inclusive with 1-based indexing)

note: as the result can be large, return the sum modulo 10 ^ 9 + 7

algorithm: 
- use binary search to directly find range sum without calculating or sorting all subarray sums 
- ID feasible range for possible subarray sums -> between smallest array element and total sum 
- range ensure no valid sums overlooked / serves as foundation for binary search 
- for each threshold, calculate count of subarrays with sums below and their cumulative sum using 
  sliding window technique 
- goal is to find threshold value T such that there are exactly k subarrays with sums less than 
  or equal to T 
- binary search narrows threshold by checking for each mid value (potential sum threshold) if it 
  satisfies condition of having at least k subarrays below it 
- by adjusting search range based on count, we pinpoint boundaries of desired range of subarray sums
- once total sum of subarrays calculated up to index right and total sum of subarrays up to index left 
  subtract these 2 sums to get sum of subarrays in range [left, right]
  
time O(nlog(sum)) where n = length of nums and sum = total sum of nums array, space O(1)
'''
def range_sum(nums, n, left, right):
    mod = 10 ** 9 + 7

    # calculate sum of first right subarray sums minus first 'left - 1' subarray sums 
    result = (sum_firstk(nums, n, right) - sum_firstk(nums, n, left - 1)) % mod   

    # ensure non-negative result by applying modulo again 
    return (result + mod) % mod

def sum_firstk(nums, n, k):
    min_sum = min(nums) # smallest sum in array 
    max_sum = sum(nums) # largest sum in array 
    T_left = min_sum
    T_right = max_sum
    
    # perform binary search to find smallest subarray sum threshold that contains at least k subarrays
    while T_left <= T_right:
        mid = T_left + (T_right - T_left) // 2
        # if there are at least k subarrays with sum <= mid  
        if count_sum(nums, n, mid)[0] >= k: 
            T_right = mid - 1 # narrow down search to left half 
        else: 
            T_left = mid + 1 # narrow down search to right half 
    
    # calculate total sum of first k subarray sums 
    count, total_sum = count_sum(nums, n, T_left)
    
    # subtract excess sum of subarrays beyond kth subarray 
    return total_sum - T_left * (count - k)

def count_sum(nums, n, target):
    count = 0 
    current_sum = 0 
    total_sum = 0 
    window_sum = 0 
    i = 0 
    
    for j in range(n):
        current_sum += nums[j] # add current element to running sum 
        window_sum += nums[j] * (j - i + 1) # add contribution of current element to window sum 
        
        # while current sum exceeds target, adjust window size by moving i 
        while current_sum > target:
            window_sum -= current_sum # remove current window sum 
            current_sum -= nums[i] # remove element at left pointer 
            i += 1 
        
        # count number of valid subarrays in current window 
        count += j - i + 1 
        total_sum += window_sum # add current window sum to total sum 
    
    return count, total_sum

