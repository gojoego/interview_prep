'''
hash map/hash table
-data structure that stores key-value pairs
-provides way to efficiently map keys to values for quick retrieval of value w/ given key 
-use hash function behind scenes to compute index or hash code for each key 
-index determines where corresponding value will be stored in underlying array 
-hash functions and collision resolution strategies aid in determining time complexities 

methods
-insert(key, value): key/value pair inserted into hash map -> hash function computes index 
based on key, index used to determine location in hash map where value stored, collision 
resolution strategy in case different keys hash to same index (chaining or open addressing),
worst case time O(n)
-search(key): hash function applied to key to compute index and retrieve value from hash map,  
then value stored at index returned, worst case time O(n)
-remove(key): removing key/value pair typically involves finding index based on key's hash and 
then removing value stored at that index, worst case time O(n)

examples
1. two sum 
2. word count 
3. find 4 elements a,b,c,d such that a+b=c+d
4. divide array into pairs whose sum divisible by 2

does your problem match this pattern? yes, if...
-data access: repeated fast access during algo
-pair-wise relation: store relationship between 2 sets of data to compute result, key/value pair 

real-world problems
-telecommunications 
-e-commerce
-file system 

'''

# design HashMap data structure with constructor(), put(key,value), get(key) and remove(key)
# time O(N), N = total number of possible keys, space O(K + M), K = key space size, M = number of unique keys inserted
class Bucket:
    def __init__(self): 
        # initialize empty list to store key/value pairs 
        self.bucket = []
    
    def get(self, key):
        # iterate through each key/value pair in bucket 
        for (k, v) in self.bucket:
            # if key matches provided key, return corresponding value 
            if k == key:
                return v
        
        # if key not found, return -1
        return -1 
    
    def update(self, key, value):
        # flag to indicate whether key found in bucket 
        found = False
        
        # iterate through each key/value pair in bucket 
        for i, kv in enumerate(self.bucket):
            # if key matches key of current key/value pair
            if key == kv[0]:
                # update value of key/value pair 
                self.bucket[i] = (key, value)
                
                # set flag to True, indicating that key found
                found = True
                break
        
        # if key not found in bucket, add it along with its value
        if not found:
            self.bucket.append((key, value))
    
    def remove(self, key):
        # iterate through each key/value pair in bucket 
        for i, kv in enumerate(self.bucket):
            # if key matches key of current key/value pair 
            if key == kv[0]:
                # delete key/value pair from bucket 
                del self.bucket[i]
                # exit loop as key has been removed 
                break

class DesignHashMap():
    # use the constructor below to initialize hash map based on the keyspace
    def __init__(self):
        # choose prime number for key space size (preferably large one)
        self.key_space = 2069 
        # create array and initialize it with empty buckets equal to key space size 
        self.bucket = [Bucket()] * self.key_space
        
    # implement supporting functions     
    # function to add key/value pair to hash map 
    def put(self, key, value):
        # generate hash key by taking modulus of input key with key space size 
        hash_key = key % self.key_space
        self.bucket[hash_key].update(key, value)
    
    # function to retrieve value associated with given key from hash map
    def get(self, key):
        hash_key = key % self.key_space
        return self.bucket[hash_key].get(key)

    # function to remove key/value pair from hash map given key 
    def remove(self, key):
        hash_key = key % self.key_space
        self.bucket[hash_key].remove(key)

