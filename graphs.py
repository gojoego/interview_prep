'''

graph
-nonlinear data structure that represents connections between entities 
-entities represented as vertices or nodes 

basic components and common properties of graphs
-vertex or node: fundamental unit of graph, usually represented as point that holds info/data
-edge: connection between 2 nodes, may have direction (directed edge) or not (undirected edge)
-weight: cost or value associated with connection/edge
-degree: number of edges incident to node 
-in-degree: number of edges coming towards node (directed graphs)
-out-degree: number of edges going away from node (directed graphs)
-adjacent nodes: nodes directed connected to each other by edge 
-path: sequence of nodes where each adjacent pair connected by edge 
-cycle: path that starts and ends at same node 

types of graphs
-undirected: edges have no direction, representing 2-way relationship between nodes 
-directed: edges have direction, 1 way relationship between nodes 
-weighted: each edge has numerical value assigned to it, indicating cost, distance, or
some other relevant measure associated with that connection 
-cyclic: contains at least 1 cycle, path that starts/ends at same node 
-acyclic: no cycles 

graph representation
-adjacency list: collection of lists, each list corresponds to node and contains its neighbors, 
weighted graphs also have weights stored with corresponding nodes, default weight 1 is omitted 
-adjacency matrix: 2D array where each cell matrix[i][j] represents edge between nodes i and j,
value of matrix[i][j] equals 1 or weight with weighted graphs if there's an edge otherwise 0 

graph traversal: depth-first search (DFS)
-explore as far along as possible along 1 path before turning back 
-from chosen source node move from neighbor to neighbor until no neighbors 
-then start backtracking, in which algorithm goes one step back and checks 
for remaining neighbor nodes until all nodes reachable from source visited 
-stacks used for implementation:
    1. initialize stack
    2. choose source node and push onto stack 
    3. while stack isn't empty, pop node, explore unvisited neighbors, push onto stack, mark visited
    4. continue until reaching node with no unvisited neighbors, then backtrack by popping stack 
    5. repeat until empty stack, ensuring all connected nodes visited 
    
graph traversal: breadth-first search
-explore graph in layers, 1 level at a time 
-begins at chosen source and visits immediate neighbor nodes marking as visited 
-moves on to visit neighbors of those nodes before proceeding to next level of neighbors 
-continues until all nodes reachable from source visited 
-queues used to implement algorithm
    1. initialize empty queue
    2. choose source node and enqueue 
    3. loop that dequeues node from front, visits neighbors, marks visited 
    4. neighbors subsequently enqueued
    5. queue ensures nodes at current level processed before progressing to next 
    6. iterative process continues until queue empty, signifying all reachable nodes visited 

graph algorithms
-Dijkstra's: variation of DFS, finds shortest path between 2 nodes in weighted graph 
-Bellman-Ford: variation of BFS, finds shortest paths in weighted graph, even w/ negative edge weights
-Floyd-Warshall: variation of BFS, finds shortest paths between all pairs of nodes in weighted graph
-topological sorting: similar to DFS and orders nodes in directed acyclic graph to satisfy dependencies 
-Prim's: finds minimum spanning tree of connected, undirected graph 
-Krushal's: also finds minimum spanning tree of connected, undirected graph 

examples: 
    1. find if path exists in graph
        a. undirected: BFS and queues 
        b. directed: BFS and queues 
    2. find if cycle exists in graph
        a. undirected: DFS and stacks
        b. directed: DFS and stacks 

-find if cycle exists in graph 

does my coding interview question follow the graph pattern? 
-yes if there are relationships between elements

real-world problems
-routing in computer networks
-flight route optimization 
-epidemic spread modeling 
-recommendation systems

'''

from queue import PriorityQueue
from collections import defaultdict

# create function to find minimum time to get from k to all other nodes 

# naive approach, Bellman-Ford algorithm, time O(n * e), space O(n + e) where n = nodes and e = edges 
def naive_network_delay_time(times, n, k):
    # initialize delay times to infinity for all nodes except starting node k
    delay_times = {i: float('inf') for i in range(1, n + 1)}
    delay_times[k] = 0 # starting node delay time 0 
    
    # relax all edges up to n - 1 times
    for _ in range(n - 1):
        # iterate over all edges
        for source, dest, delay in times:
            # if source node reached and traveling through improves delay time 
            if delay_times[source] != float('inf') and delay_times[source] + delay < delay_times[dest]:
                delay_times[dest] = delay_times[source] + delay
                
    # find max delay from starting node k to all other nodes 
    max_delay = max(delay_times.values())
    
    # if some nodes still unreachable, return - 1
    return max_delay if max_delay < float('inf') else -1 

# optimized approach using Dijkstra's algorithm, time O(logN), space O(N + E) where N = number nodes, E = number edges
def network_delay_time(times, n, k):
    # create adjacency dictionary to store info of nodes and their edges 
    adjacency = defaultdict(list)
    for source, dest, delay_time in times: # store source as key with destination and time as values 
        adjacency[source].append((dest, delay_time))
    
    # create visited set to track nodes that have already been processed 
    visited = set()
    # priority queue to store nodes and their delay times 
    pri_queue = PriorityQueue()
    pri_queue.put((0, k)) # add source node with delay time of 0
    
    delays = 0 # stores delay time 
    
    # process nodes from priority queue by first visiting node with smallest 
    # delay time and updating delay time if necessary
    while not pri_queue.empty():
        time, node = pri_queue.get() # get minimum time node from queue 
        
        if node in visited: # if node already visited continue to next iteration 
            continue
        
        visited.add(node) # mark node as visited 
        delays = max(delays, time) # update delay time if need be
        neighbors = adjacency[node]
        
        # add unvisited neighbors of processed node to priority queue with their new delay time
        for neighbor in neighbors:
            neighbor_node, neighbor_time = neighbor
            if neighbor_node not in visited:
                new_time = time + neighbor_time
                pri_queue.put((new_time, neighbor_node))
    
    # return delay time if all nodes have been processed, return -1 otherwise 
    if len(visited) == n:
        return delays
    
    return -1 
     
    
    # Driver code
def main():
    time = [
                [[2, 1, 1], [3, 2, 1], [3, 4, 2]],
                [[2, 1, 1], [1, 3, 1], [3, 4, 2], [5, 4, 2]],
                [[1, 2, 1], [2, 3, 1], [3, 4, 1]],
                [[1, 2, 1], [2, 3, 1], [3, 5, 2]],
                [[1, 2, 2]]
            ]

    n = [4, 5, 4, 5, 2]
    k = [3, 1, 1, 1, 2]

    for i in range(len(time)):
        print(i + 1, ".\t times = ", time[i], sep="")
        print("\t number of nodes 'n' = ", n[i], sep="")
        print("\t starting node 'k' = ", k[i], "\n", sep="")
        print("\t Minimum amount of time required = ", network_delay_time(time[i], n[i], k[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
    
    

