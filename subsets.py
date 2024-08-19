def find_all_subsets(nums):
    subsets = []
    if not nums:
        return [[]]
    else:
        # compute number of possible subsets of given set using 2^n where n is number of elements 
        possible_subsets = 2 ** (len(nums))
        # start loop from 0 to count of subsets and add empty list to results list in first iteration 
        for i in range(0, possible_subsets):
            subset = set()
            for j in range(0, len(nums)):
                # in each iteration, create bit mask of length n for each element in input set
                # if ith bit is set, set[i] will be present in current subset
                if get_bit(i, j) == 1 and nums[j] not in subset:
                    subset.add(nums[j])
            
            if i == 0:
                subsets.append([])
            else:
                subsets.append(list(subset))
    # after iterating, append current subset to list of subsets 
    return subsets

def get_bit(num, bit):
    temp = (1 << bit) # shift number by bit positions 
    temp = temp & num # bitwise and num 
    if temp == 0: 
        return 0
    return 1 

def permute_word(word):
    result = []
    result = permute_string_rec(word, 0, result)
    # return list of all perms 
    return result

def permute_string_rec(word, current_index, result):
    # starting from 1st index as current, recursively compute perms of input string 
    if current_index == len(word) - 1: # if we reach end of string, store current string as perm 
        result.append(word)
        return # prevents adding duplicate permutations 
    for i in range(current_index, len(word)):
        # compute perms by swapping current index w every index in remaining string 
        swapped_string = swap_char(word, current_index, i) # swaps character for each permutation 
        # recurse comp step by incrementing current index by 1 
        permute_string_rec(swapped_string, current_index + 1, result) # recursively calls itself to find each permutation

# swaps characters for every permutation 
def swap_char(word, i, j): 
    swap_index = list(word)
    swap_index[i], swap_index[j] = swap_index[j], swap_index[i] # swap i and j indexes of string 
    return ''.join(swap_index)

def letter_combinations(digits):
    # initialize empty list to store all combos 
    combos = []
    # if input string of digits empty, return empty list b/c no possible combos
    if len(digits) == 0:
        return [] 
    # initialize dictionary that maps digits to their corresponding characters 
    digit_map = {
        "1": [""],
        "2": ["a", "b", "c"], 
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"], 
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]}
    
    backtrack(0, [], digits, digit_map, combos)
    return combos

def backtrack(index, path, digits, letters, combos):
    # check if length of our current combo is same as length as input length, 
    # add it to list of results and backtrack
    if len(path) == len(digits):
        combos.append(''.join(path))
        return
    # otherwise, retrieve list of possible letters corresponding to digit at current index 
    # and iterate through each letter to generate combos recursively
    possible_letters = letters[digits[index]] 
    if possible_letters:
        for letter in possible_letters:
            path.append(letter) # add current letter to path 
            backtrack(index + 1, path, digits, letters, combos) # recursively explore next digit
            path.pop() # remove current letter from path before backtracking to explore other combos 
    

def generate_combinations(n):
    result = []
    # create output list to store all valid combos of parentheses
    output = []
    # call backtrack fxn w/ initial parameters set to n, empty string and 0 for
    # count of both opening and closing parentheses 
    back_track(n, 0, 0, output, result)
    return result

def back_track(n, left_count, right_count, output, result):
    # if opening/closing parentheses count == n, valid parentheses combo/ append string to list
    if left_count >= n and right_count >= n:
        result.append("".join(output))
    # otherwise check number of opening parentheses is less than n
    # if yes, add opening parentheses to string and increment count
    if left_count < n: # case where we can still append left braces 
        output.append('(')
        back_track(n, left_count + 1, right_count, output, result) 
        output.pop()
    # check count of closing parentheses, if less than opening
    # add closing to string and increment count  
    if right_count < left_count:
        output.append(')')
        back_track(n, left_count, right_count + 1, output, result)
        output.pop()

def get_k_sum_subsets(set_of_integers, target_sum):
    subsets = []
    find_subsets(set_of_integers, target_sum, [], 0, subsets)
    # return result list 
    return subsets

# find all possible subsets of set 
def find_subsets(numbers, target, path, index, result):
    # find sum of elements of each subset 
    # if sum for any subset equals k, add subset to result list 
    if target == 0: 
        result.append(path)
        return 
    if target < 0:
        return
    for i in range(index, len(numbers)):
        find_subsets(numbers, target - numbers[i], path + [numbers[i]], i + 1, result)
    return result

def print_result(result):
    for rs in result:
        print("\t\t ", rs)    

