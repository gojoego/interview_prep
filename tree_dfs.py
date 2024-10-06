'''

tree
-undirected
-acyclic
-connected graph where any two vertices connected by exactly 1 path 
-nodes can contain values of any type 

key tree features
-organize data in hierarchical fashion with root node at top and child nodes branching out from it 
-non-linear: elements in tree not arranged sequentially but rather in branching structure 
-search() and insert() time O(logn), n = number of elements 
-multiple strategies to traverse them 

traversal
-naive: starting at root and exploring each branch, time O(n^2)
-dfs: travels along each branch before moving on to another, no nodes revisited, time O(n)

dfs traversal method: preorder 
    1. traverse left subtree recursively
    2. traverse right subtree recursively 
    3. repeat until fully traversed 
    
dfs traversal method: inorder
    1. traverse left subtree recursively
    2. traverse parent node 
    3. traverse right subtree 
    4. repeat until fully traversed

dfs traversal method: postorder
    1. traverse left subtree
    2. traverse right subtree
    3. traverse parent node 
    4. repeat until fully traversed 
    
examples
-path sum: determine if tree contains root to leaf path, preorder traversal
-valid binary tree: inorder traversal, value of current node less than previous 

does your problem match this pattern? yes if...
-tree data structure 
-balanced/low branching factor
-hierarchical structures
-solution near the leaves
-traversal along paths
-explore all possible paths

real world problems
-find products in price range
-dependency resolution 
-syntax tree analysis 

'''

# given root of binary tree, create function to flatten into linked list using TreeNode class
# left pointer NULL, right next node, preorder, complexities: time O(n), space O(1), n = number of nodes
from typing import List
from queue import Queue
def flatten_tree(root):
    if not root:
        return
    
    current = root
    
    while current:
        # for every node, check for left child, if not go to right child
        if current.left:
            last = current.left
            
            # otherwise, find node on rightmost branch of left subtree that does not have right child
            while last.right:
                last = last.right
                
            # once rightmost node found, connect with right child of current node
            last.right = current.right
            # after connecting, set right child of current node to left child of current node 
            current.right = current.left
            # finally, set left child of current node to NULL
            current.left = None
            
        current = current.right
        
    # repeat process until given binary tree becomes flattened 
    return root   

def naive_flatten_tree(root):
    if not root:
        return None
    
    # recursively flatten left and right subtrees
    naive_flatten_tree(root.left)
    naive_flatten_tree(root.right)
    
    # save right subtree
    right_subtree = root.right
    
    # move left subtree to right 
    root.right = root.left
    root.left = None
    
    # find last node in new right subtree
    current = root
    while current.right:
        current = current.right
        
    # attach saved right subtree
    current.right = right_subtree
    
    return root

from collections import deque
def flatten_tree_queue(root):
    if not root:
        return None
    
    # queue to store nodes in preorder traversal
    queue = deque()
    
    # 1 - perform preorder traversal and populate queue 
    preorder_traversal(root, queue)

    # 2 - reconstruct tree using queue of nodes
    return reconstruct_tree(queue)

def preorder_traversal(node, queue):
    if not node:
        return
    queue.append(node) # visit current node
    preorder_traversal(node.left, queue) # traverse left
    preorder_traversal(node.right, queue) # traverse right

def reconstruct_tree(queue):
    if not queue:
        return None
    previous = queue.popleft() # start with first node
    while queue:
        current = queue.popleft() # dequeue next node 
        previous.left = None # left pointer to None
        previous.right = current # right pointer to next node
        previous = current # move to next node
    # ensure last node has no right pointer
    previous.left = None
    previous.right = None
    
    return previous

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, nodes):
        self.root = self.createBinaryTree(nodes)
        
    def createBinaryTree(self, nodes):
        if len(nodes) == 0:
            return None
        
        # create root node of binary tree
        root = TreeNode(nodes[0].data)
        
        # create queue and add root node to it
        queue = Queue()
        queue.put(root)
        
        # start iterating over list of nodes starting from second node
        i = 1
        while i < len(nodes):
            # get next node from queue
            current = queue.get()
            
            # if node not None, create new TreeNode object for its left child
            # set it as left child of current node and add it to queue
            if nodes[i] is not None:
                current.left = TreeNode(nodes[i].data)
                queue.put(current.left)
            i += 1
            
            # if there are more nodes in list and next node is not None, create new TreeNode object 
            # for right child, set it as right child of current node and add to queue 
            if i < len(nodes) and nodes[i] is not None:
                current.right = TreeNode(nodes[i].data)
                queue.put(current.right)
            i += 1
        
        return root
        # function to find a node given the value stored in the node
        
    def find(self, value):
        q = deque([self.root])
        while q:
            currentNode = q.popleft()
            if currentNode:
                if currentNode.data == value:
                    return currentNode
                q.append(currentNode.left)
                q.append(currentNode.right)
            if all(val == None for val in q):
                break
        return None    
    
