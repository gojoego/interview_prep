'''
custom data structures 
-modified version of existing data structure: array, linked list, hash map, tree, etc  
-reusable if represented as classes 

examples
1. custom stack w getMin() in O(1) complexity 
2. two sum 
3. implement arbitrary state persistence of multiple workers nodes to improve fault
   tolerance of distributed processing system 
4. enhance stack to enable popping highest value in O(1)

does your problem match this pattern? yes, if conditions met
-modification of existing data structure, like min stack or max frequency stack 
-multiple data structures involved 

real world problems
-video games 
-customizing search engines 
-managing car parking 

'''

class LinkedListNode:
    def __init__(self, pair):
        self.second = pair[1]
        self.first = pair[0]
        self.pair = pair
        self.next = None
        self.previous = None
        
class LinkedList:
    # initializes linked list type object 
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0     

    # moves given node to head 
    def move_to_head(self, node):
        if not node:
            return 
        
        if node.previous:
            node.previous.next = node.next 
            
        if node.next:
            node.next.previous = node.previous
            
        if node == self.head:
            self.head = self.head.next 
        
        # insertion at head 
        if not self.head:
            self.tail = node 
            self.head = node
        else:
            node.next = self.head 
            self.head.previous = node 
            self.head = node 
        
    # insert given pair at head 
    def insert_at_head(self, pair):
        new_node = LinkedListNode(pair)
        if not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.next = self.head 
            self.head.previous = new_node
            self.head = new_node
        
        self.size += 1 
    
    def insert_at_tail(self, pair):
        new_node = LinkedListNode(pair)
        if not self.tail:
            self.tail = new_node
            self.head = new_node
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.previous = self.tail 
            self.tail = new_node
        
        self.size += 1
        
    # removes given pair from Linked List 
    def remove(self, pair):   
        i = self.get_head()
        while i:
            if i.pair == pair:
                self.remove_node(i)
                return 
            i = i.next 
    
    # removes given node from Linked List 
    def remove_node(self, node):
        if not node:
            return 
        
        if node.previous:
            node.previous.next = node.next 
        
        if node.next:
            node.next.previous = node.previous
        
        if node == self.head:
            self.head = self.head.next 
        
        if node == self.tail:
            self.tail = self.tail.previous
            if self.tail:
                self.tail.next = None
        self.size = self.size - 1
        del node 
    
    # remove head of linked list 
    def remove_head(self):
        return self.remove_node(self.head)
    
    # remove tail of linked list 
    def remove_tail(self):
        return self.remove_node(self.tail)
    
    # return head of linked list 
    def get_head(self):
        return self.head 
    
    # return tail of linked list 
    def get_tail(self):
        return self.tail 
'''
statement: implement a Snapshot Array with the following properties:

    - constructor (length): constructor that initializes the data structure to hold the 
    specified number of indexes
    - set value (idx, val): property sets the value at a given index idx to value val
    - snapshot(): method takes no parameters and returns the Snap ID, Snap ID is the number 
    of times that the snapshot function was called, less 1, as we start the count at 0, 
    first time this function is called, it saves a snapshot and returns 0, the nth time it 
    is called, after saving the snapshot, it returns n-1
    - get value (idx, Snap ID) method returns value at index in snapshot with given Snap ID

suppose that we have three nodes whose values we wish to track in the snapshot array, 
initially, the value of all the nodes will be 0, after calling the set value (1, 4) 
function, the value of node 1 will change to 4, if we take a snapshot at this point, 
the current values of all the nodes will be saved with Snap ID 0, if we call 
set value (1, 7), the current value for node 1 will change to 7, if we call the get 
value (1, 0) function, we will get the value of node 1 from snapshot 0, that is, 

time: constructor(), get value(idx, snap id), set value(idx, val) -> O(1), snapshot() -> O(n)
space O(n x m), n = number of nodes, m = number of snapshots taken
'''
import copy 

