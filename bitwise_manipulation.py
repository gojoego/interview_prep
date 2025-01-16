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