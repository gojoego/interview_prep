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

'''
Minimum Window Subsequence

statement: given two strings, str1 and str2, find the shortest substring in str1 such that str2 
is a subsequence of that substring

- substring: contiguous sequence of characters within a string
- subsequence: sequence that can be derived from another sequence by deleting zero or 
  more elements without changing the order of the remaining elements

let's say you have the following two strings:

str1 = “abbcb”
str2 = “ac”

in this example, “abbc” is a substring of str1, from which we can derive str2 simply by 
deleting both the instances of the character b; therefore, str2 is a subsequence of this 
substring; since this substring is the shortest among all the substrings in which str2 is 
present as a subsequence, the function should return this substring, that is, “abbc”

- if there is no substring in str1 that covers all characters in str2, return an empty string
- if there are multiple minimum-length substrings that meet the subsequence requirement, return 
the one with the left-most starting index

algorithm: use sliding window to eliminate extra traversals of substrings, only consider substrings 
that are sure to contain all characters of str2 in same order, track whether subsequence has been
found or not and select shortest subsequence from str1 

time O(n * m) where n and m = lengths of str1 and str2, space O(1)
'''

def min_window(str1, str2):
    size_str1 = len(str1)
    size_str2 = len(str2)

    min_sub_length = float('inf')
    
    index_s1 = index_s2 = 0
    
    min_subsequence = "" # output = smallest possible subsequence 
    
    # iterate through str1 to find potential window that contains all chars of str2 in order 
    while index_s1 < size_str1:
        # check if characters being pointed at are the same 
        if str1[index_s1] == str2[index_s2]:
            # if pointed character same in both strings increment index_s2 
            index_s2 += 1 # index_s2 will only reach end of str2 if all chars found in str1
            
            # backtrack once potential window end found until all chars of str2 found in reverse, helps locate potential start of smallest subsequence 
            if index_s2 == size_str2: # check if index_s2 at end of str2
                # initialize start to index where all characters of str2 present in str1
                start, end = index_s1, index_s1
                index_s2 -= 1 
                
                # decrement pointer index_s2 and start reverse loop
                while index_s2 >= 0:    
                    # decrement pointer index_s2 until all characters of str2 found in str1 
                    if str1[start] == str2[index_s2]:
                        index_s2 -= 1
                    
                    # decrement start pointer everytime to find starting point of required subsequence
                    start -= 1 
                
                # repeat with 2nd character of current window until str1 end met 
                start += 1
                
                # check if min sub length of subsequence pointed by start and end pointers less than current 
                if end - start < min_sub_length:
                    # update min sub length if current subsequence shorter
                    min_sub_length = end - start
                    
                    # update min subsequence string to this new shorter string 
                    min_subsequence = str1[start : end + 1]
                
                # set index_s1 to start to continue checking in str1 after discovered subsequence
                index_s1 = start
                index_s2 = 0    

        # increment index_s1 to check next character in str1 
        index_s1 += 1   
    
    # return min window subsequence 
    return min_subsequence

'''

naive approach to the minimum window subsequence: generate all possible substrings of str1, 
check which substrings contain str2 as subsequence, return shortest 

time O(n ^ 3), space O(1)

'''

def naive_shortest_substring(str1, str2):
    n = len(str1)
    min_length = float('inf')
    result = ""
    
    for i in range(n):
        for j in range(i, n):
            
            sub = str1[i : j + 1]
            
            if is_subsequence(sub, str2):
                if len(sub) < min_length:
                    min_length = len(sub)
                    result = sub
                break
            
    return result

# helper function that checks if target is a subsequence of sub 
def is_subsequence(sub, target):
    it = iter(sub)
    return all(char in it for char in target)

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

