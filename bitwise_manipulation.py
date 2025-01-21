'''
bitwise manipulation
-in programming, everything stored in computer memory as sequences of 0s and 1s (bits)
-process of modifying bits algorithmically using bitwise operations
-logical bitwise operations fastest computations because processors natively support them 
-approach generally leads to efficient solutions in problems where can efficiently transform
input into its binary form or manipulate it directly at bit level to produce required output

unsigned vs signed binary numbers
-unsigned: nonnegative integers 
-signed: both positive and negative integers, include sign bit (leftmost bit 
in 2's complement representation) to indicate sign of number 

bitwise operation 
-works on bit string, bit array or binary numeral 

bitwise operators 
-take its as their operands and calculate corresponding bit value in result 
-include:   
    logical NOT: unary operator that flips value of bit, if 1 flip to change 0 and vice versa
    logical AND: binary operator that evaluates 2 bits to 1 if both bits also 1, otherwise evaluated result always 0 
    logical OR: binary operator evaluates 2 bits to 1 if at least one bit is also 1, evaluated result 0 otherwise 
    logical XOR: binary operator that evaluates 2 bit to 1 only if both bits different, for example:
        one is 0, other is 1, result evaluated to 0 otherwise 
    logical left shift: binary operator that shifts all bits in unsigned binary number to left by specified 
        number of places, filling vacated bit(s) on right with zero(s), each shift to left will multiply 
        number by 2, so performing shift n places to left on binary number equivalent to multiplying decimal
        representation of that number by 2 ^ n, signed numbers cannot be multiplied or divided using logical shifts 
        because shifting sign bit alone is inadequate, arithmetic shifts required for signed numbers 
    arithmetic shifts: binary operator that maintains sign or leftmost bit by keeping position unchanged (in contrast
        to logical shifts), left +/- and right shift + -> fill vacated bits w 0, right shift - 1s 
    cyclic shifts: binary operator where bits of binary number shifted to left/right, vacated bits reintroduced 
        at opposite end 
    
examples
    1. swap without extra space, swap 2 numbers without using temp variable 
    2. check for even/odd without division/modulus   
    3. check if integer power of 2 
    4. given array where every element occurs even times except for one element occurring odd times, find odd elements

does your problem match this pattern? yes, if...
    -binary representation 
    -efficient sorting 

real-world problems
-compression algorithms: encoding/decoding, compact representation of variable-length codes by concatenating bits
and optimizing storage/transmission, compression without los of information, crucial for resource strains 
-status register: each bit distinct significance, masks 
-cryptography: cyclic shifts for confusion/diffusion to enhance security, avalanche effect
-hash functions: checksums in hash functions like CRC and Adler-32, error detection, data integrity verification 
'''

'''
statement: given two strings, str1 and str2, find the index of the extra character 
that is present in only one of the strings

note: if multiple instances of the extra character exist, return the index of the 
first occurrence of the character in the longer string

time O(n), space O(1)
'''

def extra_character_index(str1, str2):
    # initialize variable result to 0
    result = 0 
    
    # find lengths of both strings 
    str1_length = len(str1)
    str2_length = len(str2)
    
    # perform bitwise XOR operation btw current value of result & ASCII value of each character in str1
    for i in range(str1_length):
        result = result ^ (ord)(str1[i]) # update value of result with computed XOR value every time 

    # perform bitwise XOR operation between current value of result and characters of str2
    for j in range(str2_length):
        result = result ^ (ord)(str2[j]) # update value of result each time with computed XOR value
    
    # result contains ASCII value of extra character 
    if len(str1) > len(str2):
        # find and return index of extra character from longer string 
        index = str1.index((chr)(result))
        return index
    else:
        index = str2.index((chr)(result))
        return index
    
# time O(nlogn), space O(1)
def naive_extra_character_index(str1, str2):
    # determine longer and shorter string 
    if len(str1) > len(str2):
        longer, shorter = str1, str2
    else: 
        longer, shorter = str2, str1
        
    # sort both strings 
    sorted_longer = sorted(longer)
    sorted_shorter = sorted(shorter)
    
    # compare sorted strings character by characters
    for i in range(len(shorter)):
        if sorted_longer[i] != sorted_shorter[i]:
            # return index of mismatched character in original longer string 
            return longer.index(sorted_longer[i])
    
    # if no mismatch found, extra character is last one in longer string 
    return longer.index(sorted_longer[-1])

# for any n positive number in base 10, return complement of its binary representation as integer in base 10
from math import log2, floor # libraries used for algorithm 

