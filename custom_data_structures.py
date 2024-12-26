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


'''

# create new entry in dictionary by copying previous value at snap_id to snap_id + 1 

# increment value of snap_id by 1 to keep track of number of snapshots taken 

# return index of snapshot taken recently, which is index at snap_id - 1

import copy 

class SnapshotArray:
    # constructor
    def __init__(self, length):
        self.snap_id = 0
        self.node_value = dict()
        self.node_value[0] = dict()
        self.ncount = length 

    # function set_value sets the value at a given index idx to val 
    def set_value(self, idx, val):
        if idx < self.ncount:
            self.node_value[self.snap_id][idx] = val
    
    # This function takes no parameters and returns the snap_id.
    # snap_id is the number of times that the snapshot() function was called minus 1. 
    def snapshot(self):
        self.node_value[self.snap_id + 1] = copy.deepcopy(self.node_value[self.snap_id])
        self.snap_id += 1
        return self.snap_id - 1 
    
    # Function get_value returns the value at the index idx with the given snap_id.
    def get_value(self, idx, snap_id):
        if self.node_value[self.snap_id + 1] >= 0 and idx < self.ncount:
            return self.node_value[snap_id][idx] if idx in self.node_value[snap_id] else 0
        else:
            return None
