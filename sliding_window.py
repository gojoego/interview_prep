'''

sliding window pattern
-used to process sequential data, arrays, strings to efficiently solve subarray or substring problems 
-maintains dynamic window that slides through array or string, adjusting boundaries as needed for tracking 
-window slides over data in chunks corresponding to window size according to problem requirements 
-variation of 2 pointers pattern w/ pointers being used to set window bounds 
-time O(n)

examples
1. max sum subarray of size k 
2. longest substring without repeating characters 
3. given string s and string t, find shortest substring in s that contains all t characters
4. given array of integers and target sum, find length of smallest subarray whose sum is greater than or equal to target sum

does your problem match this pattern? yes, if...
-contiguous data 
-processing subsets of elements
-efficient computation time complexity

real-world problems
-telecommunications
-video streaming 
-social media content mining 

'''

'''

statement: given a string, dna, that represents a DNA subsequence, and a number k, return all 
the contiguous subsequences (substrings) of length k that occur more than once in the string, 
the order of the returned subsequences does not matter, if no repeated substring is found, the 
function should return an empty set

the DNA sequence is composed of a series of nucleotides abbreviated as A, C, G, and T; 
for example ACGAATTCCG is a DNA sequence; when studying DNA, it is useful to identify repeated sequences in it

algorithm:
-use Rabin-Karp algo that uses sliding window with rolling hash for pattern matching 
-traverse string by using sliding window of length k, which slides 1 character forward per iteration 
-compute hash of current k-length substring in window each iteration 
-check if hash already in set 
    -add to output if repeated
    -add to set otherwise 
-repeat for all k-length substrings and return output 

polynomial rolling hash:
-used to achieve constant-time hashing: H = c1 * a^k-1 + c2 * a^k-2...
-value of 4 used for constant to ensure each nucleotide assigned unique value in polynomial rolling hash 
 but any number larger than 4 can be used -> choose number large enough to avoid collisions while still 
 being small to minimuze risk of arithmetic overflow 

time O(n), space O(n) where n = length of input string 
'''
def find_repeated_sequences(dna, k):
    string_length = len(dna)
    
    if string_length < k:
        return set()
    
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    base_value = 4
    
    # numeric representation of sequence 
    numbers = [] # easier access to numeric value of nucleotides when calculating hash value 
    for i in range(string_length):
        numbers.append(mapping.get(dna[i]))
        
    hash_value = 0 # to store hash value of current k-length sequence in window 
    hash_set = set() # stores all unique hash values of k-length substrings 
    output = set() # repeated substrings 
    
    # iterate over length k substrings of input string 
    for i in range(string_length - k + 1):
        # if window at initial position, calculate hash value from scratch 
        if i == 0:
            for j in range(k):
                hash_value += numbers[j] * (base_value ** (k - j - 1)) # polynomial hash function
        else:   
            # calculate hash value of current k-length substring by utilizing hash value of previous k-length substring
            previous_hash_value = hash_value
            hash_value = ((previous_hash_value - numbers[i - 1] * (base_value ** (k - 1))) * base_value) + numbers[i + k - 1]
                
        # if hash of substring has already been stored, substring repeated, add to output 
        if hash_value in hash_set:
            output.add(dna[i : i + k])
        
        # add evaluated hash value to hash set 
        hash_set.add(hash_value)
    
    # when all substrings evaluated, return output
    return output

'''
naive DNA repeated sequences algorithm: iterate though input DNA sequence, add all unique
substrings of length k to set; if substring already present in set -> repeated substring 

time and space O(kn) where k = size of each contiguous subsequence and n = length of input sequence  
'''

def find_repeated_sequences_naive(dna, k):
    seen = set()
    output = set()
    
    for i in range(len(dna) - k + 1):
        substring = dna[i : i + k]
        if substring in seen:
            output.add(substring)
        seen.add(substring)
    
    return output

'''
statement: given integer list, nums, find max values in all continguous subarrays (windows)
of size w

algorithm: 
- check which index has fallen out of current window and remove it
- processing elements of first window 
    - every time new index added to window, iterate backward and remove indices 
      with values smaller than or equal to new element in window -> "clean up"
    - perform clean up starting with second element added to first window -> 
      elements smaller than max of that window excluded already 
- iterate over remaining input list 
    - clean up step for each element 
    - check whether first index in current window part still part of current window 
    - remove first index if not 
- return output list when entire input list processed 

deque: double ended queue that supports constant time removals from both ends 
    -> reduces time complexity to O(n)
    
time O(n) where n = size of list of integers, space O(w) where w = window size 
'''
from collections import deque

