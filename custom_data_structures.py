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
        
'''
statement: design a Range Module data structure that effectively tracks ranges of numbers using 
half-open intervals and allows querying these ranges, a half-open interval [left,right) includes 
all real numbers n where left ≤ n < right

implement the RangeModule class with the following specifications:

    constructor(): initializes a new instance of the data structure, time O(1)
    add Range(): adds the half-open interval [left, right) to the ranges being tracked, 
        if the interval overlaps with existing ranges, it should add only the numbers within 
        [left, right) that are not already being tracked, time O(n)
    query Range(): returns true if every real number within interval [left, right) is currently being 
        tracked, and false otherwise, time O(n)
    remove Range(): Removes tracking for every real number within the half-open interval [left, right),
        time O(logn)

space O(n)
'''

class RangeModule():

    # initialize data structure
    def __init__(self):
        self.ranges = []
    
    # helper function to find indexes of ranges that might overlap given interval [left, right)
    def check_intervals(self, left, right):
        min_range = 0
        max_range = len(self.ranges) - 1
        mid = len(self.ranges) // 2
        
        while mid >= 1:
            while min_range + mid < len(self.ranges) and self.ranges[min_range + mid - 1][1] < left:
                min_range += mid 
            while max_range - mid >= 0 and self.ranges[max_range - mid + 1][0] > right:
                max_range -= mid 
            mid //= 2 

        return min_range, max_range
    
    # to add new range
    def add_range(self, left, right):
        # check if list empty or new range completely before or after existing ranges
        if not self.ranges or self.ranges[-1][1] < left:
            # if true, append or insert new range accordingly
            self.ranges.append((left, right))
    
        # if new range does not overlap w first range, insert at beginnging
        if self.ranges[0][0] > right:
            self.ranges.insert(0, (left, right))
            return 
    
        min_range, max_range = self.check_intervals(left, right)
        
        # merge new range w overlapping or touching ranges 
        updated_left = min(self.ranges[min_range][0], left)
        updated_right = max(self.ranges[max_range][1], right)
        
        self.ranges[min_range: max_range + 1] = [(updated_left, updated_right)]

    # to search for range 
    def query_range(self, left, right):
        if not self.ranges:
            return False
        
        # find overlapping ranges, verify if queried range fully contained within found range
        min_range, max_range = self.check_intervals(left, right)
        
        # return result 
        return self.ranges[min_range][0] <= left and right < self.ranges[min_range][1]
    
    # to remove a range
    def remove_range(self, left, right):
        # check if list empty or range to be removed outside of existing ranges
        if not self.ranges or self.ranges[0][0] > right or self.ranges[-1][1] < left:
            return
        
        min_range, max_range = self.check_intervals(left, right)
        updated_ranges = []
        k = min_range
        
        while k <= max_range:
            # add part of current range that is before interval to be removed 
            if self.ranges[k][0] < left:
                updated_ranges.append((self.ranges[k][0], left))
                
            # add part of current range that is after interval to be removed
            if self.ranges[k][1] > right:
                updated_ranges.append((right, self.ranges[k][1]))
            k += 1
        
        # replace overlapping ranges with new ranges
        self.ranges[min_range: max_range + 1] = updated_ranges
        
'''
statement: design a data structure that takes in an array of strings and efficiently computes 
the shortest distance between any two different strings in the array, implement the WordDistance class:

    WordDistance(String[] words_dict): Iinitializes the object with an array of strings
    int shortest(String word1, String word2): returns the shortest distance between word1 
    and word2 in the array of strings
'''

from collections import defaultdict

class WordDistance(object):
    
    # create dictionary to map words to their indexes in input array
    # time and space O(n) where n = number of words in input list 
    def __init__(self, words_dict):
        # initialize dictionary to map each word to its list of indices 
        self.word_indices = defaultdict(list)
        
        # populate dictionary by iterating through input array and recording word positions 
        # build dictionary mapping each word to list of its indices in words dict 
        for index, word in enumerate(words_dict):
            self.word_indices[word].append(index)    

    # time O(m + n) where m and n are lengths of index lists for query words, space O(1) 
    def shortest(self, word1, word2):
        # retrieve index lists for 2 words in shortest distance query 
        indices1, indices2 = self.word_indices[word1], self.word_indices[word2]
        
        # use 2 pointers to compare positions of words
        i = 0
        j = 0 
        min_distance = float('inf')
        
        # iterate through both lists of indices to find minimum distance 
        while i < len(indices1) and j < len(indices2):
            # update minimum distance if smaller one found
            min_distance = min(min_distance, abs(indices1[i] - indices2[j]))
            
            # move pointer with smaller index to continue finding closer word pairs until traversal is complete 
            if indices1[i] < indices2[j]:
                i += 1
            else: 
                j += 1 

        return min_distance
    