# given numerator and denominator, return fraction in string format, time and space O(pd), pd = lowest denominator
def fraction_to_decimal(numerator, denominator):
    # declare result variable to store result in form of string 
    result = ""
    # declare hash map to store remainder as key length as value 
    remainder_map = {}
    
    # if numerator 0, return 0
    if numerator == 0:
        return '0'
    
    # if numerator or denominator negative
    if (numerator < 0) ^ (denominator < 0):
        result += '-' # append minus character to result string
    
        # make numerator and denominator positive 
        numerator = abs(numerator)
        denominator = abs(denominator)

    # calculate quotient and remainder from given numerator and denominator 
    quotient = numerator/denominator
    remainder = (numerator % denominator) * 10 
    # append quotient to result 
    result += str(int(quotient))
    
    # check if remainder 0, return result 
    if remainder == 0:
        return result
    else: # if remainder not 0, append . to result
        result += "."
        
        # start loop until remainder 0
        while remainder != 0: # check if remainder in hash map
            # if remainder exists in hash map, create recurring decimal from fraction
            if remainder in remainder_map.keys():
                beginning = remainder_map.get(remainder)
                left = result[0: beginning]
                right = result[beginning: len(result)]
                result = left + "(" + right + ")"
                return result
        
            # add to hash map if remainder doesn't exist in hash map 
            remainder_map[remainder] = len(result)
            
            quotient = remainder / denominator
            
            result += str(int(quotient))
            
            remainder = (remainder % denominator) * 10 
        
        return result
    
def naive_fraction_to_decimal(numerator, denominator):
    result = "" # declare result variable to store result as string 
    
    if numerator == 0: # return string 0 if numerator is 0
        return '0'
    
    # append "-" to result if negative 
    if (numerator < 0) ^ (denominator < 0):
        result += '-'
    
    # convert parameters to positive 
    numerator = abs(numerator)
    denominator = abs(denominator)
    
    # calculate quotient and remainder
    quotient = numerator // denominator
    remainder = numerator % denominator * 10
    result += str(quotient)
    
    # return result if no remainder
    if remainder == 0:
        return result
    
    # append decimal point to result if remainder 
    result += "."
    
    remainder_array = [] # stores remainders
    decimal_part = ""
    
    # loop until remainder 0 or repetition found
    while remainder != 0:
        # check if remainder in array
        if remainder in remainder_array:
            # find start of repeating part
            repeat_index = remainder_array.index(remainder)
            non_repeating_part = decimal_part[:repeat_index]
            repeating_part = decimal_part[repeat_index:]
            result += non_repeating_part + "(" + repeating_part + ")"
            return result
        
        # if not found, add remainder to array 
        remainder_array.append(remainder)
        
        # get next digit and update remainder
        next_digit = remainder // denominator
        decimal_part += str(next_digit)
        remainder = (remainder % denominator) * 10 
    
    # append non-repeating decimal part to result 
    result += decimal_part

    return result   


'''
problem statement: for the given stream of message requests and their timestamps as input, 
implement a logger rate limiter system that decides whether the current message request is displayed,
decision depends on whether the same message has already been displayed in the last S seconds, 
decision is FALSE if so, as this message is considered a duplicate, return TRUE otherwise 

'''
from collections import deque

class RequestLoggerNaive:
    def __init__(self, time_limit):
        # queue to process incoming requests
        self.queue = deque()
        # set to ID and remove duplicates
        self.request_set = set()
        self.limit = time_limit

    # function decides whether the message request should be accepted or rejected, time and space O(n)
    def message_request_decision(self, timestamp, request): # event driven algo 
        # every incoming message prompts ID and removal of message w timestamp more than
        # S seconds older than new timestamp
        while self.queue and timestamp - self.queue[0][0] >= self.limit:
            # remove from both queue and set 
            old_timestamp, old_request = self.queue.popleft()
            self.request_set.remove(old_request)
        
        # after time limit expiry check, check if duplicate
        if request in self.request_set:
            return False
        else:
            # add to queue and request set, then return True  
            self.queue.append((timestamp, request))
            self.request_set.add(request)
            return True 

class RequestLogger:
    def __init__(self, time_limit):
        # initialize requests hash map 
        self.requests = {}
        self.limit = time_limit

    # function decides whether the message request should be accepted or rejected, time O(1), space O(n)
    def message_request_decision(self, timestamp, request):
        # check each arriving request if new or repeated by checking hash map 
        # repeated request -> check if there's been S seconds since last request 
        # if so, update timestamp for specific message in hash map 
        if request not in self.requests or timestamp - self.requests[request] >= self.limit:
            # incoming messages = keys, timestamps = values, key/value pairs to store in hash map 
            self.requests[request] = timestamp
            return True
        else: # if repeat request arrives before time limit expires, reject it 
            return False