# time and space O(1)
def find_bitwise_complement(num: int):
    if num == 0:
        return 1
    
    # calculate number of bits required to store any given positive integer/ 
    # count number of bits required by this number in binary representation 
    bit_count = num.bit_length()
    
    # create all bits set against number of bits of input value/ 
    # compute all 1-bits bitmask of number
    all_bits_set = (1 << bit_count) - 1 
    
    # flip all occurrences of 1s and 0s and 0s to 1s by computing XOR operation 
    # convert binary value back to base 10 and return complement 
    return num ^ all_bits_set

def naive_find_bitwise_complement(num: int) -> int:
    if num == 0:
        return 1 
    
    # convert number to binary representation 
    binary = bin(num)[2:] # removing 'Ob' prefix 
    
    # calculate complement manually by flipping each bit 
    complement_binary = ''.join('1' if bit == '0' else '0' for bit in binary)
    
    # convert complemented binary back to integer 
    complement = int(complement_binary, 2)
    
    return complement

'''
statement: given that an image is represented by an (n x n) matrix containing 0s and 1s,
flip and invert the image, and return the resultant image

horizontally flipping an image means that the mirror image of the matrix should be returned, 
flipping [1, 0, 0] horizontally results in [0, 0, 1]

inverting an image means that every 0 is replaced by 1 and every 1 is replaced by 0, inverting 
[0,1,1] results in [1,0,0]

time O(n^2), space O(1)
'''

def flip_and_invert_image(image):
    # get number of rows in image 
    row_count = len(image)
    
    # compute index of middle element in each row / calculate middle index of rows 
    mid = (row_count + 1) // 2 
    
    # iterate over first half of each row 
    for row in image:
        # iterate over first half of each row 
        for i in range(mid):
            # compute bitwise XOR of current element with 1, which will invert element's value 
            temp = row[i] ^ 1 # store inverted value of current element in temp variable
            
            # update/swap current element with inverted value of corresponding element from second half 
            row[i] = row[len(row) - 1 - i] ^ 1
            # element at same distance from end of row as current element is from beginning of row after 
            # performing same XOR operation on second element as well 
            
            # update corresponding element from second half with inverted value stored in temp variable 
            row[len(row) - 1 - i] = temp 

    # after iterate over all rows, return resultant image 
    return image

# solves problem by separately flipping and inverting image 
def naive_flip_invert_image(image):
    # step 1: flip image horizontally
    flipped_image = flip_horizontal(image)
    
    # step 2: invert image 
    inverted_image = invert_image(flipped_image)
    return inverted_image

# flips image horizontally by reversing each row 
def flip_horizontal(image):
    for row in image:
        row.reverse()
    return image

# inverts image by replacing 1s with 0s and 0s with 1s 
def invert_image(image):
    for row in image:
        for i in range(len(row)):
            row[i] = row[i] ^ 1
    return image

# given integer array where every element appears 2x, return single element, time O(n), space O(1)
def single_number(nums):
    # initialize variable named result with 0 
    result = 0 
    
    # traverse input array 
    for num in nums:
        # perform bitwise XOR for every element with result variable 
        result ^= num # update result each time we take XOR
        
    # after traversal, result has number that appears once, return this number 
    return result

# return 2 single elements from array in which most elements appear twice, time O(n), space O(1) 
def two_single_numbers(arr):
    # iterate through given array, performing bitwise XOR operation on each number, storing result
    bitwise_xor = 0
    for num in arr:
        bitwise_xor ^= num
    
    # find bitwise mask by performing bitwise AND operation between XOR result and its 2s' complement
    bitwise_mask = bitwise_xor & -bitwise_xor # isolates rightmost set bit in bitwise_xor 
    
    # initialize variables to store 2 unique numbers 
    result = 0 
    
    # iterate through array again, check each number if bitwise AND op btw num and mask non-zero 
    for num in arr:
        # if result of bitwise AND op non-zero, perform bitwise XOR op btw current result and number
        if num & bitwise_mask: # check if rightmost set bit in bitwise_xor is set in num 
            # num has rightmost set bit, XOR it with result 
            result ^= num 
     
    # return list containing one single number directly obtained from XOR operation and another
    # single number derived by XORing first single number w overall XOR result 
    return [result, bitwise_xor ^ result]

'''
statement: create method, encode, that converts array of strings into single string and then 
sends it over the network, create another method decode that takes encoded string and converts 
it back into original array of strings 

time and space O(m) where m = number of characters in array of strings 
'''
def encode(strings):
    encoded_string = ""
    
    for string in strings: 
        # add appended 4 byte string length to string in encoded string 
        encoded_string += length_to_bytes(string) + string
        
    # return encoded string and pass it on to decode function 
    return encoded_string

def decode(string):
    # initialize pointer 
    i = 0 
    decoded_string = []
    
    # iterate over encoded string and read its length from first four bytes
    while i < len(string):
        # extract length of that string and add that string to array 
        length = bytes_to_length(string[i : i + 4])
        i += 4
        
        # add string of computed length 
        decoded_string.append(string[i : i + length])
        # move pointer 
        i += length
        # keep on repeating until entire encoded string processed 
    
    # return decoded array of strings 
    return decoded_string