def display_tree(node, level=0, prefix="Root: "):
# """Displays the binary tree structure."""
    if not node:
        print("\t" * level + prefix + "None")
        return
    print("\t" * level + prefix + str(node.data))
    if node.left or node.right:
        display_tree(node.left, level + 1, "L--- ")
        display_tree(node.right, level + 1, "R--- ")
    
# given binary tree, compute length of tree's diameter (length of longest path between 2 nodes)
# may pass through root, length of path between 2 nodes rep by number of edges between
# time O(n), space O(n) where n = number of nodes 
def diameter_of_binaryTree(root):
    # variable for diameter
    diameter = 0
    if not root:
        return 0
    
    # compute height of tree and max diameter
    # start traversing tree from root node
    _, diameter = diameter_helper(root, diameter)
    
    # after traversing whole tree, return diameter value since it's length of tree's diameter
    return diameter

def diameter_helper(node, diameter):
    if node is None:
        return 0, diameter
    else:
        # for each node, calculate height of left and right subtree
        left_height, diameter = diameter_helper(node.left, diameter)
        right_height, diamater = diameter_helper(node.right, diameter)

        # for each node, update diameter using formula: max(diameter, left height + right height)
        diamater = max(diamater, left_height + right_height)
        
        # use larger one
        return max(left_height, right_height) + 1, diamater

# serialize given binary tree to file and deserialize it back to a tree, make sure original and deserialized identical
# serialize: write tree to file, deserialize: read from file and reconstruct tree in memory 

MARKER = "M"
m = 1

# space O(h) where h = height of tree, time O(n) where n = number of nodes in binary tree
def serialize(root): # function to serialize tree into list of integers 
    stream = []
    recursive_serializer(root, stream)
    return stream

# perform depth-first traversal and serialize individual nodes to stream
def recursive_serializer(node, stream):
    global m
    # adding marker to stream if node is None
    # serialize marker to represent NULL pointer that helps deserialize tree
    if node == None:
        stream.append(MARKER + str(m))
        m += 1
        return 
    
    # adding node to stream
    stream.append(node.data)
    
    # doing pre-order tree traversal for serialization 
    recursive_serializer(node.left, stream)
    recursive_serializer(node.right, stream)
    
# deserialize tree using preorder traversal    
# space O(h) where h = height of tree, time O(n) where n = number of nodes in binary tree
def deserialize(stream):
    stream.reverse()
    node = recursive_deserializer(stream)
    return node

def recursive_deserializer(stream):
    # pop last element from list
    value = stream.pop()
    
    # return None when marker encountered 
    if type(value) is str and value[0] == MARKER:
        return None
    
    # create new Binary Tree Node for every non-marker node using preorder traversal 
    node = TreeNode(value)
    
    # doing pre-order tree traversal for deserialization 
    node.left = recursive_deserializer(stream)
    node.right = recursive_deserializer(stream)

    # return node if it exists    
    return node

# given root node of binary tree, transform tree by swapping each node's left and right subtrees
# time O(n) where n = number of nodes, space O(h) where h = height of tree

# global variables to support step-by-step printing 
change = 0
master_root = None

def mirror_binary_tree(root): # function to mirror binary tree
    global change, master_root 
    
    # base case: end recursive call if current node null
    if not root:
        return None
    
    # perform post order traversal on left child of root node
    if root.left:
        mirror_binary_tree(root.left)
        
    # perform post order traversal on right child of root node
    if root.right:
        mirror_binary_tree(root.right)
    
    # swap left and right children of root node
    # swap left and right nodes at current level
    root.left, root.right = root.right, root.left
        
    return root

