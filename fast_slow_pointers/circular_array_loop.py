# time O(n^2), space O(1)
def circular_array_loop(nums):
    size = len(nums)
    # iterate through each index
    for i in range(size):
        # set both pointers equal to i 
        slow = fast = i
        # sets direction of loop, True if positive, False if negative 
        forward = nums[i] > 0
        while True:
            slow = next_step(slow, nums[slow], size)
            if is_not_cycle(nums, forward, slow):
                break
            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break
            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break
            
            if slow == fast:
                return True
    return False
            
    
# helper function to calculate next step
def next_step(pointer, value, size):
    # add current index and value at index and taking modulus with array size 
    result = (pointer + value) % size
    # for negative values, sized added to make it a valid index value 
    if result < 0:
        result += size
    return result

# helper function to detect a cycle doesn't exist 
def is_not_cycle(nums, prev_direction, pointer):
    # determines current direction based on sign of value at current index
    curr_direction = nums[pointer] >= 0
    # both pointers have different directions or absolute value of index value is equal to length indicating 1 element 
    if (prev_direction != curr_direction) or (abs(nums[pointer] % len(nums)) == 0):
        return True # cycle not possible
    else: 
        return False # cycle possible 

def main():

    input = (
            [-2, -3, -9],
            [-5, -4, -3, -2, -1],
            [-1, -2, -3, -4, -5],
            [2, 1, -1, -2],
            [-1, -2, -3, -4, -5, 6],
            [1, 2, -3, 3, 4, 7, 1],
            [2, 2, 2, 7, 2, -1, 2, -1, -1]
            )
    num = 1

    for i in input:
        print(f"{num}.\tCircular array = {i}")
        print(f"\n\tFound loop = {circular_array_loop(i)}")
        print("-"*100, "\n")
        num += 1


if __name__ == "__main__":
    main()