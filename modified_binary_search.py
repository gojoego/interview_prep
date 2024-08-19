def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    
    while low <= high:
        mid = low + ((high - low) // 2)
        if nums[mid] == target:
            return mid 
        elif target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]: 
            low = mid + 1
    return -1

def binary_search_recursive(nums, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high) // 2 # calculate midpoint
    
    if nums[mid] == target: # target value present at middle of array 
        return mid

    # if target greater than middle, ignore first half 
    elif nums[mid] < target:
        return binary_search_recursive(nums, mid + 1, high, target)
    
    # if target less than middle, ignore second half 
    return binary_search_recursive(nums, low, mid - 1, target)

def binary_search_rotated_iterative(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[low] <= nums[mid]: # low to mid sorted 
            if nums[low] <= target and target < nums[mid]:
                high = mid - 1 # target within sorted first half of array 
            else:
                low = mid + 1 # target not in first sorted half, examine unsorted second half 
        else: # mid to high sorted 
            if nums[mid] < target and target <= nums[high]:
                low = mid + 1 # target in sorted second half of array 
            else:
                high = mid - 1 # target not within sorted second half, examine first unsorted half     
    return -1

def binary_search_recursive(nums, low, high, target):
    if low > high:
        return -1 
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid 
    
    if nums[low] <= nums[mid]: # low to mid sorted 
        if nums[low] <= target and target < nums[mid]: # target in sorted first half 
            return binary_search_recursive(nums, low, mid - 1, target)
        return binary_search_recursive(nums, mid + 1, high, target) # target in unsorted 2nd half 
    else: # mid to high sorted 
        if nums[mid] < target and target <= nums[high]: # target in sorted 2nd half 
            return binary_search_recursive(nums, mid + 1, high, target)
        return binary_search_recursive(nums, low, mid - 1, target) # target in unsorted 1st half 

# time O(logn), space iterative O(1), space recursive O(logn)
def binary_search_rotated(nums, target):
    return binary_search_recursive(nums, 0, len(nums) - 1, target)

def is_bad_version(s):
    return s

def first_bad_version(n):
    first = 1 # initialized to first version 
    last = n # last pointer initialized to number of versions 
    calls = 0
    while first <= last: # binary search 
        mid = first + (last - first) // 2
        if is_bad_version(mid):
            last = mid - 1 # if mid bad -> first bad in left subarray 
        else:
            first = mid + 1 # not bad -> first bad in right subarray 
        calls += 1
    return [first, calls]

import random

class RandomPickWithWeight:
    def __init__(self, weights):
        self.running_sums = [] # list to store running sums of weights
        running_sum = 0 # variable to calculate running sum 
        
        for w in weights: # iterate through given weights
            running_sum += w # add current weight to running sum 
            self.running_sums.append(running_sum) # append running sum to running sums list 
            
        self.total_sum = running_sum # store total sum of weights

    def pick_index(self):
        target = random.randint(1, self.total_sum) # generate random # between 1 and total sum of array 
        low = 0 
        high = len(self.running_sums)
        
        # binary search to find first value higher than target 
        while low < high:
            mid = low + (high - low) // 2
            if target > self.running_sums[mid]:
                low = mid + 1
            else: 
                high = mid
        return low 
    
    # def find_closest_elements_naive(nums, k, target):
        
    
    def find_closest_elements(nums, k, target):
        # base case if nums == k
        if len(nums) == k:
            return nums
        if target <= nums[0]:
            return nums[0:k]
        if target >= nums[-1]:
            return nums[len(nums) - k: len(nums)]
        first_closest = binary_search(nums, target)
        
        window_left = first_closest - 1
        window_right = first_closest + 1
        
        while (window_right - window_left - 1) < k:
            if window_left == -1:
                window_right += 1
                continue
            if window_right == len(nums) or abs(nums[window_left] - target) <= abs(nums[window_right] - target):
                window_left -= 1
            else:
                window_right += 1
        return nums[window_left + 1: window_right]
    
    # space O(1), time O(logn)
    def single_non_duplicate(nums): 
        l = 0 # initialize left pointer 
        r = len(nums) - 1 # initialize right pointer
        
        while l != r: 
            mid = l + (r - l) // 2 # set value of mid to avoid integer overflow 
            if mid % 2 == 1: 
                mid -= 1 # decrement mid if odd 
            if nums[mid] == nums[mid + 1]:
                l = mid + 2 # if mid and mid + 1 equal, search right half 
            else: 
                r = mid # else search left half 
        return nums[l]
    
    def search(arr, t):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == t:
                return True
            if arr[low] == arr[mid]:
                low += 1
                continue
            if arr[low] <= arr[mid]: # low to mid sorted 
                if arr[low] <= t < arr[mid]:
                    high = mid - 1 # target within sorted first half of array 
                else:
                    low = mid + 1 # target not in first sorted half, examine unsorted second half 
            else: # mid to high sorted 
                if arr[mid] < t <= arr[high]:
                    low = mid + 1 # target in sorted second half of array 
                else:
                    high = mid - 1 # target not within sorted second half, examine first unsorted half     
        return False     
