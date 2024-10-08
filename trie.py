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
class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie():
    def __init__(self): # constructor to create trie node 
        self.root = TrieNode()
    
    # inserting string in trie, time and space O(l) where l = length of word/string 
    def insert(self, string):
        # begin from root node, iterate over string 1 character at a time 
        node = self.root
        for character in string:
            # for each character, check if current character exists as child node of current node 
            if character not in node.children: # if character not found
                node.children[character] = TrieNode() # create new node, link as child of current node
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