'''
statement: design a MyHashSet class without using any built-in hash table libraries and implement 
the following methods in it:

    void add(key): inserts the value key into the HashSet
    bool contains(key): returns TRUE if the key exists in the HashSet, FALSE otherwise
    void remove(key): removes the value key if it exists in the HashSet
    
designing hash set involves addressing 2 main challenges 
- hash function: maps given key to index in storage space, takes integer key and returns its remainder when 
  divided by predefined number, good hash function ensures that keys are evenly distributed across storage
  space, preventing clustering of keys in certain locations, even distribution helps maintain efficient 
  access to stored values 
- collision handling: collisions occur when 2 different keys map to same index, handle collisions via 
  open addressing, 2 choice hashing or separate chaining (each index of storage space or bucket contains 
  BST to store multiple values)
  
time O(log(n/k)), space O(N + K) where N = number of elements stored, K = size of bucket 
'''
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def find(self, node: TreeNode, value: int) -> TreeNode:
        if node is None or value == node.value:
            return node 
        
        return self.find(node.left, value) if value < node.value else self.find(node.right, value)
    
    def insert(self, node: TreeNode, value: int) -> TreeNode:
        if not node: 
            return TreeNode(value)
        
        if value > node.value:
            node.right = self.insert(node.right, value)
        elif value == node.value:
            return node
        else: 
            node.left = self.insert(node.left, value)
        
        return node 
    
    def find_successor(self, node):
        node = node.right 
        while node.left:
            node = node.left 
        return node.value 
    
    def find_predecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.value 
    
    def remove(self, node: TreeNode, key: int) -> TreeNode:
        if not node:
            return None
        
        if key > node.value: 
            node.right = self.remove(node.right, key)
        elif key < node.value:
            node.left = self.remove(node.left, key)
        else: 
            if not (node.left or node.right):
                node = None
            elif node.right:
                node.value = self.find_successor(node)
                node.right = self.remove(node.right, node.value)
            else:
                node.value = self.find_predecessor(node)
                node.left = self.remove(node.left, node.value)
        
        return node

# each bucket uses Binary Search Tree to manage elements within bucket 
class Bucket:
    # initialize empty BST when creating new bucket to store keys that hash to this specific bucket 
    def __init__(self):
        self.bst = BinarySearchTree()

    # add value to bucket 
    def add(self, value):
        self.bst.root = self.bst.insert(self.bst.root, value)

    # remove value from bucket
    def remove(self, value):
        self.bst.root = self.bst.remove(self.bst.root, value)

    # check if bucket contains value 
    def contains(self, value):
        return self.bst.find(self.bst.root, value) is not None

# implement hash set using separate chaining with buckets containing Binary Search Trees (BST)
class MyHashSet:
    # define size of hash table (key_range) and initialize on array of buckets 
    def __init__(self):
        # choose prime number for key space size (preferably large one)
        self.key_range = 769
        # create array and initialize with empty buckets equal to key space size 
        self.bucket_array = [Bucket() for i in range(self.key_range)]

    # hash function to map key to specific bucket index 
    def hash(self, key) -> int:
        # generate hash key by taking modulus of input key with key space size 
        return key % self.key_range
    
    # add key to hash set 
    def add(self, key):
        bucket_index = self.hash(key)
        self.bucket_array[bucket_index].add(key)

    # remove key from hash set
    def remove(self, key):
        bucket_index = self.hash(key)
        self.bucket_array[bucket_index].remove(key)

    # check if hash set contains key 
    def contains(self, key):
        bucket_index = self.hash(key)
        return self.bucket_array[bucket_index].contains(key)

'''
statement: design a custom stack class, Max Stack, that supports the basic stack operations 
and can find the maximum element present in the stack, implement the following methods for Max Stack:

    constructor: initializes the Max Stack object
    void Push(int x): pushes the provided element, x, onto the stack
    int Pop( ): removes and returns the element on the top of the stack
    int Top( ): retrieves the most recently added element on the top of the stack without removing it
    int peekMax( ): retrieves the maximum element in the stack without removing it
    int popMax( ): This retrieves the maximum element in the stack and removes it, if there is more 
        than one maximum element, remove the most recently added one (the topmost)

lazy update: updates to data structures deferred or delayed until needed, instead of applying changes 
immediately, system records update operations and only processes them when necessary 
'''
import heapq