class SnapshotArray:
    # constructor
    def __init__(self, length):
        self.snap_id = 0
        # holds all values w nodes at different times in further subdictionaries
        self.node_value = dict() # keys: snapshot ids, values: dictionaries
        self.node_value[0] = dict() # keys: node ids, values: node values 
        self.ncount = length 

    # function set_value sets the value at a given index idx to val 
    def set_value(self, idx, val):
        if idx < self.ncount:
            self.node_value[self.snap_id][idx] = val
    
    # no parameters and returns snap_id, number of times that the snapshot() function was called minus 1 
    def snapshot(self):
        # create new entry in dictionary by copying previous value at snap_id to snap_id + 1 
        self.node_value[self.snap_id + 1] = copy.deepcopy(self.node_value[self.snap_id])
        # increment value of snap_id by 1 to keep track of number of snapshots taken 
        self.snap_id += 1
        # return index of snapshot taken recently, which is index at snap_id - 1
        return self.snap_id - 1 
    
    # returns the value at the index idx with the given snap_id
    def get_value(self, idx, snap_id):
        # validates existence of snapshot 
        if snap_id < self.snap_id and snap_id >= 0 and idx < self.ncount:
            return self.node_value[snap_id][idx] if idx in self.node_value[snap_id] else 0
        else:
            return None
        
    def __str__(self):
        return str(self.node_value)

# space O(n * m), n = number of snapshots, m = length of array
# time: set_value() O(1), snapshot() O(m), get_value() O(1)
class NaiveSnapshot:
    def __init__(self, length):
        self.snap_id = 0 # current snapshot ID 
        self.array = [0] * length # initialize array with 0s 
        self.snapshots = [] # list to store snapshots / copies of array 
        
    def set_value(self, idx, val):
        self.array[idx] = val
        
    def snapshot(self):
        self.snapshots.append(self.array[:])
        self.snap_id += 1
        return self.snap_id - 1
    
    def get_value(self, idx, snap_id):
        if snap_id < len(self.snapshots):
            return self.snapshots[snap_id][idx]
        return 0
    
'''
statement: implement a data structure that can store multiple values of the same key at different 
timestamps and retrieve the key's value at a certain timestamp, implement TimeStamp class w/ following functions:

    init(): initializes the values dictionary and timestamp dictionary
    set value(key, value, timestamp): stores the key and value at any given timestamp
    get value(key, timestamp): returns the value set for this key at the specified timestamp

note: when a query requests the value of a key at a timestamp that isn't recorded, 
return the value corresponding to the most recent timestamp before the query's timestamp, 
if there are no timestamps before the query's timestamp, return an empty string

time set_value() O(1), binary_search() O(logn), space O(n)
'''
import random
        
class TimeStamp:
    def __init__(self):
        self.values_dict = {} # stores values against specific key 
        self.timestamps_dict = {} # stores timestamps corresponding to same key to track values stored at specific timestamp

    #  set TimeStamp data variables, adds key w value for given timestamp
    def set_value(self, key, value, timestamp):
        # check if given key already exists in values dictionary
        if key in self.values_dict:
            # check if given value of key already exists in values dictionary 
            if value != self.values_dict[key][len(self.values_dict[key]) - 1]:
                # store values for given key in values dictionary 
                self.values_dict[key].append(value)

                # store timestamp for given key in timestamp dictionary
                self.timestamps_dict[key].append(timestamp)
        else:
            # store value and key for given key in values dictionary 
            self.values_dict[key] = [value]
            
            # store timestamp for given key in timestamp dictionary 
            self.timestamps_dict[key] = [timestamp]
    
    # find index of right most occurrence of given timestamp using binary search 
    def search_index(self, n, key, timestamp):
        left = 0
        right = n 
        mid = 0 
        
        while left < right:
            # returns middle of current dictionary
            mid = (left + right) >> 1
            
            # increase index value if required index less than current index, otherwise decrease it 
            if self.timestamps_dict[key][mid] <= timestamp:
                left = mid + 1
            else:
                right = mid
                
        return left - 1

    # Get TimeStamp data variables
    def get_value(self, key, timestamp):
        # in order to get value, verify if given key exists / present in values dictionary
        if key not in self.values_dict:
            # return empty string if item does not exist 
            return ""
        else: 
            # find right most occurrence of given timestamp 
            index = self.search_index(len(self.timestamps_dict[key]), key, timestamp)
            
            # if timestamp exists in timestamp dictionary, return value with that timestamp 
            if index > -1: # verify if timestamp being passed is greater than previous timestamp 
                return self.values_dict[key][index] # return value for respective key and timestamp 
            
            # return empty string if required timestamp less than timestamps that were previously set 
            return ""