# given root of binary tree, return max sum of any non-empty path 
# path: sequence of nodes in which each pair of adjacent nodes have connecting edge
# node can only be included in path once at most, including root is not compulsory 
# time O(n) where n = number of nodes, space O(h) where h = height of tree 

global max_sum 

def max_path_sum(root):
    global max_sum
    
    # initialize max sum to negative infinity
    max_sum = float('-inf')
    
    max_contribution(root)
    
    return max_sum
    
def max_contribution(root):
    global max_sum
    
    if not root:
        return 0
    
    # for leaf node, determine its contribution equal to its value
    # sum of left and right subtree
    max_left = max_contribution(root.left)
    max_right = max_contribution(root.right)
    
    left_subtree = 0
    right_subtree = 0
    
    # max sum on left and right sub-trees of root 
    if max_left > 0:
        left_subtree = max_left
    if max_right > 0:
        right_subtree = max_right

    # value to start new path where root is highest root 
    value_new_path = root.data + left_subtree + right_subtree
    
    # update max sum if above greater than previous max sum
    # update max sum if it's better to start a new path 
    max_sum = max(max_sum, value_new_path)
    
    # determine node's contribution as its value + greater of contributions of l/r children
    # return max contribution if continue same path 
    return root.data + max(left_subtree, right_subtree)

# given array of integers nums, sorted in ascending order, construct height-balanced BST from this array
# height-balanced BST: difference of heights of subtrees of any node not more than 1, can be multiple
# time O(n), space O(logn)
def sorted_array_to_bst(nums):
    return array_bst_converter(nums, 0, len(nums) - 1)

def array_bst_converter(nums, low, high):
    # base case: if low is less than, there are no more elements to add to BST 
    if (low > high):
        return None
    
    # find middle element of list using low and high indexes, initialized to 0 and last index 
    mid = low + (high - low) // 2 # can also use (low + high)//2 but maybe not work for large arrays
    
    # create root node of tree from calculated middle element
    root = TreeNode(nums[mid])
    
    # using left and right subarrays from low to mid - 1 and mid + 1 to high, create left/right subtrees
    # recursively add elements in nums[low:mid-1] to left of subtree of root 
    root.left = array_bst_converter(nums, low, mid - 1)
    # recursively add elements in nums[mid+1:high] to right subtree of root 
    root.right = array_bst_converter(nums, mid + 1, high)
    
    # after traversing complete array, return root of newly created tree
    return root
    
# create binary from 2 int arrays, one being a preorder traversal and the other inorder tranversal, time O(n), space O(n)
def build_tree(p_order, i_order):
    # explicitly using List object to pass p_index by reference because in python
    # Pass-by-object-reference is used and simple variable is not an object 
    p_index = [0]
    
    # using hash map to store inorder list to reduce time complexity of search to O(1)
    mapping = {}
    
    # iterate through inorder list and map each value to index
    for i in range(len(p_order)):
        mapping[i_order[i]] = i 
        
    return tree_builder(p_order, i_order, 0, len(p_order) - 1, mapping, p_index)

def tree_builder(p_order, i_order, left, right, mapping, p_index):
    # if left is more than right, no more nodes left to construct
    if left > right:
        return None
    
    # select current element from preorder list using p_index
    current = p_order[p_index[0]]
    
    # increment preorder index variable to prepare for next recursive call
    p_index[0] += 1
    
    # create new tree node with selected element of preorder list as its data 
    root = TreeNode(current)
    
    # if node has no children then return 
    if left == right:
        return root
    
    # find index of selected element in inorder list and store it in in_index 
    in_index = mapping[current]
    
    # recursively build left subtree of root by calling function on elements 
    # before in_index in inorder list (left to in_index + 1)
    root.left = tree_builder(p_order, i_order, left, in_index - 1, mapping, p_index)
    
    # recursively build right subtree of root by calling function on elements 
    # after in_index in inorder list (in_index + 1 to right)
    root.right = tree_builder(p_order, i_order, in_index + 1, right, mapping, p_index)
    
    return root

