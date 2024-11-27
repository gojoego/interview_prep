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

# return start indices of 2 anagram, time O(n), space O(1)
def find_anagrams(a, b):
    # if string b length greater than a, return empty list 
    if len(b) > len(a):
        return []
    
    result = [] # list to store output aka start indices of anagrams of string b in a 
    
    # create 2 hash maps for counting
    hash_a = defaultdict(int) # count of characters in sliding window inside string a 
    hash_b = defaultdict(int) # frequency of characters in string b
  
    # populate hash b with count of characters in string b 
    for i in range(len(b)):
        hash_b[b[i]] += 1 
  
    # while traversing string a, move window rightward by one character in each iteration
    for window_end in range(len(a)): 
        # add new element to move window rightward/add new element and its count in hash map a 
        hash_a[a[window_end]] += 1
        
        # if length of window exceeds string b length, make equal by removing leftmost element 
        if window_end >= len(b):
            
            # index of leftmost element in sliding window 
            window_start = window_end - len(b)
        
            # if count of leftmost element is 1, safe to delete from hash map a
            if hash_a[a[window_start]] == 1:
                del hash_a[a[window_start]]
                
            # if count greater than 1, remove one occurrence of it from hash map a 
            else:
                hash_a[a[window_start]] -= 1
    
        # if count of characters in hash map a equals b, indicates anagram, append start index to result
        if hash_a == hash_b:
            start_index = window_end - len(b) + 1
            result.append(start_index)
        
    # after traversing entire string a, return array of all start indices of anagrams b in string a
    return result

# give array where each element 2 length, return length of longest palindrome, time 0(n), space O(min(n, |E|^2))
from collections import Counter

def longest_palindrome(words):
    # track frequency of each 2 letter word in dictionary
    frequencies = Counter(words)
    count = 0
    central = False 
    
    # iterate through dictionary 
    for word, frequency in frequencies.items():
        # if word palindrome, check frequency and increment length accordingly 
        if word[0] == word[1]:
            # if even occurrences
            if frequency % 2 == 0:
                count += frequency
            # if word has odd occurrences
            else: # verify presence of central word
                count += frequency - 1
                central = True
    
        # if word not palindrome, determine frequency of its reverse and increment length accordingly
        elif word[1] > word[0]:
            # get min of occurrences of word and its reverse 
            count += 2 * min(frequency, frequencies[word[1] + word[0]])
    
    # after iteration, if central word, increase length accordingly 
    if central:
        count += 1
        
    return 2 * count

# given array of strings votes, sort teams according to rank, time O(n), space O(1)
def rank_teams(votes):
    # create 2D ar0ray to store vote counts for each team
    # first dimension denotes team, second stores votes for each position
    counts = [[0] * 27 for _ in range(26)]
    
    # iterate through each string votes[i] to process ranking given by each voter 
    for t in range(26):
        counts[t][26] = chr(ord('A') + t)
    
    # for each character votes[i][j] representing team in vote, decrement rank in counts array 
    for i in range(len(votes)):
        for j,c in enumerate(votes[i]):
            counts[ord(c) - ord('A')][j] -= 1
    
    # sort counts array based on values in each row 
    counts.sort()
    
    # create empty string result to store final result 
    result = ""
    
    # for each row in sorted counts array, retrieve its corresponding team name and append it to result
    for i in range(len(votes[0])):
        result += counts[i][26]
    
    # return constructed string result, representing teams in ranked order 
    return result

def main():
    rankings = [
        ["XYZ", "ZXY", "XZY"],
        ["MNOPQ"],
        ["AB", "BA"],
        ["SING", "SIGN", "NIGS", "GINS"],
        ["QWERTYUIOPASDFGHJKLZXCVBNM", "ZXCVBNMASDFGHJKLQWERTYUIOP"]
    ]
    
    for i in range(len(rankings)):
        print(i + 1, ".\tVotes: ", '[' + ', '.join(f'"{vote}"' for vote in rankings[i]) + ']', sep="")
        print("\tRanking: \"", rank_teams(rankings[i]), "\"", sep="")
        print("-" * 100)

if __name__ == "__main__":
    main()