# express string length as string of bytes 
def length_to_bytes(string):
    # 4 characters in string -> '0004'
    length = len(string)
    
    bytes = []
    
    # iterate over string array, convert each string length into 4 bytes
    for i in range(4):
        # apply right shift operator 
        bytes.append(chr(length >> (i * 8))) # append length calculated in 4-byte format to start of particular string
        
    bytes.reverse()
    
    # convert array to string 
    bytes_string = ''.join(bytes)
    
    return bytes_string

def bytes_to_length(bytes_string):
    result = 0 
    
    for character in bytes_string:
        result = result * 256 + ord(character)
        
    return result

'''
statement: given an array of integers, nums, compute and return the sum of XOR totals for all its possible subsets

subset: any combination of elements from the original array and includes the empty subset (containing no elements) 
and the subset that includes all array elements

XOR total of a subset results from applying the XOR operation to all the elements in that subset

note: if the nums array has duplicate elements, then subsets that contain the same elements but with 
different indexes are treated as separate, each subset's XOR total is counted in the final sum

algorithm
1. bitwise OR 
2. sum of XOR totals 

XOR - bitwise operator that focuses on binary bits that are set to 1 (set bits), bits can flip XOR result 
    at that position from 0 to 1 and vice versa 
    
time O(n), space O(1)
'''
def xor_totals_sum(nums):
    # initialize variable output to 0 - stores cumulative result of performing bitwise OR operation on all num numbers 
    output = 0 
    
    # traverse over each element in nums performing bitwise OR operation between current output value and element 
    for num in nums:
        output = output | num
        
    # after processing all element, left shift result by len(nums) - 1 bits 
    # left shifted value is final result, sum of XOR totals for all subsets of nums 
    return output << (len(nums) - 1)

# return kth lucky number (4 and 7) as string for given integer k, time and space O(logk)
def kth_lucky_number(k):
    # increment k by 1 to align with 1-based indexing 
    k = k + 1
    
    # convert incremented k into its binary number string 
    result = bin(k)[3:] # exclude most significant 1 and bits left to it from binary string 

    # replace each 0 in binary string with 4 and each 1 with 7
    result = result.replace("0", "4").replace("1", "7")
    
    # return transformed string as k-th lucky number
    return result

'''
statement: given a binary array nums and an integer k, find the minimum number of flips needed 
to make all the bits in the array equal to 1, can only flip k consecutive bits at a time

[1,1,0,0] and k = 2, flip the last two bits to get [1,1,1,1], means we only need a single k 
flip to turn the entire array into all 1s

if nums cannot be converted to an array with all 1s with the given k, return -1

algorithm
- deciding when/where to flip k consecutive bits in array for minimum, need to track: 
    1. whether we have k consecutive bits with us or not 
    2. current state of k bits, need flipping? 
    3. total number of k flips made 
- traverse i, check if flip possible, i + k cannot exceed array length, return -1 if not 
- even flips -> original state, 0 to 1, 1 no flip
- odd flips -> inverted, 0 to 1, 1 no flip
- i greater than k, move to next k consecutive bits, undo effect at i - k 

time O(n), where n = length of nums
space O(k), where k = max number of slips tracked at any time 

'''
import collections

def min_k_bit_flips(nums, k):
    n = len(nums) # length of input list 
    
    # queue/eque to keep track of flips
    flip_track_queue = collections.deque()
    
    # counters for flip state and total flips 
    is_flipped = 0 # current flip state 
    total_flips = 0 # total number of flips
    
    # loop through each bit in input array nums 
    for i, num in enumerate(nums):
        
        # remove effect of oldest flip if it's out of current window 
        if i >= k:
            is_flipped ^= flip_track_queue.popleft()
        
        # check if current bit nums[i] requires flipping based on effective flip state 
        if is_flipped % 2 == nums[i]:
            
            # if flip needed but k consecutive flips out of bounds, return -1
            if i + k > n:
                return -1
    
            # record flipping by adding 1 to deque and update counters
            flip_track_queue.append(1)
            is_flipped ^= 1 # toggle state 
            total_flips += 1 # increment flip count 
        else:
            # otherwise, if no flip needed, append 0 to deqeue
            flip_track_queue.append(0)

    # after processing all bits, return count of total flips made
    return total_flips

