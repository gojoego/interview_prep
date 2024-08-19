def find_longest_substring(input_str):
    
    if len(input_str) == 0: # check for empty string
        return 0 
    
    window_start = 0 # current window start 
    longest = 0 # length of longest substring 
    last_seen_at = {} # initialize empty hashmap storing index of last occurrence of each character 
    
    # traverse string to find longest substring w/ out repeating chars 
    for index, value in enumerate(input_str):
        
        # check if current character already seen in current window 
        if value in last_seen_at and last_seen_at[value] >= window_start:
            # if yes, update start of window to index after last occurrence
            window_start = last_seen_at[value] + 1
            
        # update index of last occurrence of character
        last_seen_at[value] = index
        
        # update length of longest substring 
        longest = max(longest, index - window_start + 1)
            
    return longest

def min_sub_array_len(target, nums):
    window_size = float('inf') # store size of min subarray 
    start = 0
    current_sum = 0
    for end in range(len(nums)): # slide window over input array using start and end 
        current_sum += nums[end] # increment end and add new element of window into sum 
        while current_sum >= target: # if sum greater than or equal to target 
            current_subarray_size = (end + 1) - start # calculate current subarray size 
            window_size = min(window_size, current_subarray_size) # compare current subarray size with window size and store smaller of two 
            current_sum -= nums[start] # remove element from start of window 
            start += 1 # increment start 
    if window_size != float('inf'): # if window size +inf -> no subarray w sum equal/greater than target 
        return window_size
    
    return 0 # return 0 to indicate no subarray had equal or greater sum than target 
    
def max_profit(prices):
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

def main():
    target = [7, 4, 11, 10, 5, 15]
    input_arr = [[2, 3, 1, 2, 4, 3], [1, 4, 4], [1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 2, 3, 4], [1, 2, 1, 3], [5, 4, 9, 8, 11, 3, 7, 12, 15, 44]]
    for i in range(len(input_arr)):
        window_size = min_sub_array_len(target[i], input_arr[i])
        print(i+1, ".\t Input array: ", input_arr[i],"\n\t Target: ", target[i],
            "\n\t Minimum Length of Subarray: ", window_size, sep="")
        print("-"*100)


if __name__ == "__main__":
    main()