'''

knowing what to track 
-counting occurrences of elements in give data structure
-usually array or string 
-use frequency info to solve problem

phases:
-counting phase: iterate through elements of data structure, count frequency of element,
can use hash aps dictionaries, arrays or simple variables 
-utilization phase: use frequency data to solve problem, examples include finding frequent 
element, ID element that occurs once, check if 2 arrays are permutations of each other, etc

data structures used for pattern
-hash map: stores elements as keys, frequencies as values, update frequency if element already in
hash table or add new element with frequency of 1 
-array: index reps elements, value at index frequency, value is index to access frequency and 
increment by 1 if need be, use if range of elements known is smaller and known in advance 

examples
1. contains duplicate
2. count prefixes of given string 
3. given string, count substrings w vowels 
4. given string, check if any of its permutations can form valid palindrome
 
does your problem match this pattern? yes, if...
-frequency tracking 
-pattern recognition 
-fixed set of possibilities 

real-world problems
-DNA sequence analysis 
-video streaming
-e-commmerce 
-clickstream analysis 

'''

# check string for palindromic permutation
from itertools import permutations

# time O(n! x n^2), space O(n!)
def naive_permute_palindrome(st):
    # computer all possible permutations of given string
    for perm in set(permutations(st)):
        # iterate over permutation to see if palindrome 
        perm_str = ''.join(perm)
        if is_palindrome(perm_str):
            return True
    return False

def is_palindrome(s):
    return s == s[::-1]

# notes 1. even length characters occur even times 2. odd length, middle character once 3. true for all permutations
# time O(n) where n = number of elements in hashmap, space O(1)
def permute_palindrome(st):
    frequencies = {}
    
    # traverse input string starting from first character
    for i in st:
        # populate hash map with characters in string w/ frequency of occurence of each character
        if i in frequencies:
            frequencies[i] += 1 # increment by 1 if already present in map 
        else:
            frequencies[i] = 1 
    
    count = 0
    
    # traverse hash map to get count of characters with odd number of occurrences 
    for ch in frequencies.keys():
        if frequencies[ch] % 2:
            count += 1
    
    # if count exceeds 1, no palindromic permutation exists 
    if count <= 1:
        return True
    else:
        return False 

# check if string is anagram of another
def is_anagram_naive(string1, string2):
    if len(string1) != len(string2):
        return False
    
    return sorted(string1) == sorted(string2)

# time O(n), space O(1) 
def is_anagram(str1, str2):
    # check whether lengths of strings equal, return False if not
    if len(str1) != len(str2):
        return False
    
    # initialize hash map, character = key, value = count 
    char_counts = {}
    
    # iterate over characters in str1, increment count for each character
    for ch in str1:
        if ch in char_counts:
            char_counts[ch] += 1
        else:
            char_counts[ch] = 1
    
    # iterate over characters in str1, decrement count for each character
    for ch in str2:
        if ch in char_counts:
            char_counts[ch] -= 1
        else:
            return False
            
    # if count for all characters 0, return True, False otherwise 
    for key in char_counts:
        if char_counts[key] != 0:
            return False
    
    return True 


'''
statement: tic-tac-toe on n x n board, rules: move guaranteed to be valid if mark placed on 
empty block, no more moves allowed once winning condition reached, player who succeeds 
in placing n of their marks in horizontal, vertical or diagonal row wins game

implement TicTacToe class w constructor that initializes object and allows players to play on
board of size n x n, move(row,col,player) that indicates where player places mark on cell(row,col),
move guaranteed to be valid and returns player ID if current player wins and 0 if no one wins 

'''

class TicTacToe:
    # constructor will be used to initialize TicTacToe data members, time O(n)
    def __init__(self, n): 
        # create 2 lists to track number of moves made in each row/column
        self.rows = [0] * (n)
        self.columns = [0] * (n)
        # initialize 2 counters to store count of moves made along either diagonal to 0
        self.diagonal = 0
        self.anti_diagonal = 0

        pass        

    # move will be used to play move by specific player and identify who wins at each move
    # time O(1), space O(n) where n = length of arrays rows and columns 
    def move(self, row, col, player):
        current_player = -1 
        if player == 1:
            current_player = 1
        
        n = len(self.rows)
        
        # if player 1 move, increment count in relevant lists
        # if player 2 move, decrement count in relevants lists 
        self.rows[row] += current_player
        self.columns[col] += current_player
        
        # if mark player 1 placed along diagonal, increment relevant counter
        # if mark player 2 on diagonal, decrement relevant counter 
        if row == col:
            self.diagonal += current_player
            
        if col == (n - row - 1):
            self.anti_diagonal += current_player
        
        # if count of any element of list equal to n or if either of 2 diagonal counters
        # equal to n, return current player as winner     
        if abs(self.rows[row]) == n or abs(self.columns[col]) == n \
        or abs(self.diagonal) == n or abs(self.anti_diagonal) == n:
            return player

        # if neither count equal n, return 0
        return 0