'''
statement: given a string s and an integer k, find the length of the longest substring 
in s, where all characters are identical, after replacing, at most, k characters with any 
other lowercase English character

algorithm:
- iterate over input string using 2 pointers
- in each iteration
    - add new character into hash map if not already present or increment if present 
    - slide window 1 step forward if number of replacements required in current exceeded limit 
    - if current window longest, update length of longest substring w same character 
- return length of longest substring w same character 

time O(n) where n = length of input string, space O(1)   
'''
def longest_repeating_character_replacement(s, k):
    string_length = len(s)
    length_max_substring = 0 # length of longest substring same characters after replacement  
    start = 0 
    character_frequency = {} # hash map to store frequency of all characters in current window 
    most_freq_char = 0 
    
    # iterate over input string using sliding window pattern
    for end in range(string_length):
        # check if new character in hash map
        if s[end] not in character_frequency:
            character_frequency[s[end]] = 1 # adding new character to frequency map 
        else: 
            character_frequency[s[end]] += 1
        
        # update most frequency character 
        most_freq_char = max(most_freq_char, character_frequency[s[end]])
        
        # if number of replacements in current window exceeded limit, slide window 1 step forward 
        if end - start + 1 - most_freq_char > k:
            character_frequency[s[start]] -= 1 
            start += 1 
    
        # if current window is longest so far, store window length as length of max substring 
        length_max_substring = max(end - start + 1, length_max_substring)
            
    # return length of max substring w same characters after replacement(s)
    return length_max_substring

'''
naive algorithm for longest repeating character replacement: iterate over each character of 
string to form all possible substrings; explore possible substrings starting from that position;
calculate number of required replacements to make all characters identical using nested loop;
if count is less than or equal to k and length of substring is longer than previous longest 
identical character substring, update length

time O(n ^ 3), space O(n)
'''
def naive_longest_repeating_character_replacement(s, k):
    n = len(s)
    max_length = 0 
    
    # iterate over each character as starting piont 
    for start in range(n):
        for end in range(start, n): 
            char_count = {} # frequency of character in substring 
            max_freq = 0 
            
            # count character frequencies in substring s[start: end + 1]
            for i in range(start, end + 1):
                char_count[s[i]] = char_count.get(s[i], 0) + 1 
                max_freq = max(max_freq, char_count[s[i]])
                
            # number of replacements needed to make all characters same 
            length = end - start + 1 
            if length - max_freq <= k: 
                max_length = max(max_length, length)
    
    return max_length

'''
statement: given two strings, s and t, find the minimum window substring in s, 
which has the following properties:

    - it is the shortest substring of s that includes all of the characters 
      present in t
    - it must contain at least the same frequency of each character as in t
    - the order of the characters does not matter here

note: if there are multiple valid minimum window substrings, return any one of them

algorithm: sliding window used to eliminate cost of iterating over each substring separately; 
search for shortest substring of s that contains all characters of t; once initial window in s 
that contains all of t found -> slide window in order to find shortest 

time O(n + m) where n = s length and m = t length, space O(1)
'''
def min_window(s: str, t: str) -> str:
    if not t:
        return ""
    
    # dictionaries to store req char counts and current window char counts 
    req_count = {} # characters in 't' and their corresponding frequencies 
    window = {} # track frequency of 't' characters in current window 
    
    # populate req count with character frequencies of t 
    for character in t:
        req_count[character] = req_count.get(character, 0) + 1

    # variables to indicate whether to increase/decrease size of sliding window 
    current = 0 # incremented when char whose freq in window hash map matches freq in req count
    required = len(req_count) # stores size of req count 
    
    # result variables to track best window 
    result = [-1, -1] # stores start/end indices of min window 
    result_length = float("inf") # length of min window 
    
    # sliding window pointers   
    left = 0
    for right in range(len(s)):
        char = s[right]
        
        # if char is in 't' update window count     
        if char in req_count:
            window[char] = window.get(char, 0) + 1

            # update current if freq of char in window matches required frequency 
            if window[char] == req_count[char]:
                current += 1 
        
        # contract window while all required characters present 
        while current == required:
            # update result if current window smaller than previous best 
            if (right - left + 1) < result_length:
                result = [left, right]
                result_length = (right - left + 1)
            
            # shrink window from left 
            left_char = s[left]
            if left_char in req_count:
                # decrement count of left char in window 
                window[left_char] -= 1 
                # if left char freq in window less than required, update current 
                if window[left_char] < req_count[left_char]:
                    current -= 1 
            left += 1 # moving left pointer to shrink window 
    
    # return min window if found, empty string otherwise 
    return s[result[0]: result[1] + 1] if result_length != float("inf") else ""
            
''' 
naive solution to min window substring problem: find all possible substrings of s, 
ID shortest substring that contains all characters of t with corresponding frequencies 
equal to or greater than those in t 

time O(n ^ 2), space O(n)
'''
from collections import Counter

