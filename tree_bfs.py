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

from collections import defaultdict

# find vertical order of binary tree when root given, values of nodes from top to bottom in each column ->
# column by column from left to right, more than 1 node in same column/row, return values left to right, time/space O(n) 
def vertical_order(root):
    if root == None:
        return []
    
    # keep track of maximum and minimum column indices
    node_list = defaultdict(list) # hash map where key = index of column and value = list of codes in column 
    min_column = 0
    max_index = 0
    
    # push root into queue 
    queue = deque([(root, 0)]) # keeps track of order of nodes that need to be visited, initialize w root at column 0
    
    # traverse tree, level by level, starting from root node 
    while queue:
        node, column = queue.popleft()
        
        if node is not None:
            temp = node_list[column]
            temp.append(node.data)
            node_list[column] = temp # populate hash map with (index,node) pairs
            
            # get min and max column numbers for tree 
            min_column = min(min_column, column)
            max_index = max(max_index, column)
            
            # push nodes to queue along with their column index 
            # add current node's left and right child into queue 
            # if node has children, assign column index current - 1 to left child & current + 1 to right child
            queue.append((node.left, column - 1))
            queue.append((node.right, column + 1))

    # return node values for each column index, from minimum to maximum 
    return [node_list[x] for x in range(min_column, max_index + 1)]

def naive_vertical_order(root):
    if root is None:
        return []
    
    min_max = [0,0]
    
    find_min_max_columns(root, 0, min_max)
    
    min_column = min_max[0]
    max_column = min_max[1]
    
    result = []
    
    for column in range(min_column, max_column + 1):
        column_nodes = []
        collect_nodes_at_column(root, 0, column, column_nodes)
        if column_nodes:
            result.append(column_nodes)
    
    return result
    
def find_min_max_columns(root, column, min_max):
    if root is None:
        return
    
    min_max[0] = min(min_max[0], column)
    min_max[0] = max(min_max[1], column)
    
    find_min_max_columns(root.left, column - 1, min_max)
    find_min_max_columns(root.left, column + 1, min_max) 
    
def collect_nodes_at_column(root, column, target_column, result):
    if root is None:
        return
    
    if column == target_column:
        result.append(root.data)
        
    collect_nodes_at_column(root.left, column - 1, target_column, result)
    collect_nodes_at_column(root.right, column + 1, target_column, result)
    
# create function that checks a tree for symmetry, time and space O(n)
def is_symmetric(root):
    # create queue and insert root's left and right node
    queue = []
    queue.append(root.left)
    queue.append(root.right)
    
    # start traversing tree from root node
    while queue:
        # in loop, dequeue 2 elements and store in left and right 
        left = queue.pop(0)
        right = queue.pop(0)
        
        # if left and right NULL, continue traversing and dequeue next elements 
        if not left and not right:
            continue
        
        # if any one from left and right NULL, return False
        if not left or not right:
            return False
    
        # if value of left not equal to value of right, return False 
        if left.data != right.data:
            return False
    
        # enqueue left node of left, right node of right, right node of left, left node of right
        queue.append(left.left)
        queue.append(right.right)
        queue.append(left.right)
        queue.append(right.left)
    
    # loop terminates when queue empty, return True 
    return True

'''
prompt: given 2 words, src and dest, and words, return number of words in shortest
transformation sequence from src to dest, return 0 for no sequences 

transformation sequence: every pair differs single character

time and space O(N x M) where N = number of words, M = length of each word 
'''

def word_ladder(src, dest, words):
    # create set from given words for faster lookup
    words_set = set(words)

    # if dest not in set, return 0
    if dest not in words_set:
        return 0
    
    # queue for words to be checked
    queue = []
    # push src word into queue
    queue.append(src)   
    
    # counter to store length of sequence 
    length = 0
    
    # check words until queue empty 
    while queue:
        # increment counter in every iteration
        length += 1
        
        # store length of queue 
        size = len(queue)
        
        # check all words in current level 
        for _ in range(size):
            # pop word from queue
            current = queue.pop(0)
            
            # iterate on each character of popped word 
            for i in range(len(current)):
                alphabet = "abcdefghijklmnopqrstuvwxyz"
                
                # iterate with all possible characters 
                for letter in alphabet:
                    # strings immutable -> create list to replace ith character of popped word 
                    temp = list(current)
                    temp[i] = letter
                    temp = "".join(temp)
                    
                    # check if new word is dest 
                    if temp == dest:
                        # return value of counter once dest word found
                        return length + 1 
                    
                    # find all words in set that differ by 1 character from popped word 
                    # push all such words in queue and remove from set 
                    if temp in words_set:
                        queue.append(temp)
                        words_set.remove(temp)
    
    # repeat until queue empty or destination word found 
    return 0

# given root of perfect binary tree, connect nodes left to right, rightmost connects to first node next level
def connect_all_siblings(root):
    # if tree empty, return Null 
    if root == None:
        return None
    
    # initialize list to act as queue for level-order traversal 
    queue = []
    queue.append(root)
    
    # previous node that will be used to connect to current node 
    previous = None
    
    # traverse each level of tree starting from leftmost node 
    while queue:
        # get current node (dequeue first element)
        current = queue.pop(0)
    
        # connect each node of current level to its immediate right node using next pointer
        # connect rightmost node of current level to first node of immediate next level  
        if previous:
            previous.next = current
            
        # update previous node to be current 
        previous = current
        
        # enqueue left and right children of current node 
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    # ensure last node's next pointer is None 
    if previous:
        previous.next = None
    
    # return root node of tree 
    return root