# given string, return length of longest substring in which vowels appear even times, time O(n), space O(1)
def find_longest_substring(s): # use XOR to check even/odd: 1 odd, 0 even 
    # bitmask to track whether each vowel appear even/odd number of times 
    prefix_xor = 0 # initialize variable to keep traack of XOR state for vowel occurrences 
    
    # create map to assign unique bit value for each vowel using powers of 2 for bitwise manipulation 
    vowel_bit_map = [0] * 26
    vowel_bit_map[ord('a') - ord('a')] = 1    # 'a' -> 00001 (binary)
    vowel_bit_map[ord('e') - ord('a')] = 2    # 'e' -> 00010 (binary)
    vowel_bit_map[ord('i') - ord('a')] = 4    # 'i' -> 00100 (binary)
    vowel_bit_map[ord('o') - ord('a')] = 8    # 'o' -> 01000 (binary)
    vowel_bit_map[ord('u') - ord('a')] = 16   # 'u' -> 10000 (binary)
    
    # initialize array to store first occurrence of each XOR state, 32 possible states for 5 bit values 
    first_occurrence = [-1] * 32 # set each element to -1 to indicate no encounter 
    # initial condition: consider prefix xor of 0 starting at -1 
    first_occurrence[0] = -1
    
    # variable to store length of longest valid substring 
    length_longest_substring = 0 
    
    # traverse string tracking each character index and value 
    for i, character in enumerate(s): # perform XOR operation for each character
        # update XOR state if character vowel by toggling its bit 
        prefix_xor ^= vowel_bit_map[ord(character) - ord('a')]
        
        # if XOR result new/first occurrence and not zero, save current index in some list 
        if first_occurrence[prefix_xor] == -1 and prefix_xor != 0:
            first_occurrence[prefix_xor] = i
        # otherwise, if XOR state seen before, compute substring length from 1st occurrence to current index
        else:
            length_longest_substring = max(length_longest_substring, i - first_occurrence[prefix_xor])
            
    # after traversing string, return maximum length found
    return length_longest_substring # each vowel will only appear even number of times 

'''
statement: given an array of integers, arr, we need to find three indices, i, j, and k, such that 
0 ≤ i < j ≤ k < arr.length

define two values, a and b, as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]

b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]

note: ^ denotes the bitwise-xor operation

return the count of triplets (i, j, k) for which a is equal to b

time and space O(n) where n = length of array 
'''

from collections import defaultdict

def count_triplets(arr):
    # initialize variable to store count of valid triplets
    count = 0 
    
    # initialize variable to store running XOR value 
    prefix = 0
    
    count_map = defaultdict(int, {0: 1}) # number of occurrences of each XOR value 
    total_map = defaultdict(int) # sum of indices where each XOR value has occurred 
    
    # for each index in the array...
    for i in range(len(arr)):
        # update running XOR in prefix by taking its XOR with array at index 
        prefix ^= arr[i]
        
        # add contribution of prefix to count variable using 2 hash maps 
        count += count_map[prefix] * i - total_map[prefix]
        
        # update 2 hashmaps for current prefix value 
        
        # increment count of current XOR value 
        count_map[prefix] += 1
        
        # update sum of indices for current XOR value 
        total_map[prefix] += i + 1
    
    # return count variable, which contains number of valid triplets     
    return count

'''
statement: given an integer list, nums, find the length of the longest subarray where the 
bitwise AND of its elements equals the maximum possible bitwise AND among all subarrays of nums,
bitwise AND of a list is calculated by performing the bitwise AND operation on all elements within the subarray

time O(n) where n = length of input list, space O(1)

algorithm
-find longest contiguous subarray in list where every element contributes to highest possible bitwise AND value 
-highest AND value achieved when subarray consists of largest number in list
'''
def longest_subarray(nums):
    # initialize variables for max and value, max length, and current length 
    max_AND = max_length = current_length = 0 
    
    # iterate over each number in array 
    for num in nums:
        # update max AND reset lengths if higher number found 
        if max_AND < num:
            max_AND = num
            max_length = current_length = 0 
        
        # if current number equals max AND, increase subarray length 
        if max_AND == num:
            current_length += 1 
        else:
            # reset current length if current number does not equal max AND 
            current_length = 0 
        
        # update max length with longest subarray length found 
        max_length = max(max_length, current_length)
    
    return max_length

'''
statement: given an unsigned 32-bit integer n, we need to calculate a 32-bit unsigned integer with reversed bits,
when we say “reverse” we don't mean flipping the 0s to 1s and vice versa, but simply reversing the order in which 
they appear, i.e., from left-to-right to right-to-left

'''

def reverse_bits(n):
    # initialize variable result to store reversed bits 
    result = 0
    
    # loop to range 32 because of 32 bits
    for i in range(32):
        # left shift result by 1 position, effectively making room for next bit to be added
        result <<= 1
        
        # extract rightmost bit of n using bitwise AND op w/ 1 and perform OR op on extracted bit w/ result
        result |= (n & 1)
    
        # right shift n by 1, effectively removing processed rightmost bit 
        n >>= 1
    
        # repeat this until all bits in n have been processed to store reverse bit pattern of n in result
    
    # return result variable 
    return result