def naive_min_window(s: str, t: str) -> str:
    # return empty string if t empty 
    if not t:
        return ""
    
    # get frequency count of characters in 't' 
    req_count: dict[str, int] = Counter(t)
    
    # variables to track best window 
    result: str = ""
    result_length: int = float('inf')
    
    n: int = len(s)
    
    # generate all substrings and check if they contain 't'
    for i in range(n):
        for j in range(i, n):
            window: str = s[i : j + 1] # extract substring 
            window_count: dict[str, int] = Counter(window) # frequency count of the substring
            
            # chekc if substring contains all characters of 't' with required frequency
            if all(window_count[char] >= req_count[char] for char in req_count):
                # update result if current window smaller 
                if len(window) < result_length:
                    result = window
                    result_length = len(window)
    
    return result

'''
statement: given string 'input_str' return length of longest substring without 
repeating characters 

algorithm: modified sliding window that can grow to look for window that corresponds 
to longest substring
- traverse input string 
- use hash map to store elements along with their respective indices 
    - if current element present in map, check presence in current window; if present
      end of current window and start of next found; check if longest window seen and update
    - store current element in hash map w key as element and value as current index 
- length of longest substring with distinct characters at traversal end, return value 

time O(n) where n = input string length, space(1)
'''
def find_longest_substring_v1(input_str):
    if len(input_str) == 0:
        return 0
    
    # initialize empty hash map
    last_seen_at = {}
    # variables to track character indices and window start 
    window_start, longest, window_length = 0, 0, 0
    
    # traverse string character by character
    for index, value in enumerate(input_str):
        # store current character in hash map if not already there
        if value not in last_seen_at:
            last_seen_at[value] = index # use index as value in map 
        else: # repeating character found
            # check if if current element occurs before/after window start 
            if last_seen_at[value] >= window_start:
                window_length = index - window_start
                # update longest substring seen so far if current window greater 
                if longest < window_length:
                    longest = window_length
                # update window start to previous current char location and increment
                window_start = last_seen_at[value] + 1  

            # update last occurrence of element in hash map 
            last_seen_at[value] = index
    
    index += 1
    
    # update longest substring length and starting index 
    if longest < index - window_start:
        longest = index - window_start
        
    return longest 

def find_longest_substring(input_str):
    if len(input_str) == 0:
        return 0 
    
    last_seen_at = {} # store last seen index of each character 
    window_start = 0 # left boundary of sliding window 
    longest = 0 
    
    for index, value in enumerate(input_str):
        # if char in dictionary and within current window 
        if value in last_seen_at and last_seen_at[value] >= window_start:
            longest = max(longest, index - window_start)
            # move window start to next position after previous occurrence of char
            window_start = last_seen_at[value] + 1 

        # update latest index of char in dict 
        last_seen_at[value] = index
    
    # final update: compare longest length w last window after exiting loop
    return max(longest, len(input_str) - window_start)
'''

naive approach to longest substring without repeating characters: explore all possible 
substrings, checking for repeated characters, longest returned 

time O(n ^ 3), space(min(m,n))

'''
def find_longest_substring_naive(input_str):
    n = len(input_str)
    longest = 0 
    
    for i in range(n):
        for j in range(i, n):
            substring = input_str[i : j + 1]
            if is_unique(substring):
                longest = max(longest, j - i + 1)
    return longest

def is_unique(substring):
    return len(set(substring) == len(substring))

'''
Minimum Size Subarray Sum

statement: given an array of positive integers, nums, and a positive integer, target, 
find the minimum length of a contiguous subarray whose sum is greater than or equal to 
the target. If no such subarray is found, return 0

algorithm: traverse array using sliding window, calculate sum of elements in it, and
compare sum with target value; if sum greater than or equal to target value, store this
window size; repeat process to find min size subarray 

time O(n), space O(1)
'''
def min_sub_array_len(target, nums):
    # initialize window size with max possible value 
    window_size = float("inf")
    
    start = sum = 0 
    
    # iterate over input array
    for end in range(len(nums)):
        # add element of array in sum 
        sum += nums[end]
        
        # if sum great than or equal to target
        if sum >= target:
            # find current window size 
            curr_subarray_size = (end + 1) - start
            # compare previous window size w current -> store smaller value in window size
            window_size = min(window_size, curr_subarray_size)
            # remove elements from window start 
            sum -= nums[start]
            start += 1 
    
    # if window size not equal to positive infinity, return it
    if window_size != float('inf'):
        return window_size
    
    # otherwise, return 0
    return 0 

