'''

trie
-data structure used for storing and locating keys from set 
-keys usually strings stored character by character 
-each node of trie corresponds to single character rather than entire key 
-also called prefix trees because they provide very efficient prefix-matching operations

characteristics
-order of characters in string represented by edges between adjacent nodes 
-level of nodes signifies position of characters within word 
    -each level corresponds to specific index in word being represented 
    -at any given level, each node corresponds to distinct character in words stored in trie 
    -as we traverse down trie from root to leaf, characters encountered form word with path 
-contains end of word nodes that mark conclusion of word within trie structure 
    -each end of word node signifies termination point of word stored in trie 
    -characteristic is crucial for efficient word retrieval and validation ops: allows
     trie to distinguish between prefixes and complete words during searches or insertions 
     
methods
-insert(word):  start at root and traverse down trie, creating new nodes if required for each 
                character in string, time O(m) where m = length of word 
-search(word):  start at root and traverse down trie, following path that corresponds to 
                characters of target word, if null pointer encountered or end of word reached
                before leaf node -> word not present in trie, time O(m)
-delete(word):  start at root and traverse down trie, following path that corresponds to characters
                of target word, if found -> remove nodes corresponding to characters of string,
                may include cleanup to remove any unnecessary nodes to maintain efficiency,
                time O(m)

examples
-longest common prefix
-count unique words 
-implement contact list where you can search for contacts by names efficiently
-find all words in dictionary that start with "aba"

does your problem match this pattern? yes! if...
-partial matches: comparing 2 strings to detect partial matches based on initial characters of one or both strings
-space optimization: optimize space used to store dictionary of words, storing shared prefixes once allows for savings
-can break down string: problem statement allows breakdown of strings into individual characters 

real world problems
-autocomplete systems
-orthographic corrector 
-prefix matching in IP addresses or URLs

'''

# implement trie data structure with 3 functions that perform following tasks: insert(word), search(word), search_prefix(prefix)
class TrieNode1():
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie1():
    def __init__(self): # constructor to create trie node 
        self.root = TrieNode1()
    
    # inserting string in trie, time and space O(l) where l = length of word/string 
    def insert(self, string):
        # begin from root node, iterate over string 1 character at a time 
        node = self.root
        for character in string:
            # for each character, check if current character exists as child node of current node 
            if character not in node.children: # if character not found
                node.children[character] = TrieNode1() # create new node, link as child of current node
            # if character found, move to that child node and continue to next character
            # and move to newly created node
            node = node.children.get(character) 
        
        # for last character of word, set boolean variable to TRUE for corresponding node to indicate end of word 
        node.is_word = True
    
    # searching for a string, time O(l), space O(1)
    def search(self, string):
        node = self.root
        
        # iterate over word character by character
        for character in string:
            # if there is no child of node, return False
            if character not in node.children:
                return False
            node = node.children.get(character)
        
        # return word after traversing all nodes as it is found
        return node.is_word
    
    # searching for a prefix, time O(l), space O(1)
    def search_prefix(self, prefix):
        node = self.root
        
        # iterate over prefix character by character
        for character in prefix:
            # if no child of node, return False, prefix not found
            if character not in node.children:
                return False
            node = node.children.get(character)
        
        # return true after traversing all nodes as prefix found
        return True

'''

prompt: given array of strings called products and word to search, design system that, when 
each character of searched word typed, suggests at most three product names from products - 
suggested products should share common prefix with searched word - if more than 3 products exist
with common prefix, return first 3 lexographical names, return suggested products

'''

# space O(n)
class TrieNode2(object):
    def __init__(self):
        self.search_words = []
        self.children = {}