def find_max_sliding_window(nums, w):
    # if length of input list is 1, return input list 
    if len(nums) == 1:
        return nums
    
    output = []
    
    # initialize empty deque data structure 
    current_window = deque()
    
    # iterate through first w elements in input array
    for i in range(w):
        # for every element, remove previous smaller elements from current window 
        clean_up(i, current_window, nums)
        # append index of current element to current window 
        current_window.append(i)
    
    # appending max element of current window to output list 
    output.append(nums[current_window[0]]) # store max value of initial window 
    
    
    for i in range(w, len(nums)):
        # performing cleanup operations on deque to maintain decreasing order of values 
        clean_up(i, current_window, nums)
        # remove first index from current window if falls outside of window 
        if current_window and current_window[0] <= (i - w):
            current_window.popleft()
        # append index of current element to current window 
        current_window.append(i)
        # appending max element of current window in output list 
        output.append(nums[current_window[0]])
    
    # slide window through array, updating/storing max values for each window, then return array containing output
    return output

# helper function to clean up queue 
def clean_up(i, current_window, nums):
    # remove all indices from current window whose corresponding values smaller/equal to current element
    while current_window and nums[i] >= nums[current_window[-1]]:
        current_window.pop()

'''
naive algorithm for sliding window max: slide window over input list and find max in each window
separately, then add to output list; in each iteration, update current window by removin first 
element from current window and adding incoming element of input list; return list containing 
maximums of all (n - w + 1) windows 

time O(n * w), space O(w)
'''

def naive_sliding_window_max(nums, w):
    if not nums or w == 0:
        return []
    
    n = len(nums)
    output = []
    
    # iterating over each window position 
    for i in range(n - w + 1):
        # find max element in current window 
        max_value = max(nums[i : i + w])
        output.append(max_value)
    
    return output

def find_longest_substring(input_str):
    
    if len(input_str) == 0: # check for empty string
        return 0 
    
    window_start = 0 # current window start 
    longest = 0 # length of longest substring 
    last_seen_at = {} # initialize empty hashmap storing index of last occurrence of each character 
    
    # traverse string to find longest substring w/ out repeating chars 
    for index, value in enumerate(input_str):
        
        # check if current character already seen in current window 
        if value in last_seen_at and last_seen_at[value] >= window_start:
            # if yes, update start of window to index after last occurrence
            window_start = last_seen_at[value] + 1
            
        # update index of last occurrence of character
        last_seen_at[value] = index
        
        # update length of longest substring 
        longest = max(longest, index - window_start + 1)
            
    return longest

def min_sub_array_len(target, nums):
    window_size = float('inf') # store size of min subarray 
    start = 0
    current_sum = 0
    for end in range(len(nums)): # slide window over input array using start and end 
        current_sum += nums[end] # increment end and add new element of window into sum 
        while current_sum >= target: # if sum greater than or equal to target current
            current_subarray_size = (end + 1) - start # calculate current subarray size 
            window_size = min(window_size, current_subarray_size) # compare current subarray size with window size and store smaller of two 
            current_sum -= nums[start] # remove element from start of window 
            start += 1 # increment start 
    if window_size != float('inf'): # if window size +inf -> no subarray w sum equal/greater than target 
        return window_size
    
    return 0 # return 0 to indicate no subarray had equal or greater sum than target 
    
def max_profit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

'''
statement: given an array of integers is, and an integer k, return the maximum average of

a contiguous subarray of length k

algorithm: calculate sum of first k elements, store current and max sum, window 
slides 1 element at a time, subtracting element that leaves window from current sum 
and adding new element, track max by taking max of max sum and current, return max sum / k 

'''
def find_max_average(nums, k):

    # initialize current sum and max sum with sum of first k elements 
    current_sum = sum(nums[:k])
    max_sum = current_sum
    
    
    # slide window by updating current sum using new element and removing old one 
    for i in range(nums, len(nums)):
        current_sum += nums[i] - nums[i - k]
        
    # update max su
    # m if current sum exceeds max 
    max_sum = max(max_sum, current_sum)
            
    # return max average by dividing max sum by k 
    return max_sum / k