'''
Maximum Average Subarray I

statement: given an array of integers nums, and an integer k, return the 
maximum average of a contiguous subarray of length k

algorithm:
1. calculate sum of first k elements and stores as current/max sum 
2. slide window 1 element at a time over array 
3. for each new element that enters window, subtract leaving element and add new
   element to current sum -> meaning no complete recalculations required 
4. update max sum w current sum if value of current greater 
5. return max average = max sum / k

time O(n) where n = number of elements of nums array, space O(1)

'''

def find_max_average(nums, k):
    # initialize current and max sum with sum of first k elements 
    current_sum = max_sum = sum(nums[:k])
    
    # slide window by updating current sum using new element and removing old one 
    for i in range(k, len(nums)): # start from kth element 
        # subtract element leaving window, add new element entering 
        current_sum += nums[i] - nums[i - k]
    
        # update max sum if current sum exceeds max
        max_sum = max(max_sum, current_sum)
    
    # return max average by dividing max sum by k 
    return max_sum / k 

'''
Diet Plan Performance 

statement: a dieter consumes calories[i] calories on the i-th day; given an integer k, the 
dieter reviews their calorie intake over every sequence of k consecutive days (from calories[i] 
to calories[i + k -1] for all 0 <= i <= n-k); for each sequence, they calculate T, the total 
calories consumed over those k days:

    - if T is less than lower, the dieter performs poorly and loses 1 point
    - if T is greater than upper, the dieter performs better and gains 1 point
    - if T is between lower and upper (inclusive), the dieter's performance is 
      normal, and their points remain the same

the dieter starts with zero points; return the total points after the dieter follows this routine 
for all calories.length days; the total points can be negative

algorithm: sliding window allows current sum calculation w/out recalculating sum from scratch for 
each new sequence; maintain running sum of current k days window; move 1 day forward ->
- outgoing / + incoming

time O(n) where n = length of array, space O(1)
'''
def diet_plan_performance(calories, k, lower, upper):
    # start with 0 points 
    points = 0 
    
    # calculate sum of calories for k days 
    current_sum = sum(calories[:k])
    
    # evaluate initial window: compare sum with lower/upper thresholds to update points 
    if current_sum < lower:
        points -= 1
    elif current_sum > upper:
        points += 1 
    
    # slide window forward  across rest of days 1 day at a time 
    for i in range(k, len(calories)):
        # update window sum: subtract outgoing element / add new element 
        current_sum += calories[i] - calories[i - k]
    
        # update points based on new sum for each consecutive window
        if current_sum < lower:
            points -= 1
        elif current_sum > upper:
            points += 1  
    
    # return total points after processing all sequences of k days 
    return points

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
Fruit Into Baskets

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

return the maximum number of fruits you can collect following the above rules 
for the given array of fruits

algorithm: use sliding window to manage range of trees being considered, starts from 
small window and expands window as more trees added to allow max fruit collection, if 
fruit types grows to over 2 -> reduce window size from left until valid     

time O(n) where n = total number of fruit trees, space O(1)
'''

def total_fruit(fruits):
    # create dictionary to track count/frequency of each fruit type in current window
    baskets = {}
    # max number of fruits collected so far 
    collected = 0  
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
        
        # track current window size and update max number of fruits collected if current is greater 
        collected = max(collected, right - left + 1)
    
    # return max count after processing all trees 
    return collected          

'''
Contains Duplicate II

statement: you are given an integer array, is, and an integer k - determine whether 
two distinct indices, i and j, are in the array, such that is[i] == is[j] and the 
absolute difference between i and j is at most k - return TRUE if such indices exist; 
otherwise, return FALSE

algorithm: maintain sliding window of size k to track elements within limited range using set; 
iterate -> check if current element in set -> duplicate in range -> return True; otherwise add
to set; remove oldest element if length of set exceeds k -> ensures set contains elements within 
valid range

time O(n) where n = length of array, space O(min(n, k)) space occupied by set = size of current sliding window
'''
def contains_nearby_duplicate(nums, k):
    # create set to track elements within range k 
    seen = set()
    
    # iterate through array
    for i in range(len(nums)):

        # check if current element already exists in set, return True if so  
        if nums[i] in seen:  
            return True # indicates duplicate found within range k 
       
        # add to set if not already there 
        seen.add(nums[i])
        
        # if set size exceeds k, remove oldest element to keep k latest elements 
        if len(seen) > k: 
            seen.remove(nums[i - k])
    
    # if no duplicate iounrange(len(d, r))eturn False     
    return False