class NaiveTimeStamp:
    def __init__(self):
        self.keys = []
        self.values = []
        self.timestamps = []
        
    # set value with corresponding key and timestamp, time O(1) 
    def set_value(self, key, value, timestamp):
        self.keys.append(key)
        self.values.append(value)
        self.timestamps.append(timestamp)
    
    # get value for specific key and timestamp, time O(n)
    def get_value(self, key, timestamp):
        # perform linear search to find value 
        for i in range(len(self.keys) - 1, -1, -1):
            if self.keys[i] == key and self.timestamps[i] <= timestamp:
                return self.values[i]
        return "" # return empty string if no match found 
    
'''
statement: implement an LRU cache class with the following functions:

    init(capacity): initializes an LRU cache with the capacity size
    set(key, value): adds a new key-value pair or updates an existing key with a new value
    get(key): returns the value of the key, or -1 if the key does not exist
    
if the number of keys has reached the cache capacity, evict the least recently used key 
and then add the new key

as caches use relatively expensive, faster memory, they are not designed to store very 
large data sets, whenever the cache becomes full, we need to evict some data from it, there 
are several caching algorithms to implement a cache eviction policy, LRU is a very simple 
and commonly used algorithm, core concept of the LRU algorithm is to evict the oldest data
from the cache to accommodate more data

time O(1). space O(n) where n = size of cache 
'''

class LRUCache:    
    
    def __init__(self, capacity):
        # initializes LRU cache with capacity size 
        self.cache_capacity = capacity
        self.cache_map = {}
        self.cache_list = LinkedList()

    # returns value of key or -1 if key does not exist 
    def get(self, key):
        found_itr = None
        if key in self.cache_map:
            found_itr = self.cache_map[key]
        # to get value if given key doesn't exist, return -1
        else:
            return -1
        
        list_iterator = found_itr
        
        # move pair to front of list if it exists 
        self.cache_list.move_to_head(found_itr)
        
        # return corresponding value to key
        return list_iterator.pair[1]

    # setting a pair
    def set(self, key, value):
        
        # check if given key already exists in cache hashmap
        if key in self.cache_map: 
            
            found_iter = self.cache_map[key]
            list_iterator = found_iter
            
            # move pair/node corresponding to key to front of list 
            self.cache_list.move_to_head(found_iter)
            
            # update value of node
            list_iterator.pair[1] = value
            return 
    
        # if key does not exist and full cache
        if len(self.cache_map) == self.cache_capacity:
            # evict LRU entry by first getting key of LRU node (first element of each cache entry = key)
            key_temp = self.cache_list.get_tail().pair[0]
            
            # remove last node in list 
            self.cache_list.remove_tail()
            
            # remove entry from cache 
            del self.cache_map[key_temp]
        
        # inserts new element at front of list in constant time 
        self.cache_list.insert_at_head([key, value])
        
        # set value of key as list beginning since we added new element at head of list
        self.cache_map[key] = self.cache_list.get_head()
    