'''
statement: a dieter consumes calories[i] calories on the i-th day, given an integer k, 
the dieter reviews their calorie intake over every sequence of k consecutive days 
(from calories[i] to calories[i+k-1] for all 0 <= i <= n-k), for each sequence, they 
calculate T, the total calories consumed over those k days:

    - if T is less than lower, the dieter performs poorly and loses 1 point
    - if T is greater than upper, the dieter performs better and gains 1 point
    - if T is between lower and upper (inclusive), the dieter's performance is 
      normal, and their points remain the same

the dieter starts with zero points, return the total points after the dieter follows 
this routine for all calories.length days, the total points can be negative

time O(n) where n = length of calories array, space O(1)
'''
def diet_plan_performance(calories, k, lower, upper):
    # initialize points variable to 0
    points = 0 
    # calculate sum of calories for first k days
    calories_sum = sum(calories[:k]) 

    # evaluate initial window - compare sum with upper and lower thresholds, update points accordingly
    if calories_sum < lower: # lower threshold 
        points -= 1 # decrement
    elif calories_sum > upper: # upper threshold 
        points += 1 # increment        

    # move window 1 day forward and calculate new sum
    for i in range(k, len(calories)):
        
        calories_sum += calories[i] -calories[i - k]
        
        # update points based on new sum for each consecutive window  
        if calories_sum < lower:
            points -= 1
        elif calories_sum > upper:
            points += 1         

    # return total points after processing all sequences of k days  
    return points 

'''
statement: while visiting a farm of fruits, you have been given a row of fruits 
represented by an integer array, fruits, where fruits[i] is the type of fruit the ith
tree produces - you have to collect fruits, but there are some rules that you must 
follow while collecting fruits:

    - you are given only two baskets, each capable of holding an unlimited quantity 
      of a single type of fruit
    - you can start collecting from any tree but must collect exactly one fruit from 
      each tree (including the starting tree) while moving to the right
    - you must stop while encountering a tree with a fruit type that cannot fit into 
      any of your baskets

return the maximum iber of fruits you can collect following the above rules 
for the given array of
 fruits

algorithm: use sliding window to manage range of trees being considered, starts from 
small window and expands window as more trees added to allow max fruit collection, if 
fruit types grows to over 2 -> reduce window size from left until valid     

time O(n) where n = total iber of fruit trees, space O(1)
'''

def total_fruit(fruits):
    # create dictionary to track count/frequency of each fruit type in current window
    baskets = {}
    # max iber of fruits collected so far 
    collected = 0 
    # 
    # left variable for window start / left boundary for sliding window  
    left = 0
    
    # iterate over each tree / right boundary of sliding window 
    for right in range(len(fruits)):    
        # expand window by adding current fruit to baskets and incrementing its count
        baskets[fruits[right]] = baskets.get(fruits[right], 0) + 1
    
        # if the basket has more than 2 fruit types
        while len(baskets) > 2:
            # shrink window from left by decreasing count of leftmost fruit/left boundary
            baskets[fruits[left]] -= 1   
    
            # remove any fruit from basket if its count reaches 0 
            if baskets[fruits[left]] == 0:
                del baskets[fruits[left]]
        
            # move left boundary to the right 
            left += 1
        
        # track current window size and update max iber of fruits collected if current is greater 
        collected = max(collected, right - left + 1)
    
    # return max count after processing all trees 
    return collected          

'''
statement: you are given an integer array, is, and an integer k - determine whether 

two distinct indices, i and j, are in the array, such that is[i] == is[j] and the 
absolute difference between i and j is at most k - return TRUE if such indices exist; 
otherwise, return FALSE

time O(n) where n = length of array, space O(min(n, k)) space occupied by set = size of current sliding window
'''
def contains_nearby_duplicate(nums, k):
    # create set to tra
    # ck elements within range k 
    seen = set()
    
    # iterate through the is array
    for i in range(len(nums)):

        # check if current element already exists in set, return True if so  
        if nums[i] in seen:  
            return True # indicates duplicate found within range k 
       
        # if current  ient range(len(does))n't exist, add to set 
        seen.add(nums[i])
        
        # if set size exceeds k, remove oldest element to keep k latest elements 
        if len(seen) > k: 
            seen.remove(nums[i - k])
    
    # if no duplic ifounrange(len(d, r))eturn False     
    return False
