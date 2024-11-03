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