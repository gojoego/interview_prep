'''

union find
-used to group elements into sets based on specified property 
-each set non-overlapping/contains unique elements not present in any other set 
-uses disjoint set data structure (like arrays) to track which set elements belong to 
-each set forms tree data structure 
-has representative element that resides at root of tree 
-every element in tree maintains pointer to parent 
-reps parent pointer points to itself
-pick any element in set and follow parent pointers to reach set rep 

operations on disjoint data structure
-find(v): finds rep of set that contains v, time O(n) 
-union(v1, v2): merges sets containing v1 and v2 into one 

union by rank  
-optimization
-maintain rank for each tree, larger tree sizes mean higher rank 
-attack lower rank trees with higher to ensure shortest possible path to root 
-time O(log(n))

path compression
-update parent of node to point directly to root after each operation 
-reduces lenght of path of node to root
-no need to travel all intermediate nodes 
-time O(log(n))

examples
1. longest consecutive sequence 
2. successor with delete 

does your problem match this pattern? yes, if...
-property-based grouping 
-set combination
-graph data organization 

real-world problems
-image segmentation through regsion agglomeration 
-image manipulation
-network connectivity 
-hex(game)

'''

class UnionFind1:
    
    def __init__(self, n):
        self.parent = [] # parent list 
        self.rank = rank = [1] * (n + 1) # length based on edges 
        for i in range(n + 1):
            self.parent.append(i)
    
    # make found root parent so that no further traversal needed 
    def find_parent(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]
    
    def union(self, v1, v2):
        p1, p2 = self.find_parent(v1), self.find_parent(v2)
        
        if p1 == p2: # indicates redundant edge 
            return False
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1 
            self.rank[p1] = self.rank[p2] + self.rank[p2]
        else: 
            self.parent[p1] = p2
            self.rank[p2] = self.rank[p2] + self.rank[p1]
            
        return True

# time and space O(n)
def redundant_connection(edges):
    
    # declare object of given class and initialize parent list with default values 
    graph = UnionFind1(len(edges))
    
    # traverse edges list from first index to last index 
    for v1, v2 in edges:
        # for each edge, connect 2 nodes by marking them - single connected component
        if not graph.union(v1, v2):
            # if current edge already marked as part of connected component, return current edge 
            return [v1, v2]

from collections import defaultdict

def naive_redundant_connection(edges):
    graph = defaultdict(list)
    for v1, v2 in edges:
        # add edge temporarily to test for cycle 
        graph[v1].append(v2)
        graph[v2].append(v1)
        
        # check for cycle using DFS 
        visited = set()
        if cycle_detector(graph, v1, visited, -1):
            return [v1, v2]
        
    return []

def cycle_detector(graph, current, visited, parent):
    visited.add(current)
    for neighbor in graph[current]:
        if neighbor not in visited:
            if cycle_detector(graph, neighbor, visited, current):
                return True
        elif neighbor != parent:
            return True
    return False 

# given m x n grid, 1 = land, 0 = water, return number of islands, time and space O(m x n)
class UnionFind2:
    
    def __init__(self, grid):
        self.parent = [] 
        self.rank = []
        self.count = 0 
        m = len(grid)
        n = len(grid[0])
        # count occurrences of 1 in grid and store in count 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent.append(i * n + j) # current index 
                    self.count += 1 # increment count 
                else: # cell encountered is 0 
                    self.parent.append(-1)
                self.rank.append(0)
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    # connect all neighboring cell 1s into single component, decrement count
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1
    
    def get_count(self):
        return self.count
    
def num_islands(grid):
    if not grid:
        return 0

    columns = len(grid[0])
    rows = len(grid)
    union_find = UnionFind2(grid)    

    # traverse grid, check if 1s have neighbors top, bottom, left, right 
    for row in range(rows):
        for column in range(columns):
            if grid[row][column] == '1':
                # change value of cell 1 in grid to 0
                grid[row][column] = '0'
                
                if row + 1 < rows and grid[row + 1][column] == '1':
                    union_find.union(row * columns + column, (row + 1) * columns + column)
                if column + 1 < columns and grid[row][column + 1] == '1':
                    union_find.union(row * columns + column, row * columns + column + 1)
    
    count = union_find.get_count()
    
    # at end of traversal, count contains number of islands
    return count 

