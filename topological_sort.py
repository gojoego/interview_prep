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
    # build graph from input using adjacency lists
    # step 0: create data structures and find all unique letters 
    adj_list = defaultdict(set) 
    counts = Counter({c: 0 for word in words for c in word}) # counts/stores number of unique letters
    
    # step 1: populate adjacency list and counts 
    for word1, word2 in zip(words, words[1:]): # for each pair of adjacent words 
        for c, d in zip(word1, word2):
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    counts[d] += 1
                break
        else: # check that second word isn't prefix of first 
            if len(word2) < len(word1):
                return ""
    
    # step 2: repeatedly pick off nodes with in-degree 0
    result = []
    sources_queue = deque([c for c in counts if counts[c] == 0])
    while sources_queue:
        # remove sources (vertices with indegree = 0) from graph and add them to results array
        c = sources_queue.popleft()
        result.append(c)
        for d in adj_list[c]:
            counts[d] -= 1 # decrement indegree of sources children by 1
            if counts[d] == 0:
                sources_queue.append(d)
        # repeat until all nodes visited 
        
    # if not all letters in result, indicates cycle and no valid ordering -> return ""
    if len(result) < len(counts): 
        return ""
    
    return "".join(result)

def naive_verify_alien_dictionary(words, order):
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        
        for j in range(min(len(word1), len(word2))):
            position1 = order.index(word1[j])
            position2 = order.index(word2[j])
            
            if position1 < position2:
                break
            elif position1 > position2:
                return False
        
        if len(word1) > len(word2):
            return False
    return True

def verify_alien_dictionary(words, order):
    # if only one word to check, trivial case with not enough input (2 word min) to run algo, return TRUE
    if len(words) == 1:
        return True
    
    # store ranking of each letter from order string in data structure 
    order_map = {} # declare hash map to store characters of words 
    for index, value in enumerate(order): # traverse order and store rank in order map 
        order_map[value] = index
        
    # iterate over 2 adjacent words in words list 
    for i in range(len(words) - 1): # traverse words in array
        for j in range(len(words[i])): # traverse characters in each word 
            
            # if all letters have matched so far but current longer than next one, 2 not in order, return False 
            if j >= len(words[i + 1]): # if words[i + 1] ends before words[i], return FALSE 
                return False
            
            # check if letters in same position in 2 words different 
            if words[i][j] != words[i + 1][j]:
                if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                    return False # return FALSE if characters different in both words and words not in correct order 
                # if characters in both words different and words in correct order, exit and move to next 2 adjacent words 
                break 
            
    # at end of loop, all adjacent words have been examined, which ensure that all words sorted, return TRUE 
    return True

def naive_find_order(n, prerequisites):
    sorted_order = []
    
    # step 1: create list of course with no unmet prereqs 
    courses = set(range(n)) # all courses initially considered as possible 
    
    while courses:
        initial_length = len(sorted_order) # track size to track progress
        
        # find course that has no unmet prereqs
        for course in list(courses):
            can_take = True
            # check if course has any unmet prereqs
            for prereq in prerequisites:
                if prereq[0] == course and prereq[1] not in sorted_order:
                    can_take = False
                    break
            
            # if course has no unmet prereqs, add it to sorted order 
            if can_take:
                sorted_order.append(course)
                courses.remove(courses)
                break
        
        # no progress made indicates cycle
        if len(sorted_order) == initial_length:
            return []
    
    # if we successfully ordered all course, return result 
    if len(sorted_order) == n:
        return sorted_order
    else:
        return []
        
    
