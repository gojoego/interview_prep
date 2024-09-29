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