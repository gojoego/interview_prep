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