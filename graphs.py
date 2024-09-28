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

# create function that determines complexity of graph, time O(n^2), space O()
def naive_number_paths(n, corridors):
    adjacency = [[0] * n for _ in range(n)] # create adjacency matrix to store edges between rooms 
    
    # populate adjacency matrix with edges from corridors 
    for room1, room2 in corridors:
        adjacency[room1 - 1][room2 - 1] = 1
        adjacency[room2 - 1][room1 - 1] = 1
        
    cycles = 0 # initiate cycle count
    
    # check for all triplets (room1, room2, room3)
    for room1 in range(n):
        for room2 in range(room1 + 1, n):
            for room3 in range(room2 + 1, n):
                # check if (room1, room2), (room2, room3), (room3, room1) connected
                if adjacency[room1][room2] and adjacency[room2][room3] and adjacency[room3][room1]:
                    cycles += 1
                    
    return cycles

def number_of_paths(n, corridors): 
    # create adjacency matrix to store rooms as keys and its neighbor rooms as corresponding values
    neighbors = defaultdict(set)
    # create counter to store number of cycles 
    cycles = 0
    
    # start iterating over corridors and store neighbors of room1 and room2 in matrix
    for room1, room2 in corridors:
        neighbors[room1].add(room2)
        neighbors[room2].add(room1)
    
        # take intersection of neighbors of room1 and room2 and add length of result to counter 
        cycles += len(neighbors[room1].intersection(neighbors[room2]))
    
    # repeat process until iterated over all corridors 
    
    return cycles
    
# given reference of node in graph with data and list of neighbors, create deep copy of graph 
# properties: undirected (edges of graph bidirectional), connected (path will always exist between any 2 nodes)
# deep copy: new instance of every node created with same data as in original graph 

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

# time O(n + m), space O(n)
def clone(root):
    # initialize empty dictionary to keep track of cloned nodes 
    nodes_completed = {}
    
    # call recursive function to clone graph starting from root node
    return cloner(root, nodes_completed)

def cloner(root, nodes_completed):
    # if root node None, return None 
    if root == None:
        return None
    
    # create new Node with same data as root of original graph 
    cloned_node = Node(root.data)
    # add root node and its clone to hash map
    nodes_completed[root] = cloned_node
    
    # iterate through neighbors of root node 
    for p in root.neighbors:
        # retrieve value of key p in nodes completed hash map
        # if exists, assign corresponding cloned node to x
        # checks if neighbor node p has already been cloned  
        x = nodes_completed.get(p)
        # if neighbor not cloned yet, recursively clone it
        if not x: 
            cloned_node.neighbors += [cloner(p, nodes_completed)]
        # if neighbor already cloned, add to new node's neighbor 
        else:
            cloned_node.neighbors += [x]
             
    # return root of new graph
    return root

# determine if graph is a valid tree (all nodes connected w no cycle), time O(n), space O(n)
def valid_tree(n, edges):
    # if number of edges not equal to number of nodes - 1, return false
    if len(edges) != n - 1: # more edges, indicates cycle, less -> not all nodes connected
        return False
    
    # otherwise, create adjacency list to represent graph 
    # initialize empty list of lists (each inner list corresponds to node and stores neighbors)
    adjacency = [[] for _ in range(n)]
    
    for x, y in edges:
        adjacency[x].append(y)
        adjacency[y].append(x)
    
    # initialize set to track visited nodes, 0th node
    visited = {0} 
    # stack to track nodes, 0th node
    stack = [0]
    
    # perform DFS and pop node from stack 
    while stack:
        node = stack.pop()
    
        # iterate through neighbors from adjacency array/neighbors of popped node
        for neighbor in adjacency[node]:
            # if neighbor node not visited, mark neighbor node as visited and add to stack 
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                
    # if length of set equals number of nodes, return true, else false 
    return len(visited) == n

# prompt: given array "routes", routes[i] -> ith bus repeats, routes have 1+ stations
# source and destination -> return min number of buses from src to dest, return -1 if none 

from collections import deque # https://docs.python.org/3/library/collections.html#collections.deque

# time O(R x S), space O(R x S) where R = total number of routes, S = number of stations
def minimum_buses(bus_routes, src, dest):
    # create adjacency list that maps each station to buses that travel through station 
    adj = {}
    
    for i, stations in enumerate(bus_routes):
        for station in stations:
            if station not in adj:
                adj[station] = []
            adj[station].append(i)
    
    # initialize queue with initial source and bus count of 0
    queue = deque()
    queue.append([src, 0])

    # create set to contain visited routes of bus
    visited_buses = set()
    
    # iterate queue either till empty or destintation station arrived 
    while queue:
        # pop stationand number of buses taken and store in variables 
        station, buses_taken = queue.popleft()
        # if we have reached destination station, return number of buses taken 
        if station == dest:
            return buses_taken # return bus count
        
        # if station in graph, iterate over stations in graph 
        if station in adj: 
            for bus in adj[station]:
                # if not visited, enqueue all stations in that bus route along with incremented bus count
                if bus not in visited_buses: 
                    # visit connecting stations of dequeued station and enqueue connecting stations
                    for s in bus_routes[bus]:
                        # in every iteration, increase bus count if new bus passing through station
                        queue.append([s, buses_taken + 1])
                    visited_buses.add(bus) # mark bus as visited 
    
    # if route not found, return -1 
    return -1

'''
prompt: 

given list airline tickets where tickets[i] = [from, to] represent departure airport
and arrival airport of single flight, reconstruct itinerary in correct order and return it,
all journeys start from "JFK", prioritize smallest lexical order, 
all tickets form at least one valid itinerary, all tickets used once 

'''

from collections import defaultdict

# Hierholzer's algorithm - finding Eulerian path
# time O(|E|log|E/V|), space O(|V| + |E|) where V = number of airports, E = number of flights  
def find_itinerary(tickets):
    # create dictionary with airports as keys, each mapped to list of destinations 
    flight_map = defaultdict(list)
    # initialize list to track reconstructed itinerary 
    result = []
    
    # populate flight map with each departure and arrival 
    for departure, arrival in tickets:
        flight_map[departure].append(arrival)
    
    # sort each list of destinations lexicographically in reverse order 
    for departure in flight_map:
        flight_map[departure].sort(reverse=True)
    
    # start DFS traversal from JFK airport 
    dfs('JFK', flight_map, result)
    
    # return list in reverse order 
    return result[::-1]

def dfs(current, flight_map, result):
    # retrieve list of destinations for current airport from dictionary
    destinations = flight_map[current]
    
    # while there are destinations available, pop next destination from list
    # traverse all destinations in order of their lexicographical sorting 
    while destinations:
        # pop last destination from list (smallest lexicographical order due to reverse sorting)
        next_destination = destinations.pop()
        
        # recursively explore all available flights starting from popped destination
        # recursively perform DFS on next destination 
        dfs(next_destination, flight_map, result) 
    
    # append current airport to result list after all destinations visited 
    result.append(current)