'''
statement: given 2 distinct arrays, nums1 and nums2, where nums1 is a subset of nums2
find all greater elements for nums1 values in corresponding places of nums2, find next 
greater element present on right side of x in nums2 and store in ans array 

'''

# time O(n), space O(n)
def next_greater_element(nums1, nums2):
    # empty stack 
    stack = []
    # empty hash map
    map = {} 
    
    # iterate over nums2
    for current in nums2: 
        # while stack not empty and current element greater than top stack element 
        while stack and current > stack[-1]: # compare each element w top stack element 
            # if current nums2 element greater than top element, pop top element
            # put key/value pair in hash map, popped element is key, current element is value 
            map[stack.pop()] = current
        
        # push current element onto stack
        stack.append(current) 
        
        # repeat process until nums2 completely iterated 
    
    # iterate over remaining elements in stack, pop and set values to -1 in map 
    while stack:
        map[stack.pop()] = -1
    
    ans = []
        
    # iterate over nums1
    for num in nums1:
        # for each element, append corresponding value from hash map to new array ans 
        ans.append(map[num])
        
    # return ans array as final result 
    return ans

# time O(n1 x n2), space O(1)
def naive_next_greater_element(nums1, nums2):
    result = []
    
    # for each element in nums1, search for next greater in nums2 
    for x in nums1:
        # find index of x in nums2 
        found = False
        for i in range(len(nums2)):
            if nums2[i] == x:
                found = True
                # search for next greater from index forward 
                next_greater = -1
                for j in range(i + 1, len(nums2)):
                    if nums2[j] > x:
                        next_greater = nums2[j]
                        break
                result.append(next_greater)
                break
    
        # if element not found in nums2, append -1 
        if not found:
            result.append(-1)
            
    return result

# check if 2 strings isomorphic, fixed mapping exists for characters in both, time O(n), space O(1) 
def is_isomorphic(string1, string2):
    # hash map to store mapping from string1 to string2
    str1_str2 = {}
    # hash map to store mapping from string2 to string1
    str2_str1 = {}
    
    for i in range(len(string1)):
        # if char in hash map and mapped to diff char than one to be mapped, algo terminates, return False
        char1 = string1[i]
        char2 = string2[i]
        
        # if char1 exists in hash map and has different mapping, return False
        if char1 in str1_str2 and str1_str2[char1] != char2:
            return False
        
        # if char2 exists in hash map and has different mapping, return False
        if char2 in str2_str1 and str2_str1[char2] != char1:
            return False
        
        # check if character in hash map before storing mappings of characters 
        # map char of one string to another and vice versa 
        str1_str2[char1] = char2
        str2_str1[char2] = char1

    # if all mappings valie in both hash maps, return True 
    return True

from collections import defaultdict
from typing import List

# statement: identify duplicate files in list of directory info paths, each group has 2+ duplicates, output list 
# with groups and paths to duplicates, time and space O(M x N) where M = # values in list, N = items in paths  
def find_duplicate(paths):
    # dictionary to store content as key and list of file paths as value 
    file_map = defaultdict(list)
    
    # iterate over input string/each path path in input array
    for path in paths:
        # split all values by space/splitting directory path and files 
        values = path.split(' ')
        
        # iterate through each file in current dictionary path 
        for i in range(1, len(values)):
            # split every spliced value further by '(' to separate file contents and their names 
            name_content = values[i].split('(')
            
            # extract content part 
            content = name_content[1][:-1]
            
            directory = values[0]
            file_name = name_content[0]
            
            file_path = f"{directory}/{file_name}"
            
            # check if file name in hash map as key
            # put file path and name in list associated with that hash map key 
            # no entry in map -> create one w file contents as key, file path w/ file name in list (hash map value)
            file_map[content].append(file_path)
    
    result = [] # list to store result groups of duplicate file paths 

    # for every item in map, check if key has more than 1 value in associated list and return every such value
    for paths in file_map.values():
        # only add to result if 1+ files w same content
        if len(paths) > 1:
            result.append(paths)
            
    return result