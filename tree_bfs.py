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

# given binary tree, return zigzag level order traversal, time and space O(n) 
from collections import deque

def zigzag_level_order(root):
    # if root NULL, return empty list 
    if root is None:
        return []
    
    # creating empty list to store results 
    results = [] # initialize 2D array to store output 
    
    # creating deque with root node as only element
    dq = deque([root])
    
    # initialize order flag reverse to False, indicates direction of traversal 
    reverse = False
     
    # iterate over deque as long as it is not empty 
    while len(dq):
        # getting size of current level 
        size = len(dq)
        # insert empty list at end of results list 
        results.insert(len(results), [])
        
        # traverse nodes in current level -> for each dequed element, add its children to deque 
        # from front if value of reverse True, otherwise, append them to back of deque
        for i in range(size):
            # check direction of traversal -> deque elements, enque from back if value of reversed True
            # otherwise enque them from front and maintain order of nodes 
            # for each level, append array of its nodes to results array  
            if not reverse:
                # if direction left to right, pop node from start/left and add to current level 
                node = dq.popleft()
                results[len(results) - 1].append(node.data)
                
                # add left and right child nodes of current node to deque
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            else:
                # if direction is right to left, pop node from back/right and add to current level
                node = dq.pop()
                results[len(results) - 1].append(node.data)
                
                # add right and left child nodes of current node to deque 
                if node.right:
                    dq.appendleft(node.right)
                if node.left:
                    dq.appendleft(node.left)
        
        reverse = not reverse
              
    return results

'''

statement: given perfect binary tree, connect all nodes of same hierarchical level by setting next pointer 
to its immediate right its immediate right node, next pointers all NULL 

perfect binary tree: all levels completely filled with nodes and leaf nodes at same level 

'''

class EduTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

class EduBinaryTree:
    def __init__(self, nodes):
        self.root = self.createBinaryTree(nodes)

    def createBinaryTree(self, nodes):
        if len(nodes) == 0:
            return None

        # Create the root node of the binary tree
        root = EduTreeNode(nodes[0].data)

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
                curr.left = EduTreeNode(nodes[i].data)
                queue.put(curr.left)

            i += 1

            # If there are more nodes in the list and the next node is not None,
            # create a new TreeNode object for its right child, set it as the right child
            # of the current node, and add it to the queue
            if i < len(nodes) and nodes[i] is not None:
                curr.right = EduTreeNode(nodes[i].data)
                queue.put(curr.right)

            i += 1

        # Return the root of the binary tree
        return root
    
    # Function to find the given node and return its next node
    def get_next_node(root, nodeData):
        queue = [root]  # Use a queue for level-order traversal

        while queue:
            current = queue.pop(0)

            if current.data == nodeData:
                return current.next

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return None

# time O(n), space O(1)
def populate_next_pointers(root):
    # check if root node empty, return NULL if so 
    if not root:
        return root
    
    # traverse each level of tree starting from leftmost node 
    mostleft = root
    while mostleft.left:
        # initialize current node as mostleft node of current level 
        current = mostleft
        
        # loop through current level 
        while current:
            # for each node on current level, connect current node to its immediate right node using next pointer 
            current.left.next = current.right
            
            # if there is a next node on same level
            if current.next:
                # connect current node's right child to left child of its next node
                current.right.next = current.next.left 
            
            # move to next node on same level
            current = current.next 
        
        # move down to next level 
        mostleft = mostleft.left 
            
    # return modified root node 
    return root

from queue import Queue

def naive_populate_next_pointers(root):
    if not root: 
        return None
    
    # create empty queue to perform BFS
    queue = Queue()
    # enqueue root node into queue 
    queue.put(root)
    
    # perform level-order traversal 
    while not queue.empty():
        # initialize variable for number of nodes in current level 
        level_size = queue.qsize()
        previous_node = None
        
        # traverse through all nodes at current level 
        for i in range(level_size):
            current_node = queue.get()
            
            # set next pointer of previous node 
            if previous_node:
                previous_node.next = current_node
                
            previous_node = current_node
            
            # enqueue left and right children
            if current_node.left:
                queue.put(current_node.left)
            if current_node.right:
                queue.put(current_node.right)
    
    return root

def display_tree(root, level=0, prefix="Root: "):
    if not root:
        print("\t" * level + prefix + "None")
        return
    
    # Print the current node
    print("\t" * level + prefix + str(root.data))
    
    # Recursively print the left and right children, increasing the level (indentation)
    if root.left or root.right:
        if root.left:
            display_tree(root.left, level + 1, "L--- ")
        else:
            print("\t" * (level + 1) + "L--- None")
        
        if root.right:
            display_tree(root.right, level + 1, "R--- ")
        else:
            print("\t" * (level + 1) + "R--- None")

