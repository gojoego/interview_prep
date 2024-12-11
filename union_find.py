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
class UnionFind:
    
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
    union_find = UnionFind(grid)    

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

def main():

    def print_grid(grid):
        for i in grid:
            print("\t", i)

    grid1 = [
        ['1', '1', '1'],
        ['0', '1', '0'],
        ['1', '0', '0'],
        ['1', '0', '1']
    ]

    grid2 = [
        ['1', '1', '1', '1', '0'],
        ['1', '0', '0', '0', '1'],
        ['1', '0', '0', '1', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '1', '0', '1', '1']
    ]

    grid3 = [
        ['1', '1', '1', '1', '0'],
        ['1', '0', '0', '0', '1'],
        ['1', '1', '1', '1', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '1', '0', '1', '1']
    ]

    grid4 = [
        ['1', '0', '1', '0', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '0', '1', '0', '1'],
        ['0', '1', '0', '1', '0'],
        ['1', '0', '1', '0', '1']
    ]

    grid5 = [
        ['1', '0', '1'],
        ['0', '0', '0'],
        ['1', '0', '1']
    ]

    inputs = [grid1, grid2, grid3, grid4, grid5]
    num = 1
    for i in inputs:
        print(num, ".\tGrid:\n", sep = "")
        print_grid(i)
        print('\n\tOutput :', num_islands(i))
        print('-' * 100)
        num += 1


if __name__ == "__main__":
    main()