'''
statement: implement a Random Set data structure that can perform the following operations:

    constructor(): initializes the Random Set object
    insert(): takes an integer, data, as its parameter and, if it does not already exist in the set, 
        add it to the set, returning TRUE, if the integer already exists in the set, the function returns FALSE
    delete(): takes an integer, data, as its parameter and, if it exists in the set, removes it, returning TRUE,
        if the integer does not exist in the set, the function returns FALSE
    getRandom(): takes no parameters, returns an integer chosen at random from the set

note: implementation should aim to have a running time of O(1)(on average) for each operation

time O(1), space O(n)
'''
from random import choice

class RandomSet(): 
    # initialize data structure
    def __init__(self):
        # use hash map to track location at which each data element stored in array 
        self.indexor = {} # maps actual value to its index 
        # store data in array
        self.store = [] # store actual values in array 

    # inserts value in data structure, returns True if it did not already contain specified element
    def insert(self, val):
        if val in self.indexor:
            return False
        
        # insert actual value as key and its index as value 
        self.indexor[val] = len(self.store)
        
        # append new value to array 
        self.store.append(val)
        
        return True

    # removes a value from the data structure, returns True if it contained the specified element
    def delete(self, val):
        # use hash map to look up location of element to delete 
        if val in self.indexor:
            # swap last element in array w one to be deleted 
            last, i = self.store[-1], self.indexor[val]
            
            # in hash map, update location of element just moved 
            self.store[i], self.indexor[last] = last, i
            
            # delete key-value pair of target data element from hash map
            del self.indexor[val]
            
            # delete target element from array 
            self.store.pop()
            
            return True
    
        return False

    # choose an element at random from the data structure
    def get_random(self):
        return choice(self.store)
    
class NaiveRandomSet:
    def __init__(self):
        self.store = [] # array to store elements 
    
    def insert(self, val):
        if val in self.store:
            return False
        self.store.append(val)
        return True
    
    def delete(self, val):
        if val in self.store:
            self.store.remove(val) # linear time complexity for finding and removing value
            return True
        return False
    
    def get_random(self):
        if not self.store:
            raise ValueError("Cannot fetch from an empty set")
        return choice(self.store)
    
'''
statement: design a custom stack class, Min Stack, allowing us to push, pop, and retrieve 
the minimum value in constant time, implement the following methods for Min Stack:

    constructor: initializes the Min Stack object
    pop(): removes and returns from the stack the value that was most recently pushed onto it
    push(): pushes the provided value onto the stack
    min Number(): returns the minimum value in the stack in O(1) time

note: time complexity of all the methods above should be O(1)

time O(1) for all operations, space O(n)
'''

class Stack: 
    
    def __init__(self):
        self.stack_list = []
    
    def is_empty(self):
        return len(self.stack_list) == 0
    
    def top(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]
    
    def size(self):
        return len(self.stack_list)
    
    def push(self, value):
        self.stack_list.append(value)
        
    def pop(self):
        if self.is_empty():
            return None
        return self.stack_list.pop()
    
class MinStack:
    # initialize min and main stack here
    def __init__(self):
        self.min_stack = Stack()
        self.main_stack = Stack()

    # after pushing element when pop is called, top element of stack removed and returned 
    def pop(self):
        self.min_stack.pop()
        # returns popped value from main stack 
        return self.main_stack.pop()

    # pushes values into the min stack
    def push(self, value):
        # push input element in stack 
        self.main_stack.push(value)
        
        # if min stack empty or  pushed element less than current minimum value/top value of min stack, update 
        if self.min_stack.is_empty() or value < self.min_stack.top():
            # push new value to min stack 
            self.min_stack.push(value)
        else: # if returned value is same as minimum value, update based on values in stack 
            # keep minimum value at top of min stack 
            self.min_stack.push(self.min_stack.top())
        
    # returns minimum value from stack
    def min_number(self):
        if self.min_stack.is_empty():
            return None
        else:
            return self.min_stack.top()