# given 2D array, return max possible number of stones remove if it can only be removed 
# if it shares either same row or same column, time and space O(n) 
class UnionFind:
    # initialize 2 empty dictionaries, parents and ranks
    def __init__(self):
        self.parents = {}
        self.ranks = {}
    
    # find which group particular element belongs to
    def find(self, coordinate):
        if coordinate != self.parents[coordinate]:
            self.parents[coordinate] = self.find(self.parents[coordinate])
        return self.parents[coordinate]
    
    # join 2 coordinates into single one
    # every coordinate of stones parent of itself and has rank 0
    def union(self, x, y):
        # set parent of each node to itself if not already present in dictionary 
        self.parents.setdefault(x, x)
        self.parents.setdefault(y, y)
        
        # set ranks of each node to 0 if not already in dictionary
        self.ranks.setdefault(x, 0)
        self.ranks.setdefault(y, 0)
        
        # compare ranks of 2 nodes to decide which should be parent 
        if self.ranks[x] > self.ranks[y]:
            self.parents[self.find(y)] = self.find(x)
        elif self.ranks[y] > self.ranks[x]:
            self.parents[self.find(x)] = self.find(y)
        # if ranks equal, choose 1 node as parent and increment ranks 
        else:
            self.parents[self.find(x)] = self.find(y)
            self.ranks[y] += 1

def remove_stones(stones):
    # using offset for y coordinate to avoid possible clash with x coordinates
    offset = 100000
    stone = UnionFind()
    
    for x, y in stones:
        stone.union(x, (y + offset))
        
    groups = set()
    # for each stone, check if it shares row or column with another stone using ranks
    for i in stone.parents:
        # if it does, add it to group that has both of these stones 
        groups.add(stone.find(i))
    
    # find number of groups once all stones grouped 
    num_groups = len(groups)
    
    # return difference between number of stones and number of groups formed 
    return len(stones) - num_groups

def naive_remove_stones(stones):
    stones = set(map(tuple, stones))
    removed_count = 0
    
    while True:
        removed = False
        for stone in list(stones):
            if can_remove(stone, stones):
                stones.remove(stone)
                removed_count += 1 
                removed = True
                break
        if not removed:
            break
        
    return removed_count

def can_remove(stone, stones):
    x, y = stone
    for s in stones:
        if s != stone and (s[0] == x or s[1] == y):
            return True
    return False

# given unsorted array, return longest consecutive element sequence length, time and space O(n)
class UnionFind:
    def __init__(self, nums):
        self.parent = {num: num for num in nums}
        self.size = {num: 1 for num in nums}
        self.max_length = 1
        
    def find(self, num):
        if self.parent[num] != num:
            self.parent[num] = self.find(self.parent[num])
        return self.parent[num]
    
    def union(self, num1, num2):
        x_root = self.find(num1)
        y_root = self.find(num2)
        
        if x_root != y_root:
            if self.size[x_root] < self.size[y_root]:
                x_root, y_root = y_root, x_root
            self.parent[y_root] = x_root
            # update size of connected components
            self.size[x_root] += self.size[y_root]
            self.max_length = max(self.max_length, self.size[x_root])

def longest_consecutive_sequence(nums):
    if len(nums) == 0:
        return 0
    
    union_conseq = UnionFind(nums)
    
    # iterate through each element n in input list 
    for num in nums:
        # check whether next number n + 1 is included in input list 
        if num + 1 in union_conseq.parent:
            # if it is, merge components that contain those numbers into single connected component
            union_conseq.union(num, num + 1)
        
    # return size of longest connected component 
    return union_conseq.max_length

'''
'''