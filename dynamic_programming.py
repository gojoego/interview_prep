# dynamic programming interview practice problems 

# naive solution: space O(n), time O(2^n)
def naive_knapsack(capacity, weights, values):
    n = len(weights)
    return naive_knapsack_recursive(capacity, n, weights, values)

def naive_knapsack_recursive(capacity, weights, values, n):
    # base case - no items left or capacity is 0
    if n == 0 or capacity == 0:
        return 0
    
    # recursive cases 
    if weights[n - 1] <= capacity: # if weight of nth item less than capacity
        # either include item and deduct weight of item from knapsack capacity (to get remaining capacity)
        # or don't include item at all and pick option that yields highest value 
        include = values[n - 1] + naive_knapsack_recursive(capacity - weights[n - 1], weights, values, n - 1)
        exclude = naive_knapsack_recursive(capacity, weights, values, n - 1)
        return max(include, exclude)
    else:
        # item can't be added to knapsack if weight greater than capacity
        return naive_knapsack_recursive(capacity, weights, values, n - 1)

def memo_knapsack(capacity, weights, values):
    n = len(weights)
    # set up memo table to store solutions to subproblems
    max_profits = [[-1 for i in range(capacity + 1)] for j in range(n + 1)]
    return memo_knapsack_recursive(capacity, weights, values, n, max_profits)
    
def memo_knapsack_recursive(capacity, weights, values, n, max_profits):
    # base case 
    if n == 0 or capacity == 0:
        return 0
    
    # if subproblem already solved, fetch result from memory 
    if max_profits[n][capacity] != -1:
        return max_profits[n][capacity]
    
    # otherwise, solve and save result in lookup table 
    if weights[n - 1] <= capacity:
        include = values[n - 1] + memo_knapsack_recursive(capacity - weights[n - 1], weights, values, n - 1, max_profits)
        exclude = memo_knapsack_recursive(capacity, weights, values, n - 1, max_profits)
        max_profits[n][capacity] = max(include, exclude)
        return max_profits[n][capacity]
    
    max_profits[n][capacity] = memo_knapsack_recursive(capacity, weights, values, n - 1, max_profits)
    return max_profits[n][capacity]
    
def find_max_knapsack_profit(capacity, weights, values):
    # create 2D table to store max profit for each item and capacity 
    # initialize table with 0s for first row and column to handle base cases 
    max_profits = [0] * (capacity + 1)
    # iterate over remaining rows and columns of table, filling them in based
    # on whether weight of item less than or equal to current capacity 
    # if weight less than or equal to current cap, use max value that can be 
    # obtained by either including or excluding item 
    for i in range(len(weights)):
        for j in range(capacity, weights[i] - 1, -1):
            max_profits[j] = max(values[i] + max_profits[j - weights[i]], max_profits[j])
    # otherwise, exclude item and use previous best value at that capacity 
    # return value in last row and column of table, which reps max value
    # that can be obtained w/ given capacity and items 
    return max_profits[capacity]

# dp[i][j] = max(values[i-1]+ dp[i-1][j - weights[i-1]], dp[i-1][j])

def tab_knapsack(capacity, weights, values):
    # create table to hold intermediate values 
    n = len(weights)
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            # check if weight of current item less than current capacity 
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else: # don't include itme if weight greater than current capacity 
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1] #[n][capacity]

import copy

def tab_knapsack_optimized(capacity, weights, values):
    n = len(weights)
    
    # previous (i - 1)th row which will be used to fill up current ith row 
    dp = [0] * (capacity + 1)
    
    # current ith row that will use values of previous (i - 1)th row to fill itself 
    temp = [0] * (capacity + 1)
    
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i-1] <= j:
                temp[j] = max(values[i-1] + dp[j-weights[i-1]], dp[j])
            else:
                temp[j] = dp[j]
        
        # setting (i - 1)th row equal to ith row 
        dp = copy.deepcopy(temp)
    
    return dp[capacity]

def find_max_knapsack_profit(capacity, weights, values):
    n = len(weights)
    dp = [0] * (capacity + 1)
    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(values[i] + dp[j - weights[i]], dp[j])
    return dp[capacity]

def coin_change(coins, total):
    if total < 1:
        return 0
    # initialize counter array of size total to store min # of coins required to 
    # make up specific total values up to given total amount 
    return calculate_minimum_coins(coins, total, [float('inf')] * total)