class Trie2(object):
    def __init__(self):
        self.root = TrieNode2()
    
    # time O(L * n) where L = average length of each product, n = number of separate nodes
    def insert(self, data):
        node = self.root
        index = 0
        
        # insert all product names in trie, creating node for each new character in word 
        for character in data:
            if character not in node.children:
                node.children[character] = TrieNode2() # create new node if doesn't exist 
            node = node.children[character]
            # if there are more than 3 matched strings, return ones that appear first in 
            # lexicographical order, gam -> game, games, gamify
            if len(node.search_words) < 3:
                node.search_words.append(data) # append current product if less than 3 
            index += 1
    
    # time O(m) where m = length of prefix 
    def search(self, word):
        # as each new letter of searched word received, retrieve all words in trie 
        # whose initial characters match, gam -> game, games, gamify, gamma 
        result = []
        node = self.root
        for i, character in enumerate(word):
            if character not in node.children: 
                temp = [[] for _ in range(len(word) - i)] # append empty lists for remaining char
                return result + temp # terminate search 
            else: # if there's data corresponding to current char, append to result array 
                node = node.children[character]
                result.append(node.search_words[:])
        return result

def suggested_products(products, search_word):
    # sort products so they are in lexicographic order
    products.sort() # time O(ologn)
    trie = Trie2() # each trie node will have children dictionary and list of words to search 
    # insert products in trie by creating new nodes for each new character encountered 
    for x in products:
        trie.insert(x)
    return trie.search(search_word)

# time O(nlogn), space O(m)
def naive_suggested_products(products, search_word):
    # sort given product data in lexicographic order - helps retrieving 3 matching products 
    products.sort()
    result = []
    # iterate over word 
    for i in range(1, len(search_word) + 1):
        substring = search_word[:i] # adding current character to substring to search for 
        matching_products = []
        for product in products: # iterating over products array 
            if product.startswith(substring): # check if current substring exisrts 
                matching_products.append(product) # storing results for current substring 
            if len(matching_products) == 3: # breaking once there are 3 items in subarray
                break
        result.append(matching_products)
    return result

'''

prompt: given dictionary consisting of prefixes and sentences, replace postfix in sentence 
with prefixes in dictionary if found, return modified sentence

-postfix in sentence matches more than 1 prefix in dictionary -> replace with shortest prefix
-no root -> leave unchanged 



''' 

class TrieNode3:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie3:
    def __init__(self):
        self.root = TrieNode3()
    
    def insert(self, word):
        current = self.root
        
        # iterate over each character in word 
        for char in word:
            # if char doesn't belong to any child node of current trie node, create new trie node as child 
            if char not in current.children:
                current.children[char] = TrieNode3()
            
            # move to child of current node, either present or already added 
            current = current.children[char]
        
        # set end of word flag to True b/c end of inserted word reach 
        current.end_of_word = True
    
    def replace(self, word):
        current = self.root
        
        # iterate over each dictionary word along with index of that character
        for index, char in enumerate(word):
            # if char not current node child, return word 
            if char not in current.children:
                return word 
            
            # move to child of current node corresponding to current character
            current = current.children[char]
            
            # when end of word flag becomes True -> end of word reached in trie, return word 
            if current.end_of_word:
                return word[:index + 1]
        
        return word
# time O(m + n) where m = number of characters of all prefixes in dictionary, n = number sentence words, space O(m)
def replace_words(sentence, dictionary):
    # create trie to store each prefix present in dictionary 
    trie = Trie3()
    
    # iterate over prefixes in dictionary and insert into trie
    for prefix in dictionary:
        trie.insert(prefix)
        
    # store eaach word of sentence in new list 
    new_list = sentence.split()
    
    # for each word in sentence, check whether any initial sequence of characters match word in trie 
    for i in range(len(new_list)):
        # replace each word in new list w shortest prefix found from trie 
        new_list[i] = trie.replace(new_list[i]) # once found, replace original word in sentence w matched prefix

    # after processing all words in sentence, return modified sentence
    return " ".join(new_list) # converting list back to single sentence after replace each word w shortest matching prefix

def naive_replace_words(sentence, dictionary):
    # split sentence into individual words 
    words = sentence.split()
    
    # iterate over each word in sentence
    for i in range(len(words)):
        shortest_prefix = None # tracks shortest matching prefix 
        word = words[i]
        
        for prefix in dictionary: # iterate and compare currendt word with each dictionary prefix 
            if word.startswith(prefix): # if word starts with prefix
                # update shortest prefix if None or new prefix shorter
                if shortest_prefix is None or len(prefix) < len(shortest_prefix):
                    shortest_prefix = prefix
        
        # if matching prefix found, replace word with shortest prefix
        if shortest_prefix:
            words[i] = shortest_prefix
            
    # join words back into sentence and return 
    return " ".join(words)

