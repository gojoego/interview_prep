# time O(n), space O(1)
def find_duplicate(nums):
    fast = slow = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return fast

def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    
    # Move slow pointer one step at a time and fast pointer two steps at a time
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Reset slow pointer to the start of the array
    slow = nums[0]
    
    # Move slow and fast pointers one step at a time until they meet
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow