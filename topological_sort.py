'''

topological sort    
-   pattern used to find valid orderings of elements that have 
    dependencies on or priority over each other 
-   only applicable to directed acyclic graphs (DAGs), no cycles
-   starts with source and ends at sink 
-   source: any vertex with no incoming edge and only outgoing edges
-   sink: any vertex that has only incoming edges and no outgoing edge 

'''

# compilation order - given list of dependency pairs, find order which order classes should be compiled 

from collections import deque

class graph:
    def __init__(self):
        self.graph_list = {}

    def build_graph(self, dependencies):
        for dependency in dependencies:
            parent, child = dependency[1], dependency[0]
            if parent not in self.graph_list:
                self.graph_list[parent] = []
            self.graph_list[parent].append(child)
            
    def initializing_graph(self, dependencies):
        for x in dependencies:
            parent, child = x[1], x[0]
            self.graph[parent], self.graph[child] = [], []
    
    def building_graph(self, dependencies):
        for dependency in dependencies:
            parent, child = dependency[1], dependency[0]
            self.graph[parent].append(child)

def find_compilation_order(dependencies):
    sorted_order = [] # store topological order in array 
    graph = {}
    in_degree = {} # hash map to count in-degrees or incoming edges of vertex 
    # build graph from input using adjacency lists 
    for i in dependencies:
        parent, child = i[1], i[0]
        graph[parent], graph[child] = [], []
        in_degree[parent], in_degree[child] = 0, 0 # store in-degree of each vertex in hash map 
    
    if len(graph) <= 0: # if length of graph is 0, no vertices, return empty list 
        return sorted_order
    
    # build graph from input dependencies and populate in-degrees in hash map
    for dependency in dependencies: 
        parent, child = dependency[1], dependency[0]
        graph[parent].append(child)
        in_degree[child] += 1    
        
    sources = deque() # add sources to a queue 
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)
    
    while sources: # use breadth-first search (BFS) for traversing vertices 
        vertex = sources.popleft() # pop from queue and store node in list, sorted order
        sorted_order.append(vertex) 
        for child in graph[vertex]:
            in_degree[child] -= 1 # decrement in-degrees of node's children by 1 
            if in_degree[child] == 0: # if in-degree of node becomes 0, add to source queue 
                sources.append(child)
                # repeat until all vertices have been visited
    
    if len(sorted_order) != len(graph):
        return []
    
    return sorted_order # return sorted order list   
    
from collections import defaultdict, Counter, deque
    
def alien_order(words):
    adj_list = defaultdict(set) 
    counts = Counter({c: 0 for word in words for c in word})
    
    for word1, word2 in zip(words, words[1:]):
        for c, d in zip(word1, word2):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    counts[d] += 1
                break
        else: 
            if len(word2) < len(word1):
                return ""
    
    result = []
    sources_queue = deque([c for c in counts if counts[c] == 0])
    while sources_queue:
        c = sources_queue.popleft()
        result.append(c)
        for d in adj_list[c]:
            counts[d] -= 1
            if counts[d] == 0:
                sources_queue.append(d)
    if len(result) < len(counts):
        return ""
    return "".join(result)
    # build graph from input using adjacency lists 
    # remove sources (vertices with indegree = 0) from graph and add them to results array
    # decrement indegree of sources children by 1 
    # repeat until all nodes visited 
    return result