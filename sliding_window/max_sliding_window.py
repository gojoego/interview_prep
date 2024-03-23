from collections import deque
# time O(n * w), space O(w)
def find_max_sliding_current_window_naive(nums, w):
    if len(nums) <= w:
        return max(nums)
    output = []
    current_window = deque()
    for i in range(len(nums) - w):
        if i == 0:
            for j in range(w):
                current_window.append(nums[j])
            output.append(max(current_window))
        current_window.popleft()
        current_window.append(nums[i + w])
        output.append(max(current_window))
    return output

# time O(n), space O(w)
def find_max_sliding_window(nums, w):
    if len(nums) == 0:
        return []
    output = []
    current_window = []
    # if current_window size greater than array size, set current_window size to array size 
    if w > len(nums):
        w = len(nums)
    print("\n\tFinding the maximum in the first current_window:")
    # process elements of first current_window, from 0 to w  
    for i in range(w):
        print(f"\tAdding nums[{i}] = {nums[i]} to the first current_window:\n\t\tInitial state of current_current_window: {current_window}")
        clean_up(i, current_window, nums)
        current_window.append(i) # adding indexes instead of values to check which index has fallen out of current current_window and remove it 
        print(f"\t\tFinal state of current_current_window: {current_window}")
    
    # appending max element of current current_window to output list 
    output.append(nums[current_window[0]])
    
    print("\n\tFinding the maximum in the remaining current_windows:")
    
    # iterate over remaining input list 
    for i in range(w, len(nums)):
        print(f"\tAdding nums[{i}] = {nums[i]} to current_current_window:\n\t\tInitial state of current_current_window: {current_window}")
        # for every element, remove previous smaller elements from current current_window 
        clean_up(i, current_window, nums)   
        # remove first index from current current_window if it has fallen out of current current_window 
        if current_window and current_window[0] <= (i - w):
            print(f"\t\tIndex {current_window[0]} has fallen out of the current current_window,")
            print(f"\t\tso, remove it")
            del current_window[0]
        print(f"\t\tAppending {i} to current_window")
        current_window.append(i)
        output.append(nums[current_window[0]])
        print(f"\t\tFinal state of current_window: {current_window}")
    return output
 
def clean_up(i, current_current_window, nums):
    # remove all indexes from current current_window whose corresponding values are smaller than or equal to current element 
    while current_current_window and nums[i] >= nums[current_current_window[-1]]:
        print(f"\t\tAs nums[{i}] = {nums[i]} is greater than or equal to nums[{current_current_window[-1]}] = {nums[current_current_window[-1]]},")
        print(f"\t\tremove {current_current_window[-1]} from current_current_window")
        del current_current_window[-1]
        
def main():
    window_sizes = [3, 3, 3, 3, 2, 4, 3, 2, 3, 18]
    nums_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        [1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30],
        [10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67],
        [4, 5, 6, 1, 2, 3],
        [9, 5, 3, 1, 6, 3],
        [2, 4, 6, 8, 10, 12, 14, 16],
        [-1, -1, -2, -4, -6, -7],
        [4, 4, 4, 4, 4, 4]
    ]

    for i in range(len(nums_list)):
        print(f"{i + 1}.\tInput array:\t{nums_list[i]}")
        print(f"\tWindow size:\t{window_sizes[i]}")
        output = find_max_sliding_window(nums_list[i], window_sizes[i])
        print(f"\n\tMaximum in each sliding window:\t{output}")
        print("-"*100)

if __name__ == '__main__':
    main()