# given root of binary tree that has n nodes, return right side view in form of list 
# right side view - data of nodes visible when viewed from right side
# time O(n) where n = number of nodes, space O(h) where h = tree's height 
def right_side_view(root):
    # return empty list if root NULL
    if root is None:
        return []
    
    # initialize list to store result
    rside = []
     
    # apply DFS starting from root node and 0th level 
    dfs(root, 0, rside)
    
    # after DFS completed, return list 
    return rside

def dfs(node, level, rside): # applying depth-first search 
    # at each visited node, if length of list equal to current tree level 
    # aka level is equal to rside length 
    if level == len(rside):
        # add data of node to list 
        rside.append(node.data)
        
    # iterate over child nodes of current node (first right, then left)
    for child in [node.right, node.left]:
        if child:   # for each child, call DFS recursively
            dfs(child, level + 1, rside)
            
# given root node of binary tree with n nodes, find lowest common ancestor of two of its node, p and q
# lowest common ancestor: lowest node in tree that has both p and q as descendents 
# time O(n) where n = number of nodes, space O(h) where h = height of binary tree 
class Solution:
    def __init__(self):
        self.low_com_anc = None
    
    def lowest_common_ancestor(self, root, p, q):
        self.lca_finder(root, p, q)
        return self.low_com_anc   
    
    # helper function to find lowest common ancestor recursively
    def lca_finder(self, current_node, p, q):
        # if current node does not exist
        if not current_node:
            return False
        
        # initialize 3 tracking variables to track if either input nodes have been found
        left, right, mid = False, False, False
        
        # check if current node one of input nodes, set one of track variable to TRUE
        if p == current_node or q == current_node:
            mid = True
             
        # store results of left and right subtrees in remaining 2 tracking variables  
        # traverse left child of input binary tree using DFS 
        left = self.lca_finder(current_node.left, p, q) 
        
        # if lca not found, traverse right subtree
        if not self.low_com_anc:
            right = self.lca_finder(current_node.right, p, q)
        
        # if any two of three tracking variables are TRUE at node, means that 
        # this is the lowest common ancestor of binary tree 
        if mid + left + right >= 2:
            self.low_com_anc = current_node 
        
        # return true if any of the tracking variables true
        return mid or left or right
    
    def opt_lca(self, root, p, q):
        self.opt_lca_finder(root, p, q)
        return self.low_com_anc
    
    def opt_lca_finder(self, current_node, p, q):
        # base case: return False if node is None
        if not current_node:
            return False
        
        # check if current node one of the input nodes 
        mid = current_node == p or current_node == q
        
        # recursively search left and right subtrees 
        left = self.opt_lca_finder(current_node.left, p, q)
        right = self.opt_lca_finder(current_node.right, p, q)
        
        # if two of the three flags (left, right, mid) TRUE, current node LCA
        if mid + left + right >= 2:
            self.low_com_anc = current_node
        
        # return TRUE if current node or either subtree contain p or q
        return mid or left or right
    
'''
given root of binary tree, check if its valid BST

valid BST:
-left subtree of node contains only nodes with keys less than node's key
-right subtree of node contains only nodes with keys greater than node's key 
-both l/r valid BSTs

time O(n), space O(n) where n = number of nodes

'''
import math

def validate_bst(root):
    # explicitly using List object to pass prev by reference b/c Pass-by-object-reference used 
    # and simple variable not object in Python 
    # initialize prev variable with negative infinity
    previous = [-math.inf]
    return validator(root, previous) 
    
# start inorder traversal of binary tree
def validator(root, previous):
    # if all nodes of binary tree have been traversed and value of each node 
    # greater than value of prev, return TRUE
    if not root:
        return True
    
    # if left subtree no valid BST, return False
    if not validator(root.left, previous):
        return False
    
    # if value of current node smaller than or equal to value of prev, return FALSE
    if root.data <= previous[0]: # not valid BST
        return False
    
    # otherwise, assign value of current node to prev 
    previous[0] = root.data
    
    # continue traversal of binary tree
    return validator(root.right, previous)