'''

prompt: create WordDictionary data structure with the following methods...
    constructor() to initialize object 
    add_word(word) to store provided word in data structure 
    search_word(word) to return boolean if string in object matches query word, 
        each dot . is a wild card 
    get_words() to return all words in WordDictionary class 
    
'''

class TrieNode():
    # initialize TrieNode instance 
    def __init__(self):
        # empty list of child nodes 
        self.children = []
        # false indicates that this is not an end of a word 
        self.complete = False
        # create 26 child nodes for all the letters in the alphabet 
        for _ in range(0, 26):
            self.children.append(None)

class DepthFirstSearch():
    
    def __init__(self):
        self.root = TrieNode()
        self.can_find = False
    
    def depth_first_search(self, root, word, i):
        # if word found, return True
        if self.can_find:
            return True
        
        # return if word NULL 
        if not root:
            return 
        
        # if there's only 1 character in word, check for query match 
        if len(word) == i:
            if root.complete:
                self.can_find = True
            return
        index = ord(word[i]) - ord('a')
        self.depth_first_search(root.children[index], word, i + 1)
        
class WordDictionary:
    # initialize root with TrieNode and set can_find boolean to False 
    def __init__(self):
        self.root = TrieNode()
        self.can_find = False

    # function to add new word to dictionary, time and space O(1)   
    def add_word(self, word):
        n = len(word)
        
        # start from root node of trie and traverse word one character at a time 
        current_node = self.root
        for i, value in enumerate(word):
            # find correct index of character in list of nodes
            # calculate index of character between 1 and 26
            index = ord(value) - ord('a')
            
            # check whether character already exists in trie
            if current_node.children[index] == None:
                # if character not present in trie, create new trie node
                current_node.children[index] = TrieNode()
            # otherwise use existing trie node for this character 
            current_node = current_node.children[index]
            if i == n - 1:
                # if end of word reached and boolean flag already set
                # means that it is already present in dictionary, so return True 
                if current_node.complete:
                    print("\tWord already present!")
                    return
                # once all characters of current word added to trie
                # set boolean variable to True, marking as end of word 
                current_node.complete = True         
        print("\tWord added successfully!")
        
    # function to search for word in dictionary, time and space O(1)
    def search_word(self, word):
        # set can_find variable as False 
        self.can_find = False
        
        # perform DFS to iterate over children nodes 
        self.searcher(self.root, word, 0)
        return self.can_find
    
    def searcher(self, node, word, i):
        # if word already found and no need for further searching, return control to calling context 
        if self.can_find:
            return
        
        # return control to calling context if current node empty 
        if not node:
            return 
        
        # if last character of query string found in trie and complete flag is set, entire word found
        if len(word) == i:
            if node.complete:
                self.can_find = True
            return
        
        # if word contains wildcard character "." match with all children/letters 
        # of current node and perform DFS starting at each child 
        if word[i] == '.':
            for j in range(ord('a'), ord('z') + 1):
                self.searcher(node.children[j - ord('a')], word, i + 1)
        else:
            # otherwise, locate child corresponding to current character 
            index = ord(word[i]) - ord('a')
            # and continue DFS
            self.searcher(node.children[index], word, i + 1)

    # function to get all words in dictionary, time and space O(1) 
    def get_words(self):
        words_list = []
        
        # return empty list if root NULL 
        if not self.root:
            return []
        
        # perform DFS on trie 
        return self.dfs(self.root, "", words_list)
    
    def dfs(self, node, word, words_list):
        # if node NULL, return words list 
        if not node:
            return words_list
        
        # if word complete, add to words list 
        if node.complete:
            words_list.append(word)
        
        for j in range(ord('a'), ord('z') + 1):
            prefix = word + chr(j)
            words_list = self.dfs(node.children[j - ord('a')], prefix, words_list)
        return words_list

'''
prompt: given list of strings, find them in 2D grid of letters such that string can be constructed
from letters in sequentially adjacent cells, cells considered sequentially adjacent when they are 
neighbors to each other either horizontally or vertically, return list containing string from input list 
found in grid, order in strings do not matter

'''