def calculate_minimum_coins(coins, remaining_amount, counter): 
    # base cases 
    if remaining_amount < 0: # less than 0
        return -1 
    if remaining_amount == 0: # amount is 0
        return 0
    if counter[remaining_amount - 1] != float('inf'): # neither less than nor equal to zero 
        return counter[remaining_amount - 1]
    minimum = float('inf')
    
    # traverse coins array - at each iteration, check base cases 
    for s in coins:
        # if it's neither base case, 2 options: select coin denomination or ignore it 
        # if coin selected, recursively solve its subproblems with reduced total amount 
        result = calculate_minimum_coins(coins, remaining_amount - s, counter)
        if result >= 0 and result < minimum:
            minimum = 1 + result

    counter[remaining_amount - 1] = minimum if minimum != float('inf') else -1 
    # at end, return min number of coins required to make up given total  
    return counter[remaining_amount - 1]


def find_tribonacci(n):
    # initialize first 3 numbers as 0, 1, and 1 
    first = 0
    second = 1
    third = 1 
    # if n less than 3, result determined by base case 
    if n < 3: 
        return 1 if n else 0
    
    # else, continue computing 3rd and next numbers by adding previous 3 numbers 
    # update until required number obtained 
    for _ in range(n - 2):
        first, second, third = second, third, first + second + third
    
    return third

def memo_find_tribonacci(n):
    memo = {0: 0, 1: 1, 2: 1}
    return trib(n, memo)

def trib(n, memo):

    if n in memo: 
        return memo[n]
    
    memo[n] = trib(n - 1, memo) + trib(n - 2, memo) + trib(n - 3, memo)

    return memo[n]

def naive_can_partition_array(nums):
    nums_sum = sum(nums)
    
    if nums_sum % 2 != 0:
        return False
    
    target_sum = nums_sum // 2
    
    memo = {}
    
    return naive_partition_recursive(nums, len(nums), target_sum, memo)

def naive_partition_recursive(nums, nums_length, target_sum, memo):
    if target_sum == 0:
        return True
    if nums_length == 0:
        return False
    
    if (nums_length, target_sum) in memo:
        return memo[(nums_length, target_sum)]

    if nums[nums_length - 1] > target_sum:
        result = naive_partition_recursive(nums, nums_length - 1, target_sum, memo)
    else: 
        exclude_last = naive_partition_recursive(nums, nums_length - 1, target_sum, memo)
        include_last = naive_partition_recursive(nums, nums_length - 1, target_sum - nums[nums_length - 1], memo)
    
        if exclude_last:
            result = True
        elif include_last:
            result = True 
        else: 
            result = False
        
    memo[(nums_length, target_sum)] = result
    return result

def tab_can_partition_array(nums):
    # calculate array sum
    nums_sum = sum(nums)
    n = len(nums)
    
    # if array sum odd, cannot be partitioned into equal sum subsets 
    if nums_sum % 2 != 0:
        return False
    
    # calculate subset sum 
    subset_sum = nums_sum // 2 
    
    # create matrix of appropriate size and initialize all cells w False 
    dp = [[False for i in range(n + 1)] for j in range(subset_sum + 1)]
    
    # initialize first row as True as each array has subset whose sum is zero 
    for i in range(0, n + 1):
        dp[0][i] = True
        
    # traverse input array, element by element, fill lookup table in bottom-up manner 
    for i in range(1, subset_sum + 1):
        for j in range(1, n + 1):
            # fill cells of matrix either True or False depending upon inclusion in subset sum 
            if nums[j - 1] > i:
                dp[i][j] = dp[i][j - 1]
            else:
                if dp[i - nums[j - 1]][j - 1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i][j - 1]
                # dp[i][j] = dp[i - nums[j - 1]][j - 1] or dp[i][j - 1]
        
    # value present at last row and column indicates whether array can be partitioned 
    return dp[subset_sum][n]