class MaxStack:
    def __init__(self):
        # initialize an empty stack to maintain order elements
        self.stack = []
        # utilize secondary data structure (max-heap) to efficiently track max value
        self.max_heap = []
        self.id_num = 0 # declare an ID tracker
        self.popped = set()  # use a Set to track popped elements by their IDs

    # for each push, add new value to stack and max heap that tracks max value, time O(logn)
    def push(self, x):
        # push the value and its unique ID to both the stack and max-heap
        self.stack.append((x, self.id_num))
        heapq.heappush(self.max_heap, (-x, -self.id_num))  # use negative for max-heap
        self.id_num += 1  # increment the ID for the next element

    # for each pop, remove and return top element of stack, time O(logn)
    def pop(self):
        # ensure we skip over any elements already popped
        # store values with negative signs to facilitate max heap behavior using Python min heap
        while self.stack and self.stack[-1][1] in self.popped:
            self.stack.pop()
        # pop the top element and mark its ID as popped
        num, idx = self.stack.pop()
        self.popped.add(idx)
        return num  # return the value of the popped element

    # for each top, return top element fo stack without removing it, time O(1) 
    def top(self):
        # skip over already popped elements to find the top of the stack
        while self.stack and self.stack[-1][1] in self.popped:
            self.stack.pop()
        return self.stack[-1][0] # return the value of the top element

    # for each peek max, return top element of max tracking structure without removing it, time O(nlogn) 
    def peekMax(self):
        # skip over already popped elements to find the current max in the heap
        while self.max_heap and -self.max_heap[0][1] in self.popped:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]  # return the max value

    # for each pop max, remove and return max calue from max tracking structure, time O(logn)
    def popMax(self): # using stack and heap combo 
        # skip over already popped elements to remove the max value from the heap
        while self.max_heap and -self.max_heap[0][1] in self.popped:
            heapq.heappop(self.max_heap)
        # pop the max element and mark its ID as popped
        num, idx = heapq.heappop(self.max_heap)
        self.popped.add(-idx)
        return -num  # return the max value

# Driver code
def main():
    inputs = [
        [[4, 1, "", ""], ["push", "push", "top", "peekMax"]],
        [[5, 1, 5, "",""], ["push", "push", "push", "pop", "popMax"]],
        [[7, 2, 7, "", "", "", "", "", ""], ["push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]],
        [[-9, -3, -1, "", "", "", ""], ["push", "push", "push", "pop", "top", "popMax", "peekMax"]],
        [[10, 6, "", ""], ["push", "push", "popMax", "top"]],
        [[1, -2, 3, "", "", "", "", ""], ["push", "push", "push", "peekMax", "top", "pop", "peekMax", "popMax"]],
        [[14, "", "", 66, ""], ["push", "top", "peekMax", "push", "pop"]]]
    
    for i in range(len(inputs)):
        print(i + 1, ".\t Starting operations:", sep="")

        # initialize a queue
        max_stack_obj = MaxStack()

        # loop over all the commands
        for j in range(len(inputs[i][1])):
            if inputs[i][1][j] == "push":
                inputstr = inputs[i][1][j] + \
                    "("+str(inputs[i][0][j])+")"
                print("\t\t", inputstr, sep="")
                max_stack_obj.push(inputs[i][0][j])
            if inputs[i][1][j] == "pop":
                inputstr = inputs[i][1][j] + \
                    "("+str(inputs[i][0][j])+")"
                print("\t\t", inputstr, "   returns ",
                      max_stack_obj.pop(), sep="")
            if inputs[i][1][j] == "top":
                inputstr = inputs[i][1][j] + \
                    "("+str(inputs[i][0][j])+")"
                print("\t\t", inputstr, "  returns ",
                      max_stack_obj.top(), sep="")

            if inputs[i][1][j] == "peekMax":
                inputstr = inputs[i][1][j] + \
                    "("+str(inputs[i][0][j])+")"
                print("\t\t", inputstr, "  returns ",
                      max_stack_obj.peekMax(), sep="")
            
            if inputs[i][1][j] == "popMax":
                inputstr = inputs[i][1][j] + \
                    "("+str(inputs[i][0][j])+")"
                print("\t\t", inputstr, "  returns ",
                      max_stack_obj.popMax(), sep="")

        print("-" * 100)

if __name__ == "__main__":
    main()