# given list of words/phrases, group words that are anagrams of each other
def group_anagrams(strs):
    # initialize hash map to store key/value pairs for strings' frequency and anagrams 
    result = {}
    
    for s in strs:
        # key will be character list of length 26, initialized to all 0s, value will be array of anagrams
        count = [0] * 26 # place for every single letter in our string 
        for i in s:
            index = ord(i) - ord('a')
            
            count[index] += 1
        
        key = tuple(count)
        if key in result:
            result[key].append(s)
        else: 
            result[key] = [s]
    
    return result.values()

# time O(nllogl) where n = strings list length and l = longest string length, space O(1) 
def group_anagrams_naive(strings):
    # initialize hashmap to store strings as key and lists of anagrams as values
    result = {}
    
    for string in strings:
        # sore current string 
        sorted_string = ''.join(sorted(string))
        
        # check if sorted string is present as key in hash map 
        if sorted_string in result:
            # append original unsorted string to list of anagrams for this key
            result[sorted_string].append(string)
        else:
            # add new key/value pair to hash map 
            result[sorted_string] = [string]
    
    # return list of grouped anagrams
    return result.values()

'''
statement: design stack data structure to push and pop elements with max frequency

init() - constructor to declare frequency stack 
push(value) - push int data onto stack top 
pop() - remove and return most frequent stack element 
'''

from collections import defaultdict

class FreqStack:
    def __init__(self):
        # create hash map or dictionary to store frequencies of all elements 
        self.frequency = defaultdict(int)
        self.group = defaultdict(list)
        self.max_frequency = 0

    # time O(1), space O(n)
    def push(self, value):
        # get frequency for given value and increment frequency for given value 
        freq = self.frequency[value] + 1
        self.frequency[value] = freq
        
        # check if max frequency is lower than new frequency of given value 
        if freq > self.max_frequency:
            self.max_frequency = freq
        
        self.group[freq].append(value)

    # time O(1), space O(n)
    def pop(self):
        value = ""
        
        if self.max_frequency > 0:
            value = self.group[self.max_frequency].pop()
            self.frequency[value] -= 1
            
            if not self.group[self.max_frequency]:
                self.max_frequency -= 1
        else:
            return - 1
        return value
    
class NaiveFreqStack:
    def __init__(self):
        # use list to maintain elements in stack order 
        self.stack = []
        # dictionary to keep track of frequencies of elements 
        self.frequency = defaultdict(int)
        
    def push(self, value):
        # add element to stack 
        self.stack.append(value)
        # increment its frequency
        self.frequency[value] += 1
        
    def pop(self):
        # if stack empty, return -1
        if not self.stack:
            return -1 
        
        # find element with max frequency
        max_freq = max(self.frequency.values())
        
        # iterate from end of list to maintain "stack" behavior (most recent item)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.frequency[self.stack[i]] == max_freq:
                # once found, remove it and decrease its frequency
                element = self.stack.pop(i)
                
                self.frequency[element] -= 1
                
                if self.frequency[element] == 0:
                    del self.frequency[element] # cleanup if frequency zero 
                    
                return element
        
        return -1 # if no element found (edge case)

# time O(n), space O(1)
def first_unique_char(s):
    character_count = {} # declare hash map
    string_length = len(s) # stores length of input string 
    
    # iterate over input string 
    for i in range(string_length):
        # check if each character exists in hash map 
        if s[i] in character_count:
            # increment value if in hash map
            character_count[s[i]] += 1
        # otherwise, add new key/value pair to hash map and set value to 1
        else:
            character_count[s[i]] = 1
            
    # traverse over input string to find map characters w value 1 
    for i in range(string_length):
        # return index if character exists
        if character_count[s[i]] == 1:
            return i 
    
    # return -1 otherwise
    return -1 