def find_order(n, prerequisites):
    sorted_order = [] 
    if n <= 0: # if n smaller or equal to zero, return empty array 
        return sorted_order
    
    # create graph with node for each course and edges representing dependencies
    graph = {i: [] for i in range(n)} # step 1: initialize graph 
    
    # store in-degrees of each node in separate data structure 
    in_degree = {i: 0 for i in range(n)}
    
    # step 2: build graph 
    for prerequisite in prerequisites:
        parent, child = prerequisite[1], prerequisite[0]
        graph[parent].append(child) # add child to parent's list 
        in_degree[child] += 1 # increment child's in-degree 
    
    # step 3: bild all sources or nodes with 0 in-degrees
    sources = deque()
    
    # traverse in in-degree using key 
    for key in in_degree:
        # if in-degree at key is 0, append key in sources deque 
        if in_degree[key] == 0:
            sources.append(key)
    
    # step 4: for each source, add to sorted order and subtract one from all children in-degrees
    # if child in-degree 0, add to sources queue 
    while sources:
        # pop element from start of sources and store element in vertex 
        vertex = sources.popleft()
        
        # append vertex at end of sorted order 
        sorted_order.append(vertex)
        
        # traverse in graph at vertex using child get node's children to decrement in-degrees 
        for child in graph[vertex]:
            in_degree[child] -= 1 # decrement in-degree of node picked in previous step 
            # if in-degree at child is 0, append child to sources deque 
            if in_degree[child] == 0: # pick node with in-degree 0 and add to output list 
                sources.append(child)
                # repeat for all nodes with in-degree equal to zero 
                
    # topological sort not possible as graph has cycle
    if len(sorted_order) != n:
        return []

    return sorted_order

def can_finish(num_courses, prerequisites):
    counter = 0
    if num_courses <= 0:
        return True
    
    # step 1: initialize graph containing key as parent and value as its child's vertices 
    in_degree = {i: 0 for i in range(num_courses)}
    graph = {i: [] for i in range(num_courses)}
    
    # step 2: build graph and populate in-degree hash map 
    for edge in prerequisites:
        parent, child = edge[1], edge[0]
        graph[parent].append(child) # put child into parent list
        in_degree[child] += 1 # increment child in-degree
        
    # step 3: find all sources with 0 in-degrees 
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)
    
    # step 4: for each source, increment counter, -1 from all children in-degrees
    # if child in-degree becomes zero, add to sources queue 
    while sources:
        course = sources.popleft()
        counter += 1
        
        # get node's children to decrement their in-degrees
        for child in graph[course]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
    
    # topological sort not possible if counter not equal to num_courses
    return counter == num_courses

def find_recipes(recipes, ingredients, supplies):
    # calculate count of ingredients of each recipe (count of dependencies of each recipe)
    # step 1: create dictionary to store number of ingredients or dependencies each recipe needs
    # this will track how many more ingredients needed for each recipe to be made 
    in_degree = {recipe: 0 for recipe in recipes}
    
    # step 2: create graph to store which recipes depend on ingredients 
    # will be used to reduce dependencies as ingredients become available 
    graph = {ingredient: [] for ingredient in supplies}
    
    # step 3: build graph an in-degree count based on recipe ingredients 
    for i, recipe in enumerate(recipes):
        for ingredient in ingredients[i]:
            # if ingredient isn't in supplies, must come from another recipe or unavailable
            if ingredient not in graph:
                graph[ingredient] = []
            
            # add recipe to list of recipes that depend on this ingredient 
            graph[ingredient].append(recipe)
            
            # increase in-degree or dependency count for recipe 
            in_degree[recipe] += 1
    
    # step 4: use queue to process recipes that can be made with available supplies 
    # initially add all supplies to queue (starting point of topo sort)
    queue = supplies[:]
    
    result = [] # list to store final list of recipes that can be made
    
    # start topo sort with list of supplies as starting point 
    # step 5: perform topo sort (process ingredients/recipes in valid order)
    while queue:
        # get next available ingredient or recipe if processed and can be made 
        ingredient = queue.pop(0)
        
        # if ingredient actually recipe, add to result list 
        if ingredient in in_degree:
            result.append(ingredient)
    
        # use topo sort to decrease dependency count of each recipe
        # check recipes that depend on this ingredient 
        for recipe in graph.get(ingredient, []):
            # reduce in-degree or dependency count for recipe 
            in_degree[recipe] -= 1
            
            # scan through list of recipes and add those w 0 dependency count 
            # if recipe has no more dependencies, it can be made, so add it to queue 
            # meaning all ingredients (as supplies or other recipes) available
            if in_degree[recipe] == 0:
                queue.append(recipe)
    
    return result