'''
prompt: given nested list of integers, nested_list, where each element either int or 
list, return sum of each integer in nested_list multiplied by its weight

weight: max_depth minus depth of integer plus one 

depth: number of nested lists it is contained within 

time O(m + n), space O(m), m = number of nested lists, n = number of integers contained within nested list
'''

def weighted_depth_sum(nested_list):
    # calculate max depth
    max_depth = find_max_depth(nested_list)
    # call recursive function to calculate weighted sum
    return sum_calculator(nested_list, 0, max_depth)

# recursive function to calculate max depth 
def find_max_depth(nested_list):
    max_depth = 0
    # use DFS to traverse each nested list
    for object in nested_list:
        # if nested object is a list with length greater than 0
        if not object.is_integer() and len(object.get_list()) > 0:
            # increment depth at each level to find max_depth 
            max_depth = max(max_depth, 1 + find_max_depth(object.get_list()))
    return max_depth

# use DFS to calculate weighted sum of each integer, starting with depth of 1   
def sum_calculator(nested_list, depth, max_depth):
    # in each recursive call, initialize variable result with 0 to store weighted sum
    result = 0
    
    # for each nested object, if integer -> multiply value by weight and add to result
    for object in nested_list:
        if object.is_integer():
            result += object.get_integer() * (max_depth - depth + 1) # weight = max_depth - depth + 1
        else:
            # if nested object not integer, call recursive function again with nested object 
            # increment depth (depth + 1)
            result += sum_calculator(object.get_list(), depth + 1, max_depth)
    
    # once entire nested_list traversed, return result (weighted sum of all integers)
    return result

def createNestedList(input_list):
    def parseInput(nested_integer, input_list):
        if isinstance(input_list, int):
            nested_integer.set_integer(input_list)
        else:
            for item in input_list:
                child = NestedInteger()
                nested_integer.add(child)
                parseInput(child, item)

    nested_integer = NestedInteger()
    parseInput(nested_integer, input_list)
    return [nested_integer]

class NestedInteger:
    # If no value is specified, initializes an empty list
    # Otherwise, initializes with a single integer equal to the specified value
    def __init__(self, integer=None):
        if integer:
            self.integer = integer
        else:
            self.n_list = []
            self.integer = None 

    # Returns True if this NestedInteger holds a single integer rather than a nested list
    def is_integer(self):
        if self.integer is None:
            return False
        return True

    # Returns the single integer this NestedInteger holds, if it holds a single integer
    # Otherwise, return None if this NestedInteger holds a nested list
    def get_integer(self):
        return self.integer

    #  Sets this NestedInteger to hold a single integer equal to value
    def set_integer(self, value):
        self.n_list = None
        self.integer = value

    # Sets this NestedInteger to hold a nested list and adds the nested integer elem to it
    def add(self, elem):
        if self.integer:
            self.n_list = [] 
            self.n_list.append(NestedInteger(self.integer)) 
            self.integer = None
        self.n_list.append(elem) 

    # Returns the nested list that this NestedInteger holds, if it holds a nested list
    # Otherwise, return None if this NestedInteger holds a single integer
    def get_list(self):
        return self.n_list

# given root node of BST and specific node p, return inorder successor of p node, NULL if none
# inorder successor of p - node with smallest value greater than p.data, time O(n), space O(1)
def inorder_successor(root, p):
    # initialize variable successor to store inorder successor of given node 
    successor = None
    
    # traverse tree and compare p with root at each node 
    while root:
        # if p greater than or equal to root node, shift to right subtree of current node 
        if p.data >= root.data:
            root = root.right
        else: # store root node in successor & shift to left part of root node if p less than root 
            successor = root
            root = root.left
    
    # return successor once traverse completed, will contain inorder successor of given p node 
    return successor

