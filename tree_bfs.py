'''

tree breadth-first search 

tree
-undirected, acyclic graph
-connected where any 2 vertices connected by exactly 1 path 
-nodes can contain values of any data type 

key features that set trees apart from other data structures 
-organize data in hierarchical manner with root node at top and child nodes branching out from it 
-nonlinear -> elements in tree are not arranged sequentially but rather in branching structure 
-time complexity for serach and insert operations in trees typically O(logn), n = number of elements
-time complexity for search and insert ops in arrays and linked lists O(n), n = number of elements 
-multiple ways to traverse 

bfs: traversal method exploring level by level from root node 
-initialization: starting point = root node
-exploring adjacent nodes: explores current level (adjacent nodes) before moving to next 
-traversal strategy: layer by layer, not always left to right 
-node discovery: nodes processed according to search requirements
-stopping condition: terminates when desired node found or all nodes explored 
-data structure: queue used to maintain order of node exploration 

examples:
1. minimum depth of tree 
2. bottom-up level order traversal
3. traverse tree one level at a time and print out node values in same order
4. find shortest path between 2 given nodes
5. connect nodes at same level in binary tree 

does your problem match this pattern? yes, if...
-tree data structure
-not a wide tree
-level by level traversal 
-solution near root (DFS more suitable for leaf exploration)

real-life problems
-file system analysis 
-version control systems, like Git 
-genealogy and evolutionary trees
-traversing DOM tree: traversing DOM structures from single web page via HTML tags,
 traversing web pages via shadow tree for DOM 

'''

# statement: given root, display tree values of nodes while performing level order traversal

from typing import List
from queue import Queue

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

        # Create the root node of the binary tree
        root = TreeNode(nodes[0].data)

        # Create a queue and add the root node to it
        queue = Queue()
        queue.put(root)

        # Start iterating over the list of nodes starting from the second node
        i = 1
        while i < len(nodes):
            # Get the next node from the queue
            curr = queue.get()

            # If the node is not None, create a new TreeNode object for its left child,
            # set it as the left child of the current node, and add it to the queue
            if nodes[i] is not None:
                curr.left = TreeNode(nodes[i].data)
                queue.put(curr.left)

            i += 1

            # If there are more nodes in the list and the next node is not None,
            # create a new TreeNode object for its right child, set it as the right child
            # of the current node, and add it to the queue
            if i < len(nodes) and nodes[i] is not None:
                curr.right = TreeNode(nodes[i].data)
                queue.put(curr.right)

            i += 1

        # Return the root of the binary tree
        return root

from collections import deque

# time and space O(n)
def level_order_traversal_1st(root):
    result = ""
    
    # print None if root is empty 
    if not root:
        result = "None"
        return result
    else: 
        # declaring array of 2 queues
        queues = [deque(), deque()]
        # declare 2 queues, current_queue and next_queue
        current_queue = queues[0]
        next_queue = queues[1]
    
        # push root node to current_queue and set level to 0
        current_queue.append(root)
        level_number = 0
        
        while current_queue:
            # dequeue first element from current_queue and push children in next_queue
            temp = current_queue.popleft()
            result += str(temp.data)
            
            if temp.left:
                next_queue.append(temp.left)
            if temp.right:
                next_queue.append(temp.right)
    
            # if current_queue empty, increase level number and swap 2 queues 
            if not current_queue:
                level_number += 1
                
                if next_queue:
                    result += " : "
                current_queue = queues[level_number % 2]
                next_queue = queues[(level_number + 1) % 2]
            else:
                result += ", "
            # repeat until current_empty 
            
    return result

# time and space O(n)
def level_order_traversal_2nd(root):
    # initialize empty list 
    result = []
    
    # return None for empty tree 
    if not root:
        result = "None"
        return result
    
    # create queue to facilitate BFS
    current_queue = deque()
    # enqueue root node to initiate traversal process  
    current_queue.append(root)
    
    # begin loop that continues until current queue empty 
    while current_queue:
        # determine number of nodes at current level by getting length of current queue 
        level_size = len(current_queue)
        # initialize empty list to store data of nodes at this level 
        level_nodes = []
    
        # iterate over number of nodes in current level 
        for _ in range(level_size):
            # dequeue node from front of queue
            temp = current_queue.popleft()
            # append string representation of node data
            level_nodes.append(str(temp.data))
            
            # enqueue left and right child of node (if any) dequeued from previous step into current queue 
            if temp.left:
                current_queue.append(temp.left)
            if temp.right:
                current_queue.append(temp.right)
        
        # join elements in level nodes into single string and append to result 
        result.append(", ".join(level_nodes))
    
    # joing all level representations stored in result list with ":" as separator and return 
    return " : ".join(result)
