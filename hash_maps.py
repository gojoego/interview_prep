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
    
    
    
    
    
    