class BinarySearchTree:
    def __init__(self, values):
        self.root = self.createBinaryTree(values)

    def createBinaryTree(self, values):
        if len(values) == 0:
            return None

        # Create the root node of the binary search tree
        root = TreeNode(values[0])

        # Start iterating over the list of values starting from the second value
        for value in values[1:]:
            node = TreeNode(value)
            curr = root
            while True:
                # If the value is less than the current node's value, move to the left child
                if node.data <= curr.data:
                    if curr.left is None:
                        # If the left child is empty, insert the new node here and break the loop
                        curr.left = node
                        break
                    else:
                        # If the left child is not empty, move to the left child and continue the search
                        curr = curr.left
                else:
                    # If the value is greater or equal to the current node's value, move to the right child
                    if curr.right is None:
                        # If the right child is empty, insert the new node here and break the loop
                        curr.right = node
                        break
                    else:
                        # If the right child is not empty, move to the right child and continue the search
                        curr = curr.right

        # Return the root of the binary search tree
        return root

'''
given root of binary tree with n nodes and array queries of size m, determine height of binary tree
after each query, each query reps root of subtree that should be removed from tree, store updated
heights against each query in array and return it 

tree height: number of edges in longest path from root to any leaf node in tree 

-all values in tree unique
-guaranteed that queries[i] will not be equal to value of root 
-queries independent, tree returns to initial state after each query 

time O(n), space O(n)

'''

import collections

def heights_after_queries(root, queries):
    # traverse tree to compute and store depth and height of each node
    node_depth, node_height = {}, {}
    tree_dfs(root, 0, node_depth, node_height)
    
    depth_groups = collections.defaultdict(list) # group nodes by depth, keep 2 top heights
    
    # for each depth level, retain 2 top nodes with highest heights to efficiently
    for value, depth in node_depth.items():
        depth_groups[depth].append((node_height[value], value))
        depth_groups[depth].sort(reverse=True)
        if len(depth_groups[depth]) > 2:
            depth_groups[depth].pop()
     
    result = []
    # traverse tree again and identify depth of node to be removed for each query 
    for q in queries: # remove node, store updated height in result array
        depth = node_depth[q]
        if len(depth_groups[depth]) == 1: # no cousin, path length equals depth -1
            result.append(depth - 1)
        elif depth_groups[depth][0][1] == q: # removed node largest height, look for node with 2nd largest height
            result.append(depth_groups[depth][1][0] + depth)
        else: # look for node with largest height
            result.append(depth_groups[depth][0][0] + depth)   
     
    
    # return result array that has heights of tree after each subtree removal query 
    return result

def tree_dfs(node, depth, node_depth, node_height): # depth = root to node distance, height = node to farthest leaf distance
    if not node:
        return -1
    
    node_depth[node.data] = depth
    # determine new height of tree if highest height node removed
    height = max(tree_dfs(node.left, depth + 1, node_depth, node_height),
                 tree_dfs(node.right, depth + 1, node_depth, node_height)) + 1
    node_height[node.data] = height
    return height


# prompt: given root of binary tree, determine max depth, time and space O(n)
# max depth = count of nodes found on longest path from root to farthest leaf 
from collections import deque

def find_max_depth(root):
    # initialize counter to track max depth seen so far and stack for depth of current branch 
    max_depth = 0
    stack = deque()

    # if current node null, return counter
    if root == None:
        return 0  
    
    # start with root node at depth 1 
    stack.append((root, 1))
    
    while stack:
        node, current_depth = stack.pop()
        if node:
            # if depth of current branch exceeds max depth so far, update 
            max_depth = max(max_depth, current_depth)
            
            # check depth of left and right subtrees and push onto stack
            if node.left:
                stack.append((node.left, current_depth + 1))
            if node.right:
                stack.append((node.right, current_depth + 1))
    
    # when all branches explored, return max depth 
    return max_depth

# prompt: given root of BST and integer value k, return kth smallest value in tree, time and space O(n)
def kth_smallest_element(root, k):
    # start inorder traversal of BST
    stack = deque()
    current = root
    
    # while traversing, decrement k by 1 
    while True: # performing iterative in-order traversal
        while current: # go as far left as possible
            stack.append(current)
            current = current.left
        
        # pop node from stack
        current = stack.pop()
        
        # decrement k (counts number of nodes visited in in-order)
        k -= 1
        # check if k equals 0, return value of current node if so, containing kth smallest element
        if k == 0:
            return current.data
        
        # move to right subtree
        current = current.right
    
    # otherwise, continue traversal of BST 
