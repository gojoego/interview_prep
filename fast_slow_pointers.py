'''
fast/slow pointers 
-uses 2 pointers to traverse iterable data structure at different speeds to 
ID patterns, detect cycles, or find specific elements 
-speeds adjusted according to problem statement 
-often used to determine specific pattern or structure in data 
-pointers start at same location and move at different speeds 
-slow pointer usually moves by factor of one, fast by two 
-allows detection of patterns or properties within data structure (like cycles & intersections)
-for cycles, pointers will meet eventually 

examples
1. middle of linked list 
2. detect cycle in array 
3. identify if repeatedly computing sum of squares of digits of number 19 results in 1 

does your problem match this pattern? yes, if...
-linear data structure 
-cycle or intersection detection
-find starting element at second quantile 

real-world problems
-symlink verification
-compiling object-oriented program 

'''

# given number n, determine if happy, replace number with sum of digits, repeat until number equals 1 (happy) 
# or enters cycle (unhappy) -> return True if happy, False if not, time O(logn), space O(1)
def is_happy_number(n):
    # set up 2 pointers
    # slow pointer that points to input number
    slow_pointer = n
    # fast pointer that points to sum of squared digits of input number 
    fast_pointer = sum_of_squared_digits(n)
    
    # start loop until fast pointer reaches 1 or both pointers meet, indicating cycle 
    while slow_pointer < fast_pointer:
        if fast_pointer != 1 and fast_pointer != slow_pointer:
            # update slow by adding squares of its digits and fast by adding squares of its digits twice 
            slow_pointer = sum_of_squared_digits(slow_pointer)
            fast_pointer = sum_of_squared_digits(sum_of_squared_digits(fast_pointer))
    
    # if fast pointer equals 1, return True, indicating a happy number
    if fast_pointer == 1:
        return True
    # if loop exits without finding happy number, return False, indicating cycle and not happy number
    else:
        return False
 
def sum_of_squared_digits(number):
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit ** 2
    return total_sum