def can_partition_array(nums):
    # calculate array sum
    nums_sum = sum(nums)
    
    # if array sum odd, cannot be partitioned into equal sum subsets 
    if nums_sum % 2 != 0:
        return False
    
    # calculate subset sum 
    subset_sum = nums_sum // 2 
    
    # create array of appropriate size and initialize all cells w False 
    dp = [False] * (subset_sum + 1)
    
    # initialize first element as True (sum of 0 can always be achieved)
    dp[0] = True
        
    # traverse input array, element by element, fill lookup table in bottom-up manner 
    for num in nums:
        for i in range(subset_sum, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    return dp[subset_sum]

def counting_bits(n):
    # create empty array of length n + 1 that will be used to store results of subproblems 
    result = [0] * (n + 1)
    
    # if n 0, return empty list
    if n == 0:
        return result 
    
    # base cases: set first 2 elements of list 
    result[0] = 0
    result[1] = 1 
    
    # starting from 2 to n, calculate binary rep of each number 
    for i in range(2, n + 1):
        # count number of 1s in each binary rep and store them at their specified index in result array 
        # if i even, set ith elemnt of list to (i//2)th element
        if i % 2 == 0:
            result[i] = result[i // 2]
        # if i odd, set ith element of list to (i//2)th element + 1 
        else: 
            result[i] = result[i // 2] + 1 
    
    # once iteration complete, return result stored in array 
    return result

import math

def update_matrix(mat):
    # calculate number of rows and columns in matrix 
    m = len(mat)
    n = len(mat[0])
    
    # iterate through matrix and check for non-zero elements 
    for i in range(m):
        for j in range(n):
            if mat[i][j] > 0: # check if element greater than zero 
                
                # check element above, if none set to math.inf 
                above = mat[i - 1][j] if i > 0 else math.inf
                
                # check element left, if none set to math.inf 
                left = mat[i][j - 1] if j > 0 else math.inf
                
                # take min of above & left + 1 & store updated result to current cell 
                mat[i][j] = min(above, left) + 1
    
    # starting from bottom-right, iterate to top-left to look for shorter paths to nearest 0
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # while iterating backward, take min of below/right of current & add 1 - "candidate distance"
            if mat[i][j] > 0: # check if element greater than zero 
                
                # check element below - if none set to math.inf
                below = [i + 1][j] if i < m - 1 else math.inf
                
                # check element right - if none set to math.inf
                right = [i][j + 1] if j < n - 1 else math.inf
                
                # take min of below/right and add 1 
                min_distance = min(below, right) + 1
                
                # store min of current cell & candidate distance in current cell 
                # update current element w min of value and min distance
                mat[i][j] = min(mat[i][j], min_distance)  
    return mat

def house_robber(money):
    # check if input list empty or None 
    if len(money) == 0 or money == None:
        return 0
    
    # if input list has only 1 element, return that element
    if len(money) == 1:
        return money[0]
    
    # divide house into 2 sets - 1st does not include last house and 2nd does not include first 
    # return max value from calling helper function on input list minus last element
    # and input list minus first element 
    # compute max possible amount robbed from both sets and return greater of 2
    return max(robbing(money[:-1]), robbing(money[1:]))
    
def robbing(money):
    # create lookup array w same length as input list and initialize w 0s
    lookup_array = [0 for x in range(len(money) + 1)]
    lookup_array[0] = 0
    lookup_array[1] = money[0]
    
    # compute max possible robbery amount in each set, starting from leftmost house 
    # store max possible robbery amount against each house and use it in computations for next houses    
    # iterate through input list starting from 2nd element 
    for i in range(2, len(money) + 1):
        # update lookup array at each index with max value between 
        # current element in input list + previous element in lookup array 
        # and current element in lookup array 
        # at each house: max amount robbed = max(money in current house + 
        # max amount robbed up to house before last, max robbery up to last house)
        lookup_array[i] = max(money[i - 1] + lookup_array[i - 2], lookup_array[i - 1])
    # return max amount robbed after traversing all houses in set
    return lookup_array[len(money)]

def max_product(nums):
    # check if input list empty, return 0 if so 
    if len(nums) == 0:
        return 0
    # initialize 2 variables to store current max and min product
    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far
    # loop thru elements in list
    for i in range(1, len(nums)):
        current = nums[i]
        # update max and min product by taking max and min of current element, max prod so far and min prod so far 
        prev_max_so_far = max_so_far
        max_so_far = max(current, max_so_far * current, min_so_far * current)
        min_so_far = min(current, prev_max_so_far * current, min_so_far * current)

        # update result with max product so far 
        result = max(max_so_far, result)
        
    return result


def combination_sum(nums, target):
    # initialize array to store combos
    dp = [[] for _ in range(target + 1)]
    dp[0].append([])
    
    # for each value from 1 to target 
    for i in range(1, target + 1):
        # iterate over nums
        for j in range(len(nums)):
            if nums[j] <= i:
                # check previous results from dp 
                for previous in dp[i - nums[j]]:
                    temp = previous + [nums[j]]
                    temp.sort()
                    # if new combo not already in dp, store all newly calculated combos at dp[i]
                    if temp not in dp[i]:
                        dp[i].append(temp)

    # return dp[target], which contains all combos that sum up to target
    return dp[target]

def word_break(s, word_dict):
    n = len(s)
    # create set of words from list so that lookup cost in dictionary becomes O(1)
    word_set = set(word_dict)
    
    # initialize lookup table 
    dp = [False] * (n + 1)
    
    # set up first element in table to True as it reps an empty string 
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            # checking if substring from j to i is present in work dict and dp[j] True
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break # if substring found, no need to check further smaller substrings 
        
    # return last element of dp table 
    return dp[n]
    
    # find all possible prefixes of input string 
    # for each prefix, check if contained in dictionary 
    # if it is, repeat process w rest of string 
    # for remaining string, find all possible prefixes in dictionary 
    # continue process until whole string processed 
    # after processing whole string, return True if it could be broken into 
    # space separated dictionary words, otherwise return False 

def count_palindromic_substrings(s):
    # initialize count variable with 0 
    count = 0
    
    # initialize lookup table of dimensions len(s) * len(s)
    dp = [[False for i in range(len(s))] for i in range(len(s))]
    
    # base case 1: any string of length 1 is a palindrome, count number of characters in string and add to count
    for i in range(len(s)):
        dp[i][i] = True
        count += 1
        
    # base case 2: check all 2 letter substrings for palindromes, and update count as needed 
    for i in range(len(s) - 1):
        dp[i][i + 1] = (s[i] == s[i + 1])
        # boolean value added to count where True means 1 and False is 0
        count += dp[i][i + 1]

    # using results of previous steps, increment count of any string of length greater than 2 
    # if its first and last characters match and rest of string is also palindrome 
    for length in range(3, len(s) + 1):
        i = 0
        # checking every possible substring of any specific length 
        for j in range(length - 1, len(s)):
            dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
            count += dp[i][j]
            i += 1
    
    # return value of count, which represents number of palindromic substrings in given string 
    return count

def naive_lcs(str1, str2):
    return naive_lcs_recursive(str1, str2, 0, 0)
    
def naive_lcs_recursive(string1, string2, i, j):
    if i == len(string1) or j == len(string2):
        return 0
    
    if string1[i] == string2[j]:
        return 1 + naive_lcs_recursive(string1, string2, i + 1, j + 1)
    
    return max(naive_lcs_recursive(string1, string2, i + 1, j),\
        naive_lcs_recursive(string1, string2, i, j + 1))

def longest_common_subsequence(str1, str2):
    n = len(str1)
    m = len(str2)
    
    # create table to store computed results 
    dp = [[-1 for x in range(m)] for y in range(n)]
    
    return finding_lcs(str1, str2, 0, 0, dp)

# start iterating characters of both strings and compare them     
def finding_lcs(string1, string2, i, j, dp):
    # sequence when at least 1 string of length zero is zero 
    if i == len(string1) or j == len(string2):
        return 0    
    
    elif dp[i][j] == -1:
        # if characters equal, continue checking for next characters and store result 
        if string1[i] == string2[j]:
            dp[i][j] = 1 + finding_lcs(string1, string2, i + 1, j + 1, dp)
        # if not equal, compute result by increment both pointers individually and store max
        else:
            dp[i][j] = max(finding_lcs(string1, string2, i + 1, j, dp), finding_lcs(string1, string2, i, j + 1, dp))
     
    # return value stored in table  
    return dp[i][j]   

def word_break(s, word_dict):
    # create 2D table where each entry corresponds to prefix of input string and store array 
    # of all possible sentences that can be formed using that substring 
    dp = [[]] * (len(s) + 1)
    
    # base case 
    dp[0] = [""]
    
    # iterate over all prefixes of input string
    
    # for each substring in input string, repeat process 
    for i in range(1, len(s) + 1): 
        prefix = s[:i]
        temp = [] # temp array to store valid sentences formed from current prefix being checked 
        
        # for each prefix, iterate over its suffixes and check whether suffix valid word in dict
        # iterate over current prefix and break down into all possible suffixes
        for j in range(0, i):
            suffix = prefix[j:]
            
            # check if current suffix in word_dict - if so, it's a valid word that can be used in solution 
            if suffix in word_dict:
                
                # retrieve valid sentences from previously computed subproblem 
                for substring in dp[j]:
                    
                    # merge suffix with already calculated results 
                    temp.append((substring + " " + suffix).strip())
        
        dp[i] = temp
    # returning all sentences formed from complete string s
    return dp[len(s)]
     
    # if suffix valid word, combine w all possible sentences that can be formed 
    # using prefix to left of it 
    # store array of all possible sentences that can be formed using current prefix 
    # in corresponding entry of table 
    # after processing all prefixes of input string, return list of all possible sentences
    # that can be formed using complete string        
    
def num_of_decodings(decode_str):
    string_length = len(decode_str)
    
    # create array of length n + 1 to store number of ways to decode string and initialize with 0s 
    dp = [0] * (string_length + 1)
    
    # there is only one way to decode empty string 
    dp[0] = 1
    
    # for string of length 0, we'll compute that there's no way to decode string and add result in array
    # first element 1 if first character not 0, otherwise it is 0
    if decode_str[0] != '0':
        dp[1] = 1
 
    # iterate over string and at each increment, check whether digit is valid 1 digit number
    # if it is, add to dp[i - 1] to current index of array        
    # iterate through input string starting with 2nd character 
    for i in range(2, string_length + 1):
        # if current character not 0, add number of ways to decode string without current
        if decode_str[i] != '0':
            dp[i] += dp[i - 1]
            
        # if substring of current and previous characters valid 2 digit number
        # add number of ways to decode substring without current and previous 
        if decode_str[i - 2] == '1' or (decode_str[i - 2] == '2' and decode_str[i - 1] <= '6'):
            dp[i] += dp[i - 2]
    
    # once all iterations complete, return value stored at last index of array 
    return dp[string_length]

MOD = 1000000007

def count_good_subsequences(s):
    n = len(s) + 1
    factorials = [1] * n
    inverses = [1] * n
    
    # iterate through input string and find frequencies of all string characters 
    # calculating factorial and inverse of all numbers from 1 to n
    # instead of calculating factorial and inverse over and over again 
    # store factorial of i and use to calculate factorial number i + 1
    # factorial of number i + 1 is factorial of i-1 * i 
    for i in range(1, n):
        factorials[i] = factorials[i - 1] * i % MOD
        inverses[i] = quick_modular_inverse(factorials[i], MOD - 2, MOD)
        
    # initializing array of size 26 to hold frequencies of characters A - Z
    frequency_count = [0] * 26
    
    # initializing variable to keep record of max frequency 
    max_count = 1
    
    # calculating frequency of each character and keeping record of max freq
    for char in s: 
        # find max frequency from all character #frequencies 
        max_count = max(max_count, frequency_count[ord(char) - ord('a')] + 1)
        frequency_count[ord(char) - ord('a')] += 1 
        
    # initializing variable to store count of good subsequences 
    final_count = 0
    
    # nested loop to calc combo from 1 to max freq
    for i in range(1, max_count + 1): # start loop from 1 to max frequency
        count = 1 # in each iteration of loop, count possible combos of good subseq and add up number of combos in counter
        
        for j in range(26):
            # counting only if count of character freq greater or equal to 1
            if frequency_count[j] >= 1:
                count = count * (combination(frequency_count[j], i, factorials, inverses) + 1) % MOD
        
        # adding count to final count after subtracting 1 and taking mod 
        final_count = (final_count + count - 1) % MOD
    
    # return final count after casting to int 
    return int(final_count)
    
def quick_modular_inverse(base, exponent, modulus): # method to find modular inverse of number
    # initialize result to 1 (identity element for multiplication modulo modulus)
    result = 1
    
    while exponent != 0:
        # if exponent odd, multiply result by base and take modulo modulus 
        if (exponent & 1) == 1:
            result = result * base % modulus
        
        # right shift exponent by 1 (equivalent to dividing exponent by 2)
        exponent >>= 1
        
        # square base and take modulo modulus to reduce base in terms of modulus 
        base = base * base % modulus
    
    # after traversing string, return final count 
    return result
   
# calculating combo (n choose k)
def combination(n, k, factorials, inverses):  
    return (factorials[n] * inverses[k] % MOD) * inverses[n - k] % MOD
    
def climb_stairs(nums):
    # if there are 0 or 1 steps, only 1 way to climb stairs 
    if nums == 0 or nums == 1:
        return 1 
    
    # initialize lookup table and fill in indexes for base cases of 1 and 2 jumps
    dp = [0] * (nums)
    dp[0] = 1 # 1 way to say at ground (0th step)
    dp[1] = 1 # 1 way to climb 1 step
    
    # iterate over lookup table and add 2 previous values from lookup table to fill next index
    for i in range(2, nums + 1):
        dp[i] = dp[i - 1] + dp[i - 2] # repeat process until lookup table filled 
    
    # return index value at nums from lookup table, which is number of ways to climb stairs 
    return dp[nums]
